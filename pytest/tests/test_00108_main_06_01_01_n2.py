import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00108_main_06_01_01_n2')
def test_00108_main_06_01_01_n2(actions: DriverActions):
    """Text bubble - new - font"""
    mode = 1
    uuid = ['53d25ce6-525f-4b91-8100-891d13429c77', 'bdd10470-280e-4969-9f4b-8ded87e20922', '15cbc5f3-3380-42c3-a6b1-b2b51107f789', '274196b3-d25d-4dfe-bd5a-a5e0550a8511', 'ee9d2af3-3108-4349-b9f4-f7d15e4856a1', '71219c59-5c1b-4e10-b44d-859b7ba99785', 'c898aa71-b4b9-42e0-8a24-171326c7612c']
    with step('[Action] close_continue_edit'):
        actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
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
    with step('[Verify] snapshot: 06_01_01_no_font_panel.png'):
        actions.capture_for_gt('06_01_01_no_font_panel.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Font')
    with step('[Verify] snapshot: 06_01_01_font_default.png'):
        actions.capture_for_gt('06_01_01_font_default.png')
    if actions.compare_with_gt('06_01_01_font_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare default font panel failed'
    with step('[Verify] snapshot: 06_01_01_font_default_size.png'):
        actions.capture_for_gt('06_01_01_font_default_size.png')
    from_pos = (215, 500)
    destination = (215, 100)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(215, 500, 215, 100)
    with step('[Verify] snapshot: 06_01_01_font_extend.png'):
        actions.capture_for_gt('06_01_01_font_extend.png')
    if not actions.compare_with_gt('06_01_01_font_extend.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'extended panel fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 06_01_01_close_panel_x.png'):
        actions.capture_for_gt('06_01_01_close_panel_x.png')
    if actions.compare_with_gt('06_01_01_close_panel_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare close panel x failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Font')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]')
    with step('[Verify] snapshot: 06_01_01_change_font.png'):
        actions.capture_for_gt('06_01_01_change_font.png')
    if actions.compare_with_gt('06_01_01_change_font.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare change font failed'
    with step('[Verify] snapshot: 06_01_01_before_close_panel_drag.png'):
        actions.capture_for_gt('06_01_01_before_close_panel_drag.png')
    from_pos = (206, 482)
    destination = (206, 800)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 482, 206, 800)
    with step('[Verify] snapshot: 06_01_01_after_close_panel_drag.png'):
        actions.capture_for_gt('06_01_01_after_close_panel_drag.png')
    if not actions.compare_with_gt('06_01_01_after_close_panel_drag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare drag down close panel failed'
    with step("[Verify] test_00108 completion"):
        assert True
