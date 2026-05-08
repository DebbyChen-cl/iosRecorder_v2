import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("Tap_related2")
def test_Tap_related2(actions: DriverActions):
    with step("[Action] Tap //XCUIElementTypeImage at (36.2%, 19.8%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeImage', 36.2, 19.8)
    with step("[Action] Double tap //XCUIElementTypeImage at (92.8%, 25.9%)"):
        actions.double_tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeImage', 92.8, 25.9)
    with step("[Action] Triple tap //XCUIElementTypeImage at (5.9%, 46.7%)"):
        actions.triple_tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeImage', 5.9, 46.7)
