import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step
from driver.driver_actions import DriverActions


@pytest.mark.name("recorded_test")
def test_recorded_test(actions: DriverActions):
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
