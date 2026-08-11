import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00074_main_05_07_10_1_20260805_103130")
def test_00074_main_05_07_10_1_20260805_103130(actions: DriverActions):
    with step("[Action] Tap Edit at (22.9%, 76.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 22.9, 76.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (90.4%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 90.4, 47.6)
    with step("[Action] Tap _AT at (7.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.2, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (43.8%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 43.8, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (59.5%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 59.5, 46.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (45.5%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 45.5, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_conceal_portrait at (63.6%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 63.6, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_oilness at (55.9%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_oilness', 55.9, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Verify] Capture '00074_main_05_07_10_1_Step10' for GT comparison"):
        actions.capture_for_gt('00074_main_05_07_10_1_Step10', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (51.0%,45.2%) → slider (3.4%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 51.0, 45.2, AppiumBy.ACCESSIBILITY_ID, 'slider', 3.4, 56.1, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00074_main_05_07_10_1_Step13' for GT comparison"):
        actions.capture_for_gt('00074_main_05_07_10_1_Step13', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (7.0%,54.8%) → slider (97.5%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.0, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 97.5, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00074_main_05_07_10_1_Step16' for GT comparison"):
        actions.capture_for_gt('00074_main_05_07_10_1_Step16', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_undo at (79.6%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 79.6, 34.7)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00074_main_05_07_10_1_Step19' for GT comparison"):
        actions.capture_for_gt('00074_main_05_07_10_1_Step19', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_redo at (75.5%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 75.5, 44.9)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00074_main_05_07_10_1_Step22' for GT comparison"):
        actions.capture_for_gt('00074_main_05_07_10_1_Step22', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (71.4%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 71.4, 46.9)
    with step("[Action] Tap btnClose at (61.3%, 74.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 61.3, 74.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (24.5%, 16.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 24.5, 16.3)
    with step("[Action] Tap btn_cancel_n at (46.9%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 46.9, 38.8)
    with step("[Action] Tap homeButton at (76.9%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 76.9, 57.7)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
