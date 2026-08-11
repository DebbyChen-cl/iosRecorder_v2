import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00122_main_05_11_01_4_20260805_155236")
def test_00122_main_05_11_01_4_20260805_155236(actions: DriverActions):
    with step("[Action] Tap Edit at (71.4%, 36.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 71.4, 36.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (85.3%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 85.3, 50.0)
    with step("[Action] Tap _AT at (9.7%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.7, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (27.7%, 66.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 27.7, 66.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (33.3%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 33.3, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_addimg_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', direction='left', offset_start=(0.644, 0.392), offset_end=(0.174, 0.392), velocity=414)
    with step("[Action] Tap btn_addimg_n at (67.6%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', 67.6, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btnAlbum at (74.6%, 59.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 74.6, 59.5)
    with step("[Action] Tap _AT at (7.9%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (46.2%, 56.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 46.2, 56.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Pinch imageView scale=1.604"):
        actions.pinch(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'imageView'), scale=1.604, velocity=0.483)
    with step("[Action] Rotate imageView 47.3°"):
        actions.rotate(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'imageView'), rotation=47.3)
    with step("[Action] Scroll until imageView"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', AppiumBy.ACCESSIBILITY_ID, 'imageView', direction='left', offset_start=(0.656, 0.282), offset_end=(0.391, 0.282), velocity=190)
    with step("[Action] Tap imageView at (72.5%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 72.5, 45.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] Capture '00122_main_05_11_01_4_Step15' for GT comparison"):
        actions.capture_for_gt('00122_main_05_11_01_4_Step15', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap snapLineView at (40.5%, 97.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'snapLineView', 40.5, 97.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageContainerView', container_w=412, container_h=40)
    with step("[Verify] Capture '00122_main_05_11_01_4_Step17' for GT comparison"):
        actions.capture_for_gt('00122_main_05_11_01_4_Step17', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap snapLineView at (63.5%, 97.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'snapLineView', 63.5, 97.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageContainerView', container_w=412, container_h=40)
    with step("[Verify] Capture '00122_main_05_11_01_4_Step19' for GT comparison"):
        actions.capture_for_gt('00122_main_05_11_01_4_Step19', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap snapLineView at (77.4%, 97.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'snapLineView', 77.4, 97.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageContainerView', container_w=412, container_h=40)
    with step("[Verify] Capture '00122_main_05_11_01_4_Step21' for GT comparison"):
        actions.capture_for_gt('00122_main_05_11_01_4_Step21', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap snapLineView at (77.0%, 97.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'snapLineView', 77.0, 97.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageContainerView', container_w=412, container_h=40)
    with step("[Verify] Capture '00122_main_05_11_01_4_Step23' for GT comparison"):
        actions.capture_for_gt('00122_main_05_11_01_4_Step23', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap snapLineView at (88.8%, 97.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'snapLineView', 88.8, 97.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageContainerView', container_w=412, container_h=40)
    with step("[Verify] Capture '00122_main_05_11_01_4_Step25' for GT comparison"):
        actions.capture_for_gt('00122_main_05_11_01_4_Step25', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (32.7%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 32.7, 46.9)
    with step("[Verify] Capture '00122_main_05_11_01_4_Step27' for GT comparison"):
        actions.capture_for_gt('00122_main_05_11_01_4_Step27', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_addimg_n at (55.9%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', 55.9, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap photoCell-0 at (49.2%, 73.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 49.2, 73.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Scroll until imageView"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', AppiumBy.ACCESSIBILITY_ID, 'imageView', direction='left', offset_start=(0.83, 0.394), offset_end=(0.351, 0.394), velocity=417)
    with step("[Action] Tap imageView at (75.6%, 72.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 75.6, 72.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap snapLineView at (64.0%, 98.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'snapLineView', 64.0, 98.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageContainerView', container_w=412, container_h=40)
    with step("[Action] Tap btn_ok_n at (81.6%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 34.7)
    with step("[Action] Tap OK at (76.7%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 76.7, 66.7)
    with step("[Verify] Capture '00122_main_05_11_01_4_Step35' for GT comparison"):
        actions.capture_for_gt('00122_main_05_11_01_4_Step35', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (69.2%, 80.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 69.2, 80.8)
    with step("[Action] Tap Discard at (60.9%, 29.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 60.9, 29.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
