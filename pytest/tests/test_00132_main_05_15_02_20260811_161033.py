import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00132_main_05_15_02_20260811_161033")
def test_00132_main_05_15_02_20260811_161033(actions: DriverActions):
    with step("[Action] Tap Edit at (42.9%, 32.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 42.9, 32.0)
    with step("[Action] Tap btnAlbum at (70.6%, 26.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 70.6, 26.2)
    with step("[Action] Tap _AT at (14.3%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 14.3, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (26.9%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 26.9, 67.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (33.8%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 33.8, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Live"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Live', direction='left', offset_start=(0.8, 0.443), offset_end=(0.463, 0.443), velocity=450)
    with step("[Action] Tap Live at (53.5%, 26.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Live', 53.5, 26.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Sky at (49.3%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sky', 49.3, 26.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Scroll until Cloudy"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'skyExpandCollectionViewCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Cloudy', direction='left', offset_start=(0.652, 0.921), offset_end=(0.029, 0.921), velocity=392)
    with step("[Action] Tap Cloudy at (73.5%, 73.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cloudy', 73.5, 73.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='skyExpandCollectionViewCollectionView', container_w=375, container_h=101)
    with step("[Action] Tap 01 at (43.9%, 42.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '01', 43.9, 42.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='skyExpandCollectionViewCollectionView', container_w=374, container_h=101)
    with step("[Verify] valueLabel text equals '30'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '30')
    with step("[Action] Drag cpSlider (37.1%,43.9%) → sliderBackgroundView (16.3%,40.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 37.1, 43.9, AppiumBy.ACCESSIBILITY_ID, 'sliderBackgroundView', 16.3, 40.8, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Action] Drag cpSlider (7.7%,61.0%) → sliderBackgroundView (72.8%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.7, 61.0, AppiumBy.ACCESSIBILITY_ID, 'sliderBackgroundView', 72.8, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag cpSlider (91.1%,56.1%) → sliderBackgroundView (13.7%,40.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 91.1, 56.1, AppiumBy.ACCESSIBILITY_ID, 'sliderBackgroundView', 13.7, 40.8, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Action] Tap imgViewSelected at (47.1%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imgViewSelected', 47.1, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='skyExpandCollectionViewCollectionView', container_w=374, container_h=101)
    with step("[Action] Tap Feather at (73.0%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Feather', 73.0, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=374, container_h=119)
    with step("[Verify] lblVal text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '0')
    with step("[Action] Drag slider (52.4%,54.0%) → sliderBackgroundView (12.1%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 52.4, 54.0, AppiumBy.ACCESSIBILITY_ID, 'sliderBackgroundView', 12.1, 55.1, duration=1.0)
    with step("[Verify] Capture '00132_main_05_15_02_Step23' for GT comparison"):
        actions.capture_for_gt('00132_main_05_15_02_Step23', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Drag slider (6.3%,46.0%) → sliderBackgroundView (73.7%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 6.3, 46.0, AppiumBy.ACCESSIBILITY_ID, 'sliderBackgroundView', 73.7, 51.0, duration=1.0)
    with step("[Verify] lblVal text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '100')
    with step("[Verify] Capture '00132_main_05_15_02_Step26' for GT comparison"):
        actions.capture_for_gt('00132_main_05_15_02_Step26', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap Horizon at (55.6%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Horizon', 55.6, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=374, container_h=119)
    with step("[Verify] lblVal text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '0')
    with step("[Action] Drag slider (7.4%,58.0%) → sliderBackgroundView (74.4%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 7.4, 58.0, AppiumBy.ACCESSIBILITY_ID, 'sliderBackgroundView', 74.4, 57.1, duration=1.0)
    with step("[Verify] lblVal text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '100')
    with step("[Verify] Capture '00132_main_05_15_02_Step31' for GT comparison"):
        actions.capture_for_gt('00132_main_05_15_02_Step31', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap Land Ambient at (46.0%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Land Ambient', 46.0, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=374, container_h=119)
    with step("[Verify] lblVal text equals '35'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '35')
    with step("[Action] Drag slider (38.7%,56.0%) → sliderBackgroundView (14.2%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 38.7, 56.0, AppiumBy.ACCESSIBILITY_ID, 'sliderBackgroundView', 14.2, 57.1, duration=1.0)
    with step("[Verify] lblVal text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '0')
    with step("[Verify] Capture '00132_main_05_15_02_Step36' for GT comparison"):
        actions.capture_for_gt('00132_main_05_15_02_Step36', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Drag slider (7.0%,62.0%) → sliderBackgroundView (74.7%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 7.0, 62.0, AppiumBy.ACCESSIBILITY_ID, 'sliderBackgroundView', 74.7, 57.1, duration=1.0)
    with step("[Verify] lblVal text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '100')
    with step("[Verify] Capture '00132_main_05_15_02_Step39' for GT comparison"):
        actions.capture_for_gt('00132_main_05_15_02_Step39', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap Sky Fade at (41.3%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sky Fade', 41.3, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=374, container_h=119)
    with step("[Verify] lblVal text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '0')
    with step("[Action] Drag slider (6.6%,48.0%) → sliderBackgroundView (72.3%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 6.6, 48.0, AppiumBy.ACCESSIBILITY_ID, 'sliderBackgroundView', 72.3, 51.0, duration=1.0)
    with step("[Verify] lblVal text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '100')
    with step("[Verify] Capture '00132_main_05_15_02_Step44' for GT comparison"):
        actions.capture_for_gt('00132_main_05_15_02_Step44', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap Speed at (44.4%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Speed', 44.4, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=374, container_h=119)
    with step("[Verify] lblVal text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '1')
    with step("[Action] Drag slider (7.0%,54.0%) → sliderBackgroundView (75.6%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 7.0, 54.0, AppiumBy.ACCESSIBILITY_ID, 'sliderBackgroundView', 75.6, 59.2, duration=1.0)
    with step("[Verify] lblVal text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '100')
    with step("[Verify] Capture '00132_main_05_15_02_Step49' for GT comparison"):
        actions.capture_for_gt('00132_main_05_15_02_Step49', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap btnPlay at (62.5%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 62.5, 67.5)
    with step("[Verify] Capture '00132_main_05_15_02_Step51' for GT comparison"):
        actions.capture_for_gt('00132_main_05_15_02_Step51', AppiumBy.ACCESSIBILITY_ID, 'btnPlay', threshold=0.95)
    with step("[Action] Tap btnPlay at (57.5%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 57.5, 75.0)
    with step("[Verify] Capture '00132_main_05_15_02_Step53' for GT comparison"):
        actions.capture_for_gt('00132_main_05_15_02_Step53', AppiumBy.ACCESSIBILITY_ID, 'btnPlay', threshold=0.95)
    with step("[Action] Tap btnBack at (31.8%, 55.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 31.8, 55.4)
    with step("[Action] Tap btnBack at (50.0%, 59.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 50.0, 59.4)
    with step("[Action] Tap btn_ok_n at (83.7%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 83.7, 49.0)
    with step("[Action] Tap Still Image at (54.3%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Still Image', 54.3, 50.0)
    with step("[Action] Tap ic edit undo n at (56.4%, 38.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 56.4, 38.5)
    with step("[Verify] Capture '00132_main_05_15_02_Step59' for GT comparison"):
        actions.capture_for_gt('00132_main_05_15_02_Step59', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Live at (59.2%, 28.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Live', 59.2, 28.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Sky at (46.4%, 20.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sky', 46.4, 20.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Scroll until Cloudy"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'skyExpandCollectionViewCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Cloudy', direction='left', offset_start=(0.872, 0.931), offset_end=(0.401, 0.931), velocity=427)
    with step("[Action] Tap Cloudy at (69.5%, 57.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cloudy', 69.5, 57.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='skyExpandCollectionViewCollectionView', container_w=374, container_h=101)
    with step("[Action] Tap 01 at (53.7%, 31.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '01', 53.7, 31.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='skyExpandCollectionViewCollectionView', container_w=374, container_h=101)
    with step("[Action] Tap btnBack at (36.4%, 49.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 36.4, 49.5)
    with step("[Action] Tap btn_ok_n at (73.5%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 44.9)
    with step("[Action] Tap Video at (88.5%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Video', 88.5, 75.0)
    with step("[Verify] navDescriptionLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel')
    with step("[Action] Tap navBackButton at (38.6%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 38.6, 46.7)
    with step("[Action] Tap btn_cancel_n at (18.4%, 12.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 18.4, 12.2)
    with step("[Action] Tap Discard at (50.7%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 50.7, 75.0)
    with step("[Action] Tap homeButton at (34.6%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 34.6, 73.1)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
