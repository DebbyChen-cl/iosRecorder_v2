import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00139_main_05_07_23')
def test_00139_main_05_07_23(actions: DriverActions):
    """AI relight"""
    mode = 1
    uuid = ['d24724f2-251f-45b5-8fba-235ed86ab09f', '2a4271a5-8e72-4ce2-b5af-64d0b5a823e5', '5c70108e-eda5-4691-b9a0-8f841d48c0fe', '267cd4d1-d822-444e-9d71-4c59a2b88d0f', '5c8a446b-d941-4d5c-b7ce-dd3b4d73f58d', '6b2caeea-787f-4088-bd04-299231de6ff9', 'f1baf7d3-b8b1-48a0-a014-21505ed1cdb8', '530ccf0c-5315-4ae9-82ff-a8504c8ef6aa', 'ba53a79f-c8a4-41ae-a66b-2a9caca15638', '6f12d8b3-e482-483c-b844-b7ccbc4d3caa', '8e6d43e6-e069-43f4-8c5d-e05c2420abf8', 'e7032f61-248a-4d18-b3d6-8e55c45b015a', '8b2e15ba-3b7c-4cac-92ad-520dd0a798d4', 'ce69b8b5-f042-480c-af65-3dbb19daeee8', '92a91e24-b195-4da5-8f2e-7df3ac040287', 'c2c3143f-91fb-40c6-a39f-22cc078b61e4', '392bfda0-e9b0-40c5-a579-6c0c43716886', '42ea6d0c-ee4e-4051-9345-0ce8272bda50', '1ce87d0f-fbc9-4672-a6ba-034fa46a9e0e', 'bad56e27-bf2f-4b08-af52-519ef13fbac4', '088a2f33-64ca-4446-b578-2af959f4da8a', '1a27c828-e469-4d74-9be7-d1a067938269', '2d391b03-2926-40f6-b717-070572e9d7d9', '0874a557-107c-46e0-abc4-4ba29d4800f0', 'aacb59ee-cd32-4782-8d6b-3432727a1333', '6306e837-b509-4281-8f7b-d6446d9a0b96', '5cf223b0-ed71-4db5-bd61-7fe41f848cb4', 'fe52c734-f5ee-49df-b0fb-d16e5cc16044', '293c8629-53ee-4cee-9acf-790e52960650', '3eb5b949-a062-4ce4-a93d-eb4137d2b728', '724e758c-db65-4f02-8b6b-75d34dac724f', 'd7fa3159-ef61-47a0-87d7-c6ca63fcad27', 'facfb030-ed3d-4513-8e19-27568edb7e87', 'bd0bebf6-09b6-4e66-b64d-ac7d6e1e97ea', 'eca7734f-fa33-414a-88d3-1a8c5490b735', '9644b08b-b5a1-40bc-854d-3696dce2ed38', 'cfbe785d-04cc-4e11-b617-24e5f4837f29', 'a701df9e-1f5b-4d0c-9a19-d5bcfe9ed6a4', '240eae42-54e7-41f1-983a-d038cf447c96', '60ceb33d-74ac-40fc-b009-39a7231ec14d', 'd2d40192-cb2f-4aaf-b744-9ce3ca0cb43c', '194605af-e0fb-4728-a25c-703e25568c16', 'f5672d39-7b4a-4482-b95e-f078c0677187', 'bae4cc2a-664a-4c32-b296-9b836b09a8ae', '352e933e-5ca7-44ad-b2d1-b06a386bee94', '98ef6651-8925-47d9-872e-2dd6f92d10b3', '4d7c85c6-ec11-4bd3-b32b-234fb0509e52', '195f22df-0c5a-4b60-a1a9-3ee4e817d449', 'c7049294-b0f3-4216-b86e-048927209c4d', '270d29ac-5467-41f9-8b9f-155b085524ce', '32f82b74-192d-40ba-ac6c-ff2688670527', '8315a342-8466-4ab1-b713-c5b87984c68b', '0b2bafe6-c7d6-4e28-ac4a-9c14fdb41b70', 'b4abad40-061f-4107-8478-e83bb6a758ef', '07d21bc5-580f-497c-82bd-d9d365b70394', 'eb3a70be-375f-4abf-9dda-ed2c396cc02f', 'c8a463c0-78d4-4efc-848a-d18a796f5248', 'a220733c-aa46-4988-978a-eb34f417ed2a', '3330bf42-f3fb-4b4b-88d0-23e6ff011472', 'e8a20ce9-a30b-4cb6-a7a2-d8398358d210', 'f871dec2-9640-48da-9464-9ffd9c84b7d0', 'ef4bc664-a142-4739-994d-4934676bf7e9']
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
    with step('[Verify] snapshot: 05_07_23_before_relight.png'):
        actions.capture_for_gt('05_07_23_before_relight.png')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Relight')
    if actions.is_element_present(AppiumBy.NAME, 'Enhance Your Photo with Relight Tool'):
        pass
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Upgrade to Pro+ Premium')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, 'verify IAP failed'
    with step('[Action] close_IAP'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    with step('[Verify] snapshot: 05_07_23_face_default.png'):
        actions.capture_for_gt('05_07_23_face_default.png')
    if actions.compare_with_gt('05_07_23_face_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'face default compare failed'
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    with step('[Verify] snapshot: 05_07_23_face_color_min.png'):
        actions.capture_for_gt('05_07_23_face_color_min.png')
    if actions.compare_with_gt('05_07_23_face_color_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'face_color_min compare failed'
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Verify] snapshot: 05_07_23_face_color_max.png'):
        actions.capture_for_gt('05_07_23_face_color_max.png')
    if actions.compare_with_gt('05_07_23_face_color_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'face_color_max compare failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    with step('[Verify] snapshot: 05_07_23_face_bright_def.png'):
        actions.capture_for_gt('05_07_23_face_bright_def.png')
    if actions.compare_with_gt('05_07_23_face_bright_def.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'face_bright_def compare failed'
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3', '4', '5')):
        pass
    with step('[Verify] snapshot: 05_07_23_face_bright_min.png'):
        actions.capture_for_gt('05_07_23_face_bright_min.png')
    if actions.compare_with_gt('05_07_23_face_bright_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'face bright min compare failed'
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97', '96', '95')):
        pass
    with step('[Verify] snapshot: 05_07_23_face_bright_max.png'):
        actions.capture_for_gt('05_07_23_face_bright_max.png')
    if actions.compare_with_gt('05_07_23_face_bright_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'face bright max compare failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    with step('[Verify] snapshot: 05_07_23_face_radius_def.png'):
        actions.capture_for_gt('05_07_23_face_radius_def.png')
    if actions.compare_with_gt('05_07_23_face_radius_def.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'face_radius_def compare failed'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3', '4', '5')):
        pass
    with step('[Verify] snapshot: 05_07_23_face_radius_min.png'):
        actions.capture_for_gt('05_07_23_face_radius_min.png')
    if actions.compare_with_gt('05_07_23_face_radius_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'face radius min compare failed'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97', '96', '95')):
        pass
    with step('[Verify] snapshot: 05_07_23_face_radius_max.png'):
        actions.capture_for_gt('05_07_23_face_radius_max.png')
    if actions.compare_with_gt('05_07_23_face_radius_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'face radius max compare failed'
    with step('[Verify] snapshot: 05_07_23_face_source_og.png'):
        actions.capture_for_gt('05_07_23_face_source_og.png')
    with step('[Action] tap light source'):
        actions.tap_by_coordinates(100, 400)
    with step('[Verify] snapshot: 05_07_23_face_source_hide.png'):
        actions.capture_for_gt('05_07_23_face_source_hide.png')
    if (not actions.compare_with_gt('05_07_23_face_source_hide.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'hide light source compare failed'
    with step('[Action] tap light source'):
        actions.tap_by_coordinates(100, 400)
    with step('[Verify] snapshot: 05_07_23_face_source_show.png'):
        actions.capture_for_gt('05_07_23_face_source_show.png')
    if actions.compare_with_gt('05_07_23_face_source_show.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'show light source compare failed'
    with step('[Verify] snapshot: 05_07_23_face_source_before_move.png'):
        actions.capture_for_gt('05_07_23_face_source_before_move.png')
    from_pos = (260, 200)
    destination = (260, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(260, 200, 260, 500)
    with step('[Verify] snapshot: 05_07_23_face_source_after_move.png'):
        actions.capture_for_gt('05_07_23_face_source_after_move.png')
    if (not actions.compare_with_gt('05_07_23_face_source_after_move.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'move light source compare failed'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_07_23_relight_x.png'):
        actions.capture_for_gt('05_07_23_relight_x.png')
    if actions.compare_with_gt('05_07_23_relight_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'relight x compare failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Relight')
    with step('[Action] close_relight_intro'):
        assert actions.is_element_present(AppiumBy.NAME, 'Enhance Your Photo with Relight Tool')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Enhance Your Photo with Relight Tool')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Atmosphere')
    with step('[Verify] snapshot: 05_07_23_atmos_default.png'):
        actions.capture_for_gt('05_07_23_atmos_default.png')
    if actions.compare_with_gt('05_07_23_atmos_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'atmos default compare failed'
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0.5)
    with step('[Verify] snapshot: 05_07_23_atmos_color_mid.png'):
        actions.capture_for_gt('05_07_23_atmos_color_mid.png')
    if actions.compare_with_gt('05_07_23_atmos_color_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'atmos_color_mid compare failed'
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Verify] snapshot: 05_07_23_atmos_color_max.png'):
        actions.capture_for_gt('05_07_23_atmos_color_max.png')
    if actions.compare_with_gt('05_07_23_atmos_color_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'atmos_color_max compare failed'
    with step('[Verify] snapshot: 05_07_23_atmos_before_color_picker.png'):
        actions.capture_for_gt('05_07_23_atmos_before_color_picker.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'ic color tint n')
    with step('[Verify] snapshot: 05_07_23_atmos_color_picker_before.png'):
        actions.capture_for_gt('05_07_23_atmos_color_picker_before.png')
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0.5)
    with step('[Verify] snapshot: 05_07_23_atmos_color_picker_after.png'):
        actions.capture_for_gt('05_07_23_atmos_color_picker_after.png')
    if (not actions.compare_with_gt('05_07_23_atmos_color_picker_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'atmos_color_picker_slider compare failed'
    with step('[Action] tap light source'):
        actions.tap_by_coordinates(100, 400)
    with step('[Verify] snapshot: 05_07_23_atmos_color_picker_select.png'):
        actions.capture_for_gt('05_07_23_atmos_color_picker_select.png')
    if (not actions.compare_with_gt('05_07_23_atmos_color_picker_select.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'select a color compare failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 05_07_23_atmos_color_picker_x.png'):
        actions.capture_for_gt('05_07_23_atmos_color_picker_x.png')
    if actions.compare_with_gt('05_07_23_atmos_color_picker_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Atmosphere color picker cancel comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'ic color tint n')
    with step('[Action] tap color picker'):
        actions.tap_by_coordinates(207, 700)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step('[Verify] snapshot: 05_07_23_atmos_color_picker_v.png'):
        actions.capture_for_gt('05_07_23_atmos_color_picker_v.png')
    if (not actions.compare_with_gt('05_07_23_atmos_color_picker_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Atmosphere color picker done comparison failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    with step('[Verify] snapshot: base05_07_23_atmos_bright_def.png'):
        actions.capture_for_gt('base05_07_23_atmos_bright_def.png')
    if actions.capture_for_gt('05_07_23_atmos_bright_def.png'):
        if actions.compare_with_gt('05_07_23_atmos_bright_def.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Atmosphere brightness default comparison failed'
    else:
        assert False, 'Failed to snapshot atmosphere brightness default'
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3', '4', '5')):
        pass
    with step('[Verify] snapshot: base05_07_23_atmos_bright_min.png'):
        actions.capture_for_gt('base05_07_23_atmos_bright_min.png')
    if actions.capture_for_gt('05_07_23_atmos_bright_min.png'):
        if actions.compare_with_gt('05_07_23_atmos_bright_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Atmosphere brightness min comparison failed'
    else:
        assert False, 'Failed to snapshot atmosphere brightness min'
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97', '96', '95')):
        pass
    with step('[Verify] snapshot: base05_07_23_atmos_bright_max.png'):
        actions.capture_for_gt('base05_07_23_atmos_bright_max.png')
    if actions.capture_for_gt('05_07_23_atmos_bright_max.png'):
        if actions.compare_with_gt('05_07_23_atmos_bright_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Atmosphere brightness max comparison failed'
    else:
        assert False, 'Failed to snapshot atmosphere brightness max'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    with step('[Verify] snapshot: base05_07_23_atmos_radius_def.png'):
        actions.capture_for_gt('base05_07_23_atmos_radius_def.png')
    if actions.capture_for_gt('05_07_23_atmos_radius_def.png'):
        if actions.compare_with_gt('05_07_23_atmos_radius_def.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Atmosphere radius default comparison failed'
    else:
        assert False, 'Failed to snapshot atmosphere radius default'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3', '4', '5')):
        pass
    with step('[Verify] snapshot: base05_07_23_atmos_radius_min.png'):
        actions.capture_for_gt('base05_07_23_atmos_radius_min.png')
    if actions.capture_for_gt('05_07_23_atmos_radius_min.png'):
        if actions.compare_with_gt('05_07_23_atmos_radius_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Atmosphere radius min comparison failed'
    else:
        assert False, 'Failed to snapshot atmosphere radius min'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97', '96', '95')):
        pass
    with step('[Verify] snapshot: base05_07_23_atmos_radius_max.png'):
        actions.capture_for_gt('base05_07_23_atmos_radius_max.png')
    if actions.capture_for_gt('05_07_23_atmos_radius_max.png'):
        if actions.compare_with_gt('05_07_23_atmos_radius_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Atmosphere radius max comparison failed'
    else:
        assert False, 'Failed to snapshot atmosphere radius max'
    with step('[Verify] snapshot: 05_07_23_atmos_source_og.png'):
        actions.capture_for_gt('05_07_23_atmos_source_og.png')
    with step('[Action] tap light source'):
        actions.tap_by_coordinates(100, 400)
    if actions.capture_for_gt('05_07_23_atmos_source_show.png'):
        if (not actions.compare_with_gt('05_07_23_atmos_source_show.png', gt_folder=TD.GT_FOLDER)[0]):
            pass
        else:
            assert False, 'Light source show comparison failed'
    else:
        assert False, 'Failed to snapshot light source show'
    if actions.capture_for_gt('05_07_23_atmos_source_hide.png'):
        if (not actions.compare_with_gt('05_07_23_atmos_source_hide.png', gt_folder=TD.GT_FOLDER)[0]):
            pass
        else:
            assert False, 'Light source hide comparison failed'
    else:
        assert False, 'Failed to snapshot light source hide'
    with step('[Verify] snapshot: 05_07_23_atmos_source_before_move.png'):
        actions.capture_for_gt('05_07_23_atmos_source_before_move.png')
    from_pos = (260, 184)
    destination = (260, 690)
    for _ in range(2):
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(260, 184, 260, 690)
    if actions.capture_for_gt('05_07_23_atmos_source_after_move.png'):
        if (not actions.compare_with_gt('05_07_23_atmos_source_after_move.png', gt_folder=TD.GT_FOLDER)[0]):
            pass
        else:
            assert False, 'Light source move comparison failed'
    else:
        assert False, 'Failed to snapshot light source after move'
    for i in range(2):
        with step('[Action] tap_undo_btn_n'):
            for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
                if actions.is_element_present(__by, __val, timeout=2):
                    actions.tap_by_locator(__by, __val); break
    if actions.capture_for_gt('05_07_23_undo.png'):
        if actions.compare_with_gt('05_07_23_undo.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Undo comparison failed'
    else:
        assert False, 'Failed to snapshot undo'
    for i in range(2):
        with step('[Action] tap_redo_btn_n'):
            for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
                if actions.is_element_present(__by, __val, timeout=2):
                    actions.tap_by_locator(__by, __val); break
    if actions.capture_for_gt('05_07_23_redo.png'):
        if actions.compare_with_gt('05_07_23_redo.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Redo comparison failed'
    else:
        assert False, 'Failed to snapshot redo'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n')
    with step('[Verify] snapshot: base05_07_23_reset.png'):
        actions.capture_for_gt('base05_07_23_reset.png')
    if actions.capture_for_gt('05_07_23_reset.png'):
        if actions.compare_with_gt('05_07_23_reset.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Reset comparison failed'
    else:
        assert False, 'Failed to snapshot reset'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Ambient')
    with step('[Verify] snapshot: base05_07_23_ambient_default.png'):
        actions.capture_for_gt('base05_07_23_ambient_default.png')
    if actions.capture_for_gt('05_07_23_ambient_default.png'):
        if actions.compare_with_gt('05_07_23_ambient_default.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Ambient default comparison failed'
    else:
        assert False, 'Failed to snapshot ambient default'
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0.5)
    with step('[Verify] snapshot: 05_07_23_ambient_color_mid.png'):
        actions.capture_for_gt('05_07_23_ambient_color_mid.png')
    if actions.capture_for_gt('05_07_23_ambient_color_mid.png'):
        if actions.compare_with_gt('05_07_23_ambient_color_mid.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Ambient color mid comparison failed'
    else:
        assert False, 'Failed to snapshot ambient color mid'
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Verify] snapshot: 05_07_23_ambient_color_max.png'):
        actions.capture_for_gt('05_07_23_ambient_color_max.png')
    if actions.capture_for_gt('05_07_23_ambient_color_max.png'):
        if actions.compare_with_gt('05_07_23_ambient_color_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Ambient color max comparison failed'
    else:
        assert False, 'Failed to snapshot ambient color max'
    with step('[Verify] snapshot: 05_07_23_ambient_before_color_picker.png'):
        actions.capture_for_gt('05_07_23_ambient_before_color_picker.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'ic color tint n')
    with step('[Verify] snapshot: 05_07_23_ambient_color_picker_before.png'):
        actions.capture_for_gt('05_07_23_ambient_color_picker_before.png')
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0.5)
    with step('[Verify] snapshot: 05_07_23_ambient_color_picker_after.png'):
        actions.capture_for_gt('05_07_23_ambient_color_picker_after.png')
    if (not actions.compare_with_gt('05_07_23_ambient_color_picker_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Ambient color picker slider adjustment comparison failed'
    with step('[Action] tap color picker'):
        actions.tap_by_coordinates(207, 700)
    with step('[Verify] snapshot: 05_07_23_ambient_color_picker_select.png'):
        actions.capture_for_gt('05_07_23_ambient_color_picker_select.png')
    if (not actions.compare_with_gt('05_07_23_ambient_color_picker_select.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Ambient color picker color selection comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 05_07_23_ambient_color_picker_x.png'):
        actions.capture_for_gt('05_07_23_ambient_color_picker_x.png')
    if actions.compare_with_gt('05_07_23_ambient_color_picker_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Ambient color picker cancel comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'ic color tint n')
    with step('[Action] tap color picker'):
        actions.tap_by_coordinates(207, 700)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step('[Verify] snapshot: 05_07_23_ambient_color_picker_v.png'):
        actions.capture_for_gt('05_07_23_ambient_color_picker_v.png')
    if (not actions.compare_with_gt('05_07_23_ambient_color_picker_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Ambient color picker done comparison failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '0'):
        pass
    with step('[Verify] snapshot: 05_07_23_ambient_bright_def.png'):
        actions.capture_for_gt('05_07_23_ambient_bright_def.png')
    if actions.compare_with_gt('05_07_23_ambient_bright_def.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Ambient brightness default comparison failed'
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('-100', '-99', '-98', '-97', '-96', '-95')):
        pass
    with step('[Verify] snapshot: 05_07_23_ambient_bright_min.png'):
        actions.capture_for_gt('05_07_23_ambient_bright_min.png')
    if actions.compare_with_gt('05_07_23_ambient_bright_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Ambient brightness min comparison failed'
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97', '96', '95')):
        pass
    with step('[Verify] snapshot: 05_07_23_ambient_bright_max.png'):
        actions.capture_for_gt('05_07_23_ambient_bright_max.png')
    if actions.compare_with_gt('05_07_23_ambient_bright_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Ambient brightness max comparison failed'
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    with step("[Verify] test_00139 completion"):
        assert True
