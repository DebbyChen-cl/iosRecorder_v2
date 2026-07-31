# ─────────────────────────────────────────────
# auto_healing.py  –  Auto-Healing integration
# ─────────────────────────────────────────────
# Ported from rdqe-ios-autotest-phdm/SFT/conftest.py.
#
# Responsibilities (Phase 1, executed inside this pytest run):
#   C1  pytest_runtest_protocol  – immediate retry for crash/network failures
#   C2  heuristic classification – decide retry / defer, no AI involved
#   C3  state.json               – per-run machine-readable result ledger
#   C4  test registry            – stable case ids for every collected test
#       failure evidence         – screenshot + hierarchy + metadata per failure
#       Phase 2 trigger          – hand deferred cases to the healing agent
#
# conftest.py owns the pytest hooks/fixtures and delegates into this module,
# so every entry point here is safe to call and never raises into the run.
#
# Environment switches
#   AUTO_HEALING=0                  disable everything (evidence, state, retry)
#   AUTO_HEALING_PHASE2=0           keep Phase 1 only; never launch the agent
#   AUTO_HEALING_PROJECT_PATH=...   location of iOS_auto_healing_agent
#   AUTO_HEALING_REGISTRY_PATH=...  override the test registry file
#   AUTO_HEALING_REPLAY=1           set by the agent's replay.py (internal run)
#   AUTO_HEALING_CONTEXT=...        root-cause/patch summary for a replay run
#   AUTO_HEALING_NOT_HEALED_REASON  skip all tests, reporting this reason
#   AUTO_HEALING_APP_VERSION=...    app version recorded into state.json

import json
import logging
import os
import re
import shutil
import subprocess
import time

import pytest

import config

logger = logging.getLogger(__name__)


# ─── Paths & Switches ────────────────────────────────────────────────────────

# pytest is launched from this directory (pytest.ini lives here), so nodeids
# and evidence paths recorded in state.json are relative to it — that is what
# the healing agent passes back as TEST_PROJECT when it replays a case.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(PROJECT_ROOT)

HEALING_PROJECT_PATH = os.environ.get(
    'AUTO_HEALING_PROJECT_PATH',
    os.path.join(os.path.dirname(_REPO_ROOT), 'iOS_auto_healing_agent'),
)
HEALING_SKILL_PATH = os.path.join(
    HEALING_PROJECT_PATH, 'auto_healing_skills', 'auto-healing-phase1-decision'
)
# Own registry file: the shared test_registry.json belongs to the phdm project
# and keying both suites into it would mix two unrelated case-id namespaces.
REGISTRY_PATH = os.environ.get(
    'AUTO_HEALING_REGISTRY_PATH',
    os.path.join(HEALING_PROJECT_PATH, 'registry', 'test_registry_ios_recorder.json'),
)
CASE_ID_PREFIX = os.environ.get('AUTO_HEALING_CASE_ID_PREFIX', 'IOSREC-AUTO')
EVIDENCE_ROOT = os.path.join(PROJECT_ROOT, 'Self-healing', 'evidence')


def _flag(name, default='1'):
    return os.environ.get(name, default).strip().lower() not in ('0', 'false', 'no', 'off')


ENABLED = _flag('AUTO_HEALING')
PHASE2_ENABLED = _flag('AUTO_HEALING_PHASE2')
IS_REPLAY = os.environ.get('AUTO_HEALING_REPLAY') == '1'
PHASE2_TIMEOUT_SEC = int(os.environ.get('AUTO_HEALING_PHASE2_TIMEOUT', '660'))

_retry_budget = {
    'used': 0,
    'max_cases': int(os.environ.get('AUTO_HEALING_MAX_RETRY_CASES', '3')),
    'max_time_increase_pct': 15,
}

_RUN_ID = None

# Set by the conftest `driver` fixture so failure evidence can be pulled from
# the live session — this project has no session-scoped driver singleton.
_active_driver = None


def set_active_driver(driver):
    """Publish the current test's Appium driver for evidence collection."""
    global _active_driver
    _active_driver = driver


# ─── Small Helpers ───────────────────────────────────────────────────────────

def _project_root():
    return PROJECT_ROOT


def _safe_artifact_name(value):
    value = str(value or 'unknown').strip()
    value = value.replace(os.sep, '-')
    value = re.sub(r'[^A-Za-z0-9_.-]+', '-', value)
    return value.strip('-') or 'unknown'


