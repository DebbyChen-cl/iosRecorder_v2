import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00111_main_06_01_01_n5')
def test_00111_main_06_01_01_n5(actions: DriverActions):
    """Text bubble - new - color"""
    mode = 1
    uuid = ['b1e7e632-fb76-4627-8921-c595627afebe', '2cc8893f-708e-41c2-85be-c0ed29c8474a', '94c154d1-b6d3-4578-8185-bb11259dae72', '15e52dd1-dc79-4ddc-981c-6749cc8c045e', '2f6307fd-bd33-44ff-8469-6cb04365269b', '2eae3f37-79d6-4362-92ad-841474d5305a', '2e8c9047-8990-4bad-bcb1-1a5ea1ba7a9c', '97f5bd6f-7d22-4a98-b915-76f170c799c6', '64a399c7-2434-4de7-8bb1-67af41d52f16', '716c1c62-e494-4d6e-9136-f9806f451d68', 'b12947cf-6d7f-42f8-814b-ec0edfd5f04e', 'a607c248-0017-4e46-bc6d-676add8a4d6f', '7c676e0b-a24b-4aa2-820b-1f2d6d753f55', '0a281b6b-7041-4062-862f-2bf34be6dddb', '4ea75d60-2b87-40e8-ac4f-3ee94cc2ab6b', '44b3ff5b-3aa9-444c-a736-b0feb65844c9', 'b26224b6-c271-443d-8809-d5b27fe90507', 'eeb73d29-3a12-4165-b732-b8032d826155', 'dd2eb631-bdac-4544-b2d1-a44f4e76c20e', 'd294205b-0389-458c-ac1b-8884bb0b42f0', '3a2e99af-2f1e-4c9f-be4d-6e2f4e8e8809', '8c54ad2d-6d65-4a31-9664-ab9dd5679905', '91a20d33-fd47-4df2-b777-04426dbfbc84', 'eba2fa13-9241-43b7-bf5a-f401eb6a05c2', 'e69a01f3-f241-43a2-a36f-8efcc803bd5f', '7d564edc-df72-47fa-b5b4-6636fa1bf59b', '20d13911-016f-4d3a-9107-a342ab363ff0', '4c83f1ed-b11d-44af-91a9-66f49827297d', 'a0bcc00a-a21d-4f5e-97f2-37c2f0429e0c', 'e89c7e01-4cb2-4c41-9f6e-08f4498c6a13', '6f0b9412-5bba-461b-a32c-b43c9a32abf6', '111e75d1-a291-4d90-a49c-837f7a40c5ab', '706742fa-778e-451a-8a24-235dea2cd2af', '2de44abc-c55e-435a-8a77-d0b097b3f0ab', 'b96a7e09-88b3-4245-912f-41d106a66698', '7dc1157a-6af9-4cb8-84c2-7de0b41c1264', '01d7f7e8-8dcb-4380-b511-1dc9292e5dc7', '9cb2d7be-f6c6-4c0a-878c-a067d7807d3a', 'e81a80bf-ba04-40f3-b8ff-bc86efd92abd']
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
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_edit1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    from_pos = (380, 770)
    destination = (50, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text Bubble')
    with step('[Verify] snapshot: 06_01_01_no_color_panel.png'):
        actions.capture_for_gt('06_01_01_no_color_panel.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step('[Verify] snapshot: 06_01_01_color_default.png'):
        actions.capture_for_gt('06_01_01_color_default.png')
    if actions.compare_with_gt('06_01_01_color_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'default color panel 0 fail'
    with step('[Verify] snapshot: 06_01_01_color_default_size.png'):
        actions.capture_for_gt('06_01_01_color_default_size.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 06_01_01_close_color_panel_x.png'):
        actions.capture_for_gt('06_01_01_close_color_panel_x.png')
    if actions.compare_with_gt('06_01_01_close_color_panel_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tap x close panel fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step('[Action] select_text_panel_color_bubble'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[6]')
    with step('[Verify] snapshot: 06_01_01_solid_color.png'):
        actions.capture_for_gt('06_01_01_solid_color.png')
    if actions.compare_with_gt('06_01_01_solid_color.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'color-3 0 fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '100') == '100'):
        pass
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 06_01_01_solid_color_opacity_min.png'):
        actions.capture_for_gt('06_01_01_solid_color_opacity_min.png')
    if actions.compare_with_gt('06_01_01_solid_color_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity min 0 fail'
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0.5')
    with step('[Verify] snapshot: 06_01_01_solid_color_opacity_mid.png'):
        actions.capture_for_gt('06_01_01_solid_color_opacity_mid.png')
    if actions.compare_with_gt('06_01_01_solid_color_opacity_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity mid 0 fail'
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 06_01_01_solid_color_opacity_max.png'):
        actions.capture_for_gt('06_01_01_solid_color_opacity_max.png')
    if actions.compare_with_gt('06_01_01_solid_color_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity max 0 fail'
    from_pos = (30, 580)
    destination = (390, 580)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 580, 390, 580)
    with step('[Verify] snapshot: 06_01_01_solid_color_before_picker.png'):
        actions.capture_for_gt('06_01_01_solid_color_before_picker.png')
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 06_01_01_solid_color_picker_slider.png'):
        actions.capture_for_gt('06_01_01_solid_color_picker_slider.png')
    if actions.compare_with_gt('06_01_01_solid_color_picker_slider.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'color picker slider 0 fail'
    with step('[Action] tap_color_picker'):
        assert actions.tap_by_coordinates(250, 620)
    with step('[Verify] snapshot: 06_01_01_solid_color_picker_select.png'):
        actions.capture_for_gt('06_01_01_solid_color_picker_select.png')
    if actions.compare_with_gt('06_01_01_solid_color_picker_select.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'pick up color 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 100)
    destination = (219, 351)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 100, 219, 351)
    with step('[Verify] snapshot: 06_01_01_solid_color_picker_dropper.png'):
        actions.capture_for_gt('06_01_01_solid_color_picker_dropper.png')
    if actions.compare_with_gt('06_01_01_solid_color_picker_dropper.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'dropper 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 06_01_01_solid_color_picker_cancel.png'):
        actions.capture_for_gt('06_01_01_solid_color_picker_cancel.png')
    if actions.compare_with_gt('06_01_01_solid_color_picker_cancel.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'cancel picker fail'
    from_pos = (30, 580)
    destination = (390, 580)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 580, 390, 580)
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Action] tap_color_picker'):
        assert actions.tap_by_coordinates(250, 620)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step('[Verify] snapshot: 06_01_01_solid_color_picker_done.png'):
        actions.capture_for_gt('06_01_01_solid_color_picker_done.png')
    if actions.compare_with_gt('06_01_01_solid_color_picker_done.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'add user color btn 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Gradient')
    with step('[Action] select_text_panel_color_bubble'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]')
    with step('[Verify] snapshot: 06_01_01_gradient_color.png'):
        actions.capture_for_gt('06_01_01_gradient_color.png')
    if actions.compare_with_gt('06_01_01_gradient_color.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'color-2 0 fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '50') == '50'):
        pass
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '50') == '50'):
        pass
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '100') == '100'):
        pass
    with step('[Action] adjust_color_gradient_angle_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] adjust_color_gradient_angle_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 06_01_01_gradient_angle_min.png'):
        actions.capture_for_gt('06_01_01_gradient_angle_min.png')
    if actions.compare_with_gt('06_01_01_gradient_angle_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'gradient_angle min 0 fail'
    with step('[Action] adjust_color_gradient_angle_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 06_01_01_gradient_angle_max.png'):
        actions.capture_for_gt('06_01_01_gradient_angle_max.png')
    if actions.compare_with_gt('06_01_01_gradient_angle_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'gradient_angle max 0 fail'
    with step('[Action] adjust_color_gradient_angle_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 06_01_01_gradient_angle_mid.png'):
        actions.capture_for_gt('06_01_01_gradient_angle_mid.png')
    if actions.compare_with_gt('06_01_01_gradient_angle_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'gradient_angle mid 0 fail'
    with step('[Action] adjust_color_gradient_transition_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Action] adjust_color_gradient_transition_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Verify] snapshot: 06_01_01_gradient_transition_min.png'):
        actions.capture_for_gt('06_01_01_gradient_transition_min.png')
    if actions.compare_with_gt('06_01_01_gradient_transition_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'gradient_transition min 0 fail'
    with step('[Action] adjust_color_gradient_transition_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Verify] snapshot: 06_01_01_gradient_transition_max.png'):
        actions.capture_for_gt('06_01_01_gradient_transition_max.png')
    if actions.compare_with_gt('06_01_01_gradient_transition_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'gradient_transition max 0 fail'
    with step('[Action] adjust_color_gradient_transition_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0.5')
    with step('[Verify] snapshot: 06_01_01_gradient_transition_mid.png'):
        actions.capture_for_gt('06_01_01_gradient_transition_mid.png')
    if actions.compare_with_gt('06_01_01_gradient_transition_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'gradient_transition mid 0 fail'
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '1')
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0')
    with step('[Verify] snapshot: 06_01_01_gradient_opacity_min.png'):
        actions.capture_for_gt('06_01_01_gradient_opacity_min.png')
    if actions.compare_with_gt('06_01_01_gradient_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'gradient_opacity min 0 fail'
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0.5')
    with step('[Verify] snapshot: 06_01_01_gradient_opacity_mid.png'):
        actions.capture_for_gt('06_01_01_gradient_opacity_mid.png')
    if actions.compare_with_gt('06_01_01_gradient_opacity_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'gradient_opacity mid 0 fail'
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0')
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '1')
    with step('[Verify] snapshot: 06_01_01_gradient_opacity_max.png'):
        actions.capture_for_gt('06_01_01_gradient_opacity_max.png')
    if actions.compare_with_gt('06_01_01_gradient_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'gradient_opacity max 0 fail'
    from_pos = (30, 580)
    destination = (390, 580)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 580, 390, 580)
    with step('[Verify] snapshot: 06_01_01_gradient_color_before_picker.png'):
        actions.capture_for_gt('06_01_01_gradient_color_before_picker.png')
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 06_01_01_gradient_color_picker_slider1.png'):
        actions.capture_for_gt('06_01_01_gradient_color_picker_slider1.png')
    if actions.compare_with_gt('06_01_01_gradient_color_picker_slider1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'color 1 picker slider 0 fail'
    with step('[Action] tap_color_picker'):
        assert actions.tap_by_coordinates(250, 720)
    with step('[Verify] snapshot: 06_01_01_gradient_color_picker_select1.png'):
        actions.capture_for_gt('06_01_01_gradient_color_picker_select1.png')
    if actions.compare_with_gt('06_01_01_gradient_color_picker_select1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'pick up color 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 100)
    destination = (205, 229)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 100, 205, 229)
    with step('[Verify] snapshot: 06_01_01_gradient_color_picker_dropper1.png'):
        actions.capture_for_gt('06_01_01_gradient_color_picker_dropper1.png')
    if actions.compare_with_gt('06_01_01_gradient_color_picker_dropper1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'dropper 0 fail'
    with step('[Action] tap_text_gradient_color2_picker_btn_b'):
        assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeButton[2]')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 06_01_01_gradient_color_picker_slider2.png'):
        actions.capture_for_gt('06_01_01_gradient_color_picker_slider2.png')
    if actions.compare_with_gt('06_01_01_gradient_color_picker_slider2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'color 2 picker slider 0 fail'
    with step('[Action] tap_color_picker'):
        assert actions.tap_by_coordinates(331, 713)
    with step('[Verify] snapshot: 06_01_01_gradient_color_picker_select2.png'):
        actions.capture_for_gt('06_01_01_gradient_color_picker_select2.png')
    if actions.compare_with_gt('06_01_01_gradient_color_picker_select2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'pick up color 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 110)
    destination = (150, 150)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 110, 150, 150)
    with step('[Verify] snapshot: 06_01_01_gradient_color_picker_dropper2.png'):
        actions.capture_for_gt('06_01_01_gradient_color_picker_dropper2.png')
    if actions.compare_with_gt('06_01_01_gradient_color_picker_dropper2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'dropper 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 06_01_01_gradient_color_picker_cancel.png'):
        actions.capture_for_gt('06_01_01_gradient_color_picker_cancel.png')
    if actions.compare_with_gt('06_01_01_gradient_color_picker_cancel.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'cancel picker fail'
    from_pos = (30, 580)
    destination = (390, 580)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 580, 390, 580)
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Action] tap_color_picker'):
        assert actions.tap_by_coordinates(250, 720)
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'currentEndingColorView')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] tap_color_picker'):
        assert actions.tap_by_coordinates(331, 713)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step('[Verify] snapshot: 06_01_01_gradient_color_picker_done.png'):
        actions.capture_for_gt('06_01_01_gradient_color_picker_done.png')
    if actions.compare_with_gt('06_01_01_gradient_color_picker_done.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'add user color btn 0 fail'
    with step('[Verify] snapshot: 06_01_01_before_close_color_drag.png'):
        actions.capture_for_gt('06_01_01_before_close_color_drag.png')
    from_pos = (206, 482)
    destination = (206, 800)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 482, 206, 800)
    with step('[Verify] snapshot: 06_01_01_after_close_color_drag.png'):
        actions.capture_for_gt('06_01_01_after_close_color_drag.png')
    if not actions.compare_with_gt('06_01_01_after_close_color_drag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'drag down close panel fail'
    with step("[Verify] test_00111 completion"):
        assert True
