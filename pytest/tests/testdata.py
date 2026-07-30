"""Centralised test data for the SFT_renew converted suite.

Values copied verbatim from the legacy SFT suite
(rdqe-ios-autotest-phdm): fixtures/conftest.py TestFixtures and the
inline call sites in SFT/tests/test_pytest_iPHD_SFT_sce_01.py.

NOTE: GT reference images are intentionally NOT bundled. Before running
this suite against a device, populate `pytest/screenshots/ground_truth/SFT_renew/`
(flat, named by snapshot filename) — otherwise compare_with_gt will fail.
"""

# --- Cyberlink account sign-in (legacy: settings_page.sign_in) ---
SIGN_IN_ACCOUNT = "debby_chen+1@cyberlink.com"
SIGN_IN_PASSWORD = "123-/:qwe"

# --- Feedback mail field (legacy: settings_page.input_feedback_mail) ---
FEEDBACK_MAIL_INVALID = "aaa"                 # invalid-format probe
FEEDBACK_MAIL_VALID = "CLTQAATtest@CLT.com"   # valid address

# --- Report distribution (legacy: fixtures/conftest.py receiver_email) ---
RECEIVER_EMAIL = ["terence_chang@cyberlink.com"]

# --- GT comparison folder for this suite (compare_with_gt gt_folder=...) ---
GT_FOLDER = "pytest/screenshots/ground_truth/SFT_renew"


# ─────────────────────────────────────────────────────────────────────────────
# UGC template content fetch + ETag cache
# Ported verbatim from legacy pages/UGC_Page.py (module-level helpers). Pure
# network/file logic with no driver dependency, so it lives in TD to keep the
# UGC test bodies using only `actions` + `TD`. Used by test_00191/00192/00193.
# ─────────────────────────────────────────────────────────────────────────────
import json as _json
import ssl as _ssl
from pathlib import Path as _Path
from urllib.parse import urlencode as _urlencode
from urllib.request import Request as _Request, urlopen as _urlopen
from urllib.error import URLError as _URLError, HTTPError as _HTTPError

_PROJECT_ROOT = _Path(__file__).resolve().parent.parent.parent
_UGC_PATH = "/service/PhotoDirector%20Mobile%20(iOS)/1.0/Deluxe/iOS/UGC_Template/contents"


def _get_ugc_base_url():
    """Return the UGC content base URL based on the active profile's stage_server_content flag."""
    use_stage = False
    try:
        import yaml  # optional; falls back to the online host when unavailable
        with open(_PROJECT_ROOT / "run_config.yaml", encoding="utf-8") as fh:
            cfg = yaml.safe_load(fh) or {}
        profile_name = cfg.get("active_profile", "online")
        use_stage = cfg.get("profiles", {}).get(profile_name, {}).get("stage_server_content", False)
    except Exception:
        use_stage = False
    host = "genesis-test.cyberlink.com" if use_stage else "genesis.cyberlink.com"
    return f"https://{host}{_UGC_PATH}"


def fetch_ugc_template_contents_with_etag_cache(
    cache_file_path,
    etag_file_path=None,
    lang="en_US",
    content_ver="2.0",
    sindex=1,
    eindex=201,
    timeout=20,
):
    """Fetch UGC template contents and update local cache only when ETag changes.

    Returns a dict: ok / updated / etag / cache_file / etag_file / content.
    """
    base_url = _get_ugc_base_url()
    query = _urlencode({
        "lang": lang,
        "contentVer": content_ver,
        "sindex": sindex,
        "eindex": eindex,
    })
    url = f"{base_url}?{query}"

    cache_path = _Path(cache_file_path)
    if not cache_path.is_absolute():
        cache_path = _PROJECT_ROOT / cache_path

    if etag_file_path:
        etag_path = _Path(etag_file_path)
        if not etag_path.is_absolute():
            etag_path = _PROJECT_ROOT / etag_path
    else:
        etag_path = cache_path.with_suffix(cache_path.suffix + ".etag")

    cache_path.parent.mkdir(parents=True, exist_ok=True)

    local_etag = None
    if etag_path.exists():
        local_etag = etag_path.read_text(encoding="utf-8").strip() or None

    request_headers = {
        "User-Agent": "iPHD-Autotest/1.0",
        "Accept": "application/json",
    }

    def _urlopen_with_ssl_retry(request_obj):
        try:
            return _urlopen(request_obj, timeout=timeout)
        except _ssl.SSLCertVerificationError:
            insecure_context = _ssl._create_unverified_context()
            return _urlopen(request_obj, timeout=timeout, context=insecure_context)
        except _URLError as error:
            reason = getattr(error, "reason", None)
            reason_text = str(reason) if reason is not None else str(error)
            cert_failed = isinstance(reason, _ssl.SSLCertVerificationError) or "CERTIFICATE_VERIFY_FAILED" in reason_text
            if cert_failed:
                insecure_context = _ssl._create_unverified_context()
                return _urlopen(request_obj, timeout=timeout, context=insecure_context)
            raise

    remote_etag = None
    try:
        head_request = _Request(url, headers=request_headers, method="HEAD")
        with _urlopen_with_ssl_retry(head_request) as head_response:
            remote_etag = head_response.headers.get("ETag")
    except Exception:
        pass

    if remote_etag and local_etag and remote_etag == local_etag and cache_path.exists():
        body = cache_path.read_text(encoding="utf-8")
        try:
            content = _json.loads(body)
        except _json.JSONDecodeError:
            content = body
        return {
            "ok": True,
            "updated": False,
            "etag": local_etag,
            "cache_file": str(cache_path),
            "etag_file": str(etag_path),
            "content": content,
        }

    get_headers = dict(request_headers)
    if local_etag:
        get_headers["If-None-Match"] = local_etag

    try:
        get_request = _Request(url, headers=get_headers)
        with _urlopen_with_ssl_retry(get_request) as response:
            body = response.read().decode("utf-8", errors="replace")
            new_etag = response.headers.get("ETag") or remote_etag or local_etag

            cache_path.write_text(body, encoding="utf-8")
            if new_etag:
                etag_path.write_text(new_etag, encoding="utf-8")

            try:
                content = _json.loads(body)
            except _json.JSONDecodeError:
                content = body

            return {
                "ok": True,
                "updated": True,
                "etag": new_etag,
                "cache_file": str(cache_path),
                "etag_file": str(etag_path),
                "content": content,
            }
    except _HTTPError as error:
        if error.code == 304 and cache_path.exists():
            body = cache_path.read_text(encoding="utf-8")
            try:
                content = _json.loads(body)
            except _json.JSONDecodeError:
                content = body
            return {
                "ok": True,
                "updated": False,
                "etag": local_etag,
                "cache_file": str(cache_path),
                "etag_file": str(etag_path),
                "content": content,
            }
    except Exception:
        pass

    return {
        "ok": False,
        "updated": False,
        "etag": local_etag,
        "cache_file": str(cache_path),
        "etag_file": str(etag_path),
        "content": None,
    }
