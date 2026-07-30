import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00128_main_05_16_01_1')
def test_00128_main_05_16_01_1(actions: DriverActions):
    """Live - elements"""
    mode = 1
    uuid = ['869c0b5e-2d63-447c-9643-e6377f762403', '99fa5716-fa7f-4c23-94c7-d38848d43759', 'af9cbe87-bf2f-4e14-91eb-eb09deca3eda', '8e26c371-cc8a-4335-85c0-5d70ff37b22c', 'bfb56eb5-fa6a-4741-bbd0-f0a343c89360', 'b3aef766-9d32-40f6-ac89-6d9c27164640', '1ae65970-2d2d-4bad-ada9-30b65b1cd930', 'ab4e5833-51f0-41cf-b9f6-1b5f94e0e4e2', 'bb81fb78-d636-411a-a108-8ffcfaf5efb3', 'a43d71b8-80c2-4b1d-ad41-fc689e3ebbef', '826c27a8-53b4-44ca-ae0d-92a992b61a87', '5f981512-9000-4dc4-b8b9-458718f8c337', 'c4e24248-c2b1-4d68-a2d2-f4447b9aa76c', '8ee05833-007d-4b29-89cf-41bf2e5ea629', '9bdedf32-d821-4a1c-82a5-2e85462e9c0f', '17ef1c27-1184-4169-bea8-04cd59ce6a4d']
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
    with step('[Action] close_live_warning_dialog'):
        actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Complete your photo edits before applying animated effects.')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ok')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n')
    with step('[Verify] snapshot: 05_16_01_empty.png'):
        actions.capture_for_gt('05_16_01_empty.png')
    with step('[Action] select_element_template_2'):
        assert actions.tap_by_coordinates(160, 666), 'Fail to select element template 2'
    with step('[Verify] snapshot: 05_16_01_add_temp2.png'):
        actions.capture_for_gt('05_16_01_add_temp2.png')
    if (not actions.compare_with_gt('05_16_01_add_temp2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare add template failed'
    if actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1') and actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "animated_elements"`]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeStaticText') in '2x':
        pass
    else:
        assert False, 'adjust speed to 2x failed'
    if actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0.5') and actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "animated_elements"`]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeStaticText') in '1x':
        pass
    else:
        assert False, 'adjust speed to 1x failed'
    if actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0') and actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "animated_elements"`]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeStaticText') in '0.5x':
        pass
    else:
        assert False, 'adjust speed to 0.5x failed'
    if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'label == "photo animation btn pause n"'):
        pass
    else:
        assert False, 'verify playback failed'
    with step('[Action] tap_wraparound_pause'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    from_pos = (210, 250)
    destination = (170, 110)
    mode = 1
    with step('[Verify] snapshot: 05_16_01_before_move.png'):
        actions.capture_for_gt('05_16_01_before_move.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(210, 250, 170, 110)
    with step('[Action] tap_wraparound_pause'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Verify] snapshot: 05_16_01_after_move.png'):
        actions.capture_for_gt('05_16_01_after_move.png')
    if (not actions.compare_with_gt('05_16_01_after_move.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare move element failed'
    with step('[Action] tap_undo_btn_n2'):
        actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "btnUndo"`][2]')
    from_pos = (206, 395)
    destination = (107, 347)
    with step('[Verify] snapshot: 05_16_01_before_rotate.png'):
        actions.capture_for_gt('05_16_01_before_rotate.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 395, 107, 347)
    with step('[Verify] snapshot: 05_16_01_after_rotate.png'):
        actions.capture_for_gt('05_16_01_after_rotate.png')
    if (not actions.compare_with_gt('05_16_01_after_rotate.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare resize/rotate element failed'
    with step('[Verify] snapshot: 05_16_01_before_flip.png'):
        actions.capture_for_gt('05_16_01_before_flip.png')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFlip')
    with step('[Action] tap_wraparound_pause'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Verify] snapshot: 05_16_01_after_flip.png'):
        actions.capture_for_gt('05_16_01_after_flip.png')
    if (not actions.compare_with_gt('05_16_01_after_flip.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare flip elements failed'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step('[Verify] snapshot: 05_16_01_after_del.png'):
        actions.capture_for_gt('05_16_01_after_del.png')
    if actions.compare_with_gt('05_16_01_after_del.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare delete elements failed'
    with step('[Action] select_element_template_1'):
        assert actions.tap_by_coordinates(160, 750), 'Fail to select element template 1'
    with step('[Action] tap_wraparound_pause'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Verify] snapshot: 05_16_01_1elements.png'):
        actions.capture_for_gt('05_16_01_1elements.png')
    with step('[Action] select_element_template_2'):
        assert actions.tap_by_coordinates(160, 666), 'Fail to select element template 2'
    with step('[Action] tap_wraparound_pause'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Verify] snapshot: 05_16_01_2elements.png'):
        actions.capture_for_gt('05_16_01_2elements.png')
    if (not actions.compare_with_gt('05_16_01_2elements.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare multi elements failed'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_wraparound_n')
    with step("[Verify] test_00128 completion"):
        assert True
