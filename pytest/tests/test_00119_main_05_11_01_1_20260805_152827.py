import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00119_main_05_11_01_1_20260805_152827")
def test_00119_main_05_11_01_1_20260805_152827(actions: DriverActions):
    with step("[Action] Tap Edit at (54.3%, 72.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 54.3, 72.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (69.5%, 81.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 69.5, 81.0)
    with step("[Action] Tap _AT at (9.7%, 95.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.7, 95.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (9.2%, 79.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 9.2, 79.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (68.9%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 68.9, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_addimg_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', direction='left', offset_start=(0.7, 0.412), offset_end=(0.247, 0.412), velocity=275)
    with step("[Action] Tap btn_addimg_n at (54.5%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', 54.5, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btnAlbum at (71.6%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 71.6, 28.6)
    with step("[Action] Tap _AT at (11.5%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 11.5, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-1 at (32.3%, 64.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 32.3, 64.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Drag imageView (49.3%,51.5%) → backgroundView (51.2%,61.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'imageView', 49.3, 51.5, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 51.2, 61.2, duration=1.0)
    with step("[Verify] Capture '00119_main_05_11_01_1_Step12' for GT comparison"):
        actions.capture_for_gt('00119_main_05_11_01_1_Step12', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.94)
    with step("[Action] Tap btn_cancel_n at (59.2%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 59.2, 46.9)
    with step("[Action] Tap btn_addimg_n at (72.7%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', 72.7, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btnAlbum at (93.4%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 93.4, 52.4)
    with step("[Action] Tap _AT at (8.2%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.2, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-1 at (37.7%, 64.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 37.7, 64.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Drag rotateImageView (85.2%,33.3%) → backgroundView (30.9%,46.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'rotateImageView', 85.2, 33.3, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 30.9, 46.7, duration=1.0)
    with step("[Verify] Capture '00119_main_05_11_01_1_Step19' for GT comparison"):
        actions.capture_for_gt('00119_main_05_11_01_1_Step19', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.94)
    with step("[Action] Rotate imageView 55.1°"):
        actions.rotate(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'imageView'), rotation=55.1)
    with step("[Verify] Capture '00119_main_05_11_01_1_Step21' for GT comparison"):
        actions.capture_for_gt('00119_main_05_11_01_1_Step21', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.94)
    with step("[Action] Tap btnFlip at (44.4%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnFlip', 44.4, 55.6)
    with step("[Verify] Capture '00119_main_05_11_01_1_Step23' for GT comparison"):
        actions.capture_for_gt('00119_main_05_11_01_1_Step23', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.94)
    with step("[Action] Tap imageView at (56.1%, 22.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 56.1, 22.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag slider (92.1%,52.0%) → backgroundView (5.3%,81.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 92.1, 52.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 5.3, 81.0, duration=1.0)
    with step("[Verify] Capture '00119_main_05_11_01_1_Step26' for GT comparison"):
        actions.capture_for_gt('00119_main_05_11_01_1_Step26', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.94)
    with step("[Verify] lblVal text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '0')
    with step("[Action] Drag slider (7.9%,38.0%) → backgroundView (77.9%,81.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 7.9, 38.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 77.9, 81.3, duration=1.0)
    with step("[Verify] lblVal text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '100')
    with step("[Verify] Capture '00119_main_05_11_01_1_Step30' for GT comparison"):
        actions.capture_for_gt('00119_main_05_11_01_1_Step30', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.94)
    with step("[Action] Tap btn_ok_n at (89.8%, 10.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 89.8, 10.2)
    with step("[Action] Tap OK at (16.7%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 16.7, 75.0)
    with step("[Verify] Capture '00119_main_05_11_01_1_Step33' for GT comparison"):
        actions.capture_for_gt('00119_main_05_11_01_1_Step33', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.94)
    with step("[Action] Tap homeButton at (57.7%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 57.7, 73.1)
    with step("[Action] Tap Discard at (81.2%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 81.2, 58.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Action] Tap Edit at (54.3%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 54.3, 60.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (76.1%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 76.1, 54.8)
    with step("[Action] Tap _AT at (9.7%, 31.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.7, 31.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (17.7%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 17.7, 65.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (71.1%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 71.1, 51.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_addimg_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', direction='left', offset_start=(0.828, 0.371), offset_end=(0.319, 0.371), velocity=373)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Scroll until btn_addimg_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', direction='left', offset_start=(0.297, 0.546), offset_end=(0.216, 0.546), velocity=50)
    with step("[Action] Tap btn_addimg_n at (41.2%, 39.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', 41.2, 39.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Action] Tap btnCamera at (52.5%, 41.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnCamera', 52.5, 41.5)
    with step("[Action] Tap PhotoCapture at (57.5%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoCapture', 57.5, 52.5)
    with step("[Action] Tap Use Photo at (45.9%, 65.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Use Photo', 45.9, 65.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap btn_ok_n at (91.8%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 91.8, 55.1)
    with step("[Action] Tap OK at (63.3%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 63.3, 83.3)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.98)
    with step("[Action] Tap homeButton at (61.5%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 57.7)
    with step("[Action] Tap Discard at (65.2%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 65.2, 58.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.94)
    assert True
