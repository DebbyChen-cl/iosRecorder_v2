import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00099_main_05_08_01_n')
def test_00099_main_05_08_01_n(actions: DriverActions):
    """Text tools - text new - basic edit"""
    mode = 1
    uuid = ['35bf38a2-c4e8-46dd-b306-ab9012a903eb', '6c1a8f7f-cf5d-4029-921e-65bb5fe0b5e8', 'bd18515f-52cc-4d95-87a2-876a37dfe0bd', '63f63bd3-f79c-4c21-aaa2-238528d98a0e', 'b4dc18ab-ff42-4b8a-8414-63597140e788', '53153fb1-6661-45a2-af67-e08c893468a3', 'd0176191-9094-4e43-9345-bc6df7da98de', '59999755-5015-431d-880b-cbcaea202840', '55e0b27e-7a54-4d51-8728-2962c0661712', '84930db2-69b5-430f-829a-e281d8aed96e', '04e9d70a-0640-4d51-970a-302ca2973be5', '2b0c8cd8-0a1a-4711-94e9-8bb730c0405f', '38244437-8e3f-4945-8284-137fc00ce92d', 'd2b88a70-a6b5-4cc0-b353-0ffb71d4ae50', 'fe2858ca-2462-4d2d-a2b4-5bccb0420ebd', '5826bab5-2752-455d-81d0-4365a1ef99cb', '0eb2f160-3ef8-440a-9a25-111c4d42e132', '6997a3b9-8e14-47dd-adb2-9c05cc336966', '6b14ddf8-7fc8-4aa5-8038-6fb4f9cefe8a', '1c80f8f9-ae35-4462-98ce-0649cdc3a4ac', '085b3949-05da-4eaf-b945-230d3c83bbcf', '608432ad-e42e-4be1-9221-671373b58d4c', '37fca073-f651-4c97-ade4-a06329c409de', 'ae699548-b1df-4f22-b84c-3cd377d86560', '4932f4e8-7185-4fe1-ad1c-ccfdfb6efc1a', '4582da08-902b-410d-8991-bfb6ebb8bb60', 'c9422533-a6b5-4685-b999-dc52d7199806', '35456d9b-cd8d-4b8a-b861-02bdb5a3c0d7']
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
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_edit1_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    from_pos = (380, 770)
    destination = (50, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 50, 770)
    with step('[Verify] snapshot: 05_08_01_before_text.png'):
        actions.capture_for_gt('05_08_01_before_text.png')
    if actions.is_element_present(AppiumBy.NAME, 'xpromo btn close n', timeout=2):
        with step('[Action] tap_close_xpromo_btn'):
            actions.tap_by_locator(AppiumBy.NAME, 'xpromo btn close n')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTextEdit')
    with step('[Verify] snapshot: 05_08_01_keyboard.png'):
        actions.capture_for_gt('05_08_01_keyboard.png')
    if actions.compare_with_gt('05_08_01_keyboard.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare keyboard fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'A')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'a')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'a')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Return')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'A')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next keyboard')
    with step('[Verify] snapshot: 05_08_01_change_kb_lan.png'):
        actions.capture_for_gt('05_08_01_change_kb_lan.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next keyboard')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leftAlignmentButton')
    with step('[Verify] snapshot: 05_08_01_input_align_left.png'):
        actions.capture_for_gt('05_08_01_input_align_left.png')
    if actions.compare_with_gt('05_08_01_input_align_left.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare align left fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'centerAlignmentButton')
    with step('[Verify] snapshot: 05_08_01_input_align_center.png'):
        actions.capture_for_gt('05_08_01_input_align_center.png')
    if actions.compare_with_gt('05_08_01_input_align_center.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare align center fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'rightAlignmentButton')
    with step('[Verify] snapshot: 05_08_01_input_align_right.png'):
        actions.capture_for_gt('05_08_01_input_align_right.png')
    with step('[Verify] compare: 05_08_01_input_align_right.png'):
        assert actions.compare_with_gt('05_08_01_input_align_right.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn top done n')
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Font')
    with step('[Verify] snapshot: 05_08_01_og.png'):
        actions.capture_for_gt('05_08_01_og.png')
    handle = actions.get_element_bounds(AppiumBy.ACCESSIBILITY_ID, 'imgView')
    from_pos = (handle[0] + handle[2] // 2 - 30, handle[1] + handle[3] // 2)
    destination = (handle[0] + handle[2] // 2, from_pos[1] + 80)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(from_pos[0], from_pos[1], destination[0], destination[1])
    with step('[Verify] snapshot: 05_08_01_move.png'):
        actions.capture_for_gt('05_08_01_move.png')
    if actions.compare_with_gt('05_08_01_move.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare move fail'
    with step('[Verify] snapshot: 05_08_01_after_move.png'):
        actions.capture_for_gt('05_08_01_after_move.png')
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_08_01_undo.png'):
        actions.capture_for_gt('05_08_01_undo.png')
    if actions.compare_with_gt('05_08_01_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo comparison fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_08_01_redo.png'):
        actions.capture_for_gt('05_08_01_redo.png')
    if actions.compare_with_gt('05_08_01_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo comparison fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    destination = (150, 270)
    with step('[Verify] snapshot: 05_08_01_before_rotate.png'):
        actions.capture_for_gt('05_08_01_before_rotate.png')
    with step('[Action] drag_text_rotate_n'):
        x, y, width, height = actions.get_element_bounds(AppiumBy.ACCESSIBILITY_ID, 'rotateImageView')
        actions.drag_coordinates(x + width // 2, y + height // 2, destination[0], destination[1])
    with step('[Verify] snapshot: 05_08_01_after_rotate.png'):
        actions.capture_for_gt('05_08_01_after_rotate.png')
    if (not actions.compare_with_gt('05_08_01_after_rotate.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Resize/rotate comparison fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_08_01_undo_rotate.png'):
        actions.capture_for_gt('05_08_01_undo_rotate.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDuplicate')
    with step('[Verify] snapshot: 05_08_01_duplicate.png'):
        actions.capture_for_gt('05_08_01_duplicate.png')
    if actions.compare_with_gt('05_08_01_duplicate.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare duplicate fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: base05_08_01_undo_duplicate.png'):
        actions.capture_for_gt('base05_08_01_undo_duplicate.png')
    with step('[Verify] snapshot: base05_08_01_dre_focus_text.png'):
        actions.capture_for_gt('base05_08_01_dre_focus_text.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTextEdit')
    with step('[Verify] snapshot: 05_08_01_edit_keyboard.png'):
        actions.capture_for_gt('05_08_01_edit_keyboard.png')
    if actions.compare_with_gt('05_08_01_edit_keyboard.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare edit keyboard fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.NAME, 'btn top cancel p')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step('[Verify] snapshot: 05_08_01_delete.png'):
        actions.capture_for_gt('05_08_01_delete.png')
    if actions.compare_with_gt('05_08_01_delete.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare delete fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_08_01_before_erase.png'):
        actions.capture_for_gt('05_08_01_before_erase.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'maskButton')
    from_pos = (205, 300)
    destination = (205, 511)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(205, 300, 205, 511)
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_08_01_after_erase.png'):
        actions.capture_for_gt('05_08_01_after_erase.png')
    if not actions.compare_with_gt('05_08_01_after_erase.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Eraser comparison fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n')
    with step('[Verify] snapshot: 05_08_01_before_brush_page.png'):
        actions.capture_for_gt('05_08_01_before_brush_page.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'maskButton')
    from_pos = (122, 378)
    destination = (386, 511)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(122, 378, 386, 511)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') == '50'):
        pass
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('8', '9', '10', '11', '12')):
        pass
    else:
        assert False, 'Min slider value verification fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'Max slider value verification fail'
    with step('[Verify] snapshot: 05_08_01_before_brush.png'):
        actions.capture_for_gt('05_08_01_before_brush.png')
    from_pos = (122, 378)
    destination = (386, 511)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(122, 378, 386, 511)
    with step('[Verify] snapshot: base05_08_01_brush.png'):
        actions.capture_for_gt('base05_08_01_brush.png')
    with step('[Verify] snapshot: 05_08_01_after_brush.png'):
        actions.capture_for_gt('05_08_01_after_brush.png')
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_08_01_undo_brush.png'):
        actions.capture_for_gt('05_08_01_undo_brush.png')
    if actions.compare_with_gt('05_08_01_undo_brush.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo brush comparison fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_08_01_redo_brush.png'):
        actions.capture_for_gt('05_08_01_redo_brush.png')
    if (not actions.compare_with_gt('05_08_01_redo_brush.png', gt_folder=TD.GT_FOLDER)[0]):
        assert False, 'Redo brush comparison fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_08_01_brush_page_x.png'):
        actions.capture_for_gt('05_08_01_brush_page_x.png')
    if actions.compare_with_gt('05_08_01_brush_page_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'X of brush page comparison fail'
    with step("[Verify] test_00099 completion"):
        assert True
