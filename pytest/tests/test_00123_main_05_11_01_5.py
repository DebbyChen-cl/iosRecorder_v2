import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00123_main_05_11_01_5')
def test_00123_main_05_11_01_5(actions: DriverActions):
    """add-image eraser , frame, delete"""
    mode = 1
    uuid = ['19040718-40f0-45b0-b348-f49fb5a2f2a0', '0266a7c9-21c8-48af-96c3-64f4819f6779', 'b381f46c-0d34-4cd0-b918-eb5715589852', 'bb1edaa9-272a-4b63-8a23-3fad27420190', '91b64447-ab63-44cb-aa14-180b710760f1', '629bcf58-e260-41dc-8382-283fc572c2f5', 'dcccbe84-db67-4494-8bb0-da052b13d62e', '50bca1e6-f705-4d36-a62d-ca6a2710e252', '90fee9a7-6aef-4789-a2e8-736a8d639782', 'e530c9e1-cbbe-4a41-b6a0-9e7a25701d9f', '93f1a956-f01a-4546-8049-9b45989217aa', '34d07b56-3c31-47bc-b316-5bca7fdf4bfc']
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
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    destination = (364, 624)
    with step('[Action] drag_add_image_rotate'):
        actions.long_press_drag_from_element_to_coordinates(
            AppiumBy.IOS_CLASS_CHAIN,
            '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]',
            50.0,
            50.0,
            destination[0],
            destination[1],
        )
    with step('[Verify] snapshot: 05_11_01_before_eraser.png'):
        actions.capture_for_gt('05_11_01_before_eraser.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'maskButton')
    from_pos = (60, 150)
    destination = (365, 500)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 150, 365, 500)
    with step('[Verify] snapshot: 05_11_01_brush-.png'):
        actions.capture_for_gt('05_11_01_brush-.png')
    if actions.compare_with_gt('05_11_01_brush-.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'brush- comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    from_pos = (60, 400)
    destination = (300, 400)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 400, 300, 400)
    with step('[Verify] snapshot: 05_11_01_brush+.png'):
        actions.capture_for_gt('05_11_01_brush+.png')
    if actions.compare_with_gt('05_11_01_brush+.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'brush+ comparison failed'
    with step('[Action] tap_done_btn'):
        assert actions.try_tap_any([
            (AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'),
            (AppiumBy.NAME, 'btnDone'),
            (AppiumBy.NAME, 'btn ok n'),
            (AppiumBy.ACCESSIBILITY_ID, 'doneButton'),
        ]), 'test failed'
    with step('[Verify] snapshot: 05_11_01_after_eraser.png'):
        actions.capture_for_gt('05_11_01_after_eraser.png')
    if not actions.compare_with_gt('05_11_01_after_eraser.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'test failed'
    from_pos = (360, 780)
    destination = (100, 780)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(360, 780, 100, 780)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Frame')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Simple Frames')):
        assert False, 'test failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')):
        assert False, 'test failed'
    with step('[Action] tap_done_btn_add_image2'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Verify] snapshot: 05_11_01_after_frame.png'):
        actions.capture_for_gt('05_11_01_after_frame.png')
    if not actions.compare_with_gt('05_11_01_after_frame.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'test failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step('[Verify] snapshot: 05_11_01_after_delete.png'):
        actions.capture_for_gt('05_11_01_after_delete.png')
    if not actions.compare_with_gt('05_11_01_after_delete.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'test failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] focus_added_image'):
        assert actions.tap_by_coordinates(205, 400), 'Fail to focus on added image'
    with step('[Verify] snapshot: 05_11_01_1_before_brush_page.png'):
        actions.capture_for_gt('05_11_01_1_before_brush_page.png')
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
        assert False, 'Fail to verify default brush size'
    if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('8', '9', '10', '11', '12'))):
        pass
    else:
        assert False, 'test failed'
    if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100'))):
        pass
    else:
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_1_before_brush.png'):
        actions.capture_for_gt('05_11_01_1_before_brush.png')
    from_pos = (300, 200)
    destination = (170, 500)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(300, 200, 170, 500)
    with step('[Verify] snapshot: 05_11_01_1_after_brush.png'):
        actions.capture_for_gt('05_11_01_1_after_brush.png')
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_11_01_1_undo_brush.png'):
        actions.capture_for_gt('05_11_01_1_undo_brush.png')
    if actions.compare_with_gt('05_11_01_1_undo_brush.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Fail to verify undo of brush'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_11_01_1_redo_brush.png'):
        actions.capture_for_gt('05_11_01_1_redo_brush.png')
    if actions.compare_with_gt('05_11_01_1_redo_brush.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Fail to verify redo of brush'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_11_01_1_brush_page_x.png'):
        actions.capture_for_gt('05_11_01_1_brush_page_x.png')
    if actions.compare_with_gt('05_11_01_1_brush_page_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Fail to verify x button of brush page'
    with step("[Verify] test_00123 completion"):
        assert True
