import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00033_adjustment_exposure_contrast_highlights_shadows_20260808_163319")
def test_00033_adjustment_exposure_contrast_highlights_shadows_20260808_163319(actions: DriverActions):
    with step("[Action] Tap Edit at (54.3%, 28.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 54.3, 28.0)
    with step("[Action] Tap btnAlbum at (75.6%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 75.6, 71.4)
    with step("[Action] Tap _AT at (10.4%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.4, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (44.6%, 47.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 44.6, 47.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Enhance at (54.8%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 54.8, 62.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Adjustments"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Adjustments', direction='left', offset_start=(0.253, 0.536), offset_end=(0.177, 0.536), velocity=50)
    with step("[Action] Tap Adjustments at (52.8%, 21.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Adjustments', 52.8, 21.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] adjustmentValueLabel text equals '0.00'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '0.00')
    with step("[Action] Drag adjustmentValueSlider (49.7%,48.0%) → sliderViewArea (2.6%,42.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 49.7, 48.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 2.6, 42.9, duration=1.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step10' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step10', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Verify] adjustmentValueLabel text equals '-4.00'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '-4.00')
    with step("[Action] Drag adjustmentValueSlider (5.8%,42.0%) → sliderViewArea (82.8%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 5.8, 42.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 82.8, 57.1, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '4.00'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '4.00')
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step14' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step14', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag EditingImageView_ImageView (86.7%,51.4%) → photodirector.AdjustmentsProViewController (14.4%,40.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 86.7, 51.4, AppiumBy.ACCESSIBILITY_ID, 'photodirector.AdjustmentsProViewController', 14.4, 40.3, duration=1.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step16' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step16', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag EditingImageView_ImageView (13.7%,51.4%) → photodirector.AdjustmentsProViewController (80.7%,39.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 13.7, 51.4, AppiumBy.ACCESSIBILITY_ID, 'photodirector.AdjustmentsProViewController', 80.7, 39.7, duration=1.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step18' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step18', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap reginalAdjustmentButton at (42.5%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton', 42.5, 47.5)
    with step("[Action] Drag EditingImageView_ImageView (50.0%,48.6%) → toneAdjustmentMaskView (50.0%,28.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 50.0, 48.6, AppiumBy.ACCESSIBILITY_ID, 'toneAdjustmentMaskView', 50.0, 28.0, duration=1.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step21' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step21', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap reginalAdjustmentButton at (50.0%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton', 50.0, 70.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step23' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step23', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap reginalAdjustmentButton at (47.5%, 27.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton', 47.5, 27.5)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step25' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step25', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap reginalAdjustmentButton at (65.0%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton', 65.0, 62.5)
    with step("[Action] Tap Auto at (50.7%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Auto', 50.7, 75.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step28' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step28', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (34.7%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 34.7, 40.8)
    with step("[Action] Tap Adjustments at (70.8%, 10.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Adjustments', 70.8, 10.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step31' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step31', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Contrast at (56.3%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Contrast', 56.3, 83.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step33' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step33', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Verify] adjustmentValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '0')
    with step("[Action] Drag adjustmentValueSlider (50.5%,52.0%) → sliderViewArea (2.6%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 50.5, 52.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 2.6, 49.0, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '-100')
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step37' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step37', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag adjustmentValueSlider (3.0%,38.0%) → sliderViewArea (84.0%,40.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 3.0, 38.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 84.0, 40.8, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '100')
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step40' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step40', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag EditingImageView_ImageView (84.2%,49.6%) → photodirector.AdjustmentsProViewController (17.7%,38.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 84.2, 49.6, AppiumBy.ACCESSIBILITY_ID, 'photodirector.AdjustmentsProViewController', 17.7, 38.5, duration=1.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step42' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step42', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag EditingImageView_ImageView (15.1%,53.6%) → Vertical scroll bar, 1 page (16.7%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 15.1, 53.6, AppiumBy.ACCESSIBILITY_ID, 'Vertical scroll bar, 1 page', 16.7, 51.0, duration=1.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step44' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step44', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap reginalAdjustmentButton at (65.0%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton', 65.0, 60.0)
    with step("[Action] Drag EditingImageView_ImageView (50.0%,61.8%) → toneAdjustmentMaskView (49.3%,29.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 50.0, 61.8, AppiumBy.ACCESSIBILITY_ID, 'toneAdjustmentMaskView', 49.3, 29.5, duration=1.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step47' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step47', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap reginalAdjustmentButton at (40.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton', 40.0, 52.5)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step49' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step49', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap reginalAdjustmentButton at (65.0%, 35.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton', 65.0, 35.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step51' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step51', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap reginalAdjustmentButton at (80.0%, 42.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton', 80.0, 42.5)
    with step("[Action] Tap btn_cancel_n at (32.7%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 32.7, 38.8)
    with step("[Action] Tap Adjustments at (80.6%, 21.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Adjustments', 80.6, 21.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Highlight at (54.9%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Highlight', 54.9, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Verify] adjustmentValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '0')
    with step("[Action] Drag adjustmentValueSlider (49.7%,46.0%) → sliderViewArea (3.7%,46.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 49.7, 46.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 3.7, 46.9, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '-100')
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step59' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step59', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag adjustmentValueSlider (4.7%,40.0%) → sliderViewArea (84.7%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 4.7, 40.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 84.7, 57.1, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '100')
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step62' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step62', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag EditingImageView_ImageView (83.5%,51.4%) → photodirector.AdjustmentsProViewController (17.2%,39.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 83.5, 51.4, AppiumBy.ACCESSIBILITY_ID, 'photodirector.AdjustmentsProViewController', 17.2, 39.2, duration=1.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step64' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step64', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag EditingImageView_ImageView (8.6%,55.7%) → photodirector.AdjustmentsProViewController (86.7%,41.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 8.6, 55.7, AppiumBy.ACCESSIBILITY_ID, 'photodirector.AdjustmentsProViewController', 86.7, 41.3, duration=1.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step66' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step66', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap reginalAdjustmentButton at (57.5%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton', 57.5, 55.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step68' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step68', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap reginalAdjustmentButton at (75.0%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton', 75.0, 30.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step70' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step70', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (44.9%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 44.9, 49.0)
    with step("[Action] Tap Adjustments at (61.1%, 21.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Adjustments', 61.1, 21.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Scroll until Shadow"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'AdjustmentEffectBottomBar', AppiumBy.ACCESSIBILITY_ID, 'Shadow', direction='left', offset_start=(0.595, 0.577), offset_end=(0.244, 0.577), velocity=237)
    with step("[Action] Tap Shadow at (31.0%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Shadow', 31.0, 83.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Verify] adjustmentValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '0')
    with step("[Action] Drag adjustmentValueSlider (50.3%,52.0%) → sliderViewArea (2.3%,42.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 50.3, 52.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 2.3, 42.9, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '-100')
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step78' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step78', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag adjustmentValueSlider (4.9%,54.0%) → sliderViewArea (85.1%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueSlider', 4.9, 54.0, AppiumBy.ACCESSIBILITY_ID, 'sliderViewArea', 85.1, 53.1, duration=1.0)
    with step("[Verify] adjustmentValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'adjustmentValueLabel', '100')
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step81' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step81', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag EditingImageView_ImageView (89.8%,52.9%) → photodirector.AdjustmentsProViewController (4.7%,41.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 89.8, 52.9, AppiumBy.ACCESSIBILITY_ID, 'photodirector.AdjustmentsProViewController', 4.7, 41.8, duration=1.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step83' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step83', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag EditingImageView_ImageView (7.9%,55.0%) → photodirector.AdjustmentsProViewController (90.7%,41.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 7.9, 55.0, AppiumBy.ACCESSIBILITY_ID, 'photodirector.AdjustmentsProViewController', 90.7, 41.1, duration=1.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step85' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step85', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (65.3%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 65.3, 49.0)
    with step("[Verify] Capture '00033_adjustment_exposure_contrast_highlights_shadows_Step87' for GT comparison"):
        actions.capture_for_gt('00033_adjustment_exposure_contrast_highlights_shadows_Step87', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (50.0%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 50.0, 76.9)
    with step("[Action] Tap Discard at (79.7%, 79.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 79.7, 79.2)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
