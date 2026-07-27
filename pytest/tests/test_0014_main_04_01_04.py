import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_04_01_04")
def test_test_main_04_01_04(actions: DriverActions):
    with step("[Action] Tap Camera"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Camera')
    with step("[Verify] btnMore is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnMore'), 'element btnMore should be visible'
    with step("[Action] Tap btnPortrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPortrait')
    with step("[Action] Tap faceRetouchAutoSwitch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'faceRetouchAutoSwitch')
    with step("[Action] Tap Reshape"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Reshape')
    with step("[Action] Tap Jaw"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Jaw')
    with step("[Action] Tap Forehead"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Forehead')
    with step("[Action] Tap Chin"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Chin')
    with step("[Action] Tap Size"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Size')
    with step("[Action] Tap Distance"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Distance')
    with step("[Action] Tap Height"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Height')
    with step("[Action] Tap Distance"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Distance')
    with step("[Action] Tap Height"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Height')
    with step("[Action] Tap Thickness"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Thickness')
    with step("[Action] Tap Size"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Size')
    with step("[Action] Tap Ala"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ala')
    with step("[Action] Tap brushSizeSliderView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushSizeSliderView')
    with step("[Action] Tap Height"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Height')
    with step("[Action] Tap Thickness"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Thickness')
    with step("[Action] Tap btnTakePhoto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Unlock premium features is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Unlock premium features'), 'element Unlock premium features should not be visible'
    assert True
