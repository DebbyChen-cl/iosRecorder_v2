import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_splash")
def test_test_splash(actions: DriverActions):
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
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap Splash"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Splash')
    with step("[Verify] Splash is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Splash'), 'element Splash should not be visible'
    with step("[Verify] //*[@name=\"Splash\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Splash"]'), 'element //*[@name="Splash"] should not be visible'
    with step("[Verify] //*[@label=\"Splash\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="Splash"]'), 'element //*[@label="Splash"] should not be visible'
    with step("[Verify] //*[@value=\"Splash\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="Splash"]'), 'element //*[@value="Splash"] should not be visible'
    assert False, "original pytest run failed — this recording reproduces a failing run"
