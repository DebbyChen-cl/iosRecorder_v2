import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_removal_manual")
def test_test_removal_manual(actions: DriverActions):
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
    with step("[Action] Tap AI Removal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')
    with step("[Verify] Remove with faster selection tool is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Remove with faster selection tool'), 'element Remove with faster selection tool should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Verify] Remove with faster selection tool is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Remove with faster selection tool'), 'element Remove with faster selection tool should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Verify] Try First is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Try First'), 'element Try First should be visible'
    with step("[Action] Tap Try First"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step("[Verify] Try First is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Try First'), 'element Try First should not be visible'
    with step("[Action] Tap Manual"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Manual')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap redoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'redoButton')
    with step("[Action] Tap Eraser"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step("[Action] Tap applyButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'applyButton')
    with step("[Verify] magicText is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'magicText'), 'element magicText should not be visible'
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap redoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'redoButton')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap AI Removal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')
    with step("[Verify] Remove with faster selection tool is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Remove with faster selection tool'), 'element Remove with faster selection tool should not be visible'
    with step("[Verify] Try First is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Try First'), 'element Try First should not be visible'
    with step("[Action] Tap Manual"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Manual')
    with step("[Action] Tap applyButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'applyButton')
    with step("[Verify] magicText is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'magicText'), 'element magicText should not be visible'
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    assert True
