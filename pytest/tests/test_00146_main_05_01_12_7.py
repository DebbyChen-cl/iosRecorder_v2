import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00146_main_05_01_12_7')
def test_00146_main_05_01_12_7(actions: DriverActions):
    """quick action - wire removal"""
    uuid = ['9b9a12c3-b992-4ff6-b9b8-fa49b288be9b', '6757c7f8-0e69-4571-ab9d-c9e5768a1519', '5c289f84-3eab-431e-930a-126d16c95a35', 'be93c4c7-6436-4476-b587-bb9ea589c622', 'b6d5a525-a958-4a34-a0c9-8bdc826983d5']
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    enter_about_page_success = False
    for attempt in range(3):
        with step('[Action] enter_about_page'):
            if actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'About') and actions.is_element_present(
                AppiumBy.ACCESSIBILITY_ID, 'developerButton'
            ):
                enter_about_page_success = True
                break
    if not enter_about_page_success:
        assert False, 'Enter about page fail after 3 retries'
    with step('[Action] enable_plan_from_settings'):
        assert actions.is_element_present(AppiumBy.NAME, 'Develop Info')
        assert actions.find_element(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="1"])[2]')
        actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[6]')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle')
    with step('[Verify] snapshot: 05_01_12_before_quick_wire.png'):
        actions.capture_for_gt('05_01_12_before_quick_wire.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Wire Removal')
    with step('[Action] close_free_try'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'labelWaiting', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'labelWaiting')
    with step('[Verify] snapshot: 05_01_12_wire_remove.png'):
        actions.capture_for_gt('05_01_12_wire_remove.png')
    if actions.compare_with_gt('05_01_12_wire_remove.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare wire_remove default fail'
    with step('[Action] flip_switch'):
        actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeSwitch[@value="1"]')
    with step('[Verify] snapshot: 05_01_12_wire_remove_off.png'):
        actions.capture_for_gt('05_01_12_wire_remove_off.png')
    with step('[Verify] compare: 05_01_12_wire_remove_off.png'):
        assert actions.compare_with_gt('05_01_12_wire_remove_off.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] flip_switch'):
        actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeSwitch[@value="0"]')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap done_btn [v] fail'
    if (not actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1)):
        pass
    else:
        assert False, 'Verify IAP [v] fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Wire Removal')
    with step('[Action] close_free_try'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'labelWaiting', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'labelWaiting')
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_01_12_wire_x.png'):
        actions.capture_for_gt('05_01_12_wire_x.png')
    if actions.compare_with_gt('05_01_12_wire_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare wire_x [x] fail'
    with step("[Verify] test_00146 completion"):
        assert True
