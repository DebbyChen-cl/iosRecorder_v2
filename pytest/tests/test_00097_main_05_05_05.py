import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00097_main_05_05_05')
def test_00097_main_05_05_05(actions: DriverActions):
    """Overlays - lens flare"""
    mode = 1
    uuid = ['eeda57fa-c793-49d4-8d1b-6258212375f2', '50e8f7b0-9f04-436f-86f7-ccfa5d75c74f', 'ee7e0433-f804-483b-8a48-aaf0dccf343c', '1db02af9-eee4-4877-9c7f-25bb33895acd', '0ca253e0-ba53-4ec1-bd3d-548d0448c10c', '0fb648ee-cdaa-47bd-87f0-91db4b343c94', '7994758a-9558-47a2-a45e-f0df584b6d56', '9aeeceb0-3c20-4858-94e0-a614814fd535', '5df65f1e-6838-4037-98c2-d26db46ee47a', 'cc6f620b-07ac-4d0d-9bdd-e0e27fbb7418', '21f9f732-084d-4321-99a4-a23e2c5b5ee9']
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
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(3):
        from_pos = (380, 770)
        destination = (50, 770)
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Verify] snapshot: 05_05_05_before_lensflare.png'):
        actions.capture_for_gt('05_05_05_before_lensflare.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Overlay Effect')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lens Flare')
    with step('[Verify] snapshot: 05_05_05_temp1.png'):
        actions.capture_for_gt('05_05_05_temp1.png')
    if actions.compare_with_gt('05_05_05_temp1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'template 1 fail'
    with step('[Action] adjust_overlays_slider'):
        assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)
    with step('[Verify] snapshot: 05_05_05_slider_left.png'):
        actions.capture_for_gt('05_05_05_slider_left.png')
    if actions.compare_with_gt('05_05_05_slider_left.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'min fail'
    with step('[Action] adjust_overlays_slider'):
        assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0.5)
    with step('[Verify] snapshot: 05_05_05_slider_half.png'):
        actions.capture_for_gt('05_05_05_slider_half.png')
    if actions.compare_with_gt('05_05_05_slider_half.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '50% fail'
    with step('[Action] adjust_overlays_slider'):
        assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)
    with step('[Verify] snapshot: 05_05_05_slider_right.png'):
        actions.capture_for_gt('05_05_05_slider_right.png')
    if actions.compare_with_gt('05_05_05_slider_right.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'max fail'
    destination = (150, 235)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Action] drag_lensflare_zoom'):
        x, y, width, height = actions.get_element_bounds(
            AppiumBy.IOS_CLASS_CHAIN,
            '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]',
        )
        actions.drag_coordinates(x + width // 2, y + height // 2, destination[0], destination[1])
    with step('[Verify] snapshot: 05_05_05_zoom.png'):
        actions.capture_for_gt('05_05_05_zoom.png')
    if actions.compare_with_gt('05_05_05_zoom.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'adjust size/rotate fail'
    from_pos = (200, 400)
    destination = (200, 350)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(200, 400, 200, 350)
    with step('[Verify] snapshot: 05_05_05_move.png'):
        actions.capture_for_gt('05_05_05_move.png')
    if actions.compare_with_gt('05_05_05_move.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'move fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'tap [x] fail'
    with step('[Verify] snapshot: 05_05_05_tap_x.png'):
        actions.capture_for_gt('05_05_05_tap_x.png')
    if actions.compare_with_gt('05_05_05_tap_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Overlay Effect')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lens Flare')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'tap [v] fail'
    with step('[Verify] snapshot: 05_05_05_tap_v.png'):
        actions.capture_for_gt('05_05_05_tap_v.png')
    if (not actions.compare_with_gt('05_05_05_tap_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00097 completion"):
        assert True
