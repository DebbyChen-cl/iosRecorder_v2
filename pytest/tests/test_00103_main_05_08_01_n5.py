import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00103_main_05_08_01_n5')
def test_00103_main_05_08_01_n5(actions: DriverActions):
    """Text tools - text new - color"""
    mode = 1
    uuid = ['757f0d17-ff4f-4c05-8f0e-ca35f4ca9dbd', '457504dc-946d-4a1c-b01c-5b7da7944620', '00901a33-7c8c-4ff1-9a21-40f408b6ccd0', '89be60a2-861d-4423-9bc4-42c922a92571', '8b93937e-5730-4856-ba27-8592036e1ad9', 'ecdce129-b4b5-4f0d-a324-53e5dc072abc', 'e97cf499-ba6b-4371-b11a-27ce414852bf', '7c538cf7-d676-45b4-b0e5-e90a5f63dceb', 'c425d302-68c8-4fd8-b49c-54206f6a078b', '1d4fdc56-8308-42a6-aec3-825723c84865', 'd1e8b71f-3988-42ac-b877-97d059602687', '42d20f01-3ef3-4e7b-aef0-b6b9705bebbd', '6dd4b4e5-436f-4216-beb6-9e57568a5e8c', '81e793c6-631a-40cf-9701-3362c9c781a1', '52a7c7f9-8a2c-4ce8-b96c-11a992d12c70', 'b69f0418-296b-4d37-b820-7fbe2e513da8', 'fce914d4-ed64-4adb-bd18-f88583e2ac68', '1384c2ae-5510-4708-808a-bb71f0a78524', '722a3991-5e59-490a-8e7b-04c37f5d2f86', '7ca8b409-8f8c-46f8-8dbc-20570f67e8ca', '445ccd28-57df-411e-9db7-8dc35d3c871c', '757a5f4b-72c3-49fe-8cb1-2edd9721e66f', 'c212e3e1-1125-4bea-a160-e1a3194d704f', '94b0de26-53b3-4d1e-8c45-9b27a7849fd1', '68bf8902-03a3-4e96-ada4-cb30f836642d', '11d0d1a5-121b-4c6c-9137-1f0d5a070f00', '0773f666-7428-4776-84c1-81c66f363fa8', '873470b5-6b6c-40b4-bbb4-6d3c5748c144', 'b982741a-87ba-4892-a651-ebd442f334b5', 'e0b31280-9775-4fa2-9848-166ec27fedfc', 'be694c57-561a-42e5-9f3d-7f7418db3f80', 'bac36b17-dd3e-41ab-a083-9eab10f84a1b', '3dbdd5d1-bdef-47d2-b7b2-b2459a1e21de', 'ae792dcd-e563-4ea6-b41d-e950a213c6fd', '295e7a9a-0b3f-452d-99b6-c80b94753f31', 'c256c0b8-cdf4-430d-be4f-8dd9800e48e1', '297024eb-a331-483f-ab2a-e75b8a06e677', '6049fb9c-de7c-468c-abda-ccdb19ee078a', 'eebb620c-2a12-47e1-b017-8f13c2e0fcfa']
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
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Verify] snapshot: 05_08_01_no_color_panel.png'):
        actions.capture_for_gt('05_08_01_no_color_panel.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step('[Verify] snapshot: 05_08_01_color_default.png'):
        actions.capture_for_gt('05_08_01_color_default.png')
    if actions.compare_with_gt('05_08_01_color_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare color default fail'
    with step('[Verify] snapshot: 05_08_01_color_default_size.png'):
        actions.capture_for_gt('05_08_01_color_default_size.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 05_08_01_close_color_panel_x.png'):
        actions.capture_for_gt('05_08_01_close_color_panel_x.png')
    if not actions.compare_with_gt('05_08_01_close_color_panel_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Close color panel x comparison fail'
    with step('[Action] focus_text'):
        actions.tap_by_coordinates(205, 455)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step('[Action] select_text_panel_color'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[6]')
    with step('[Verify] snapshot: 05_08_01_solid_color.png'):
        actions.capture_for_gt('05_08_01_solid_color.png')
    if actions.compare_with_gt('05_08_01_solid_color.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare color-3 fail'
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '100') == '100'):
        pass
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_08_01_solid_color_opacity_min.png'):
        actions.capture_for_gt('05_08_01_solid_color_opacity_min.png')
    if actions.compare_with_gt('05_08_01_solid_color_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare opacity min fail'
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0.5')
    with step('[Verify] snapshot: 05_08_01_solid_color_opacity_mid.png'):
        actions.capture_for_gt('05_08_01_solid_color_opacity_mid.png')
    if actions.compare_with_gt('05_08_01_solid_color_opacity_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare opacity mid fail'
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_08_01_solid_color_opacity_max.png'):
        actions.capture_for_gt('05_08_01_solid_color_opacity_max.png')
    if actions.compare_with_gt('05_08_01_solid_color_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare opacity max fail'
    with step('[Verify] snapshot: 05_08_01_solid_color_before_picker.png'):
        actions.capture_for_gt('05_08_01_solid_color_before_picker.png')
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 05_08_01_solid_color_picker_slider.png'):
        actions.capture_for_gt('05_08_01_solid_color_picker_slider.png')
    if actions.compare_with_gt('05_08_01_solid_color_picker_slider.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare color picker slider fail'
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(250, 600)
    with step('[Verify] snapshot: 05_08_01_solid_color_picker_select.png'):
        actions.capture_for_gt('05_08_01_solid_color_picker_select.png')
    if actions.compare_with_gt('05_08_01_solid_color_picker_select.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare pick up color fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 100)
    destination = (219, 420)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 100, 219, 420)
    with step('[Verify] snapshot: 05_08_01_solid_color_picker_dropper.png'):
        actions.capture_for_gt('05_08_01_solid_color_picker_dropper.png')
    if actions.compare_with_gt('05_08_01_solid_color_picker_dropper.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare dropper fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 05_08_01_solid_color_picker_cancel.png'):
        actions.capture_for_gt('05_08_01_solid_color_picker_cancel.png')
    if actions.compare_with_gt('05_08_01_solid_color_picker_cancel.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare cancel picker fail'
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(250, 600)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step('[Verify] snapshot: 05_08_01_solid_color_picker_done.png'):
        actions.capture_for_gt('05_08_01_solid_color_picker_done.png')
    if actions.compare_with_gt('05_08_01_solid_color_picker_done.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare color picker done fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Gradient')
    with step('[Action] select_text_panel_color'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]')
    with step('[Verify] snapshot: 05_08_01_gradient_color.png'):
        actions.capture_for_gt('05_08_01_gradient_color.png')
    if actions.compare_with_gt('05_08_01_gradient_color.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient color fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') == '100'):
        pass
    with step('[Action] adjust_color_gradient_angle_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Action] adjust_color_gradient_angle_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 05_08_01_gradient_angle_min.png'):
        actions.capture_for_gt('05_08_01_gradient_angle_min.png')
    if actions.compare_with_gt('05_08_01_gradient_angle_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient angle min fail'
    with step('[Action] adjust_color_gradient_angle_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 05_08_01_gradient_angle_max.png'):
        actions.capture_for_gt('05_08_01_gradient_angle_max.png')
    if actions.compare_with_gt('05_08_01_gradient_angle_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient angle max fail'
    with step('[Action] adjust_color_gradient_angle_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 05_08_01_gradient_angle_mid.png'):
        actions.capture_for_gt('05_08_01_gradient_angle_mid.png')
    if actions.compare_with_gt('05_08_01_gradient_angle_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient angle mid fail'
    with step('[Action] adjust_color_gradient_transition_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Action] adjust_color_gradient_transition_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Verify] snapshot: 05_08_01_gradient_transition_min.png'):
        actions.capture_for_gt('05_08_01_gradient_transition_min.png')
    if actions.compare_with_gt('05_08_01_gradient_transition_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient transition min fail'
    with step('[Action] adjust_color_gradient_transition_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Verify] snapshot: 05_08_01_gradient_transition_max.png'):
        actions.capture_for_gt('05_08_01_gradient_transition_max.png')
    if actions.compare_with_gt('05_08_01_gradient_transition_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient transition max fail'
    with step('[Action] adjust_color_gradient_transition_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0.5')
    with step('[Verify] snapshot: 05_08_01_gradient_transition_mid.png'):
        actions.capture_for_gt('05_08_01_gradient_transition_mid.png')
    if actions.compare_with_gt('05_08_01_gradient_transition_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient transition mid fail'
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '1')
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0')
    with step('[Verify] snapshot: 05_08_01_gradient_opacity_min.png'):
        actions.capture_for_gt('05_08_01_gradient_opacity_min.png')
    if actions.compare_with_gt('05_08_01_gradient_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient opacity min fail'
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0.5')
    with step('[Verify] snapshot: 05_08_01_gradient_opacity_mid.png'):
        actions.capture_for_gt('05_08_01_gradient_opacity_mid.png')
    if actions.compare_with_gt('05_08_01_gradient_opacity_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient opacity mid fail'
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '0')
    with step('[Action] adjust_color_gradient_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', '1')
    with step('[Verify] snapshot: 05_08_01_gradient_opacity_max.png'):
        actions.capture_for_gt('05_08_01_gradient_opacity_max.png')
    if actions.compare_with_gt('05_08_01_gradient_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient opacity max fail'
    with step('[Verify] snapshot: 05_08_01_gradient_color_before_picker.png'):
        actions.capture_for_gt('05_08_01_gradient_color_before_picker.png')
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0.5')
    with step('[Verify] snapshot: 05_08_01_gradient_color_picker_slider1.png'):
        actions.capture_for_gt('05_08_01_gradient_color_picker_slider1.png')
    if actions.compare_with_gt('05_08_01_gradient_color_picker_slider1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient color picker slider1 fail'
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(250, 600)
    with step('[Verify] snapshot: 05_08_01_gradient_color_picker_select1.png'):
        actions.capture_for_gt('05_08_01_gradient_color_picker_select1.png')
    if actions.compare_with_gt('05_08_01_gradient_color_picker_select1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient color picker select1 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 100)
    destination = (205, 200)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 100, 205, 200)
    with step('[Verify] snapshot: 05_08_01_gradient_color_picker_dropper1.png'):
        actions.capture_for_gt('05_08_01_gradient_color_picker_dropper1.png')
    if actions.compare_with_gt('05_08_01_gradient_color_picker_dropper1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient color picker dropper1 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'currentEndingColorView')
    with step('[Action] adjust_text_color_picker_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 05_08_01_gradient_color_picker_slider2.png'):
        actions.capture_for_gt('05_08_01_gradient_color_picker_slider2.png')
    if actions.compare_with_gt('05_08_01_gradient_color_picker_slider2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient color picker slider2 fail'
    with step('[Action] pick_color'):
        actions.tap_by_coordinates(331, 570)
    with step('[Verify] snapshot: 05_08_01_gradient_color_picker_select2.png'):
        actions.capture_for_gt('05_08_01_gradient_color_picker_select2.png')
    if actions.compare_with_gt('05_08_01_gradient_color_picker_select2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient color picker select2 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    from_pos = (100, 110)
    destination = (150, 150)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 110, 150, 150)
    with step('[Verify] snapshot: 05_08_01_gradient_color_picker_dropper2.png'):
        actions.capture_for_gt('05_08_01_gradient_color_picker_dropper2.png')
    if actions.compare_with_gt('05_08_01_gradient_color_picker_dropper2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient color picker dropper2 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step('[Verify] snapshot: 05_08_01_gradient_color_picker_cancel.png'):
        actions.capture_for_gt('05_08_01_gradient_color_picker_cancel.png')
    if actions.compare_with_gt('05_08_01_gradient_color_picker_cancel.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient color picker cancel fail'
    with step('[Action] tap_text_color_picker'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'cellImageView'), (AppiumBy.ACCESSIBILITY_ID, 'cellImageView')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
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
    with step('[Verify] snapshot: 05_08_01_gradient_color_picker_done.png'):
        actions.capture_for_gt('05_08_01_gradient_color_picker_done.png')
    if actions.compare_with_gt('05_08_01_gradient_color_picker_done.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare gradient color picker done fail'
    with step('[Verify] snapshot: 05_08_01_before_close_color_drag.png'):
        actions.capture_for_gt('05_08_01_before_close_color_drag.png')
    from_pos = (206, 476)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 476, 150, 150)
    with step('[Verify] snapshot: 05_08_01_after_close_color_drag.png'):
        actions.capture_for_gt('05_08_01_after_close_color_drag.png')
    if not actions.compare_with_gt('05_08_01_after_close_color_drag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare drag down close color panel fail'
    with step("[Verify] test_00103 completion"):
        assert True
