import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00055_main_05_04a_03_20260804_163022")
def test_00055_main_05_04a_03_20260804_163022(actions: DriverActions):
    with step("[Action] Tap Edit at (60.0%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 60.0, 52.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (77.2%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 77.2, 54.8)
    with step("[Action] Tap _AT at (7.5%, 31.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.5, 31.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (30.0%, 36.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 30.0, 36.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (64.4%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 64.4, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until ic_mosaic"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_mosaic', direction='left', offset_start=(0.8, 0.557), offset_end=(0.219, 0.557), velocity=440)
    with step("[Action] Tap ic_mosaic at (47.1%, 84.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_mosaic', 47.1, 84.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Manual at (70.7%, 60.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Manual', 70.7, 60.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=110, container_h=46)
    with step("[Verify] Capture '00055_main_05_04a_03_Step09' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step09', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag cpSlider (45.8%,50.0%) → EditingImageView_ImageView (29.2%,79.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 45.8, 50.0, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 29.2, 79.5, duration=1.0)
    with step("[Action] Drag cpSlider (33.9%,56.0%) → EditingImageView_ImageView (24.1%,87.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 33.9, 56.0, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 24.1, 87.4, duration=1.0)
    with step("[Verify] Capture '00055_main_05_04a_03_Step12' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step12', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag cpSlider (10.0%,60.0%) → EditingImageView_ImageView (90.0%,79.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 10.0, 60.0, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 90.0, 79.5, duration=1.0)
    with step("[Action] Drag cpSlider (8.5%,50.0%) → valueLabel (0.0%,61.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 8.5, 50.0, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 0.0, 61.2, duration=1.0)
    with step("[Action] Drag cpSlider (7.7%,58.0%) → EditingImageView_ImageView (89.7%,96.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.7, 58.0, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 89.7, 96.1, duration=1.0)
    with step("[Verify] Capture '00055_main_05_04a_03_Step16' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step16', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (75.5%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 32.7)
    with step("[Verify] Capture '00055_main_05_04a_03_Step18' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step18', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (61.5%, 59.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 61.5, 59.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00055_main_05_04a_03_Step20' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step20', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_mosaic at (41.2%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_mosaic', 41.2, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Manual at (67.2%, 39.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Manual', 67.2, 39.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=110, container_h=46)
    with step("[Action] Drag cpSlider (45.4%,52.0%) → EditingImageView_ImageView (22.3%,78.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 45.4, 52.0, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 22.3, 78.5, duration=1.0)
    with step("[Action] Drag EditingImageView_ImageView (51.0%,9.6%) → middleView (49.1%,65.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 51.0, 9.6, AppiumBy.ACCESSIBILITY_ID, 'middleView', 49.1, 65.1, duration=1.0)
    with step("[Verify] Capture '00055_main_05_04a_03_Step25' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step25', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag cpSlider (7.0%,54.0%) → EditingImageView_ImageView (88.2%,79.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.0, 54.0, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 88.2, 79.2, duration=1.0)
    with step("[Action] Drag EditingImageView_ImageView (5.4%,50.5%) → middleView (83.7%,50.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 5.4, 50.5, AppiumBy.ACCESSIBILITY_ID, 'middleView', 83.7, 50.4, duration=1.0)
    with step("[Verify] Capture '00055_main_05_04a_03_Step28' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step28', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (48.0%, 63.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 48.0, 63.3)
    with step("[Verify] Capture '00055_main_05_04a_03_Step30' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step30', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_reset_n at (46.0%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n', 46.0, 26.5)
    with step("[Verify] Capture '00055_main_05_04a_03_Step32' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step32', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap mosaic_rectangle at (39.4%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'mosaic_rectangle', 39.4, 75.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='mosaicStyleCollectionViewCollectionView', container_w=430, container_h=88)
    with step("[Action] Drag EditingImageView_ImageView (56.4%,19.5%) → middleView (55.1%,30.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 56.4, 19.5, AppiumBy.ACCESSIBILITY_ID, 'middleView', 55.1, 30.8, duration=1.0)
    with step("[Action] Tap ic_undo at (56.0%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 56.0, 32.7)
    with step("[Verify] Capture '00055_main_05_04a_03_Step36' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step36', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_redo at (52.0%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 52.0, 34.7)
    with step("[Verify] Capture '00055_main_05_04a_03_Step38' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step38', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btt_eraser_n at (37.5%, 87.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 37.5, 87.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushMenuView"]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag cpSlider (45.4%,58.0%) → EditingImageView_ImageView (24.9%,78.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 45.4, 58.0, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 24.9, 78.7, duration=1.0)
    with step("[Action] Drag EditingImageView_ImageView (27.7%,24.9%) → middleView (78.6%,24.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 27.7, 24.9, AppiumBy.ACCESSIBILITY_ID, 'middleView', 78.6, 24.4, duration=1.0)
    with step("[Verify] Capture '00055_main_05_04a_03_Step42' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step42', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag cpSlider (7.4%,58.0%) → EditingImageView_ImageView (87.7%,79.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.4, 58.0, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 87.7, 79.2, duration=1.0)
    with step("[Action] Drag EditingImageView_ImageView (54.6%,11.6%) → middleView (53.7%,46.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 54.6, 11.6, AppiumBy.ACCESSIBILITY_ID, 'middleView', 53.7, 46.0, duration=1.0)
    with step("[Verify] Capture '00055_main_05_04a_03_Step45' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step45', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (75.5%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 38.8)
    with step("[Verify] Capture '00055_main_05_04a_03_Step47' for GT comparison"):
        actions.capture_for_gt('00055_main_05_04a_03_Step47', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (76.9%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 76.9, 57.7)
    with step("[Action] Tap Discard at (53.6%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 53.6, 41.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
