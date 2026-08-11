import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00109_main_06_01_01_n3_20260808_212507")
def test_00109_main_06_01_01_n3_20260808_212507(actions: DriverActions):
    with step("[Action] Tap Edit at (54.3%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 54.3, 48.0)
    with step("[Action] Tap btnAlbum at (74.1%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 74.1, 61.9)
    with step("[Action] Tap _AT at (13.3%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 13.3, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (52.3%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 52.3, 40.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (66.7%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 66.7, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Text"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Text', direction='left', offset_start=(0.286, 0.361), offset_end=(0.177, 0.361), velocity=55)
    with step("[Action] Tap Text at (55.6%, 26.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text', 55.6, 26.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Text Bubble at (70.1%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text Bubble', 70.1, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap imageView at (50.2%, 49.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 50.2, 49.6)
    with step("[Action] Tap A at (51.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'A', 51.2, 50.0)
    with step("[Action] Tap a at (51.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'a', 51.2, 50.0)
    with step("[Action] Tap a at (51.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'a', 51.2, 50.0)
    with step("[Action] Tap Return at (54.2%, 35.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Return', 54.2, 35.7)
    with step("[Action] Tap A at (53.5%, 44.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'A', 53.5, 44.6)
    with step("[Action] Tap applyButton at (61.4%, 43.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'applyButton', 61.4, 43.2)
    with step("[Verify] Capture '00109_main_06_01_01_n3_Step16' for GT comparison"):
        actions.capture_for_gt('00109_main_06_01_01_n3_Step16', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap Format at (41.3%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Format', 41.3, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textBubbleBottomBarCollectionView', container_w=430, container_h=71)
    with step("[Verify] Capture '00109_main_06_01_01_n3_Step18' for GT comparison"):
        actions.capture_for_gt('00109_main_06_01_01_n3_Step18', AppiumBy.ACCESSIBILITY_ID, 'mainPanel', threshold=0.95)
    with step("[Action] Tap leaveButton at (41.2%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'leaveButton', 41.2, 48.1)
    with step("[Verify] Capture '00109_main_06_01_01_n3_Step20' for GT comparison"):
        actions.capture_for_gt('00109_main_06_01_01_n3_Step20', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap Format at (73.0%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Format', 73.0, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textBubbleBottomBarCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap alignLeftButton at (68.2%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'alignLeftButton', 68.2, 55.6)
    with step("[Verify] Capture '00109_main_06_01_01_n3_Step23' for GT comparison"):
        actions.capture_for_gt('00109_main_06_01_01_n3_Step23', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap alignCenterButton at (31.8%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'alignCenterButton', 31.8, 55.6)
    with step("[Verify] Capture '00109_main_06_01_01_n3_Step25' for GT comparison"):
        actions.capture_for_gt('00109_main_06_01_01_n3_Step25', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap alignRightButton at (68.2%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'alignRightButton', 68.2, 55.6)
    with step("[Verify] Capture '00109_main_06_01_01_n3_Step27' for GT comparison"):
        actions.capture_for_gt('00109_main_06_01_01_n3_Step27', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap boldButton at (56.8%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'boldButton', 56.8, 55.6)
    with step("[Verify] Capture '00109_main_06_01_01_n3_Step29' for GT comparison"):
        actions.capture_for_gt('00109_main_06_01_01_n3_Step29', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap italicButton at (59.1%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'italicButton', 59.1, 33.3)
    with step("[Verify] Capture '00109_main_06_01_01_n3_Step31' for GT comparison"):
        actions.capture_for_gt('00109_main_06_01_01_n3_Step31', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Drag mainPanel (53.0%,5.4%) → backgroundView (51.9%,88.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'mainPanel', 53.0, 5.4, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 51.9, 88.5, duration=1.0)
    with step("[Verify] Capture '00109_main_06_01_01_n3_Step33' for GT comparison"):
        actions.capture_for_gt('00109_main_06_01_01_n3_Step33', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (69.4%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 69.4, 38.8)
    with step("[Action] Tap OK at (56.7%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 56.7, 50.0)
    with step("[Action] Tap homeButton at (69.2%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 69.2, 46.2)
    with step("[Action] Tap Discard at (79.7%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 79.7, 58.3)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
