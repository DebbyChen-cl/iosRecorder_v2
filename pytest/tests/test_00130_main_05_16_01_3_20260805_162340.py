import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00130_main_05_16_01_3_20260805_162340")
def test_00130_main_05_16_01_3_20260805_162340(actions: DriverActions):
    with step("[Action] Tap Edit at (65.7%, 72.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 65.7, 72.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (70.1%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 70.1, 54.8)
    with step("[Action] Tap _AT at (8.2%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.2, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (34.6%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 34.6, 59.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (47.9%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 47.9, 51.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_live_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', direction='left', offset_start=(0.807, 0.381), offset_end=(0.205, 0.381), velocity=569)
    with step("[Action] Tap btn_live_n at (54.5%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', 54.5, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_live_overlay_n at (63.4%, 77.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_overlay_n', 63.4, 77.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap blackBackgroundView at (37.9%, 86.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 37.9, 86.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="panelView"]/XCUIElementTypeCollectionView', container_w=381, container_h=97)
    with step("[Action] Drag speedSlider (50.6%,50.0%) → sliderBackgroundView (77.4%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'speedSlider', 50.6, 50.0, AppiumBy.ACCESSIBILITY_ID, 'sliderBackgroundView', 77.4, 55.1, duration=1.0)
    with step("[Verify] lblSpeed text equals '2x'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblSpeed', '2x')
    with step("[Action] Drag speedSlider (96.3%,56.0%) → sliderBackgroundView (17.4%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'speedSlider', 96.3, 56.0, AppiumBy.ACCESSIBILITY_ID, 'sliderBackgroundView', 17.4, 49.0, duration=1.0)
    with step("[Verify] lblSpeed text equals '0.5x'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblSpeed', '0.5x')
    with step("[Action] Tap blackBackgroundView at (57.2%, 86.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 57.2, 86.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="panelView"]/XCUIElementTypeCollectionView', container_w=381, container_h=97)
    with step("[Action] Tap btnMaskSwitch at (55.0%, 48.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch', 55.0, 48.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=689)
    with step("[Action] Drag blackBackgroundView (21.4%,16.7%) → blackBackgroundView (75.6%,68.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 21.4, 16.7, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 75.6, 68.6, duration=1.0)
    with step("[Verify] Capture '00130_main_05_16_01_3_Step17' for GT comparison"):
        actions.capture_for_gt('00130_main_05_16_01_3_Step17', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (79.6%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 79.6, 40.8)
    with step("[Verify] Capture '00130_main_05_16_01_3_Step19' for GT comparison"):
        actions.capture_for_gt('00130_main_05_16_01_3_Step19', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_redo at (61.2%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 61.2, 34.7)
    with step("[Verify] Capture '00130_main_05_16_01_3_Step21' for GT comparison"):
        actions.capture_for_gt('00130_main_05_16_01_3_Step21', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnBrush at (67.5%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBrush', 67.5, 58.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=689)
    with step("[Action] Drag blackBackgroundView (31.9%,27.3%) → blackBackgroundView (62.6%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 31.9, 27.3, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 62.6, 56.1, duration=1.0)
    with step("[Verify] Capture '00130_main_05_16_01_3_Step24' for GT comparison"):
        actions.capture_for_gt('00130_main_05_16_01_3_Step24', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (24.0%,64.3%) → sliderBackgroundView (74.0%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 24.0, 64.3, AppiumBy.ACCESSIBILITY_ID, 'sliderBackgroundView', 74.0, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag blackBackgroundView (17.2%,16.4%) → blackBackgroundView (56.7%,66.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 17.2, 16.4, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 56.7, 66.8, duration=1.0)
    with step("[Verify] Capture '00130_main_05_16_01_3_Step28' for GT comparison"):
        actions.capture_for_gt('00130_main_05_16_01_3_Step28', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnMaskSwitch at (55.0%, 39.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch', 55.0, 39.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=689)
    with step("[Action] Tap btnBack at (45.0%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 45.0, 58.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap btn_live_wraparound_n at (36.6%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_wraparound_n', 36.6, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap btn_ok_n at (91.8%, 20.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 91.8, 20.4)
    with step("[Action] Tap btnClose at (67.7%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 67.7, 48.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (38.8%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 38.8, 40.8)
    with step("[Action] Tap Discard at (84.5%, 87.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 84.5, 87.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="wraparound"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView', container_w=430, container_h=689)
    with step("[Action] Tap homeButton at (61.5%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 46.2)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
