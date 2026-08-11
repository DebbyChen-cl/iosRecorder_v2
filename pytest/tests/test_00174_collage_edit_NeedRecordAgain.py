import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00174_collage_edit_20260809_163403")
def test_00174_collage_edit_20260809_163403(actions: DriverActions):
    # with step("[Action] Scroll until Collage"):
    #     actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'Collage', direction='left', offset_start=(0.977, 0.448), offset_end=(0.06, 0.448), velocity=352)
    # with step("[Action] Tap Collage at (62.5%, 35.1%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collage', 62.5, 35.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    # with step("[Action] Tap 2 at (54.5%, 36.8%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '2', 54.5, 36.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.CollageWebViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=396, container_h=44)
    # with step("[Action] Tap CMS-phdm_20230610_IndependenceDay_G_1_02 at (56.9%, 50.7%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_20230610_IndependenceDay_G_1_02', 56.9, 50.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='CollageContentViewCell-contentCollectionView', container_w=413, container_h=138)
    # with step("[Action] Tap btnAlbum at (75.1%, 47.6%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 75.1, 47.6)
    # with step("[Action] Tap _AT at (6.8%, 59.1%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 6.8, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=632)
    # with step("[Action] Tap photoCell-0 at (46.9%, 60.8%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 46.9, 60.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    # with step("[Action] Tap photoCell-1 at (60.0%, 56.9%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 60.0, 56.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    # with step("[Action] Tap Next at (55.9%, 57.9%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next', 55.9, 57.9)
    # with step("[Verify] Capture '00174_collage_edit_Step10' for GT comparison"):
    #     actions.capture_for_gt('00174_collage_edit_Step10', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    # with step("[Action] Tap CMS-Optional(\"phdm_202302_Graduation_J1_02\") at (48.5%, 46.4%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_202302_Graduation_J1_02")', 48.5, 46.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=357, container_h=80)
    # with step("[Action] Tap //XCUIElementTypeOther[@name=\"photodirector.AddImageViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther[2] at (51.7%, 47.6%)"):
    #     actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther[2]', 51.7, 47.6)
    # with step("[Action] Tap lblText at (80.6%, 41.9%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lblText', 80.6, 41.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=359, container_h=80)
    # with step("[Action] Tap btnCamera at (60.0%, 65.9%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnCamera', 60.0, 65.9)
    # with step("[Action] Tap PhotoCapture at (60.0%, 55.0%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoCapture', 60.0, 55.0)
    # with step("[Action] Tap Use Photo at (17.6%, 39.1%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Use Photo', 17.6, 39.1)
    # with step("[Action] Tap lblText at (55.2%, 48.4%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lblText', 55.2, 48.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=359, container_h=80)
    # with step("[Action] Tap photoCell-6 at (40.8%, 48.5%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 40.8, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    # with step("[Verify] Capture '00174_collage_edit_Step20' for GT comparison"):
    #     actions.capture_for_gt('00174_collage_edit_Step20', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap imageView at (69.7%, 58.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 69.7, 58.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=359, container_h=80)
    with step("[Verify] Capture '00174_collage_edit_Step22' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step22', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap imageView at (66.7%, 61.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 66.7, 61.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=359, container_h=80)
    with step("[Verify] Capture '00174_collage_edit_Step24' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step24', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap lblText at (44.8%, 38.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lblText', 44.8, 38.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=359, container_h=80)
    with step("[Action] Tap Light at (78.2%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Light', 78.2, 52.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=206, container_h=46)
    with step("[Action] Tap btn_effect at (78.8%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_effect', 78.8, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Verify] Capture '00174_collage_edit_Step28' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step28', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_effect at (45.5%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_effect', 45.5, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (50.3%,54.0%) → sliderViewArea (84.7%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 50.3, 54.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 84.7, 59.2, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '4.00'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '4.00')
    with step("[Verify] Capture '00174_collage_edit_Step32' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step32', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_contrast at (75.8%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_contrast', 75.8, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (50.8%,50.0%) → sliderViewArea (84.7%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 50.8, 50.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 84.7, 49.0, duration=1.0)
    with step("[Verify] Capture '00174_collage_edit_Step35' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step35', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_brightness at (30.3%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_brightness', 30.3, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (50.3%,48.0%) → sliderViewArea (3.0%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 50.3, 48.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 3.0, 53.1, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '-100')
    with step("[Verify] Capture '00174_collage_edit_Step39' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step39', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Bright at (80.6%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Bright', 80.6, 58.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (49.2%,42.0%) → sliderViewArea (86.0%,44.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 49.2, 42.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 86.0, 44.9, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '100')
    with step("[Verify] Capture '00174_collage_edit_Step43' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step43', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (71.4%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 71.4, 51.0)
    with step("[Action] Tap ic_undo at (57.1%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 57.1, 53.1)
    with step("[Action] Tap ic_undo at (57.1%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 57.1, 53.1)
    with step("[Action] Tap ic_undo at (57.1%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 57.1, 53.1)
    with step("[Action] Tap Midtone at (50.0%, 16.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Midtone', 50.0, 16.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (50.3%,46.0%) → sliderViewArea (85.1%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 50.3, 46.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 85.1, 55.1, duration=1.0)
    with step("[Verify] Capture '00174_collage_edit_Step50' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step50', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (69.4%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 69.4, 44.9)
    with step("[Action] Tap ic_dark at (45.5%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_dark', 45.5, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (49.2%,50.0%) → sliderViewArea (85.8%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 49.2, 50.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 85.8, 59.2, duration=1.0)
    with step("[Verify] Capture '00174_collage_edit_Step54' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step54', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (71.4%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 71.4, 49.0)
    with step("[Action] Tap ic_shadow at (6.1%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_shadow', 6.1, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (51.6%,64.0%) → sliderViewArea (7.9%,73.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 51.6, 64.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 7.9, 73.5, duration=1.0)
    with step("[Verify] Capture '00174_collage_edit_Step58' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step58', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (83.7%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 83.7, 46.9)
    with step("[Action] Tap Color at (50.9%, 58.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Color', 50.9, 58.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=206, container_h=46)
    with step("[Action] Tap btn_effect at (48.5%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_effect', 48.5, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Verify] Capture '00174_collage_edit_Step62' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step62', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (77.6%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 77.6, 46.9)
    with step("[Action] Tap ic_saturation at (57.6%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_saturation', 57.6, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (50.5%,50.0%) → sliderViewArea (75.1%,61.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 50.5, 50.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 75.1, 61.2, duration=1.0)
    with step("[Verify] Capture '00174_collage_edit_Step66' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step66', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (75.5%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 75.5, 49.0)
    with step("[Action] Tap Details at (58.6%, 60.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Details', 58.6, 60.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=206, container_h=46)
    with step("[Action] Tap ic_sharpness at (66.7%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_sharpness', 66.7, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag sharpnessValueSlider (6.6%,56.0%) → sliderViewArea (84.7%,61.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'sharpnessValueSlider', 6.6, 56.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 84.7, 61.2, duration=1.0)
    with step("[Verify] Capture '00174_collage_edit_Step71' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step71', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (79.6%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 79.6, 59.2)
    with step("[Action] Tap Color at (40.4%, 65.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Color', 40.4, 65.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=206, container_h=46)
    with step("[Action] Tap Temperature at (56.3%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Temperature', 56.3, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (50.0%,50.0%) → sliderViewArea (84.7%,44.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 84.7, 44.9, duration=1.0)
    with step("[Verify] Capture '00174_collage_edit_Step76' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step76', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (75.5%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 75.5, 55.1)
    with step("[Action] Tap Tint at (62.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Tint', 62.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag adjustmentValueSlider (51.6%,62.0%) → sliderViewArea (2.1%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 51.6, 62.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 2.1, 59.2, duration=1.0)
    with step("[Verify] Capture '00174_collage_edit_Step80' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step80', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (93.9%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 93.9, 34.7)
    with step("[Action] Tap ic_curve at (97.0%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_curve', 97.0, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag CurveView (68.5%,32.7%) → PhotoDirector (70.2%,73.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'CurveView', 68.5, 32.7, AppiumBy.ACCESSIBILITY_ID, 'PhotoDirector', 70.2, 73.9, duration=1.0)
    with step("[Verify] Capture '00174_collage_edit_Step84' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step84', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (77.6%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 77.6, 30.6)
    with step("[Action] Tap ic_hsl at (36.4%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_hsl', 36.4, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag hueSlider (50.0%,53.3%) → EditingImageView_ImageView (83.6%,83.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 50.0, 53.3, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 83.6, 83.3, duration=1.0)
    with step("[Action] Drag saturationSlider (50.7%,51.1%) → EditingImageView_ImageView (81.4%,90.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 50.7, 51.1, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 81.4, 90.5, duration=1.0)
    with step("[Action] Drag lightnessSlider (51.4%,55.6%) → EditingImageView_ImageView (80.7%,97.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'lightnessSlider', 51.4, 55.6, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 80.7, 97.3, duration=1.0)
    with step("[Verify] Capture '00174_collage_edit_Step90' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step90', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (95.9%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 95.9, 46.9)
    with step("[Verify] Capture '00174_collage_edit_Step92' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step92', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Scroll until lblText"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', AppiumBy.ACCESSIBILITY_ID, 'lblText', direction='left', offset_start=(0.786, 0.2), offset_end=(0.393, 0.2), velocity=94)
    with step("[Action] Tap lblText at (44.8%, 32.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lblText', 44.8, 32.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=359, container_h=80)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CMS-a0df0f61-ddc2-41ad-8810-4e3c3a1f40e6_trending\"]/XCUIElementTypeOther/XCUIElementTypeImage at (62.5%, 52.1%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-a0df0f61-ddc2-41ad-8810-4e3c3a1f40e6_trending"]/XCUIElementTypeOther/XCUIElementTypeImage', 62.5, 52.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=94)
    with step("[Verify] Capture '00174_collage_edit_Step96' for GT comparison"):
        actions.capture_for_gt('00174_collage_edit_Step96', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (73.5%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 40.8)
    with step("[Action] Tap btn_ok_n at (79.6%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 79.6, 26.5)
    with step("[Action] Tap OK at (10.0%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 10.0, 75.0)
    with step("[Action] Tap navHomeButton at (61.4%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton', 61.4, 60.0)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
