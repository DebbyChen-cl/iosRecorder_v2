import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00027_removal_auto_20260808_160324")
def test_00027_removal_auto_20260808_160324(actions: DriverActions):
    with step("[Action] Tap Edit at (60.0%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 60.0, 56.0)
    with step("[Action] Tap btnAlbum at (74.1%, 64.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 74.1, 64.3)
    with step("[Action] Tap _AT at (15.4%, 40.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 15.4, 40.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (43.1%, 55.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 43.1, 55.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (75.6%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 75.6, 62.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until icon_removal"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'icon_removal', direction='right', offset_start=(0.033, 0.433), offset_end=(0.34, 0.433), velocity=360)
    with step("[Action] Tap icon_removal at (60.6%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_removal', 60.6, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap checkbox_uncheck at (42.3%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'checkbox_uncheck', 42.3, 48.1)
    with step("[Action] Tap Try First at (68.6%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try First', 68.6, 33.3)
    with step("[Action] Tap ic_box at (72.5%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_box', 72.5, 45.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="bottomBar"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag EditingImageView_ImageView (39.8%,15.4%) → backgroundView (72.1%,53.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 39.8, 15.4, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 72.1, 53.8, duration=1.0)
    with step("[Verify] Capture '00027_removal_auto_Step10' for GT comparison"):
        actions.capture_for_gt('00027_removal_auto_Step10', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap undoButton at (55.0%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 55.0, 47.5)
    with step("[Verify] Capture '00027_removal_auto_Step12' for GT comparison"):
        actions.capture_for_gt('00027_removal_auto_Step12', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap redoButton at (40.0%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'redoButton', 40.0, 55.0)
    with step("[Verify] Capture '00027_removal_auto_Step14' for GT comparison"):
        actions.capture_for_gt('00027_removal_auto_Step14', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Remove at (24.2%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Remove', 24.2, 56.5)
    with step("[Verify] Capture '00027_removal_auto_Step16' for GT comparison"):
        actions.capture_for_gt('00027_removal_auto_Step16', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap undoButton at (30.0%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 30.0, 57.5)
    with step("[Verify] Capture '00027_removal_auto_Step18' for GT comparison"):
        actions.capture_for_gt('00027_removal_auto_Step18', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap redoButton at (25.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'redoButton', 25.0, 50.0)
    with step("[Verify] Capture '00027_removal_auto_Step20' for GT comparison"):
        actions.capture_for_gt('00027_removal_auto_Step20', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap undoButton at (45.0%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 45.0, 55.0)
    with step("[Action] Tap resetButton at (50.0%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'resetButton', 50.0, 65.4)
    with step("[Verify] Capture '00027_removal_auto_Step23' for GT comparison"):
        actions.capture_for_gt('00027_removal_auto_Step23', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_circle at (40.0%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_circle', 40.0, 40.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="bottomBar"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Paint on EditingImageView_ImageView (25 points)"):
        actions.paint_in_element(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', [(51.6, 14.3, 0), (47.4, 16.4, 138), (38.8, 26.8, 188), (34.0, 35.0, 221), (32.6, 38.6, 237), (31.9, 41.1, 254), (31.2, 63.2, 388), (31.2, 76.1, 454), (32.3, 88.2, 538), (37.4, 97.1, 754), (42.8, 100.0, 854), (51.4, 100.0, 954), (57.0, 99.3, 1004), (62.6, 96.4, 1103), (65.1, 95.7, 1154), (68.1, 92.9, 1204), (71.2, 88.2, 1238), (73.3, 72.5, 1337), (73.3, 40.7, 1588), (71.4, 31.1, 1653), (69.3, 26.4, 1688), (67.2, 22.9, 1721), (66.0, 19.3, 1754), (61.6, 13.9, 1871), (51.6, 12.1, 2317)], duration_ms=2316)
    with step("[Verify] Capture '00027_removal_auto_Step26' for GT comparison"):
        actions.capture_for_gt('00027_removal_auto_Step26', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Remove at (40.9%, 43.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Remove', 40.9, 43.5)
    with step("[Verify] Capture '00027_removal_auto_Step28' for GT comparison"):
        actions.capture_for_gt('00027_removal_auto_Step28', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap undoButton at (27.5%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 27.5, 67.5)
    with step("[Action] Tap resetButton at (61.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'resetButton', 61.5, 50.0)
    with step("[Action] Tap ic_swipe at (35.0%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_swipe', 35.0, 55.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="bottomBar"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag EditingImageView_ImageView (55.3%,17.9%) → backgroundView (56.3%,52.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 55.3, 17.9, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 56.3, 52.3, duration=1.0)
    with step("[Verify] Capture '00027_removal_auto_Step33' for GT comparison"):
        actions.capture_for_gt('00027_removal_auto_Step33', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Remove at (0.0%, 91.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Remove', 0.0, 91.3)
    with step("[Verify] Capture '00027_removal_auto_Step35' for GT comparison"):
        actions.capture_for_gt('00027_removal_auto_Step35', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (75.5%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 38.8)
    with step("[Action] Tap btnClose at (51.6%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 51.6, 48.4)
    with step("[Action] Tap btn_cancel_n at (24.5%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 24.5, 28.6)
    with step("[Action] Tap homeButton at (53.8%, 34.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 53.8, 34.6)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
