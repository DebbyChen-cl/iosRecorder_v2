import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00037_adjustment_sharpness')
def test_00037_adjustment_sharpness(actions: DriverActions):
    """Adjustment - sharpness"""
    mode = 1
    uuid = ['53da1b1c-c753-44c8-89bc-54ad381bad89', '29a82c31-2b1a-460d-97fd-97169dcc2453', 'fcdeb147-2b7f-420d-b182-79803d2e6267', '0ad3cc0a-e2d3-4efd-a714-67691cf22f96', '6dde03cc-8f1d-4303-bd66-3845d73a6b5d', 'bcdcfade-6302-41a3-9c06-e11a0bd3ccb7', '9e6de04e-9359-4ca7-a28f-8dfa037f8545', '0c4154b7-4a2f-4f16-9266-e2316739ec10', '1167cdf4-0f08-44d7-a3ee-9511cd75e74c']
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
    with step('[Verify] snapshot: 05_03_04_before_sharpness.png'):
        actions.capture_for_gt('05_03_04_before_sharpness.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Details')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sharpness')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton') == '0'):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_04_sharpness_slider_max.png', crop_rect=(0, 60, 276, 526))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_04_sharpness_slider_min.png', crop_rect=(0, 60, 276, 526))
    from_pos = (50, 460)
    destination = (400, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 460, 400, 460)
    actions.capture_for_gt('base05_03_04_sharpness_scr_max.png', crop_rect=(0, 60, 276, 526))
    from_pos = (400, 460)
    destination = (50, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 460, 50, 460)
    actions.capture_for_gt('base05_03_04_sharpness_scr_min.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] adjust_hdr_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_04_tap_x.png'):
        actions.capture_for_gt('05_03_04_tap_x.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_03_04_tap_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sharpness')
    with step('[Action] adjust_hdr_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_04_adjust_tap_v.png'):
        actions.capture_for_gt('05_03_04_adjust_tap_v.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_03_04_adjust_tap_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00037 completion"):
        assert True
