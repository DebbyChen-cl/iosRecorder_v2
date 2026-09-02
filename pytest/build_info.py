"""Persistent build metadata shared by Jenkins setup and pytest cases.

The file is intentionally outside the test modules so a TestFlight update
performed in one Python process is available to the pytest process Jenkins
starts afterwards.
"""

from __future__ import annotations

import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


DEFAULT_BUILD_INFO = {
    # Keep the values that were previously hard-coded in 03_01_06_2 so the
    # case remains runnable locally before Jenkins has supplied a build.
    "project": "",
    "sr_code": "PHI260623-02",
    "tr_code": "",
    "version": "20.15.0",
    "build_number": "2607211827",
    "build_display": "2607211827 (64)",
    "short_description": "",
    "jenkins_build": "",
    "updated_at": "",
}


def build_info_path() -> Path:
    """Return the state-file location, optionally overridden for local runs."""
    configured = os.environ.get("BUILD_INFO_PATH")
    if configured:
        return Path(configured).expanduser().resolve()
    return Path(__file__).resolve().with_name("build_info.json")


def load_build_info() -> dict[str, str]:
    """Load build metadata, falling back to the previous local test values."""
    info = dict(DEFAULT_BUILD_INFO)
    path = build_info_path()
    try:
        with path.open(encoding="utf-8") as source:
            saved = json.load(source)
    except FileNotFoundError:
        return info
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Unable to read build information from {path}: {exc}") from exc

    if not isinstance(saved, Mapping):
        raise RuntimeError(f"Build information in {path} must be a JSON object")

    for key in info:
        value = saved.get(key)
        if value is not None:
            info[key] = str(value)
    return info


def save_build_info(values: Mapping[str, Any]) -> dict[str, str]:
    """Atomically save build metadata and return the normalized result."""
    info = dict(DEFAULT_BUILD_INFO)
    for key in info:
        value = values.get(key)
        if value is not None:
            info[key] = str(value)
    info["updated_at"] = datetime.now(timezone.utc).isoformat()

    path = build_info_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", delete=False
    ) as temporary:
        json.dump(info, temporary, ensure_ascii=False, indent=2, sort_keys=True)
        temporary.write("\n")
        temporary_path = Path(temporary.name)
    temporary_path.replace(path)
    return info
