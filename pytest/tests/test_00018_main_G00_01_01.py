import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00018_main_G00_01_01')
def test_00018_main_G00_01_01(actions: DriverActions):
    """credit system"""
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mine')
    elements = ['str_upgrade_to_pro', 'str_upgrade_to_pro2']
    if not any((actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Upgrade to Pro+!'), actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'))):
        assert False, '[G00_01_01] Failed to verify mine page'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTaskCenter')
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.NAME, 'Routine Task')
    with step('[Action] perform_task'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Invite Friends')
    with step('[Verify] snapshot: G00_01_01_invite_friend.png'):
        actions.capture_for_gt('G00_01_01_invite_friend.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="shareCell" and @label="AirDrop"]')
    with step('[Action] close_share_menu'):
        assert actions.tap_by_coordinates(150, 200)
    with step('[Verify] snapshot: G00_01_01_back01.png'):
        actions.capture_for_gt('G00_01_01_back01.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] close_share_menu'):
        assert actions.tap_by_coordinates(150, 200)
    with step('[Verify] snapshot: G00_01_01_share_artwork.png'):
        actions.capture_for_gt('G00_01_01_share_artwork.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="shareCell" and @label="AirDrop"]')
    with step('[Action] close_share_menu'):
        assert actions.tap_by_coordinates(150, 200)
    with step('[Verify] snapshot: G00_01_01_back02.png'):
        actions.capture_for_gt('G00_01_01_back02.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] perform_task'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Follow us on Instagram')
    with step('[Verify] snapshot: G00_01_01_ig.png'):
        actions.capture_for_gt('G00_01_01_ig.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.NAME, 'photodirector_app')
    with step('[Action] Tap'):
        assert actions.tap_by_coordinates(46, 39)
    with step('[Verify] snapshot: G00_01_01_back03.png'):
        actions.capture_for_gt('G00_01_01_back03.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] perform_task'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Subscribe to Our YouTube')
    with step('[Verify] snapshot: G00_01_01_y2b.png'):
        actions.capture_for_gt('G00_01_01_y2b.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.NAME, 'PhotoDirector Photo Editor - CyberLink')
    with step('[Action] Tap'):
        assert actions.tap_by_coordinates(46, 39)
    with step('[Verify] snapshot: G00_01_01_back04.png'):
        actions.capture_for_gt('G00_01_01_back04.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClaim')
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, '5 Free Credits Have Been Issued to You')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Upgrade Now')
    with step('[Action] verify_IAP'):
        assert actions.find_element(AppiumBy.NAME, 'Start 7-Day Free Trial')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_IAP'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Buy Now')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Get 300 Free Credits Each Month!')
    with step('[Action] verify_IAP'):
        assert actions.find_element(AppiumBy.NAME, 'Start 7-Day Free Trial')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_IAP'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '50')
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Get 50 Credits for $9.99')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '100')
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Get 100 Credits for $17.99')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '200')
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Get 200 Credits for $31.99')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Purchase')
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, '200 Credits')
    with step('[Action] click_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'dismiss')
    with step("[Verify] test_00018 completion"):
        assert True
