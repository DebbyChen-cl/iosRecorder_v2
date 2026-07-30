import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00019_main_05_01_02')
def test_00019_main_05_01_02(actions: DriverActions):
    """fisheye"""
    uuid = ['0a3c6d44-d988-4981-aaad-46784271b547', 'cd862526-b397-4dd0-b036-5916b39baf0a', 'd0638d47-24ba-4859-9abf-dfb6df8f557a', '68530325-fcb7-4e29-bfa8-ac55d7b38475', '476493b8-1f2f-426e-8d80-105f2118255a']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Fisheye')):
        assert False  # legacy raise
    from_pos = (205, 453)
    destination = (205, 292)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(*from_pos, *destination)
    with step('[Action] tap_effect_area'):
        assert actions.tap_by_coordinates(220, 220)
    with step('[Action] adjust_fisheye_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')):
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')):
        assert False  # legacy raise
    with step("[Verify] test_00019 completion"):
        assert True
