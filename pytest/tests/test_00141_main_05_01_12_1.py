import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00141_main_05_01_12_1')
def test_00141_main_05_01_12_1(actions: DriverActions):
    """quick action - auto"""
    mode = 1
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle')
    with step('[Verify] snapshot: 05_01_12_before_quick_auto.png'):
        actions.capture_for_gt('05_01_12_before_quick_auto.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'labelWaiting', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'labelWaiting')
    with step('[Verify] snapshot: 05_01_12_auto_default.png'):
        actions.capture_for_gt('05_01_12_auto_default.png')
    with step('[Verify] compare: 05_01_12_auto_default.png'):
        assert actions.compare_with_gt('05_01_12_auto_default.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'None')
    with step('[Verify] snapshot: 05_01_12_auto_none.png'):
        actions.capture_for_gt('05_01_12_auto_none.png')
    with step('[Verify] compare: 05_01_12_auto_none.png'):
        assert actions.compare_with_gt('05_01_12_auto_none.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Basic')
    with step('[Verify] snapshot: 05_01_12_auto_basic.png'):
        actions.capture_for_gt('05_01_12_auto_basic.png')
    with step('[Verify] compare: 05_01_12_auto_basic.png'):
        assert actions.compare_with_gt('05_01_12_auto_basic.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light')
    with step('[Verify] snapshot: 05_01_12_auto_light.png'):
        actions.capture_for_gt('05_01_12_auto_light.png')
    with step('[Verify] compare: 05_01_12_auto_light.png'):
        assert actions.compare_with_gt('05_01_12_auto_light.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] verify_IAP'):
        assert actions.find_element(AppiumBy.NAME, 'Start 7-Day Free Trial')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_IAP'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_01_12_auto_x.png'):
        actions.capture_for_gt('05_01_12_auto_x.png')
    with step('[Verify] compare: 05_01_12_auto_x.png'):
        assert actions.compare_with_gt('05_01_12_auto_x.png', gt_folder=TD.GT_FOLDER)[0]
    with step("[Verify] test_00141 completion"):
        assert True
