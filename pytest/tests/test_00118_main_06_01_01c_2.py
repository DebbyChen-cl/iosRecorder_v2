import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00118_main_06_01_01c_2')
def test_00118_main_06_01_01c_2(actions: DriverActions):
    """stroke"""
    mode = 1
    uuid = ['28fe5a6b-1dd2-11b2-8000-080027b246c3', '1307edf0-b500-4b73-a2b0-c1592cdea7e2', '20f487ac-e6ee-4be8-b8ec-ace5f2399302', '28fe5a6b-1dd2-11b2-8001-080027b246c3', 'bf9a4f7c-6560-4178-890a-4b7c55866470', '354e586a-8a5b-443f-911c-38606c0c3a80', '28fe5a6b-1dd2-11b2-8002-080027b246c3', '3ece6ae8-1649-44bb-a16d-2cf298b4ae2b', 'c3018ce5-0e3f-4e90-91ba-b3a7fe460f48', '187eef17-12b9-428c-a248-b522cb1fc38d', 'f893f210-8bee-4d2a-a0ea-e02d0c954442', '64737b76-bfe8-4920-afb0-26f536ac0082', '251ce181-3a05-4c05-a83b-2610e66b6cf2', '7cb29b7a-e11d-4635-8657-7c952b623ddd', '5ca1e35f-4e43-4717-8bbe-f629fe1bb54f', 'b19b7283-e7ca-4e00-97af-451fe41afde6', '2629e550-3bf6-4b1d-8753-7254c326fb34', '4d8489c2-d231-4724-8115-209644902086', '7b49d0a7-039e-405d-960c-a2ccd4b35d75', 'e3dd373e-0f4d-4def-a768-b5819c8c492a', 'ef1aa345-e9f1-4580-a353-b2201dcc302d', '2fee556f-baa2-41d1-bcd8-209221f73948', '35b6e1ca-1dd2-11b2-8000-080027b246c3', '35b6e1ca-1dd2-11b2-8001-080027b246c3', '35b6e1ca-1dd2-11b2-8002-080027b246c3', '35b6e1ca-1dd2-11b2-8003-080027b246c3', '35b6e1ca-1dd2-11b2-8004-080027b246c3', '35b6e1ca-1dd2-11b2-8005-080027b246c3', '35b6e1ca-1dd2-11b2-8006-080027b246c3', '35b6e1ca-1dd2-11b2-8007-080027b246c3', '35b6e1ca-1dd2-11b2-8008-080027b246c3', '35b6e1ca-1dd2-11b2-8009-080027b246c3', '35b6e1ca-1dd2-11b2-800a-080027b246c3', '35b6e1ca-1dd2-11b2-800b-080027b246c3', '35b6e1ca-1dd2-11b2-800c-080027b246c3', '35b6e1ca-1dd2-11b2-800d-080027b246c3', '35b6e1ca-1dd2-11b2-800e-080027b246c3', '35b6e1ca-1dd2-11b2-800f-080027b246c3', '35b6e1ca-1dd2-11b2-8010-080027b246c3', '35b6e1ca-1dd2-11b2-8011-080027b246c3', '35b6e1ca-1dd2-11b2-8012-080027b246c3', '35b6e1ca-1dd2-11b2-8013-080027b246c3', '35b6e1ca-1dd2-11b2-8014-080027b246c3', '35b6e1ca-1dd2-11b2-8015-080027b246c3', '35b6e1ca-1dd2-11b2-8016-080027b246c3', 'b9d2b56d-05b0-4d63-a167-174455f03fb1', 'fe67cdbf-84a8-4565-875b-38f0c3582ba6', '99ccf6b2-b158-4a1c-804d-2704067db784', 'c28d6a37-b64c-461d-ac8e-adcb83162553', 'c697d1c2-e3f8-45c2-86ac-cec9c4d7002a', '34ab1203-ba56-4e8d-86f1-05e9e7985b70']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[1]')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Stroke')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_6')):
        assert False, 'select stroke 1 fail'
    with step('[Verify] snapshot: 06_01_01_stroke1.png'):
        actions.capture_for_gt('06_01_01_stroke1.png')
    if actions.compare_with_gt('06_01_01_stroke1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'stroke-1 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-2')):
        assert False, 'color 1-2 fail'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')):
        assert False, 'Stroke 1 thickness slider fail'
    with step('[Verify] snapshot: 06_01_01_stroke1_after.png'):
        actions.capture_for_gt('06_01_01_stroke1_after.png')
    if actions.compare_with_gt('06_01_01_stroke1_after.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Stroke 1 thickness slider fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_2')):
        assert False, 'select stroke 2 fail'
    with step('[Verify] snapshot: 06_01_01_stroke2.png'):
        actions.capture_for_gt('06_01_01_stroke2.png')
    if actions.compare_with_gt('06_01_01_stroke2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'stroke-2 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-5')
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')):
        assert False, 'Stroke 2 thickness slider fail'
    with step('[Verify] snapshot: 06_01_01_stroke2_after.png'):
        actions.capture_for_gt('06_01_01_stroke2_after.png')
    if actions.compare_with_gt('06_01_01_stroke2_after.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Stroke 2 thickness slider fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_3')):
        assert False, 'select stroke 3 fail'
    with step('[Verify] snapshot: 06_01_01_stroke3.png'):
        actions.capture_for_gt('06_01_01_stroke3.png')
    if actions.compare_with_gt('06_01_01_stroke3.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'stroke-3 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-5')):
        assert False, 'color 3-1 fail'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')):
        assert False, 'Stroke 3 thickness slider fail'
    with step('[Verify] snapshot: 06_01_01_stroke3_after.png'):
        actions.capture_for_gt('06_01_01_stroke3_after.png')
    if actions.compare_with_gt('06_01_01_stroke3_after.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Stroke 3 thickness slider fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_1')):
        assert False, 'select stroke 4 fail'
    with step('[Verify] snapshot: 06_01_01_stroke4.png'):
        actions.capture_for_gt('06_01_01_stroke4.png')
    if actions.compare_with_gt('06_01_01_stroke4.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'stroke-4 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-5')):
        assert False, 'color 4-5 fail'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')):
        assert False, 'Stroke 4 thickness slider fail'
    with step('[Verify] snapshot: 06_01_01_stroke4_after.png'):
        actions.capture_for_gt('06_01_01_stroke4_after.png')
    if actions.compare_with_gt('06_01_01_stroke4_after.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Stroke 4 thickness slider fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_4')):
        assert False, 'select stroke 5 fail'
    with step('[Verify] snapshot: 06_01_01_stroke5.png'):
        actions.capture_for_gt('06_01_01_stroke5.png')
    if actions.compare_with_gt('06_01_01_stroke5.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'stroke-5 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-5')):
        assert False, 'color 5-5 fail'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')):
        assert False, 'Stroke 5 thickness slider fail'
    with step('[Verify] snapshot: 06_01_01_stroke5_after.png'):
        actions.capture_for_gt('06_01_01_stroke5_after.png')
    if actions.compare_with_gt('06_01_01_stroke5_after.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Stroke 5 thickness slider fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_7')):
        assert False, 'select stroke 6 fail'
    with step('[Verify] snapshot: 06_01_01_stroke6.png'):
        actions.capture_for_gt('06_01_01_stroke6.png')
    if actions.compare_with_gt('06_01_01_stroke6.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'stroke-6 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-6')):
        assert False, 'color 6-6 fail'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')):
        assert False, 'Stroke 6 thickness slider fail'
    with step('[Verify] snapshot: 06_01_01_stroke6_after.png'):
        actions.capture_for_gt('06_01_01_stroke6_after.png')
    if actions.compare_with_gt('06_01_01_stroke6_after.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Stroke 6 thickness slider fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_5')):
        assert False, 'select stroke 7 fail'
    with step('[Verify] snapshot: 06_01_01_stroke7.png'):
        actions.capture_for_gt('06_01_01_stroke7.png')
    if actions.compare_with_gt('06_01_01_stroke7.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'stroke-7 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-7')):
        assert False, 'color 7-7 fail'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')):
        assert False, 'Stroke 7 thickness slider fail'
    with step('[Verify] snapshot: 06_01_01_stroke7_after.png'):
        actions.capture_for_gt('06_01_01_stroke7_after.png')
    if actions.compare_with_gt('06_01_01_stroke7_after.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Stroke 7 thickness slider fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btn edit n')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    from_pos = (194, 406)
    destination = (227, 607)
    with step('[Verify] snapshot: 06_01_01_stroke_before_brush-.png'):
        actions.capture_for_gt('06_01_01_stroke_before_brush-.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(194, 406, 227, 607)
    with step('[Verify] snapshot: 06_01_01_stroke_after_brush-.png'):
        actions.capture_for_gt('06_01_01_stroke_after_brush-.png')
    if (not actions.compare_with_gt('06_01_01_stroke_after_brush-.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'eraser - fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    from_pos = (187, 371)
    destination = (230, 629)
    with step('[Verify] snapshot: 06_01_01_stroke_before_brush+.png'):
        actions.capture_for_gt('06_01_01_stroke_before_brush+.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(187, 371, 230, 629)
    with step('[Verify] snapshot: 06_01_01_stroke_after_brush+.png'):
        actions.capture_for_gt('06_01_01_stroke_after_brush+.png')
    if (not actions.compare_with_gt('06_01_01_stroke_after_brush+.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'eraser + fail'
    with step("[Verify] test_00118 completion"):
        assert True
