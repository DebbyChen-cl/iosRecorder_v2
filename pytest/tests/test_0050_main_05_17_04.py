import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_17_04")
def test_test_main_05_17_04(actions: DriverActions):
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap Light Hits"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light Hits')
    with step("[Action] Tap LightHitCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'LightHitCell-0')
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
    with step("[Action] Tap btn_1lv_adjustment_s"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_1lv_adjustment_s')
    with step("[Action] Tap Flip Horizontal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Horizontal')
    with step("[Action] Tap at (220, 220)"):
        actions.tap_by_coordinates(220, 220)
    with step("[Action] Tap Flip Horizontal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Horizontal')
    with step("[Verify] Color is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Color'), 'element Color should be visible'
    with step("[Verify] Contrast is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Contrast'), 'element Contrast should be visible'
    with step("[Action] Drag Color (50.0%,50.0%) → Contrast (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Color', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Contrast', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Flip Vertical"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Vertical')
    with step("[Action] Tap Flip Vertical"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Vertical')
    with step("[Verify] Contrast is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Contrast'), 'element Contrast should be visible'
    with step("[Verify] Color is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Color'), 'element Color should be visible'
    with step("[Action] Drag Contrast (50.0%,50.0%) → Color (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Contrast', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Color', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Softness"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Softness')
    with step("[Action] Tap Brightness"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brightness')
    with step("[Action] Tap Contrast"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Contrast')
    with step("[Action] Tap Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Light Hits"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light Hits')
    with step("[Action] Tap LightHitCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'LightHitCell-0')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
