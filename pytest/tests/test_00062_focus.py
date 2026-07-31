import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00062_focus')
def test_00062_focus(actions: DriverActions):
    """focus (Blur With Depth)"""
    mode = 1
    uuid = ['306c70b2-1dd2-11b2-8000-080027b246c3', '306c70b2-1dd2-11b2-8001-080027b246c3', '306c70b2-1dd2-11b2-8002-080027b246c3', '306c70b2-1dd2-11b2-8003-080027b246c3', '306c70b2-1dd2-11b2-8004-080027b246c3', '306c70b2-1dd2-11b2-8005-080027b246c3', '306c70b2-1dd2-11b2-8006-080027b246c3', '306c70b2-1dd2-11b2-8007-080027b246c3', '306c70b2-1dd2-11b2-8008-080027b246c3', '306c70b2-1dd2-11b2-8009-080027b246c3', '306c70b2-1dd2-11b2-800a-080027b246c3', '306c70b2-1dd2-11b2-800b-080027b246c3', '42ef93af-14c2-4de6-b973-8facacba31fd', 'dc83342e-b34d-47af-9dbb-72abca996841', 'bb3052d4-9d64-4154-9ef3-15b29bcbe92c']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit')
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
    with step('[Verify] snapshot: 05_19_01_before_focus.png'):
        actions.capture_for_gt('05_19_01_before_focus.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Focus')
    with step('[Verify] snapshot: base05_19_01_auto_detect.png'):
        actions.capture_for_gt('base05_19_01_auto_detect.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_19_01_auto_detect.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Auto detect fail'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)):
        assert False, 'Adjust slider fail'
    with step('[Verify] snapshot: base05_19_01_focus_max.png'):
        actions.capture_for_gt('base05_19_01_focus_max.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_19_01_focus_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider right fail'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)):
        assert False, 'Adjust slider fail'
    with step('[Verify] snapshot: base05_19_01_focus_min.png'):
        actions.capture_for_gt('base05_19_01_focus_min.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_19_01_focus_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider left fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blur')):
        assert False, 'Tap blur fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "focus"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '30'):
        pass
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)):
        assert False, 'Adjust slider fail'
    with step('[Verify] snapshot: base05_19_01_focus_blur_min.png'):
        actions.capture_for_gt('base05_19_01_focus_blur_min.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_19_01_focus_blur_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider left fail'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)):
        assert False, 'Adjust slider fail'
    with step('[Verify] snapshot: base05_19_01_focus_blur_max.png'):
        actions.capture_for_gt('base05_19_01_focus_blur_max.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_19_01_focus_blur_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider left fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'Tap x fail'
    with step('[Verify] snapshot: 05_19_01_leave_focus_x.png'):
        actions.capture_for_gt('05_19_01_leave_focus_x.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if actions.compare_with_gt('05_19_01_leave_focus_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Exit color shift fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.NAME, 'Focus')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap v fail'
    with step('[Verify] snapshot: 05_19_01_tap_v.png'):
        actions.capture_for_gt('05_19_01_tap_v.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if (not actions.compare_with_gt('05_19_01_tap_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    with step("[Verify] test_00062 completion"):
        assert True
