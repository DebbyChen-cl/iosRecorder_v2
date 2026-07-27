import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_06_01_01_n")
def test_test_main_06_01_01_n(actions: DriverActions):
    with step("[Verify] Would you like to continue editing? is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Would you like to continue editing?'), 'element Would you like to continue editing? should not be visible'
    with step("[Verify] closeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'closeButton'), 'element closeButton should not be visible'
    with step("[Verify] navCloseButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton'), 'element navCloseButton should not be visible'
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap Text"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step("[Verify] Text is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Text'), 'element Text should not be visible'
    with step("[Verify] //*[@name=\"Text\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Text"]'), 'element //*[@name="Text"] should not be visible'
    with step("[Verify] //*[@label=\"Text\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="Text"]'), 'element //*[@label="Text"] should not be visible'
    with step("[Verify] //*[@value=\"Text\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="Text"]'), 'element //*[@value="Text"] should not be visible'
    assert False, "original pytest run failed — this recording reproduces a failing run"
