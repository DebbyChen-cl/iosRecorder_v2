import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_04_01")
def test_test_main_05_04_01(actions: DriverActions):
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap Enhance"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    with step("[Action] Tap Filter"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Filter')
    with step("[Verify] Select a source photo to extract its filter. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Select a source photo to extract its filter.'), 'element Select a source photo to extract its filter. should be visible'
    with step("[Action] Tap at (220, 220)"):
        actions.tap_by_coordinates(220, 220)
    with step("[Verify] Select a source photo to extract its filter. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Select a source photo to extract its filter.'), 'element Select a source photo to extract its filter. should be visible'
    with step("[Action] Tap Basic"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Basic')
    with step("[Action] Tap Vlogger 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Vlogger 01')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Filter"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Filter')
    with step("[Action] Tap Basic"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Basic')
    with step("[Action] Tap Vlogger 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Vlogger 01')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Unlock premium features is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Unlock premium features'), 'element Unlock premium features should not be visible'
    with step("[Action] Tap Vlogger 02"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Vlogger 02')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Filter"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Filter')
    with step("[Action] Tap Basic"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Basic')
    with step("[Action] Tap Vlogger 02"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Vlogger 02')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
