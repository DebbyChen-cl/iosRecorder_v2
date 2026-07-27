import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_18_02")
def test_test_main_05_18_02(actions: DriverActions):
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
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap Background"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step("[Action] Tap Background Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background Art')
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap CMS-phdm_BG_Greenery_18_free_trending"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_BG_Greenery_18_free_trending')
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
    with step("[Action] Tap btnMask"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMask')
    with step("[Action] Tap btt_eraser_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n')
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
    with step("[Action] Tap btt_eraser_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n')
    with step("[Verify] btt_eraser_n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btt_eraser_n'), 'element btt_eraser_n should not be visible'
    with step("[Verify] //*[@name=\"btt_eraser_n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btt_eraser_n"]'), 'element //*[@name="btt_eraser_n"] should not be visible'
    with step("[Verify] //*[@label=\"btt_eraser_n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="btt_eraser_n"]'), 'element //*[@label="btt_eraser_n"] should not be visible'
    with step("[Verify] //*[@value=\"btt_eraser_n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="btt_eraser_n"]'), 'element //*[@value="btt_eraser_n"] should not be visible'
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap btnMask"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMask')
    with step("[Action] Tap btt_eraser_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap Background"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step("[Action] Tap Background Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background Art')
    with step("[Action] Tap CMS-phdm_BG_Greenery_18_free_trending"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_BG_Greenery_18_free_trending')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
