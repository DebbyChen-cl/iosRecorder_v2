import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00108_main_06_01_01_n2_20260808_211227")
def test_00108_main_06_01_01_n2_20260808_211227(actions: DriverActions):
    with step("[Action] Tap Edit at (45.7%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 45.7, 56.0)
    with step("[Action] Tap btnAlbum at (81.2%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 81.2, 52.4)
    with step("[Action] Tap _AT at (7.2%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.2, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (31.5%, 33.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 31.5, 33.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (66.7%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 66.7, 51.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Text"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Text', direction='left', offset_start=(0.423, 0.433), offset_end=(0.326, 0.433), velocity=68)
    with step("[Action] Tap Text at (41.7%, 36.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text', 41.7, 36.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Text Bubble at (64.9%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text Bubble', 64.9, 83.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap Font at (46.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Font', 46.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textBubbleBottomBarCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap leaveButton at (52.9%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'leaveButton', 52.9, 53.8)
    with step("[Verify] Capture '00108_main_06_01_01_n2_Step01' for GT comparison"):
        actions.capture_for_gt('00108_main_06_01_01_n2_Step01', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap Font at (46.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Font', 46.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textBubbleBottomBarCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap progressView at (27.0%, 49.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'progressView', 27.0, 49.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='fontCollectionView', container_w=430, container_h=308)
    with step("[Verify] Capture '00108_main_06_01_01_n2_Step14' for GT comparison"):
        actions.capture_for_gt('00108_main_06_01_01_n2_Step14', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Drag mainPanel (51.9%,4.1%) → backgroundView (51.4%,92.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'mainPanel', 51.9, 4.1, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 51.4, 92.6, duration=1.0)
    with step("[Verify] Capture '00108_main_06_01_01_n2_Step02' for GT comparison"):
        actions.capture_for_gt('00108_main_06_01_01_n2_Step02', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (85.7%, 22.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 85.7, 22.4)
    with step("[Action] Tap OK at (16.7%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 16.7, 41.7)
    with step("[Action] Tap homeButton at (38.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 38.5, 50.0)
    with step("[Action] Tap Discard at (58.0%, 12.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 58.0, 12.5)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
