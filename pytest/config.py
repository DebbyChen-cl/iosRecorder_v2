# ─────────────────────────────────────────────
# config.py  –  Device & App configuration
# ─────────────────────────────────────────────
# Fill in the values that match your physical device
# and Appium server before running tests.

APPIUM_SERVER_URL = "http://localhost:4723"

# Bundle ID of the app under test. Used by conftest for reset/launch/terminate
# flows AND set in appium:bundleId below so WDA queries the AUT's element tree
# (system alerts overlaying the AUT are accessible through it in XCUITest).
TARGET_BUNDLE_ID = "com.cyberlink.photodirector"

# ─── Launch deep link ────────────────────────────────────────
# Every test *except* the ones listed in conftest._NO_DEEPLINK_TESTS starts the
# app through this custom URL scheme instead of a plain launch/activate.
# `skipLaunchPopups=true` asks the app itself to suppress the IAP / promo /
# interstitial dialogs, so the post-launch popup sweep has nothing to chase.
# Set to "" to go back to the plain launch_app / activate_app path everywhere.
LAUNCH_DEEPLINK_URL = "clphd://uiTest?skipLaunchPopups=true"

# ─── Auto-Healing ────────────────────────────────────────────
# Master switch for pytest/auto_healing.py: failure evidence, state.json,
# the immediate-retry lane, and handing deferred cases to the Phase 2 agent.
# Set False to run pytest with no auto-healing side effects at all.
AUTO_HEALING_ENABLED = False

# After Phase 2, let the healing agent commit its patches to a new
# '<branch>_YYMMDD_hhmmss' branch and push it.
# WARNING: the agent stages the ENTIRE working tree (git add -A), so any
# unrelated work-in-progress is committed and pushed along with the patches,
# and the repo is left checked out on the new branch. Set False to review the
# patches yourself before committing.
AUTO_HEALING_CREATE_BRANCH = False

# Enable the post-run Phase 2 healing agent.
AUTO_HEALING_PHASE2 = False

# Skip auto-healing for a *known* issue that failed the same way as last run.
# A case listed in pytest/known_issue.json is already understood (waiting on RD,
# needs re-recording, needs a QA decision...), so handing it to the healing agent
# burns a Phase 2 window on a diagnosis nobody is waiting for. The signature of
# every failure is stored back into known_issue.json, so the FIRST failure — and
# any failure that looks different from the stored one — still goes through the
# normal retry/defer lanes; only a repeat of the recorded signature is skipped.
AUTO_HEALING_SKIP_KNOWN_ISSUE = True

# Phase 2 AI backend. Keep these explicit so auto-healing uses Luna with the
# maximum reasoning setting even if the external healing agent's defaults change.
AUTO_HEALING_AI_BACKEND = "codex"
AUTO_HEALING_CODEX_MODEL = "gpt-5.6-luna"
AUTO_HEALING_CODEX_REASONING_EFFORT = "max"

# All three settings are overridable per run by the environment variables
# AUTO_HEALING=0 / AUTO_HEALING_CREATE_BRANCH=0 /
# AUTO_HEALING_SKIP_KNOWN_ISSUE=0.

# ─── Numeric text tolerance (verify_text) ────────────────────────────
# Element id → how far the number in its text may differ from the recorded one.
#
# 'valueLabel' is the readout of the app's sliders. A recorded slider drag stores
# a finger coordinate, and on these controls one unit of slider travel is well
# under a logical point — replaying the same coordinate lands within a unit or two
# of the value that was recorded (measured on device: the same end coordinate gave
# 50, 51 and 52 depending on where the press landed on the thumb). An exact string
# compare therefore fails at random even when the drag worked perfectly.
#
# Only the ids listed here are compared numerically; every other verify_text stays
# an exact string match. A test can override per instance with
# `actions.text_numeric_tolerance = {...}`, or per call with
# `actions.verify_text(..., tolerance=N)`.
#
# 3 is measured, not guessed: the 14 slider verifies of
# test_00015_main_04_01_05 came in at 0 (×9), 1 (×3) and 2 (×2) off the recorded
# value, so the ceiling is the observed maximum plus one unit of margin. It still
# catches every failure mode that matters — a slider that never moved reads 0
# against an expected 50, and a wrong-direction or half-way drag is far outside 3.
TEXT_NUMERIC_TOLERANCE = {
    "valueLabel": 3,
}

# ─── Slider thumb size (points) ──────────────────────────────────────
# Used to place the press point on a slider's thumb, since XCUITest does not
# publish the thumb as its own element. The app's sliders track the finger
# *relative to where it grabbed*, so a press that is off-centre biases the
# result — 4 pt of offset was measured as ~1.5 units of value error.
#
# Measured on this app: value = value_at_press + (end_x - press_x) / 2.70 on a
# 310 pt control, i.e. 270 pt of travel, i.e. a 40 pt thumb (iOS's own default is
# 31.5 pt). Raise or lower only with the same kind of measurement behind it.
SLIDER_THUMB_SIZE = 40.0

IOS_CAPABILITIES = {
    "platformName": "iOS",
    "appium:automationName": "XCUITest",
    # ------ Physical device identifiers ------
    "appium:udid": "00008130-000A750C36F0001C",          # e.g. "00008101-001234AB3456001E"
    "appium:deviceName": "QADM_DST2311025_iPhine15ProMax",    # e.g. "John's iPhone 15"
    # ------ App ------
    "appium:bundleId": "com.cyberlink.photodirector",
    # "appium:app": "/path/to/your.ipa",        # or install from .ipa
    # ------ Code signing (required for physical device) ------
    "appium:xcodeOrgId": "PRFSC7SPL9",           # 10-char Team ID from Apple Developer Portal
    "appium:xcodeSigningId": "Apple Development",
    # ------ Session behaviour ------
    "appium:noReset": True,            # keep app state between sessions
    "appium:fullReset": False,
    "appium:autoLaunch": False,        # don't auto-launch any app; conftest handles activate_app
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
