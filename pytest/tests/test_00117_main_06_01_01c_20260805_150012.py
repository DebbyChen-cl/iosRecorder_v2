import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00117_main_06_01_01c_20260805_150012")
def test_00117_main_06_01_01c_20260805_150012(actions: DriverActions):
    with step("[Action] Tap Edit at (42.9%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 42.9, 64.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (72.1%, 69.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 72.1, 69.0)
    with step("[Action] Tap _AT at (8.2%, 40.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.2, 40.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (30.8%, 73.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 30.8, 73.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (40.0%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 40.0, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_cutout at (69.7%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_cutout', 69.7, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Auto at (57.9%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Auto', 57.9, 54.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] Capture '00117_main_06_01_01c_Step08' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step08', AppiumBy.ACCESSIBILITY_ID, 'CLViewContainer', threshold=0.95)
    with step("[Action] Tap btn_reset_n at (64.0%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n', 64.0, 34.7)
    with step("[Verify] Capture '00117_main_06_01_01c_Step10' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step10', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap ic_box at (65.0%, 72.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_box', 65.0, 72.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag instanceSegmentationGestureReceiverView (20.9%,14.2%) → instanceSegmentationGestureReceiverView (84.9%,93.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 20.9, 14.2, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 84.9, 93.7, duration=1.0)
    with step("[Verify] Capture '00117_main_06_01_01c_Step13' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step13', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap btn_reset_n at (66.0%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n', 66.0, 46.9)
    with step("[Verify] Capture '00117_main_06_01_01c_Step15' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step15', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap ic_circle at (55.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_circle', 55.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Paint on instanceSegmentationGestureReceiverView (34 points)"):
        actions.paint_in_element(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', [(53.1, 15.0, 0), (47.6, 15.6, 59), (41.3, 17.0, 109), (35.7, 18.7, 175), (31.3, 20.9, 209), (27.1, 23.8, 242), (23.4, 27.0, 275), (17.2, 34.2, 342), (12.5, 44.0, 425), (10.7, 50.1, 475), (10.4, 68.3, 592), (10.4, 70.2, 609), (11.6, 73.1, 642), (16.9, 79.9, 792), (24.8, 85.6, 925), (33.9, 90.7, 1075), (42.5, 93.2, 1159), (50.6, 94.4, 1225), (64.0, 94.3, 1375), (69.4, 93.5, 1442), (79.6, 90.6, 1509), (86.3, 89.2, 1575), (88.9, 87.8, 1625), (92.1, 84.2, 1675), (94.2, 81.1, 1709), (96.1, 76.5, 1742), (96.5, 74.0, 1759), (96.5, 62.3, 1825), (93.5, 54.4, 1875), (88.9, 47.6, 1942), (77.3, 35.2, 2109), (68.2, 26.6, 2242), (59.6, 15.8, 2442), (52.2, 15.9, 2675)], duration_ms=2757)
    with step("[Verify] Capture '00117_main_06_01_01c_Step18' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step18', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap btn_reset_n at (60.0%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n', 60.0, 46.9)
    with step("[Verify] Capture '00117_main_06_01_01c_Step20' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step20', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap btt_brush_n at (65.0%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 65.0, 45.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag instanceSegmentationGestureReceiverView (50.8%,12.2%) → instanceSegmentationGestureReceiverView (50.8%,87.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 50.8, 12.2, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 50.8, 87.8, duration=1.0)
    with step("[Verify] Capture '00117_main_06_01_01c_Step23' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step23', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Drag cpSlider (26.2%,52.0%) → slider (3.7%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 26.2, 52.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 3.7, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '8'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '8')
    with step("[Action] Drag instanceSegmentationGestureReceiverView (35.3%,14.4%) → instanceSegmentationGestureReceiverView (35.7%,89.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 35.3, 14.4, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 35.7, 89.5, duration=1.0)
    with step("[Verify] Capture '00117_main_06_01_01c_Step27' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step27', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Drag cpSlider (7.7%,56.0%) → slider (94.8%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.7, 56.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 94.8, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag instanceSegmentationGestureReceiverView (77.3%,11.4%) → instanceSegmentationGestureReceiverView (77.5%,88.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 77.3, 11.4, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 77.5, 88.3, duration=1.0)
    with step("[Verify] Capture '00117_main_06_01_01c_Step31' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step31', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap ic_undo at (44.0%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 44.0, 44.9)
    with step("[Verify] Capture '00117_main_06_01_01c_Step33' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step33', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap ic_redo at (72.0%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 72.0, 30.6)
    with step("[Verify] Capture '00117_main_06_01_01c_Step35' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step35', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap Cutout at (62.3%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cutout', 62.3, 47.6)
    with step("[Action] Tap btn edit n at (37.5%, 42.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn edit n', 37.5, 42.5)
    with step("[Action] Tap btt_eraser_n at (65.0%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 65.0, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag cpSlider (24.0%,58.0%) → slider (3.4%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 24.0, 58.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 3.4, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '8'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '8')
    with step("[Action] Drag instanceSegmentationGestureReceiverView (11.4%,41.6%) → Vertical scroll bar, 1 page (33.3%,42.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 11.4, 41.6, AppiumBy.ACCESSIBILITY_ID, 'Vertical scroll bar, 1 page', 33.3, 42.4, duration=1.0)
    with step("[Verify] Capture '00117_main_06_01_01c_Step42' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step42', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Drag cpSlider (8.1%,44.0%) → valueLabel (3.1%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 8.1, 44.0, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 3.1, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag instanceSegmentationGestureReceiverView (4.4%,76.2%) → instanceSegmentationGestureReceiverView (89.6%,77.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 4.4, 76.2, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 89.6, 77.0, duration=1.0)
    with step("[Verify] Capture '00117_main_06_01_01c_Step46' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step46', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap ic_foreground at (62.5%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_foreground', 62.5, 65.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap Cutout at (56.6%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cutout', 56.6, 66.7)
    with step("[Verify] Capture '00117_main_06_01_01c_Step49' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step49', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Tap btn edit n at (40.0%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn edit n', 40.0, 47.5)
    with step("[Action] Tap btt_eraser_n at (55.0%, 77.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 55.0, 77.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag instanceSegmentationGestureReceiverView (23.7%,22.7%) → instanceSegmentationGestureReceiverView (73.3%,87.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 23.7, 22.7, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 73.3, 87.0, duration=1.0)
    with step("[Action] Tap Cutout at (50.9%, 81.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cutout', 50.9, 81.0)
    with step("[Verify] Capture '00117_main_06_01_01c_Step54' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step54', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (8.2%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 8.2, 42.9)
    with step("[Action] Tap Discard at (52.1%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 52.1, 62.5)
    with step("[Action] Tap ic_cutout at (42.4%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_cutout', 42.4, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_foreground at (45.0%, 32.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_foreground', 45.0, 32.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap Cutout at (47.2%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cutout', 47.2, 47.6)
    with step("[Action] Tap CMS- at (50.0%, 41.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-', 50.0, 41.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]', container_w=408, container_h=71)
    with step("[Verify] Capture '00117_main_06_01_01c_Step61' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step61', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (26.5%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 26.5, 34.7)
    with step("[Action] Tap Discard at (42.3%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 42.3, 33.3)
    with step("[Action] Tap ic_cutout at (60.6%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_cutout', 60.6, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_foreground at (70.0%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_foreground', 70.0, 57.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap Cutout at (69.8%, 38.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cutout', 69.8, 38.1)
    with step("[Action] Tap pickedColorView at (51.6%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'pickedColorView', 51.6, 44.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]', container_w=408, container_h=71)
    with step("[Action] Tap Done at (52.3%, 39.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Done', 52.3, 39.1)
    with step("[Verify] Capture '00117_main_06_01_01c_Step69' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step69', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (36.7%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 36.7, 46.9)
    with step("[Action] Tap Discard at (71.8%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 71.8, 58.3)
    with step("[Action] Tap ic_cutout at (54.5%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_cutout', 54.5, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_foreground at (70.0%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_foreground', 70.0, 67.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap Cutout at (77.4%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cutout', 77.4, 42.9)
    with step("[Action] Tap btn_addimg_n at (75.0%, 31.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', 75.0, 31.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]', container_w=408, container_h=71)
    with step("[Action] Tap btnAlbum at (74.6%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 74.6, 61.9)
    with step("[Action] Tap BG at (6.8%, 31.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'BG', 6.8, 31.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-4 at (49.2%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4', 49.2, 46.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture '00117_main_06_01_01c_Step79' for GT comparison"):
        actions.capture_for_gt('00117_main_06_01_01c_Step79', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (34.7%, 22.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 34.7, 22.4)
    with step("[Action] Tap Discard at (67.6%, 45.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 67.6, 45.8)
    with step("[Action] Tap ic_cutout at (30.3%, 39.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_cutout', 30.3, 39.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_foreground at (40.0%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_foreground', 40.0, 70.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap Cutout at (86.8%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cutout', 86.8, 71.4)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]')
    with step("[Action] Tap btn_addimg_n at (60.0%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', 60.0, 58.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]', container_w=408, container_h=71)
    with step("[Action] Tap btnCamera at (62.5%, 43.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnCamera', 62.5, 43.9)
    with step("[Action] Tap PhotoCapture at (56.2%, 61.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoCapture', 56.2, 61.3)
    with step("[Action] Tap Use Photo at (40.0%, 60.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Use Photo', 40.0, 60.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]', expected_result='different', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (93.9%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 93.9, 34.7)
    with step("[Action] Tap homeButton at (65.4%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 69.2)
    with step("[Action] Tap Discard at (58.0%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 58.0, 70.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
