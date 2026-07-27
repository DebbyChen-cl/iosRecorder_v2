import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_adjustment_hsl")
def test_test_adjustment_hsl(actions: DriverActions):
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
    with step("[Action] Tap Enhance"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    with step("[Action] Tap Adjustments"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')
    with step("[Action] Tap Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step("[Action] Tap HSL"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HSL')
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap btn_reset_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n')
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap btnHSLCurveReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset')
    with step("[Action] Tap HSLColorCollectionViewCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HSLColorCollectionViewCell-2')
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Verify] btn arrow down n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn arrow down n'), 'element btn arrow down n should not be visible'
    with step("[Verify] //*[@name=\"btn arrow down n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn arrow down n"]'), 'element //*[@name="btn arrow down n"] should not be visible'
    with step("[Verify] arrowButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'arrowButton'), 'element arrowButton should be visible'
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap btn_reset_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n')
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap btnHSLCurveReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Adjustments"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')
    with step("[Verify] Sharpness is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Sharpness'), 'element Sharpness should not be visible'
    with step("[Action] Tap HSL"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HSL')
    with step("[Verify] HSL is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'HSL'), 'element HSL should not be visible'
    with step("[Verify] //*[@name=\"HSL\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="HSL"]'), 'element //*[@name="HSL"] should not be visible'
    with step("[Verify] //*[@label=\"HSL\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="HSL"]'), 'element //*[@label="HSL"] should not be visible'
    with step("[Verify] //*[@value=\"HSL\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="HSL"]'), 'element //*[@value="HSL"] should not be visible'
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
