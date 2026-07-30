import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00105_main_05_08_01_n7')
def test_00105_main_05_08_01_n7(actions: DriverActions):
    """Text tools - text new - shadow"""
    mode = 1
    uuid = ['7485c8c9-93d7-44d1-b837-b45a3d7b94ad', '1207624e-c69f-11ec-9d64-0242ac120002', '792872c5-ab7d-43b4-a69d-f939a8695f9f', 'a237a954-0496-40bd-a05e-2acaabf0dd27', 'd8a71145-5538-4017-96b5-0866bc7a2cfb', '34e9d838-afdc-46e5-b1ce-06473da8efb2', '492c7e26-d1c7-44fb-a65d-61feaa1ca1a5', '68dbab46-d472-45ef-a264-9386e2802429', 'a9dfac3a-759b-465f-9415-a0112bc79507', 'c376e01e-f9a9-4afb-bdf5-08b9be08b6b5', 'da14fd5d-27a7-43e8-b2e8-5ca17505072d', '94297867-0330-4527-9c70-83675b7773c3', '1cf67459-d75e-42cd-9870-1a2f45be8172', 'f763fed5-adc3-48ff-b830-17e1096d2fc0', '139130c5-52c0-4c7f-8fd9-393ad8c5318b', 'bc6cd4ca-7ddf-48c0-9279-2fb52bf0dda5', 'd5d7c0da-04f7-4d53-81ba-a5c978fc8113', 'c61db510-7196-4069-817f-676f5208bd4a', 'f9bb5157-27bd-45c3-a099-3651d1dc2dca', '17083f0c-897c-4c26-8ab0-cf218096e6b9', '18c18833-5027-43e1-9e51-37f91fc7448f', 'ffe756c3-3e95-4618-9927-b725743b92ea', 'd9137aa5-c058-4e03-9039-cdf6ddd7d4ac', '6f82fe07-c57f-4aa9-bfc8-0b53dec403e5']
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
    from_pos = (380, 770)
    destination = (50, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    from_pos = (284, 277)
    destination = (308, 308)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(284, 277, 308, 308)
    with step('[Verify] snapshot: 05_08_01_no_shadow_panel.png'):
        actions.capture_for_gt('05_08_01_no_shadow_panel.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')
    with step('[Verify] snapshot: 05_08_01_shadow_default.png'):
        actions.capture_for_gt('05_08_01_shadow_default.png')
    if actions.compare_with_gt('05_08_01_shadow_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow default fail'
    with step('[Verify] snapshot: 05_08_01_shadow_default_size.png'):
        actions.capture_for_gt('05_08_01_shadow_default_size.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 05_08_01_close_shadow_panel_x.png'):
        actions.capture_for_gt('05_08_01_close_shadow_panel_x.png')
    if not actions.compare_with_gt('05_08_01_close_shadow_panel_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Close shadow panel x comparison fail'
    with step('[Action] focus_text'):
        actions.tap_by_coordinates(205, 455)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')
    with step('[Action] select_text_panel_shadow_color'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[9]')
    with step('[Verify] snapshot: 05_08_01_shadow.png'):
        actions.capture_for_gt('05_08_01_shadow.png')
    if actions.compare_with_gt('05_08_01_shadow.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '30') == '30'):
        pass
    with step('[Action] adjust_shadow_blur_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] adjust_shadow_blur_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 05_08_01_shadow_blur_min.png'):
        actions.capture_for_gt('05_08_01_shadow_blur_min.png')
    if actions.compare_with_gt('05_08_01_shadow_blur_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow blur min fail'
    with step('[Action] adjust_shadow_blur_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 05_08_01_shadow_blur_mid.png'):
        actions.capture_for_gt('05_08_01_shadow_blur_mid.png')
    if actions.compare_with_gt('05_08_01_shadow_blur_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow blur mid fail'
    with step('[Action] adjust_shadow_blur_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_shadow_blur_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 05_08_01_shadow_blur_max.png'):
        actions.capture_for_gt('05_08_01_shadow_blur_max.png')
    if actions.compare_with_gt('05_08_01_shadow_blur_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow blur max fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '30'):
        pass
    with step('[Action] adjust_shadow_distance_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Action] adjust_shadow_distance_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Verify] snapshot: 05_08_01_shadow_distance_min.png'):
        actions.capture_for_gt('05_08_01_shadow_distance_min.png')
    if actions.compare_with_gt('05_08_01_shadow_distance_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow distance min fail'
    with step('[Action] adjust_shadow_distance_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0.5')
    with step('[Verify] snapshot: 05_08_01_shadow_distance_mid.png'):
        actions.capture_for_gt('05_08_01_shadow_distance_mid.png')
    if actions.compare_with_gt('05_08_01_shadow_distance_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow distance mid fail'
    with step('[Action] adjust_shadow_distance_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Action] adjust_shadow_distance_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Verify] snapshot: 05_08_01_shadow_distance_max.png'):
        actions.capture_for_gt('05_08_01_shadow_distance_max.png')
    if actions.compare_with_gt('05_08_01_shadow_distance_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow distance max fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '100') == '100'):
        pass
    with step('[Action] adjust_shadow_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '1')
    with step('[Action] adjust_shadow_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0')
    with step('[Verify] snapshot: 05_08_01_shadow_opacity_min.png'):
        actions.capture_for_gt('05_08_01_shadow_opacity_min.png')
    if actions.compare_with_gt('05_08_01_shadow_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow opacity min fail'
    with step('[Action] adjust_shadow_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0.5')
    with step('[Verify] snapshot: 05_08_01_shadow_opacity_mid.png'):
        actions.capture_for_gt('05_08_01_shadow_opacity_mid.png')
    if actions.compare_with_gt('05_08_01_shadow_opacity_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow opacity mid fail'
    with step('[Action] adjust_shadow_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0')
    with step('[Action] adjust_shadow_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '1')
    with step('[Verify] snapshot: 05_08_01_shadow_opacity_max.png'):
        actions.capture_for_gt('05_08_01_shadow_opacity_max.png')
    if actions.compare_with_gt('05_08_01_shadow_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow opacity max fail'
    from_pos = (30, 630)
    destination = (390, 630)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 630, 390, 630)
    with step('[Verify] snapshot: 05_08_01_shadow_before_picker.png'):
        actions.capture_for_gt('05_08_01_shadow_before_picker.png')
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 05_08_01_shadow_picker_slider.png'):
        actions.capture_for_gt('05_08_01_shadow_picker_slider.png')
    if actions.compare_with_gt('05_08_01_shadow_picker_slider.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow picker slider fail'
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(250, 600)
    with step('[Verify] snapshot: 05_08_01_shadow_picker_select.png'):
        actions.capture_for_gt('05_08_01_shadow_picker_select.png')
    if actions.compare_with_gt('05_08_01_shadow_picker_select.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow picker select fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 100)
    destination = (205, 229)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 100, 205, 229)
    with step('[Verify] snapshot: 05_08_01_shadow_picker_dropper.png'):
        actions.capture_for_gt('05_08_01_shadow_picker_dropper.png')
    if actions.compare_with_gt('05_08_01_shadow_picker_dropper.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow picker dropper fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 05_08_01_shadow_picker_cancel.png'):
        actions.capture_for_gt('05_08_01_shadow_picker_cancel.png')
    if actions.compare_with_gt('05_08_01_shadow_picker_cancel.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow picker cancel fail'
    from_pos = (30, 630)
    destination = (390, 630)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 630, 390, 630)
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
    with step('[Verify] snapshot: 05_08_01_shadow_picker_done.png'):
        actions.capture_for_gt('05_08_01_shadow_picker_done.png')
    if actions.compare_with_gt('05_08_01_shadow_picker_done.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare shadow picker done fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Toggle off withoutText')
    with step('[Verify] snapshot: 05_08_01_fill_shadow_on.png'):
        actions.capture_for_gt('05_08_01_fill_shadow_on.png')
    if actions.compare_with_gt('05_08_01_fill_shadow_on.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare fill shadow on fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Toggle on withoutText')
    with step('[Verify] snapshot: 05_08_01_fill_shadow_off.png'):
        actions.capture_for_gt('05_08_01_fill_shadow_off.png')
    if actions.compare_with_gt('05_08_01_fill_shadow_off.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare fill shadow off fail'
    with step('[Verify] snapshot: 05_08_01_before_close_shadow_drag.png'):
        actions.capture_for_gt('05_08_01_before_close_shadow_drag.png')
    from_pos = (206, 476)
    destination = (206, 800)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 476, 206, 800)
    with step('[Verify] snapshot: 05_08_01_after_close_shadow_drag.png'):
        actions.capture_for_gt('05_08_01_after_close_shadow_drag.png')
    if not actions.compare_with_gt('05_08_01_after_close_shadow_drag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare drag down close shadow panel fail'
    with step("[Verify] test_00105 completion"):
        assert True
