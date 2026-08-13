import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00123_main_05_11_01_5_20260805_155928")
def test_00123_main_05_11_01_5_20260805_155928(actions: DriverActions):
    with step("[Action] Tap Edit at (34.3%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 34.3, 52.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (74.6%, 31.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 74.6, 31.0)
    with step("[Action] Tap _AT at (7.9%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (26.2%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 26.2, 53.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (33.3%, 24.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 33.3, 24.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_addimg_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', direction='left', offset_start=(0.649, 0.412), offset_end=(0.172, 0.412), velocity=369)
    with step("[Action] Tap btn_addimg_n at (75.8%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', 75.8, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap photoCell-0 at (16.2%, 56.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 16.2, 56.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Pinch imageView scale=3.206"):
        actions.pinch(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'imageView'), scale=3.206, velocity=3.771)
    with step("[Action] Rotate imageView 50.9°"):
        actions.rotate(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'imageView'), rotation=50.9)
    with step("[Action] Tap maskButton at (30.0%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'maskButton', 30.0, 55.0)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage (45.1%,15.6%) → //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1] (47.0%,80.1%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', 45.1, 15.6, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]', 47.0, 80.1, duration=1.0)
    with step("[Verify] Capture '00123_main_05_11_01_5_Step13' for GT comparison"):
        actions.capture_for_gt('00123_main_05_11_01_5_Step13', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap btt_brush_n at (50.0%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 50.0, 67.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="menuView"]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther (13.3%,43.2%) → //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage (75.6%,46.7%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther', 13.3, 43.2, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', 75.6, 46.7, duration=1.0)
    with step("[Verify] Capture '00123_main_05_11_01_5_Step16' for GT comparison"):
        actions.capture_for_gt('00123_main_05_11_01_5_Step16', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (77.6%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 44.9)
    with step("[Verify] Capture '00123_main_05_11_01_5_Step18' for GT comparison"):
        actions.capture_for_gt('00123_main_05_11_01_5_Step18', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Scroll until lblText"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="lblText" and @label="Frame"]', direction='left', offset_start=(0.823, 0.282), offset_end=(0.34, 0.282), velocity=387)
    with step("[Action] Tap lblText at (63.5%, 72.7%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="lblText" and @label="Frame"]', 63.5, 72.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap Simple Frames at (47.5%, 64.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Simple Frames', 47.5, 64.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap 01 at (49.2%, 92.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '01', 49.2, 92.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap btn_ok_n at (75.5%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 46.9)
    with step("[Verify] Capture '00123_main_05_11_01_5_Step24' for GT comparison"):
        actions.capture_for_gt('00123_main_05_11_01_5_Step24', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap btnDelete at (74.1%, 51.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDelete', 74.1, 51.9)
    with step("[Verify] Capture '00123_main_05_11_01_5_Step26' for GT comparison"):
        actions.capture_for_gt('00123_main_05_11_01_5_Step26', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (54.0%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 54.0, 40.8)
    with step("[Verify] Capture '00123_main_05_11_01_5_Step28' for GT comparison"):
        actions.capture_for_gt('00123_main_05_11_01_5_Step28', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_redo at (62.0%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 62.0, 38.8)
    with step("[Verify] Capture '00123_main_05_11_01_5_Step30' for GT comparison"):
        actions.capture_for_gt('00123_main_05_11_01_5_Step30', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (34.0%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 34.0, 26.5)
    with step("[Action] Tap imageView at (49.5%, 55.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 49.5, 55.4)
    with step("[Action] Tap maskButton at (62.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'maskButton', 62.5, 50.0)
    with step("[Action] Drag cpSlider (46.8%,54.8%) → sliderArea (3.3%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 46.8, 54.8, AppiumBy.ACCESSIBILITY_ID, 'sliderArea', 3.3, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '8'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '8')
    with step("[Action] Drag cpSlider (5.3%,59.5%) → sliderArea (78.1%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.3, 59.5, AppiumBy.ACCESSIBILITY_ID, 'sliderArea', 78.1, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap btt_eraser_n at (60.0%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Eraser', 60.0, 70.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="menuView"]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther (48.3%,4.3%) → //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage (50.1%,82.4%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther', 48.3, 4.3, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', 50.1, 82.4, duration=1.0)
    with step("[Verify] Capture '00123_main_05_11_01_5_Step40' for GT comparison"):
        actions.capture_for_gt('00123_main_05_11_01_5_Step40', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (63.3%, 63.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 63.3, 63.3)
    with step("[Verify] Capture '00123_main_05_11_01_5_Step42' for GT comparison"):
        actions.capture_for_gt('00123_main_05_11_01_5_Step42', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_redo at (61.2%, 61.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 61.2, 61.2)
    with step("[Verify] Capture '00123_main_05_11_01_5_Step44' for GT comparison"):
        actions.capture_for_gt('00123_main_05_11_01_5_Step44', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (18.4%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 18.4, 32.7)
    with step("[Action] Tap btn_cancel_n at (36.7%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 36.7, 44.9)
    with step("[Action] Tap homeButton at (65.4%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 73.1)
    with step("[Action] Tap Discard at (55.1%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 55.1, 58.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
