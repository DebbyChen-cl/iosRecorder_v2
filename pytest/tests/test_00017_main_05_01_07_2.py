import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00017_main_05_01_07_2')
def test_00017_main_05_01_07_2(actions: DriverActions):
    """crop & rotate"""
    uuid = ['4c60aa1b-8cd0-414b-8baf-4d808b66036c', 'c25b2f15-ec0f-4d6d-92b9-c226a5bc808f', 'c7e7113e-dcfb-4eb1-886f-d90eeec3bda8', 'e3e3d0a0-53a5-4c1a-9dc6-f21ad287d30a', '8319bc63-ae61-4c5d-80cd-64e9beef11e9', '207b3ce9-76f0-4b21-beb4-9742c75e4e2f', 'ca4a14af-c245-45c3-b20e-1a17cdee0577', 'a40bcae6-e27a-4b3f-92e3-a6fc56ecc232', '215b4ae7-1dd2-11b2-8000-080027b246c3', '215b4ae7-1dd2-11b2-8001-080027b246c3', '215b4ae7-1dd2-11b2-8002-080027b246c3', '215b4ae7-1dd2-11b2-8003-080027b246c3', '215b4ae7-1dd2-11b2-8004-080027b246c3', '215b4ae7-1dd2-11b2-8005-080027b246c3', '215b4ae7-1dd2-11b2-8006-080027b246c3', '7158302e-13a0-4e9c-b0c0-c2d9d5a650ce', 'b7f80468-5028-47bc-8e0a-b7561eeee87b', 'd7321d8e-62c3-45d5-b3ec-32d589c7877a', 'a7f63d1a-bbea-47de-beb4-38d1433e8da4', 'ff600db0-8d92-4545-83ef-1908e2d8d9ae', 'dd6730b8-1052-48e0-b969-577f713ecee8', 'bcfe663a-4643-4f2e-8b15-97cc2e82f4f9', '5e616fa1-c411-436b-8d44-8045aa45e8ae', '3b09541c-7a41-4453-b3e5-081249f7ba7c', '2d30582c-e92f-4f78-84ed-54b47b406f0c', '2cae2cd4-d572-4d1c-9316-2391ba14b1f7']
    with step('[Action] close_xmas'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Close', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Close')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Close')
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
            actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    with step('[Verify] snapshot: 05_01_07_OG_without_crop.png'):
        actions.capture_for_gt('05_01_07_OG_without_crop.png', crop_rect=(0, 60, 276, 597))
    destination = (150, 300)
    source_bounds = actions.get_element_bounds(AppiumBy.ACCESSIBILITY_ID, 'crop_control_topL')
    if source_bounds:
        source_x, source_y, source_w, source_h = source_bounds
        actions.drag_coordinates(source_x + source_w // 2, source_y + source_h // 2, *destination)
    else:
        assert False, 'Crop control not found'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step('[Verify] snapshot: 05_01_07_OG_after_tap_original.png'):
        actions.capture_for_gt('05_01_07_OG_after_tap_original.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_01_07_OG_after_tap_original.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Custom')):
        assert False  # legacy raise
    destination = (150, 400)
    source_bounds = actions.get_element_bounds(AppiumBy.ACCESSIBILITY_ID, 'crop_control_topL')
    if source_bounds:
        source_x, source_y, source_w, source_h = source_bounds
        actions.drag_coordinates(source_x + source_w // 2, source_y + source_h // 2, *destination)
    else:
        assert False, 'Crop control not found'
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Square')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')):
        assert False  # legacy raise
    with step('[Action] adjust_rotate_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Square')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')):
        assert False  # legacy raise
        assert False  # legacy raise
    with step('[Action] adjust_rotate_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:4')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')):
        assert False  # legacy raise
    with step('[Action] adjust_rotate_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')):
        assert False  # legacy raise
    with step('[Action] adjust_rotate_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '2:3')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')):
        assert False  # legacy raise
    with step('[Action] adjust_rotate_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')):
        assert False  # legacy raise
    with step('[Action] adjust_rotate_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '9:16')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')):
        assert False  # legacy raise
    with step('[Action] adjust_rotate_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feed')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')):
        assert False  # legacy raise
    with step('[Action] adjust_rotate_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feed')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Story')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')):
        assert False  # legacy raise
    with step('[Action] adjust_rotate_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feed')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Story')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Profile')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')):
        assert False  # legacy raise
    with step('[Action] adjust_rotate_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feed')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cover')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_01_07_crop_original.png'):
        actions.capture_for_gt('05_01_07_crop_original.png', crop_rect=(0, 60, 276, 597))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')):
        assert False  # legacy raise
    with step('[Action] adjust_rotate_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        pass
    with step('[Verify] snapshot: 05_01_07_after_tap_x.png'):
        actions.capture_for_gt('05_01_07_after_tap_x.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_01_07_after_tap_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Horizontally')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Horizontally')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Vertically')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Vertically')):
        assert False  # legacy raise
    with step('[Verify] crop_or_rotate_state'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    with step('[Action] tap_feature_x_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00017 completion"):
        assert True
