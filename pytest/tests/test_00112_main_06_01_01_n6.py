import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00112_main_06_01_01_n6')
def test_00112_main_06_01_01_n6(actions: DriverActions):
    """Text bubble - new - border"""
    mode = 1
    uuid = ['4dd868e2-eb47-44a2-aa08-e0f98865d64b', '7811edf4-e1d3-4522-87dc-10cb85802dda', 'de1d5aa9-2c99-4d9b-8cef-970dc2318e2e', '5984e9da-dffa-4b5a-94b2-23bfcf17de8a', '7391e5f9-0ad4-4d33-9d81-7bb9694e2ad9', 'b12af5b6-dd85-4fe7-b701-f7fe7a223d00', 'f5949548-770b-4764-99d5-d3a8879c6e8f', 'b70fcd1a-c5af-4b78-9d29-e8b5f17de45d', 'd9000b1c-881e-47ad-9cfc-8ef52c1c069e', 'd2afb225-394e-44f2-a022-e23447d6c3c3', '87fe4c18-eb35-4ab5-8c65-2f7f84211e97', 'f969a2bf-2315-4936-8542-5466eec58ef0', '65edea72-624c-4db7-be16-d39155a6d1fc', '9de01931-30de-46c4-a234-1eb4ee65f53c', 'b5b9e20a-c32e-47ad-821c-04b1cf2c0cff', 'a60b99a8-187e-458c-8864-9c16c20346c3', 'c10f0e6d-60fa-4ad5-9154-3f19212ef34b', '4a6a86cc-aef4-411c-88a1-bb0f6622cbd2', '52701bb7-b7d2-4473-b5b3-092e4213ec91', '7e19a31a-6632-4323-8b9e-f8df9a646984', '846a6cd0-1c11-4eac-a641-ba13492b5c71', '384db1ea-725a-40f4-b55c-30cf4d54a868', '84aabfa0-3cc3-4133-ab5b-ae8e35f4f175', 'f90be441-b082-4adc-86bd-cb3fe699da14', 'dc7ac0ab-67d4-45eb-8e8a-85eb6e76a2f1', '952d688f-004b-4379-85ff-2782502d4a7e', '24c06d77-999f-49b2-9987-6677da9932f0', '6d91e8a3-b5e7-4e7e-9c39-de52c3961b5f', 'a399402d-6bc8-45b1-976d-807210b7d08a', 'dc4d398e-9516-4c33-8494-66954c8079c2', 'ba58f715-2b46-4e17-a06e-dabbd658eae3', 'a661ec51-24b9-4b56-b730-52fac143c0c8', 'd19abcaa-adf7-427d-adb8-80498f24ded7']
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
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
    with step('[Verify] snapshot: 06_01_01_no_border_panel.png'):
        actions.capture_for_gt('06_01_01_no_border_panel.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Border')
    with step('[Verify] snapshot: 06_01_01_border_default.png'):
        actions.capture_for_gt('06_01_01_border_default.png')
    if actions.compare_with_gt('06_01_01_border_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'default border panel 0 fail'
    with step('[Verify] snapshot: 06_01_01_border_default_size.png'):
        actions.capture_for_gt('06_01_01_border_default_size.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 06_01_01_close_border_panel_x.png'):
        actions.capture_for_gt('06_01_01_close_border_panel_x.png')
    if not actions.compare_with_gt('06_01_01_close_border_panel_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tap x close panel fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Border')
    with step('[Action] select_text_panel_border_color_b'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[8]')
    with step('[Verify] snapshot: 06_01_01_border1.png'):
        actions.capture_for_gt('06_01_01_border1.png')
    if actions.compare_with_gt('06_01_01_border1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'color-5 0 fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '30') == '30'):
        pass
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 06_01_01_border_size_min.png'):
        actions.capture_for_gt('06_01_01_border_size_min.png')
    if actions.compare_with_gt('06_01_01_border_size_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'border_size min 0 fail'
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 06_01_01_border_size_mid.png'):
        actions.capture_for_gt('06_01_01_border_size_mid.png')
    if actions.compare_with_gt('06_01_01_border_size_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'border_size mid 0 fail'
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 06_01_01_border_size_max.png'):
        actions.capture_for_gt('06_01_01_border_size_max.png')
    if actions.compare_with_gt('06_01_01_border_size_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'border_size max 0 fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '100') == '100'):
        pass
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Verify] snapshot: 06_01_01_border_opacity_min.png'):
        actions.capture_for_gt('06_01_01_border_opacity_min.png')
    if actions.compare_with_gt('06_01_01_border_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity min 0 fail'
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0.5')
    with step('[Verify] snapshot: 06_01_01_border_opacity_mid.png'):
        actions.capture_for_gt('06_01_01_border_opacity_mid.png')
    if actions.compare_with_gt('06_01_01_border_opacity_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity mid 0 fail'
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Verify] snapshot: 06_01_01_border_opacity_max.png'):
        actions.capture_for_gt('06_01_01_border_opacity_max.png')
    if actions.compare_with_gt('06_01_01_border_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity max 0 fail'
    from_pos = (30, 615)
    destination = (390, 615)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 615, 390, 615)
    with step('[Verify] snapshot: 06_01_01_border_before_picker.png'):
        actions.capture_for_gt('06_01_01_border_before_picker.png')
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 06_01_01_border_picker_slider.png'):
        actions.capture_for_gt('06_01_01_border_picker_slider.png')
    if actions.compare_with_gt('06_01_01_border_picker_slider.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'color picker slider 0 fail'
    with step('[Action] tap_color_picker'):
        assert actions.tap_by_coordinates(250, 620)
    with step('[Verify] snapshot: 06_01_01_border_picker_select.png'):
        actions.capture_for_gt('06_01_01_border_picker_select.png')
    if actions.compare_with_gt('06_01_01_border_picker_select.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'pick up color 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 100)
    destination = (205, 129)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 100, 205, 129)
    with step('[Verify] snapshot: 06_01_01_border_picker_dropper.png'):
        actions.capture_for_gt('06_01_01_border_picker_dropper.png')
    if actions.compare_with_gt('06_01_01_border_picker_dropper.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'dropper 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 06_01_01_border_picker_cancel.png'):
        actions.capture_for_gt('06_01_01_border_picker_cancel.png')
    if actions.compare_with_gt('06_01_01_border_picker_cancel.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'cancel picker fail'
    from_pos = (30, 615)
    destination = (390, 615)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 615, 390, 615)
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Action] tap_color_picker'):
        assert actions.tap_by_coordinates(250, 620)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step('[Verify] snapshot: 06_01_01_border_picker_done.png'):
        actions.capture_for_gt('06_01_01_border_picker_done.png')
    if actions.compare_with_gt('06_01_01_border_picker_done.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'add user color btn 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Border 2')
    with step('[Action] select_text_panel_border_color_b'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[10]')
    with step('[Verify] snapshot: 06_01_01_border2.png'):
        actions.capture_for_gt('06_01_01_border2.png')
    if actions.compare_with_gt('06_01_01_border2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'color-5 0 fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '30') == '30'):
        pass
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 06_01_01_border2_size_min.png'):
        actions.capture_for_gt('06_01_01_border2_size_min.png')
    if actions.compare_with_gt('06_01_01_border2_size_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'border2_size min 0 fail'
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 06_01_01_border2_size_mid.png'):
        actions.capture_for_gt('06_01_01_border2_size_mid.png')
    if actions.compare_with_gt('06_01_01_border2_size_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'border2_size mid 0 fail'
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_border_size_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 06_01_01_border2_size_max.png'):
        actions.capture_for_gt('06_01_01_border2_size_max.png')
    if actions.compare_with_gt('06_01_01_border2_size_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'border2_size max 0 fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '100') == '100'):
        pass
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Verify] snapshot: 06_01_01_border2_opacity_min.png'):
        actions.capture_for_gt('06_01_01_border2_opacity_min.png')
    if actions.compare_with_gt('06_01_01_border2_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity min 0 fail'
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0.5')
    with step('[Verify] snapshot: 06_01_01_border2_opacity_mid.png'):
        actions.capture_for_gt('06_01_01_border2_opacity_mid.png')
    if actions.compare_with_gt('06_01_01_border2_opacity_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity mid 0 fail'
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Action] adjust_border_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Verify] snapshot: 06_01_01_border2_opacity_max.png'):
        actions.capture_for_gt('06_01_01_border2_opacity_max.png')
    if actions.compare_with_gt('06_01_01_border2_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity max 0 fail'
    from_pos = (30, 615)
    destination = (390, 615)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 615, 390, 615)
    with step('[Verify] snapshot: 06_01_01_border2_before_picker.png'):
        actions.capture_for_gt('06_01_01_border2_before_picker.png')
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 06_01_01_border2_picker_slider.png'):
        actions.capture_for_gt('06_01_01_border2_picker_slider.png')
    if actions.compare_with_gt('06_01_01_border2_picker_slider.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'color picker slider 0 fail'
    with step('[Action] tap_color_picker'):
        assert actions.tap_by_coordinates(260, 613)
    with step('[Verify] snapshot: 06_01_01_border2_picker_select.png'):
        actions.capture_for_gt('06_01_01_border2_picker_select.png')
    if actions.compare_with_gt('06_01_01_border2_picker_select.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'pick up color 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 100)
    destination = (250, 150)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 100, 250, 150)
    with step('[Verify] snapshot: 06_01_01_border2_picker_dropper.png'):
        actions.capture_for_gt('06_01_01_border2_picker_dropper.png')
    if actions.compare_with_gt('06_01_01_border2_picker_dropper.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'dropper 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 06_01_01_border2_picker_cancel.png'):
        actions.capture_for_gt('06_01_01_border2_picker_cancel.png')
    if actions.compare_with_gt('06_01_01_border2_picker_cancel.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'cancel picker fail'
    from_pos = (30, 615)
    destination = (390, 615)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 615, 390, 615)
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] tap_color_picker'):
        assert actions.tap_by_coordinates(260, 613)
    with step('[Verify] snapshot: 06_01_01_border2_picker_done.png'):
        actions.capture_for_gt('06_01_01_border2_picker_done.png')
    if actions.compare_with_gt('06_01_01_border2_picker_done.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'add user color btn 0 fail'
    with step('[Verify] snapshot: 06_01_01_before_close_border_drag.png'):
        actions.capture_for_gt('06_01_01_before_close_border_drag.png')
    from_pos = (206, 482)
    destination = (206, 800)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 482, 206, 800)
    with step('[Verify] snapshot: 06_01_01_after_close_border_drag.png'):
        actions.capture_for_gt('06_01_01_after_close_border_drag.png')
    if not actions.compare_with_gt('06_01_01_after_close_border_drag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'drag down close panel fail'
    with step("[Verify] test_00112 completion"):
        assert True
