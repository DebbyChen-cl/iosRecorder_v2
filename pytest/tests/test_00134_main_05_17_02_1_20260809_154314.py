import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00134_main_05_17_02_1_20260809_154314")
def test_00134_main_05_17_02_1_20260809_154314(actions: DriverActions):
    with step("[Action] Tap Edit at (25.7%, 36.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 25.7, 36.0)
    with step("[Action] Tap btnAlbum at (74.1%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 74.1, 71.4)
    with step("[Action] Tap _AT at (8.2%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.2, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (31.5%, 73.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 31.5, 73.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (46.5%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 46.5, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Live"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Live', direction='left', offset_start=(0.798, 0.381), offset_end=(0.0, 0.381), velocity=890)
    with step("[Action] Tap Live at (45.1%, 15.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Live', 45.1, 15.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Scroll until Sparkle"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'Sparkle', direction='left', offset_start=(0.637, 0.361), offset_end=(0.14, 0.361), velocity=664)
    with step("[Action] Tap Sparkle at (66.7%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sparkle', 66.7, 26.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap blackBackgroundView at (43.0%, 87.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 43.0, 87.4)
    with step("[Verify] Capture '00134_main_05_17_02_1_Step11' for GT comparison"):
        actions.capture_for_gt('00134_main_05_17_02_1_Step11', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (25.4%,56.1%) → blackBackgroundView (71.4%,74.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 25.4, 56.1, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 71.4, 74.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag cpSlider (94.7%,43.9%) → blackBackgroundView (16.7%,74.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 94.7, 43.9, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 16.7, 74.2, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Action] Tap btnPlay at (50.0%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 50.0, 57.5)
    with step("[Verify] Capture '00134_main_05_17_02_1_Step17' for GT comparison"):
        actions.capture_for_gt('00134_main_05_17_02_1_Step17', AppiumBy.ACCESSIBILITY_ID, 'btnPlay', threshold=0.95)
    with step("[Action] Tap btnPlay at (50.0%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 50.0, 45.0)
    with step("[Verify] Capture '00134_main_05_17_02_1_Step19' for GT comparison"):
        actions.capture_for_gt('00134_main_05_17_02_1_Step19', AppiumBy.ACCESSIBILITY_ID, 'btnPlay', threshold=0.95)
    with step("[Action] Tap imageViewAdj at (72.0%, 68.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageViewAdj', 72.0, 68.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='sparkleSelectionViewSparklesCollectionView', container_w=359, container_h=77)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (51.0%,51.2%) → blackBackgroundView (72.1%,74.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 51.0, 51.2, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 72.1, 74.5, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00134_main_05_17_02_1_Step24' for GT comparison"):
        actions.capture_for_gt('00134_main_05_17_02_1_Step24', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (93.7%,51.2%) → blackBackgroundView (14.7%,74.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 93.7, 51.2, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 14.7, 74.4, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00134_main_05_17_02_1_Step27' for GT comparison"):
        actions.capture_for_gt('00134_main_05_17_02_1_Step27', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap Amount at (74.6%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Amount', 74.6, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=123)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (50.6%,63.4%) → blackBackgroundView (72.8%,74.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 50.6, 63.4, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 72.8, 74.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00134_main_05_17_02_1_Step32' for GT comparison"):
        actions.capture_for_gt('00134_main_05_17_02_1_Step32', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (93.7%,61.0%) → blackBackgroundView (13.3%,74.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 93.7, 61.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 13.3, 74.0, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00134_main_05_17_02_1_Step35' for GT comparison"):
        actions.capture_for_gt('00134_main_05_17_02_1_Step35', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap Color at (39.7%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Color', 39.7, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=123)
    with step("[Verify] hueValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel', '0')
    with step("[Verify] saturationValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel', '0')
    with step("[Action] Drag hueSlider (50.7%,44.7%) → blackBackgroundView (20.0%,70.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 50.7, 44.7, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 20.0, 70.5, duration=1.0)
    with step("[Verify] hueValueLabel text equals '-180'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel', '-180')
    with step("[Verify] Capture '00134_main_05_17_02_1_Step41' for GT comparison"):
        actions.capture_for_gt('00134_main_05_17_02_1_Step41', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag hueSlider (7.4%,55.3%) → blackBackgroundView (80.9%,70.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 7.4, 55.3, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 80.9, 70.2, duration=1.0)
    with step("[Verify] hueValueLabel text equals '180'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel', '180')
    with step("[Verify] Capture '00134_main_05_17_02_1_Step44' for GT comparison"):
        actions.capture_for_gt('00134_main_05_17_02_1_Step44', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag saturationSlider (50.7%,53.2%) → blackBackgroundView (20.7%,75.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 50.7, 53.2, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 20.7, 75.1, duration=1.0)
    with step("[Verify] saturationValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel', '-100')
    with step("[Verify] Capture '00134_main_05_17_02_1_Step47' for GT comparison"):
        actions.capture_for_gt('00134_main_05_17_02_1_Step47', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag saturationSlider (7.0%,46.8%) → blackBackgroundView (82.6%,75.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 7.0, 46.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 82.6, 75.2, duration=1.0)
    with step("[Verify] saturationValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel', '100')
    with step("[Verify] Capture '00134_main_05_17_02_1_Step50' for GT comparison"):
        actions.capture_for_gt('00134_main_05_17_02_1_Step50', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (77.6%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 46.9)
    with step("[Action] Tap Still Image at (62.8%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Still Image', 62.8, 70.8)
    with step("[Verify] Capture '00134_main_05_17_02_1_Step53' for GT comparison"):
        actions.capture_for_gt('00134_main_05_17_02_1_Step53', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (88.5%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 88.5, 42.3)
    with step("[Action] Tap Discard at (73.9%, 54.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 73.9, 54.2)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
