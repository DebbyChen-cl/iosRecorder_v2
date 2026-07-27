import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_03_01_06_2")
def test_test_main_03_01_06_2(actions: DriverActions):
    with step("[Action] Tap btnSettings"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step("[Action] Tap Camera Settings"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Camera Settings')
    with step("[Verify] Save GPS Location is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Save GPS Location'), 'element Save GPS Location should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap About"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'About')
    with step("[Verify] developerButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'developerButton'), 'element developerButton should be visible'
    assert False, "original pytest run failed — this recording reproduces a failing run"
