import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00060_main_05_18_01')
def test_00060_main_05_18_01(actions: DriverActions):
    """surreal art"""
    mode = 1
    uuid = ['150180c5-1dd2-11b2-8000-080027b246c3', '150180c5-1dd2-11b2-8001-080027b246c3', '150180c5-1dd2-11b2-8002-080027b246c3', '150180c5-1dd2-11b2-8003-080027b246c3', '150180c5-1dd2-11b2-8004-080027b246c3', '150180c5-1dd2-11b2-8005-080027b246c3', '150180c5-1dd2-11b2-8006-080027b246c3', '150180c5-1dd2-11b2-8007-080027b246c3', '150180c5-1dd2-11b2-8008-080027b246c3', '150180c5-1dd2-11b2-8009-080027b246c3', '150180c5-1dd2-11b2-800a-080027b246c3', '150180c5-1dd2-11b2-800b-080027b246c3', '150180c5-1dd2-11b2-800c-080027b246c3', '150180c5-1dd2-11b2-800d-080027b246c3', '150180c5-1dd2-11b2-800e-080027b246c3']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background Art')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Template')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "surreal_art"`]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "surreal_art"`]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeButton[2]') == '50'):
        pass
    else:
        assert False, 'Default harmonization value incorrect'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "surreal_art"`]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeButton[2]') in ('0', '1', '2', '3')):
        pass
    else:
        assert False, 'Adjust to min fail'
    with step('[Verify] snapshot: 5_18_01_surreal_slider0.png'):
        actions.capture_for_gt('5_18_01_surreal_slider0.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "surreal_art"`]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeButton[2]') in ('99', '100')):
        pass
    else:
        assert False, 'Adjust to max fail'
    with step('[Verify] snapshot: 5_18_01_surreal_slider100.png'):
        actions.capture_for_gt('5_18_01_surreal_slider100.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 5_18_01_surreal_undo.png'):
        actions.capture_for_gt('5_18_01_surreal_undo.png')
    if actions.compare_with_gt('5_18_01_surreal_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 5_18_01_surreal_redo.png'):
        actions.capture_for_gt('5_18_01_surreal_redo.png')
    if actions.compare_with_gt('5_18_01_surreal_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMask')
    from_pos = (325, 300)
    destination = (325, 500)
    with step('[Verify] snapshot: 05_18_01_before1.png'):
        actions.capture_for_gt('05_18_01_before1.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(325, 300, 325, 500)
    with step('[Verify] snapshot: 05_18_01_after1.png'):
        actions.capture_for_gt('05_18_01_after1.png')
    if (not actions.compare_with_gt('05_18_01_after1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Compare fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 5_18_01_after1_undo.png'):
        actions.capture_for_gt('5_18_01_after1_undo.png')
    if actions.compare_with_gt('5_18_01_after1_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 5_18_01_after1_redo.png'):
        actions.capture_for_gt('5_18_01_after1_redo.png')
    if actions.compare_with_gt('5_18_01_after1_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    from_pos = (125, 400)
    destination = (325, 400)
    with step('[Verify] snapshot: 05_18_01_before2.png'):
        actions.capture_for_gt('05_18_01_before2.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(125, 400, 325, 400)
    with step('[Verify] snapshot: 05_18_01_after2.png'):
        actions.capture_for_gt('05_18_01_after2.png')
    if (not actions.compare_with_gt('05_18_01_after2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Compare fail'
    with step('[Verify] snapshot: 05_18_01_surreal_before.png'):
        actions.capture_for_gt('05_18_01_surreal_before.png')
    with step('[Action] adjust_harmonization_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_18_01_surreal_after.png'):
        actions.capture_for_gt('05_18_01_surreal_after.png')
    if (not actions.compare_with_gt('05_18_01_surreal_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Compare fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'Tap x fail'
    with step('[Verify] snapshot: 05_18_01_surreal_exit_brush.png'):
        actions.capture_for_gt('05_18_01_surreal_exit_brush.png')
    with step('[Verify] compare: 5_18_01_surreal_slider100.png'):
        assert actions.compare_with_gt('5_18_01_surreal_slider100.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMask')
    from_pos = (125, 400)
    destination = (325, 400)
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step('[Action] adjust_harmonization_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(125, 400, 325, 400)
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_18_01_surreal_apply_brush.png'):
        actions.capture_for_gt('05_18_01_surreal_apply_brush.png')
    if actions.compare_with_gt('5_18_01_surreal_slider100.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'Exit brush page fail'
    with step('[Action] tap_feature_x_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00060 completion"):
        assert True
