import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_04_01_05")
def test_test_main_04_01_05(actions: DriverActions):
    with step("[Action] Tap Camera"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Camera')
    with step("[Verify] btnMore is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnMore'), 'element btnMore should be visible'
    with step("[Action] Tap btnPortrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPortrait')
    with step("[Action] Tap faceRetouchAutoSwitch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'faceRetouchAutoSwitch')
    with step("[Action] Tap btnTakePhoto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    with step("[Action] Tap Conceal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Conceal')
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
    with step("[Action] Tap Smooth"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Smooth')
    with step("[Verify] Smooth is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Smooth'), 'element Smooth should not be visible'
    with step("[Verify] //*[@name=\"Smooth\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Smooth"]'), 'element //*[@name="Smooth"] should not be visible'
    with step("[Verify] //*[@label=\"Smooth\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="Smooth"]'), 'element //*[@label="Smooth"] should not be visible'
    with step("[Verify] //*[@value=\"Smooth\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="Smooth"]'), 'element //*[@value="Smooth"] should not be visible'
    with step("[Action] Tap Skin Tone"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Skin Tone')
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
    with step("[Action] Tap Teeth Whiten"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Teeth Whiten')
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
    with step("[Action] Tap Eye Brighten"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Brighten')
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
    with step("[Action] Tap Eye Bags"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Bags')
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
    with step("[Action] Tap Oiliness"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Oiliness')
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
