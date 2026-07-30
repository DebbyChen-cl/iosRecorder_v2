import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00079_main_05_07_13_2')
def test_00079_main_05_07_13_2(actions: DriverActions):
    """wrinkle, no face"""
    uuid = ['c7608e0f-3d45-47b3-a18a-e8e36bfe1a7d', '293575f7-3fc1-4ca9-8a9f-eed3b3659454', 'a487b6df-ff6d-41e6-b2e3-1c9da52e23f5', '7c5fdad1-48a1-447b-8fad-5a6965b18fc9', 'cbe2f710-1d93-41dd-8a48-87938a21b8cc', '000be3b7-c66b-49b1-87c5-d9a9d8a38103']
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
    with step('[Verify] snapshot: 05_07_13_before_wrinkle2.png'):
        actions.capture_for_gt('05_07_13_before_wrinkle2.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Wrinkle')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Please choose another photo'):
        pass
    else:
        assert False, 'No face dialog fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')):
        assert False, 'Tap ok fail'
    with step("[Verify] test_00079 completion"):
        assert True
