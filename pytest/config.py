# ─────────────────────────────────────────────
# config.py  –  Device & App configuration
# ─────────────────────────────────────────────
# Fill in the values that match your physical device
# and Appium server before running tests.

APPIUM_SERVER_URL = "http://localhost:4723"

IOS_CAPABILITIES = {
    "platformName": "iOS",
    "appium:automationName": "XCUITest",
    # ------ Physical device identifiers ------
    "appium:udid": "00008020-001E49603CE9002E",          # e.g. "00008101-001234AB3456001E"
    "appium:deviceName": "Amber 的 iPhone",    # e.g. "John's iPhone 15"
    # ------ App ------
    "appium:bundleId": "com.cyberlink.photodirector",   # already installed app
    # "appium:app": "/path/to/your.ipa",        # or install from .ipa
    # ------ Code signing (required for physical device) ------
    "appium:xcodeOrgId": "PRFSC7SPL9",           # 10-char Team ID from Apple Developer Portal
    "appium:xcodeSigningId": "Apple Development",
    # ------ Session behaviour ------
    "appium:noReset": True,            # keep app state between sessions
    "appium:fullReset": False,
    "appium:newCommandTimeout": 120,   # seconds before Appium kills idle session
    "appium:wdaLocalPort": 8200,           # avoid port conflict with recorder (8100)
    "appium:wdaLaunchTimeout": 120000,     # ms to wait for WDA to start
    "appium:wdaConnectionTimeout": 240000,
    # ── Keep WDA alive so recorder can resume after pytest ──
    "appium:useNewWDA": False,             # don't kill the running WDA process
    "appium:skipServerInstallation": True, # don't reinstall WDA (use already-running instance)
}
