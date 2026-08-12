import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00136_main_06_02_01_20260811_162557")
def test_00136_main_06_02_01_20260811_162557(actions: DriverActions):
    with step("[Action] Tap Edit at (94.3%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 94.3, 48.0)
    with step("[Action] Tap btnAlbum at (65.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 65.5, 50.0)
    with step("[Action] Tap _AT at (8.2%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.2, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (46.9%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 46.9, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (54.9%, 64.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 54.9, 64.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Live"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Live', direction='left', offset_start=(0.795, 0.412), offset_end=(0.237, 0.412), velocity=181)
    with step("[Action] Tap Live at (53.5%, 26.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Live', 53.5, 26.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Scroll until Animation"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'Animation', direction='left', offset_start=(0.635, 0.454), offset_end=(0.44, 0.454), velocity=255)
    with step("[Action] Tap Animation at (46.4%, 35.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Animation', 46.4, 35.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap Motion at (79.4%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Motion', 79.4, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationGPUPhotoAnimationMenuViewCollectionView', container_w=375, container_h=97)
    with step("[Action] Drag blackBackgroundView (34.4%,19.0%) → blackBackgroundView (32.1%,72.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 34.4, 19.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 32.1, 72.5, duration=1.0)
    with step("[Verify] Capture '00136_main_06_02_01_Step12' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step12', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag blackBackgroundView (12.6%,49.5%) → blackBackgroundView (85.6%,50.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 12.6, 49.5, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 85.6, 50.1, duration=1.0)
    with step("[Verify] Capture '00136_main_06_02_01_Step14' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step14', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnPlay at (75.0%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 75.0, 60.0)
    with step("[Verify] Capture '00136_main_06_02_01_Step16' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step16', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (71.4%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 71.4, 46.9)
    with step("[Verify] Capture '00136_main_06_02_01_Step18' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step18', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_redo at (65.3%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 65.3, 40.8)
    with step("[Verify] Capture '00136_main_06_02_01_Step20' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step20', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap Anchor at (81.0%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Anchor', 81.0, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationGPUPhotoAnimationMenuViewCollectionView', container_w=375, container_h=97)
    with step("[Action] Tap blackBackgroundView at (31.4%, 31.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 31.4, 31.0)
    with step("[Action] Tap blackBackgroundView at (45.8%, 37.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 45.8, 37.4)
    with step("[Action] Tap blackBackgroundView at (57.7%, 43.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 57.7, 43.1)
    with step("[Action] Tap blackBackgroundView at (73.0%, 47.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 73.0, 47.9)
    with step("[Verify] Capture '00136_main_06_02_01_Step26' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step26', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnPlay at (65.0%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 65.0, 75.0)
    with step("[Verify] Capture '00136_main_06_02_01_Step28' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step28', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (34.7%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 34.7, 26.5)
    with step("[Verify] Capture '00136_main_06_02_01_Step30' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step30', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_redo at (67.3%, 12.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 67.3, 12.2)
    with step("[Verify] Capture '00136_main_06_02_01_Step32' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step32', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap Freeze at (58.7%, 31.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Freeze', 58.7, 31.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationGPUPhotoAnimationMenuViewCollectionView', container_w=375, container_h=97)
    with step("[Action] Drag blackBackgroundView (78.1%,26.4%) → blackBackgroundView (34.7%,67.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 78.1, 26.4, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 34.7, 67.8, duration=1.0)
    with step("[Verify] Capture '00136_main_06_02_01_Step35' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step35', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnPlay at (32.5%, 37.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 32.5, 37.5)
    with step("[Verify] Capture '00136_main_06_02_01_Step37' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step37', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (49.0%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 49.0, 40.8)
    with step("[Verify] Capture '00136_main_06_02_01_Step39' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step39', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_redo at (95.9%, 16.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 95.9, 16.3)
    with step("[Verify] Capture '00136_main_06_02_01_Step41' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step41', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (23.3%,50.0%) → blackBackgroundView (77.0%,78.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 23.3, 50.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 77.0, 78.5, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag cpSlider (93.9%,45.2%) → blackBackgroundView (13.3%,78.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 93.9, 45.2, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 13.3, 78.3, duration=1.0)
    with step("[Verify] valueLabel text equals '8'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '8')
    with step("[Action] Tap btnMaskSwitch at (67.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch', 67.5, 50.0)
    with step("[Action] Tap btnErase at (60.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnErase', 60.0, 52.5)
    with step("[Action] Drag cpSlider (8.0%,50.0%) → blackBackgroundView (73.3%,78.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 8.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 73.3, 78.3, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag blackBackgroundView (68.4%,29.8%) → blackBackgroundView (93.0%,42.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 68.4, 29.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 93.0, 42.9, duration=1.0)
    with step("[Verify] Capture '00136_main_06_02_01_Step51' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step51', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (92.7%,54.8%) → blackBackgroundView (14.7%,78.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 92.7, 54.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 14.7, 78.0, duration=1.0)
    with step("[Verify] valueLabel text equals '8'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '8')
    with step("[Action] Drag blackBackgroundView (29.1%,63.6%) → blackBackgroundView (58.4%,73.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 29.1, 63.6, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 58.4, 73.0, duration=1.0)
    with step("[Verify] Capture '00136_main_06_02_01_Step55' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step55', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (59.2%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 59.2, 49.0)
    with step("[Action] Tap ic_undo at (67.3%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 67.3, 49.0)
    with step("[Verify] Capture '00136_main_06_02_01_Step58' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step58', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_redo at (81.6%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 81.6, 40.8)
    with step("[Verify] Capture '00136_main_06_02_01_Step60' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step60', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap Speed at (50.8%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Speed', 50.8, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationGPUPhotoAnimationMenuViewCollectionView', container_w=375, container_h=97)
    with step("[Verify] valueLabel text equals '75'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '75')
    with step("[Action] Drag cpSlider (74.2%,42.9%) → blackBackgroundView (6.5%,79.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 74.2, 42.9, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 6.5, 79.7, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag cpSlider (6.0%,52.4%) → blackBackgroundView (76.3%,78.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.0, 52.4, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 76.3, 78.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap btn_delete_n at (36.6%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_delete_n', 36.6, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationGPUPhotoAnimationMenuViewCollectionView', container_w=375, container_h=97)
    with step("[Action] Tap blackBackgroundView at (41.6%, 49.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 41.6, 49.7)
    with step("[Verify] Capture '00136_main_06_02_01_Step69' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step69', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (85.7%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 85.7, 32.7)
    with step("[Verify] Capture '00136_main_06_02_01_Step71' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step71', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_redo at (49.0%, 61.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 49.0, 61.2)
    with step("[Verify] Capture '00136_main_06_02_01_Step73' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step73', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap blackBackgroundView at (31.6%, 31.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 31.6, 31.3)
    with step("[Action] Tap blackBackgroundView at (31.9%, 31.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 31.9, 31.0)
    with step("[Action] Tap blackBackgroundView at (46.5%, 37.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 46.5, 37.7)
    with step("[Verify] Capture '00136_main_06_02_01_Step77' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step77', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (75.5%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 75.5, 53.1)
    with step("[Action] Tap ic_undo at (71.4%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 71.4, 49.0)
    with step("[Verify] Capture '00136_main_06_02_01_Step80' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step80', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_redo at (55.1%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 55.1, 49.0)
    with step("[Action] Tap ic_redo at (59.2%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 59.2, 49.0)
    with step("[Verify] Capture '00136_main_06_02_01_Step83' for GT comparison"):
        actions.capture_for_gt('00136_main_06_02_01_Step83', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (57.1%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 57.1, 38.8)
    with step("[Action] Tap navSaveButton at (47.7%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton', 47.7, 46.7)
    with step("[Action] Tap navHomeButton at (50.0%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton', 50.0, 62.2)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
