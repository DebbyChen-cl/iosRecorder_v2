import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00065_main_05_07_03_2')
def test_00065_main_05_07_03_2(actions: DriverActions):
    """face smoother, no face"""
    mode = 1
    uuid = ['74cd8d94-8abc-4b50-8155-89366b5bbedf', '50a14198-efaa-4e61-b6ef-9c7819b8e550', '125e989d-67c3-4849-8ba3-a82f16019503', '7255aab9-2838-4f26-9145-1bd330447cd3', 'a237bedc-f9fc-45fe-8751-e74248f44b5c', '8d290495-0377-47a2-96b0-93fd206a942d']
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    from_pos = (400, 780)
    destination = (50, 780)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 780, 50, 780)
    with step('[Verify] snapshot: 05_07_03_before_face_smoother2.png'):
        actions.capture_for_gt('05_07_03_before_face_smoother2.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Smooth')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    if actions.is_element_present(AppiumBy.NAME, 'No faces were detected.'):
        pass
    else:
        assert False, 'No face dialog fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Face')
    with step('[Action] close_add_face_tutorial'):
        assert actions.is_element_present(AppiumBy.NAME, 'Drag to move the crosses over the eyes and lips.')
        assert actions.tap_by_coordinates(250, 250)
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Drag to move the crosses over the eyes and lips.')
    with step('[Action] tap_to_add_face'):
        assert actions.tap_by_coordinates(205, 401)
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] select_a_face'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'Tap x fail'
    with step('[Verify] snapshot: 05_07_03_[x]2.png'):
        actions.capture_for_gt('05_07_03_[x]2.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_07_03_[x]2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[x] fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Smooth')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Face')
    with step('[Action] tap_to_add_face'):
        assert actions.tap_by_coordinates(205, 401)
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] select_a_face'):
        actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap [v] fail'
    with step('[Verify] snapshot: base05_07_03_[v]2.png'):
        actions.capture_for_gt('base05_07_03_[v]2.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_07_03_[v]2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[v] fail'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00065 completion"):
        assert True
