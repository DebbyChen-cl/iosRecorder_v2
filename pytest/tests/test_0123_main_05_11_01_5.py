import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_11_01_5")
def test_test_main_05_11_01_5(actions: DriverActions):
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
    with step("[Action] Tap Add Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step("[Action] Tap Add Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Verify] photoCell-0 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0'), 'element photoCell-0 should be visible'
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Drag (0,0) → (0,0)"):
        actions.drag_coordinates(0, 0, 0, 0, duration=1.0)
    with step("[Action] Tap maskButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'maskButton')
    with step("[Action] Tap Brush"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap Frame"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Frame')
    with step("[Verify] Frame is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Frame'), 'element Frame should not be visible'
    with step("[Verify] //*[@name=\"Frame\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Frame"]'), 'element //*[@name="Frame"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
    with step("[Action] Tap Simple Frames"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Simple Frames')
    with step("[Action] Tap 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnDelete"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap at (205, 400)"):
        actions.tap_by_coordinates(205, 400)
    with step("[Action] Tap maskButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'maskButton')
    with step("[Action] Tap Brush"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
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
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    assert True
