import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00040_adjustment_grain')
def test_00040_adjustment_grain(actions: DriverActions):
    """Adjustment - grain"""
    mode = 1
    uuid = ['e915a94f-aa26-4863-ab21-21bd9b532b37', 'ea850edd-175d-41ec-be68-ced79f55d43e', 'b6e61a2c-0278-442f-a228-2e8420094dd8', 'b1a15979-c7f8-4170-b987-2a02c3edae88', '69b9da30-f1d2-44bc-acf5-8644b27bd1b9']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_10_before_grain.png'):
        actions.capture_for_gt('05_03_10_before_grain.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Details')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Grain')):
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_10_grain_slider_max.png', crop_rect=(0, 60, 276, 429))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_10_grain_slider_min.png', crop_rect=(0, 60, 276, 429))
    from_pos = (50, 460)
    destination = (400, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 460, 400, 460)
    actions.capture_for_gt('base05_03_10_grain_scr_max.png', crop_rect=(0, 60, 276, 429))
    from_pos = (400, 460)
    destination = (50, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 460, 50, 460)
    actions.capture_for_gt('base05_03_10_grain_scr_min.png', crop_rect=(0, 60, 276, 429))
    with step("[Verify] test_00040 completion"):
        assert True
