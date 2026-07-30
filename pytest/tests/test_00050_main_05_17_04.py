import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00050_main_05_17_04')
def test_00050_main_05_17_04(actions: DriverActions):
    """Lighthits"""
    mode = 1
    uuid = ['1a4288ad-1dd2-11b2-8000-080027b246c3', '1a4288ad-1dd2-11b2-8001-080027b246c3', '1a4288ad-1dd2-11b2-8002-080027b246c3', '1a4288ad-1dd2-11b2-8003-080027b246c3', '1a4288ad-1dd2-11b2-8004-080027b246c3', '1a4288ad-1dd2-11b2-8005-080027b246c3', '1a4288ad-1dd2-11b2-8006-080027b246c3', '1a4288ad-1dd2-11b2-8007-080027b246c3', '1a4288ad-1dd2-11b2-8008-080027b246c3', '1a4288ad-1dd2-11b2-8009-080027b246c3', '1a4288ad-1dd2-11b2-800a-080027b246c3', '1a4288ad-1dd2-11b2-800b-080027b246c3', '1a4288ad-1dd2-11b2-800c-080027b246c3', '1a4288ad-1dd2-11b2-800d-080027b246c3', '1a4288ad-1dd2-11b2-800e-080027b246c3', '1a4288ad-1dd2-11b2-800f-080027b246c3', '1a4288ad-1dd2-11b2-8010-080027b246c3', 'ed383c1a-6d0b-4e31-8f33-83a3db49bcd4', '0771f421-912b-41db-b0a2-b52c1596f14b', '0d5dd710-86cf-479e-9d02-3b30ee6baebb', '5cd2482f-6f7d-4298-813b-bc0396fb8199', 'afad6123-1407-48f5-a609-4dc7fb9270ca', '823ec2f9-b22a-472f-b444-adecfc63430b', 'd216fb2f-7765-4fd1-9b0c-f5f3f913e6ba']
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
    with step('[Verify] snapshot: 5_17_04_before_lighthit.png'):
        actions.capture_for_gt('5_17_04_before_lighthit.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_effects1_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light Hits')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_hits"`]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]')
    with step('[Action] adjust_lighthits_softness_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 5_17_04_opacity_min.png'):
        actions.capture_for_gt('5_17_04_opacity_min.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 5_17_04_opacity_min.png'):
        assert actions.compare_with_gt('5_17_04_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Verify] snapshot: 5_17_04_min.png'):
        actions.capture_for_gt('5_17_04_min.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_lighthits_softness_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 5_17_04_opacity_max.png'):
        actions.capture_for_gt('5_17_04_opacity_max.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 5_17_04_opacity_max.png'):
        assert actions.compare_with_gt('5_17_04_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Verify] snapshot: 5_17_04_max.png'):
        actions.capture_for_gt('5_17_04_max.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 5_17_04_after_undo.png'):
        actions.capture_for_gt('5_17_04_after_undo.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('5_17_04_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 5_17_04_redo.png'):
        actions.capture_for_gt('5_17_04_redo.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('5_17_04_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo fail'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_1lv_adjustment_s')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Horizontal')
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Verify] snapshot: 5_17_04_flip_H.png'):
        actions.capture_for_gt('5_17_04_flip_H.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('5_17_04_flip_H.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'flip horizontal fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Horizontal')):
        assert False, 'tap flip horizontal fail'
    with step('[Verify] snapshot: 5_17_04_flip_H_og.png'):
        actions.capture_for_gt('5_17_04_flip_H_og.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('5_17_04_flip_H_og.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'flip horizontal again fail'
    with step('[Action] swipe_lighthits_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Color'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Contrast'))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Vertical')):
        assert False, 'tap flip vertical fail'
    with step('[Verify] snapshot: 5_17_04_flip_V.png'):
        actions.capture_for_gt('5_17_04_flip_V.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('5_17_04_flip_V.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'flip vertical fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Vertical')):
        assert False, 'tap flip vertical fail'
    with step('[Verify] snapshot: 5_17_04_flip_V_og.png'):
        actions.capture_for_gt('5_17_04_flip_V_og.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('5_17_04_flip_V_og.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'flip vertical again fail'
    with step('[Action] swipe_lighthits_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Contrast'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Color'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Softness')
    with step('[Action] adjust_lighthits_softness_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_lighthits_softness_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_hits"`]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeButton[2]') in ('96', '97', '98', '99', '100')):
        pass
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brightness')
    with step('[Action] adjust_lighthits_brightness_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_lighthits_brightness_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_hits"`]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeButton[2]') in ('97', '98', '99', '100')):
        pass
    else:
        assert False, 'Adjust brightness fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Contrast')
    with step('[Action] adjust_lighthits_contrast_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Action] adjust_lighthits_contrast_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_hits"`]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeButton[2]') in ('-96', '-97', '-98', '-99', '-100')):
        pass
    else:
        assert False, 'Adjust contrast fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')):
        assert False, 'tap color button fail'
    with step('[Action] adjust_lighthits_color_hue_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_lighthits_color_hue_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '180') in ('171', '172', '173', '174', '175', '176', '177', '178', '179', '180')):
        pass
    else:
        assert False, 'Adjust hue fail'
    with step('[Action] adjust_lighthits_color_saturation_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Action] adjust_lighthits_color_saturation_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '100') in ('92', '93', '94', '95', '96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'Adjust saturation fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    if (not actions.compare_with_gt('5_17_04_lighthit_x.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'tap [x] button fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light Hits')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_hits"`]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]')
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 5_17_04_lighthit_v.png'):
        actions.capture_for_gt('5_17_04_lighthit_v.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00050 completion"):
        assert True
