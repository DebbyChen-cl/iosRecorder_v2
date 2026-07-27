import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_04a_07")
def test_test_main_05_04a_07(actions: DriverActions):
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
    with step("[Action] Tap Invert"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Invert')
    with step("[Action] Tap Invert"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Invert')
    with step("[Action] Tap btn autofocus n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn autofocus n')
    with step("[Verify] btn autofocus n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn autofocus n'), 'element btn autofocus n should not be visible'
    with step("[Verify] //*[@name=\"btn autofocus n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn autofocus n"]'), 'element //*[@name="btn autofocus n"] should not be visible'
    with step("[Verify] autoFocusButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'autoFocusButton'), 'element autoFocusButton should be visible'
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap Invert"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Invert')
    with step("[Action] Tap btn invert n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn invert n')
    with step("[Verify] btn invert n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn invert n'), 'element btn invert n should not be visible'
    with step("[Verify] //*[@name=\"btn invert n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn invert n"]'), 'element //*[@name="btn invert n"] should not be visible'
    with step("[Verify] maskInvertButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'maskInvertButton'), 'element maskInvertButton should be visible'
    with step("[Action] Tap btn invert n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn invert n')
    with step("[Verify] btn invert n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn invert n'), 'element btn invert n should not be visible'
    with step("[Verify] //*[@name=\"btn invert n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn invert n"]'), 'element //*[@name="btn invert n"] should not be visible'
    with step("[Verify] maskInvertButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'maskInvertButton'), 'element maskInvertButton should be visible'
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap btnRedo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRedo')
    with step("[Action] Tap redoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'redoButton')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Action] Tap Eraser"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
