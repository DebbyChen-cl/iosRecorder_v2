import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00001_main_05_01_06')
def test_00001_main_05_01_06(actions: DriverActions):
    """1. Tap "Edit Photo" icon on main page"""
    with step('[Action] close_xmas'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Close', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Close')
    with step('[Action] tap_try_now_back_to_main'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
    with step('[Verify] snapshot: before_photo_permission.png'):
        actions.capture_for_gt('before_photo_permission.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] tap_editphoto_1st'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
        assert actions.is_element_present(AppiumBy.NAME, '“PhotoDirector” would like full access to your Photo Library.')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Full Access')
    with step('[Verify] snapshot: after photo_permission.png'):
        actions.capture_for_gt('after photo_permission.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] tap_photo_picker_back_btn_to_main'):
        assert actions.try_tap_any([
            (AppiumBy.ACCESSIBILITY_ID, 'btnBack'),
            (AppiumBy.ACCESSIBILITY_ID, 'btnClose'),
        ])
        assert actions.is_element_present(AppiumBy.NAME, 'Edit')
    with step("[Verify] test_00001 completion"):
        assert True
