import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_reshape_with_face")
def test_test_reshape_with_face(actions: DriverActions):
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
    with step("[Action] Tap Beautify"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step("[Action] Tap Reshape"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Reshape')
    with step("[Action] Tap Natural"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Natural')
    with step("[Action] Tap Oval"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Oval')
    with step("[Action] Tap V-line"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'V-line')
    with step("[Action] Tap Baby"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Baby')
    with step("[Action] Tap Original"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step("[Action] Tap Face"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Face')
    with step("[Action] Tap Jaw"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Jaw')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Right"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Right')
    with step("[Action] Tap Forehead"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Forehead')
    with step("[Action] Tap Chin"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Chin')
    with step("[Action] Tap Size"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Size')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Right"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Right')
    with step("[Action] Tap Height"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Height')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Right"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Right')
    with step("[Action] Tap Lift"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lift')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Right"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Right')
    with step("[Action] Tap Angle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Angle')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Right"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Right')
    with step("[Action] Tap Width"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Width')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Right"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Right')
    with step("[Action] Tap Distance"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Distance')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Right"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Right')
    with step("[Action] Tap Pupil"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pupil')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Right"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Right')
    with step("[Action] Tap Lift"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lift')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Right"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Right')
    with step("[Action] Tap Eyebrows"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyebrows')
    with step("[Action] Tap Distance"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Distance')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Right"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Right')
    with step("[Action] Tap Thickness"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Thickness')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Right"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Right')
    with step("[Action] Tap Angle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Angle')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Right"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Right')
    with step("[Action] Tap Size"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Size')
    with step("[Action] Tap Height"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Height')
    with step("[Action] Tap Bridge"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Bridge')
    with step("[Action] Tap Ala"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ala')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
    with step("[Action] Tap Right"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Right')
    with step("[Action] Tap Tip"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tip')
    with step("[Action] Tap Size"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Size')
    with step("[Action] Tap Smile"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Smile')
    with step("[Action] Tap Lift"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lift')
    with step("[Action] Tap Thickness"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Thickness')
    with step("[Action] Tap Both"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
    with step("[Action] Tap Upper"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Upper')
    with step("[Action] Tap Upper"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Upper')
    with step("[Action] Tap Lower"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lower')
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
    assert True
