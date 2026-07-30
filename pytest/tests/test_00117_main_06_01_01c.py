import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00117_main_06_01_01c')
def test_00117_main_06_01_01c(actions: DriverActions):
    """cutout"""
    mode = 1
    uuid = ['28fe5a6b-1dd2-11b2-8000-080027b246c3', '1307edf0-b500-4b73-a2b0-c1592cdea7e2', '20f487ac-e6ee-4be8-b8ec-ace5f2399302', '28fe5a6b-1dd2-11b2-8001-080027b246c3', 'bf9a4f7c-6560-4178-890a-4b7c55866470', '354e586a-8a5b-443f-911c-38606c0c3a80', '28fe5a6b-1dd2-11b2-8002-080027b246c3', '3ece6ae8-1649-44bb-a16d-2cf298b4ae2b', 'c3018ce5-0e3f-4e90-91ba-b3a7fe460f48', '187eef17-12b9-428c-a248-b522cb1fc38d', 'f893f210-8bee-4d2a-a0ea-e02d0c954442', '64737b76-bfe8-4920-afb0-26f536ac0082', '251ce181-3a05-4c05-a83b-2610e66b6cf2', '7cb29b7a-e11d-4635-8657-7c952b623ddd', '5ca1e35f-4e43-4717-8bbe-f629fe1bb54f', 'b19b7283-e7ca-4e00-97af-451fe41afde6', '2629e550-3bf6-4b1d-8753-7254c326fb34', '4d8489c2-d231-4724-8115-209644902086', '7b49d0a7-039e-405d-960c-a2ccd4b35d75', 'e3dd373e-0f4d-4def-a768-b5819c8c492a', 'ef1aa345-e9f1-4580-a353-b2201dcc302d', '2fee556f-baa2-41d1-bcd8-209221f73948', '35b6e1ca-1dd2-11b2-8000-080027b246c3', '35b6e1ca-1dd2-11b2-8001-080027b246c3', '35b6e1ca-1dd2-11b2-8002-080027b246c3', '35b6e1ca-1dd2-11b2-8003-080027b246c3', '35b6e1ca-1dd2-11b2-8004-080027b246c3', '35b6e1ca-1dd2-11b2-8005-080027b246c3', '35b6e1ca-1dd2-11b2-8006-080027b246c3', '35b6e1ca-1dd2-11b2-8007-080027b246c3', '35b6e1ca-1dd2-11b2-8008-080027b246c3', '35b6e1ca-1dd2-11b2-8009-080027b246c3', '35b6e1ca-1dd2-11b2-800a-080027b246c3', '35b6e1ca-1dd2-11b2-800b-080027b246c3', '35b6e1ca-1dd2-11b2-800c-080027b246c3', '35b6e1ca-1dd2-11b2-800d-080027b246c3', '35b6e1ca-1dd2-11b2-800e-080027b246c3', '35b6e1ca-1dd2-11b2-800f-080027b246c3', '35b6e1ca-1dd2-11b2-8010-080027b246c3', '35b6e1ca-1dd2-11b2-8011-080027b246c3', '35b6e1ca-1dd2-11b2-8012-080027b246c3', '35b6e1ca-1dd2-11b2-8013-080027b246c3', '35b6e1ca-1dd2-11b2-8014-080027b246c3', '35b6e1ca-1dd2-11b2-8015-080027b246c3', '35b6e1ca-1dd2-11b2-8016-080027b246c3', 'b9d2b56d-05b0-4d63-a167-174455f03fb1', 'fe67cdbf-84a8-4565-875b-38f0c3582ba6', '99ccf6b2-b158-4a1c-804d-2704067db784', 'c28d6a37-b64c-461d-ac8e-adcb83162553', 'c697d1c2-e3f8-45c2-86ac-cec9c4d7002a', '34ab1203-ba56-4e8d-86f1-05e9e7985b70']
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
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Auto'):
        pass
    else:
        assert False, 'default enter mask editing fail'
    from_pos = (80, 150)
    destination = (370, 690)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(80, 150, 370, 690)
    with step('[Verify] snapshot: 06_01_01_box.png'):
        actions.capture_for_gt('06_01_01_box.png')
    if actions.compare_with_gt('06_01_01_box.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'box fail'
    with step('[Action] tap_cutout_mask_button'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[-4]')
    with step('[Verify] snapshot: 06_01_01_reset.png'):
        actions.capture_for_gt('06_01_01_reset.png')
    if actions.compare_with_gt('06_01_01_reset.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'reset fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Circle')
    from_pos = (80, 150)
    destination = (370, 690)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(80, 150, 370, 690)
    with step('[Verify] snapshot: 06_01_01_circle.png'):
        actions.capture_for_gt('06_01_01_circle.png')
    if actions.compare_with_gt('06_01_01_circle.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'circle fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    with step('[Verify] snapshot: 06_01_01c_cutout_brush+_before.png'):
        actions.capture_for_gt('06_01_01c_cutout_brush+_before.png')
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 06_01_01c_cutout_brush+_after.png'):
        actions.capture_for_gt('06_01_01c_cutout_brush+_after.png')
    if (not actions.compare_with_gt('06_01_01c_cutout_brush+_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust brush size fail'
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 06_01_01_before_brush+.png'):
        actions.capture_for_gt('06_01_01_before_brush+.png')
    from_pos = (90, 120)
    destination = (90, 550)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(90, 120, 90, 550)
    with step('[Verify] snapshot: 06_01_01_after_brush+.png'):
        actions.capture_for_gt('06_01_01_after_brush+.png')
    if (not actions.compare_with_gt('06_01_01_after_brush+.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'brush fail'
    with step('[Action] tap_cutout_mask_button'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[-3]')
    with step('[Verify] snapshot: 06_01_01_undo.png'):
        actions.capture_for_gt('06_01_01_undo.png')
    if actions.compare_with_gt('06_01_01_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo fail'
    with step('[Action] tap_cutout_mask_button'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[-2]')
    with step('[Verify] snapshot: 06_01_01_redo.png'):
        actions.capture_for_gt('06_01_01_redo.png')
    if actions.compare_with_gt('06_01_01_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step('[Verify] snapshot: 06_01_01c_cutout_brush-_before.png'):
        actions.capture_for_gt('06_01_01c_cutout_brush-_before.png')
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 06_01_01c_cutout_brush-_after.png'):
        actions.capture_for_gt('06_01_01c_cutout_brush-_after.png')
    if (not actions.compare_with_gt('06_01_01c_cutout_brush-_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust brush size fail'
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 06_01_01_before_brush-.png'):
        actions.capture_for_gt('06_01_01_before_brush-.png')
    from_pos = (90, 120)
    destination = (90, 550)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(90, 120, 90, 550)
    with step('[Verify] snapshot: 06_01_01_after_brush-.png'):
        actions.capture_for_gt('06_01_01_after_brush-.png')
    if (not actions.compare_with_gt('06_01_01_after_brush-.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'eraser - fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step('[Verify] snapshot: 06_01_01_auto.png'):
        actions.capture_for_gt('06_01_01_auto.png')
    if actions.compare_with_gt('06_01_01_auto.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'auto fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step('[Verify] snapshot: 06_01_01_apply_mask.png'):
        actions.capture_for_gt('06_01_01_apply_mask.png')
    if actions.compare_with_gt('06_01_01_apply_mask.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'apply_mask fail'
    with step('[Verify] snapshot: 06_01_01_mask1.png'):
        actions.capture_for_gt('06_01_01_mask1.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btn edit n')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Auto'):
        pass
    else:
        assert False, 'enter mask editing fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    from_pos = (90, 120)
    destination = (250, 550)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(90, 120, 250, 550)
    with step('[Action] tap_cutout_mask_button'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[-5]')
    with step('[Verify] snapshot: 06_01_01_mask2.png'):
        actions.capture_for_gt('06_01_01_mask2.png')
    if actions.compare_with_gt('06_01_01_mask2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'edit mask x fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step('[Action] tap_edit1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]')):
        assert False, 'Tap user background fail'
    with step('[Verify] snapshot: 06_01_01_bg_color.png'):
        actions.capture_for_gt('06_01_01_bg_color.png')
    if actions.compare_with_gt('06_01_01_bg_color.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'BG color fail'
    with step('[Action] tap_feature_x_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[3]')):
        assert False, 'Tap color picker fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')):
        assert False, 'Tap v for color picker fail'
    with step('[Verify] snapshot: 06_01_01_bg_color_picker.png'):
        actions.capture_for_gt('06_01_01_bg_color_picker.png')
    if actions.compare_with_gt('06_01_01_bg_color_picker.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'BG color picker fail'
    with step('[Action] tap_feature_x_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[4]')):
        assert False, 'Tap user background fail'
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'BG')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')):
        assert False, 'select photo  BG fail'
    with step('[Verify] snapshot: 06_01_01_user_bg.png'):
        actions.capture_for_gt('06_01_01_user_bg.png')
    if actions.compare_with_gt('06_01_01_user_bg.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'user BG fail'
    with step('[Action] tap_feature_x_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step('[Verify] snapshot: 06_01_01_before_take_shot.png'):
        actions.capture_for_gt('06_01_01_before_take_shot.png')
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[4]')):
        assert False, 'Tap user background fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCamera')):
        assert False, 'tap camera fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')):
        assert False, 'shot photo fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use Photo')):
        assert False, 'use_photo fail'
    with step('[Verify] snapshot: 06_01_01_after_take_photo.png'):
        actions.capture_for_gt('06_01_01_after_take_photo.png')
    if (not actions.compare_with_gt('06_01_01_after_take_photo.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'apply taked photo fail'
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step("[Verify] test_00117 completion"):
        assert True
