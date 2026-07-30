import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00028_removal_flux')
def test_00028_removal_flux(actions: DriverActions):
    """removal - flux"""
    uuid = ['e0a1b05d-3b37-4ae5-aa7d-d1f3d4228d85', '32990581-f3ea-46b5-ad62-abce2c0857a1', '57c5ae49-6327-4f20-a669-da084e1c294a', 'affdd43b-d5d9-4933-abb8-b90283cf68b0', '5bb3df1c-92bd-43db-863e-1ebd93f0642a', '5648b65c-c139-4f7b-b428-33697eccb766', '276f7202-dd89-4d24-bdda-7cde22e296ae']
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] close_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')
    with step('[Action] close_airemoval_iap_dialog'):
        actions.is_element_present(AppiumBy.NAME, 'Remove with faster selection tool')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
        actions.wait_for_invisible(AppiumBy.NAME, 'Remove with faster selection tool')
    with step('[Action] close_airemoval_iap_dialog'):
        actions.is_element_present(AppiumBy.NAME, 'Remove with faster selection tool')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
        actions.wait_for_invisible(AppiumBy.NAME, 'Remove with faster selection tool')
    with step('[Action] close_airemoval_iap_dialog2'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'proPlusToggle')
    if actions.is_element_present(AppiumBy.NAME, 'Generative AI Removal'):
        pass
    else:
        assert False, 'upgrade dialog fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Upgrade to Pro+ Premium')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, 'IAP fail'
    with step('[Action] close_IAP'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
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
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')):
        assert False  # legacy raise
    with step('[Action] close_IAP'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] close_airemoval_iap_dialog2'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'proPlusToggle')):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Generative AI Removal'):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Upgrade to Pro+ Premium')):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
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
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'proPlusToggle'):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Manual')
    with step('[Verify] snapshot: 05_01_03_before_flux.png'):
        actions.capture_for_gt('05_01_03_before_flux.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    from_pos = (280, 300)
    destination = (280, 441)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(280, 300, 280, 441)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'applyButton')):
        assert False  # legacy raise
    with step('[Action] wait_remove_process'):
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'magicText')
    actions.capture_for_gt('05_01_03_after_flux.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Verify] test_00028 completion"):
        assert True
