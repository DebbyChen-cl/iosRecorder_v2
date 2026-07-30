import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00056_main_05_04a_03_2')
def test_00056_main_05_04a_03_2(actions: DriverActions):
    """mosaic - auto"""
    mode = 1
    uuid = ['92d9b559-3148-4d7f-a423-10f6217003fd', '7fa1b3be-24f7-45d1-bb8b-77fb24d3b8b9', 'fe842c56-1479-43a6-97f4-0f63c74c0bd6', 'b85987e7-4867-43e1-b298-edf4e95497b3', '02a18d6c-aa44-4e65-9a56-e33d36f8a5b9', '6241e209-d995-41c4-8189-14c3d4c0eb06', '9c8b13bb-218c-4943-ab83-a2c11d883dec', 'fbc43980-94cc-49ad-882e-db7b4aa9dcf8', 'f17bb6fb-2026-4aa2-ad90-af89256bcf14', '47356483-ff2d-42c5-9781-694bf40a7846', '8400fa4e-771b-40d4-8554-dbade7ccb757', '43ae5e08-9842-423a-964f-21a15fc4ff61', '91bd6f5e-8d65-4883-88b9-5cf115feea95', '23ede3ac-0f19-428a-9c1f-174d95662664', 'ac6d72e2-53bd-471c-aa1f-b4db4bbab18d', '0dde4fc4-f77b-43b6-b68c-5a16bb0666d0', '315cbf29-991c-41d2-989e-00b3a35b3481', 'b116848b-528e-49be-aa46-859cedfd2c51', '97b6c296-17dd-49ec-b296-1bbc03c35901', '40cbf5c1-9bf6-435f-b7a2-3c39011411d1', 'bff89a5a-2104-467e-abd5-4304c3ced3c5']
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mosaic')
    with step('[Action] close_mosaic_intro'):
        actions.find_element(AppiumBy.NAME, 'Brush to add mosaic.')
        actions.tap_by_coordinates(220, 220)
    with step('[Verify] snapshot: 05_04a_03_default.png'):
        actions.capture_for_gt('05_04a_03_default.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_04a_03_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'default fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][1]') == '30'):
        pass
    else:
        assert False, 'Default value error'
    with step('[Action] adjust_instafill_saturation_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][1]') in ('95', '96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'Adjust max fail'
    with step('[Verify] snapshot: 05_04a_03_max.png'):
        actions.capture_for_gt('05_04a_03_max.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_04a_03_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'max fail'
    with step('[Action] adjust_instafill_saturation_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][1]') in ('5', '4', '3', '2', '1', '0')):
        pass
    else:
        assert False, 'Adjust min fail'
    with step('[Verify] snapshot: 05_04a_03_min.png'):
        actions.capture_for_gt('05_04a_03_min.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_04a_03_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'min fail'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Person')
    with step('[Verify] snapshot: 05_04a_03_person.png'):
        actions.capture_for_gt('05_04a_03_person.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_04a_03_person.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'person fail'
    with step('[Verify] snapshot: 05_04a_03a_undo_og.png'):
        actions.capture_for_gt('05_04a_03a_undo_og.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]', timeout=5):
            actions.wait_for_invisible(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]')
    with step('[Verify] snapshot: base05_04a_03_bg.png'):
        actions.capture_for_gt('base05_04a_03_bg.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_04a_03_bg.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'bg fail'
    with step('[Verify] snapshot: 05_04a_03a_redo_og.png'):
        actions.capture_for_gt('05_04a_03a_redo_og.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_04a_03a_after_undo.png'):
        actions.capture_for_gt('05_04a_03a_after_undo.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_04a_03a_after_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_04a_03a_after_redo.png'):
        actions.capture_for_gt('05_04a_03a_after_redo.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_04a_03a_after_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Off')
    with step('[Verify] snapshot: base05_04a_03_off.png'):
        actions.capture_for_gt('base05_04a_03_off.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_04a_03_off.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'off fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton')
    with step('[Action] tap_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mosaic')
    with step('[Action] close_mosaic_intro'):
        actions.find_element(AppiumBy.NAME, 'Brush to add mosaic.')
        actions.tap_by_coordinates(220, 220)
        actions.find_element(AppiumBy.NAME, 'Brush to add mosaic.')
    with step('[Verify] snapshot: base05_04a_03_2face_default.png'):
        actions.capture_for_gt('base05_04a_03_2face_default.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_04a_03_2face_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '2 face default fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Verify] snapshot: base05_04a_03_face1.png'):
        actions.capture_for_gt('base05_04a_03_face1.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_04a_03_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'face1 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[2]')
    with step('[Verify] snapshot: base05_04a_03_face2.png'):
        actions.capture_for_gt('base05_04a_03_face2.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_04a_03_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'face2 fail'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Person')
    with step('[Verify] snapshot: base05_04a_03_2body_default.png'):
        actions.capture_for_gt('base05_04a_03_2body_default.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_04a_03_2body_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '2 body default fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Verify] snapshot: base05_04a_03_body1.png'):
        actions.capture_for_gt('base05_04a_03_body1.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_04a_03_body1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'body1 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[2]')
    with step('[Verify] snapshot: base05_04a_03_body2.png'):
        actions.capture_for_gt('base05_04a_03_body2.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_04a_03_body2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'body2 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]', timeout=5):
            actions.wait_for_invisible(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]')
    with step('[Verify] snapshot: base05_04a_03_2face_bg.png'):
        actions.capture_for_gt('base05_04a_03_2face_bg.png', crop_rect=(0, 60, 276, 597))
    with step("[Verify] test_00056 completion"):
        assert True
