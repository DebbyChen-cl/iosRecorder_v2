import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00138_main_05_14_01_20260809_161044")
def test_00138_main_05_14_01_20260809_161044(actions: DriverActions):
    with step("[Action] Tap Edit at (71.4%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 71.4, 64.0)
    with step("[Action] Tap btnAlbum at (76.6%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 76.6, 54.8)
    with step("[Action] Tap _AT at (9.7%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.7, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (33.1%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 33.1, 61.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (54.9%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 54.9, 62.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Live"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Live', direction='left', offset_start=(0.616, 0.433), offset_end=(0.214, 0.433), velocity=115)
    with step("[Action] Tap Live at (60.6%, 26.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Live', 60.6, 26.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Scroll until Dispersion"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'Dispersion', direction='left', offset_start=(0.684, 0.34), offset_end=(0.3, 0.34), velocity=481)
    with step("[Action] Tap Dispersion at (34.8%, 11.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Dispersion', 34.8, 11.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap btnBack at (56.4%, 40.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 56.4, 40.2)
    with step("[Action] Tap Dispersion at (47.8%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Dispersion', 47.8, 26.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '25'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '25')
    with step("[Action] Drag blackBackgroundView (48.1%,17.3%) → blackBackgroundView (48.1%,69.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 48.1, 17.3, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 48.1, 69.0, duration=1.0)
    with step("[Verify] Capture '00138_main_05_14_01_Step14' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step14', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (26.0%,54.8%) → blackBackgroundView (14.2%,78.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 26.0, 54.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 14.2, 78.5, duration=1.0)
    with step("[Verify] valueLabel text equals '8'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '8')
    with step("[Action] Drag blackBackgroundView (32.1%,20.9%) → blackBackgroundView (30.7%,66.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 32.1, 20.9, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 30.7, 66.2, duration=1.0)
    with step("[Verify] Capture '00138_main_05_14_01_Step18' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step18', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (8.0%,50.0%) → blackBackgroundView (74.2%,78.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 8.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 74.2, 78.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag blackBackgroundView (71.9%,17.6%) → blackBackgroundView (71.9%,71.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 71.9, 17.6, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 71.9, 71.6, duration=1.0)
    with step("[Verify] Capture '00138_main_05_14_01_Step22' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step22', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (57.1%, 24.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 57.1, 24.5)
    with step("[Verify] Capture '00138_main_05_14_01_Step24' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step24', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_redo at (61.2%, 20.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 61.2, 20.4)
    with step("[Verify] Capture '00138_main_05_14_01_Step26' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step26', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnErase at (65.0%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnErase', 65.0, 65.0)
    with step("[Action] Drag blackBackgroundView (9.8%,44.2%) → blackBackgroundView (93.3%,43.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 9.8, 44.2, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 93.3, 43.8, duration=1.0)
    with step("[Verify] Capture '00138_main_05_14_01_Step29' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step29', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnMaskSwitch at (57.5%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch', 57.5, 62.5)
    with step("[Action] Tap btnMaskSwitch at (42.5%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch', 42.5, 47.5)
    with step("[Action] Tap Shape at (63.5%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Shape', 63.5, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=375, container_h=97)
    with step("[Action] Tap Square_thumb at (38.9%, 72.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Square_thumb', 38.9, 72.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="shapeView"]/XCUIElementTypeCollectionView', container_w=375, container_h=97)
    with step("[Verify] Capture '00138_main_05_14_01_Step34' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step34', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnBack at (45.5%, 56.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 45.5, 56.7)
    with step("[Action] Tap Size at (69.8%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Size', 69.8, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=375, container_h=97)
    with step("[Verify] valueLabel text equals '15'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '15')
    with step("[Action] Drag cpSlider (22.6%,57.1%) → blackBackgroundView (14.7%,78.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 22.6, 57.1, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 14.7, 78.8, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00138_main_05_14_01_Step40' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step40', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (7.9%,54.8%) → blackBackgroundView (75.8%,78.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.9, 54.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 75.8, 78.5, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00138_main_05_14_01_Step43' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step43', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (69.4%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 69.4, 34.7)
    with step("[Verify] Capture '00138_main_05_14_01_Step45' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step45', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_redo at (77.6%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 77.6, 46.9)
    with step("[Verify] Capture '00138_main_05_14_01_Step47' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step47', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap Direction at (63.5%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Direction', 63.5, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=375, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag cpSlider (8.3%,64.3%) → blackBackgroundView (78.4%,78.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 8.3, 64.3, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 78.4, 78.3, duration=1.0)
    with step("[Verify] valueLabel text equals '360'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '360')
    with step("[Verify] Capture '00138_main_05_14_01_Step52' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step52', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (59.2%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 59.2, 38.8)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Tap ic_redo at (61.2%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 61.2, 28.6)
    with step("[Verify] valueLabel text equals '360'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '360')
    with step("[Action] Tap Mode at (73.0%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Mode', 73.0, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=375, container_h=97)
    with step("[Action] Tap Straight at (81.0%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Straight', 81.0, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='modeView', container_w=375, container_h=97)
    with step("[Verify] Capture '00138_main_05_14_01_Step59' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step59', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap Shrink at (54.0%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Shrink', 54.0, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='modeView', container_w=375, container_h=97)
    with step("[Verify] Capture '00138_main_05_14_01_Step61' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step61', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap Spread at (73.0%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Spread', 73.0, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='modeView', container_w=375, container_h=97)
    with step("[Verify] Capture '00138_main_05_14_01_Step63' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step63', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnBack at (56.4%, 58.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 56.4, 58.8)
    with step("[Action] Tap Stretch at (42.9%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Stretch', 42.9, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=375, container_h=97)
    with step("[Verify] valueLabel text equals '25'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '25')
    with step("[Action] Drag cpSlider (29.1%,54.8%) → blackBackgroundView (14.0%,78.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 29.1, 54.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 14.0, 78.8, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00138_main_05_14_01_Step69' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step69', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (8.3%,59.5%) → blackBackgroundView (75.8%,78.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 8.3, 59.5, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 75.8, 78.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00138_main_05_14_01_Step72' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step72', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Scroll until Fade"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'Fade', direction='left', offset_start=(0.293, 0.392), offset_end=(0.099, 0.392), velocity=81)
    with step("[Action] Tap Fade at (54.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Fade', 54.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=375, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag cpSlider (6.4%,59.5%) → blackBackgroundView (76.5%,78.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.4, 59.5, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 76.5, 78.4, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00138_main_05_14_01_Step78' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step78', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (81.6%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 81.6, 34.7)
    with step("[Action] Scroll until Speed"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'Speed', direction='left', offset_start=(0.667, 0.454), offset_end=(0.085, 0.454), velocity=268)
    with step("[Action] Tap Speed at (57.1%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Speed', 57.1, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=375, container_h=97)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (50.9%,50.0%) → blackBackgroundView (14.4%,78.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 50.9, 50.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 14.4, 78.5, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Action] Drag cpSlider (6.8%,57.1%) → blackBackgroundView (76.7%,78.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.8, 57.1, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 76.7, 78.3, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap btnPlay at (75.0%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 75.0, 47.5)
    with step("[Verify] Capture '00138_main_05_14_01_Step87' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step87', AppiumBy.ACCESSIBILITY_ID, 'btnPlay', threshold=0.95)
    with step("[Action] Tap btnPlay at (52.5%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 52.5, 57.5)
    with step("[Verify] Capture '00138_main_05_14_01_Step89' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step89', AppiumBy.ACCESSIBILITY_ID, 'btnPlay', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (73.5%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 38.8)
    with step("[Action] Tap Still Image at (87.2%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Still Image', 87.2, 83.3)
    with step("[Verify] Capture '00138_main_05_14_01_Step92' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step92', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (46.2%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 46.2, 46.2)
    with step("[Verify] Capture '00138_main_05_14_01_Step94' for GT comparison"):
        actions.capture_for_gt('00138_main_05_14_01_Step94', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Live at (59.2%, 31.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Live', 59.2, 31.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Scroll until Dispersion"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'Dispersion', direction='left', offset_start=(0.733, 0.433), offset_end=(0.307, 0.433), velocity=309)
    with step("[Action] Tap Dispersion at (33.3%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Dispersion', 33.3, 26.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Drag blackBackgroundView (67.2%,22.4%) → blackBackgroundView (38.1%,64.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 67.2, 22.4, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 38.1, 64.6, duration=1.0)
    with step("[Action] Tap btn_ok_n at (77.6%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 40.8)
    with step("[Action] Tap Video at (42.3%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Video', 42.3, 62.5)
    with step("[Action] Tap ic_gif_n at (55.6%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_gif_n', 55.6, 56.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoExportTypeViewCollectionView', container_w=430, container_h=80)
    with step("[Action] Tap navSaveButton at (34.1%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton', 34.1, 48.9)
    with step("[Action] Tap OK at (53.6%, 54.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 53.6, 54.2)
    with step("[Action] Tap ic_video_n at (44.4%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_video_n', 44.4, 56.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoExportTypeViewCollectionView', container_w=430, container_h=80)
    with step("[Action] Tap navSaveButton at (56.8%, 42.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton', 56.8, 42.2)
    with step("[Action] Tap navHomeButton at (47.7%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton', 47.7, 51.1)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
