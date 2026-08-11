import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00120_main_05_11_01_2_20260805_153334")
def test_00120_main_05_11_01_2_20260805_153334(actions: DriverActions):
    with step("[Action] Tap Edit at (80.0%, 88.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 80.0, 88.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (78.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 78.2, 50.0)
    with step("[Action] Tap _AT at (10.8%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.8, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (32.3%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 32.3, 70.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (64.4%, 42.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 64.4, 42.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_addimg_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', direction='left', offset_start=(0.719, 0.485), offset_end=(0.23, 0.485), velocity=403)
    with step("[Action] Tap btn_addimg_n at (42.4%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', 42.4, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btnAlbum at (74.6%, 38.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 74.6, 38.1)
    with step("[Action] Tap _AT at (9.3%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.3, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-1 at (50.8%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 50.8, 53.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap imageView at (31.7%, 42.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="AddImageMainPanelCell-2"]', 31.7, 42.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap btn_rotate_n at (61.0%, 82.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_rotate_n', 61.0, 82.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step13' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step13', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_rotate_n at (65.9%, 70.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_rotate_n', 65.9, 70.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step15' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step15', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_rotate_n at (26.8%, 70.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_rotate_n', 26.8, 70.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step17' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step17', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_rotate_n at (90.2%, 53.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_rotate_n', 90.2, 53.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step19' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step19', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_flipH_n at (31.7%, 39.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_flipH_n', 31.7, 39.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step21' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step21', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_flipV_n at (78.0%, 31.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_flipV_n', 78.0, 31.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step23' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step23', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"CropViewController\"]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeSlider (51.4%,53.3%) → 0° (3.2%,54.5%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeSlider', 51.4, 53.3, AppiumBy.ACCESSIBILITY_ID, '0°', 3.2, 54.5, duration=1.0)
    with step("[Verify] 45° text equals '45°'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '45°', '45°')
    with step("[Verify] Capture '00120_main_05_11_01_2_Step26' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step26', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_original_size at (19.5%, 39.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_original_size', 19.5, 39.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step28' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step28', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_square at (70.0%, 70.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_square', 70.0, 70.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step30' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step30', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_4v5 at (78.0%, 56.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_4v5', 78.0, 56.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=431, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step32' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step32', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_5v4 at (68.3%, 65.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_5v4', 68.3, 65.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step34' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step34', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_3v4 at (43.9%, 56.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_3v4', 43.9, 56.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=431, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step36' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step36', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"croppingRotationCollectionView\"]/XCUIElementTypeCell[4] at (82.1%, 33.3%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="croppingRotationCollectionView"]/XCUIElementTypeCell[4]', 82.1, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step38' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step38', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_2v3 at (58.5%, 48.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_2v3', 58.5, 48.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=431, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step40' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step40', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_3v2 at (41.5%, 82.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_3v2', 41.5, 82.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=431, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step42' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step42', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_9v16 at (53.7%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_9v16', 53.7, 58.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=431, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step44' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step44', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_16v9 at (53.7%, 56.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_16v9', 53.7, 56.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=431, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step46' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step46', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_IG4v5 at (53.7%, 48.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_IG4v5', 53.7, 48.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=431, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step48' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step48', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_IG9v16 at (36.6%, 80.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_IG9v16', 36.6, 80.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step50' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step50', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_tictok9v16 at (47.5%, 48.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_tictok9v16', 47.5, 48.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step52' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step52', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_tictok16v9 at (65.9%, 80.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_tictok16v9', 65.9, 80.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step54' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step54', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_snapchat9v16 at (67.5%, 53.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_snapchat9v16', 67.5, 53.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step56' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step56', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_Youtube16v9 at (65.9%, 56.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_Youtube16v9', 65.9, 56.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step58' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step58', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_FB1v1 at (42.5%, 36.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_FB1v1', 42.5, 36.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step60' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step60', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_FBCover at (63.4%, 70.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_FBCover', 63.4, 70.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step62' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step62', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_FB1.91v1 at (56.1%, 80.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_FB1.91v1', 56.1, 80.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step64' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step64', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (93.9%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 93.9, 42.9)
    with step("[Verify] Capture '00120_main_05_11_01_2_Step66' for GT comparison"):
        actions.capture_for_gt('00120_main_05_11_01_2_Step66', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (69.4%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 69.4, 30.6)
    with step("[Action] Tap OK at (40.0%, 95.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 40.0, 95.8)
    with step("[Action] Tap homeButton at (61.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 50.0)
    with step("[Action] Tap Discard at (85.5%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 85.5, 58.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
