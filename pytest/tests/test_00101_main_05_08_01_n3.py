import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00101_main_05_08_01_n3')
def test_00101_main_05_08_01_n3(actions: DriverActions):
    """Text tools - text new - format"""
    mode = 1
    uuid = ['131f5fcc-384d-4e49-a675-f23e50f20a07', 'c5567916-54c1-42b7-88bf-bc35fd7e774e', 'c6ad691d-0f94-4605-bac2-9f5aaf860480', 'ba8745fa-627c-45df-a7b8-b29e27236e98', 'dce11a56-9975-41cf-b82d-206fad2869ba', '332e1852-cb13-4e3a-b798-c3700491e835', '923903a3-73d8-417d-848d-37fba1dd5b42', '119b067d-d1e8-4995-8d82-8e75f71867ca', '9dd8d011-8471-462e-b299-160c695eec40']
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
    with step('[Action] tap_edit1_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    from_pos = (380, 770)
    destination = (50, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 50, 770)
    if actions.is_element_present(AppiumBy.NAME, 'xpromo btn close n', timeout=2):
        with step('[Action] tap_close_xpromo_btn'):
            actions.tap_by_locator(AppiumBy.NAME, 'xpromo btn close n')
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'Text')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTextEdit')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'A')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'a')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'a')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Return')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'A')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn top done n')
    with step('[Verify] snapshot: 05_08_01_no_format_panel.png'):
        actions.capture_for_gt('05_08_01_no_format_panel.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Format')
    with step('[Verify] snapshot: 05_08_01_format_default.png'):
        actions.capture_for_gt('05_08_01_format_default.png')
    if actions.compare_with_gt('05_08_01_format_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare format default fail'
    with step('[Verify] snapshot: 05_08_01_before_close_format_panel_x.png'):
        actions.capture_for_gt('05_08_01_before_close_format_panel_x.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 05_08_01_close_format_panel_x.png'):
        actions.capture_for_gt('05_08_01_close_format_panel_x.png')
    if not actions.compare_with_gt('05_08_01_close_format_panel_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Close format panel x comparison fail'
    with step('[Action] focus_text'):
        actions.tap_by_coordinates(205, 455)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Format')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'alignLeftButton')
    with step('[Verify] snapshot: 05_08_01_format_left.png'):
        actions.capture_for_gt('05_08_01_format_left.png')
    if actions.compare_with_gt('05_08_01_format_left.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare format left fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'alignRightButton')
    with step('[Verify] snapshot: 05_08_01_format_right.png'):
        actions.capture_for_gt('05_08_01_format_right.png')
    if actions.compare_with_gt('05_08_01_format_right.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare format right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'alignCenterButton')
    with step('[Verify] snapshot: 05_08_01_format_center.png'):
        actions.capture_for_gt('05_08_01_format_center.png')
    if actions.compare_with_gt('05_08_01_format_center.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare format center fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'boldButton')
    with step('[Verify] snapshot: 05_08_01_format_bold.png'):
        actions.capture_for_gt('05_08_01_format_bold.png')
    if actions.compare_with_gt('05_08_01_format_bold.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare format bold fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'italicButton')
    with step('[Verify] snapshot: 05_08_01_format_italic.png'):
        actions.capture_for_gt('05_08_01_format_italic.png')
    if actions.compare_with_gt('05_08_01_format_italic.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare format italic fail'
    with step('[Verify] snapshot: 05_08_01_before_adjust_slider.png'):
        actions.capture_for_gt('05_08_01_before_adjust_slider.png')
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0.5')
    with step('[Verify] snapshot: 05_08_01_after_adjust_slider.png'):
        actions.capture_for_gt('05_08_01_after_adjust_slider.png')
    if not actions.compare_with_gt('05_08_01_after_adjust_slider.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Size slider comparison fail'
    with step('[Verify] snapshot: 05_08_01_before_close_format_drag.png'):
        actions.capture_for_gt('05_08_01_before_close_format_drag.png')
    from_pos = (206, 476)
    destination = (206, 800)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 476, 206, 800)
    with step('[Verify] snapshot: 05_08_01_after_close_format_drag.png'):
        actions.capture_for_gt('05_08_01_after_close_format_drag.png')
    if not actions.compare_with_gt('05_08_01_after_close_format_drag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Drag down close panel comparison fail'
    with step("[Verify] test_00101 completion"):
        assert True
