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
    # ── WDA is managed externally (started by Xcode or start.sh iproxy) ──
    # Setting webDriverAgentUrl tells Appium to connect to the already-running WDA
    # and skip ALL lifecycle management: no install, no launch, and critically
    # NO wda.quit() on driver.quit() — so WDA stays alive after pytest finishes.
    "appium:webDriverAgentUrl": "http://localhost:8100",
    "appium:wdaConnectionTimeout": 240000,
    "appium:useNewWDA": False,             # don't replace the running WDA process
    "appium:skipServerInstallation": True, # don't reinstall WDA
}
