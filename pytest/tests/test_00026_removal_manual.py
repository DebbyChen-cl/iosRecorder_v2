import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00026_removal_manual')
def test_00026_removal_manual(actions: DriverActions):
    """removal - manual"""
    mode = 1
    uuid = ['d4f06494-5d67-4d1c-b1b8-71cadbcf72e1', '4bb879a8-1039-4ba9-82d2-1f347c0e9817', '1064c782-d448-4044-8d68-ed0a799a4492', '45871133-6a98-4e0a-ac1d-a3602d42b92d', '5b2c27cd-6b54-47a6-856d-e133c76f8a10', '91c8fba9-6f1c-448f-8848-d22a963ccc45', '14625380-842b-43db-949b-6313d32f491d', 'edbc569a-2d50-4948-a175-ebcadc8607cc', 'a7e6f0e3-386a-4c62-8c50-2d41adf106ab', 'c6d321b3-e4d0-49b9-a37c-8a800bde0210', '76774317-1f08-4488-bfc2-6fef0b44bfad', '4410d745-9496-40c7-afc1-65ecc7283dde', '6499b7bd-3ec6-45a9-8fdc-10e7cf113b84', '80f4e7d6-4ff6-4757-b768-5083e4d86105', '21d6d66b-0240-4050-b4c2-a244efad0d34', '8ab17e86-21ed-4db6-97d1-622d2c708f21', '602cf00d-f0bf-40b3-93b8-e46d11b617ae', '3ee8746f-fdd0-43ed-a7ec-2e610c044f24', '7744e8c0-2fac-4c85-a7f5-2152d846de21']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')
    with step('[Action] close_airemoval_iap_dialog'):
        actions.is_element_present(AppiumBy.NAME, 'Remove with faster selection tool')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
        actions.wait_for_invisible(AppiumBy.NAME, 'Remove with faster selection tool')
    with step('[Action] close_airemoval_iap_dialog'):
        actions.is_element_present(AppiumBy.NAME, 'Remove with faster selection tool')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
        actions.wait_for_invisible(AppiumBy.NAME, 'Remove with faster selection tool')
    with step('[Action] close_airemoval_iap_dialog2'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Manual')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_01_03_brushsize_before.png'):
        actions.capture_for_gt('05_01_03_brushsize_before.png', crop_rect=(0, 725, 367, 783))
    with step('[Action] adjust_removal_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_removal_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_01_03_brushsize_after.png'):
        actions.capture_for_gt('05_01_03_brushsize_after.png', crop_rect=(0, 725, 367, 783))
    if (not actions.compare_with_gt('05_01_03_brushsize_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust brush size fail'
    from_pos = (360, 300)
    destination = (360, 702)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(360, 300, 360, 702)
    with step('[Verify] snapshot: 05-01-03_removal_mask1.png'):
        actions.capture_for_gt('05-01-03_removal_mask1.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    from_pos = (250, 300)
    destination = (250, 702)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(250, 300, 250, 702)
    with step('[Verify] snapshot: 05-01-03_removal_brush+.png'):
        actions.capture_for_gt('05-01-03_removal_brush+.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Verify] snapshot: 05-01-03_removal_mask2.png'):
        actions.capture_for_gt('05-01-03_removal_mask2.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05-01-03_removal_undo_mask.png'):
        actions.capture_for_gt('05-01-03_removal_undo_mask.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if actions.compare_with_gt('05-01-03_removal_undo_mask.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo brush fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'redoButton')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05-01-03_removal_redo_mask.png'):
        actions.capture_for_gt('05-01-03_removal_redo_mask.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    assert actions.compare_with_gt('05-01-03_removal_redo_mask.png', gt_folder=TD.GT_FOLDER)[0]
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')):
        pass
    from_pos = (250, 300)
    destination = (250, 702)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(250, 300, 250, 702)
    actions.capture_for_gt('base05-01-03_removal_brush-.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Verify] snapshot: 05-01-03_before_remove1.png'):
        actions.capture_for_gt('05-01-03_before_remove1.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'applyButton')):
        assert False  # legacy raise
    with step('[Action] wait_remove_process'):
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'magicText')
    actions.capture_for_gt('base05-01-03_removal_result.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Verify] snapshot: 05-01-03_removal_result2.png'):
        actions.capture_for_gt('05-01-03_removal_result2.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    actions.capture_for_gt('05-01-03_undo_remove.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    assert actions.compare_with_gt('05-01-03_undo_remove.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_redo_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'redoButton')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'tap [x] fail'
    with step('[Verify] snapshot: 05-01-03_tap_x.png'):
        actions.capture_for_gt('05-01-03_tap_x.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')
    with step('[Action] close_airemoval_iap_dialog'):
        actions.is_element_present(AppiumBy.NAME, 'Remove with faster selection tool')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
        actions.wait_for_invisible(AppiumBy.NAME, 'Remove with faster selection tool')
    with step('[Action] close_airemoval_iap_dialog2'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Manual')
    with step('[Action] adjust_removal_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_removal_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    from_pos = (250, 300)
    destination = (250, 702)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(250, 300, 250, 702)
    from_pos = (200, 300)
    destination = (200, 702)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(200, 300, 200, 702)
    from_pos = (150, 300)
    destination = (150, 702)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(150, 300, 150, 702)
    from_pos = (50, 300)
    destination = (280, 300)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(50, 300, 280, 300)
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'applyButton')
    with step('[Action] wait_remove_process'):
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'magicText')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, 'tap [v] fail'
    with step("[Verify] test_00026 completion"):
        assert True