def _json_safe(value):
    try:
        json.dumps(value)
        return value
    except TypeError:
        if isinstance(value, dict):
            return {str(k): _json_safe(v) for k, v in value.items()}
        if isinstance(value, (list, tuple, set)):
            return [_json_safe(v) for v in value]
        return str(value)


def _git_value(args):
    try:
        return subprocess.check_output(
            ['git'] + args,
            cwd=PROJECT_ROOT,
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        return None


def _run_id(pytest_config):
    global _RUN_ID
    if _RUN_ID is None:
        env_run_id = (
            os.environ.get('RP_LAUNCH_UUID')
            or os.environ.get('BUILD_TAG')
            or os.environ.get('BUILD_NUMBER')
        )
        if env_run_id:
            _RUN_ID = env_run_id
        else:
            start_time = getattr(pytest_config, '_start_time', time.time())
            _RUN_ID = time.strftime('%Y%m%d%H%M%S', time.localtime(start_time))
    return _RUN_ID


def _write_text(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content or '')


def _bundle_id():
    return getattr(config, 'TARGET_BUNDLE_ID', '') or config.IOS_CAPABILITIES.get('appium:bundleId', '')


def _device_context():
    """This project has no run_config.yaml — device facts come from config.py."""
    caps = getattr(config, 'IOS_CAPABILITIES', {}) or {}
    return {
        'name': caps.get('appium:deviceName'),
        'udid': caps.get('appium:udid'),
        'platformName': caps.get('platformName'),
        'platformVersion': caps.get('appium:platformVersion'),
        'bundleId': caps.get('appium:bundleId'),
        'appiumServerUrl': getattr(config, 'APPIUM_SERVER_URL', None),
    }


def _build_context():
    return {'version': os.environ.get('AUTO_HEALING_APP_VERSION')}


def _driver_capabilities(appium_driver):
    try:
        return _json_safe(getattr(appium_driver, 'capabilities', {}) or {})
    except Exception:
        return {}


def _screenshot_is_black(path):
    """True when the fail-moment screenshot is (near) fully black — a strong
    signal the app died and only a blank surface was captured."""
    try:
        from PIL import Image

        with Image.open(path) as im:
            sample = im.convert('L').resize((32, 32))
        return max(sample.getdata()) <= 12
    except Exception:
        return None


def _collect_app_state(appium_driver):
    state = {}
    for name, getter in [
        ('current_context', lambda: appium_driver.current_context),
        ('orientation', lambda: appium_driver.orientation),
        ('window_size', lambda: appium_driver.get_window_size()),
        ('app_state', lambda: appium_driver.query_app_state(_bundle_id())),
    ]:
        try:
            state[name] = getter()
        except Exception as e:
            state[name] = {'collection_error': str(e)}
    return _json_safe(state)


# ─── State.json Management (C3) ──────────────────────────────────────────────

def _state_json_path(pytest_config):
    return os.path.join(HEALING_PROJECT_PATH, 'runs', _run_id(pytest_config), 'state.json')


def _init_state_json(pytest_config):
    state_path = _state_json_path(pytest_config)
    os.makedirs(os.path.dirname(state_path), exist_ok=True)

    device_config = _device_context()
    build_config = _build_context()

    state = {
        'run_id': _run_id(pytest_config),
        'branch': _git_value(['rev-parse', '--abbrev-ref', 'HEAD']),
        'commit': _git_value(['rev-parse', 'HEAD']),
        'app_version': build_config.get('version'),
        'device': device_config.get('name'),
        'ios_version': device_config.get('platformVersion'),
        'started_at': time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(pytest_config._start_time)),
        'ended_at': None,
        'phase': 'phase_1',
        'immediate_retry_budget': {
            'max_cases': _retry_budget['max_cases'],
            'used': 0,
            'max_time_increase_pct': _retry_budget['max_time_increase_pct'],
        },
        'cases': {},
        'summary': {
            'total': 0, 'pass': 0, 'fail': 0,
            'pass_with_healing': 0, 'pass_after_retry': 0,
            'deferred': 0, 'manual_review': 0, 'product_bug': 0,
            'healing_attempted': 0, 'healing_succeeded': 0,
        },
    }

    with open(state_path, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    logger.info('[Auto-Healing] state.json initialized at %s', state_path)


def _read_state_json(pytest_config):
    state_path = _state_json_path(pytest_config)
    if not os.path.exists(state_path):
        return None
    with open(state_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def _write_state_json(pytest_config, state):
    state_path = _state_json_path(pytest_config)
    with open(state_path, 'w', encoding='utf-8') as f:
        json.dump(_json_safe(state), f, indent=2, ensure_ascii=False)


def _update_case_in_state(pytest_config, case_id, case_data):
    state = _read_state_json(pytest_config)
    if state is None:
        return
    if case_id not in state['cases']:
        state['cases'][case_id] = {}
    state['cases'][case_id].update(case_data)
    _write_state_json(pytest_config, state)


def _finalize_state_json(pytest_config):
    state = _read_state_json(pytest_config)
    if state is None:
        return
    state['ended_at'] = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime())
    state['immediate_retry_budget']['used'] = _retry_budget['used']

    counts = {'pass': 0, 'fail': 0, 'pass_after_retry': 0, 'deferred': 0, 'manual_review': 0}
    for c in state['cases'].values():
        status = c.get('original_status', 'unknown')
        retry = c.get('retry')
        scheduling = c.get('scheduling')
        if retry and retry.get('result') == 'pass':
            counts['pass_after_retry'] += 1
        elif status == 'pass':
            counts['pass'] += 1
        elif scheduling and scheduling.get('action') == 'deferred':
            counts['deferred'] += 1
        elif scheduling and scheduling.get('action') == 'manual_review':
            counts['manual_review'] += 1
        else:
            counts['fail'] += 1

    state['summary'].update(counts)
    state['summary']['total'] = len(state['cases'])
    _write_state_json(pytest_config, state)
    logger.info('[Auto-Healing] state.json finalized: %s', counts)


# ─── Heuristic Failure Classification (C2) ───────────────────────────────────

def _classify_failure_heuristic(evidence_path, remaining_budget):
    """Instant heuristic classification — no AI, no blocking.
    App crash → retry immediately. Everything else → defer to Phase 2."""
    metadata = {}
    if evidence_path:
        try:
            with open(os.path.join(evidence_path, 'metadata.json'), 'r', encoding='utf-8') as f:
                metadata = json.load(f)
        except Exception:
            pass

    app_state = metadata.get('app_state', {})
    stack = ''
    try:
        with open(os.path.join(evidence_path, 'stack_trace.txt'), 'r', encoding='utf-8') as f:
            stack = f.read().lower()
    except Exception:
        pass

    app_state_val = app_state.get('app_state')
    app_not_running = (
        not app_state                                                        # driver unavailable (empty dict)
        or app_state_val in (1, '1')                                         # Appium confirms app not running
        or (isinstance(app_state_val, dict) and 'collection_error' in app_state_val)  # query_app_state threw
    )
    if app_not_running or app_state.get('screenshot_is_black'):
        if remaining_budget > 0:
            return {'lane': 'A', 'action': 'retry', 'preliminary_category': 'app_crash',
                    'reason': 'App not running or black screen — immediate retry'}
        return {'lane': 'C', 'action': 'deferred', 'preliminary_category': 'app_crash',
                'reason': 'App crash but retry budget exhausted'}

    network_keywords = ['connectionerror', 'timeouterror', 'urlopen', 'network', 'server error', 'status code 5']
    if any(kw in stack for kw in network_keywords):
        if remaining_budget > 0:
            return {'lane': 'A', 'action': 'retry', 'preliminary_category': 'network_issue',
                    'reason': 'Network/server error in stack trace — immediate retry'}
        return {'lane': 'C', 'action': 'deferred', 'preliminary_category': 'network_issue',
                'reason': 'Network issue but retry budget exhausted'}

    return {'lane': 'C', 'action': 'deferred', 'preliminary_category': 'unknown',
            'reason': 'Deferred to Phase 2 for AI root cause analysis'}


# ─── Test Registry Bootstrap (C4) ────────────────────────────────────────────

def _load_registry():
    if os.path.exists(REGISTRY_PATH):
        try:
            with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.warning('[Auto-Healing] registry unreadable (%s); starting fresh', e)
    return {}


def _next_registry_counter(registry):
    highest = 0
    for cid in registry:
        match = re.fullmatch(rf'{re.escape(CASE_ID_PREFIX)}-(\d+)', cid)
        if match:
            highest = max(highest, int(match.group(1)))
    return highest + 1


def _bootstrap_test_registry(items):
    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)
    registry = _load_registry()

    # Key existing auto-generated entries by nodeid so a rerun reuses the same
    # stable id instead of minting a new one on every session.
    by_nodeid = {
        entry.get('test_nodeid'): cid
        for cid, entry in registry.items()
        if entry.get('test_nodeid')
    }
    counter = _next_registry_counter(registry)

    for item in items:
        case_id_marker = item.get_closest_marker('case_id')
        if case_id_marker and case_id_marker.args:
            stable_id = str(case_id_marker.args[0])
        elif item.nodeid in by_nodeid:
            stable_id = by_nodeid[item.nodeid]
        else:
            stable_id = f'{CASE_ID_PREFIX}-{counter:04d}'
            counter += 1

        if stable_id in registry:
            registry[stable_id]['test_nodeid'] = item.nodeid
            by_nodeid[item.nodeid] = stable_id
            continue

        test_name = getattr(item, 'originalname', item.name)
        test_file = os.path.relpath(str(item.fspath), PROJECT_ROOT) if item.fspath else None
        cls_name = item.cls.__name__ if item.cls else None
        feature_guess = None
        if cls_name and cls_name.startswith('Test'):
            feature_guess = cls_name[4:] if len(cls_name) > 4 else None

        registry[stable_id] = {
            'stable_case_id': stable_id,
            'case_name': test_name,
            'test_file': test_file,
            'test_nodeid': item.nodeid,
            'feature': feature_guess,
            'priority': 'P2',
            'blocking_type': 'non-blocking',
            'app_area': None,
            'primary_test_component': None,
            'identity_complete': False,
        }
        by_nodeid[item.nodeid] = stable_id

    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
    logger.info('[Auto-Healing] test registry updated: %d entries at %s', len(registry), REGISTRY_PATH)
    return registry


