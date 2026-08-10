import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00101_main_05_08_01_n3_20260808_202325")
def test_00101_main_05_08_01_n3_20260808_202325(actions: DriverActions):
    with step("[Action] Tap Edit at (51.4%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 51.4, 48.0)
    with step("[Action] Tap btnAlbum at (72.6%, 64.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 72.6, 64.3)
    with step("[Action] Tap _AT at (11.1%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 11.1, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (44.6%, 56.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 44.6, 56.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (53.3%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 53.3, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Text"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Text', direction='left', offset_start=(0.286, 0.495), offset_end=(0.205, 0.495), velocity=50)
    with step("[Action] Tap Text at (59.2%, 36.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text', 59.2, 36.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Text at (57.1%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text', 57.1, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap btnTextEdit at (44.4%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTextEdit', 44.4, 44.4)
    with step("[Action] Tap A at (51.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'A', 51.2, 50.0)
    with step("[Action] Tap a at (51.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'a', 51.2, 50.0)
    with step("[Action] Tap a at (51.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'a', 51.2, 50.0)
    with step("[Action] Tap Return at (54.2%, 35.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Return', 54.2, 35.7)
    with step("[Action] Tap A at (53.5%, 44.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'A', 53.5, 44.6)
    with step("[Action] Tap applyButton at (52.3%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'applyButton', 52.3, 45.5)
    with step("[Action] Tap Style at (52.8%, 47.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Style', 52.8, 47.4)
    with step("[Action] Tap Format at (59.3%, 59.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Format', 59.3, 59.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=45)
    with step("[Verify] Capture '00101_main_05_08_01_n3_Step19' for GT comparison"):
        actions.capture_for_gt('00101_main_05_08_01_n3_Step19', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag mainPanel (50.2%,3.0%) → backgroundView (50.0%,86.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'mainPanel', 50.2, 3.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 50.0, 86.3, duration=1.0)
    with step("[Verify] mainPanel is not visible"):
        actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'mainPanel')
    with step("[Action] Tap imageView at (50.7%, 50.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 50.7, 50.2)
    with step("[Action] Tap Style at (25.0%, 21.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Style', 25.0, 21.1)
    with step("[Action] Tap Format at (54.7%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Format', 54.7, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=45)
    with step("[Action] Tap alignLeftButton at (68.2%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'alignLeftButton', 68.2, 55.6)
    with step("[Verify] Capture '00101_main_05_08_01_n3_Step26' for GT comparison"):
        actions.capture_for_gt('00101_main_05_08_01_n3_Step26', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap alignCenterButton at (63.6%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'alignCenterButton', 63.6, 46.7)
    with step("[Verify] Capture '00101_main_05_08_01_n3_Step28' for GT comparison"):
        actions.capture_for_gt('00101_main_05_08_01_n3_Step28', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap alignRightButton at (45.5%, 42.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'alignRightButton', 45.5, 42.2)
    with step("[Verify] Capture '00101_main_05_08_01_n3_Step30' for GT comparison"):
        actions.capture_for_gt('00101_main_05_08_01_n3_Step30', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap alignCenterButton at (70.5%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'alignCenterButton', 70.5, 48.9)
    with step("[Action] Tap boldButton at (59.1%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'boldButton', 59.1, 62.2)
    with step("[Verify] Capture '00101_main_05_08_01_n3_Step33' for GT comparison"):
        actions.capture_for_gt('00101_main_05_08_01_n3_Step33', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap italicButton at (54.5%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'italicButton', 54.5, 48.9)
    with step("[Verify] Capture '00101_main_05_08_01_n3_Step35' for GT comparison"):
        actions.capture_for_gt('00101_main_05_08_01_n3_Step35', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"textSizeAdjustmentView\"]/XCUIElementTypeSlider (16.0%,47.4%) → backgroundView (30.7%,79.4%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="textSizeAdjustmentView"]/XCUIElementTypeSlider', 16.0, 47.4, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 30.7, 79.4, duration=1.0)
    with step("[Verify] Capture '00101_main_05_08_01_n3_Step37' for GT comparison"):
        actions.capture_for_gt('00101_main_05_08_01_n3_Step37', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"textSizeAdjustmentView\"]/XCUIElementTypeSlider (6.9%,45.6%) → backgroundView (84.0%,79.4%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="textSizeAdjustmentView"]/XCUIElementTypeSlider', 6.9, 45.6, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 84.0, 79.4, duration=1.0)
    with step("[Verify] Capture '00101_main_05_08_01_n3_Step40' for GT comparison"):
        actions.capture_for_gt('00101_main_05_08_01_n3_Step40', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Verify] valueLabel text equals '65'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '65')
    with step("[Action] Tap btn_ok_n at (75.5%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 49.0)
    with step("[Action] Tap OK at (50.0%, 29.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 50.0, 29.2)
    with step("[Action] Tap homeButton at (65.4%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 53.8)
    with step("[Action] Tap Discard at (39.1%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 39.1, 66.7)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
