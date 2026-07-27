import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_07_15")
def test_test_main_05_07_15(actions: DriverActions):
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
    with step("[Action] Tap ScrollableMenuViewCell-Portrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step("[Action] Tap Body Reshape"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Body Reshape')
    with step("[Action] Tap btn_leg_width_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_leg_width_n')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap Length"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Length')
    with step("[Action] Tap Waist"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Waist')
    with step("[Action] Tap Resize"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Resize')
    with step("[Action] Tap Arm"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Arm')
    with step("[Action] Tap Shoulder"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shoulder')
    with step("[Action] Tap Width"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Width')
    with step("[Action] Tap Hip"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hip')
    with step("[Action] Tap Height"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Height')
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
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Unlock premium features is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Unlock premium features'), 'element Unlock premium features should not be visible'
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap Crop"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')
    with step("[Action] Tap Crop & Rotate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    with step("[Action] Tap Custom"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Custom')
    with step("[Action] Tap Square"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Square')
    with step("[Action] Tap 4:3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step("[Action] Tap 3:2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')
    with step("[Action] Tap 16:9"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnDone"):
        actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    with step("[Action] Tap btn ok n"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn ok n')
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnDone"):
        actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    with step("[Action] Tap btn ok n"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn ok n')
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnDone"):
        actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    with step("[Action] Tap btn ok n"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn ok n')
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnDone"):
        actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    with step("[Action] Tap btn ok n"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn ok n')
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnDone"):
        actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    with step("[Action] Tap btn ok n"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn ok n')
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step("[Action] Tap ScrollableMenuViewCell-Portrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step("[Action] Tap Body Reshape"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Body Reshape')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] Discard is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Discard'), 'element Discard should not be visible'
    with step("[Verify] //*[@name=\"Discard\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Discard"]'), 'element //*[@name="Discard"] should not be visible'
    with step("[Verify] //*[@label=\"Discard\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="Discard"]'), 'element //*[@label="Discard"] should not be visible'
    with step("[Verify] //*[@value=\"Discard\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="Discard"]'), 'element //*[@value="Discard"] should not be visible'
    assert True