def _get_case_id_for_item(item):
    case_id_marker = item.get_closest_marker('case_id')
    if case_id_marker and case_id_marker.args:
        return str(case_id_marker.args[0])
    registry = _load_registry()
    for cid, entry in registry.items():
        if entry.get('test_nodeid') == item.nodeid:
            return cid
    return item.nodeid


# ─── Failure Evidence ────────────────────────────────────────────────────────

def _evidence_dir_for_item(item, create=True):
    evidence_dir = getattr(item, '_failure_evidence_dir', None)
    if evidence_dir is None:
        evidence_dir = new_evidence_dir(getattr(item, 'originalname', item.name))
        item._failure_evidence_dir = evidence_dir
        item._failure_evidence_rel_dir = os.path.relpath(evidence_dir, PROJECT_ROOT)
    if create:
        os.makedirs(evidence_dir, exist_ok=True)
    return evidence_dir


def new_evidence_dir(test_name):
    stamp = time.strftime('%Y%m%d%H%M%S', time.localtime()) + f'{int((time.time() % 1) * 1000):03d}'
    return os.path.join(EVIDENCE_ROOT, f'{stamp}-{_safe_artifact_name(test_name)}')


def cleanup_passed_evidence(item):
    failed = any(
        getattr(item, f'rep_{phase}', None) is not None and getattr(item, f'rep_{phase}').failed
        for phase in ('setup', 'call', 'teardown')
    )
    evidence_dir = getattr(item, '_failure_evidence_dir', None)
    if not failed and evidence_dir and os.path.exists(evidence_dir):
        shutil.rmtree(evidence_dir, ignore_errors=True)


