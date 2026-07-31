import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00053_glitch')
def test_00053_glitch(actions: DriverActions):
    """glitch"""
    mode = 1
    uuid = ['8537a54d-a7f8-437f-beb8-f19bcfb6b3de', '84d18433-9ec6-4aa0-a49f-1cbe3ccc93ec', '46a04393-ce71-4de6-b7f8-cbb6d3e69fc1', 'a8ee2818-b9cc-4379-9798-bead1b8f31cc', '4305aac3-aff9-4033-95c4-52fc42385ad2', 'ce2f0178-b64d-4d47-8742-7880b8ca6891', 'cda3eb88-9e01-453f-83ba-0fed26b6164f', '5ae56bf7-560d-4468-8820-a022343b18e3', '1d107d4f-52d0-4aa6-9039-335cdf5bfe26', '90042052-2b7f-45ba-9423-2934477a05ef', 'ab2bc9f1-1197-4d34-8b7e-fb7541148d4a', '23d1ec03-8786-438b-a71c-fa08e129d47f', 'e12e139e-885a-41f3-acd8-655584d69bcc', '1d6d56aa-8f1d-423b-97a3-c81280e4d733', '50ec37a6-e911-42f2-b291-b39502b28c07', 'c647a318-fd8c-476a-8f58-3da1a907aadc', 'cbc164b4-d861-476f-8071-84e67c0dfc8d', 'defa1434-e9b4-4e46-ad7e-6bdc963f1fb8', '013ff7ec-f019-4c3c-b46f-da429e607ac0', 'de165bf4-6a82-4cb7-93f7-46c89653095d', 'f2f8867e-a2a9-4491-8bb6-b78cc542d08e', '0b2f1ee8-3779-4b6a-b974-245b9eaa0a51', '6d4b26fa-6c55-477b-ad5a-54a4a79f017e', '919ed412-9a8f-4e10-83fe-a6cbd7a54776', 'a24fdef9-2a8f-4b37-ab0e-adcd7921f762', '974fad40-0eb2-4880-8060-3b857b1db144', 'b82441ea-86ac-4467-91d4-185f4c820abd', 'bcc98de0-f330-4711-836d-2e358227553a', 'ac89d0c9-23c7-4964-bb7a-1e94988e4806', 'cd87ce57-5164-4627-bf34-717360af592d', '3e4c3ab5-fe39-4a28-b765-962db6ec79c3', '11e44f5d-e23d-4dfb-9681-66790f7143ce', 'fe74831d-caac-45c0-a24f-d73079a1462d', 'b229c1dc-2a37-43b8-a9bf-a2c86dc39c17']
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Glitch')
    with step('[Verify] snapshot: 05_04_03_temp1_default.png'):
        actions.capture_for_gt('05_04_03_temp1_default.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    with step('[Verify] compare: 05_04_03_temp1_default.png'):
        assert actions.compare_with_gt('05_04_03_temp1_default.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '7')
    with step('[Verify] snapshot: 05_04_03_temp7_default.png'):
        actions.capture_for_gt('05_04_03_temp7_default.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    with step('[Verify] compare: 05_04_03_temp7_default.png'):
        assert actions.compare_with_gt('05_04_03_temp7_default.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_glitch_slider_angle'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    with step('[Action] adjust_glitch_slider_fade7'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    with step('[Action] adjust_glitch_slider_distance'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    with step('[Verify] snapshot: 05_04_03_temp7_min.png'):
        actions.capture_for_gt('05_04_03_temp7_min.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    with step('[Verify] compare: 05_04_03_temp7_min.png'):
        assert actions.compare_with_gt('05_04_03_temp7_min.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_glitch_slider_distance'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_glitch_slider_angle'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_glitch_slider_fade7'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Verify] snapshot: 05_04_03_temp7_max.png'):
        actions.capture_for_gt('05_04_03_temp7_max.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    with step('[Verify] compare: 05_04_03_temp7_max.png'):
        assert actions.compare_with_gt('05_04_03_temp7_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1')
    with step('[Action] adjust_glitch_slider_horizontal'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    with step('[Action] adjust_glitch_slider_vertical'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    with step('[Action] adjust_glitch_slider_fade1'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    with step('[Verify] snapshot: 05_04_03_temp1_min.png'):
        actions.capture_for_gt('05_04_03_temp1_min.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    with step('[Verify] compare: 05_04_03_temp1_min.png'):
        assert actions.compare_with_gt('05_04_03_temp1_min.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_glitch_slider_horizontal'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_glitch_slider_vertical'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_glitch_slider_fade1'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Verify] snapshot: 05_04_03_temp1_max.png'):
        actions.capture_for_gt('05_04_03_temp1_max.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    with step('[Verify] compare: 05_04_03_temp1_max.png'):
        assert actions.compare_with_gt('05_04_03_temp1_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_glitch_slider_fade1'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    with step('[Verify] snapshot: 05_04_03_no_mask.png'):
        actions.capture_for_gt('05_04_03_no_mask.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskModeButton')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'circle_thumb')):
        assert False, 'Tap downloaded mask fail'
    with step('[Verify] snapshot: 05_04_03_dled_mask.png'):
        actions.capture_for_gt('05_04_03_dled_mask.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    if actions.compare_with_gt('05_04_03_dled_mask.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Downloaded mask comparison fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'drop_thumb')):
        assert False, 'Tap build-in mask fail'
    with step('[Verify] snapshot: 05_04_03_og_mask.png'):
        actions.capture_for_gt('05_04_03_og_mask.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    if actions.compare_with_gt('05_04_03_og_mask.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Build-in mask comparison fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskInvertButton')):
        assert False, 'Tap inverse mask fail'
    with step('[Verify] snapshot: 05_04_03_inverse_mask.png'):
        actions.capture_for_gt('05_04_03_inverse_mask.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    if (not actions.compare_with_gt('05_04_03_inverse_mask.png', gt_folder=TD.GT_FOLDER)[0]):
        assert False, 'Inverse mask comparison fail'
    with step('[Verify] snapshot: 05_04_03_before_rotate.png'):
        actions.capture_for_gt('05_04_03_before_rotate.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    rotate_button_pos = actions.get_element_bounds(AppiumBy.NAME, 'btn_FontRotate_n')
    rotate_button_des = (rotate_button_pos[0] + 100, rotate_button_pos[1])
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(
            rotate_button_pos[0],
            rotate_button_pos[1],
            rotate_button_des[0],
            rotate_button_des[1],
        )
    with step('[Verify] snapshot: 05_04_03_after_rotate.png'):
        actions.capture_for_gt('05_04_03_after_rotate.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    if actions.compare_with_gt('05_04_03_after_rotate.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, '[Glitch] Resize/rotate mask comparison fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step('[Verify] snapshot: 05_04_03_leave_mask_x.png'):
        actions.capture_for_gt('05_04_03_leave_mask_x.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    with step('[Verify] compare: 05_04_03_leave_mask_x.png'):
        assert actions.compare_with_gt('05_04_03_leave_mask_x.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskModeButton')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[3]')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap done button fail'
    with step('[Verify] snapshot: base05_04_03_tap_maskv.png'):
        actions.capture_for_gt('base05_04_03_tap_maskv.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    with step('[Verify] compare: 05_04_03_tap_maskv.png'):
        assert actions.compare_with_gt('05_04_03_tap_maskv.png', gt_folder=TD.GT_FOLDER)[0]
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap v fail'
    with step('[Verify] snapshot: 05_04_03_tap_v.png'):
        actions.capture_for_gt('05_04_03_tap_v.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Verify] compare: 05_04_03_tap_v.png'):
        assert actions.compare_with_gt('05_04_03_tap_v.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_04_03_before_enter_glitch.png'):
        actions.capture_for_gt('05_04_03_before_enter_glitch.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Glitch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1')
    with step('[Verify] snapshot: 05_04_03_before_enter_brush.png'):
        actions.capture_for_gt('05_04_03_before_enter_brush.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton')
    with step('[Verify] snapshot: 05_04_03_brush-_before.png'):
        actions.capture_for_gt('05_04_03_brush-_before.png')
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')):
        pass
    with step('[Verify] snapshot: 05_04_03_brush-_after.png'):
        actions.capture_for_gt('05_04_03_brush-_after.png')
    if actions.compare_with_gt('05_04_03_brush-_after.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'Adjust brush size fail'
    from_pos = (205, 100)
    destination = (350, 600)
    with step('[Verify] snapshot: 05_04_03_before_brush-.png'):
        actions.capture_for_gt('05_04_03_before_brush-.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(205, 100, 350, 600)
    with step('[Verify] snapshot: 05_04_03_after_brush-.png'):
        actions.capture_for_gt('05_04_03_after_brush-.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if (not actions.compare_with_gt('05_04_03_after_brush-.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Eraser - fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    with step('[Verify] snapshot: 05_04_03_brush+_before.png'):
        actions.capture_for_gt('05_04_03_brush+_before.png')
    with step('[Action] adjust_cutout_brush_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_04_03_brush+_after.png'):
        actions.capture_for_gt('05_04_03_brush+_after.png')
    if (not actions.compare_with_gt('05_04_03_brush+_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Adjust brush size fail'
    from_pos = (205, 100)
    destination = (350, 600)
    with step('[Verify] snapshot: 05_04_03_before_brush+.png'):
        actions.capture_for_gt('05_04_03_before_brush+.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] adjust_cutout_brush_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(205, 100, 350, 600)
    with step('[Verify] snapshot: 05_04_03_after_brush+.png'):
        actions.capture_for_gt('05_04_03_after_brush+.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if (not actions.compare_with_gt('05_04_03_after_brush+.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Eraser + fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn invert n')):
        assert False, 'Tap inverse fail'
    with step('[Verify] snapshot: 05_04_03_inverse_brush.png'):
        actions.capture_for_gt('05_04_03_inverse_brush.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Verify] compare: 05_04_03_inverse_brush.png'):
        assert actions.compare_with_gt('05_04_03_inverse_brush.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step('[Verify] snapshot: 05_04_03_leave_brush_x.png'):
        actions.capture_for_gt('05_04_03_leave_brush_x.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Verify] compare: 05_04_03_leave_brush_x.png'):
        assert actions.compare_with_gt('05_04_03_leave_brush_x.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton')
    from_pos = (20, 100)
    destination = (350, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(20, 100, 350, 600)
    with step('[Verify] snapshot: 05_04_03_smart_brush_on.png'):
        actions.capture_for_gt('05_04_03_smart_brush_on.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn filterEdge n')
    from_pos = (20, 100)
    destination = (350, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(20, 100, 350, 600)
    with step('[Verify] snapshot: 05_04_03_smart_brush_off.png'):
        actions.capture_for_gt('05_04_03_smart_brush_off.png')
    if actions.compare_with_gt('05_04_03_smart_brush_off.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'Smart brush fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap v fail'
    with step('[Verify] snapshot: 05_04_03_tap_brush_v.png'):
        actions.capture_for_gt('05_04_03_tap_brush_v.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView')
    with step('[Verify] compare: 05_04_03_tap_brush_v.png'):
        assert actions.compare_with_gt('05_04_03_tap_brush_v.png', gt_folder=TD.GT_FOLDER)[0]
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'Tap x fail'
    with step('[Verify] snapshot: 05_04_03_leave_glitch_x.png'):
        actions.capture_for_gt('05_04_03_leave_glitch_x.png')
    with step('[Verify] compare: 05_04_03_leave_glitch_x.png'):
        assert actions.compare_with_gt('05_04_03_leave_glitch_x.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00053 completion"):
        assert True
