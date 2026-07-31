import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00054_vhs')
def test_00054_vhs(actions: DriverActions):
    """vhs"""
    mode = 1
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
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'VHS')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'VHS_1')
    with step('[Action] get_noise_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText')
    with step('[Action] adjust_VHS_noise_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    if (not (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        assert False, 'Adjust max fail'
    with step('[Action] adjust_VHS_noise_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    if (not (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText') in ('5', '4', '3', '2', '1', '0'))):
        assert False, 'Adjust min fail'
    with step('[Action] get_distortion_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText')
    with step('[Action] adjust_VHS_distortion_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    if (not (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        assert False, 'Adjust max fail'
    with step('[Action] adjust_VHS_distortion_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    if (not (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('5', '4', '3', '2', '1', '0'))):
        assert False, 'Adjust min fail'
    with step('[Action] get_position_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText')
    with step('[Action] adjust_VHS_position_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '1')
    if (not (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        assert False, 'Adjust max fail'
    with step('[Action] adjust_VHS_position_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0')
    if (not (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText') in ('5', '4', '3', '2', '1', '0'))):
        assert False, 'Adjust min fail'
    with step('[Action] get_VHS_fade_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText')
    with step('[Action] adjust_VHS_fade_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[4]', '1')
    if (not (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        assert False, 'Adjust max fail'
    with step('[Action] adjust_VHS_fade_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[4]', '0')
    if (not (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('5', '4', '3', '2', '1', '0'))):
        assert False, 'Adjust min fail'
    with step('[Verify] snapshot: 05_04a_04_no_mask.png'):
        actions.capture_for_gt('05_04a_04_no_mask.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskModeButton')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[2]')
    with step('[Verify] snapshot: 05_04a_04_dled_mask.png'):
        actions.capture_for_gt('05_04a_04_dled_mask.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Verify] compare: 05_04a_04_dled_mask.png'):
        assert actions.compare_with_gt('05_04a_04_dled_mask.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[3]')
    with step('[Verify] snapshot: 05_04a_04_og_mask.png'):
        actions.capture_for_gt('05_04a_04_og_mask.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Verify] compare: 05_04a_04_og_mask.png'):
        assert actions.compare_with_gt('05_04a_04_og_mask.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskInvertButton')
    with step('[Verify] snapshot: 05_04a_04_inverse_mask.png'):
        actions.capture_for_gt('05_04a_04_inverse_mask.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Verify] compare: 05_04a_04_inverse_mask.png'):
        assert actions.compare_with_gt('05_04a_04_inverse_mask.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Verify] snapshot: 05_04a_04_before_rotate.png'):
        actions.capture_for_gt('05_04a_04_before_rotate.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    rotate_button_pos = actions.get_element_bounds(AppiumBy.NAME, 'btn_FontRotate_n')
    rotate_button_des = (rotate_button_pos[0] + 100, rotate_button_pos[1])
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(
            rotate_button_pos[0],
            rotate_button_pos[1],
            rotate_button_des[0],
            rotate_button_des[1],
        )
    with step('[Verify] snapshot: 05_04a_04_after_rotate.png'):
        actions.capture_for_gt('05_04a_04_after_rotate.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if actions.compare_with_gt('05_04a_04_after_rotate.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, '[VHS] Resize/rotate mask comparison fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_04a_04_leave_mask_x.png'):
        actions.capture_for_gt('05_04a_04_leave_mask_x.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Verify] compare: 05_04a_04_leave_mask_x.png'):
        assert actions.compare_with_gt('05_04a_04_leave_mask_x.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[3]')
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_04a_04_tap_maskv.png'):
        actions.capture_for_gt('05_04a_04_tap_maskv.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Verify] compare: 05_04a_04_tap_maskv.png'):
        assert actions.compare_with_gt('05_04a_04_tap_maskv.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Verify] snapshot: 05_04a_04_tap_v.png'):
        actions.capture_for_gt('05_04a_04_tap_v.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Verify] compare: 05_04a_04_tap_v.png'):
        assert actions.compare_with_gt('05_04a_04_tap_v.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_04a_04_before_enter_VHS.png'):
        actions.capture_for_gt('05_04a_04_before_enter_VHS.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'VHS')
    with step('[Action] adjust_VHS_distortion_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Verify] snapshot: 05_04a_04_before_enter_brush.png'):
        actions.capture_for_gt('05_04a_04_before_enter_brush.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step('[Verify] snapshot: 05_04a_04_brush-_before.png'):
        actions.capture_for_gt('05_04a_04_brush-_before.png')
    with step('[Action] adjust_cutout_brush_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_04a_04_brush-_after.png'):
        actions.capture_for_gt('05_04a_04_brush-_after.png')
    if actions.compare_with_gt('05_04a_04_brush-_after.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'Adjust brush size fail'
    from_pos = (20, 100)
    destination = (350, 600)
    with step('[Verify] snapshot: 05_04a_04_before_brush-.png'):
        actions.capture_for_gt('05_04a_04_before_brush-.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(20, 100, 350, 600)
    with step('[Verify] snapshot: 05_04a_04_after_brush-.png'):
        actions.capture_for_gt('05_04a_04_after_brush-.png')
    if actions.compare_with_gt('05_04a_04_after_brush-.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'Eraser - fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    with step('[Verify] snapshot: 05_04a_04_brush+_before.png'):
        actions.capture_for_gt('05_04a_04_brush+_before.png')
    with step('[Action] adjust_cutout_brush_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_04a_04_brush+_after.png'):
        actions.capture_for_gt('05_04a_04_brush+_after.png')
    if actions.compare_with_gt('05_04a_04_brush+_after.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'Adjust brush size fail'
    with step('[Action] adjust_cutout_brush_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    from_pos = (30, 100)
    destination = (380, 620)
    with step('[Verify] snapshot: 05_04a_04_before_brush+.png'):
        actions.capture_for_gt('05_04a_04_before_brush+.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 100, 380, 620)
    with step('[Verify] snapshot: 05_04a_04_after_brush+.png'):
        actions.capture_for_gt('05_04a_04_after_brush+.png')
    if actions.compare_with_gt('05_04a_04_after_brush+.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'Eraser + fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'invertButton')
    with step('[Verify] snapshot: 05_04a_04_inverse_brush.png'):
        actions.capture_for_gt('05_04a_04_inverse_brush.png')
    with step('[Verify] compare: 05_04a_04_inverse_brush.png'):
        assert actions.compare_with_gt('05_04a_04_inverse_brush.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_04a_04_leave_brush_x.png'):
        actions.capture_for_gt('05_04a_04_leave_brush_x.png')
    with step('[Verify] compare: 05_04a_04_leave_brush_x.png'):
        assert actions.compare_with_gt('05_04a_04_leave_brush_x.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'edgeDetectionButton')
    from_pos = (20, 100)
    destination = (350, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(20, 100, 350, 600)
    with step('[Verify] snapshot: 05_04a_04_smart_brush_on.png'):
        actions.capture_for_gt('05_04a_04_smart_brush_on.png')
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'edgeDetectionButton')
    from_pos = (20, 100)
    destination = (350, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(20, 100, 350, 600)
    with step('[Verify] snapshot: 05_04a_04_smart_brush_off.png'):
        actions.capture_for_gt('05_04a_04_smart_brush_off.png')
    if actions.compare_with_gt('05_04a_04_smart_brush_off.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'Smart brush fail'
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_04a_04_tap_brush_v.png'):
        actions.capture_for_gt('05_04a_04_tap_brush_v.png')
    with step('[Verify] compare: 05_04a_04_tap_brush_v.png'):
        assert actions.compare_with_gt('05_04a_04_tap_brush_v.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_04a_04_leave_VHS_x.png'):
        actions.capture_for_gt('05_04a_04_leave_VHS_x.png')
    with step('[Verify] compare: 05_04a_04_leave_VHS_x.png'):
        assert actions.compare_with_gt('05_04a_04_leave_VHS_x.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00054 completion"):
        assert True
