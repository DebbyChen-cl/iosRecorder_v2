import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00124_main_05_11_01_6')
def test_00124_main_05_11_01_6(actions: DriverActions):
    """add-image cutout"""
    mode = 1
    uuid = ['2f7f2e6c-1dd2-11b2-8000-080027b246c3', '2f7f2e6c-1dd2-11b2-8001-080027b246c3', '2f7f2e6c-1dd2-11b2-8002-080027b246c3', '2f7f2e6c-1dd2-11b2-8003-080027b246c3', '2f7f2e6c-1dd2-11b2-8004-080027b246c3', '83933c69-4eeb-428d-a587-4638c62b8b43', '66930736-6a6b-4f88-9725-f96583082424', 'a3b283e5-aebd-4577-9270-8703106ee3cf', 'd2bdf663-d017-4ed7-8df2-2941b11678dd', '2f7f2e6c-1dd2-11b2-8005-080027b246c3', 'c121a89c-99b4-4b2f-a66b-f4927ae1049d', '9a63bd29-f398-4446-88e8-9a6cc8b5357e', '3cedbf13-cf32-4599-9ce8-cd0ba31bb619', 'a3b283e5-aebd-4577-9270-8703106ee3cf', '136337ef-bf62-4589-a468-e8169f91c8f0', '50783f34-3202-4994-a27a-d4b3b5ab972b', '8baaee7e-a2a7-4c84-977d-80cdc3a5a6ed']
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
    with step('[Verify] snapshot: 05_11_01_before_cutout.png'):
        actions.capture_for_gt('05_11_01_before_cutout.png')
    from_pos = (360, 780)
    destination = (100, 780)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(360, 780, 100, 780)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step('[Verify] snapshot: 05_11_01_cutout_brush-_before.png'):
        actions.capture_for_gt('05_11_01_cutout_brush-_before.png')
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_11_01_cutout_brush-_after.png'):
        actions.capture_for_gt('05_11_01_cutout_brush-_after.png')
    if (not actions.compare_with_gt('05_11_01_cutout_brush-_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Fail to verify adjust brush size of cutout'
    from_pos = (194, 406)
    destination = (227, 607)
    with step('[Verify] snapshot: 05_11_01_before_brush-.png'):
        actions.capture_for_gt('05_11_01_before_brush-.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(194, 406, 227, 607)
    with step('[Verify] snapshot: 05_11_01_after_brush-.png'):
        actions.capture_for_gt('05_11_01_after_brush-.png')
    if (not actions.compare_with_gt('05_11_01_after_brush-.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Fail to verify eraser -'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    from_pos = (194, 406)
    destination = (227, 607)
    with step('[Verify] snapshot: 05_11_01_before_brush+.png'):
        actions.capture_for_gt('05_11_01_before_brush+.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(194, 406, 227, 607)
    with step('[Verify] snapshot: 05_11_01_after_brush+.png'):
        actions.capture_for_gt('05_11_01_after_brush+.png')
    if (not actions.compare_with_gt('05_11_01_after_brush+.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Fail to verify brush +'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_6')):
        assert False, 'Fail to select stroke template 1'
    with step('[Verify] snapshot: 05_11_01_stroke1.png'):
        actions.capture_for_gt('05_11_01_stroke1.png')
    if actions.compare_with_gt('05_11_01_stroke1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Fail to verify stroke template 1'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-3')):
        assert False, 'Fail to change stroke color'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')):
        assert False, 'Fail to adjust stroke thickness slider'
    with step('[Verify] snapshot: 05_11_01_stroke1_after.png'):
        actions.capture_for_gt('05_11_01_stroke1_after.png')
    if actions.compare_with_gt('05_11_01_stroke1_after.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'stroke1_after comparison failed'
    with step('[Action] tap_done_btn'):
        assert actions.try_tap_any([
            (AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'),
            (AppiumBy.NAME, 'btnDone'),
            (AppiumBy.NAME, 'btn ok n'),
            (AppiumBy.ACCESSIBILITY_ID, 'doneButton'),
        ]), 'test failed'
    with step('[Action] focus_added_image'):
        assert actions.tap_by_coordinates(205, 400), 'Fail to tap on added image to focus'
    with step('[Verify] snapshot: 05_11_01_6_before_brush_page.png'):
        actions.capture_for_gt('05_11_01_6_before_brush_page.png')
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
        assert False, 'Fail to set brush size to minimum value'
    if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100'))):
        pass
    else:
        assert False, 'Fail to set brush size to maximum value'
    with step('[Verify] snapshot: 05_11_01_6_before_brush.png'):
        actions.capture_for_gt('05_11_01_6_before_brush.png')
    from_pos = (300, 200)
    destination = (170, 500)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(300, 200, 170, 500)
    with step('[Verify] snapshot: 05_11_01_6_after_brush.png'):
        actions.capture_for_gt('05_11_01_6_after_brush.png')
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_11_01_6_undo_brush.png'):
        actions.capture_for_gt('05_11_01_6_undo_brush.png')
    if actions.compare_with_gt('05_11_01_6_undo_brush.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Fail to verify undo brush operation'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_11_01_6_redo_brush.png'):
        actions.capture_for_gt('05_11_01_6_redo_brush.png')
    if actions.compare_with_gt('05_11_01_6_redo_brush.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Fail to verify redo brush operation'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_11_01_6_brush_page_x.png'):
        actions.capture_for_gt('05_11_01_6_brush_page_x.png')
    if actions.compare_with_gt('05_11_01_6_brush_page_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Fail to verify X button closes brush page correctly'
    with step("[Verify] test_00124 completion"):
        assert True
