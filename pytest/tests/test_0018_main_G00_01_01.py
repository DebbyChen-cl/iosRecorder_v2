import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_G00_01_01")
def test_test_main_G00_01_01(actions: DriverActions):
    with step("[Verify] Would you like to continue editing? is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Would you like to continue editing?'), 'element Would you like to continue editing? should not be visible'
    with step("[Verify] closeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'closeButton'), 'element closeButton should not be visible'
    with step("[Verify] navCloseButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton'), 'element navCloseButton should not be visible'
    with step("[Action] Tap Mine"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mine')
    with step("[Verify] Upgrade to Pro+! is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Upgrade to Pro+!'), 'element Upgrade to Pro+! should not be visible'
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap btnTaskCenter"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTaskCenter')
    with step("[Verify] Routine Task is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Routine Task'), 'element Routine Task should be visible'
    with step("[Verify] Invite Friends is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Invite Friends'), 'element Invite Friends should not be visible'
    assert False, "original pytest run failed — this recording reproduces a failing run"
