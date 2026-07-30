import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00109_main_06_01_01_n3')
def test_00109_main_06_01_01_n3(actions: DriverActions):
    """Text bubble - new - format"""
    mode = 1
    uuid = ['456fbf33-5355-4b0a-bf85-c42134f038c8', '4e9e3fca-9211-4783-9db3-568981abdf3f', '744dbfa7-6ced-4a7a-ad1a-310895374dec', '1d101924-40db-48df-85e5-955d8705e810', '7e4f0b35-4122-4fcb-b345-b94983b8e5e2', 'cc3bb91a-b888-4ec5-b59b-eea6cbe2169d', '6e055197-e623-4a75-9693-e36f05b72699', '469328c5-8cc8-423f-bcdb-783f715e7190', '98f768e2-d947-4dcf-a480-587d02dcd80a']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    from_pos = (380, 770)
    destination = (50, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text Bubble')
    with step('[Action] focus_text'):
        actions.tap_by_coordinates(205, 400)
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
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next keyboard')
    with step('[Verify] snapshot: 06_01_01_change_kb_lan.png'):
        actions.capture_for_gt('06_01_01_change_kb_lan.png')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next keyboard')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next keyboard')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next keyboard')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn top done n')
    with step('[Verify] snapshot: 06_01_01_no_format_panel.png'):
        actions.capture_for_gt('06_01_01_no_format_panel.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Format')
    with step('[Verify] snapshot: 06_01_01_format_default.png'):
        actions.capture_for_gt('06_01_01_format_default.png')
    if actions.compare_with_gt('06_01_01_format_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare default format panel failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 06_01_01_close_format_panel_x.png'):
        actions.capture_for_gt('06_01_01_close_format_panel_x.png')
    if actions.compare_with_gt('06_01_01_close_format_panel_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tap x close panel fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Format')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'alignLeftButton')
    with step('[Verify] snapshot: 06_01_01_format_left.png'):
        actions.capture_for_gt('06_01_01_format_left.png')
    if actions.compare_with_gt('06_01_01_format_left.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'align left 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'alignRightButton')
    with step('[Verify] snapshot: 06_01_01_format_right.png'):
        actions.capture_for_gt('06_01_01_format_right.png')
    if actions.compare_with_gt('06_01_01_format_right.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'align right 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'alignCenterButton')
    with step('[Verify] snapshot: 06_01_01_format_center.png'):
        actions.capture_for_gt('06_01_01_format_center.png')
    if actions.compare_with_gt('06_01_01_format_center.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'align center 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'boldButton')
    with step('[Verify] snapshot: 06_01_01_format_bold.png'):
        actions.capture_for_gt('06_01_01_format_bold.png')
    if actions.compare_with_gt('06_01_01_format_bold.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'bold 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'italicButton')
    with step('[Verify] snapshot: 06_01_01_format_italic.png'):
        actions.capture_for_gt('06_01_01_format_italic.png')
    if actions.compare_with_gt('06_01_01_format_italic.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'italic 0 fail'
    with step('[Verify] snapshot: 06_01_01_before_close_format_drag.png'):
        actions.capture_for_gt('06_01_01_before_close_format_drag.png')
    from_pos = (206, 482)
    destination = (206, 800)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 482, 206, 800)
    with step('[Verify] snapshot: 06_01_01_after_close_format_drag.png'):
        actions.capture_for_gt('06_01_01_after_close_format_drag.png')
    if not actions.compare_with_gt('06_01_01_after_close_format_drag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'drag down close panel fail'
    with step("[Verify] test_00109 completion"):
        assert True
