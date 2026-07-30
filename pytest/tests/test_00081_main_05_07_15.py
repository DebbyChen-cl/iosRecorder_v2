import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00081_main_05_07_15')
def test_00081_main_05_07_15(actions: DriverActions):
    """body reshape"""
    mode = 1
    uuid = ['f745cc78-d008-450e-ae6d-ecfa9d302a6f', '362c5e51-fb6c-434a-acbd-a11d2f4570cc', '9dd5c1c5-22a0-4d75-8c42-f16a8ecb575c', 'ce6bb72f-b9d3-47e6-8aac-85f74b664849', 'a712d5da-0c5a-4737-a1c5-b53c6f2050b8', '68f26286-a5d0-4312-8803-a58cb0b9ece1', 'e2f941e5-0681-4a4c-acb2-47ad0096c9c9', '79ea35f5-98f0-4f9c-bb13-7a88ffec4024', 'fcaf2818-0d14-4638-9611-174f59f96f8a', '3bab7888-0f53-4bed-852a-0db4f40a28d2', '1454d451-3d3d-48ce-8fa4-31fc7bda1b7b', 'd2644e12-668a-4dab-857d-4a17e6a4b53e', 'c57c9707-c694-42d4-8655-3d89e5ca59ad', '804e1a6d-ec4b-4919-bfa8-c0d5642914ce', '3d179e52-657a-4098-90ac-6a06ca76d4a1', 'f2a9bf30-7e61-419e-bc29-310308e6f0f7', '7bbba761-e8ea-4025-a2e3-1a4452497086', 'a093a182-f5e3-46f7-b8b3-188914eb4014', '4acbb77c-cc4a-4079-86f8-37ac4992d9ab', '12bd50d9-961c-4431-8166-38b41d2c058d', 'dbc6864e-c591-4701-821d-9fddb83441be', 'ec94a979-1797-4162-b6f3-ab9acf7b35fc', '29a1001f-755d-46e6-bc80-b1c86059c3ae', '993c744a-eb34-433d-ae4c-72ecaf853d92', '0f29ee12-e004-49d2-9716-45d4e73cefda', '993b1750-e429-4f8f-80cd-61fb97c59f69', '3f3669e4-55a8-490f-a17b-dbe651149a85', '5fcbc22f-1dfa-48f3-badd-b497c4fa9d94', 'e6425bfa-7f76-4099-a1cc-f76449074e3b', '5e3b408a-5973-4f06-b22e-4b19cc5c0e92', '2b8602f2-2e4f-4460-b4e5-8893e7d63f5c', '84fb4aab-e22c-4c09-bf2b-342e2d6aca50', 'd925c5d7-3090-4c98-86a6-92fae472ee0e', '6b0b8b16-1b4d-491d-b02d-774a633581f5']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Body Reshape')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_leg_width_n')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
        pass
    else:
        assert False, 'Leg width default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_07_15_leg_width_min.png'):
        actions.capture_for_gt('05_07_15_leg_width_min.png')
    if actions.compare_with_gt('05_07_15_leg_width_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Leg width min fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_15_leg_width_max.png'):
        actions.capture_for_gt('05_07_15_leg_width_max.png')
    if actions.compare_with_gt('05_07_15_leg_width_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Leg width max fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Length')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
        pass
    else:
        assert False, 'Leg length default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_07_15_leg_length_min.png'):
        actions.capture_for_gt('05_07_15_leg_length_min.png')
    if actions.compare_with_gt('05_07_15_leg_length_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Leg length min fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_15_leg_length_max.png'):
        actions.capture_for_gt('05_07_15_leg_length_max.png')
    if actions.compare_with_gt('05_07_15_leg_length_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Leg length max fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Waist')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
        pass
    else:
        assert False, 'Waist default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_07_15_waist_min.png'):
        actions.capture_for_gt('05_07_15_waist_min.png')
    if actions.compare_with_gt('05_07_15_waist_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Waist min fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_15_waist_max.png'):
        actions.capture_for_gt('05_07_15_waist_max.png')
    if actions.compare_with_gt('05_07_15_waist_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Waist max fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Resize')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
        pass
    else:
        assert False, 'Bust default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_07_15_bust_min.png'):
        actions.capture_for_gt('05_07_15_bust_min.png')
    if actions.compare_with_gt('05_07_15_bust_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Bust min fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_15_bust_max.png'):
        actions.capture_for_gt('05_07_15_bust_max.png')
    if actions.compare_with_gt('05_07_15_bust_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Bust max fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Arm')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
        pass
    else:
        assert False, 'Arm default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_07_15_arm_min.png'):
        actions.capture_for_gt('05_07_15_arm_min.png')
    if actions.compare_with_gt('05_07_15_arm_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Arm min fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_15_arm_max.png'):
        actions.capture_for_gt('05_07_15_arm_max.png')
    if actions.compare_with_gt('05_07_15_arm_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Arm max fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shoulder')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
        pass
    else:
        assert False, 'Shoulder default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_07_15_shoulder_min.png'):
        actions.capture_for_gt('05_07_15_shoulder_min.png')
    if actions.compare_with_gt('05_07_15_shoulder_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Shoulder min fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_15_shoulder_max.png'):
        actions.capture_for_gt('05_07_15_shoulder_max.png')
    if actions.compare_with_gt('05_07_15_shoulder_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Shoulder max fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Width')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
        pass
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_07_15_body_width_min.png'):
        actions.capture_for_gt('05_07_15_body_width_min.png')
    if actions.compare_with_gt('05_07_15_body_width_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Body width min fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_15_body_width_max.png'):
        actions.capture_for_gt('05_07_15_body_width_max.png')
    if actions.compare_with_gt('05_07_15_body_width_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Body width max fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hip')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
        pass
    else:
        assert False, 'Hip default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_07_15_hip_min.png'):
        actions.capture_for_gt('05_07_15_hip_min.png')
    if actions.compare_with_gt('05_07_15_hip_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Hip min fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_15_hip_max.png'):
        actions.capture_for_gt('05_07_15_hip_max.png')
    if actions.compare_with_gt('05_07_15_hip_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Hip max fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Height')
    from_pos = (40, 225)
    destination = (40, 150)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(40, 225, 40, 150)
    with step('[Verify] snapshot: 05_07_15_adjust_range.png'):
        actions.capture_for_gt('05_07_15_adjust_range.png')
    if actions.compare_with_gt('05_07_15_adjust_range.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Adjust range fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
        pass
    else:
        assert False, 'Body height default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_07_15_height_min.png'):
        actions.capture_for_gt('05_07_15_height_min.png')
    if actions.compare_with_gt('05_07_15_height_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Height min fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_15_height_max.png'):
        actions.capture_for_gt('05_07_15_height_max.png')
    if actions.compare_with_gt('05_07_15_height_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Height max fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_15_undo.png'):
        actions.capture_for_gt('05_07_15_undo.png')
    if actions.compare_with_gt('05_07_15_height_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo comparison fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_15_redo.png'):
        actions.capture_for_gt('05_07_15_redo.png')
    if actions.compare_with_gt('05_07_15_height_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo comparison fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap done button fail'
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, 'Verify IAP fail'
    with step('[Action] close_IAP'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_07_15_bodyreshape_x.png'):
        actions.capture_for_gt('05_07_15_bodyreshape_x.png')
    if actions.compare_with_gt('05_07_15_bodyreshape_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[x] comparison fail'
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Custom')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Square')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Body Reshape')
    with step('[Verify] snapshot: 05_07_15_nobody.png'):
        actions.capture_for_gt('05_07_15_nobody.png')
    if actions.compare_with_gt('05_07_15_nobody.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Nobody comparison fail'
    with step('[Action] tap_feature_x_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00081 completion"):
        assert True
