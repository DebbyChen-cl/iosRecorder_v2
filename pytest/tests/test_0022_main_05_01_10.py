import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_01_10")
def test_test_main_05_01_10(actions: DriverActions):
    with step("[Verify] Would you like to continue editing? is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Would you like to continue editing?'), 'element Would you like to continue editing? should not be visible'
    with step("[Verify] closeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'closeButton'), 'element closeButton should not be visible'
    with step("[Verify] navCloseButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton'), 'element navCloseButton should not be visible'
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
    with step("[Action] Tap AI Enhance"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Enhance')
    with step("[Verify] btn close outline n is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n'), 'element btn close outline n should be visible'
    with step("[Action] Tap btn close outline n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
    with step("[Verify] btn close outline n is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n'), 'element btn close outline n should not be visible'
    with step("[Verify] Enhancing is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Enhancing'), 'element Enhancing should not be visible'
    with step("[Action] Tap aiEnhanceStandardModeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiEnhanceStandardModeButton')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap AI Enhance"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Enhance')
    with step("[Verify] btn close outline n is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n'), 'element btn close outline n should be visible'
    with step("[Action] Tap btn close outline n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
    with step("[Verify] btn close outline n is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n'), 'element btn close outline n should not be visible'
    with step("[Action] Tap generateButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'generateButton')
    with step("[Verify] Enhancing is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Enhancing'), 'element Enhancing should not be visible'
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
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    assert True
