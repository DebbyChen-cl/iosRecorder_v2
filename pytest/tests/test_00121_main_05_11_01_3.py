import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00121_main_05_11_01_3')
def test_00121_main_05_11_01_3(actions: DriverActions):
    """add-image adjustment"""
    mode = 1
    uuid = ['22c119fa-12f3-4763-a9b3-ea31ca33668f', 'dd53fe8f-0005-4619-9b02-4f4947e45e1f', '10980fcd-b158-4f2b-a046-ef301ce31e49', '122efa02-d26e-4e6e-9a38-15762135ef20', '111facec-21cc-41e2-96bd-d7c2c076720d', '19b3f34e-cfdc-4d72-b60a-1b87fc154e25', '5a46c35b-ad39-42fd-b1e6-099695e0f7c3', 'aabda53f-5ad0-43df-bb01-25e4d13cf04f', 'ee64a757-565e-45c8-8ace-bd5aae6e091f', 'd863d08e-fc67-491a-8b3e-529086eef62e', 'a4968363-c9f3-41ad-9a64-548b1cbc8d2a', 'f1b30cad-bfa8-4bdb-bdc6-7e9ed9e9edb8', '81dd6204-649b-466d-849e-af93236e5e11', '548a3b6d-53b7-4c77-9786-7bea941adb34', '5e7cd74e-1e05-4bb5-8b3a-07161c307629']
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
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category_add_image'):
        assert actions.tap_by_locator(AppiumBy.NAME, '_AT')
    with step('[Action] add_image'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Verify] snapshot: 05_11_01_before_adjustment.png'):
        actions.capture_for_gt('05_11_01_before_adjustment.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjust')
    with step('[Verify] snapshot: 05_11_01_before_adjust_auto_light.png'):
        actions.capture_for_gt('05_11_01_before_adjust_auto_light.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step('[Verify] snapshot: 05_11_01_adjust_auto_light.png'):
        actions.capture_for_gt('05_11_01_adjust_auto_light.png')
    if not actions.compare_with_gt('05_11_01_adjust_auto_light.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Fail to adjust auto light'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False, 'Fail to adjust exposure slider to right'
    with step('[Verify] snapshot: 05_11_01_exposure_slider_max.png'):
        actions.capture_for_gt('05_11_01_exposure_slider_max.png')
    if actions.compare_with_gt('05_11_01_exposure_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Exposure max comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Contrast')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False, 'Fail to adjust contrast slider to right'
    with step('[Verify] snapshot: 05_11_01_contrast_slider_max.png'):
        actions.capture_for_gt('05_11_01_contrast_slider_max.png')
    if actions.compare_with_gt('05_11_01_contrast_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'contrast max comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Highlight')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False, 'Fail to adjust highlights slider to left'
    with step('[Verify] snapshot: 05_11_01_highlights_slider_min.png'):
        actions.capture_for_gt('05_11_01_highlights_slider_min.png')
    if actions.compare_with_gt('05_11_01_highlights_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'highlights min comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Bright')
    with step('[Action] adjust_hdr_slider'):
        assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)
    with step('[Verify] snapshot: 05_11_01_adjust_bright.png'):
        actions.capture_for_gt('05_11_01_adjust_bright.png')
    if actions.compare_with_gt('05_11_01_adjust_bright.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'bright comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Midtone')
    with step('[Action] adjust_hdr_slider'):
        assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)
    with step('[Verify] snapshot: 05_11_01_adjust_midtone.png'):
        actions.capture_for_gt('05_11_01_adjust_midtone.png')
    if actions.compare_with_gt('05_11_01_adjust_midtone.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'midtone comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dark')
    with step('[Action] adjust_hdr_slider'):
        assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)
    with step('[Verify] snapshot: 05_11_01_adjust_dark.png'):
        actions.capture_for_gt('05_11_01_adjust_dark.png')
    if actions.compare_with_gt('05_11_01_adjust_dark.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'dark comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False, 'Fail to adjust shadows slider to left'
    with step('[Verify] snapshot: 05_11_01_shadows_slider_min.png'):
        actions.capture_for_gt('05_11_01_shadows_slider_min.png')
    if actions.compare_with_gt('05_11_01_shadows_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'shadows min comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step('[Verify] snapshot: 05_11_01_before_adjust_auto_color.png'):
        actions.capture_for_gt('05_11_01_before_adjust_auto_color.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto Color')
    with step('[Verify] snapshot: 05_11_01_adjust_auto_color.png'):
        actions.capture_for_gt('05_11_01_adjust_auto_color.png')
    if (not actions.compare_with_gt('05_11_01_adjust_auto_color.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'test failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Saturation')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_saturation_slider_max.png'):
        actions.capture_for_gt('05_11_01_saturation_slider_max.png')
    if actions.compare_with_gt('05_11_01_saturation_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'saturation max comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Details')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sharpness')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_sharpness_slider_max.png'):
        actions.capture_for_gt('05_11_01_sharpness_slider_max.png')
    if actions.compare_with_gt('05_11_01_sharpness_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'sharpness max comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Temperature')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_temperature_slider_max.png'):
        actions.capture_for_gt('05_11_01_temperature_slider_max.png')
    if actions.compare_with_gt('05_11_01_temperature_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'temperature max comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tint')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_tint_slider_min.png'):
        actions.capture_for_gt('05_11_01_tint_slider_min.png')
    if actions.compare_with_gt('05_11_01_tint_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tint min comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Curve')
    from_pos = (230, 707)
    destination = (230, 760)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(230, 707, 230, 760)
    with step('[Verify] snapshot: 05_11_01_adjust_curve.png'):
        actions.capture_for_gt('05_11_01_adjust_curve.png')
    if actions.compare_with_gt('05_11_01_adjust_curve.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'adjust curve comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HSL')
    with step('[Action] adjust_hsl_hue_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_saturation_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Verify] snapshot: 05_11_01_adjust_hsl.png'):
        actions.capture_for_gt('05_11_01_adjust_hsl.png')
    if actions.compare_with_gt('05_11_01_adjust_hsl.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'adjust hsl comparison failed'
    with step("[Verify] test_00121 completion"):
        assert True
