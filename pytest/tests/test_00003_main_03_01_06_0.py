import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00003_main_03_01_06_0')
def test_00003_main_03_01_06_0(actions: DriverActions):
    """1. Enter setting page"""

    with step('Close promo IAP'):
        with step('[Action] close_promo_IAP'):
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('Enter setting page'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
        with step('[Action] verify_settings_page'):
            assert (
                actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Setting', timeout=5)
                or actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle', timeout=5)
            )
    with step('Enter about page'):
        enter_about_page_success = False
        for attempt in range(3):
            with step('[Action] enter_about_page'):
                if actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'About') and actions.is_element_present(
                    AppiumBy.ACCESSIBILITY_ID, 'developerButton', timeout=3
                ):
                    enter_about_page_success = True
                    break
        if not enter_about_page_success:
            assert False, 'Enter about page fail after 3 retries'
    with step('Open debug setting and enable snapshot'):
        with step('Open debug setting'):
            with step('[Action] open_debug_setting'):
                for _ in range(5):
                    actions.tap_by_coordinates(60, 165)
                assert actions.is_element_present(AppiumBy.NAME, 'Develop Info')
        with step('Enable snapshot'):
            with step('[Action] force_allow_screenshot_on'):
                actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[6]')
        with step('Verify snapshot enabled'):
            with step('[Action] verify_force_allow_snapshot_on'):
                assert actions.find_element(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="1"])[2]')
        with step('Tap back button'):
            with step('[Action] tap_phd_btn'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
        with step('Tap setting back button'):
            with step('[Action] tap_phd_btn'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] test_00003 completion"):
        assert True
