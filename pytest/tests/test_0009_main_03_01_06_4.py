import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_03_01_06_4")
def test_test_main_03_01_06_4(actions: DriverActions):
    with step("[Action] Tap btnIAP"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] imgViewTitle is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'imgViewTitle'), 'element imgViewTitle should not be visible'
    with step("[Action] Tap Mine"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mine')
    with step("[Action] Tap btnNotification"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNotification')
    with step("[Verify] Notices is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Notices'), 'element Notices should be visible'
    with step("[Action] Tap imgDisclosure"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'imgDisclosure')
    with step("[Action] Tap Try Now"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try Now')
    assert True
