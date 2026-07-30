import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00023_main_05_01_10_1')
def test_00023_main_05_01_10_1(actions: DriverActions):
    """AI enhance pro+"""
    uuid = ['0986e8e2-2c87-47a9-a34d-bcc84f2fcb0e', '5654898f-974b-46f3-a5cc-99c2db353683', 'f5097c28-d824-44dd-9ca9-35ac44452363', '56fc19c9-d1e5-43bc-b251-df603d2d1965', '7d322096-6185-413f-a49b-489800b2b8df']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Verify] snapshot: 05_01_10_before_aienhance_p.png'):
        actions.capture_for_gt('05_01_10_before_aienhance_p.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Enhance')):
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')):
        assert False  # legacy raise
    with step('[Action] wait_enhance_process'):
        actions.wait_for_invisible(AppiumBy.NAME, 'Enhancing')
    with step('[Verify] snapshot: base_05_01_10_aienhance_p.png'):
        actions.capture_for_gt('base_05_01_10_aienhance_p.png', crop_rect=(0, 60, 276, 429))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    settings_locators = [(AppiumBy.ACCESSIBILITY_ID, 'settingButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnSettings'), (AppiumBy.ACCESSIBILITY_ID, 'ic settings launcher')]
    if not actions.try_tap_any(settings_locators):
        assert False, 'Tap setting button fail'
    with step('[Action] verify_settings_page'):
        assert (actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Setting') or
                actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'))
    enter_about_page_success = False
    for attempt in range(3):
        with step('[Action] enter_about_page'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'About')
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton')
        enter_about_page_success = True
        break
        if attempt < 2:
            pass
    if not enter_about_page_success:
        assert False, 'Enter about page fail after 3 retries'
    with step('[Action] enable_plan_from_settings'):
        actions.is_element_present(AppiumBy.NAME, 'Develop Info')
        actions.find_element(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="1"])[2]')
        actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[6]')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_enhance1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Enhance')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pro')
    with step('[Action] click_element'):
        actions.tap_by_locator(AppiumBy.CLASS_NAME, 'XCUIElementTypeSwitch')
    with step('[Action] wait_enhance_process'):
        actions.wait_for_invisible(AppiumBy.NAME, 'Enhancing')
    assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'settingButton')
    with step('[Action] verify_settings_page'):
        assert (actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Setting') or
                actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'))
    enter_about_page_success = False
    for attempt in range(3):
        with step('[Action] enter_about_page'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'About')
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton')
        enter_about_page_success = True
        break
        if attempt < 2:
            pass
    if not enter_about_page_success:
        assert False, 'Enter about page fail after 3 retries'
    with step('[Action] enable_plan_from_settings'):
        actions.is_element_present(AppiumBy.NAME, 'Develop Info')
        actions.find_element(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="1"])[2]')
        actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[6]')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_enhance1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Enhance')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pro')
    with step('[Action] click_element'):
        actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[`value == "0"`]')
    with step('[Action] wait_enhance_process'):
        actions.wait_for_invisible(AppiumBy.NAME, 'Enhancing')
    assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])
    actions.capture_for_gt('05_01_10_aienhance_v_p.png', crop_rect=(0, 60, 276, 429))
    with step("[Verify] test_00023 completion"):
        assert True
