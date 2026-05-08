import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("Tap_Related")
def test_Tap_Related(actions: DriverActions):
    with step("[Action] Tap PhotoDirector"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoDirector')
    with step("[Action] Double tap PhotoDirector"):
        actions.double_tap(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoDirector'))
    with step("[Action] Triple tap PhotoDirector"):
        actions.triple_tap(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoDirector'))
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Long press ic edit compare n"):
        actions.long_press(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit compare n'), duration=1.0)
