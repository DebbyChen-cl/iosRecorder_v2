import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_07_18_1")
def test_test_main_05_07_18_1(actions: DriverActions):
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
    with step("[Action] Tap Beautify"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step("[Action] Tap Plumpness"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Plumpness')
    with step("[Action] Tap Auto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step("[Action] Tap Auto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step("[Action] Tap Tear Trough"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tear Trough')
    with step("[Action] Tap Cheek Apples"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cheek Apples')
    with step("[Action] Tap Cheeks"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cheeks')
    with step("[Action] Tap Nasal Base"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Nasal Base')
    with step("[Action] Tap Eye Smile"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Smile')
    with step("[Action] Tap Eye Sockets"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Sockets')
    with step("[Action] Tap Eyebrow Arch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyebrow Arch')
    with step("[Action] Tap Chin"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Chin')
    with step("[Action] Tap Mouth Corner"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mouth Corner')
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
