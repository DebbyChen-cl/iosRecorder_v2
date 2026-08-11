import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00068_main_05_07_06_1_20260805_100025")
def test_00068_main_05_07_06_1_20260805_100025(actions: DriverActions):
    with step("[Action] Tap Edit at (62.9%, 12.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 62.9, 12.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (77.7%, 40.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 77.7, 40.5)
    with step("[Action] Tap _AT at (7.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.5, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-3 at (43.8%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3', 43.8, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (58.1%, 37.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 58.1, 37.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (45.5%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 45.5, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Scroll until ic_teeth_whiten_portrait"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'photoEditFeatureCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_teeth_whiten_portrait', direction='left', offset_start=(0.628, 0.361), offset_end=(0.163, 0.361), velocity=236)
    with step("[Action] Tap ic_teeth_whiten_portrait at (41.2%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_teeth_whiten_portrait', 41.2, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Verify] Capture '00068_main_05_07_06_1_Step10' for GT comparison"):
        actions.capture_for_gt('00068_main_05_07_06_1_Step10', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (49.9%,57.1%) → slider (0.8%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 49.9, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 0.8, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00068_main_05_07_06_1_Step13' for GT comparison"):
        actions.capture_for_gt('00068_main_05_07_06_1_Step13', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.4%,45.2%) → slider (98.6%,63.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.4, 45.2, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.6, 63.4, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00068_main_05_07_06_1_Step16' for GT comparison"):
        actions.capture_for_gt('00068_main_05_07_06_1_Step16', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_undo at (65.3%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 65.3, 55.1)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00068_main_05_07_06_1_Step19' for GT comparison"):
        actions.capture_for_gt('00068_main_05_07_06_1_Step19', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_redo at (44.9%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 44.9, 38.8)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00068_main_05_07_06_1_Step22' for GT comparison"):
        actions.capture_for_gt('00068_main_05_07_06_1_Step22', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (67.3%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 67.3, 32.7)
    with step("[Action] Tap btnClose at (61.3%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 61.3, 67.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (34.7%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 34.7, 32.7)
    with step("[Action] Tap btn_cancel_n at (44.9%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 44.9, 34.7)
    with step("[Action] Tap homeButton at (65.4%, 88.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 88.5)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
