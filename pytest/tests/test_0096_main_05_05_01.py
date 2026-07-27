import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_05_01")
def test_test_main_05_05_01(actions: DriverActions):
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap Overlay Effect"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Overlay Effect')
    with step("[Action] Tap Blender"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blender')
    with step("[Action] Tap btn eraser n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn eraser n')
    with step("[Verify] btn eraser n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn eraser n'), 'element btn eraser n should not be visible'
    with step("[Verify] //*[@name=\"btn eraser n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn eraser n"]'), 'element //*[@name="btn eraser n"] should not be visible'
    with step("[Verify] brushButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'brushButton'), 'element brushButton should be visible'
    with step("[Action] Tap Brush"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    with step("[Action] Tap btn invert n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn invert n')
    with step("[Verify] btn invert n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn invert n'), 'element btn invert n should not be visible'
    with step("[Verify] //*[@name=\"btn invert n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn invert n"]'), 'element //*[@name="btn invert n"] should not be visible'
    with step("[Verify] btnInvert is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnInvert'), 'element btnInvert should be visible'
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap btn eraser n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn eraser n')
    with step("[Verify] btn eraser n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn eraser n'), 'element btn eraser n should not be visible'
    with step("[Verify] //*[@name=\"btn eraser n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn eraser n"]'), 'element //*[@name="btn eraser n"] should not be visible'
    with step("[Verify] brushButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'brushButton'), 'element brushButton should be visible'
    with step("[Action] Tap Eraser"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step("[Action] Tap btnEdge"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnEdge')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap btn eraser n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn eraser n')
    with step("[Verify] btn eraser n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn eraser n'), 'element btn eraser n should not be visible'
    with step("[Verify] //*[@name=\"btn eraser n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn eraser n"]'), 'element //*[@name="btn eraser n"] should not be visible'
    with step("[Verify] brushButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'brushButton'), 'element brushButton should be visible'
    with step("[Action] Tap btnEdge"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnEdge')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap addSrcImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addSrcImageView')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap BG"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'BG')
    with step("[Action] Tap photoCell-4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step("[Action] Tap addSrcImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addSrcImageView')
    with step("[Action] Tap btnCamera"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCamera')
    with step("[Action] Tap PhotoCapture"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoCapture')
    with step("[Action] Tap Use Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use Photo')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Overlay Effect"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Overlay Effect')
    with step("[Action] Tap Blender"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blender')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
