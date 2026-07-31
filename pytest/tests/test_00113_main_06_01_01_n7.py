import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00113_main_06_01_01_n7')
def test_00113_main_06_01_01_n7(actions: DriverActions):
    """Text bubble - new - shadow"""
    mode = 1
    uuid = ['6130d23c-703f-44e2-b853-4b34d8816b40', '9a0995ae-bd2e-4c4c-b494-b4f4bde4767a', 'dd5c2005-c4c0-4c1c-bb77-731d762c9d7b', '1fe68862-dd10-4a16-9d80-8cdf609be00d', 'e067cbfd-5990-4534-b024-0c556202b4cc', 'ec0fa10e-04eb-4a73-851e-20badd3a8a67', '2d9f2310-0f59-4bf5-afc9-14e5c393d87d', '66714a91-dbd6-4de6-8b63-75a0d1eef003', '0de65f09-4ed5-44df-aa83-6a3b0f3816c9', '4027f595-f343-4236-b5a9-6e9ad0d14db3', '9d8d4bcf-0dd3-4a12-a366-9ecdb3cb757c', '44d7814a-57d9-49ff-94ed-9140d21b33ac', '15650431-9544-4b27-8855-6f75faaf0711', 'b8603baa-e90a-4c4e-80e8-9f4dc826ae0d', '21235788-f16c-4a1f-81ca-4727af969173', '029f5223-0bb2-496f-b0a8-3153cf8ce838', '3a2357b0-204a-49fd-bafe-9404c5f8620d', '7f325898-8b17-48e4-a6ab-7758fc118eeb', '081aa24f-e837-4ffe-b997-24446b365542', '604088a8-dee3-4754-92e5-06009de9181a', '1a0652c8-a3a7-42c8-8cc0-f81dfea641b6', 'b3aca256-6c41-4178-8a5f-a02c134ec7e6', '5eccebc0-cb33-4fb6-ac1d-cd303ceb3c9c', '308f85c6-baf8-496b-a576-63e7223cffd9']
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
    with step('[Verify] snapshot: 06_01_01_no_shadow_panel.png'):
        actions.capture_for_gt('06_01_01_no_shadow_panel.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')
    with step('[Verify] snapshot: 06_01_01_shadow_default.png'):
        actions.capture_for_gt('06_01_01_shadow_default.png')
    if actions.compare_with_gt('06_01_01_shadow_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'default shadow panel 0 fail'
    with step('[Verify] snapshot: 06_01_01_shadow_default_size.png'):
        actions.capture_for_gt('06_01_01_shadow_default_size.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 06_01_01_close_shadow_panel_x.png'):
        actions.capture_for_gt('06_01_01_close_shadow_panel_x.png')
    if not actions.compare_with_gt('06_01_01_close_shadow_panel_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tap x close panel fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')
    with step('[Action] select_text_panel_shadow_color'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[9]')
    with step('[Verify] snapshot: 06_01_01_shadow.png'):
        actions.capture_for_gt('06_01_01_shadow.png')
    if actions.compare_with_gt('06_01_01_shadow.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'color-5 0 fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '30') == '30'):
        pass
    with step('[Action] adjust_shadow_blur_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] adjust_shadow_blur_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 06_01_01_shadow_blur_min.png'):
        actions.capture_for_gt('06_01_01_shadow_blur_min.png')
    if actions.compare_with_gt('06_01_01_shadow_blur_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'shadow_blur min 0 fail'
    with step('[Action] adjust_shadow_blur_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 06_01_01_shadow_blur_mid.png'):
        actions.capture_for_gt('06_01_01_shadow_blur_mid.png')
    if actions.compare_with_gt('06_01_01_shadow_blur_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'shadow_blur mid 0 fail'
    with step('[Action] adjust_shadow_blur_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_shadow_blur_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 06_01_01_shadow_blur_max.png'):
        actions.capture_for_gt('06_01_01_shadow_blur_max.png')
    if actions.compare_with_gt('06_01_01_shadow_blur_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'shadow_blur max 0 fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '30') == '30'):
        pass
    with step('[Action] adjust_shadow_distance_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Action] adjust_shadow_distance_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Verify] snapshot: 06_01_01_shadow_distance_min.png'):
        actions.capture_for_gt('06_01_01_shadow_distance_min.png')
    if actions.compare_with_gt('06_01_01_shadow_distance_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'shadow_distance min 0 fail'
    with step('[Action] adjust_shadow_distance_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0.5')
    with step('[Verify] snapshot: 06_01_01_shadow_distance_mid.png'):
        actions.capture_for_gt('06_01_01_shadow_distance_mid.png')
    if actions.compare_with_gt('06_01_01_shadow_distance_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'shadow_distance mid 0 fail'
    with step('[Action] adjust_shadow_distance_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Action] adjust_shadow_distance_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Verify] snapshot: 06_01_01_shadow_distance_max.png'):
        actions.capture_for_gt('06_01_01_shadow_distance_max.png')
    if actions.compare_with_gt('06_01_01_shadow_distance_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'shadow_distance max 0 fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '100') == '100'):
        pass
    with step('[Action] adjust_shadow_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '1')
    with step('[Action] adjust_shadow_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0')
    with step('[Verify] snapshot: 06_01_01_shadow_opacity_min.png'):
        actions.capture_for_gt('06_01_01_shadow_opacity_min.png')
    if actions.compare_with_gt('06_01_01_shadow_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'shadow_opacity min 0 fail'
    with step('[Action] adjust_shadow_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0.5')
    with step('[Verify] snapshot: 06_01_01_shadow_opacity_mid.png'):
        actions.capture_for_gt('06_01_01_shadow_opacity_mid.png')
    if actions.compare_with_gt('06_01_01_shadow_opacity_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'shadow_opacity mid 0 fail'
    with step('[Action] adjust_shadow_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0')
    with step('[Action] adjust_shadow_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '1')
    with step('[Verify] snapshot: 06_01_01_shadow_opacity_max.png'):
        actions.capture_for_gt('06_01_01_shadow_opacity_max.png')
    if actions.compare_with_gt('06_01_01_shadow_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity max 0 fail'
    with step('[Verify] snapshot: 06_01_01_shadow_before_picker.png'):
        actions.capture_for_gt('06_01_01_shadow_before_picker.png')
    from_pos = (30, 570)
    destination = (390, 570)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 570, 390, 570)
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 06_01_01_shadow_picker_slider.png'):
        actions.capture_for_gt('06_01_01_shadow_picker_slider.png')
    if actions.compare_with_gt('06_01_01_shadow_picker_slider.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'color picker slider 0 fail'
    with step('[Action] tap_color_picker'):
        assert actions.tap_by_coordinates(250, 550)
    with step('[Verify] snapshot: 06_01_01_shadow_picker_select.png'):
        actions.capture_for_gt('06_01_01_shadow_picker_select.png')
    if actions.compare_with_gt('06_01_01_shadow_picker_select.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'pick up color 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 100)
    destination = (205, 229)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 100, 205, 229)
    with step('[Verify] snapshot: 06_01_01_shadow_picker_dropper.png'):
        actions.capture_for_gt('06_01_01_shadow_picker_dropper.png')
    if actions.compare_with_gt('06_01_01_shadow_picker_dropper.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'dropper 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 06_01_01_shadow_picker_cancel.png'):
        actions.capture_for_gt('06_01_01_shadow_picker_cancel.png')
    if actions.compare_with_gt('06_01_01_shadow_picker_cancel.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'cancel picker fail'
    from_pos = (30, 570)
    destination = (390, 570)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 570, 390, 570)
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Action] tap_color_picker'):
        assert actions.tap_by_coordinates(250, 550)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step('[Verify] snapshot: 06_01_01_shadow_picker_done.png'):
        actions.capture_for_gt('06_01_01_shadow_picker_done.png')
    if actions.compare_with_gt('06_01_01_shadow_picker_done.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'add user color btn 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Toggle off withoutText')
    with step('[Verify] snapshot: 06_01_01_fill_shadow_on.png'):
        actions.capture_for_gt('06_01_01_fill_shadow_on.png')
    if actions.compare_with_gt('06_01_01_fill_shadow_on.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'fill_shadow_on 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Toggle on withoutText')
    with step('[Verify] snapshot: 06_01_01_fill_shadow_off.png'):
        actions.capture_for_gt('06_01_01_fill_shadow_off.png')
    if actions.compare_with_gt('06_01_01_fill_shadow_off.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'fill_shadow_off 0 fail'
    with step('[Verify] snapshot: 06_01_01_before_close_shadow_drag.png'):
        actions.capture_for_gt('06_01_01_before_close_shadow_drag.png')
    from_pos = (206, 482)
    destination = (206, 800)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 482, 206, 800)
    with step('[Verify] snapshot: 06_01_01_after_close_shadow_drag.png'):
        actions.capture_for_gt('06_01_01_after_close_shadow_drag.png')
    if not actions.compare_with_gt('06_01_01_after_close_shadow_drag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'drag down close panel fail'
    with step("[Verify] test_00113 completion"):
        assert True
