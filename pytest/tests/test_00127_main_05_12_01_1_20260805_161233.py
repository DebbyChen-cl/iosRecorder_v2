import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00127_main_05_12_01_1_20260805_161233")
def test_00127_main_05_12_01_1_20260805_161233(actions: DriverActions):
    with step("[Action] Tap Edit at (51.4%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 51.4, 44.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (77.7%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 77.7, 61.9)
    with step("[Action] Tap _AT at (11.5%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 11.5, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (38.5%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 38.5, 69.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (71.1%, 37.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 71.1, 37.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_frame_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_frame_n', direction='left', offset_start=(0.752, 0.474), offset_end=(0.114, 0.474), velocity=425)
    with step("[Action] Tap btn_frame_n at (51.5%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_frame_n', 51.5, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn effect store n at (49.2%, 44.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn effect store n', 49.2, 44.3)
    with step("[Action] Tap New at (37.5%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'New', 37.5, 75.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="WebStoreViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeWebView', container_w=430, container_h=873)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"WebStoreViewController\"]/XCUIElementTypeOther[2] at (15.8%, 24.7%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="WebStoreViewController"]/XCUIElementTypeOther[2]', 15.8, 24.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="WebStoreViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeWebView', container_w=430, container_h=873)
    with step("[Action] Tap Download at (44.8%, 43.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Download', 44.8, 43.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="WebStoreViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeWebView', container_w=430, container_h=873)
    with step("[Action] Tap Use at (56.0%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Use', 56.0, 53.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="WebStoreViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeWebView', container_w=430, container_h=873)
    with step("[Verify] Capture '00127_main_05_12_01_1_Step13' for GT comparison"):
        actions.capture_for_gt('00127_main_05_12_01_1_Step13', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="EditFrameViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (77.6%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 40.8)
    with step("[Verify] Capture '00127_main_05_12_01_1_Step15' for GT comparison"):
        actions.capture_for_gt('00127_main_05_12_01_1_Step15', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (57.7%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 57.7, 42.3)
    with step("[Action] Tap Discard at (84.1%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 84.1, 75.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
