import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00126_main_05_11_01_8')
def test_00126_main_05_11_01_8(actions: DriverActions):
    """add-image text / text bubble"""
    mode = 1
    uuid = ['30123793-5e76-4d4b-9fa1-1550b8d38648', '5a55502b-a423-4e4c-a79e-f91c5b262757', 'e9823e12-e49a-4564-978f-9d489fd56ec3', '73cf08f0-558a-4ff0-a04b-a410c22b9b7a', '905de001-bf70-4e81-b7e4-d8ab8f929e64', '864aceb3-b12c-45a6-b26b-0ca72f0f2236', '6ea99591-f658-4629-bbab-4df335ad5a73', 'b106c3b8-16b5-4407-b9c1-04e3d33408d6', 'fc6648f6-5310-46e5-848c-5177b786c54d']
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
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category_add_image'):
        assert actions.tap_by_locator(AppiumBy.NAME, '_AT')
    with step('[Action] add_image'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Verify] snapshot: 05_11_01_add_1_photo.png'):
        actions.capture_for_gt('05_11_01_add_1_photo.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Add Text')
    destination = (380, 350)
    with step('[Action] drag_text_rotate_n'):
        actions.long_press_drag_from_element_to_coordinates(
            AppiumBy.ACCESSIBILITY_ID,
            'rotateImageView',
            50.0,
            50.0,
            destination[0],
            destination[1],
        )
    with step('[Verify] snapshot: 05_11_01_add_before_font.png'):
        actions.capture_for_gt('05_11_01_add_before_font.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Font')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[2]')
    with step('[Verify] snapshot: 05_11_01_after_font.png'):
        actions.capture_for_gt('05_11_01_after_font.png')
    if (not actions.compare_with_gt('05_11_01_after_font.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Fail to verify font change'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step('[Action] select_text_panel_color'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[6]')
    with step('[Verify] snapshot: 05_11_01_after_solid.png'):
        actions.capture_for_gt('05_11_01_after_solid.png')
    if (not actions.compare_with_gt('05_11_01_after_solid.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Fail to verify solid color change'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Gradient')
    with step('[Action] select_text_panel_color'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]')
    with step('[Verify] snapshot: 05_11_01_after_gradient.png'):
        actions.capture_for_gt('05_11_01_after_gradient.png')
    if (not actions.compare_with_gt('05_11_01_after_gradient.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Fail to verify gradient color change'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Format')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'boldButton')
    with step('[Verify] snapshot: 05_11_01_after_format.png'):
        actions.capture_for_gt('05_11_01_after_format.png')
    if (not actions.compare_with_gt('05_11_01_after_format.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Fail to verify text format change'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Border')
    with step('[Action] select_text_panel_border_color'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[8]')
    with step('[Verify] snapshot: 05_11_01_after_border.png'):
        actions.capture_for_gt('05_11_01_after_border.png')
    if (not actions.compare_with_gt('05_11_01_after_border.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Fail to verify border color change'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')
    with step('[Action] select_text_panel_shadow_color'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[9]')
    with step('[Verify] snapshot: 05_11_01_after_shadow.png'):
        actions.capture_for_gt('05_11_01_after_shadow.png')
    if (not actions.compare_with_gt('05_11_01_after_shadow.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Fail to verify shadow change'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Text Bubble')
    with step('[Verify] snapshot: 05_11_01_after_text_bubble.png'):
        actions.capture_for_gt('05_11_01_after_text_bubble.png')
    if (not actions.compare_with_gt('05_11_01_after_text_bubble.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Fail to verify text bubble was added'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Font')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 05_11_01_after_font_b.png'):
        actions.capture_for_gt('05_11_01_after_font_b.png')
    if (not actions.compare_with_gt('05_11_01_after_font_b.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Fail to verify bubble font change'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step('[Action] select_text_panel_color_bubble'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[6]')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 05_11_01_after_solid_b.png'):
        actions.capture_for_gt('05_11_01_after_solid_b.png')
    if (not actions.compare_with_gt('05_11_01_after_solid_b.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Fail to verify bubble solid color change'
    with step("[Verify] test_00126 completion"):
        assert True
