import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00141_main_05_01_12_1_20260805_165503")
def test_00141_main_05_01_12_1_20260805_165503(actions: DriverActions):
    with step("[Action] Tap Edit at (57.1%, 68.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 57.1, 68.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (71.6%, 31.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 71.6, 31.0)
    with step("[Action] Tap _AT at (8.6%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.6, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (38.5%, 76.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 38.5, 76.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Quick Actions at (52.8%, 77.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions', 52.8, 77.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap btn_effect at (47.1%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_effect', 47.1, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00141_main_05_01_12_1_Step07' for GT comparison"):
        actions.capture_for_gt('00141_main_05_01_12_1_Step07', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AutoQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap icon_style_none at (39.8%, 78.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_style_none', 39.8, 78.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00141_main_05_01_12_1_Step09' for GT comparison"):
        actions.capture_for_gt('00141_main_05_01_12_1_Step09', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AutoQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Basic at (55.5%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Basic', 55.5, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00141_main_05_01_12_1_Step11' for GT comparison"):
        actions.capture_for_gt('00141_main_05_01_12_1_Step11', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AutoQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Light at (34.5%, 85.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Light', 34.5, 85.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00141_main_05_01_12_1_Step13' for GT comparison"):
        actions.capture_for_gt('00141_main_05_01_12_1_Step13', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AutoQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Auto at (91.4%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Auto', 91.4, 44.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap btnClose at (51.6%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 51.6, 48.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap Auto at (7.7%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Auto', 7.7, 34.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Verify] Capture '00141_main_05_01_12_1_Step17' for GT comparison"):
        actions.capture_for_gt('00141_main_05_01_12_1_Step17', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (69.2%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 69.2, 46.2)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
