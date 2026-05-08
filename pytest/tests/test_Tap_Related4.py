import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("Tap_Related4")
def test_Tap_Related4(actions: DriverActions):
    with step("[Action] Tap btn eraser n at (53.3%, 50%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn eraser n', 53.3, 50)
    with step("[Action] Tap //XCUIElementTypeImage at (51.6%, 18%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeImage', 51.6, 18)
    with step("[Action] Tap btn_ok_n at (80.6%, 36.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 80.6, 36.1)
    with step("[Action] Long press ic edit compare n at (50%, 63.3%)"):
        actions.long_press_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit compare n', 50, 63.3, duration=1.0)
