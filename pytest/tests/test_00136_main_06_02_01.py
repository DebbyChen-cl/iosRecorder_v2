import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00136_main_06_02_01')
def test_00136_main_06_02_01(actions: DriverActions):
    """Live - animation"""
    mode = 1
    uuid = ['b493917b-da1f-44be-a8ff-2853b60282d3', 'be2d3287-17c5-47ec-b39f-e0fbf30827b1', '5160eb5d-b3d2-4aa9-aade-fee08e2927c1', '002ffb76-428a-4c0a-a522-cb90ab2fc31a', '924091b0-110f-4c63-9f73-cbadb761769d', 'de744736-7013-4eb1-a3e5-e8e6b5e02f36', '767ab7f3-f868-44c1-ab6a-66c117bde291', '304c77fc-46cc-48a8-81e2-1c78ea0f9401', '75a22c3b-0345-4670-91fd-6c4abd07992d', 'e671f4c3-681c-4ec2-a45b-a6d490e8c69f', 'ec0b5d46-c253-4660-baba-0461beec980a', '49189455-0a47-4527-8939-252ce5e006d5', '4401a83c-89d0-4826-8100-0fc2999b4211', '6d03e81e-6448-4db9-b656-7a7a176fd382', 'd031eb01-5b12-4380-9efb-63c4624df2ae', 'a035936e-8e8e-462a-9f1c-b38f831bdb8d', 'db55dfc2-fb64-42a3-a585-c7eaa37f2554', '19e55a01-2d97-457e-8dd3-2714c01b109b', '08ce9d16-dd4f-41c5-9e01-76c415fc6eec', '283cf26c-cd05-49f8-8295-78b837a96939', 'f825e506-9427-4490-aec5-67f2046fbaba', '42571920-3a68-426c-a6c7-776c8cb57f83', '40d0a87a-3dd4-48df-a191-34edc7fd5b32', '69569c72-e336-4a3f-b813-003da81ddba1', '27c52ef4-f155-4e9f-ad49-287d7d24cd6f', 'a657d102-0964-4539-8251-f10fd49de7dc', '010ee5f3-610a-4651-b406-e62627868e16', '6058dd76-cd28-4e6c-a371-ad7f6cc397f2', '33f8f855-ed6e-4f5a-8f5f-146884ad36af', 'd023f78c-6437-43bc-a1e3-67c401d71769', '9684d45b-c442-4efd-aaff-1a0490f45eae', '8d6808e1-c721-416b-8bfc-116a76a82e2f', 'f06e9980-f77c-4203-a225-e698499da782', '17bd3651-48be-4554-a3f1-64c23a113b9b', '9ae10ce7-154e-4686-8d11-507eb05e69a0', 'd35c346f-38b2-4d00-b575-9a67f1f7c043', '7fd492f5-ca0b-44a6-982e-a3f25e41305b']
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
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btn_live_wraparound_n'):
        pass
    else:
        assert False, 'leave animation page failed'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')):
        assert False, 'tap animation_motion failed'
    from_pos = (60, 100)
    destination = (60, 500)
    with step('[Verify] snapshot: 06_02_01_before_add_motion1.png'):
        actions.capture_for_gt('06_02_01_before_add_motion1.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Verify] snapshot: 06_02_01_after_add_motion1.png'):
        actions.capture_for_gt('06_02_01_after_add_motion1.png')
    if (not actions.compare_with_gt('06_02_01_before_add_motion1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare add motion 1 failed'
    from_pos = (370, 600)
    destination = (70, 100)
    mode = 1
    with step('[Verify] snapshot: 06_02_01_before_add_motion2.png'):
        actions.capture_for_gt('06_02_01_before_add_motion2.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(370, 600, 70, 100)
    with step('[Verify] snapshot: 06_02_01_after_add_motion2.png'):
        actions.capture_for_gt('06_02_01_after_add_motion2.png')
    if (not actions.compare_with_gt('06_02_01_before_add_motion2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare add motion 2 failed'
    if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'label == "photo animation btn pause n"'):
        pass
    else:
        assert False, 'verify playback failed'
    with step('[Action] tap_wraparound_pause'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Verify] snapshot: 06_02_01_before_undo_add_motion.png'):
        actions.capture_for_gt('06_02_01_before_undo_add_motion.png')
    with step('[Action] tap_live_undo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    actions.capture_for_gt('06_02_01_after_undo_add_motion.png')
    if not actions.compare_with_gt('06_02_01_after_undo_add_motion.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo add motion failed'
    with step('[Action] tap_live_redo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    actions.capture_for_gt('06_02_01_after_redo_add_motion.png')
    if not actions.compare_with_gt('06_02_01_after_redo_add_motion.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo add motion failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Anchor')):
        assert False, 'tap animation_anchor failed'
    with step('[Verify] snapshot: 06_02_01_before_add_anchor.png'):
        actions.capture_for_gt('06_02_01_before_add_anchor.png')
    with step('[Action] Tap'):
        actions.tap_by_coordinates(223, 223)
    with step('[Action] Tap'):
        actions.tap_by_coordinates(271, 305)
    with step('[Action] Tap'):
        actions.tap_by_coordinates(163, 256)
    with step('[Action] Tap'):
        actions.tap_by_coordinates(142, 284)
    with step('[Action] Tap'):
        actions.tap_by_coordinates(126, 314)
    with step('[Action] Tap'):
        actions.tap_by_coordinates(107, 444)
    with step('[Action] Tap'):
        actions.tap_by_coordinates(179, 499)
    with step('[Action] Tap'):
        actions.tap_by_coordinates(231, 710)
    with step('[Action] Tap'):
        actions.tap_by_coordinates(329, 661)
    with step('[Action] Tap'):
        actions.tap_by_coordinates(303, 586)
    actions.capture_for_gt('06_02_01_after_add_anchor.png')
    if not actions.compare_with_gt('06_02_01_after_add_anchor.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'add anchor failed'
    if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'label == "photo animation btn pause n"'):
        pass
    else:
        assert False, 'verify playback after anchor failed'
    with step('[Action] tap_wraparound_pause'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Verify] snapshot: 06_02_01_before_undo_add_anchor.png'):
        actions.capture_for_gt('06_02_01_before_undo_add_anchor.png')
    with step('[Action] tap_live_undo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    actions.capture_for_gt('06_02_01_after_undo_add_anchor.png')
    if not actions.compare_with_gt('06_02_01_after_undo_add_anchor.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo add anchor failed'
    with step('[Action] tap_live_redo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    actions.capture_for_gt('06_02_01_after_redo_add_anchor.png')
    if not actions.compare_with_gt('06_02_01_after_redo_add_anchor.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo add anchor failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Freeze')):
        assert False, 'tap animation_freeze failed'
    from_pos = (248, 330)
    destination = (257, 482)
    mode = 1
    with step('[Verify] snapshot: 06_02_01_before_add_freeze.png'):
        actions.capture_for_gt('06_02_01_before_add_freeze.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(248, 330, 257, 482)
    with step('[Verify] snapshot: 06_02_01_after_add_freeze.png'):
        actions.capture_for_gt('06_02_01_after_add_freeze.png')
    if (not actions.compare_with_gt('06_02_01_before_add_freeze.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'add freeze failed'
    with step('[Action] tap_wraparound_play2'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Action] tap_wraparound_pause'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Verify] snapshot: 06_02_01_before_undo_freeze.png'):
        actions.capture_for_gt('06_02_01_before_undo_freeze.png')
    with step('[Action] tap_live_undo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    actions.capture_for_gt('06_02_01_after_undo_freeze.png')
    if not actions.compare_with_gt('06_02_01_after_undo_freeze.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo add freeze failed'
    with step('[Action] tap_live_redo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    actions.capture_for_gt('06_02_01_after_redo_freeze.png')
    if not actions.compare_with_gt('06_02_01_after_redo_freeze.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo add freeze failed'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')):
        assert False, 'adjust brush+ size failed'
    from_pos = (248, 230)
    destination = (257, 382)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(248, 230, 257, 382)
    with step('[Verify] snapshot: 06_02_01_brush+size_max.png'):
        actions.capture_for_gt('06_02_01_brush+size_max.png')
    if (not actions.compare_with_gt('06_02_01_brush+size_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare brush+ size failed'
    with step('[Action] adjust_harmonization_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnErase')
    from_pos = (248, 230)
    destination = (257, 382)
    mode = 1
    with step('[Verify] snapshot: 06_02_01_brush-_before.png'):
        actions.capture_for_gt('06_02_01_brush-_before.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(248, 230, 257, 382)
    with step('[Verify] snapshot: 06_02_01_brush-_min.png'):
        actions.capture_for_gt('06_02_01_brush-_min.png')
    if (not actions.compare_with_gt('06_02_01_brush-_before.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'eraser brush- failed'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')):
        assert False, 'adjust brush- size failed'
    from_pos = (248, 230)
    destination = (262, 300)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(248, 230, 262, 300)
    with step('[Verify] snapshot: 06_02_01_brush-_max.png'):
        actions.capture_for_gt('06_02_01_brush-_max.png')
    if (not actions.compare_with_gt('06_02_01_brush-_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'eraser size failed'
    with step('[Verify] snapshot: 06_02_01_before_undo_brush-.png'):
        actions.capture_for_gt('06_02_01_before_undo_brush-.png')
    with step('[Action] tap_live_undo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    actions.capture_for_gt('06_02_01_after_undo_brush-.png')
    if not actions.compare_with_gt('06_02_01_after_undo_brush-.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo brush- failed'
    with step('[Action] tap_live_redo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    actions.capture_for_gt('06_02_01_after_redo_brush-.png')
    if not actions.compare_with_gt('06_02_01_after_redo_brush-.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo brush- failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Speed')):
        assert False, 'tap animation_speed failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "photoanimation"`]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '75'):
        pass
    else:
        assert False, 'get default speed failed'
    with step('[Action] adjust_bokeh_speed_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "photoanimation"`]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('0', '1', '2')):
        pass
    else:
        assert False, 'adjust speed to min failed'
    with step('[Action] adjust_bokeh_speed_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "photoanimation"`]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('98', '99', '100')):
        pass
    else:
        assert False, 'adjust speed to max failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Delete')):
        assert False, 'tap animation_delete failed'
    with step('[Verify] snapshot: 06_02_01_before_del_motion.png'):
        actions.capture_for_gt('06_02_01_before_del_motion.png')
    with step('[Action] Tap'):
        actions.tap_by_coordinates(60, 300)
    with step('[Verify] snapshot: 06_02_01_after_del_motion.png'):
        actions.capture_for_gt('06_02_01_after_del_motion.png')
    if (not actions.compare_with_gt('06_02_01_after_del_motion.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'delete motion failed'
    with step('[Verify] snapshot: 06_02_01_before_undo_del_motion.png'):
        actions.capture_for_gt('06_02_01_before_undo_del_motion.png')
    with step('[Action] tap_live_undo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    actions.capture_for_gt('06_02_01_after_undo_del_motion.png')
    if not actions.compare_with_gt('06_02_01_after_undo_del_motion.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo delete motion failed'
    with step('[Action] tap_live_redo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    actions.capture_for_gt('06_02_01_after_redo_del_motion.png')
    if not actions.compare_with_gt('06_02_01_after_redo_del_motion.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo delete motion failed'
    with step('[Verify] snapshot: 06_02_01_before_del_anchor.png'):
        actions.capture_for_gt('06_02_01_before_del_anchor.png')
    with step('[Action] Tap'):
        actions.tap_by_coordinates(107, 444)
    with step('[Verify] snapshot: 06_02_01_after_del_anchor.png'):
        actions.capture_for_gt('06_02_01_after_del_anchor.png')
    if (not actions.compare_with_gt('06_02_01_after_del_anchor.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'delete anchor failed'
    with step('[Verify] snapshot: 06_02_01_before_undo_del_anchor.png'):
        actions.capture_for_gt('06_02_01_before_undo_del_anchor.png')
    with step('[Action] tap_live_undo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    actions.capture_for_gt('06_02_01_after_undo_del_anchor.png')
    if not actions.compare_with_gt('06_02_01_after_undo_del_anchor.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo delete anchor failed'
    with step('[Action] tap_live_redo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    actions.capture_for_gt('06_02_01_after_redo_del_anchor.png')
    if not actions.compare_with_gt('06_02_01_after_redo_del_anchor.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo delete anchor failed'
    if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'label == "photo animation btn pause n"'):
        pass
    else:
        assert False, 'verify final playback failed'
    with step('[Action] tap_wraparound_pause'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step("[Verify] test_00136 completion"):
        assert True
