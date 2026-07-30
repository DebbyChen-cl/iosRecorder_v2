import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00027_removal_auto')
def test_00027_removal_auto(actions: DriverActions):
    """removal - auto"""
    mode = 1
    uuid = ['e7d2eeed-5513-463e-b80f-0f81f085dc2c', '44374028-b434-439b-9aaa-5f37fc9a83f1', '0c80d203-e38d-423a-8650-f664f10fb00a', 'b91c1c57-afd3-4b5e-838a-072a93279ecd', 'b1cad862-3726-4cda-857e-4db630d6aa28', 'd9a891e4-8919-4d19-b181-80376f527e1c', '7eff47af-0857-4dd2-8331-9d43a4e96338', '11606f03-91b1-483e-978f-24ee0bda09f6', '7133da22-0a14-453e-8592-b0d6e30893f0', 'af9d8887-e930-4287-8d7d-4773a608e3d6', '1f7bbe7a-e0ac-4313-a553-45618df23724', 'ba649b27-bae9-4013-95d8-997ca70c3479', 'd71b25d3-68b9-476b-bd0d-1fc086922caa']
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
    with step('[Action] close_tutorial'):
        actions.is_element_present(AppiumBy.NAME, 'Undo / Redo', timeout=2)
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')
    if actions.is_element_present(AppiumBy.NAME, 'Remove with faster selection tool'):
        pass
    else:
        assert False  # legacy raise
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
    actions.capture_for_gt('base05_01_03_default.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] snapshot: 05_01_03_no_box_mask.png'):
        actions.capture_for_gt('05_01_03_no_box_mask.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    from_pos = (100, 229)
    destination = (360, 702)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(100, 229, 360, 702)
    with step('[Verify] snapshot: 05_01_03_box.png'):
        actions.capture_for_gt('05_01_03_box.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    actions.capture_for_gt('base05_01_03_box.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    actions.capture_for_gt('05_01_03_undo_mask_box.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    assert actions.compare_with_gt('05_01_03_undo_mask_box.png', gt_folder=TD.GT_FOLDER)[0]
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'redoButton')):
        assert False  # legacy raise
    actions.capture_for_gt('05_01_03_redo_mask_box.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    assert actions.compare_with_gt('05_01_03_redo_mask_box.png', gt_folder=TD.GT_FOLDER)[0]
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'applyButton')):
        assert False  # legacy raise
    with step('[Action] wait_remove_process'):
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'magicText')
    with step('[Verify] snapshot: 05_01_03_box_remove.png'):
        actions.capture_for_gt('05_01_03_box_remove.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    actions.capture_for_gt('base05_01_03_box_remove.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])
    actions.capture_for_gt('05_01_03_undo_remove_box.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    assert actions.compare_with_gt('05_01_03_undo_remove_box.png', gt_folder=TD.GT_FOLDER)[0]
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'redoButton')):
        assert False  # legacy raise
    actions.capture_for_gt('05_01_03_redo_remove_box.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    assert actions.compare_with_gt('05_01_03_redo_remove_box.png', gt_folder=TD.GT_FOLDER)[0]
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'resetButton')):
        assert False  # legacy raise
    actions.capture_for_gt('05_01_03_reset_box.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    assert actions.compare_with_gt('05_01_03_reset_box.png', gt_folder=TD.GT_FOLDER)[0]
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Circle')):
        assert False  # legacy raise
    from_pos = (80, 100)
    destination = (360, 633)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(80, 100, 360, 633)
    with step('[Verify] snapshot: 05_01_03_circle.png'):
        actions.capture_for_gt('05_01_03_circle.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    actions.capture_for_gt('base05_01_03_circle.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'applyButton')):
        assert False  # legacy raise
    with step('[Action] wait_remove_process'):
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'magicText')
    with step('[Verify] snapshot: 05_01_03_circle_remove.png'):
        actions.capture_for_gt('05_01_03_circle_remove.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    actions.capture_for_gt('base05_01_03_circle_remove.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'resetButton')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Swipe')):
        assert False  # legacy raise
    from_pos = (208, 166)
    destination = (208, 341)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(208, 166, 208, 341)
    with step('[Verify] snapshot: 05_01_03_swipe.png'):
        actions.capture_for_gt('05_01_03_swipe.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    actions.capture_for_gt('base05_01_03_swipe.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'applyButton')):
        assert False  # legacy raise
    with step('[Action] wait_remove_process'):
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'magicText')
    with step('[Verify] snapshot: 05_01_03_swipe_remove.png'):
        actions.capture_for_gt('05_01_03_swipe_remove.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    actions.capture_for_gt('base05_01_03_swipe_remove.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Verify] test_00027 completion"):
        assert True
