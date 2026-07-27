import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_01_12_4")
def test_test_main_05_01_12_4(actions: DriverActions):
    with step("[Action] Tap btnSettings"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step("[Verify] Setting is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Setting'), 'element Setting should not be visible'
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap About"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'About')
    with step("[Verify] developerButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'developerButton'), 'element developerButton should be visible'
    with step("[Verify] Develop Info is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Develop Info'), 'element Develop Info should be visible'
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Action] Tap Free"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Free')
    with step("[Action] Tap Pro+"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pro+')
    with step("[Action] Tap chevron.left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Home"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Home')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap Quick Actions"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
    with step("[Verify] waitingTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle'), 'element waitingTitle should be visible'
    with step("[Verify] waitingTitle is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle'), 'element waitingTitle should not be visible'
    with step("[Action] Tap Background"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step("[Verify] Detecting Background is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Detecting Background'), 'element Detecting Background should not be visible'
    with step("[Action] Tap None"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'None')
    with step("[Action] Tap exposureResetButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'exposureResetButton')
    with step("[Action] Tap saturationResetButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'saturationResetButton')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap Background"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step("[Verify] Detecting Background is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Detecting Background'), 'element Detecting Background should not be visible'
    with step("[Action] Tap Blur"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blur')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap intensityResetButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap Circle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Circle')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap intensityResetButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap Heart"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Heart')
    with step("[Action] Tap intensityResetButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap Sparkle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sparkle')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap intensityResetButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap Star"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Star')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap intensityResetButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap Zoom"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Zoom')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap intensityResetButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap Radial"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Radial')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap intensityResetButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic edit redo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n')
    with step("[Action] Tap ic reset n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic reset n')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap Background"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    assert True
