import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00052_main_05_03_05_20260804_145907")
def test_00052_main_05_03_05_20260804_145907(actions: DriverActions):
    with step("[Action] Tap Edit at (45.7%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 45.7, 48.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (91.4%, 45.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 91.4, 45.2)
    with step("[Action] Tap _AT at (7.9%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (38.5%, 43.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 38.5, 43.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Enhance at (58.3%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 58.3, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Verify] Capture '00052_main_05_03_05_Step06' for GT comparison"):
        actions.capture_for_gt('00052_main_05_03_05_Step06', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Scroll until btn_dehaze"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_dehaze', direction='left', offset_start=(0.8, 0.351), offset_end=(0.342, 0.351), velocity=350)
    with step("[Action] Tap btn_dehaze at (66.7%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_dehaze', 66.7, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00052_main_05_03_05_Step09' for GT comparison"):
        actions.capture_for_gt('00052_main_05_03_05_Step09', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.DeHazeViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag cpSlider (50.6%,54.8%) → slider (1.8%,46.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 50.6, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.8, 46.3, duration=1.0)
    with step("[Verify] Capture '00052_main_05_03_05_Step11' for GT comparison"):
        actions.capture_for_gt('00052_main_05_03_05_Step11', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.DeHazeViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag cpSlider (6.4%,57.1%) → slider (97.9%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.4, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 97.9, 56.1, duration=1.0)
    with step("[Verify] Capture '00052_main_05_03_05_Step14' for GT comparison"):
        actions.capture_for_gt('00052_main_05_03_05_Step14', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.DeHazeViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap btn_cancel_n at (40.8%, 24.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 40.8, 24.5)
    with step("[Verify] Capture '00052_main_05_03_05_Step17' for GT comparison"):
        actions.capture_for_gt('00052_main_05_03_05_Step17', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_dehaze at (51.5%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_dehaze', 51.5, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_ok_n at (73.5%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 42.9)
    with step("[Verify] Capture '00052_main_05_03_05_Step20' for GT comparison"):
        actions.capture_for_gt('00052_main_05_03_05_Step20', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (61.5%, 38.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 38.5)
    with step("[Action] Tap Discard at (50.7%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 50.7, 33.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
