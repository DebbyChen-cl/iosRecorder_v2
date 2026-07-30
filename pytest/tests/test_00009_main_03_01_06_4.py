import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00009_main_03_01_06_4')
def test_00009_main_03_01_06_4(actions: DriverActions):
    """1. Tap shopping cart icon to enter IAP page"""
    with step('[Action] tap_shoppping_cart'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_IAP_back_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'imgViewTitle')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mine')
    with step('[Action] tap_notice_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNotification')
        assert actions.is_element_present(AppiumBy.NAME, 'Notices')
    with step('[Action] tap_expend_notice'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'imgDisclosure')
    with step('[Action] tap_notice_link'):
        assert actions.try_tap_any([
            (AppiumBy.ACCESSIBILITY_ID, 'Try Now'),
            (AppiumBy.NAME, 'Show more>>'),
            (AppiumBy.NAME, 'Show Me More >>'),
        ])
    with step("[Verify] test_00009 completion"):
        assert True
