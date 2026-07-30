# @sft-convert:generated  (自動生成；若手動編輯，請把檔名加進 .scratch/sft-convert/PROTECT.txt
#                          或把本行改成 '# @manual'，即不會被覆蓋)
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00174_collage_edit')
def test_00174_collage_edit(actions: DriverActions):
    """collage edit"""
    uuid = ['3b1ed267-5789-42f1-a49e-2b18e75639d2', 'bdfe1a0c-f0e5-44c8-b32c-e5197d139f84', '64726fe2-8b5f-4a35-9f22-19d2adb04e14', 'd89ea913-eb8f-45ca-9868-b359487b5aaa', '8058cd42-6400-4fe6-99a2-e0e253c85ab8', 'e24702fd-3775-4490-8e9c-29d76e26b0f9', '91095643-577c-46ea-946d-5b8228de6428', 'ebebeaf2-bfbc-47f2-87c9-d5fd196df773', 'c745f445-25ab-4878-bd04-285c84533152', 'f3eecaf1-98c0-4809-ba22-95eef68facc2', 'f8bf5636-d79a-4905-8bcf-42337a46864b', 'b135de9a-4464-49cc-9b5d-f617a2ccd926', 'bd459815-9514-4a48-a9bb-c68269b4f046', 'bbed28b2-717f-499d-a869-06b7464c07c4', 'a7238bc9-ae7c-405c-833b-add0ba2ae1ce', 'c493f32b-2279-48cf-9a22-1f382a11005f', '68438997-4caf-4cb9-8ba5-4c818c739b51', 'a4968363-c9f3-41ad-9a64-548b1cbc8d2a', 'f1b30cad-bfa8-4bdb-bdc6-7e9ed9e9edb8', '81dd6204-649b-466d-849e-af93236e5e11', '548a3b6d-53b7-4c77-9786-7bea941adb34', '5e7cd74e-1e05-4bb5-8b3a-07161c307629']
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'More')):
        pass
    else:
        if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Less')):
            pass
        else:
            assert False, 'Failed to tap more or less button'
    assert actions.try_tap(AppiumBy.NAME, 'Collage'), '[06_03_01] Failed to tap collage'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn2'), '[06_03_01_2] Failed to switch to 2 photo'
    assert actions.tap_by_coordinates(70, 280)
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.NAME, '_AT')
    with step('[Verify] snapshot: 06_03_01_no_photo_selected.png'):
        actions.capture_for_gt('06_03_01_no_photo_selected.png')
    assert actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0'), '[06_03_01_2] Failed to select photo1'
    assert actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1'), '[06_03_01_2] Failed to select photo2'
    with step('[Action] click_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('[Verify] snapshot: 06_03_01_2_before_apply.png'):
        actions.capture_for_gt('06_03_01_2_before_apply.png')
    assert actions.tap_by_coordinates(390, 767)
    with step('[Verify] snapshot: 06_03_01_2_after_apply.png'):
        actions.capture_for_gt('06_03_01_2_after_apply.png')
    for x in range(20):
        from_pos = (400, 780)
        destination = (50, 780)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(400, 780, 50, 780)
    assert actions.tap_by_coordinates(384, 781)
    assert actions.tap_by_coordinates(205, 300)
    with step('[Verify] snapshot: 06_03_01_before_replace.png'):
        actions.capture_for_gt('06_03_01_before_replace.png')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace'), '[06_03_01_2] Failed to tap replace'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCamera'), '[06_03_01_2] Failed to tap take_a_shot'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto'), '[06_03_01_2] Failed to tap shot'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use Photo'), '[06_03_01_2] Failed to tap use_photo'
    with step('[Verify] snapshot: 06_03_01_after_replace_camera.png'):
        actions.capture_for_gt('06_03_01_after_replace_camera.png')
    if (not actions.compare_with_gt('06_03_01_after_replace_camera.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace'), '[06_03_01_2] Failed to tap replace again'
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6'), '[06_03_01_2] Failed to add image'
    with step('[Verify] snapshot: 06_03_01_after_replace.png'):
        actions.capture_for_gt('06_03_01_after_replace.png')
    if (not actions.compare_with_gt('06_03_01_after_replace.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AddImageCollagePhotoPanelCell-1'), '[06_03_01_2] Failed to tap flip H'
    with step('[Verify] snapshot: 06_03_01_after_flip_H.png'):
        actions.capture_for_gt('06_03_01_after_flip_H.png')
    if (not actions.compare_with_gt('06_03_01_after_flip_H.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AddImageCollagePhotoPanelCell-2'), '[06_03_01_2] Failed to tap flip V'
    with step('[Verify] snapshot: 06_03_01_after_flip_V.png'):
        actions.capture_for_gt('06_03_01_after_flip_V.png')
    if (not actions.compare_with_gt('06_03_01_after_flip_V.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AddImageCollagePhotoPanelCell-3'), '[06_03_01_2] Failed to tap adjustments'
    with step('[Verify] snapshot: 06_03_01_adjust_og.png'):
        actions.capture_for_gt('06_03_01_adjust_og.png')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto'), '[06_03_01_2] Failed to tap auto'
    with step('[Verify] snapshot: 06_03_01_adjust_auto_light.png'):
        actions.capture_for_gt('06_03_01_adjust_auto_light.png')
    if (not actions.compare_with_gt('06_03_01_adjust_auto_light.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    actions.capture_for_gt('06_03_01_exposure_slider_max.png')
    if actions.compare_with_gt('06_03_01_exposure_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Contrast'), '[06_03_01_2] Failed to tap contrast'
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    actions.capture_for_gt('06_03_01_contrast_slider_max.png')
    if actions.compare_with_gt('06_03_01_contrast_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Highlight'), '[06_03_01_2] Failed to tap highlights'
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    actions.capture_for_gt('06_03_01_highlights_slider_min.png')
    if actions.compare_with_gt('06_03_01_highlights_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Bright'), '[06_03_01_2] Failed to tap bright'
    assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1), '[06_03_01_2] Failed to adjust bright slider'
    actions.capture_for_gt('06_03_01_adjust_bright.png')
    if actions.compare_with_gt('06_03_01_adjust_bright.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Midtone'), '[06_03_01_2] Failed to tap midtone'
    assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1), '[06_03_01_2] Failed to adjust midtone slider'
    actions.capture_for_gt('06_03_01_adjust_midtone.png')
    if actions.compare_with_gt('06_03_01_adjust_midtone.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dark'), '[06_03_01_2] Failed to tap dark'
    assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1), '[06_03_01_2] Failed to adjust dark slider'
    actions.capture_for_gt('06_03_01_adjust_dark.png')
    if actions.compare_with_gt('06_03_01_adjust_dark.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow'), '[06_03_01_2] Failed to tap shadow'
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    actions.capture_for_gt('06_03_01_shadows_slider_min.png')
    if actions.compare_with_gt('06_03_01_shadows_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color'), '[06_03_01_2] Failed to tap text_color'
    with step('[Verify] snapshot: 06_03_01_adjust_color_og.png'):
        actions.capture_for_gt('06_03_01_adjust_color_og.png')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto Color'), '[06_03_01_2] Failed to tap auto_color'
    with step('[Verify] snapshot: 06_03_01_adjust_auto_color.png'):
        actions.capture_for_gt('06_03_01_adjust_auto_color.png')
    if (not actions.compare_with_gt('06_03_01_adjust_auto_color.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Saturation'), '[06_03_01_2] Failed to tap saturation'
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    actions.capture_for_gt('06_03_01_saturation_slider_max.png')
    if actions.compare_with_gt('06_03_01_saturation_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Details')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sharpness'), '[06_03_01_2] Failed to tap sharpness'
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    actions.capture_for_gt('06_03_01_sharpness_slider_max.png')
    if actions.compare_with_gt('06_03_01_sharpness_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Temperature'), '[06_03_01_2] Failed to tap temperature'
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    actions.capture_for_gt('06_03_01_temperature_slider_max.png')
    if actions.compare_with_gt('06_03_01_temperature_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    actions.capture_for_gt('06_03_01_tint_slider_min.png')
    if actions.compare_with_gt('06_03_01_tint_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Curve'), '[06_03_01_2] Failed to tap curve'
    from_pos = (230, 707)
    destination = (230, 760)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(230, 707, 230, 760)
    actions.capture_for_gt('06_03_01_adjust_curve.png')
    if actions.compare_with_gt('06_03_01_adjust_curve.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HSL'), '[06_03_01_2] Failed to tap hsl'
    assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1), '[06_03_01_2] Failed to adjust hsl hue slider'
    assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1), '[06_03_01_2] Failed to adjust hsl saturation slider'
    assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1), '[06_03_01_2] Failed to adjust hsl lightness slider'
    actions.capture_for_gt('06_03_01_adjust_hsl.png')
    if actions.compare_with_gt('06_03_01_adjust_hsl.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 06_03_01_after_adjust.png'):
        actions.capture_for_gt('06_03_01_after_adjust.png')
    if (not actions.compare_with_gt('06_03_01_after_adjust.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Filter'), '[06_03_01_2] Failed to tap effects_filter'
    assert actions.tap_by_coordinates(180, 779)
    with step('[Verify] snapshot: 06_03_01_after_filter.png'):
        actions.capture_for_gt('06_03_01_after_filter.png')
    if (not actions.compare_with_gt('06_03_01_after_filter.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step("[Verify] test_00174 completion"):
        assert True
