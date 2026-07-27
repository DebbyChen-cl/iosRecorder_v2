# ─────────────────────────────────────────────
# config.py  –  Device & App configuration
# ─────────────────────────────────────────────
# Fill in the values that match your physical device
# and Appium server before running tests.

APPIUM_SERVER_URL = "http://localhost:4723"

# Bundle ID of the app under test. Used by conftest for reset/launch/terminate
# flows. Kept SEPARATE from the session's appium:bundleId (left unset below) so
# the Appium session still attaches to whichever app is foreground — including
# SpringBoard system permission alerts — while reset_app still knows which app
# to restart between tests.
TARGET_BUNDLE_ID = "com.cyberlink.photodirector"

IOS_CAPABILITIES = {
    "platformName": "iOS",
    "appium:automationName": "XCUITest",
    # ------ Physical device identifiers ------
    "appium:udid": "00008130-000A750C36F0001C",          # e.g. "00008101-001234AB3456001E"
    "appium:deviceName": "QADM_DST2311025_iPhone15ProMax",    # e.g. "John's iPhone 15"
    # Do not set appium:bundleId here: attach to whichever app is currently
    # foreground, including SpringBoard system alerts.
    # "appium:bundleId": "com.cyberlink.photodirector",
    # "appium:app": "/path/to/your.ipa",        # or install from .ipa
    # ------ Code signing (required for physical device) ------
    "appium:xcodeOrgId": "PRFSC7SPL9",           # 10-char Team ID from Apple Developer Portal
    "appium:xcodeSigningId": "Apple Development",
    # ------ Session behaviour ------
    "appium:noReset": True,            # keep app state between sessions
    "appium:fullReset": False,
    "appium:newCommandTimeout": 12000,   # seconds before Appium kills idle session
    # Don't wait for UI quiescence before every command. Matches the phdm project;
    # also avoids WDA hanging when a system permission alert (springboard) is up.
    "appium:waitForQuiescence": False,
    # ── WDA is managed externally (started by Xcode or start.sh iproxy) ──
    # Setting webDriverAgentUrl tells Appium to connect to the already-running WDA
    # and skip ALL lifecycle management: no install, no launch, and critically
    # NO wda.quit() on driver.quit() — so WDA stays alive after pytest finishes.
    "appium:webDriverAgentUrl": "http://localhost:8100",
    "appium:wdaConnectionTimeout": 240000,
    "appium:useNewWDA": False,             # don't replace the running WDA process
    "appium:skipServerInstallation": True, # don't reinstall WDA
}
