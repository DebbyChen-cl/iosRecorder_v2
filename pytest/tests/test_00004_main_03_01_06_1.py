import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00004_main_03_01_06_1')
def test_00004_main_03_01_06_1(actions: DriverActions):
    """1. Enter setting page"""
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step('Verify Sign In'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Sign in', timeout=10):
            with step('Sign In to Cyberlink Account'):
                with step('[Action] sign_in'):
                    assert actions.tap_by_locator(AppiumBy.NAME, 'Sign in')
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
                    assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Sign in')
                    actions.type_text_by_locator(AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Email"]', TD.SIGN_IN_ACCOUNT)
                    actions.type_text_by_locator(AppiumBy.XPATH, '//XCUIElementTypeSecureTextField[@value="Password (6-20 characters)"]', TD.SIGN_IN_PASSWORD)
                    assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Sign In"]')
            with step('Verify Sign In'):
                if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Sign in', timeout=10)):
                    assert False, 'Verify sign in fail'
    with step("[Verify] test_00004 completion"):
        assert True
