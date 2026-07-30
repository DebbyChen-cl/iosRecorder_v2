import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00083_main_05_07_16_2')
def test_00083_main_05_07_16_2(actions: DriverActions):
    """conceal, no face"""
    uuid = ['8522ab50-321c-4c9b-bbca-4f6ffb10b311', '20db337b-8a28-4055-a0a8-f59127f31efd', '5ca3e5b3-9c82-441c-99ac-255e9e8739ce', '7c48bb79-4fa0-445b-8ea6-8496bfba49b5', '08616cd0-8ca2-489c-8eed-b6faf03fdbe6', '7e0d69ee-ec3b-4fa2-bce7-8c33b41295dc']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step('[Verify] snapshot: 05_07_16_before_conceal2.png'):
        actions.capture_for_gt('05_07_16_before_conceal2.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Conceal')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Please choose another photo'):
        pass
    else:
        assert False, 'No face dialog verification failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')):
        assert False, 'Tap ok fail'
    with step("[Verify] test_00083 completion"):
        assert True
