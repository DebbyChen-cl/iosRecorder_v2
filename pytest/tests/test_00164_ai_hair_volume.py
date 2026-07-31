import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00164_ai_hair_volume')
def test_00164_ai_hair_volume(actions: DriverActions):
    """AI hair volume"""
    uuid = ['e31346bd-147c-4324-8777-9c6ab28eaffe', '1c374574-adc7-4cdd-ad9e-d7c8dfce50e5', '1ffc2e7b-62db-477f-b272-d6261be2c9f8', '9c8e7120-4ed8-42b8-a86d-4c6231dca0ec', '41f56f62-de05-406b-a8b2-743ee9ac366f', '662e1465-28b6-4f0c-89ef-7efff1756ae6', '1cb19500-59a6-42af-9d7a-38cf8d3c015b', '31be13d0-7526-4780-b1c2-ea25949ff698', '0040bfb5-67c7-4291-925a-334b0dcdcc1a', '8a931463-58a5-424c-8878-3645db23d531', '782a376b-9ff3-41d7-adf3-6ab542526366', '1559f3ce-f00f-4e24-a62e-e4d4380249b2', '01963044-1603-4a73-847f-5b7ecea50137', '5259a7f8-bf9c-4199-86d7-1f81ce9afa02', 'd48cbb79-2dde-4adb-b1de-6b10816a1c3a', '8c96e0a9-d494-4e65-aeb4-ec64d8de06d9', 'a0ed6747-9536-4e27-bc59-f739e43b54ff']
    with step('[Action] close_backup_dialog'):
        if actions.is_element_present(AppiumBy.NAME, 'Cloud Backup Expired'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
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
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Verify] snapshot: G02_01_05_before_hairvolume.png'):
        actions.capture_for_gt('G02_01_05_before_hairvolume.png')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hair')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hair Volume')
    if (actions.is_element_present(AppiumBy.NAME, 'The face in the chosen photo is either too small or blurry. This may result in a poor face swap or unexpected defects in the photo. We recommended using a larger photo where the face is clearer.')
            or actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'The face in this photo is too small or blurry, which may result in poorly generated results.')
            or actions.is_element_present(AppiumBy.NAME, 'We cannot locate any faces in the chosen photo. Faces in the chosen photo may be too small.')):
        pass
    else:
        assert False, '[G02_02_05] Failed to verify small face dialog'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK'), '[G02_02_05] Failed to tap_ok2_btn'
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Edit'):
        pass
    else:
        assert False, '[G02_02_05] Failed to verify tab_edit after tap OK'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hair')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hair Volume')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway')
    with step('[Verify] snapshot: G02_02_05_no_style.png'):
        actions.capture_for_gt('G02_02_05_no_style.png')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Subtle'), '[G02_02_05] Failed to select_hairvolume 1'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate'), '[G02_02_05] Failed to tap generate_ai for subtle'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    actions.capture_for_gt('G02_02_05_style1.png')
    if (not actions.compare_with_gt('G02_02_05_style1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, '[G02_02_05] Compare fail for subtle'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Natural'), '[G02_02_05] Failed to select_hairvolume 2'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate'), '[G02_02_05] Failed to tap generate_ai for natural'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    actions.capture_for_gt('G02_02_05_style2.png')
    if (not actions.compare_with_gt('G02_02_05_style2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, '[G02_02_05] Compare fail for natural'
    assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]), '[G02_02_05] Failed to tap_undo_btn_n'
    actions.capture_for_gt('G02_02_05_undo.png')
    if actions.compare_with_gt('G02_02_05_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[G02_02_05] Compare fail for undo'
    assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]), '[G02_02_05] Failed to tap_redo_btn_n'
    actions.capture_for_gt('G02_02_05_redo.png')
    if actions.compare_with_gt('G02_02_05_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[G02_02_05] Compare fail for redo'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Medium'), '[G02_02_05] Failed to select_hairvolume 3'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate'), '[G02_02_05] Failed to tap generate_ai for medium'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    actions.capture_for_gt('G02_02_05_style3.png')
    if (not actions.compare_with_gt('G02_02_05_style3.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, '[G02_02_05] Compare fail for medium'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'High'), '[G02_02_05] Failed to select_hairvolume 4'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate'), '[G02_02_05] Failed to tap generate_ai for high'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    actions.capture_for_gt('G02_02_05_style4.png')
    if (not actions.compare_with_gt('G02_02_05_style4.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, '[G02_02_05] Compare fail for high'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Maximized'), '[G02_02_05] Failed to select_hairvolume 5'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate'), '[G02_02_05] Failed to tap generate_ai for max'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    actions.capture_for_gt('G02_02_05_style5.png')
    if (not actions.compare_with_gt('G02_02_05_style5.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, '[G02_02_05] Compare fail for max'
    assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btnReset'), (AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n'), (AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset')]), '[G02_02_05] Failed to tap_reset_btn2'
    actions.capture_for_gt('G02_02_05_reset.png')
    if actions.compare_with_gt('G02_02_05_reset.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[G02_02_05] Compare fail for reset'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btnCancel'), (AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n'), (AppiumBy.NAME, 'btn cancel n'), (AppiumBy.NAME, 'btn top cancel p')]), '[G02_02_05] Failed to tap_feature_x_btn'
    actions.capture_for_gt('G02_02_05_x.png')
    if actions.compare_with_gt('G02_02_05_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[G02_02_05] Compare fail for x'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hair')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hair Volume'), '[G02_02_05] Failed to tap hairvolume for v'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway')
    with step('[Action] select_hairvolume'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'High')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate'), '[G02_02_05] Failed to tap generate_ai for v'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]), '[G02_02_05] Failed to tap_done_btn'
    actions.capture_for_gt('G02_02_05_v.png')
    if (not actions.compare_with_gt('G02_02_05_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, '[G02_02_05] Compare fail for v'
    assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]), '[G02_02_05] Failed to tap_edit_home'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard'), '[G02_02_05] Failed to tap discard'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos'), '[G02_02_05] Failed to tap ai_photos'
    actions.scroll('up')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hair Volume'), '[G02_02_05] Failed to tap hairvolume from ai magic'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue'), '[G02_02_05] Failed to tap continue'
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    actions.tap_by_coordinates(180, 75)
    with step('[Verify] snapshot: G02_02_05_face1_og.png'):
        actions.capture_for_gt('G02_02_05_face1_og.png')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'High'), '[G02_02_05] Failed to select_hairvolume 4 for face 1'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate'), '[G02_02_05] Failed to tap generate_ai for face 1'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    actions.capture_for_gt('G02_02_05_face1.png')
    if (not actions.compare_with_gt('G02_02_05_face1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, '[G02_02_05] Compare fail for face 1'
    actions.tap_by_coordinates(230, 75)
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'High'), '[G02_02_05] Failed to select_hairvolume 4 for face 2'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate'), '[G02_02_05] Failed to tap generate_ai for face 2'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    actions.capture_for_gt('G02_02_05_face2.png')
    if (not actions.compare_with_gt('G02_02_05_face2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, '[G02_02_05] Compare fail for face 2'
    with step("[Verify] test_00164 completion"):
        assert True
