import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00107_main_06_01_01_n')
def test_00107_main_06_01_01_n(actions: DriverActions):
    """Text bubble - new - basic edit"""
    mode = 1
    uuid = ['7ecd2230-d9c7-4b6f-b83d-6413a17ec72f', '760d658b-26aa-4632-be2b-817d4a6f0226', 'de255683-679a-4995-96f9-e63464120240', '7f25ae28-d700-4956-8f52-05dbe461058e', 'ab0bed30-642c-46fd-be87-a03e7a8c442f', 'bff4b41f-16e3-4cc0-8d50-a0487530d045', '1f168cb4-3b8d-4001-bd54-49fe1914691b', '4aa0c69b-6e77-4989-aebf-03fc42efbf1b', '95b9c6e6-ea1d-417f-b020-3d2656dfb29b', '8b95ab7c-cdbd-4f7d-b304-b8d703d97f05', '2f200768-78cc-4eed-b216-a01ffd9f9956', '6c2bed87-606d-4b40-811d-a1856f383bb1', 'dd8450d3-eb52-4e4b-883a-2cbd21d003ef', '8f51c1d6-239a-4220-a34f-31dae4700b2a', 'c33752a2-8253-46a0-ba3c-27d83d91c171', '7af77495-8073-4b8f-9f8b-d8cd06759fef', 'f4ba7ff9-50ca-4217-8e33-5925927a6543', '45238599-2307-4db5-b037-337b07188e58', '88106573-3896-4fa3-9e0d-36e4a175913e']
    with step('[Action] close_continue_edit'):
        actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    from_pos = (380, 770)
    destination = (50, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 50, 770)
    with step('[Verify] snapshot: 06_01_01_before_text_bubble.png'):
        actions.capture_for_gt('06_01_01_before_text_bubble.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text Bubble')
    with step('[Verify] snapshot: 06_01_01_og.png'):
        actions.capture_for_gt('06_01_01_og.png')
    from_pos = (210, 400)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(210, 400, 50, 770)
    with step('[Verify] snapshot: 06_01_01_move.png'):
        actions.capture_for_gt('06_01_01_move.png')
    if actions.compare_with_gt('06_01_01_move.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare move failed'
    with step('[Verify] snapshot: 06_01_01_after_move.png'):
        actions.capture_for_gt('06_01_01_after_move.png')
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 06_01_01_undo.png'):
        actions.capture_for_gt('06_01_01_undo.png')
    if actions.compare_with_gt('06_01_01_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare undo failed'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 06_01_01_redo.png'):
        actions.capture_for_gt('06_01_01_redo.png')
    if actions.compare_with_gt('06_01_01_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare redo failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    destination = (100, 400)
    with step('[Verify] snapshot: 06_01_01_before_rotate.png'):
        actions.capture_for_gt('06_01_01_before_rotate.png')
    with step('[Action] drag_add_image_rotate'):
        rotate_x, rotate_y, rotate_w, rotate_h = actions.get_element_bounds(
            AppiumBy.ACCESSIBILITY_ID, 'rotateImageView'
        )
        actions.drag_coordinates(
            rotate_x + rotate_w // 2,
            rotate_y + rotate_h // 2,
            destination[0],
            destination[1],
        )
    with step('[Verify] snapshot: 06_01_01_after_rotate.png'):
        actions.capture_for_gt('06_01_01_after_rotate.png')
    if (not actions.compare_with_gt('06_01_01_after_rotate.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare resize/rotate failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDuplicate')
    with step('[Verify] snapshot: 06_01_01_duplicate.png'):
        actions.capture_for_gt('06_01_01_duplicate.png')
    if actions.compare_with_gt('06_01_01_duplicate.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare duplicate failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] focus_text'):
        actions.tap_by_coordinates(205, 400)
    with step('[Action] focus_text'):
        actions.tap_by_coordinates(205, 400)
    with step('[Verify] snapshot: 06_01_01_edit_keyboard.png'):
        actions.capture_for_gt('06_01_01_edit_keyboard.png')
    if actions.compare_with_gt('06_01_01_edit_keyboard.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare edit_keyboard failed'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.NAME, 'btn top cancel p')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step('[Verify] snapshot: 06_01_01_delete.png'):
        actions.capture_for_gt('06_01_01_delete.png')
    if actions.compare_with_gt('06_01_01_delete.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare delete failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] focus_text'):
        actions.tap_by_coordinates(205, 400)
    with step('[Verify] snapshot: 06_01_01_before_erase.png'):
        actions.capture_for_gt('06_01_01_before_erase.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'maskButton')
    from_pos = (50, 200)
    destination = (300, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 200, 300, 600)
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 06_01_01_after_erase.png'):
        actions.capture_for_gt('06_01_01_after_erase.png')
    if not actions.compare_with_gt('06_01_01_after_erase.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare eraser failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n')
    with step('[Action] focus_text'):
        actions.tap_by_coordinates(205, 400)
    with step('[Verify] snapshot: 06_01_01_before_brush_page.png'):
        actions.capture_for_gt('06_01_01_before_brush_page.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'maskButton')
    from_pos = (300, 200)
    destination = (170, 500)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(300, 200, 170, 500)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') == '50'):
        pass
    else:
        assert False, 'default brush size failed'
    if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('8', '9', '10', '11', '12'))):
        pass
    else:
        assert False, 'min brush size failed'
    if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100'))):
        pass
    else:
        assert False, 'max brush size failed'
    with step('[Verify] snapshot: 06_01_01_before_brush.png'):
        actions.capture_for_gt('06_01_01_before_brush.png')
    with step('[Verify] snapshot: 06_01_01_before_brush_debug.png'):
        actions.capture_for_gt('06_01_01_before_brush_debug.png')
    from_pos = (300, 200)
    destination = (170, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(300, 200, 170, 600)
    with step('[Verify] snapshot: 06_01_01_brush.png'):
        actions.capture_for_gt('06_01_01_brush.png')
    if actions.compare_with_gt('06_01_01_brush.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare brush failed'
    with step('[Verify] snapshot: 06_01_01_after_brush.png'):
        actions.capture_for_gt('06_01_01_after_brush.png')
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 06_01_01_undo_brush.png'):
        actions.capture_for_gt('06_01_01_undo_brush.png')
    if actions.compare_with_gt('06_01_01_undo_brush.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare undo brush failed'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 06_01_01_redo_brush.png'):
        actions.capture_for_gt('06_01_01_redo_brush.png')
    if actions.compare_with_gt('06_01_01_redo_brush.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare redo brush failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 06_01_01_brush_page_x.png'):
        actions.capture_for_gt('06_01_01_brush_page_x.png')
    if actions.compare_with_gt('06_01_01_brush_page_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare brush page x failed'
    with step("[Verify] test_00107 completion"):
        assert True
