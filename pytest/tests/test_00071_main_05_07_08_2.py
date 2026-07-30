import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00071_main_05_07_08_2')
def test_00071_main_05_07_08_2(actions: DriverActions):
    """nose enhance, no face"""
    mode = 1
    uuid = ['873ce987-1f57-4794-ae3a-128af2f698bf', '7c868114-b05e-47c4-b58b-42098b6558a2', '5f26183a-bed7-4a64-889c-52358b40eb6b', 'fb6dbb6a-0829-41d4-a81a-25178d5dd324', '5ea74000-74ae-4e70-9da7-0bda1a40ad09', '5f664645-0c60-4e63-aa8b-f1891430d472']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step('[Verify] snapshot: 05_07_08_before_nose2.png'):
        actions.capture_for_gt('05_07_08_before_nose2.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Nose Enhance')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Please choose another photo'):
        pass
    else:
        assert False, 'No face dialog fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')):
        assert False, 'Tap ok fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Face')
    with step('[Action] close_add_face_tutorial'):
        assert actions.is_element_present(AppiumBy.NAME, 'Drag to move the crosses over the eyes and lips.')
        assert actions.tap_by_coordinates(250, 250)
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Drag to move the crosses over the eyes and lips.')
    with step('[Action] tap_image'):
        assert actions.tap_by_coordinates(205, 401)
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] select_a_face'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'Tap x fail'
    with step('[Verify] snapshot: 05_07_08_[x]2.png'):
        actions.capture_for_gt('05_07_08_[x]2.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_07_08_[x]2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[x] comparison fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Nose Enhance')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap [v] fail'
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, '[v] fail'
    with step("[Verify] test_00071 completion"):
        assert True
