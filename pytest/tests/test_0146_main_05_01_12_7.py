import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_01_12_7")
def test_test_main_05_01_12_7(actions: DriverActions):
    with step("[Action] Tap btnSettings"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
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
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap Sample Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos')
    with step("[Action] Tap photoCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap Quick Actions"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
    with step("[Verify] waitingTitle is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle'), 'element waitingTitle should not be visible'
    with step("[Action] Tap Wire Removal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Wire Removal')
    with step("[Action] Tap btn close outline n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
    with step("[Verify] labelWaiting is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'labelWaiting'), 'element labelWaiting should not be visible'
    with step("[Verify] switchButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'switchButton'), 'element switchButton should be visible'
    with step("[Verify] switchButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'switchButton'), 'element switchButton should be visible'
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Unlock premium features is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Unlock premium features'), 'element Unlock premium features should not be visible'
    with step("[Verify] Auto-renewal for NT$1,190.00 / year is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Auto-renewal for NT$1,190.00 / year'), 'element Auto-renewal for NT$1,190.00 / year should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Action] Tap Quick Actions"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
    with step("[Verify] waitingTitle is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle'), 'element waitingTitle should not be visible'
    with step("[Action] Tap Wire Removal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Wire Removal')
    with step("[Action] Tap btn close outline n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
    with step("[Verify] labelWaiting is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'labelWaiting'), 'element labelWaiting should not be visible'
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    assert True
