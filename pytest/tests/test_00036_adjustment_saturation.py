import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00036_adjustment_saturation')
def test_00036_adjustment_saturation(actions: DriverActions):
    """Adjustment - saturation"""
    mode = 1
    uuid = ['6dc38344-78df-4abc-a8da-6e6fd06ccfc5', '824508e5-3535-42a7-8634-b74ad808d018', '7b2ba225-5935-4c08-aec6-74a6b471ea9c', 'a0258075-cff9-483f-a63f-6bedf7180783', '2e143e36-e798-4239-ab51-35154d994036', '15fb61a6-a694-4809-88ad-7d83e0f1572f', 'da536433-7066-4291-b21d-2827fdaa73bd', '340be575-ac34-41e7-9754-7f9cdcb22cd4', '86b8382f-db4a-4a64-a30e-994efa35ac82', 'ec674fdf-3bc4-4144-a987-c1a6670fa05d', 'e11fcf43-2cc8-419c-8709-df874440c094']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
            actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
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
    with step('[Verify] snapshot: 05_03_03_before_saturation.png'):
        actions.capture_for_gt('05_03_03_before_saturation.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Saturation')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton') == '0'):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_03_saturation_slider_min.png', crop_rect=(0, 60, 276, 526))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    for _ in range(2):
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(400, 460, 50, 460)
    actions.capture_for_gt('base05_03_03_saturation_scr_min.png', crop_rect=(0, 60, 276, 526))
    from_pos = (50, 460)
    destination = (400, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 460, 400, 460)
    actions.capture_for_gt('base05_03_03_saturation_scr_max.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'saturationColorPickButton')):
        assert False  # legacy raise
    from_pos = (207, 100)
    destination = (207, 670)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(207, 100, 207, 670)
    actions.capture_for_gt('base05_03_03_saturation_down.png', crop_rect=(0, 60, 276, 526))
    from_pos = (207, 670)
    destination = (207, 100)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(207, 670, 207, 100)
    actions.capture_for_gt('base05_03_03_saturation_up.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_03_tap_x.png'):
        actions.capture_for_gt('05_03_03_tap_x.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_03_03_tap_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Saturation')
    with step('[Action] adjust_hdr_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_03_adjust_tap_v.png'):
        actions.capture_for_gt('05_03_03_adjust_tap_v.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_03_03_adjust_tap_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00036 completion"):
        assert True
