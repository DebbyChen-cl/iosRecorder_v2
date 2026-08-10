import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00118_main_06_01_01c_2_20260809_151125")
def test_00118_main_06_01_01c_2_20260809_151125(actions: DriverActions):
    with step("[Action] Tap Edit at (71.4%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 71.4, 48.0)
    with step("[Action] Tap btnAlbum at (68.0%, 59.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 68.0, 59.5)
    with step("[Action] Tap _AT at (9.3%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.3, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (26.2%, 66.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 26.2, 66.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (57.8%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 57.8, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Cutout"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Cutout', direction='left', offset_start=(0.614, 0.392), offset_end=(0.428, 0.392), velocity=266)
    with step("[Action] Tap Cutout at (48.6%, 26.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cutout', 48.6, 26.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Auto at (64.5%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Auto', 64.5, 63.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step09' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step09', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap Cutout at (39.6%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cutout', 39.6, 61.9)
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step11' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step11', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Tap Stroke at (47.8%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Stroke', 47.8, 33.3)
    with step("[Action] Tap stroke_thumb_6 at (60.6%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_6', 60.6, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='strokeCollection', container_w=337, container_h=71)
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step14' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step14', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"ColorSelectionViewColorCell-4\"]/XCUIElementTypeOther at (74.1%, 46.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="ColorSelectionViewColorCell-4"]/XCUIElementTypeOther', 74.1, 46.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='colorCollectionView', container_w=430, container_h=40)
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step16' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step16', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Drag cpSlider (50.6%,53.7%) → //XCUIElementTypeOther[@name=\"cutout_with_design\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther (82.8%,52.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 50.6, 53.7, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther', 82.8, 52.3, duration=1.0)
    with step("[Verify] valueLabel text equals '20'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '20')
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step19' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step19', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Drag cpSlider (94.7%,48.8%) → slider (1.8%,60.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 94.7, 48.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.8, 60.0, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step22' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step22', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Tap stroke_thumb_2 at (60.6%, 85.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_2', 60.6, 85.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='strokeCollection', container_w=337, container_h=71)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"ColorSelectionViewColorCell-10\"]/XCUIElementTypeOther at (14.8%, 32.1%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="ColorSelectionViewColorCell-10"]/XCUIElementTypeOther', 14.8, 32.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='colorCollectionView', container_w=430, container_h=40)
    with step("[Action] Drag cpSlider (41.5%,58.5%) → //XCUIElementTypeOther[@name=\"cutout_with_design\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther (82.3%,56.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 41.5, 58.5, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther', 82.3, 56.8, duration=1.0)
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step26' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step26', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Tap stroke_thumb_3 at (66.7%, 78.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_3', 66.7, 78.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='strokeCollection', container_w=337, container_h=71)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"ColorSelectionViewColorCell-6\"]/XCUIElementTypeOther at (74.1%, 53.6%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="ColorSelectionViewColorCell-6"]/XCUIElementTypeOther', 74.1, 53.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='colorCollectionView', container_w=430, container_h=40)
    with step("[Action] Drag cpSlider (50.6%,53.7%) → valueLabel (10.8%,65.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 50.6, 53.7, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 10.8, 65.0, duration=1.0)
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step30' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step30', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Tap stroke_thumb_1 at (59.7%, 64.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_1', 59.7, 64.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='strokeCollection', container_w=337, container_h=71)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"ColorSelectionViewColorCell-6\"]/XCUIElementTypeOther at (44.4%, 71.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="ColorSelectionViewColorCell-6"]/XCUIElementTypeOther', 44.4, 71.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='colorCollectionView', container_w=430, container_h=40)
    with step("[Action] Drag cpSlider (41.2%,53.7%) → valueLabel (3.1%,45.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 41.2, 53.7, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 3.1, 45.0, duration=1.0)
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step34' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step34', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Tap stroke_thumb_4 at (55.2%, 39.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_4', 55.2, 39.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='strokeCollection', container_w=337, container_h=71)
    with step("[Action] Drag centerSlider (21.3%,58.5%) → slider (98.8%,55.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 21.3, 58.5, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.8, 55.0, duration=1.0)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"ColorSelectionViewColorCell-8\"]/XCUIElementTypeOther at (66.7%, 64.3%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="ColorSelectionViewColorCell-8"]/XCUIElementTypeOther', 66.7, 64.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='colorCollectionView', container_w=430, container_h=40)
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step38' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step38', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Tap stroke_thumb_7 at (53.7%, 78.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_7', 53.7, 78.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='strokeCollection', container_w=337, container_h=71)
    with step("[Action] Drag cpSlider (32.2%,46.3%) → slider (98.8%,45.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 32.2, 46.3, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.8, 45.0, duration=1.0)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"ColorSelectionViewColorCell-9\"]/XCUIElementTypeOther at (55.6%, 71.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="ColorSelectionViewColorCell-9"]/XCUIElementTypeOther', 55.6, 71.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='colorCollectionView', container_w=430, container_h=40)
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step42' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step42', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Tap stroke_thumb_5 at (39.4%, 66.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_5', 39.4, 66.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='strokeCollection', container_w=337, container_h=71)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"ColorSelectionViewColorCell-8\"]/XCUIElementTypeOther at (77.8%, 71.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="ColorSelectionViewColorCell-8"]/XCUIElementTypeOther', 77.8, 71.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='colorCollectionView', container_w=430, container_h=40)
    with step("[Action] Drag cpSlider (36.5%,53.7%) → slider (99.1%,55.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 36.5, 53.7, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.1, 55.0, duration=1.0)
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step46' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step46', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Tap btn edit n at (67.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn edit n', 67.5, 50.0)
    with step("[Action] Tap btt_eraser_n at (60.0%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 60.0, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag cpSlider (23.2%,56.0%) → slider (96.3%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 23.2, 56.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 96.3, 53.1, duration=1.0)
    with step("[Action] Drag instanceSegmentationGestureReceiverView (49.4%,13.9%) → instanceSegmentationGestureReceiverView (73.3%,90.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 49.4, 13.9, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 73.3, 90.9, duration=1.0)
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step51' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step51', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Drag cpSlider (95.2%,58.0%) → brushSizeSliderView (24.2%,46.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 95.2, 58.0, AppiumBy.ACCESSIBILITY_ID, 'brushSizeSliderView', 24.2, 46.9, duration=1.0)
    with step("[Action] Tap Brush at (53.9%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Brush', 53.9, 45.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag instanceSegmentationGestureReceiverView (48.3%,15.0%) → instanceSegmentationGestureReceiverView (72.9%,91.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 48.3, 15.0, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 72.9, 91.7, duration=1.0)
    with step("[Verify] Capture '00118_main_06_01_01c_2_Step55' for GT comparison"):
        actions.capture_for_gt('00118_main_06_01_01c_2_Step55', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap Cutout at (81.1%, 90.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cutout', 81.1, 90.5)
    with step("[Action] Tap stroke_thumb_7 at (68.2%, 53.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_7', 68.2, 53.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='strokeCollection', container_w=337, container_h=71)
    with step("[Action] Tap btn_ok_n at (87.8%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 87.8, 42.9)
    with step("[Action] Tap btnClose at (54.8%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 54.8, 54.8)
    with step("[Action] Tap stroke_thumb_5 at (40.9%, 39.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_5', 40.9, 39.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='strokeCollection', container_w=337, container_h=71)
    with step("[Action] Tap btn_ok_n at (85.7%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 85.7, 44.9)
    with step("[Action] Tap btnClose at (54.8%, 54.8%) if exist"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose'):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 54.8, 54.8)
    with step("[Action] Tap navHomeButton at (65.9%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton', 65.9, 48.9)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
