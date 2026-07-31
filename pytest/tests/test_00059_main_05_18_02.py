import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00059_main_05_18_02')
def test_00059_main_05_18_02(actions: DriverActions):
    """background art"""
    mode = 1
    uuid = ['ef1164cc-219e-427b-9c17-34892f1085e6', '0948c714-31d6-44a6-8e2c-9a6310c7995b', '1d338d63-9929-495c-8ccb-7d56a0fdd29c', '1c7b80b6-7ba0-42a0-b0d0-a2a7fd35ffb6', 'a88d4474-2064-4019-94d8-a012de9bc089', '49dc6f0d-963f-4807-b8b3-f9ac81b92a61', 'fd1d67bb-e8dc-4032-a9d5-3dbac775b02e', '29989825-b850-4358-a740-8ab86eda753d', '3eb0ebcf-d3e5-48fd-86b9-45d28c8b168b', '029003ce-afc5-403c-8c6f-91abbaa6d2f3', '0905acdf-cb0c-4cd9-8e89-364c18c20714', 'c6acbf09-a11e-4a37-964d-4f087c20cf95', '5694fec0-5ca8-4b16-8866-4939b10045c5', '55adb7c1-a592-469b-8e80-cb6210f28dac', 'dbd85599-ddeb-4612-a1ee-0d15d90a1cf1', 'fd3957d8-c403-446a-81f6-0ad6ccbdef34', '9bb446ec-7864-4dcb-9d89-db2f5ae0fe13']
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
    with step('[Verify] snapshot: 5_18_02_before_background.png'):
        actions.capture_for_gt('5_18_02_before_background.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background Art')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]', timeout=5):
            actions.wait_for_invisible(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_BG_Greenery_18_free_trending')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "change_background"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') == '50'):
        pass
    else:
        assert False, 'Default harmonization value incorrect'
    with step('[Action] adjust_bgart_slider'):
        assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "change_background"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'Adjust slider to min fail'
    with step('[Verify] snapshot: 5_18_02_background_before_max.png'):
        actions.capture_for_gt('5_18_02_background_before_max.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_bgart_slider'):
        assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "change_background"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('97', '98', '99', '100')):
        pass
    else:
        assert False, 'Adjust slider to max fail'
    with step('[Verify] snapshot: 5_18_02_background_slider100.png'):
        actions.capture_for_gt('5_18_02_background_slider100.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 5_18_02_background_tap_undo.png'):
        actions.capture_for_gt('5_18_02_background_tap_undo.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('5_18_02_background_tap_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 5_18_02_background_tap_redo.png'):
        actions.capture_for_gt('5_18_02_background_tap_redo.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('5_18_02_background_tap_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMask')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n')
    from_pos = (110, 120)
    destination = (110, 600)
    with step('[Verify] snapshot: 05_18_02_before1.png'):
        actions.capture_for_gt('05_18_02_before1.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(110, 120, 110, 600)
    with step('[Verify] snapshot: 05_18_02_after1.png'):
        actions.capture_for_gt('05_18_02_after1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_18_02_after1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Eraser + fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 5_18_02_after1_undo.png'):
        actions.capture_for_gt('5_18_02_after1_undo.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('5_18_02_after1_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo brush fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 5_18_02_after1_redo.png'):
        actions.capture_for_gt('5_18_02_after1_redo.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('5_18_02_after1_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo brush fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n')
    from_pos = (180, 120)
    destination = (180, 600)
    with step('[Verify] snapshot: 05_18_02_before2.png'):
        actions.capture_for_gt('05_18_02_before2.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(180, 120, 180, 600)
    with step('[Verify] snapshot: 05_18_02_after2.png'):
        actions.capture_for_gt('05_18_02_after2.png')
    if (not actions.compare_with_gt('05_18_02_after2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Eraser - fail'
    with step('[Verify] snapshot: 05_18_02_background_before.png'):
        actions.capture_for_gt('05_18_02_background_before.png')
    with step('[Action] adjust_harmonization_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_18_02_background_after.png'):
        actions.capture_for_gt('05_18_02_background_after.png')
    if (not actions.compare_with_gt('05_18_02_background_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Adjust brush size fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMask')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n')
    from_pos = (110, 120)
    destination = (110, 430)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(110, 120, 110, 430)
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_18_02_background_apply_brush.png'):
        actions.capture_for_gt('05_18_02_background_apply_brush.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('5_18_02_background_slider100.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Exit brush fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 5_18_02_background_x.png'):
        actions.capture_for_gt('5_18_02_background_x.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if actions.compare_with_gt('5_18_02_before_background.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[x] fail'
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background Art')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_BG_Greenery_18_free_trending')
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 5_18_02_background_v.png'):
        actions.capture_for_gt('5_18_02_background_v.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if (not actions.compare_with_gt('5_18_02_before_background.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, '[v] fail'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00059 completion"):
        assert True
