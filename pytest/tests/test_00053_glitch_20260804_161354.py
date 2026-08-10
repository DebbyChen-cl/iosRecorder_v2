import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00053_glitch_20260804_161354")
def test_00053_glitch_20260804_161354(actions: DriverActions):
    with step("[Action] Tap Edit at (71.4%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 71.4, 48.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (83.2%, 40.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 83.2, 40.5)
    with step("[Action] Tap _AT at (12.2%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 12.2, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (57.7%, 50.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 57.7, 50.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (33.8%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 33.8, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_glitch"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_glitch', direction='left', offset_start=(0.726, 0.505), offset_end=(0.337, 0.505), velocity=491)
    with step("[Action] Tap btn_glitch at (66.7%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_glitch', 66.7, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00053_glitch_Step08' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step08', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Scroll until 7"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'styleCollectionView', AppiumBy.ACCESSIBILITY_ID, '7', direction='left', offset_start=(0.816, 0.309), offset_end=(0.304, 0.309), velocity=560)
    with step("[Action] Tap 7 at (44.6%, 16.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '7', 44.6, 16.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=418, container_h=94)
    with step("[Verify] Capture '00053_glitch_Step11' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step11', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag horizentalSlider (58.5%,53.7%) → parameterBackgroundView (25.6%,18.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'horizentalSlider', 58.5, 53.7, AppiumBy.ACCESSIBILITY_ID, 'parameterBackgroundView', 25.6, 18.3, duration=1.0)
    with step("[Action] Drag verticalSlider (61.4%,53.7%) → parameterBackgroundView (23.7%,51.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'verticalSlider', 61.4, 53.7, AppiumBy.ACCESSIBILITY_ID, 'parameterBackgroundView', 23.7, 51.7, duration=1.0)
    with step("[Verify] Capture '00053_glitch_Step14' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step14', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag horizentalSlider (11.2%,68.3%) → parameterBackgroundView (80.5%,20.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'horizentalSlider', 11.2, 68.3, AppiumBy.ACCESSIBILITY_ID, 'parameterBackgroundView', 80.5, 20.0, duration=1.0)
    with step("[Action] Drag verticalSlider (10.0%,58.5%) → parameterBackgroundView (80.0%,55.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'verticalSlider', 10.0, 58.5, AppiumBy.ACCESSIBILITY_ID, 'parameterBackgroundView', 80.0, 55.8, duration=1.0)
    with step("[Action] Drag fadeSlider (9.1%,65.9%) → parameterBackgroundView (79.1%,87.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'fadeSlider', 9.1, 65.9, AppiumBy.ACCESSIBILITY_ID, 'parameterBackgroundView', 79.1, 87.5, duration=1.0)
    with step("[Verify] Capture '00053_glitch_Step18' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step18', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Scroll until 1"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'styleCollectionView', AppiumBy.ACCESSIBILITY_ID, '1', direction='right', offset_start=(0.136, 0.521), offset_end=(0.782, 0.521), velocity=480)
    with step("[Action] Tap 1 at (70.3%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '1', 70.3, 61.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=418, container_h=94)
    with step("[Action] Drag horizentalSlider (92.1%,43.9%) → parameterBackgroundView (27.7%,18.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'horizentalSlider', 92.1, 43.9, AppiumBy.ACCESSIBILITY_ID, 'parameterBackgroundView', 27.7, 18.3, duration=1.0)
    with step("[Action] Drag verticalSlider (92.5%,61.0%) → parameterBackgroundView (26.5%,49.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'verticalSlider', 92.5, 61.0, AppiumBy.ACCESSIBILITY_ID, 'parameterBackgroundView', 26.5, 49.2, duration=1.0)
    with step("[Action] Drag fadeSlider (92.1%,58.5%) → parameterBackgroundView (25.8%,80.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'fadeSlider', 92.1, 58.5, AppiumBy.ACCESSIBILITY_ID, 'parameterBackgroundView', 25.8, 80.8, duration=1.0)
    with step("[Verify] Capture '00053_glitch_Step24' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step24', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag horizentalSlider (10.4%,56.1%) → parameterBackgroundView (81.2%,19.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'horizentalSlider', 10.4, 56.1, AppiumBy.ACCESSIBILITY_ID, 'parameterBackgroundView', 81.2, 19.2, duration=1.0)
    with step("[Action] Drag verticalSlider (9.1%,58.5%) → parameterBackgroundView (77.2%,51.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'verticalSlider', 9.1, 58.5, AppiumBy.ACCESSIBILITY_ID, 'parameterBackgroundView', 77.2, 51.7, duration=1.0)
    with step("[Action] Drag fadeSlider (9.1%,48.8%) → parameterBackgroundView (80.2%,86.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'fadeSlider', 9.1, 48.8, AppiumBy.ACCESSIBILITY_ID, 'parameterBackgroundView', 80.2, 86.7, duration=1.0)
    with step("[Verify] Capture '00053_glitch_Step28' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step28', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag fadeSlider (92.5%,46.3%) → parameterBackgroundView (27.2%,83.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'fadeSlider', 92.5, 46.3, AppiumBy.ACCESSIBILITY_ID, 'parameterBackgroundView', 27.2, 83.3, duration=1.0)
    with step("[Verify] Capture '00053_glitch_Step30' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step30', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap shapeMaskModeButton at (60.0%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskModeButton', 60.0, 45.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=687)
    with step("[Action] Tap circle_thumb at (30.9%, 34.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'circle_thumb', 30.9, 34.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='shapeMaskCollectionView', container_w=366, container_h=108)
    with step("[Verify] Capture '00053_glitch_Step33' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step33', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap drop_thumb at (77.8%, 56.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'drop_thumb', 77.8, 56.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='shapeMaskCollectionView', container_w=366, container_h=108)
    with step("[Verify] Capture '00053_glitch_Step35' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step35', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap shapeMaskInvertButton at (57.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskInvertButton', 57.5, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=687)
    with step("[Verify] Capture '00053_glitch_Step37' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step37', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Rotate //XCUIElementTypeScrollView[@name=\"editingImageView\"]/XCUIElementTypeOther[2]/XCUIElementTypeImage[2] 99.9°"):
        actions.rotate(actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[2]/XCUIElementTypeImage[2]'), rotation=99.9)
    with step("[Verify] Capture '00053_glitch_Step39' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step39', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Pinch //XCUIElementTypeScrollView[@name=\"editingImageView\"]/XCUIElementTypeOther[2]/XCUIElementTypeImage[2] scale=0.653"):
        actions.pinch(actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[2]/XCUIElementTypeImage[2]'), scale=0.653, velocity=-0.366)
    with step("[Verify] Capture '00053_glitch_Step41' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step41', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (38.8%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 38.8, 42.9)
    with step("[Verify] Capture '00053_glitch_Step43' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step43', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap shapeMaskModeButton at (35.0%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskModeButton', 35.0, 70.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=687)
    with step("[Action] Tap film_thumb at (30.9%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'film_thumb', 30.9, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='shapeMaskCollectionView', container_w=366, container_h=108)
    with step("[Action] Tap btn_ok_n at (71.4%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 71.4, 42.9)
    with step("[Verify] Capture '00053_glitch_Step47' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step47', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (77.6%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 59.2)
    with step("[Verify] Capture '00053_glitch_Step49' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step49', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (64.1%, 71.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 64.1, 71.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00053_glitch_Step51' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step51', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_glitch at (36.4%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_glitch', 36.4, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap brushModeButton at (57.5%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton', 57.5, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=687)
    with step("[Action] Drag cpSlider (43.8%,59.5%) → slider (99.0%,65.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 43.8, 59.5, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.0, 65.9, duration=1.0)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"editingImageView\"]/XCUIElementTypeOther[1] (53.4%,15.5%) → EditingImageView_ImageView (54.5%,81.1%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', 53.4, 15.5, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 54.5, 81.1, duration=1.0)
    with step("[Verify] Capture '00053_glitch_Step56' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step56', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btt_brush_n at (42.5%, 77.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 42.5, 77.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"editingImageView\"]/XCUIElementTypeOther[1] (13.0%,53.6%) → EditingImageView_ImageView (84.9%,53.2%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', 13.0, 53.6, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 84.9, 53.2, duration=1.0)
    with step("[Verify] Capture '00053_glitch_Step59' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step59', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btnInvert at (60.0%, 77.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnInvert', 60.0, 77.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=687)
    with step("[Verify] Capture '00053_glitch_Step61' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step61', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (24.5%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 24.5, 42.9)
    with step("[Verify] Capture '00053_glitch_Step63' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step63', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap brushModeButton at (42.5%, 35.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton', 42.5, 35.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=687)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"editingImageView\"]/XCUIElementTypeOther[1] (54.1%,21.6%) → EditingImageView_ImageView (55.9%,85.8%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', 54.1, 21.6, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 55.9, 85.8, duration=1.0)
    with step("[Action] Tap btn_ok_n at (73.5%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 38.8)
    with step("[Verify] Capture '00053_glitch_Step67' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step67', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (46.9%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 46.9, 53.1)
    with step("[Action] Tap btn_glitch at (63.6%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_glitch', 63.6, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap brushModeButton at (70.0%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton', 70.0, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=687)
    with step("[Action] Tap btnFilterEdge at (57.5%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnFilterEdge', 57.5, 47.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=687)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"editingImageView\"]/XCUIElementTypeOther[1] (50.3%,21.0%) → EditingImageView_ImageView (51.3%,77.7%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', 50.3, 21.0, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 51.3, 77.7, duration=1.0)
    with step("[Verify] Capture '00053_glitch_Step73' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step73', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (81.6%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 51.0)
    with step("[Verify] Capture '00053_glitch_Step75' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step75', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (81.6%, 75.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 75.5)
    with step("[Verify] Capture '00053_glitch_Step77' for GT comparison"):
        actions.capture_for_gt('00053_glitch_Step77', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (42.3%, 34.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 42.3, 34.6)
    with step("[Action] Tap Discard at (50.7%, 95.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 50.7, 95.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
