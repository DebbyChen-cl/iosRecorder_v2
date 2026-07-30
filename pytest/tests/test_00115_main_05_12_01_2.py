import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00115_main_05_12_01_2')
def test_00115_main_05_12_01_2(actions: DriverActions):
    """frame apply"""
    mode = 1
    uuid = ['1efdb518-5115-41fb-a39c-88c95e1812bf', 'b95dddad-50d0-4723-9969-9d2bcb0b2b96', '89017b20-227a-48a4-967c-a70314021a49', '2660971c-6492-462c-95a8-7d66de452b21']
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
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Frame')
    with step('[Verify] snapshot: 05_12_01_frame_default.png'):
        actions.capture_for_gt('05_12_01_frame_default.png')
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[3]')):
        assert False, 'tap frame frame pack 1 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')):
        assert False, 'tap frame frame 1 fail'
    with step('[Verify] snapshot: 05_12_01_frame_after_apply.png'):
        actions.capture_for_gt('05_12_01_frame_after_apply.png')
    if (not actions.compare_with_gt('05_12_01_frame_after_apply.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'apply frame fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'tap x fail'
    with step('[Verify] snapshot: 05_12_01_tap_x.png'):
        actions.capture_for_gt('05_12_01_tap_x.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if actions.compare_with_gt('05_12_01_tap_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tap x fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Frame')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[3]')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'tap v fail'
    with step('[Verify] snapshot: 05_12_01_tap_v.png'):
        actions.capture_for_gt('05_12_01_tap_v.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if actions.compare_with_gt('05_12_01_tap_v.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tap v fail'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00115 completion"):
        assert True
