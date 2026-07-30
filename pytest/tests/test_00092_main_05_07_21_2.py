import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00092_main_05_07_21_2')
def test_00092_main_05_07_21_2(actions: DriverActions):
    """jawline no face"""
    mode = 1
    uuid = ['2331105a-e2b8-4a4a-a964-a6082e3eb18a', '9ecd318b-5046-4a44-ba3e-65f9cdb25297', 'ea3f55a8-48c3-4fb2-962d-247c9bd71f52', 'fd36e32a-3a62-4696-84b4-e00ac7cce1c0', '6aaf2583-2f82-4991-bd1a-932fa0b9b0a5', '4c9c041d-16be-4f86-bb63-2ed4de0b7377']
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
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    from_pos = (400, 780)
    destination = (10, 780)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 780, 10, 780)
    with step('[Verify] snapshot: 05_07_21_before_jawline2.png'):
        actions.capture_for_gt('05_07_21_before_jawline2.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Jawline')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Please choose another photo'):
        pass
    else:
        assert False, 'no face dialog fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')):
        assert False, 'Tap ok fail'
    with step("[Verify] test_00092 completion"):
        assert True
