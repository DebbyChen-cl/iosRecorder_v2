import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00188_regression_quick_action')
def test_00188_regression_quick_action(actions: DriverActions):
    """regression - quick action"""    
    with step('Close any popups on main page'):
        with step('[Action] close_xmas'):
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Close', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Close')
        with step('[Action] close_continue_edit'):
            if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('Tap Edit button'):
        with step('[Action] tap_editphoto'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('Expand album list > Select Regression album'):
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Regression')
    with step('Select multi-face photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('Tap Quick Action tab'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
    with step('Verify Retouch entry exists'):
        if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')):
            assert False, 'Retouch entry not found in Quick Action tab'
    with step("[Verify] test_00188 completion"):
        assert True
