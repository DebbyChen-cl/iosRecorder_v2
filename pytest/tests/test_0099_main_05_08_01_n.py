import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_08_01_n")
def test_test_main_05_08_01_n(actions: DriverActions):
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
    with step("[Verify] xpromo btn close n is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'xpromo btn close n'), 'element xpromo btn close n should be visible'
    with step("[Action] Tap xpromo btn close n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'xpromo btn close n')
    with step("[Action] Tap Text"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step("[Action] Tap Text"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step("[Action] Tap btnTextEdit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTextEdit')
    with step("[Action] Tap A"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'A')
    with step("[Action] Tap a"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'a')
    with step("[Action] Tap a"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'a')
    with step("[Action] Tap Return"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Return')
    with step("[Action] Tap A"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'A')
    with step("[Action] Tap Next keyboard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next keyboard')
    with step("[Action] Tap Next keyboard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next keyboard')
    with step("[Action] Tap leftAlignmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leftAlignmentButton')
    with step("[Action] Tap centerAlignmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'centerAlignmentButton')
    with step("[Action] Tap rightAlignmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'rightAlignmentButton')
    with step("[Action] Tap btn top done n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn top done n')
    with step("[Verify] btn top done n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn top done n'), 'element btn top done n should not be visible'
    with step("[Verify] //*[@name=\"btn top done n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn top done n"]'), 'element //*[@name="btn top done n"] should not be visible'
    with step("[Verify] applyButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'applyButton'), 'element applyButton should be visible'
    with step("[Verify] Font is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Font'), 'element Font should be visible'
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
    with step("[Action] Drag rotateImageView (50.0%,50.0%) → 270 (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'rotateImageView', 50.0, 50.0, AppiumBy.XPATH, '270', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap btnDuplicate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDuplicate')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap at (205, 435)"):
        actions.tap_by_coordinates(205, 435)
    with step("[Action] Tap btnTextEdit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTextEdit')
    with step("[Action] Tap btn top cancel p"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn top cancel p')
    with step("[Verify] btn top cancel p is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btn top cancel p'), 'element btn top cancel p should not be visible'
    with step("[Verify] //*[@name=\"btn top cancel p\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn top cancel p"]'), 'element //*[@name="btn top cancel p"] should not be visible'
    with step("[Verify] cancelButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'cancelButton'), 'element cancelButton should be visible'
    with step("[Action] Tap btnDelete"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap at (205, 455)"):
        actions.tap_by_coordinates(205, 455)
    with step("[Action] Tap maskButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'maskButton')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btn_add_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n')
    with step("[Action] Tap at (205, 455)"):
        actions.tap_by_coordinates(205, 455)
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
