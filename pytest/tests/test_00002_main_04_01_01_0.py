import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00002_main_04_01_01_0')
def test_00002_main_04_01_01_0(actions: DriverActions):
    """1. Enter camera, check if permission pop up, and allow it"""
    with step('[Action] close_promo_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] tap_camera_1st'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Camera')
    with step('[Verify] snapshot: 03_01_01_camera_permission.png'):
        actions.capture_for_gt('03_01_01_camera_permission.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] close_camera_permission'):
        assert actions.is_element_present(AppiumBy.NAME, '“PhotoDirector” would like to access the Camera.')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow')
    microphone_handled = False
    location_handled = False
    for attempt in range(2):
        if not microphone_handled:
            with step('[Verify] snapshot: snapshot'):
                actions.capture_for_gt(
                    f'03_01_01_permission_check_{attempt}.png',
                    crop_rect=(0, 60, 276, 597),
                )
            if actions.is_element_present(AppiumBy.NAME, '“PhotoDirector” Would Like to Access the Microphone'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow')
                assert actions.wait_for_invisible(
                    AppiumBy.NAME,
                    '“PhotoDirector” Would Like to Access the Microphone',
                    timeout=3,
                )
                microphone_handled = True
                continue
            else:
                microphone_handled = True
                continue
        if not location_handled:
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Allow “PhotoDirector” to use your location?'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow While Using App')
                assert actions.wait_for_invisible(
                    AppiumBy.ACCESSIBILITY_ID,
                    'Allow “PhotoDirector” to use your location?',
                    timeout=3,
                )
                location_handled = True
                continue
            else:
                location_handled = True
                continue
    if not microphone_handled:
        assert False, 'Microphone permission dialog not found'
    if not location_handled:
        assert False, 'Location permission dialog not found'
    with step("[Verify] test_00002 completion"):
        assert True
