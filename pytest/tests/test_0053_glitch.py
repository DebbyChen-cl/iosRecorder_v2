import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_glitch")
def test_test_glitch(actions: DriverActions):
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
    with step("[Action] Tap Glitch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Glitch')
    with step("[Action] Tap Glitch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Glitch')
    with step("[Action] Tap Glitch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Glitch')
    with step("[Action] Tap 7"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '7')
    with step("[Action] Tap 7"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '7')
    with step("[Action] Tap 1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1')
    with step("[Action] Tap shapeMaskModeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskModeButton')
    with step("[Action] Tap circle_thumb"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'circle_thumb')
    with step("[Action] Tap drop_thumb"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'drop_thumb')
    with step("[Action] Tap shapeMaskInvertButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskInvertButton')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap shapeMaskModeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskModeButton')
    with step("[Action] Tap SplashMaskCollectionViewCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'SplashMaskCollectionViewCell-2')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap Glitch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Glitch')
    with step("[Action] Tap 1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1')
    with step("[Action] Tap brushModeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton')
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
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap brushModeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap brushModeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton')
    with step("[Action] Tap btn filterEdge n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn filterEdge n')
    with step("[Verify] btn filterEdge n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn filterEdge n'), 'element btn filterEdge n should not be visible'
    with step("[Verify] //*[@name=\"btn filterEdge n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn filterEdge n"]'), 'element //*[@name="btn filterEdge n"] should not be visible'
    with step("[Verify] btnFilterEdge is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnFilterEdge'), 'element btnFilterEdge should be visible'
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
