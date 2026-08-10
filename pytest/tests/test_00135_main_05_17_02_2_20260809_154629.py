import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00135_main_05_17_02_2_20260810_115520")
def test_00135_main_05_17_02_2_20260810_115520(actions: DriverActions):
    with step("[Action] Tap Edit at (77.1%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 77.1, 56.0)
    with step("[Action] Tap btnAlbum at (68.0%, 45.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 68.0, 45.2)
    with step("[Action] Tap _AT at (10.4%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.4, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (34.6%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 34.6, 65.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (45.1%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 45.1, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Live"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Live', direction='left', offset_start=(0.867, 0.412), offset_end=(0.24, 0.412), velocity=778)
    with step("[Action] Tap Live at (50.7%, 31.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Live', 50.7, 31.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Scroll until blackBackgroundView"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', direction='left', offset_start=(0.793, 0.351), offset_end=(0.163, 0.351), velocity=528)
    with step("[Action] Tap Sparkle at (54.3%, 20.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sparkle', 54.3, 20.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap Manual add at (59.3%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Manual add', 59.3, 50.0)
    with step("[Action] Tap blackBackgroundView at (42.3%, 86.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 42.3, 86.3)
    with step("[Verify] Capture '00135_main_05_17_02_2_Step12' for GT comparison"):
        actions.capture_for_gt('00135_main_05_17_02_2_Step12', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap blackBackgroundView at (25.6%, 27.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 25.6, 27.3)
    with step("[Action] Tap blackBackgroundView at (26.0%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 26.0, 54.5)
    with step("[Action] Tap blackBackgroundView at (75.1%, 42.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 75.1, 42.5)
    with step("[Action] Tap blackBackgroundView at (77.4%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 77.4, 52.0)
    with step("[Verify] Capture '00135_main_05_17_02_2_Step17' for GT comparison"):
        actions.capture_for_gt('00135_main_05_17_02_2_Step17', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (27.5%,65.9%) → blackBackgroundView (17.0%,74.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 27.5, 65.9, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 17.0, 74.4, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00135_main_05_17_02_2_Step20' for GT comparison"):
        actions.capture_for_gt('00135_main_05_17_02_2_Step20', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (7.0%,46.3%) → blackBackgroundView (71.2%,74.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.0, 46.3, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 71.2, 74.4, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00135_main_05_17_02_2_Step23' for GT comparison"):
        actions.capture_for_gt('00135_main_05_17_02_2_Step23', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnPlay at (57.5%, 37.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 57.5, 37.5)
    with step("[Verify] Capture '00135_main_05_17_02_2_Step25' for GT comparison"):
        actions.capture_for_gt('00135_main_05_17_02_2_Step25', AppiumBy.ACCESSIBILITY_ID, 'btnPlay', threshold=0.95)
    with step("[Action] Tap btnPlay at (70.0%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 70.0, 47.5)
    with step("[Verify] Capture '00135_main_05_17_02_2_Step27' for GT comparison"):
        actions.capture_for_gt('00135_main_05_17_02_2_Step27', AppiumBy.ACCESSIBILITY_ID, 'btnPlay', threshold=0.95)
    with step("[Action] Tap imageViewAdj at (28.0%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageViewAdj', 28.0, 44.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='sparkleSelectionViewSparklesCollectionView', container_w=359, container_h=77)
    with step("[Action] Tap Intensity at (46.0%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Intensity', 46.0, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=123)
    with step("[Action] Drag cpSlider (51.0%,51.2%) → blackBackgroundView (15.3%,74.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 51.0, 51.2, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 15.3, 74.1, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00135_main_05_17_02_2_Step32' for GT comparison"):
        actions.capture_for_gt('00135_main_05_17_02_2_Step32', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (6.7%,46.3%) → blackBackgroundView (72.1%,74.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.7, 46.3, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 72.1, 74.5, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00135_main_05_17_02_2_Step35' for GT comparison"):
        actions.capture_for_gt('00135_main_05_17_02_2_Step35', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap Color at (44.4%, 27.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Color', 44.4, 27.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=123)
    with step("[Verify] hueValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel', '0')
    with step("[Verify] saturationValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel', '0')
    with step("[Action] Drag hueSlider (51.8%,53.2%) → blackBackgroundView (20.0%,70.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 51.8, 53.2, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 20.0, 70.5, duration=1.0)
    with step("[Verify] hueValueLabel text equals '-180'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel', '-180')
    with step("[Verify] Capture '00135_main_05_17_02_2_Step41' for GT comparison"):
        actions.capture_for_gt('00135_main_05_17_02_2_Step41', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag hueSlider (6.6%,46.8%) → blackBackgroundView (81.6%,70.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 6.6, 46.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 81.6, 70.0, duration=1.0)
    with step("[Verify] hueValueLabel text equals '180'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel', '180')
    with step("[Verify] Capture '00135_main_05_17_02_2_Step44' for GT comparison"):
        actions.capture_for_gt('00135_main_05_17_02_2_Step44', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag saturationSlider (52.2%,63.8%) → blackBackgroundView (21.2%,75.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 52.2, 63.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 21.2, 75.5, duration=1.0)
    with step("[Verify] saturationValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel', '-100')
    with step("[Verify] Capture '00135_main_05_17_02_2_Step47' for GT comparison"):
        actions.capture_for_gt('00135_main_05_17_02_2_Step47', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag saturationSlider (7.0%,63.8%) → blackBackgroundView (79.8%,75.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 7.0, 63.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 79.8, 75.4, duration=1.0)
    with step("[Verify] saturationValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel', '100')
    with step("[Verify] Capture '00135_main_05_17_02_2_Step50' for GT comparison"):
        actions.capture_for_gt('00135_main_05_17_02_2_Step50', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (69.4%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 69.4, 57.1)
    with step("[Action] Tap Still Image at (61.7%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Still Image', 61.7, 83.3)
    with step("[Verify] Capture '00135_main_05_17_02_2_Step53' for GT comparison"):
        actions.capture_for_gt('00135_main_05_17_02_2_Step53', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (80.8%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 80.8, 53.8)
    with step("[Action] Tap Discard at (78.3%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 78.3, 58.3)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
