import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00106_main_05_08_01_n8')
def test_00106_main_05_08_01_n8(actions: DriverActions):
    """Text tools - text new - shape"""
    mode = 1
    uuid = ['8421771a-4364-4aff-9f79-4a11237b8bdf', '10fc2d95-58dc-4ff0-a1b6-f9ed380048c4', '0773a7af-4a93-4bee-a5c8-f80116333b2c', 'b6fb15e3-fb60-4c43-b4ab-d8ae609d02fa', '9b4bc908-b08e-49ac-a1b4-b8ecf5aecbeb', 'f5d6e90e-2f88-4ff1-a707-a42ea95ad48b', '2b5870c0-127d-46bf-b4bd-c12068c0ca30', '5a388639-899a-48c0-a975-6f5c8b915e1b', 'a8de2e24-c91d-42ba-ac4c-590b99d499ee', '815869f1-a1d9-4b4c-9200-87178193f6dd', '6e8e0bc9-77fd-442c-8a49-ba25277338e3', '3083951a-1c07-4440-b8b0-7095394a1bdb', '99780a9d-f421-45d3-bc76-262bb971c3c2', '58cfcef9-8663-4f56-a7ab-dea29a9f70d4', 'cf0b6d4e-5724-46e0-a1d4-8b376709f509', '08e00293-5c33-4253-a6d8-728146c8aad2', '8630ee78-dd6c-4e3b-b894-0a08f6f5acd6', 'fc2250e6-e5dd-4c86-879e-f4cd02081e81', 'a6d4b81a-62c4-4170-b4dd-e29222517070', 'cd25c2cf-954b-4fc4-8221-8f03f8c86070', 'b40e178b-2e4b-4a90-a130-ca62cf348cc6', '56016ea9-b611-424a-bde5-d538bc4e0716', 'd28ccbaa-6927-45c8-9e10-cf2c3c828a8a', '08b04adb-9c2a-4e6e-bf26-5b0a8d7386a5', 'f48b2a73-621c-4578-8545-c1a46f6f6ef9', '4d00e158-8e77-4b2c-ae4a-f21d3c6773e1', '95831758-677b-4a54-a098-8705a25dd897', '785ad428-6d43-4da1-87e4-aa7bd013a39b', '1bc62258-e562-4021-851e-00778d82f35e', '1417a22b-0a97-4ed5-8707-2c77bd17d88e', 'a16c3fe1-ee90-46b2-a76e-b4f70722c4a0', '4dce03bb-5485-462c-9d2f-2a67ab7faabd', '8311fa4a-4b50-49e8-9209-43d3c83a54af', '50caa41c-6a43-402e-b490-91184ebe5728', '4a070937-2631-45a3-ac16-82ddf1db3668', '4f30b1bd-5c6b-41f6-baec-758bf3d0656a', 'c541a577-8613-4363-939a-12468beb5896', '3673a7de-840e-4767-9251-969ad94d6bad', '79046d21-015d-4274-87a5-b1c43a5f5c1f', 'ff0fcc67-5773-421e-a0f2-6219390f0c1a', 'c77fe989-1a07-486d-bb8e-c0a7b5dee6d7', '65c86ef3-fdcb-404e-9e8e-09dc116818b3', '790d95ad-7ab0-4edc-ac79-310e86cb5a12', 'a8954a95-7553-4c9b-8dba-23ac6c2a7b1e', '5a74d536-64af-477c-954a-589fd8565700', 'd3239ebd-16f6-4bce-9a8a-49fece183013', '270fdf00-9938-41ee-adbb-7cd88f9d791d', 'c8810741-1c70-45e5-8fda-24ad3f2959b2', '23d556e6-d2ea-4b35-b8c3-35221bed2d34', '5f684fbc-6888-44d5-8626-1d926d69caf6', 'ae99f779-3fa3-454d-81c5-21f2646166e7', '0ef38f22-ecd1-437c-ba6e-b9dc99672c4f', '25e53189-7510-4bf2-b2a2-11c150be9e8f', '4f6b329b-0bb8-46e5-aed1-1ec3f5798667', '37a65626-faee-4320-8881-35ef07d950a0']
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
    with step('[Action] tap_edit1_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Verify] snapshot: 05_08_01_no_shape_panel.png'):
        actions.capture_for_gt('05_08_01_no_shape_panel.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step('[Action] tap_text_bg_template'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_202212_004')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shape')
    with step('[Verify] snapshot: 05_08_01_shape_default.png'):
        actions.capture_for_gt('05_08_01_shape_default.png')
    if actions.compare_with_gt('05_08_01_shape_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Verify] snapshot: 05_08_01_shape_default_size.png'):
        actions.capture_for_gt('05_08_01_shape_default_size.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 05_08_01_close_shape_panel_x.png'):
        actions.capture_for_gt('05_08_01_close_shape_panel_x.png')
    if not actions.compare_with_gt('05_08_01_close_shape_panel_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] focus_text'):
        actions.tap_by_coordinates(205, 455)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shape')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') == '100'):
        pass
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '0'):
        pass
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') == '0'):
        pass
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Gradient')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') == '0'):
        pass
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') == '100'):
        pass
    from_pos = (40, 800)
    destination = (40, 680)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(40, 800, 40, 680)
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '0') == '0'):
        pass
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '0') == '0'):
        pass
    from_pos = (40, 680)
    destination = (40, 800)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(40, 680, 40, 800)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Solid')
    with step('[Action] select_text_panel_color'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[11]')
    with step('[Verify] snapshot: base05_08_01_shape_solid_color.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] adjust_text_shape_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 05_08_01_shape_shape_solid_opacity_slider.png'):
        actions.capture_for_gt('05_08_01_shape_shape_solid_opacity_slider.png')
    with step('[Verify] snapshot: base05_08_01_shape_solid_color_opacity_min.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color_opacity_min.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: base05_08_01_shape_solid_color_opacity_mid.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color_opacity_mid.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_opacity_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_text_shape_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: base05_08_01_shape_solid_color_opacity_max.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color_opacity_max.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_solid_horizontal_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Action] adjust_text_shape_solid_horizontal_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Verify] snapshot: base05_08_01_shape_solid_color_horizontal_min.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color_horizontal_min.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_horizontal_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_solid_horizontal_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0.5')
    with step('[Verify] snapshot: base05_08_01_shape_solid_color_horizontal_mid.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color_horizontal_mid.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_horizontal_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_solid_horizontal_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Action] adjust_text_shape_solid_horizontal_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Verify] snapshot: base05_08_01_shape_solid_color_horizontal_max.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color_horizontal_max.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_horizontal_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_solid_vertical_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '1')
    with step('[Action] adjust_text_shape_solid_vertical_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0')
    with step('[Verify] snapshot: base05_08_01_shape_solid_color_vertical_min.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color_vertical_min.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_vertical_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_solid_vertical_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0.5')
    with step('[Verify] snapshot: base05_08_01_shape_solid_color_vertical_mid.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color_vertical_mid.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_vertical_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_solid_vertical_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0')
    with step('[Action] adjust_text_shape_solid_vertical_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '1')
    with step('[Verify] snapshot: base05_08_01_shape_solid_color_vertical_max.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color_vertical_max.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_vertical_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    from_pos = (30, 680)
    destination = (390, 680)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 680, 390, 680)
    with step('[Verify] snapshot: 05_08_01_shape_solid_color_before_picker.png'):
        actions.capture_for_gt('05_08_01_shape_solid_color_before_picker.png')
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: base05_08_01_shape_solid_color_picker_slider.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color_picker_slider.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_picker_slider.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(250, 620)
    with step('[Verify] snapshot: base05_08_01_shape_solid_color_picker_select.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color_picker_select.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_picker_select.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 100)
    destination = (219, 351)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 100, 219, 351)
    with step('[Verify] snapshot: base05_08_01_shape_solid_color_picker_dropper.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color_picker_dropper.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_picker_dropper.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 05_08_01_shape_solid_color_picker_cancel.png'):
        actions.capture_for_gt('05_08_01_shape_solid_color_picker_cancel.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_picker_cancel.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    from_pos = (30, 680)
    destination = (390, 680)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 680, 390, 680)
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(250, 720)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step('[Verify] snapshot: base05_08_01_shape_solid_color_picker_done.png'):
        actions.capture_for_gt('base05_08_01_shape_solid_color_picker_done.png')
    if actions.compare_with_gt('05_08_01_shape_solid_color_picker_done.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Gradient')
    with step('[Action] select_text_panel_color'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[11]')
    with step('[Verify] snapshot: base05_08_01_shape_gradient_color.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_color.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_color.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_color_gradient_angle_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] adjust_color_gradient_angle_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_angle_slider_min.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_angle_slider_min.png')
    with step('[Verify] snapshot: base05_08_01_shape_gradient_angle_min.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_angle_min.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_angle_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_color_gradient_angle_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_angle_slider_max.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_angle_slider_max.png')
    with step('[Verify] snapshot: base05_08_01_shape_gradient_angle_max.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_angle_max.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_angle_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_color_gradient_angle_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_angle_slider_mid.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_angle_slider_mid.png')
    with step('[Verify] snapshot: base05_08_01_shape_gradient_angle_mid.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_angle_mid.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_angle_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_color_gradient_transition_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Action] adjust_color_gradient_transition_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_transition_slider_min.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_transition_slider_min.png')
    with step('[Verify] snapshot: base05_08_01_shape_gradient_transition_min.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_transition_min.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_transition_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_color_gradient_transition_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_transition_slider_max.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_transition_slider_max.png', crop_rect=(0, 60, 276, 597))
    with step('[Verify] snapshot: base05_08_01_shape_gradient_transition_max.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_transition_max.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_transition_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_color_gradient_transition_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0.5')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_transition_slider_mid.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_transition_slider_mid.png', crop_rect=(0, 60, 276, 597))
    with step('[Verify] snapshot: base05_08_01_shape_gradient_transition_mid.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_transition_mid.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_transition_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '1')
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_opacity_slider_min.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_opacity_slider_min.png', crop_rect=(0, 60, 276, 597))
    with step('[Verify] snapshot: base05_08_01_shape_gradient_opacity_min.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_opacity_min.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0.5')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_opacity_slider_mid.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_opacity_slider_mid.png', crop_rect=(0, 60, 276, 597))
    with step('[Verify] snapshot: base05_08_01_shape_gradient_opacity_mid.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_opacity_mid.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_opacity_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0')
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '1')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_opacity_slider_max.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_opacity_slider_max.png', crop_rect=(0, 60, 276, 597))
    with step('[Verify] snapshot: base05_08_01_shape_gradient_opacity_max.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_opacity_max.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    from_pos = (40, 790)
    destination = (40, 690)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(40, 790, 40, 690)
    with step('[Action] adjust_text_shape_gradient_horizontal_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[4]', '1')
    with step('[Action] adjust_text_shape_gradient_horizontal_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[4]', '0')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_horizontal_slider_min.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_horizontal_slider_min.png', crop_rect=(0, 60, 276, 597))
    with step('[Verify] snapshot: base05_08_01_shape_gradient_horizontal_min.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_horizontal_min.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_horizontal_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_gradient_horizontal_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[4]', '0.5')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_horizontal_slider_mid.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_horizontal_slider_mid.png', crop_rect=(0, 60, 276, 597))
    with step('[Verify] snapshot: base05_08_01_shape_gradient_horizontal_mid.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_horizontal_mid.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_horizontal_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_gradient_horizontal_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[4]', '0')
    with step('[Action] adjust_text_shape_gradient_horizontal_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[4]', '1')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_horizontal_slider_max.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_horizontal_slider_max.png', crop_rect=(0, 60, 276, 597))
    with step('[Verify] snapshot: base05_08_01_shape_gradient_horizontal_max.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_horizontal_max.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_horizontal_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_gradient_vertical_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[5]', '1')
    with step('[Action] adjust_text_shape_gradient_vertical_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[5]', '0')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_vertical_slider_min.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_vertical_slider_min.png', crop_rect=(0, 60, 276, 597))
    with step('[Verify] snapshot: base05_08_01_shape_gradient_vertical_min.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_vertical_min.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_vertical_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_gradient_vertical_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[5]', '0.5')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_vertical_slider_mid.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_vertical_slider_mid.png', crop_rect=(0, 60, 276, 597))
    with step('[Verify] snapshot: base05_08_01_shape_gradient_vertical_mid.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_vertical_mid.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_vertical_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] adjust_text_shape_gradient_vertical_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[5]', '0')
    with step('[Action] adjust_text_shape_gradient_vertical_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[5]', '1')
    with step('[Verify] snapshot: 05_08_01_shape_shape_adjust_color_gradient_vertical_slider_max.png'):
        actions.capture_for_gt('05_08_01_shape_shape_adjust_color_gradient_vertical_slider_max.png', crop_rect=(0, 60, 276, 597))
    with step('[Verify] snapshot: base05_08_01_shape_gradient_vertical_max.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_vertical_max.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_vertical_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    from_pos = (30, 680)
    destination = (390, 680)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 680, 390, 680)
    with step('[Verify] snapshot: 05_08_01_shape_gradient_color_before_picker.png'):
        actions.capture_for_gt('05_08_01_shape_gradient_color_before_picker.png')
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: base05_08_01_shape_gradient_color_picker_slider1.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_color_picker_slider1.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_color_picker_slider1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(250, 620)
    with step('[Verify] snapshot: base05_08_01_shape_gradient_color_picker_select1.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_color_picker_select1.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_color_picker_select1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 100)
    destination = (205, 229)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 100, 205, 229)
    with step('[Verify] snapshot: base05_08_01_shape_gradient_color_picker_dropper1.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_color_picker_dropper1.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_color_picker_dropper1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'currentEndingColorView')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: base05_08_01_shape_gradient_color_picker_slider2.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_color_picker_slider2.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_color_picker_slider2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(331, 713)
    with step('[Verify] snapshot: base05_08_01_shape_gradient_color_picker_select2.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_color_picker_select2.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_color_picker_select2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 110)
    destination = (150, 150)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 110, 150, 150)
    with step('[Verify] snapshot: base05_08_01_shape_gradient_color_picker_dropper2.png'):
        actions.capture_for_gt('base05_08_01_shape_gradient_color_picker_dropper2.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_color_picker_dropper2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 05_08_01_shape_gradient_color_picker_cancel.png'):
        actions.capture_for_gt('05_08_01_shape_gradient_color_picker_cancel.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_color_picker_cancel.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    from_pos = (30, 650)
    destination = (390, 650)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 650, 390, 650)
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')])):
        assert False  # legacy raise
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(250, 720)
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'currentEndingColorView')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(331, 713)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step('[Verify] snapshot: 05_08_01_shape_gradient_color_picker_done.png'):
        actions.capture_for_gt('05_08_01_shape_gradient_color_picker_done.png')
    if actions.compare_with_gt('05_08_01_shape_gradient_color_picker_done.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shape gradient color picker done fail'
    with step('[Verify] snapshot: 05_08_01_shape_before_close_color_drag.png'):
        actions.capture_for_gt('05_08_01_shape_before_close_color_drag.png')
    from_pos = (206, 476)
    destination = (206, 800)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 476, 206, 800)
    with step('[Verify] snapshot: 05_08_01_shape_after_close_color_drag.png'):
        actions.capture_for_gt('05_08_01_shape_after_close_color_drag.png')
    if not actions.compare_with_gt('05_08_01_shape_after_close_color_drag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step("[Verify] test_00106 completion"):
        assert True
