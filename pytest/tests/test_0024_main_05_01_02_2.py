import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_01_02_2")
def test_test_main_05_01_02_2(actions: DriverActions):
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap Crop"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')
    with step("[Action] Tap Perspective"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Perspective')
    with step("[Action] Tap Horizontal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Horizontal')
    assert True
