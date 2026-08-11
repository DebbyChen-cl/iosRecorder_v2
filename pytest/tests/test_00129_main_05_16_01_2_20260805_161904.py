import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00129_main_05_16_01_2_20260805_161904")
def test_00129_main_05_16_01_2_20260805_161904(actions: DriverActions):
    with step("[Action] Tap Edit at (37.1%, 32.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 37.1, 32.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (70.6%, 38.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 70.6, 38.1)
    with step("[Action] Tap _AT at (7.9%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (20.0%, 75.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 20.0, 75.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (50.7%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 50.7, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_live_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', direction='left', offset_start=(0.805, 0.423), offset_end=(0.035, 0.423), velocity=500)
    with step("[Action] Tap btn_live_n at (66.7%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', 66.7, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_live_wraparound_n at (46.3%, 42.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_wraparound_n', 46.3, 42.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap blackBackgroundView at (21.9%, 86.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 21.9, 86.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="wraparound"]/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView', container_w=375, container_h=97)
    with step("[Verify] Capture '00129_main_05_16_01_2_Step10' for GT comparison"):
        actions.capture_for_gt('00129_main_05_16_01_2_Step10', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.94)
    with step("[Action] Drag speedSlider (48.9%,60.0%) → blackBackgroundView (72.1%,77.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'speedSlider', 48.9, 60.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 72.1, 77.8, duration=1.0)
    with step("[Verify] lblSpeed text equals '2x'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblSpeed', '2x')
    with step("[Action] Drag speedSlider (94.3%,52.0%) → blackBackgroundView (4.7%,77.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'speedSlider', 94.3, 52.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 4.7, 77.9, duration=1.0)
    with step("[Verify] lblSpeed text equals '0.5x'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblSpeed', '0.5x')
    with step("[Action] Tap btnPlay at (47.5%, 51.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 47.5, 51.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="wraparound"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView', container_w=430, container_h=689)
    with step("[Action] Tap blackBackgroundView at (39.5%, 85.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 39.5, 85.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="wraparound"]/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView', container_w=375, container_h=97)
    with step("[Verify] Capture '00129_main_05_16_01_2_Step17' for GT comparison"):
        actions.capture_for_gt('00129_main_05_16_01_2_Step17', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.94)
    with step("[Action] Drag blackBackgroundView (47.4%,58.2%) → blackBackgroundView (44.4%,37.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 47.4, 58.2, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 44.4, 37.4, duration=1.0)
    with step("[Verify] Capture '00129_main_05_16_01_2_Step19' for GT comparison"):
        actions.capture_for_gt('00129_main_05_16_01_2_Step19', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.94)
    with step("[Action] Rotate blackBackgroundView 89.4°"):
        actions.rotate(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView'), rotation=89.4)
    with step("[Verify] Capture '00129_main_05_16_01_2_Step21' for GT comparison"):
        actions.capture_for_gt('00129_main_05_16_01_2_Step21', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.94)
    with step("[Action] Tap btnFlip at (51.9%, 81.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnFlip', 51.9, 81.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="wraparound"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView', container_w=430, container_h=689)
    with step("[Verify] Capture '00129_main_05_16_01_2_Step23' for GT comparison"):
        actions.capture_for_gt('00129_main_05_16_01_2_Step23', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.94)
    with step("[Action] Tap btnDelete at (44.4%, 63.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDelete', 44.4, 63.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="wraparound"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView', container_w=430, container_h=689)
    with step("[Verify] Capture '00129_main_05_16_01_2_Step25' for GT comparison"):
        actions.capture_for_gt('00129_main_05_16_01_2_Step25', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.94)
    with step("[Action] Tap btn_ok_n at (85.7%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 85.7, 44.9)
    with step("[Action] Tap homeButton at (61.5%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 73.1)
    with step("[Action] Tap Discard at (69.6%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 69.6, 66.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.94)
    assert True
