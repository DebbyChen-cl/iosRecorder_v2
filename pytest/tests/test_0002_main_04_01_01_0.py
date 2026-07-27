import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_04_01_01_0")
def test_test_main_04_01_01_0(actions: DriverActions):
    with step("[Verify] btnClose is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnClose'), 'element btnClose should not be visible'
    with step("[Action] Tap Camera"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Camera')
    with step("[Verify] “PhotoDirector” would like to access the Camera. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '“PhotoDirector” would like to access the Camera.'), 'element “PhotoDirector” would like to access the Camera. should be visible'
    with step("[Action] Tap Allow"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow')
    with step("[Verify] “PhotoDirector” Would Like to Access the Microphone is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, '“PhotoDirector” Would Like to Access the Microphone'), 'element “PhotoDirector” Would Like to Access the Microphone should not be visible'
    with step("[Action] Tap Allow"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow')
    with step("[Verify] Allow “PhotoDirector” to use your location? is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Allow “PhotoDirector” to use your location?'), 'element Allow “PhotoDirector” to use your location? should be visible'
    with step("[Action] Tap Allow While Using App"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow While Using App')
    with step("[Verify] Allow “PhotoDirector” to use your location? is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Allow “PhotoDirector” to use your location?'), 'element Allow “PhotoDirector” to use your location? should not be visible'
    with step("[Verify] “PhotoDirector” Would Like to Access the Microphone is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, '“PhotoDirector” Would Like to Access the Microphone'), 'element “PhotoDirector” Would Like to Access the Microphone should not be visible'
    with step("[Action] Tap Allow"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow')
    with step("[Verify] “PhotoDirector” Would Like to Access the Microphone is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, '“PhotoDirector” Would Like to Access the Microphone'), 'element “PhotoDirector” Would Like to Access the Microphone should not be visible'
    assert True
