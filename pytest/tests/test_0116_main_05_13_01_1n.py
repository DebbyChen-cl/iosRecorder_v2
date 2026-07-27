import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_13_01_1n")
def test_test_main_05_13_01_1n(actions: DriverActions):
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
    with step("[Action] Tap Sticker"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sticker')
    with step("[Action] Tap Sticker"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sticker')
    with step("[Action] Tap Static Sticker"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Static Sticker')
    with step("[Action] Tap at (360, 790)"):
        actions.tap_by_coordinates(360, 790)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Verify] EditViewControllerBottomBarCollectionView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView'), 'element EditViewControllerBottomBarCollectionView should be visible'
    with step("[Action] Tap Sticker"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sticker')
    with step("[Action] Tap Static Sticker"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Static Sticker')
    with step("[Action] Tap at (360, 790)"):
        actions.tap_by_coordinates(360, 790)
    with step("[Action] Drag (0,0) → (0,0)"):
        actions.drag_coordinates(0, 0, 0, 0, duration=1.0)
    with step("[Action] Tap btnFlip"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFlip')
    with step("[Action] Tap Shadow"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')
    with step("[Verify] Shadow is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Shadow'), 'element Shadow should not be visible'
    with step("[Verify] //*[@name=\"Shadow\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Shadow"]'), 'element //*[@name="Shadow"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
    with step("[Action] Tap Shadow"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')
    with step("[Verify] Shadow is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Shadow'), 'element Shadow should not be visible'
    with step("[Verify] //*[@name=\"Shadow\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Shadow"]'), 'element //*[@name="Shadow"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
    with step("[Action] Tap Opacity"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Opacity')
    with step("[Verify] Opacity is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Opacity'), 'element Opacity should not be visible'
    with step("[Verify] //*[@name=\"Opacity\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Opacity"]'), 'element //*[@name="Opacity"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
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
    with step("[Action] Tap btnDuplicate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDuplicate')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap at (205, 400)"):
        actions.tap_by_coordinates(205, 400)
    with step("[Action] Tap btnRedo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRedo')
    with step("[Action] Tap redoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'redoButton')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Action] Tap at (205, 480)"):
        actions.tap_by_coordinates(205, 480)
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    assert False, "original pytest run failed — this recording reproduces a failing run"
