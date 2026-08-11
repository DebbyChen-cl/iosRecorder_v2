import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00107_main_06_01_01_n_20260808_205931")
def test_00107_main_06_01_01_n_20260808_205931(actions: DriverActions):
    with step("[Action] Tap Edit at (54.3%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 54.3, 44.0)
    with step("[Action] Tap btnAlbum at (70.6%, 38.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 70.6, 38.1)
    with step("[Action] Tap _AT at (10.4%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.4, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (49.2%, 56.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 49.2, 56.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (62.2%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 62.2, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Text"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Text', direction='left', offset_start=(0.428, 0.443), offset_end=(0.326, 0.443), velocity=79)
    with step("[Action] Tap Text at (50.0%, 15.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text', 50.0, 15.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Text Bubble at (44.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text Bubble', 44.2, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step09' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step09', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Drag imageView (51.4%,50.1%) → backgroundView (50.0%,60.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'imageView', 51.4, 50.1, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 50.0, 60.1, duration=1.0)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step11' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step11', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (52.0%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 52.0, 57.1)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step13' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step13', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_redo at (66.0%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 66.0, 34.7)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step15' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step15', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (56.0%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 56.0, 46.9)
    with step("[Action] Drag imageView (66.7%,61.4%) → backgroundView (76.0%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'imageView', 66.7, 61.4, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 76.0, 57.1, duration=1.0)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step18' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step18', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Rotate imageView 69.3°"):
        actions.rotate(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'imageView'), rotation=69.3)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step20' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step20', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (78.0%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 78.0, 38.8)
    with step("[Action] Tap ic_undo at (84.0%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 84.0, 38.8)
    with step("[Action] Tap btnDuplicate at (63.0%, 59.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDuplicate', 63.0, 59.3)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step24' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step24', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (72.0%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 72.0, 34.7)
    with step("[Action] Tap imageView at (50.0%, 50.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 50.0, 50.6)
    with step("[Action] Tap imageView at (49.3%, 49.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 49.3, 49.1)
    with step("[Action] Tap applyButton at (54.5%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'applyButton', 54.5, 54.5)
    with step("[Action] Tap btnDelete at (70.4%, 40.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDelete', 70.4, 40.7)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step30' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step30', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (64.0%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 64.0, 38.8)
    with step("[Action] Tap imageView at (50.2%, 49.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 50.2, 49.1)
    with step("[Action] Tap maskButton at (62.5%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'maskButton', 62.5, 30.0)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther (44.6%,3.7%) → //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage (46.8%,73.9%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther', 44.6, 3.7, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', 46.8, 73.9, duration=1.0)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step35' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step35', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (61.2%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 61.2, 46.9)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step37' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step37', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (52.0%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 52.0, 38.8)
    with step("[Action] Tap maskButton at (62.5%, 42.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'maskButton', 62.5, 42.5)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (47.1%,54.8%) → sliderArea (1.9%,40.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 47.1, 54.8, AppiumBy.ACCESSIBILITY_ID, 'sliderArea', 1.9, 40.8, duration=1.0)
    with step("[Verify] valueLabel text equals '8'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '8')
    with step("[Action] Drag cpSlider (5.3%,47.6%) → sliderArea (80.9%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.3, 47.6, AppiumBy.ACCESSIBILITY_ID, 'sliderArea', 80.9, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1] (49.3%,24.3%) → //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther (46.3%,98.6%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]', 49.3, 24.3, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther', 46.3, 98.6, duration=1.0)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step46' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step46', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btt_brush_n at (25.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 25.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="menuView"]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1] (52.3%,16.9%) → //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1] (50.9%,77.2%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]', 52.3, 16.9, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]', 50.9, 77.2, duration=1.0)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step49' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step49', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap ic_undo at (69.4%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 69.4, 42.9)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step51' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step51', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap ic_redo at (65.3%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 65.3, 57.1)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step53' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step53', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (44.9%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 44.9, 38.8)
    with step("[Verify] Capture '00107_main_06_01_01_n_Step55' for GT comparison"):
        actions.capture_for_gt('00107_main_06_01_01_n_Step55', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (65.3%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 65.3, 32.7)
    with step("[Action] Tap OK at (40.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 40.0, 50.0)
    with step("[Action] Tap homeButton at (53.8%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 53.8, 65.4)
    with step("[Action] Tap Discard at (42.0%, 79.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 42.0, 79.2)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
