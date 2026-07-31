import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00114_main_06_01_01a')
def test_00114_main_06_01_01a(actions: DriverActions):
    """pen tools - brush / magic brush"""
    mode = 1
    uuid = ['ec3028cc-8db8-4645-9847-2bf4b3e6d856', '25c26bcc-f855-43e3-9efa-a4ad981fe2f4', '93945bda-5d96-453a-8884-23c9099100f5', 'e6892632-8d54-4b51-8ebf-ffda84dd5902', 'a41a96f1-6ab1-48b1-9c76-8574faf1322c', 'bbe2324e-6434-415f-a5da-b3243382407f', '127d072d-fbca-428d-8f58-c434b2aac716', '3f0e643d-2a9b-4f5c-a9d1-18afcb28688e', 'ecb20be7-18d1-4814-ae18-6e6fff861e5a', '27846c93-f184-468f-a968-cef9a8cdeda8', '5553e3bf-0148-48ca-8de7-44d3c80cc1f3', '55275dd9-af6f-454a-a80e-db039a06c8b4', 'ea07c8e6-6288-4786-a3d2-1e9210b8c252', 'e8750fc7-c4e6-46ef-9711-e93e590f6b95']
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
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]')):
        assert False, 'select mode fail'
    with step('[Verify] snapshot: 06_01_01a_before_brush_mode.png'):
        actions.capture_for_gt('06_01_01a_before_brush_mode.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    from_pos = (50, 100)
    destination = (370, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 100, 370, 600)
    with step('[Verify] snapshot: 06_01_01a_brush_mode.png'):
        actions.capture_for_gt('06_01_01a_brush_mode.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    if actions.compare_with_gt('06_01_01a_brush_mode.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'brush mode 0 fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False, 'tap undo fail'
    with step('[Verify] snapshot: 06_01_01a_undo_brush_mode.png'):
        actions.capture_for_gt('06_01_01a_undo_brush_mode.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    if actions.compare_with_gt('06_01_01a_undo_brush_mode.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo fail'
    with step('[Verify] snapshot: 06_01_01a_before_brush_color.png'):
        actions.capture_for_gt('06_01_01a_before_brush_color.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')):
        assert False, 'tap color fail'
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]')):
        assert False, 'select color fail'
    from_pos = (50, 100)
    destination = (370, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 100, 370, 600)
    from_pos = (370, 100)
    destination = (40, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(370, 100, 40, 600)
    with step('[Verify] snapshot: 06_01_01a_brush_color.png'):
        actions.capture_for_gt('06_01_01a_brush_color.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    if actions.compare_with_gt('06_01_01a_brush_color.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'brush color 0 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')):
        assert False, 'tap clear fail'
    with step('[Verify] snapshot: 06_01_01a_clear_brush_color.png'):
        actions.capture_for_gt('06_01_01a_clear_brush_color.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    if actions.compare_with_gt('06_01_01a_clear_brush_color.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'clear fail'
    with step('[Verify] snapshot: 06_01_01a_before_brush_size.png'):
        actions.capture_for_gt('06_01_01a_before_brush_size.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    with step('[Action] adjust_harmonization_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    from_pos = (50, 100)
    destination = (370, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 100, 370, 600)
    with step('[Verify] snapshot: 06_01_01a_brush_size.png'):
        actions.capture_for_gt('06_01_01a_brush_size.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    if actions.compare_with_gt('06_01_01a_brush_size.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'brush size 0 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'tap x fail'
    with step('[Verify] snapshot: 06_01_01a_tap_x.png'):
        actions.capture_for_gt('06_01_01a_tap_x.png')
    if actions.compare_with_gt('06_01_01a_tap_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tap x fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    from_pos = (50, 100)
    destination = (370, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 100, 370, 600)
    from_pos = (370, 100)
    destination = (50, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(370, 100, 50, 600)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn brush n')):
        assert False, 'tap erase fail'
    with step('[Action] adjust_harmonization_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 06_01_01a_before_erase_size.png'):
        actions.capture_for_gt('06_01_01a_before_erase_size.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    from_pos = (50, 100)
    destination = (370, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 100, 370, 600)
    with step('[Verify] snapshot: 06_01_01a_erase_size.png'):
        actions.capture_for_gt('06_01_01a_erase_size.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    if actions.compare_with_gt('06_01_01a_erase_size.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'erase size 0 fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'tap v fail'
    with step('[Verify] snapshot: 06_01_01a_tap_v.png'):
        actions.capture_for_gt('06_01_01a_tap_v.png')
    if (not actions.compare_with_gt('06_01_01a_tap_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'txp v fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 06_01_01b_before_enter_magic.png'):
        actions.capture_for_gt('06_01_01b_before_enter_magic.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Magic Brush')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Neon')):
        assert False, 'select magic style fail'
    with step('[Verify] snapshot: 06_01_01b_before_magic.png'):
        actions.capture_for_gt('06_01_01b_before_magic.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    from_pos = (50, 100)
    destination = (570, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 100, 570, 600)
    with step('[Verify] snapshot: 06_01_01b_magic.png'):
        actions.capture_for_gt('06_01_01b_magic.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    if actions.compare_with_gt('06_01_01b_magic.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'magic rush 0 fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False, 'tap undo fail'
    with step('[Verify] snapshot: 06_01_01b_undo_magic.png'):
        actions.capture_for_gt('06_01_01b_undo_magic.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    with step('[Verify] compare: 06_01_01b_undo_magic.png'):
        assert actions.compare_with_gt('06_01_01b_undo_magic.png', gt_folder=TD.GT_FOLDER)[0]
    from_pos = (50, 100)
    destination = (370, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 100, 370, 600)
    from_pos = (370, 100)
    destination = (40, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(370, 100, 40, 600)
    with step('[Verify] snapshot: 06_01_01b_magic_before_erase.png'):
        actions.capture_for_gt('06_01_01b_magic_before_erase.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn brush n')):
        assert False, 'tap eraser fail'
    from_pos = (50, 100)
    destination = (370, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 100, 370, 600)
    with step('[Verify] snapshot: 06_01_01b_magic_after_erase.png'):
        actions.capture_for_gt('06_01_01b_magic_after_erase.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    if actions.compare_with_gt('06_01_01b_magic_after_erase.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'erase fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')):
        assert False, 'tap clear fail'
    with step('[Verify] snapshot: 06_01_01b_clear_magic.png'):
        actions.capture_for_gt('06_01_01b_clear_magic.png', AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeImage')
    with step('[Verify] compare: 06_01_01b_clear_magic.png'):
        assert actions.compare_with_gt('06_01_01b_clear_magic.png', gt_folder=TD.GT_FOLDER)[0]
    from_pos = (50, 100)
    destination = (370, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 100, 370, 600)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'tap x fail'
    with step('[Verify] snapshot: 06_01_01b_tap_x.png'):
        actions.capture_for_gt('06_01_01b_tap_x.png')
    if actions.compare_with_gt('06_01_01b_tap_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tap x fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Magic Brush')
    from_pos = (50, 100)
    destination = (370, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 100, 370, 600)
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'tap v fail'
    with step('[Verify] snapshot: 06_01_01b_tap_v.png'):
        actions.capture_for_gt('06_01_01b_tap_v.png')
    if (not actions.compare_with_gt('06_01_01b_tap_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'tap v fail'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00114 completion"):
        assert True
