import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_04a_03_2")
def test_test_main_05_04a_03_2(actions: DriverActions):
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
    with step("[Action] Tap Mosaic"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mosaic')
    with step("[Action] Tap Mosaic"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mosaic')
    with step("[Verify] Brush to add mosaic. is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Brush to add mosaic.'), 'element Brush to add mosaic. should not be visible'
    with step("[Action] Tap Person"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Person')
    with step("[Action] Tap Background"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
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
    with step("[Action] Tap Off"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Off')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap photoPickerButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap Mosaic"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mosaic')
    with step("[Verify] Brush to add mosaic. is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Brush to add mosaic.'), 'element Brush to add mosaic. should not be visible'
    with step("[Action] Tap CircleCheckMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleCheckMenuCell-0')
    with step("[Action] Tap CircleCheckMenuCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleCheckMenuCell-1')
    with step("[Action] Tap Person"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Person')
    with step("[Action] Tap CircleCheckMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleCheckMenuCell-0')
    with step("[Action] Tap CircleCheckMenuCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleCheckMenuCell-1')
    with step("[Action] Tap Background"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    assert True
