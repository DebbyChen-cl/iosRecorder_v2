import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00063_skin_smoother_20260804_175126")
def test_00063_skin_smoother_20260804_175126(actions: DriverActions):
    with step("[Action] Tap Edit at (82.9%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 82.9, 52.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (86.8%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 86.8, 57.1)
    with step("[Action] Tap _AT at (7.9%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (71.5%, 33.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 71.5, 33.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (62.2%, 71.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 62.2, 71.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until ic_beautify"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', direction='left', offset_start=(0.598, 0.361), offset_end=(0.309, 0.361), velocity=82)
    with step("[Action] Tap ic_beautify at (79.4%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 79.4, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_skin_smooth at (60.6%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_skin_smooth', 60.6, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Drag EditingImageView_ImageView (47.5%,17.3%) → photodirector.SkinSmoothProViewController (55.8%,30.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 47.5, 17.3, AppiumBy.ACCESSIBILITY_ID, 'photodirector.SkinSmoothProViewController', 55.8, 30.6, duration=1.0)
    with step("[Verify] Capture '00063_skin_smoother_Step10' for GT comparison"):
        actions.capture_for_gt('00063_skin_smoother_Step10', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (61.2%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 61.2, 34.7)
    with step("[Verify] Capture '00063_skin_smoother_Step12' for GT comparison"):
        actions.capture_for_gt('00063_skin_smoother_Step12', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_redo at (67.3%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 67.3, 40.8)
    with step("[Verify] Capture '00063_skin_smoother_Step14' for GT comparison"):
        actions.capture_for_gt('00063_skin_smoother_Step14', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap eraserButton at (75.0%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'eraserButton', 75.0, 66.7)
    with step("[Action] Drag EditingImageView_ImageView (65.5%,17.5%) → photodirector.SkinSmoothProViewController (42.3%,28.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 65.5, 17.5, AppiumBy.ACCESSIBILITY_ID, 'photodirector.SkinSmoothProViewController', 42.3, 28.8, duration=1.0)
    with step("[Verify] Capture '00063_skin_smoother_Step17' for GT comparison"):
        actions.capture_for_gt('00063_skin_smoother_Step17', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (63.3%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 63.3, 49.0)
    with step("[Action] Tap btn_ok_n at (85.7%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 85.7, 46.9)
    with step("[Verify] Capture '00063_skin_smoother_Step20' for GT comparison"):
        actions.capture_for_gt('00063_skin_smoother_Step20', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (81.6%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 81.6, 38.8)
    with step("[Verify] Capture '00063_skin_smoother_Step22' for GT comparison"):
        actions.capture_for_gt('00063_skin_smoother_Step22', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_skin_smooth at (63.6%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_skin_smooth', 63.6, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_cancel_n at (34.7%, 63.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 34.7, 63.3)
    with step("[Verify] Capture '00063_skin_smoother_Step25' for GT comparison"):
        actions.capture_for_gt('00063_skin_smoother_Step25', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_skin_smooth at (75.8%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_skin_smooth', 75.8, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Drag EditingImageView_ImageView (63.2%,15.6%) → photodirector.SkinSmoothProViewController (42.3%,30.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 63.2, 15.6, AppiumBy.ACCESSIBILITY_ID, 'photodirector.SkinSmoothProViewController', 42.3, 30.3, duration=1.0)
    with step("[Action] Tap btn_ok_n at (81.6%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 57.1)
    with step("[Action] Tap btn_ok_n at (83.7%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 83.7, 49.0)
    with step("[Verify] Capture '00063_skin_smoother_Step30' for GT comparison"):
        actions.capture_for_gt('00063_skin_smoother_Step30', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (30.8%, 34.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 30.8, 34.6)
    with step("[Action] Tap Discard at (46.4%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 46.4, 58.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
