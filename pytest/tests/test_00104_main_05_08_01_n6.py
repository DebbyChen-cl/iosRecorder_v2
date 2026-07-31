import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00104_main_05_08_01_n6')
def test_00104_main_05_08_01_n6(actions: DriverActions):
    """Text tools - text new - border"""
    mode = 1
    uuid = ['bf43b766-596d-4d50-8d17-b9d1df28d4e9', 'ef73b271-6052-4aff-8e61-7f654e57848e', 'c8916dae-f933-491e-96d8-7c2fb7aee519', '3898629e-4486-4305-ada2-f95f9f8c89aa', 'b79db1ff-c9a1-40f5-a051-203a54544c92', 'b5dcd44f-3248-4487-92c1-7309a22dca26', 'f3aa0ac5-8933-4bbe-8e25-adda7c17f0b3', 'a135b970-c3f4-4e91-91f5-d23de7abaf06', '132d2285-00e0-4a83-b1b2-ac60a957d03e', 'bfeee182-ed0e-4843-a086-01b4557f702c', '95a58478-96f9-4c85-be10-cbc9c382163f', '781ca63c-4c5f-41c5-82bb-6cb8f7604c25', '7d68d490-d17c-4dd8-98ac-09b20ea238d4', 'acab6f8c-3413-4d11-9204-f8765d2bdc26', '9e97ae4d-f06d-474c-9808-20ff21c02858', '60ba5370-4a3d-490d-a0a2-7b004de35135', 'c623a444-e60e-4bb8-9e84-a0672e1d7f55', 'f6dc5f96-c041-499c-809e-40f0703a45a2', '4cccaa36-f81d-4dd1-9fe1-a6430d75c04c', '7dfa447d-e32f-4173-a806-ec3e413bbca7', '2580790c-b60e-4d14-8dcd-2cd02594d18a', '0a51c690-0b17-4ee7-87f3-7800cc005e57', 'c4e762be-78b0-4471-996f-82eb108623f4', 'f86e5047-bbad-4e38-a47c-2881f100e09f', '5565edec-62d3-4e09-b6df-db8cc7657f04', '421cf8a6-16ab-429b-ac7e-68ab0fdce7f1', '405f6b80-e33c-4f12-9721-461545d0066a', 'bd2823cb-411e-4990-a52c-ebb8cbaabafd', '5af623ef-fade-41fe-9d69-e5d7adb7ca80', 'fdb19acf-9c70-4392-a59a-c78f7bdcefc2', 'c4663ddc-5bbd-4fef-a200-e393d39dbd5c', '5d5b8d4f-7c12-4a2c-bb37-1c2ae92a7636', 'b5479cca-bfba-4d62-bf5e-666d0e9aa1a0']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit')
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
    from_pos = (380, 770)
    destination = (50, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 50, 770)
    if actions.is_element_present(AppiumBy.NAME, 'xpromo btn close n', timeout=2):
        with step('[Action] tap_close_xpromo_btn'):
            actions.tap_by_locator(AppiumBy.NAME, 'xpromo btn close n')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Verify] snapshot: 05_08_01_no_border_panel.png'):
        actions.capture_for_gt('05_08_01_no_border_panel.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Border')
    with step('[Verify] snapshot: 05_08_01_border_default.png'):
        actions.capture_for_gt('05_08_01_border_default.png')
    if actions.compare_with_gt('05_08_01_border_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border default fail'
    with step('[Verify] snapshot: 05_08_01_border_default_size.png'):
        actions.capture_for_gt('05_08_01_border_default_size.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 05_08_01_close_border_panel_x.png'):
        actions.capture_for_gt('05_08_01_close_border_panel_x.png')
    if not actions.compare_with_gt('05_08_01_close_border_panel_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Close border panel x comparison fail'
    with step('[Action] focus_text'):
        actions.tap_by_coordinates(205, 455)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Border')
    with step('[Action] select_text_panel_border_color'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[8]')
    with step('[Verify] snapshot: 05_08_01_border1.png'):
        actions.capture_for_gt('05_08_01_border1.png')
    if actions.compare_with_gt('05_08_01_border1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border1 fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '30') == '30'):
        pass
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 05_08_01_border_size_min.png'):
        actions.capture_for_gt('05_08_01_border_size_min.png')
    if actions.compare_with_gt('05_08_01_border_size_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border size min fail'
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 05_08_01_border_size_mid.png'):
        actions.capture_for_gt('05_08_01_border_size_mid.png')
    if actions.compare_with_gt('05_08_01_border_size_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border size mid fail'
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 05_08_01_border_size_max.png'):
        actions.capture_for_gt('05_08_01_border_size_max.png')
    if actions.compare_with_gt('05_08_01_border_size_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border size max fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '100'):
        pass
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Verify] snapshot: 05_08_01_border_opacity_min.png'):
        actions.capture_for_gt('05_08_01_border_opacity_min.png')
    if actions.compare_with_gt('05_08_01_border_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border opacity min fail'
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0.5')
    with step('[Verify] snapshot: 05_08_01_border_opacity_mid.png'):
        actions.capture_for_gt('05_08_01_border_opacity_mid.png')
    if actions.compare_with_gt('05_08_01_border_opacity_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border opacity mid fail'
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Verify] snapshot: 05_08_01_border_opacity_max.png'):
        actions.capture_for_gt('05_08_01_border_opacity_max.png')
    if actions.compare_with_gt('05_08_01_border_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border opacity max fail'
    from_pos = (30, 650)
    destination = (390, 650)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 650, 390, 650)
    with step('[Verify] snapshot: 05_08_01_border_before_picker.png'):
        actions.capture_for_gt('05_08_01_border_before_picker.png')
    from_pos = (30, 658)
    destination = (390, 680)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 658, 390, 680)
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_08_01_border_enter_color_picker.png'):
        actions.capture_for_gt('05_08_01_border_enter_color_picker.png')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 05_08_01_border_picker_slider.png'):
        actions.capture_for_gt('05_08_01_border_picker_slider.png')
    if actions.compare_with_gt('05_08_01_border_picker_slider.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border picker slider fail'
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(250, 720)
    with step('[Verify] snapshot: 05_08_01_border_picker_select.png'):
        actions.capture_for_gt('05_08_01_border_picker_select.png')
    if actions.compare_with_gt('05_08_01_border_picker_select.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border picker select fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 100)
    destination = (205, 229)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 100, 205, 229)
    with step('[Verify] snapshot: 05_08_01_border_picker_dropper.png'):
        actions.capture_for_gt('05_08_01_border_picker_dropper.png')
    if actions.compare_with_gt('05_08_01_border_picker_dropper.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border picker dropper fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 05_08_01_border_picker_cancel.png'):
        actions.capture_for_gt('05_08_01_border_picker_cancel.png')
    if actions.compare_with_gt('05_08_01_border_picker_cancel.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border picker cancel fail'
    from_pos = (30, 650)
    destination = (390, 650)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 650, 390, 650)
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(250, 720)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step('[Verify] snapshot: 05_08_01_border_picker_done.png'):
        actions.capture_for_gt('05_08_01_border_picker_done.png')
    if actions.compare_with_gt('05_08_01_border_picker_done.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border picker done fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Border 2')
    with step('[Action] select_text_panel_border_color'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[10]')
    with step('[Verify] snapshot: 05_08_01_border2.png'):
        actions.capture_for_gt('05_08_01_border2.png')
    if actions.compare_with_gt('05_08_01_border2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border2 fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '30') == '30'):
        pass
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 05_08_01_border2_size_min.png'):
        actions.capture_for_gt('05_08_01_border2_size_min.png')
    if actions.compare_with_gt('05_08_01_border2_size_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border2 size min fail'
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 05_08_01_border2_size_mid.png'):
        actions.capture_for_gt('05_08_01_border2_size_mid.png')
    if actions.compare_with_gt('05_08_01_border2_size_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border2 size mid fail'
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 05_08_01_border2_size_max.png'):
        actions.capture_for_gt('05_08_01_border2_size_max.png')
    if actions.compare_with_gt('05_08_01_border2_size_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border2 size max fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '100'):
        pass
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Verify] snapshot: 05_08_01_border2_opacity_min.png'):
        actions.capture_for_gt('05_08_01_border2_opacity_min.png')
    if actions.compare_with_gt('05_08_01_border2_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border2 opacity min fail'
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0.5')
    with step('[Verify] snapshot: 05_08_01_border2_opacity_mid.png'):
        actions.capture_for_gt('05_08_01_border2_opacity_mid.png')
    if actions.compare_with_gt('05_08_01_border2_opacity_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border2 opacity mid fail'
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Verify] snapshot: 05_08_01_border2_opacity_max.png'):
        actions.capture_for_gt('05_08_01_border2_opacity_max.png')
    if actions.compare_with_gt('05_08_01_border2_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border2 opacity max fail'
    from_pos = (30, 680)
    destination = (390, 680)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 680, 390, 680)
    with step('[Verify] snapshot: 05_08_01_border2_before_picker.png'):
        actions.capture_for_gt('05_08_01_border2_before_picker.png')
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_08_01_border_enter_color_picker2.png'):
        actions.capture_for_gt('05_08_01_border_enter_color_picker2.png')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 05_08_01_border2_picker_slider.png'):
        actions.capture_for_gt('05_08_01_border2_picker_slider.png')
    if actions.compare_with_gt('05_08_01_border2_picker_slider.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border2 picker slider fail'
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(331, 600)
    with step('[Verify] snapshot: 05_08_01_border2_picker_select.png'):
        actions.capture_for_gt('05_08_01_border2_picker_select.png')
    if actions.compare_with_gt('05_08_01_border2_picker_select.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border2 picker select fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 100)
    destination = (250, 150)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 100, 250, 150)
    with step('[Verify] snapshot: 05_08_01_border2_picker_dropper.png'):
        actions.capture_for_gt('05_08_01_border2_picker_dropper.png')
    if actions.compare_with_gt('05_08_01_border2_picker_dropper.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border2 picker dropper fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 05_08_01_border2_picker_cancel.png'):
        actions.capture_for_gt('05_08_01_border2_picker_cancel.png')
    if actions.compare_with_gt('05_08_01_border2_picker_cancel.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border2 picker cancel fail'
    from_pos = (30, 680)
    destination = (390, 680)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 680, 390, 680)
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_08_01_border_enter_color_picker3.png'):
        actions.capture_for_gt('05_08_01_border_enter_color_picker3.png')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(331, 600)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step('[Verify] snapshot: 05_08_01_border2_picker_done.png'):
        actions.capture_for_gt('05_08_01_border2_picker_done.png')
    if actions.compare_with_gt('05_08_01_border2_picker_done.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare border2 picker done fail'
    with step('[Verify] snapshot: 05_08_01_before_close_border_drag.png'):
        actions.capture_for_gt('05_08_01_before_close_border_drag.png')
    from_pos = (206, 476)
    destination = (206, 800)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 476, 206, 800)
    with step('[Verify] snapshot: 05_08_01_after_close_border_drag.png'):
        actions.capture_for_gt('05_08_01_after_close_border_drag.png')
    if not actions.compare_with_gt('05_08_01_after_close_border_drag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare drag down close border panel fail'
    with step("[Verify] test_00104 completion"):
        assert True
