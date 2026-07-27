import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_11_01_01")
def test_test_main_11_01_01(actions: DriverActions):
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
    with step("[Action] Tap Camera"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Camera')
    with step("[Verify] btnMore is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnMore'), 'element btnMore should be visible'
    with step("[Action] Tap btnFilter"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFilter')
    with step("[Action] Tap Pure"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pure')
    with step("[Action] Tap at (100, 730)"):
        actions.tap_by_coordinates(100, 730)
    with step("[Action] Tap btnTakePhoto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
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
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap BEAUTIFY"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'BEAUTIFY')
    with step("[Action] Tap Conceal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Conceal')
    with step("[Action] Tap btnTakePhoto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
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
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap Skin Tone"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Skin Tone')
    with step("[Action] Tap btnTakePhoto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
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
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap Teeth Whiten"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Teeth Whiten')
    with step("[Action] Tap btnTakePhoto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
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
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap Eye Brighten"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Brighten')
    with step("[Action] Tap btnTakePhoto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
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
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap Eye Bags"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Bags')
    with step("[Action] Tap btnTakePhoto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
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
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap Oiliness"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Oiliness')
    with step("[Action] Tap btnTakePhoto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
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
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap MAKEUP"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'MAKEUP')
    with step("[Action] Tap Lipstick"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lipstick')
    with step("[Action] Tap Nude 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Nude 01')
    with step("[Action] Tap btnTakePhoto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
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
    assert True
