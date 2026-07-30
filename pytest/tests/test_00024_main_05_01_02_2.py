import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00024_main_05_01_02_2')
def test_00024_main_05_01_02_2(actions: DriverActions):
    """Perspective"""
    uuid = ['30e7cb86-148e-4e0d-a2c9-7d085ae67db0', '63368d55-1b53-47f2-adde-de1dc52b4fcf', '802bd011-10ca-4b2b-9cbf-bacaef7c4552', '93df2572-7040-405d-ac84-b65e28617ce7', '72d27453-4f57-4947-9571-b2e0917e00f0', 'efbdf89f-e88e-49c9-b082-78e332f223fd', '1cddcf74-e0f6-41fd-8ea4-e754332b862f']
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Perspective')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')):
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')):
        assert False  # legacy raise
    actions.capture_for_gt('base_05_01_02_perspectiveV-100.png', crop_rect=(0, 60, 276, 429))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')):
        assert False  # legacy raise
    actions.capture_for_gt('base_05_01_02_perspectiveV100.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Horizontal')):
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')):
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')):
        assert False  # legacy raise
    actions.capture_for_gt('base_05_01_02_perspectiveH-100.png', crop_rect=(0, 60, 276, 429))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')):
        assert False  # legacy raise
    actions.capture_for_gt('base_05_01_02_perspectiveH100.png', crop_rect=(0, 60, 276, 429))
    with step("[Verify] test_00024 completion"):
        assert True
