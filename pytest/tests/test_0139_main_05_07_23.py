import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_07_23")
def test_test_main_05_07_23(actions: DriverActions):
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
    with step("[Action] Tap AI Relight"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Relight')
    with step("[Action] Tap AI Relight"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Relight')
    with step("[Action] Tap AI Relight"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Relight')
    with step("[Verify] Enhance Your Photo with Relight Tool is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Enhance Your Photo with Relight Tool'), 'element Enhance Your Photo with Relight Tool should be visible'
    with step("[Action] Tap Upgrade to Pro+ Premium"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Upgrade to Pro+ Premium')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Unlock premium features is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Unlock premium features'), 'element Unlock premium features should not be visible'
    with step("[Verify] barImageView is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'barImageView'), 'element barImageView should not be visible'
    with step("[Action] Tap at (100, 400)"):
        actions.tap_by_coordinates(100, 400)
    with step("[Action] Tap at (100, 400)"):
        actions.tap_by_coordinates(100, 400)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap AI Relight"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Relight')
    with step("[Verify] Enhance Your Photo with Relight Tool is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Enhance Your Photo with Relight Tool'), 'element Enhance Your Photo with Relight Tool should be visible'
    with step("[Action] Tap Try First"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step("[Verify] Enhance Your Photo with Relight Tool is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Enhance Your Photo with Relight Tool'), 'element Enhance Your Photo with Relight Tool should not be visible'
    with step("[Action] Tap Atmosphere"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Atmosphere')
    with step("[Action] Tap ic color tint n"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic color tint n')
    with step("[Verify] ic color tint n is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'ic color tint n'), 'element ic color tint n should not be visible'
    with step("[Verify] //*[@name=\"ic color tint n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="ic color tint n"]'), 'element //*[@name="ic color tint n"] should not be visible'
    with step("[Verify] colorCustomizationButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'colorCustomizationButton'), 'element colorCustomizationButton should be visible'
    with step("[Action] Tap at (207, 700)"):
        actions.tap_by_coordinates(207, 700)
    with step("[Action] Tap cancelButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step("[Action] Tap ic color tint n"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic color tint n')
    with step("[Verify] ic color tint n is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'ic color tint n'), 'element ic color tint n should not be visible'
    with step("[Verify] //*[@name=\"ic color tint n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="ic color tint n"]'), 'element //*[@name="ic color tint n"] should not be visible'
    with step("[Verify] colorCustomizationButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'colorCustomizationButton'), 'element colorCustomizationButton should be visible'
    with step("[Action] Tap at (207, 700)"):
        actions.tap_by_coordinates(207, 700)
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step("[Action] Tap at (100, 400)"):
        actions.tap_by_coordinates(100, 400)
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
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
    with step("[Action] Tap btnRedo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRedo')
    with step("[Action] Tap redoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'redoButton')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Action] Tap btn_reset_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n')
    with step("[Action] Tap Ambient"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ambient')
    with step("[Action] Tap ic color tint n"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic color tint n')
    with step("[Verify] ic color tint n is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'ic color tint n'), 'element ic color tint n should not be visible'
    with step("[Verify] //*[@name=\"ic color tint n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="ic color tint n"]'), 'element //*[@name="ic color tint n"] should not be visible'
    with step("[Verify] colorCustomizationButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'colorCustomizationButton'), 'element colorCustomizationButton should be visible'
    with step("[Action] Tap at (207, 700)"):
        actions.tap_by_coordinates(207, 700)
    with step("[Action] Tap cancelButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step("[Action] Tap ic color tint n"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic color tint n')
    with step("[Verify] ic color tint n is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'ic color tint n'), 'element ic color tint n should not be visible'
    with step("[Verify] //*[@name=\"ic color tint n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="ic color tint n"]'), 'element //*[@name="ic color tint n"] should not be visible'
    with step("[Verify] colorCustomizationButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'colorCustomizationButton'), 'element colorCustomizationButton should be visible'
    with step("[Action] Tap at (207, 700)"):
        actions.tap_by_coordinates(207, 700)
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    assert True
