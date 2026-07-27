import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_try_on_04")
def test_test_ai_try_on_04(actions: DriverActions):
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap AI Try-On"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On')
    with step("[Verify] notShowAgainCheckBox is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox'), 'element notShowAgainCheckBox should not be visible'
    with step("[Action] Tap importButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Verify] We cannot find any faces. Try choosing another one. Thank you. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'We cannot find any faces. Try choosing another one. Thank you.'), 'element We cannot find any faces. Try choosing another one. Thank you. should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Verify] More than one person detected. Try choosing another one. Thank you. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'More than one person detected. Try choosing another one. Thank you.'), 'element More than one person detected. Try choosing another one. Thank you. should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    assert True
