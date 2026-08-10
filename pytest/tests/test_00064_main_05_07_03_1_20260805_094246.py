import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00064_main_05_07_03_1_20260805_094246")
def test_00064_main_05_07_03_1_20260805_094246(actions: DriverActions):
    with step("[Action] Tap Edit at (48.6%, 36.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 48.6, 36.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (84.3%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 84.3, 54.8)
    with step("[Action] Tap _AT at (6.1%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 6.1, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (39.2%, 63.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 39.2, 63.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (51.4%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 51.4, 51.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (69.7%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 69.7, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_skin_smooth at (60.6%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_skin_smooth', 60.6, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Auto at (56.8%, 54.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Auto', 56.8, 54.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=110, container_h=46)
    with step("[Verify] intensityValueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'intensityValueLabel', '50')
    with step("[Verify] Capture '00064_main_05_07_03_1_Step10' for GT comparison"):
        actions.capture_for_gt('00064_main_05_07_03_1_Step10', AppiumBy.ACCESSIBILITY_ID, 'middleArea', threshold=0.95)
    with step("[Action] Drag intensityCPSlider (50.4%,55.4%) → controlArea (4.9%,51.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'intensityCPSlider', 50.4, 55.4, AppiumBy.ACCESSIBILITY_ID, 'controlArea', 4.9, 51.6, duration=1.0)
    with step("[Verify] Capture '00064_main_05_07_03_1_Step12' for GT comparison"):
        actions.capture_for_gt('00064_main_05_07_03_1_Step12', AppiumBy.ACCESSIBILITY_ID, 'middleArea', threshold=0.95)
    with step("[Verify] intensityValueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'intensityValueLabel', '1')
    with step("[Action] Drag intensityCPSlider (6.6%,49.2%) → controlArea (83.7%,54.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'intensityCPSlider', 6.6, 49.2, AppiumBy.ACCESSIBILITY_ID, 'controlArea', 83.7, 54.7, duration=1.0)
    with step("[Verify] Capture '00064_main_05_07_03_1_Step15' for GT comparison"):
        actions.capture_for_gt('00064_main_05_07_03_1_Step15', AppiumBy.ACCESSIBILITY_ID, 'middleArea', threshold=0.95)
    with step("[Verify] intensityValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'intensityValueLabel', '100')
    with step("[Action] Tap ic_undo at (65.3%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 65.3, 38.8)
    with step("[Verify] Capture '00064_main_05_07_03_1_Step18' for GT comparison"):
        actions.capture_for_gt('00064_main_05_07_03_1_Step18', AppiumBy.ACCESSIBILITY_ID, 'middleArea', threshold=0.95)
    with step("[Action] Tap ic_redo at (79.6%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 79.6, 38.8)
    with step("[Verify] Capture '00064_main_05_07_03_1_Step20' for GT comparison"):
        actions.capture_for_gt('00064_main_05_07_03_1_Step20', AppiumBy.ACCESSIBILITY_ID, 'middleArea', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (32.7%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 32.7, 30.6)
    with step("[Verify] Capture '00064_main_05_07_03_1_Step22' for GT comparison"):
        actions.capture_for_gt('00064_main_05_07_03_1_Step22', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_skin_smooth at (81.8%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_skin_smooth', 81.8, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Auto at (94.6%, 63.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Auto', 94.6, 63.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=110, container_h=46)
    with step("[Action] Drag intensityCPSlider (49.6%,50.8%) → controlArea (82.8%,54.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'intensityCPSlider', 49.6, 50.8, AppiumBy.ACCESSIBILITY_ID, 'controlArea', 82.8, 54.7, duration=1.0)
    with step("[Action] Tap btn_ok_n at (77.6%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 44.9)
    with step("[Action] Tap btn_ok_n at (67.3%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 67.3, 44.9)
    with step("[Action] Tap homeButton at (65.4%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 69.2)
    with step("[Action] Tap Discard at (85.5%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 85.5, 70.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
