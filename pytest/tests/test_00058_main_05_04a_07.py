import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00058_main_05_04a_07')
def test_00058_main_05_04a_07(actions: DriverActions):
    """invert"""
    mode = 1
    uuid = ['a693f4da-1f61-46f7-b6b6-61be0eef6485', '0fe56d4a-7c73-446f-ada7-37b5ae3cb56c', '3966feb1-7194-4957-9239-100eb74a52c5', '2a66b3d5-6296-4c1a-9b1f-c4ae1776275b', '78c5e025-88d6-436d-bca3-11591d7b848f', '537fb6de-863c-4a10-87dd-b6fa0896ff06', '46400fde-55de-452e-a5b8-a7cbb05eb9e0', 'cc79254b-c988-4b9b-a460-b5b228afe2b2', '9229249f-3b41-4e1f-a44b-6dfbad5bf789', '1daca9e5-83a8-4e11-8a10-c2e1b0e67d00', '36ab60f1-9ca2-43f5-b1be-f93e5743fcbe', '7e3330e4-dbc0-400d-9b82-b890af00c0c7', 'cc79254b-c988-4b9b-a460-b5b228afe2b2']
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Invert')
    with step('[Verify] snapshot: 05_04a_07_invert.png'):
        actions.capture_for_gt('05_04a_07_invert.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_04a_07_invert.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn autofocus n')
    with step('[Verify] snapshot: 05_04a_07_object.png'):
        actions.capture_for_gt('05_04a_07_object.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_04a_07_object.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap done fail'
    with step('[Verify] snapshot: 05_04a_07_tap_v.png'):
        actions.capture_for_gt('05_04a_07_tap_v.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_04a_07_tap_v.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_04a_07_before_enter_invert.png'):
        actions.capture_for_gt('05_04a_07_before_enter_invert.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Invert')
    with step('[Verify] snapshot: 05_04a_07_before_enter_brush.png'):
        actions.capture_for_gt('05_04a_07_before_enter_brush.png', crop_rect=(0, 60, 276, 597))
    with step('[Verify] snapshot: 05_04a_07_brush+_before.png'):
        actions.capture_for_gt('05_04a_07_brush+_before.png')
    with step('[Action] adjust_slider_1'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 05_04a_07_brush+_after.png'):
        actions.capture_for_gt('05_04a_07_brush+_after.png')
    if (not actions.compare_with_gt('05_04a_07_brush+_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Compare fail'
    with step('[Action] adjust_slider_1'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    from_pos = (25, 100)
    destination = (370, 600)
    with step('[Verify] snapshot: 05_04a_07_before_brush+.png'):
        actions.capture_for_gt('05_04a_07_before_brush+.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(25, 100, 370, 600)
    with step('[Verify] snapshot: 05_04a_07_after_brush+.png'):
        actions.capture_for_gt('05_04a_07_after_brush+.png')
    if (not actions.compare_with_gt('05_04a_07_after_brush+.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Compare fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn invert n')):
        assert False, 'Tap inverse fail'
    with step('[Verify] snapshot: 05_04a_07_inverse_brush.png'):
        actions.capture_for_gt('05_04a_07_inverse_brush.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_04a_07_inverse_brush.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare fail'
    with step('[Verify] snapshot: 05_04a_07_inverse_OG_undo.png'):
        actions.capture_for_gt('05_04a_07_inverse_OG_undo.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn invert n')
    with step('[Verify] snapshot: 05_04a_07_inverse_before_undo.png'):
        actions.capture_for_gt('05_04a_07_inverse_before_undo.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_04a_07_inverse_undo.png'):
        actions.capture_for_gt('05_04a_07_inverse_undo.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_04a_07_inverse_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_04a_07_inverse_redo.png'):
        actions.capture_for_gt('05_04a_07_inverse_redo.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_04a_07_inverse_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step('[Verify] snapshot: 05_04a_07_brush-_before.png'):
        actions.capture_for_gt('05_04a_07_brush-_before.png')
    with step('[Action] adjust_slider_1'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 05_04a_07_brush-_after.png'):
        actions.capture_for_gt('05_04a_07_brush-_after.png')
    if (not actions.compare_with_gt('05_04a_07_brush-_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Compare fail'
    with step('[Action] adjust_slider_1'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    from_pos = (25, 100)
    destination = (370, 600)
    with step('[Verify] snapshot: 05_04a_07_before_brush-.png'):
        actions.capture_for_gt('05_04a_07_before_brush-.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(25, 100, 370, 600)
    with step('[Verify] snapshot: 05_04a_07_after_brush-.png'):
        actions.capture_for_gt('05_04a_07_after_brush-.png')
    if (not actions.compare_with_gt('05_04a_07_after_brush-.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Compare fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'Tap x fail'
    with step('[Verify] snapshot: 05_04a_07_tap_x.png'):
        actions.capture_for_gt('05_04a_07_tap_x.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_04a_07_tap_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare fail'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00058 completion"):
        assert True
