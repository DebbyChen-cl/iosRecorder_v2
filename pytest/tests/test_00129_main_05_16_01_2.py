import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00129_main_05_16_01_2')
def test_00129_main_05_16_01_2(actions: DriverActions):
    """Live - wraparounds"""
    mode = 1
    uuid = ['2f270619-1dd2-11b2-8000-080027b246c3', '2f270619-1dd2-11b2-8001-080027b246c3', '2f270619-1dd2-11b2-8002-080027b246c3', '2f270619-1dd2-11b2-8003-080027b246c3', '2f270619-1dd2-11b2-8004-080027b246c3', '2f270619-1dd2-11b2-8005-080027b246c3', '2f270619-1dd2-11b2-8006-080027b246c3', '2f270619-1dd2-11b2-8007-080027b246c3', '2f270619-1dd2-11b2-8008-080027b246c3', '2f270619-1dd2-11b2-8009-080027b246c3', '2f270619-1dd2-11b2-800a-080027b246c3', '2f270619-1dd2-11b2-800c-080027b246c3']
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
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_wraparound_n')
    with step('[Verify] snapshot: 05_16_01_no_wraparound.png'):
        actions.capture_for_gt('05_16_01_no_wraparound.png')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_wraparound_vday01_220126')):
        assert False, 'tap wraparound template1 failed'
    with step('[Verify] snapshot: 05_16_01_after_wraparound.png'):
        actions.capture_for_gt('05_16_01_after_wraparound.png')
    if (not actions.compare_with_gt('05_16_01_after_wraparound.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare wraparound template failed'
    if actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1') and actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "wraparound"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeStaticText') in '2x':
        pass
    else:
        assert False, 'adjust wraparound speed to 2x failed'
    if actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0.5') and actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "wraparound"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeStaticText') in '1x':
        pass
    else:
        assert False, 'adjust wraparound speed to 1x failed'
    if actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0') and actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "wraparound"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeStaticText') in '0.5x':
        pass
    else:
        assert False, 'adjust wraparound speed to 0.5x failed'
    if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'label == "photo animation btn pause n"'):
        pass
    else:
        assert False, 'verify wraparound playback failed'
    with step('[Action] tap_wraparound_pause'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Verify] snapshot: 05_16_01_before_temp2.png'):
        actions.capture_for_gt('05_16_01_before_temp2.png')
    with step('[Action] tap_phd_element'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_wraparound_vday02_220126')
    with step('[Action] tap_wraparound_pause'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Verify] snapshot: 05_16_01_after_temp2.png'):
        actions.capture_for_gt('05_16_01_after_temp2.png')
    if (not actions.compare_with_gt('05_16_01_after_temp2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare change wraparound template failed'
    with step('[Action] tap_phd_element'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_wraparound_vday01_220126')
    from_pos = (300, 500)
    destination = (100, 250)
    mode = 1
    with step('[Verify] snapshot: 05_16_01_before_move_w.png'):
        actions.capture_for_gt('05_16_01_before_move_w.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(300, 500, 100, 250)
    with step('[Action] tap_wraparound_pause'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Verify] snapshot: 05_16_01_after_move_w.png'):
        actions.capture_for_gt('05_16_01_after_move_w.png')
    if (not actions.compare_with_gt('05_16_01_after_move_w.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare move wraparound failed'
    from_pos = (338, 475)
    destination = (300, 350)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(338, 475, 300, 350)
    with step('[Verify] snapshot: 05_16_01_before_rotate_w.png'):
        actions.capture_for_gt('05_16_01_before_rotate_w.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(338, 475, 300, 350)
    with step('[Action] tap_wraparound_pause'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Verify] snapshot: 05_16_01_after_rotate_w.png'):
        actions.capture_for_gt('05_16_01_after_rotate_w.png')
    if (not actions.compare_with_gt('05_16_01_after_rotate_w.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare resize/rotate wraparound failed'
    from_pos = (100, 250)
    destination = (300, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(100, 250, 300, 500)
    with step('[Verify] snapshot: 05_16_01_before_flip_w.png'):
        actions.capture_for_gt('05_16_01_before_flip_w.png')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFlip')
    with step('[Action] tap_wraparound_pause'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Verify] snapshot: 05_16_01_after_flip_w.png'):
        actions.capture_for_gt('05_16_01_after_flip_w.png')
    if (not actions.compare_with_gt('05_16_01_after_flip_w.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare flip wraparound failed'
    with step('[Verify] snapshot: 05_16_01_before_del_w.png'):
        actions.capture_for_gt('05_16_01_before_del_w.png')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step('[Verify] snapshot: 05_16_01_after_del_w.png'):
        actions.capture_for_gt('05_16_01_after_del_w.png')
    if (not actions.compare_with_gt('05_16_01_after_del_w.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare delete wraparound failed'
    with step("[Verify] test_00129 completion"):
        assert True
