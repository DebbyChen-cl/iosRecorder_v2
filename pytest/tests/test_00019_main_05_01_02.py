import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00019_main_05_01_02')
def test_00019_main_05_01_02(actions: DriverActions):
    """fisheye"""
    uuid = ['0a3c6d44-d988-4981-aaad-46784271b547', 'cd862526-b397-4dd0-b036-5916b39baf0a', 'd0638d47-24ba-4859-9abf-dfb6df8f557a', '68530325-fcb7-4e29-bfa8-ac55d7b38475', '476493b8-1f2f-426e-8d80-105f2118255a']

    with step("[Action] Tap Edit at (25.7%, 68.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 25.7, 68.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (82.7%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 82.7, 47.6)
    with step("[Action] Tap _AT at (8.2%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.2, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (62.3%, 49.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 62.3, 49.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (25.4%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 25.4, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap btn_fisheye_s at (60.6%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_fisheye_s', 60.6, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"DistortionViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther (31.4%,40.6%) → PhotoDirector (66.3%,53.4%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="DistortionViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther', 31.4, 40.6, AppiumBy.ACCESSIBILITY_ID, 'PhotoDirector', 66.3, 53.4, duration=1.0)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"DistortionViewController\"]/XCUIElementTypeOther[1] at (50.7%, 50.2%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="DistortionViewController"]/XCUIElementTypeOther[1]', 50.7, 50.2)
    with step("[Action] Drag centerSlider (50.2%,61.0%) → slider (96.8%,65.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.2, 61.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 96.8, 65.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture 'fisheye_Step11' for GT comparison"):
        actions.capture_for_gt('fisheye_Step11', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="DistortionViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag centerSlider (93.8%,53.7%) → slider (1.9%,52.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 93.8, 53.7, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.9, 52.5, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture 'fisheye_Step14' for GT comparison"):
        actions.capture_for_gt('fisheye_Step14', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="DistortionViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
        
    with step("[Verify] test_00019 completion"):
        assert True
