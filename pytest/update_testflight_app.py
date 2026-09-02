#!/usr/bin/env python3
"""Backward-compatible entry point for the consolidated TestFlight installer.

New Jenkins jobs call ``installbuild.py`` directly. Keep this filename for
manual commands and integrations that used the earlier script name.
"""

from installbuild import main


if __name__ == "__main__":
    raise SystemExit(main())
