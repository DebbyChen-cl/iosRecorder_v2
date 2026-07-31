import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00080_main_05_07_14')
def test_00080_main_05_07_14(actions: DriverActions):
    """skin tone"""
    mode = 1
    uuid = ['4f0bf7d1-29a0-4d78-94b9-f3afd9f8876f', 'd4edafd3-2bdd-4eae-a06b-56bd57092138', 'be9d2c43-c137-4be7-9cc1-71d68e927e3d', 'dd4b7ad9-7672-4392-b5f1-fc5c4d44faef', '6bbc42f2-4a53-48a6-bf40-6e902aab1296', '14588c4a-152c-4f1b-bbd5-115f07fea4c6', '394bdd00-346b-4aa6-a606-964baa924613', '2a87f4f3-3b09-4270-8a5b-6f2db77a6d4c', '2b0f3573-0701-45b4-89ff-dfffa23ff902', 'c25bfd52-8236-44c1-9b14-c8179ba13dee', '5c325bc3-8c95-419f-bbb0-21e015e90421', '17684438-7829-4ced-b47a-28cd886d348c', '8c4a55ed-3cf9-404e-bac6-bb74b57b92ff', 'e64430d6-f119-4828-adc4-6cfe1b61b36a', 'a808feed-5b05-41a0-a9e6-ac7d04a8376c']
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
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step('[Verify] snapshot: 05_07_14_before_skintone.png'):
        actions.capture_for_gt('05_07_14_before_skintone.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Skin Tone')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    with step('[Verify] snapshot: 05_07_14_skintone_default.png'):
        actions.capture_for_gt('05_07_14_skintone_default.png')
    if actions.compare_with_gt('05_07_14_skintone_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Snapshot skin tone default fail'
    with step('[Action] tap_skin_tone_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cellColor-1')
    with step('[Verify] snapshot: 05_07_14_skintone_1.png'):
        actions.capture_for_gt('05_07_14_skintone_1.png')
    if actions.compare_with_gt('05_07_14_skintone_1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Snapshot skin tone preset 1 fail'
    with step('[Action] tap_skin_tone_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cellColor-2')
    with step('[Verify] snapshot: 05_07_14_skintone_2.png'):
        actions.capture_for_gt('05_07_14_skintone_2.png')
    if actions.compare_with_gt('05_07_14_skintone_2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Snapshot skin tone preset 2 fail'
    with step('[Action] tap_skin_tone_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cellColor-3')
    with step('[Verify] snapshot: 05_07_14_skintone_3.png'):
        actions.capture_for_gt('05_07_14_skintone_3.png')
    if actions.compare_with_gt('05_07_14_skintone_3.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Snapshot skin tone preset 3 fail'
    with step('[Action] tap_skin_tone_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cellColor-4')
    with step('[Verify] snapshot: 05_07_14_skintone_4.png'):
        actions.capture_for_gt('05_07_14_skintone_4.png')
    if actions.compare_with_gt('05_07_14_skintone_4.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Snapshot skin tone preset 4 fail'
    with step('[Action] adjust_slider_1'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: base05_07_14_color_min.png'):
        actions.capture_for_gt('base05_07_14_color_min.png')
    if actions.compare_with_gt('05_07_14_color_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Snapshot color min fail'
    with step('[Action] adjust_slider_1'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    with step('[Verify] snapshot: 05_07_14_color_max.png'):
        actions.capture_for_gt('05_07_14_color_max.png')
    if actions.compare_with_gt('05_07_14_color_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Snapshot color max fail'
    with step('[Action] adjust_slider_2'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Verify] snapshot: 05_07_14_bright_min.png'):
        actions.capture_for_gt('05_07_14_bright_min.png')
    if actions.compare_with_gt('05_07_14_bright_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Snapshot bright min fail'
    with step('[Verify] snapshot: 05_07_14_bright_min2.png'):
        actions.capture_for_gt('05_07_14_bright_min2.png')
    with step('[Action] adjust_slider_2'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Verify] snapshot: 05_07_14_bright_max.png'):
        actions.capture_for_gt('05_07_14_bright_max.png')
    with step('[Verify] snapshot: 05_07_14_bright_max.png'):
        actions.capture_for_gt('05_07_14_bright_max.png')
    if actions.compare_with_gt('05_07_14_bright_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Snapshot bright max fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_14_undo.png'):
        actions.capture_for_gt('05_07_14_undo.png')
    if actions.compare_with_gt('05_07_14_bright_min2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_14_redo.png'):
        actions.capture_for_gt('05_07_14_redo.png')
    if actions.compare_with_gt('05_07_14_bright_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap done button fail'
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, 'Verify IAP fail'
    with step('[Action] close_IAP'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_07_14_skintone_x.png'):
        actions.capture_for_gt('05_07_14_skintone_x.png')
    if actions.compare_with_gt('05_07_14_skintone_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[x] fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Custom')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Square')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_portrait_tab'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Skin Tone')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'No bodies were detected.'):
        pass
    else:
        assert False, 'No bodies detected message fail'
    with step("[Verify] test_00080 completion"):
        assert True
