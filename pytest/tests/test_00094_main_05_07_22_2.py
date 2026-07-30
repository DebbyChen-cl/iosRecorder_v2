import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00094_main_05_07_22_2')
def test_00094_main_05_07_22_2(actions: DriverActions):
    """double chin no face"""
    mode = 1
    uuid = ['0a591584-556e-48d5-8754-6e754c97663d', '2688db32-f315-4792-97be-765c93a16391', 'de5a6713-a61d-4960-8162-08af28ff1933', '31445a6e-e4c1-4f08-9a0f-a9978d498ac3', '7723876f-05b5-4cc5-9154-e0e0e22a578b', 'fc132242-3135-4f95-836d-ac158edb86fb']
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
    with step('[Verify] snapshot: 05_07_22_before_jawline2.png'):
        actions.capture_for_gt('05_07_22_before_jawline2.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Double Chin')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Please choose another photo'):
        pass
    else:
        assert False, 'no face dialog fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')):
        assert False, 'Tap ok fail'
    with step("[Verify] test_00094 completion"):
        assert True