_STEP_RE = re.compile(r'''with\s+step\(\s*["'](.+?)["']''')
_DEF_RE = re.compile(r'^\s*def\s+\w+\s*\(')
_TB_MARKER_RE = re.compile(r'^E\s+')


def _fail_line_in_test_file(call, test_path):
    """Line number inside the test file where the exception surfaced."""
    if call is None or getattr(call, 'excinfo', None) is None:
        return None
    try:
        target = os.path.abspath(test_path)
        for entry in reversed(list(call.excinfo.traceback)):
            if os.path.abspath(str(entry.path)) == target:
                return entry.lineno + 1
    except Exception:
        pass
    return None


def _infer_fail_step(test_path, fail_line):
    """This project's tests are plain functions using `with step("...")`, so
    there is no runtime step object to read. Recover the failing step by
    scanning the test source for the nearest `with step(...)` above the
    failing line — same information the healing agent expects in fail_step."""
    if not fail_line:
        return None
    try:
        with open(test_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception:
        return None

    # Count only inside the enclosing test function so `order` matches the
    # step number the reader sees in that test, not the whole module.
    body_start = 0
    for idx, text in enumerate(lines[:fail_line]):
        if _DEF_RE.match(text):
            body_start = idx

    order = 0
    label = None
    for text in lines[body_start:fail_line]:
        match = _STEP_RE.search(text)
        if match:
            order += 1
            label = match.group(1)
    if label is None:
        return None
    return {'id': f'step_{order}', 'order': order, 'action_name': label}


def collect_failure_evidence(item, rep, call):
    """Save raw failure evidence only. Root-cause analysis is intentionally out of scope."""
    test_name = getattr(item, 'originalname', item.name)
    evidence_dir = _evidence_dir_for_item(item)

    collection_errors = []
    screenshot_name = 'fail_moment.png'
    hierarchy_name = 'fail_moment_hierarchy.xml'
    screenshot_path = os.path.join(evidence_dir, screenshot_name)
    hierarchy_path = os.path.join(evidence_dir, hierarchy_name)

    appium_driver = _active_driver

    if appium_driver is not None:
        try:
            appium_driver.save_screenshot(screenshot_path)
        except Exception as e:
            collection_errors.append(f'screenshot: {e}')
        try:
            _write_text(hierarchy_path, appium_driver.page_source)
        except Exception as e:
            collection_errors.append(f'ui_hierarchy: {e}')
    else:
        collection_errors.append('driver: no active driver for this test')

    pytest_config = item.config
    location_path, location_line, location_function = rep.location
    exception_type = call.excinfo.typename if call.excinfo is not None else None
    exception_message = str(call.excinfo.value) if call.excinfo is not None else None

    test_path = str(item.fspath) if item.fspath else os.path.join(PROJECT_ROOT, location_path)
    fail_line = _fail_line_in_test_file(call, test_path)
    current_step = _infer_fail_step(test_path, fail_line)

    app_state = _collect_app_state(appium_driver) if appium_driver is not None else {}
    if os.path.exists(screenshot_path):
        is_black = _screenshot_is_black(screenshot_path)
        if is_black is not None:
            app_state['screenshot_is_black'] = is_black

    stable_case_id = None
    case_id_marker = item.get_closest_marker('case_id')
    if case_id_marker and case_id_marker.args:
        stable_case_id = str(case_id_marker.args[0])

    metadata = {
        'schema_version': 'failure_evidence_v1',
        'collected_at': time.strftime('%Y-%m-%dT%H:%M:%S%z', time.localtime()),
        'collection_scope': 'failure_evidence_only',
        'analysis_performed': False,
        'evidence_dir': getattr(item, '_failure_evidence_rel_dir',
                                os.path.relpath(evidence_dir, PROJECT_ROOT)),
        'identity': {
            'stable_case_id': stable_case_id,
            'case_name': test_name,
            'nodeid': rep.nodeid,
            'test_file_path': location_path,
            'identity_gap': stable_case_id is None,
            'identity_gap_reason': None if stable_case_id else
                'No @pytest.mark.case_id marker; id resolved from the auto-healing test registry.',
        },
        'run_context': {
            'run_id': _run_id(pytest_config),
            'branch': _git_value(['rev-parse', '--abbrev-ref', 'HEAD']),
            'commit': _git_value(['rev-parse', 'HEAD']),
            'profile': None,
            'environment': getattr(pytest_config.option, 'markexpr', ''),
            'app_version': _build_context().get('version'),
            'build': _json_safe(_build_context()),
            'device': _json_safe(_device_context()),
            'driver_capabilities': _driver_capabilities(appium_driver) if appium_driver is not None else {},
        },
        'failure_location': {
            'phase': rep.when,
            'test_line': fail_line if fail_line else location_line + 1,
            'test_function': location_function,
            'fail_step_id': current_step.get('id') if current_step else None,
            'fail_step_order': current_step.get('order') if current_step else None,
            'fail_step_action_name': current_step.get('action_name') if current_step else None,
            'step_evidence_gap': True,
            'step_evidence_gap_reason':
                'This suite records no per-step screenshots; fail_step is inferred from the '
                'nearest `with step(...)` above the failing line.',
        },
        'error_evidence': {
            'exception_type': exception_type,
            'exception_message': exception_message,
            'assertion_message': exception_message if exception_type == 'AssertionError' else None,
            'timeout_info': exception_message if exception_type and 'timeout' in exception_type.lower() else None,
            'stack_trace_file': 'stack_trace.txt',
            'duration': rep.duration,
        },
        'visual_evidence': {
            'fail_moment_screenshot': screenshot_name if os.path.exists(screenshot_path) else None,
        },
        'ui_hierarchy': {
            'fail_moment_hierarchy': hierarchy_name if os.path.exists(hierarchy_path) else None,
        },
        'step_evidence': {
            'steps': [],
            'fail_step_before_snapshot': None,
            'fail_step_before_hierarchy': None,
            'fail_step_after_snapshot': None,
            'fail_step_after_hierarchy': None,
            'fail_moment_snapshot': screenshot_name if os.path.exists(screenshot_path) else None,
            'fail_moment_hierarchy': hierarchy_name if os.path.exists(hierarchy_path) else None,
        },
        'app_state': app_state,
        'conditional_evidence': {
            'network_evidence': None,
            'device_state': None,
            'dependency_state': {'phase': rep.when} if rep.when == 'setup' else None,
            'retry_evidence': None,
        },
        'collection_errors': collection_errors,
    }

    _write_text(os.path.join(evidence_dir, 'stack_trace.txt'), getattr(rep, 'longreprtext', '') or '')
    with open(os.path.join(evidence_dir, 'metadata.json'), 'w', encoding='utf-8') as f:
        json.dump(_json_safe(metadata), f, indent=2, ensure_ascii=False)
    logger.info('[Auto-Healing] Failure evidence saved to %s', evidence_dir)


# ─── Retry Protocol Hook (C1) ────────────────────────────────────────────────

def runtest_protocol(item, nextitem):
    """Returns True when this module handled the protocol, None to fall through."""
    from _pytest.runner import runtestprotocol

    if not ENABLED or IS_REPLAY:
        return None

    reports = runtestprotocol(item, nextitem=nextitem, log=False)

    call_report = next((r for r in reports if r.when == 'call'), None)
    call_failed = call_report is not None and call_report.failed

    case_id = _get_case_id_for_item(item)
    pytest_config = item.config

    if call_failed:
        evidence_dir = getattr(item, '_failure_evidence_dir', None)
        evidence_rel = os.path.relpath(evidence_dir, PROJECT_ROOT) if evidence_dir else None

        remaining_budget = _retry_budget['max_cases'] - _retry_budget['used']
        scheduling = _classify_failure_heuristic(evidence_dir, remaining_budget) if evidence_dir else {
            'lane': 'C', 'action': 'deferred', 'preliminary_category': 'unknown',
            'reason': 'no evidence dir available'}

        error_summary = None
        error_type = None
        fail_step = None
        longrepr = getattr(call_report, 'longreprtext', '') or ''
        if longrepr:
            lines = longrepr.strip().splitlines()
            # Prefer the last `E   <Exception>: <message>` line — it carries the
            # actual failure message; pytest's final line is only file:line.
            exc_lines = [_TB_MARKER_RE.sub('', ln).strip() for ln in lines if _TB_MARKER_RE.match(ln)]
            if exc_lines:
                error_summary = exc_lines[0][:200]
            elif lines:
                error_summary = lines[-1][:200]
            for line in exc_lines or lines:
                clean = _TB_MARKER_RE.sub('', line).strip()
                if 'Error' in clean and ':' in clean:
                    error_type = clean.split(':')[0].strip().split('.')[-1]
                    break
            if not error_type and error_summary:
                error_type = 'AssertionError' if 'assert' in error_summary.lower() else 'UnknownError'

        metadata_path = os.path.join(evidence_dir, 'metadata.json') if evidence_dir else None
        if metadata_path and os.path.exists(metadata_path):
            try:
                with open(metadata_path, 'r', encoding='utf-8') as f:
                    location = json.load(f).get('failure_location', {})
                if location.get('fail_step_id'):
                    fail_step = {'id': location.get('fail_step_id'),
                                 'order': location.get('fail_step_order'),
                                 'action': location.get('fail_step_action_name')}
            except Exception:
                pass

        case_data = {
            'case_name': getattr(item, 'originalname', item.name),
            'test_file': item.nodeid,
            'original_status': 'fail',
            'error_summary': error_summary,
            'error_type': error_type,
            'fail_step': fail_step,
            'evidence_path': evidence_rel,
            'evidence_complete': evidence_dir is not None and os.path.exists(
                os.path.join(evidence_dir, 'metadata.json')),
            'scheduling': scheduling,
            'retry': None,
            'root_cause': None, 'patch': None, 'replay': None,
            'final_status': None, 'pr_eligible': False,
        }

        logger.info('[Auto-Healing] %s: %s (category: %s, lane: %s)', case_id,
                    scheduling.get('action'), scheduling.get('preliminary_category'),
                    scheduling.get('lane'))

        if scheduling.get('action') == 'retry' and remaining_budget > 0:
            logger.info('[Auto-Healing] Retrying %s (reason: %s)', case_id,
                        scheduling.get('preliminary_category'))

            original_evidence_dir = evidence_dir
            item._failure_evidence_dir = None
            item._original_evidence_preserved = original_evidence_dir

            retry_reports = runtestprotocol(item, nextitem=nextitem, log=False)
            _retry_budget['used'] += 1

            retry_call = next((r for r in retry_reports if r.when == 'call'), None)
            retry_passed = retry_call is not None and not retry_call.failed

            retry_evidence_dir = getattr(item, '_failure_evidence_dir', None)
            retry_evidence_rel = os.path.relpath(retry_evidence_dir, PROJECT_ROOT) if retry_evidence_dir else None

            status_after = 'fail'
            if retry_passed:
                category = scheduling.get('preliminary_category', '')
                if category == 'app_crash':
                    status_after = 'pass_after_app_crash_retry'
                elif category in ('network_issue', 'server_busy'):
                    status_after = 'pass_after_network_retry'
                elif category == 'generation_fail':
                    status_after = 'pass_after_generation_retry'
                else:
                    status_after = 'pass_after_retry'

            case_data['retry'] = {
                'count': 1,
                'reason': scheduling.get('preliminary_category'),
                'result': 'pass' if retry_passed else 'fail',
                'status_after': status_after if retry_passed else None,
                'evidence_path': retry_evidence_rel,
            }

            reports = retry_reports
            logger.info('[Auto-Healing] Retry result for %s: %s', case_id,
                        'PASS' if retry_passed else 'FAIL')

        _update_case_in_state(pytest_config, case_id, case_data)
    else:
        _update_case_in_state(pytest_config, case_id, {
            'case_name': getattr(item, 'originalname', item.name),
            'test_file': item.nodeid,
            'original_status': 'pass',
        })

    for report in reports:
        item.ihook.pytest_runtest_logreport(report=report)

    return True


# ─── Collection ──────────────────────────────────────────────────────────────

def collection_modifyitems(pytest_config, items):
    if not ENABLED:
        return

    try:
        _bootstrap_test_registry(items)
    except Exception as e:
        logger.warning('[Auto-Healing] Registry bootstrap failed: %s', e)

    if IS_REPLAY:
        for item in items:
            item.add_marker(pytest.mark.auto_healing)

    not_healed_reason = os.environ.get('AUTO_HEALING_NOT_HEALED_REASON')
    if not_healed_reason:
        for item in items:
            item.add_marker(pytest.mark.skip(reason=not_healed_reason))


# ─── Session lifecycle ───────────────────────────────────────────────────────

def configure(pytest_config):
    pytest_config._start_time = time.time()
    if not ENABLED or IS_REPLAY:
        return
    try:
        _init_state_json(pytest_config)
    except Exception as e:
        logger.warning('[Auto-Healing] state.json init failed: %s', e)


def _rp_launch_uuid(pytest_config):
    """The current ReportPortal launch is still open (finish_launch() has not
    run yet — sessionfinish blocks below), so Phase 2 replays can report into
    this SAME launch instead of opening a new one."""
    try:
        service = getattr(pytest_config, 'py_test_service', None)
        if service is None:
            return None
        launch_uuid = getattr(getattr(service, 'rp', None), 'launch_uuid', None)
        if isinstance(launch_uuid, str) and len(launch_uuid) >= 32:
            return launch_uuid
    except Exception as e:
        logger.info('[Auto-Healing] Could not read RP launch id: %s', e)
    return None


def _trigger_phase2(session):
    state = _read_state_json(session.config)
    if not state:
        return

    deferred_count = sum(
        1 for c in state.get('cases', {}).values()
        if c.get('scheduling', {}).get('action') == 'deferred'
    )
    if deferred_count == 0:
        logger.info('[Auto-Healing] No deferred cases — Phase 2 not needed')
        return

    if not PHASE2_ENABLED:
        logger.info('[Auto-Healing] %d deferred cases — Phase 2 disabled (AUTO_HEALING_PHASE2=0)',
                    deferred_count)
        return

    run_id = _run_id(session.config)
    run_dir = os.path.join(HEALING_PROJECT_PATH, 'runs', run_id)
    log_path = os.path.join(run_dir, 'phase2.log')
    healing_results_path = os.path.join(run_dir, 'healing_results.json')
    sentinel_path = os.path.join(run_dir, '.phase2_done')

    orchestrator_py = os.path.join(HEALING_PROJECT_PATH, 'tools', 'orchestrator.py')
    if not os.path.exists(orchestrator_py):
        logger.warning('[Auto-Healing] Phase 2 orchestrator not found at %s', orchestrator_py)
        return

    logger.info('[Auto-Healing] %d deferred cases — opening Phase 2 window', deferred_count)

    rp_launch_id = _rp_launch_uuid(session.config)

    wrapper = os.path.join(run_dir, '_phase2_run.sh')
    with open(wrapper, 'w') as f:
        f.write('#!/bin/bash\n')
        f.write(f'echo -ne "\\033]0;Auto-Healing Phase 2 — {run_id}\\007"\n')
        f.write(f'export HEALING_PROJECT="{HEALING_PROJECT_PATH}"\n')
        # pytest.ini/conftest.py live in PROJECT_ROOT, so that is the directory
        # replay.py has to run pytest from.
        f.write(f'export TEST_PROJECT="{PROJECT_ROOT}"\n')
        if rp_launch_id:
            f.write(f'export AUTO_HEALING_RP_LAUNCH_ID="{rp_launch_id}"\n')
        f.write(f'python3 "{orchestrator_py}" "{run_id}" 2>&1 | tee "{log_path}"\n')
        f.write(f'touch "{sentinel_path}"\n')
        f.write('echo ""\n')
        f.write('echo "Phase 2 complete."\n')
        f.write('sleep 3\n')
    os.chmod(wrapper, 0o755)

    subprocess.Popen(['open', '-a', 'Terminal', wrapper])

    deadline = time.time() + PHASE2_TIMEOUT_SEC
    while not os.path.exists(sentinel_path) and time.time() < deadline:
        time.sleep(2)

    if not os.path.exists(healing_results_path):
        logger.warning('[Auto-Healing] Phase 2 timed out or no results')
        return

    with open(healing_results_path, 'r', encoding='utf-8') as f:
        healing_results = json.load(f)
    logger.info('[Auto-Healing] ── Phase 2 Results ──')
    for r in healing_results:
        cid = r.get('case_id', '?')
        rc = r.get('root_cause', {}) or {}
        status = r.get('final_status', 'unknown')
        logger.info('[Auto-Healing]   %s: %s (confidence=%s) → %s', cid,
                    rc.get('type', '?'), rc.get('confidence', '?'), status)
        if rc.get('reason'):
            logger.info('[Auto-Healing]     %s', rc['reason'][:200])
    healed = sum(1 for r in healing_results if r.get('healed'))
    logger.info('[Auto-Healing] Phase 2 done: %d/%d healed', healed, len(healing_results))


def sessionfinish(session, exitstatus):
    if not ENABLED:
        return

    try:
        _finalize_state_json(session.config)
    except Exception as e:
        logger.warning('[Auto-Healing] state.json finalize failed: %s', e)

    if IS_REPLAY:
        return

    try:
        _trigger_phase2(session)
    except Exception as e:
        logger.warning('[Auto-Healing] Phase 2 auto-trigger failed: %s', e)
