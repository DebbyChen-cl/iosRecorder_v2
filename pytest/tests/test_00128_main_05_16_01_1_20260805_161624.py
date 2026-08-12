import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00128_main_05_16_01_1_20260805_161624")
def test_00128_main_05_16_01_1_20260805_161624(actions: DriverActions):
    with step("[Action] Tap Edit at (57.1%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 57.1, 44.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (76.1%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 76.1, 66.7)
    with step("[Action] Tap _AT at (7.9%, 86.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 86.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (43.8%, 79.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 43.8, 79.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (64.8%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 64.8, 46.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_live_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', direction='left', offset_start=(0.642, 0.351), offset_end=(0.133, 0.351), velocity=352)
    with step("[Action] Tap btn_live_n at (32.4%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', 32.4, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_ellements_n at (51.2%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n', 51.2, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap blackBackgroundView at (40.7%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 40.7, 75.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="animated_elements"]/XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeCollectionView[2]', container_w=422, container_h=185)
    with step("[Verify] Capture '00128_main_05_16_01_1_Step10' for GT comparison"):
        actions.capture_for_gt('00128_main_05_16_01_1_Step10', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag speedSlider (49.2%,58.0%) → blackBackgroundView (71.4%,60.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'speedSlider', 49.2, 58.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 71.4, 60.0, duration=1.0)
    with step("[Verify] lblSpeed text equals '2x'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblSpeed', '2x')
    with step("[Action] Drag speedSlider (94.3%,56.0%) → blackBackgroundView (3.0%,59.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'speedSlider', 94.3, 56.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 3.0, 59.5, duration=1.0)
    with step("[Verify] lblSpeed text equals '0.5x'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblSpeed', '0.5x')
    with step("[Action] Drag blackBackgroundView (49.5%,37.0%) → blackBackgroundView (49.8%,18.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 49.5, 37.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 49.8, 18.0, duration=1.0)
    with step("[Verify] Capture '00128_main_05_16_01_1_Step18' for GT comparison"):
        actions.capture_for_gt('00128_main_05_16_01_1_Step18', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (69.4%, 63.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 69.4, 63.3)
    with step("[Verify] Capture '00128_main_05_16_01_1_Step20' for GT comparison"):
        actions.capture_for_gt('00128_main_05_16_01_1_Step20', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag rotateImageView (48.1%,48.1%) → blackBackgroundView (21.2%,39.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'rotateImageView', 48.1, 48.1, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 21.2, 39.6, duration=1.0)
    with step("[Verify] Capture '00128_main_05_16_01_1_Step22' for GT comparison"):
        actions.capture_for_gt('00128_main_05_16_01_1_Step22', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnFlip at (51.9%, 77.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnFlip', 51.9, 77.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="animated_elements"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView', container_w=430, container_h=524)
    with step("[Verify] Capture '00128_main_05_16_01_1_Step24' for GT comparison"):
        actions.capture_for_gt('00128_main_05_16_01_1_Step24', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnDelete at (66.7%, 70.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDelete', 66.7, 70.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="animated_elements"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView', container_w=430, container_h=524)
    with step("[Action] Tap blackBackgroundView at (15.6%, 75.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 15.6, 75.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="animated_elements"]/XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeCollectionView[2]', container_w=422, container_h=185)
    with step("[Action] Tap btnPlay at (55.0%, 53.7%)"):
        actions.tap_within_element(AppiumBy.IOS_PREDICATE, "name == 'btnPlay' AND visible == 1", 55.0, 53.7)
    with step("[Action] Tap blackBackgroundView at (40.5%, 76.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 40.5, 76.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="animated_elements"]/XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeCollectionView[2]', container_w=422, container_h=185)
    with step("[Action] Tap btnPlay at (62.5%, 61.0%)"):
        actions.tap_within_element(AppiumBy.IOS_PREDICATE, "name == 'btnPlay' AND visible == 1", 55.0, 53.7)
    with step("[Verify] Capture '00128_main_05_16_01_1_Step30' for GT comparison"):
        actions.capture_for_gt('00128_main_05_16_01_1_Step30', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ID, 'btn_ok_n')
    with step("[Action] Tap Still Image at (57.4%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Still Image', 57.4, 70.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="animated_elements"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView', container_w=430, container_h=524)
    with step("[Action] Tap homeButton at (65.4%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 42.3)
    with step("[Action] Tap Discard at (60.9%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 60.9, 58.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
