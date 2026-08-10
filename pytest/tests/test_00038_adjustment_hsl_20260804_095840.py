import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00038_adjustment_hsl_20260804_095840")
def test_00038_adjustment_hsl_20260804_095840(actions: DriverActions):
    with step("[Action] Tap Edit at (80.0%, 72.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 80.0, 72.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (80.7%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 80.7, 42.9)
    with step("[Action] Tap _AT at (7.2%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.2, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (68.5%, 43.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 68.5, 43.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Enhance at (56.0%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 56.0, 62.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Verify] Capture '00038_adjustment_hsl_Step06' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step06', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_adjustment_n at (78.8%, 78.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_adjustment_n', 78.8, 78.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Color at (73.7%, 76.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Color', 73.7, 76.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=206, container_h=46)
    with step("[Action] Tap ic_hsl at (63.6%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_hsl', 63.6, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Verify] Capture '00038_adjustment_hsl_Step10' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step10', AppiumBy.ACCESSIBILITY_ID, 'containerView', threshold=0.95)
    with step("[Action] Tap arrowButton at (67.5%, 32.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'arrowButton', 67.5, 32.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Verify] Capture '00038_adjustment_hsl_Step12' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step12', AppiumBy.ACCESSIBILITY_ID, 'containerView', threshold=0.95)
    with step("[Action] Tap arrowButton at (50.0%, 37.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'arrowButton', 50.0, 37.5)
    with step("[Verify] hueValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel', '0')
    with step("[Verify] saturationValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel', '0')
    with step("[Verify] lightnessValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lightnessValueLabel', '0')
    with step("[Action] Drag hueSlider (50.0%,57.8%) → slidersStack (5.0%,19.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 50.0, 57.8, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 5.0, 19.7, duration=1.0)
    with step("[Verify] hueValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel', '-100')
    with step("[Verify] Capture '00038_adjustment_hsl_Step19' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step19', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag hueSlider (8.2%,55.6%) → slidersStack (93.9%,18.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 8.2, 55.6, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 93.9, 18.2, duration=1.0)
    with step("[Verify] hueValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel', '100')
    with step("[Verify] Capture '00038_adjustment_hsl_Step22' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step22', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btnHSLCurveReset at (55.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset', 55.0, 52.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Verify] Capture '00038_adjustment_hsl_Step24' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step24', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag saturationSlider (50.4%,64.4%) → slidersStack (7.2%,52.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 50.4, 64.4, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 7.2, 52.3, duration=1.0)
    with step("[Verify] saturationValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel', '-100')
    with step("[Verify] Capture '00038_adjustment_hsl_Step27' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step27', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag saturationSlider (7.1%,53.3%) → slidersStack (92.4%,49.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 7.1, 53.3, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 92.4, 49.2, duration=1.0)
    with step("[Verify] saturationValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel', '100')
    with step("[Verify] Capture '00038_adjustment_hsl_Step30' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step30', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btnHSLCurveReset at (60.0%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset', 60.0, 40.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Verify] Capture '00038_adjustment_hsl_Step32' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step32', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag lightnessSlider (50.7%,55.6%) → slidersStack (0.7%,87.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'lightnessSlider', 50.7, 55.6, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 0.7, 87.1, duration=1.0)
    with step("[Verify] lightnessValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lightnessValueLabel', '-100')
    with step("[Verify] Capture '00038_adjustment_hsl_Step35' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step35', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag lightnessSlider (7.8%,48.9%) → slidersStack (93.2%,84.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'lightnessSlider', 7.8, 48.9, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 93.2, 84.8, duration=1.0)
    with step("[Verify] lightnessValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lightnessValueLabel', '100')
    with step("[Verify] Capture '00038_adjustment_hsl_Step38' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step38', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btnHSLCurveReset at (30.0%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset', 30.0, 55.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Verify] Capture '00038_adjustment_hsl_Step40' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step40', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"HSLColorCollectionViewCell-2\"]/XCUIElementTypeOther/XCUIElementTypeImage[2] at (80.0%, 70.8%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="HSLColorCollectionViewCell-2"]/XCUIElementTypeOther/XCUIElementTypeImage[2]', 80.0, 70.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='colorCollectionView', container_w=430, container_h=44)
    with step("[Verify] Capture '00038_adjustment_hsl_Step42' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step42', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag hueSlider (51.4%,51.1%) → slidersStack (4.0%,15.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 51.4, 51.1, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 4.0, 15.2, duration=1.0)
    with step("[Verify] hueValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel', '-100')
    with step("[Verify] Capture '00038_adjustment_hsl_Step45' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step45', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag hueSlider (9.6%,60.0%) → slidersStack (95.0%,17.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 9.6, 60.0, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 95.0, 17.4, duration=1.0)
    with step("[Verify] hueValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel', '100')
    with step("[Verify] Capture '00038_adjustment_hsl_Step48' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step48', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btnHSLCurveReset at (60.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset', 60.0, 52.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Verify] Capture '00038_adjustment_hsl_Step50' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step50', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag saturationSlider (51.1%,55.6%) → slidersStack (4.0%,49.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 51.1, 55.6, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 4.0, 49.2, duration=1.0)
    with step("[Verify] saturationValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel', '-100')
    with step("[Action] Drag saturationSlider (8.5%,64.4%) → slidersStack (96.8%,54.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 8.5, 64.4, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 96.8, 54.5, duration=1.0)
    with step("[Verify] saturationValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel', '100')
    with step("[Verify] Capture '00038_adjustment_hsl_Step55' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step55', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btnHSLCurveReset at (70.0%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset', 70.0, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Verify] Capture '00038_adjustment_hsl_Step57' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step57', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag lightnessSlider (50.7%,64.4%) → slidersStack (3.6%,87.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'lightnessSlider', 50.7, 64.4, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 3.6, 87.1, duration=1.0)
    with step("[Verify] lightnessValueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lightnessValueLabel', '-100')
    with step("[Verify] Capture '00038_adjustment_hsl_Step60' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step60', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag lightnessSlider (6.0%,51.1%) → slidersStack (92.1%,80.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'lightnessSlider', 6.0, 51.1, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 92.1, 80.3, duration=1.0)
    with step("[Verify] lightnessValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lightnessValueLabel', '100')
    with step("[Verify] Capture '00038_adjustment_hsl_Step63' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step63', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btnHSLCurveReset at (65.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset', 65.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Verify] Capture '00038_adjustment_hsl_Step65' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step65', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag hueSlider (50.7%,51.1%) → slidersStack (5.4%,18.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 50.7, 51.1, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 5.4, 18.9, duration=1.0)
    with step("[Action] Drag saturationSlider (50.0%,48.9%) → slidersStack (5.8%,53.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 50.0, 48.9, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 5.8, 53.8, duration=1.0)
    with step("[Action] Drag lightnessSlider (51.1%,64.4%) → slidersStack (4.7%,89.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'lightnessSlider', 51.1, 64.4, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 4.7, 89.4, duration=1.0)
    with step("[Action] Tap btn_cancel_n at (38.8%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 38.8, 42.9)
    with step("[Verify] Capture '00038_adjustment_hsl_Step70' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step70', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_adjustment_n at (66.7%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_adjustment_n', 66.7, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Color at (36.8%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Color', 36.8, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=206, container_h=46)
    with step("[Action] Tap ic_hsl at (33.3%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_hsl', 33.3, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag hueSlider (51.1%,57.8%) → slidersStack (7.9%,18.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 51.1, 57.8, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 7.9, 18.9, duration=1.0)
    with step("[Action] Drag saturationSlider (49.3%,48.9%) → slidersStack (6.8%,48.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 49.3, 48.9, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 6.8, 48.5, duration=1.0)
    with step("[Action] Drag lightnessSlider (51.8%,53.3%) → slidersStack (7.6%,85.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'lightnessSlider', 51.8, 53.3, AppiumBy.ACCESSIBILITY_ID, 'slidersStack', 7.6, 85.6, duration=1.0)
    with step("[Action] Tap btn_ok_n at (73.5%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 38.8)
    with step("[Verify] Capture '00038_adjustment_hsl_Step78' for GT comparison"):
        actions.capture_for_gt('00038_adjustment_hsl_Step78', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (38.5%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 38.5, 73.1)
    with step("[Action] Tap Discard at (55.1%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 55.1, 83.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
