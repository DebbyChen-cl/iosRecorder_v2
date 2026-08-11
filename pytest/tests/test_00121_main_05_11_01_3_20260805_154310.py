import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00121_main_05_11_01_3_20260805_154310")
def test_00121_main_05_11_01_3_20260805_154310(actions: DriverActions):
    with step("[Action] Tap Edit at (48.6%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 48.6, 60.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (68.0%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 68.0, 61.9)
    with step("[Action] Tap _AT at (9.7%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.7, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (48.5%, 62.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 48.5, 62.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (40.0%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 40.0, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_addimg_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', direction='left', offset_start=(0.659, 0.402), offset_end=(0.241, 0.402), velocity=255)
    with step("[Action] Tap btn_addimg_n at (67.6%, 21.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', 67.6, 21.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Action] Tap btnAlbum at (78.7%, 59.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 78.7, 59.5)
    with step("[Action] Tap _AT at (8.6%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.6, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-1 at (40.8%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 40.8, 70.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap imageView at (70.7%, 70.0%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="AddImageMainPanelCell-3"]', 70.7, 70.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap btn_effect at (69.7%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_effect', 69.7, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step13' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step13', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag adjustmentValueSlider (45.3%,50.0%) → sliderViewArea (84.0%,42.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 45.3, 50.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 84.0, 42.9, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '4.00'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '4.00')
    with step("[Verify] Capture '00121_main_05_11_01_3_Step16' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step16', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (57.1%, 22.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 57.1, 22.4)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step18' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step18', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Scroll until ic_contrast"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'AdjustmentEffectBottomBar', AppiumBy.ACCESSIBILITY_ID, 'ic_contrast', direction='left', offset_start=(0.626, 0.549), offset_end=(0.305, 0.549), velocity=92)
    with step("[Action] Tap ic_contrast at (64.7%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_contrast', 64.7, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (48.9%,46.0%) → sliderViewArea (84.4%,61.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 48.9, 46.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 84.4, 61.2, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '100')
    with step("[Verify] Capture '00121_main_05_11_01_3_Step23' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step23', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (65.3%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 65.3, 69.4)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step25' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step25', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_brightness at (45.5%, 84.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_brightness', 45.5, 84.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Verify] adjustmentValueLabel text equals '47'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '47')
    with step("[Action] Drag adjustmentValueSlider (72.5%,64.0%) → sliderViewArea (2.6%,63.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 72.5, 64.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 2.6, 63.3, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '-100')
    with step("[Verify] Capture '00121_main_05_11_01_3_Step30' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step30', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (79.6%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 79.6, 40.8)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step32' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step32', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_bright at (76.5%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_bright', 76.5, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Verify] adjustmentValueLabel text equals '-34'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '-34')
    with step("[Action] Drag adjustmentValueSlider (32.1%,38.0%) → sliderViewArea (85.6%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 32.1, 38.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 85.6, 51.0, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '100')
    with step("[Verify] Capture '00121_main_05_11_01_3_Step37' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step37', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (57.1%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 57.1, 46.9)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step39' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step39', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_midtone at (91.2%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_midtone', 91.2, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (50.3%,56.0%) → sliderViewArea (85.6%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 50.3, 56.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 85.6, 49.0, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '100')
    with step("[Verify] Capture '00121_main_05_11_01_3_Step43' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step43', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (93.9%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 93.9, 28.6)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step45' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step45', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_dark at (60.6%, 84.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_dark', 60.6, 84.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Verify] adjustmentValueLabel text equals '26'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '26')
    with step("[Action] Drag adjustmentValueSlider (62.6%,54.0%) → sliderViewArea (84.0%,63.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 62.6, 54.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 84.0, 63.3, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '100')
    with step("[Verify] Capture '00121_main_05_11_01_3_Step50' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step50', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (71.4%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 71.4, 32.7)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step52' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step52', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_shadow at (63.6%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_shadow', 63.6, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (50.5%,56.0%) → sliderViewArea (5.3%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 50.5, 56.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 5.3, 49.0, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '-100')
    with step("[Verify] Capture '00121_main_05_11_01_3_Step56' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step56', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (75.5%, 22.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 75.5, 22.4)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step58' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step58', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Color at (77.2%, 47.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Color', 77.2, 47.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=206, container_h=46)
    with step("[Action] Tap btn_effect at (69.7%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_effect', 69.7, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step61' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step61', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (67.3%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 67.3, 44.9)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step63' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step63', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_saturation at (90.9%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_saturation', 90.9, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (49.2%,46.0%) → sliderViewArea (70.9%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 49.2, 46.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 70.9, 55.1, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '100')
    with step("[Verify] Capture '00121_main_05_11_01_3_Step67' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step67', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (65.3%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 65.3, 44.9)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step69' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step69', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Details at (38.6%, 95.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Details', 38.6, 95.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=206, container_h=46)
    with step("[Action] Tap ic_sharpness at (93.9%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_sharpness', 93.9, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag sharpnessValueSlider (5.2%,48.0%) → sliderViewArea (85.6%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'sharpnessValueSlider', 5.2, 48.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 85.6, 49.0, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '100')
    with step("[Verify] Capture '00121_main_05_11_01_3_Step74' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step74', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (53.1%, 18.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 53.1, 18.4)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step76' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step76', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Color at (57.9%, 80.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Color', 57.9, 80.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=206, container_h=46)
    with step("[Action] Tap AdjustmentEffectCell-2 at (38.7%, 78.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AdjustmentEffectCell-2', 38.7, 78.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (50.5%,42.0%) → sliderViewArea (84.7%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 50.5, 42.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 84.7, 57.1, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '100')
    with step("[Verify] Capture '00121_main_05_11_01_3_Step81' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step81', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (83.7%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 83.7, 53.1)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step83' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step83', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_tint at (36.4%, 30.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_tint', 36.4, 30.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (51.9%,56.0%) → sliderViewArea (4.2%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 51.9, 56.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 4.2, 49.0, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '-100')
    with step("[Verify] Capture '00121_main_05_11_01_3_Step87' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step87', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (59.2%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 59.2, 51.0)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step89' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step89', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_curve at (57.6%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_curve', 57.6, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag CurveView (67.7%,33.3%) → PhotoDirector (70.9%,73.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'CurveView', 67.7, 33.3, AppiumBy.ACCESSIBILITY_ID, 'PhotoDirector', 70.9, 73.1, duration=1.0)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step92' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step92', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (79.6%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 79.6, 32.7)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step94' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step94', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_hsl at (42.4%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_hsl', 42.4, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag hueSlider (52.5%,60.0%) → slidersStack (93.2%,19.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 52.5, 60.0, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 93.2, 19.7, duration=1.0)
    with step("[Action] Drag saturationSlider (48.6%,55.6%) → slidersStack (95.3%,50.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 48.6, 55.6, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 95.3, 50.8, duration=1.0)
    with step("[Action] Drag lightnessSlider (51.4%,57.8%) → slidersStack (97.5%,85.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'lightnessSlider', 51.4, 57.8, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 97.5, 85.6, duration=1.0)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step99' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step99', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (71.4%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 71.4, 46.9)
    with step("[Action] Tap btn_ok_n at (89.8%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 89.8, 46.9)
    with step("[Action] Tap OK at (66.7%, 79.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 66.7, 79.2)
    with step("[Verify] Capture '00121_main_05_11_01_3_Step103' for GT comparison"):
        actions.capture_for_gt('00121_main_05_11_01_3_Step103', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (61.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 50.0)
    with step("[Action] Tap Discard at (76.8%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 76.8, 58.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
