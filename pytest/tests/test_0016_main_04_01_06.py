import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_04_01_06")
def test_test_main_04_01_06(actions: DriverActions):
    with step("[Action] Tap Camera"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Camera')
    with step("[Verify] btnMore is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnMore'), 'element btnMore should be visible'
    with step("[Action] Tap btnMakeup"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMakeup')
    with step("[Action] Tap Lipstick"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lipstick')
    with step("[Action] Tap Dried Rose 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dried Rose 01')
    with step("[Action] Tap Eyebrows"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyebrows')
    with step("[Action] Tap Daily"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')
    with step("[Action] Tap Eye Shadow"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Shadow')
    with step("[Action] Tap Daily"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')
    with step("[Action] Tap Eyeliner"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyeliner')
    with step("[Action] Tap Eyeliner"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyeliner')
    with step("[Action] Tap Daily"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')
    with step("[Action] Tap Eyelashes"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyelashes')
    with step("[Action] Tap Eyelashes"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyelashes')
    with step("[Action] Tap Daily"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')
    with step("[Action] Tap Contour"):
        actions.tap_by_locator(AppiumBy.NAME, 'Contour')
    with step("[Action] Tap Contour"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Contour')
    with step("[Action] Tap Blush"):
        actions.tap_by_locator(AppiumBy.NAME, 'Blush')
    with step("[Action] Tap Blush"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blush')
    with step("[Action] Tap Natural"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Natural')
    with step("[Action] Tap btnTakePhoto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    assert True
