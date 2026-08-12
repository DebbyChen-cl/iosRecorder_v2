#!/usr/bin/env python3
"""Rebuild known_issue.json from the test file names.

A test whose file name carries an error reason (`..._NeedRDLocator.py`,
`..._NeedRecordAgain.py`) is a known issue: auto_healing.py skips healing it once
it fails the same way twice. That list has to be refreshed whenever a test file
is renamed — dropping the suffix retires the entry, adding one creates it — and
`test_unittest/test_known_issue_skip.py` fails while it is stale.

    python3 pytest/refresh_known_issue.py            # rewrite the file
    python3 pytest/refresh_known_issue.py --check     # report drift, change nothing

Hand-maintained fields (`bug_code`) and the recorded failure signature
(`last_fail`) are carried over by file name, so refreshing never loses them.
"""

import argparse
import json
import os
import re
import sys

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
TESTS_DIR = os.path.join(MODULE_DIR, 'tests')
KNOWN_ISSUE_PATH = os.path.join(MODULE_DIR, 'known_issue.json')

# The reason starts at the first `need`/`should` word — everything from there to
# the extension is the reason, so compound reasons (`NeedCheckQA_WhereisSpeed`)
# stay intact.
REASON_RE = re.compile(r'_(?=(?:need|should)\w*)', re.I)
TEST_FUNC_RE = re.compile(r'^def (test_\w+)', re.M)


def _first_test_name(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            match = TEST_FUNC_RE.search(f.read())
    except OSError:
        return ''
    return match.group(1) if match else ''


def scan(tests_dir=TESTS_DIR):
    entries = []
    for file_name in sorted(os.listdir(tests_dir)):
        # Only what pytest collects: pytest.ini sets python_files = test_*.py, so
        # a `defeature_*` file never runs and must not claim a known-issue entry.
        if not (file_name.startswith('test_') and file_name.endswith('.py')):
            continue
        match = REASON_RE.search(file_name[:-3])
        if not match:
            continue
        entries.append({
            'file_name': file_name,
            'test_name': _first_test_name(os.path.join(tests_dir, file_name)),
            'error_reason': file_name[:-3][match.start() + 1:],
            'bug_code': '',
        })
    return entries


def merge(entries, existing_path=KNOWN_ISSUE_PATH):
    """Carry `bug_code` and `last_fail` over from the current file, by file name."""
    if not os.path.exists(existing_path) or os.path.getsize(existing_path) == 0:
        return entries
    try:
        with open(existing_path, 'r', encoding='utf-8') as f:
            existing = {e['file_name']: e for e in json.load(f) if isinstance(e, dict)}
    except (OSError, ValueError, KeyError):
        return entries

    for entry in entries:
        previous = existing.get(entry['file_name'])
        if not previous:
            continue
        entry['bug_code'] = previous.get('bug_code', '')
        if previous.get('last_fail'):
            entry['last_fail'] = previous['last_fail']
    return entries


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true',
                        help='exit 1 when the file is out of date; write nothing')
    args = parser.parse_args(argv)

    entries = merge(scan())
    rendered = json.dumps(entries, indent=2, ensure_ascii=False) + '\n'

    current = ''
    if os.path.exists(KNOWN_ISSUE_PATH):
        with open(KNOWN_ISSUE_PATH, 'r', encoding='utf-8') as f:
            current = f.read()

    if args.check:
        if rendered == current:
            print(f'known_issue.json is up to date ({len(entries)} entries)')
            return 0
        print('known_issue.json is out of date — run: python3 pytest/refresh_known_issue.py')
        return 1

    with open(KNOWN_ISSUE_PATH, 'w', encoding='utf-8') as f:
        f.write(rendered)
    print(f'known_issue.json rewritten: {len(entries)} entries')
    return 0


if __name__ == '__main__':
    sys.exit(main())
