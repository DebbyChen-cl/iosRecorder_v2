import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00093_main_05_07_22_20260805_114338")
def test_00093_main_05_07_22_20260805_114338(actions: DriverActions):
    with step("[Action] Tap Edit at (25.7%, 32.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 25.7, 32.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (77.2%, 21.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 77.2, 21.4)
    with step("[Action] Tap _AT at (7.2%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.2, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (33.1%, 74.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 33.1, 74.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (67.6%, 64.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 67.6, 64.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (42.4%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 42.4, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_conceal_portrait at (33.3%, 87.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 33.3, 87.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_double_chin at (58.8%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_double_chin', 58.8, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (51.8%,47.6%) → slider (2.8%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 51.8, 47.6, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.8, 56.1, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00093_main_05_07_22_Step12' for GT comparison"):
        actions.capture_for_gt('00093_main_05_07_22_Step12', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.7%,54.8%) → //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4] (82.6%,46.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.7, 54.8, AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]', 82.6, 46.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00093_main_05_07_22_Step15' for GT comparison"):
        actions.capture_for_gt('00093_main_05_07_22_Step15', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_undo at (65.3%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 65.3, 44.9)
    with step("[Verify] Capture '00093_main_05_07_22_Step17' for GT comparison"):
        actions.capture_for_gt('00093_main_05_07_22_Step17', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_redo at (81.6%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 81.6, 55.1)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00093_main_05_07_22_Step20' for GT comparison"):
        actions.capture_for_gt('00093_main_05_07_22_Step20', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (91.8%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 91.8, 55.1)
    with step("[Action] Tap btnClose at (64.5%, 77.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 64.5, 77.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (22.4%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 22.4, 32.7)
    with step("[Action] Tap btn_cancel_n at (42.9%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 42.9, 34.7)
    with step("[Action] Tap homeButton at (73.1%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 73.1, 57.7)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
