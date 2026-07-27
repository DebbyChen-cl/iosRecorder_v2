import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_03_01_06_1")
def test_test_main_03_01_06_1(actions: DriverActions):
    with step("[Action] Tap btnSettings"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step("[Verify] Sign in is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Sign in'), 'element Sign in should not be visible'
    assert True
