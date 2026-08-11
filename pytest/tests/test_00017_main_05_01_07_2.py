import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00017_main_05_01_07_2')
def test_00017_main_05_01_07_2(actions: DriverActions):
    """crop & rotate"""
    uuid = ['4c60aa1b-8cd0-414b-8baf-4d808b66036c', 'c25b2f15-ec0f-4d6d-92b9-c226a5bc808f', 'c7e7113e-dcfb-4eb1-886f-d90eeec3bda8', 'e3e3d0a0-53a5-4c1a-9dc6-f21ad287d30a', '8319bc63-ae61-4c5d-80cd-64e9beef11e9', '207b3ce9-76f0-4b21-beb4-9742c75e4e2f', 'ca4a14af-c245-45c3-b20e-1a17cdee0577', 'a40bcae6-e27a-4b3f-92e3-a6fc56ecc232', '215b4ae7-1dd2-11b2-8000-080027b246c3', '215b4ae7-1dd2-11b2-8001-080027b246c3', '215b4ae7-1dd2-11b2-8002-080027b246c3', '215b4ae7-1dd2-11b2-8003-080027b246c3', '215b4ae7-1dd2-11b2-8004-080027b246c3', '215b4ae7-1dd2-11b2-8005-080027b246c3', '215b4ae7-1dd2-11b2-8006-080027b246c3', '7158302e-13a0-4e9c-b0c0-c2d9d5a650ce', 'b7f80468-5028-47bc-8e0a-b7561eeee87b', 'd7321d8e-62c3-45d5-b3ec-32d589c7877a', 'a7f63d1a-bbea-47de-beb4-38d1433e8da4', 'ff600db0-8d92-4545-83ef-1908e2d8d9ae', 'dd6730b8-1052-48e0-b969-577f713ecee8', 'bcfe663a-4643-4f2e-8b15-97cc2e82f4f9', '5e616fa1-c411-436b-8d44-8045aa45e8ae', '3b09541c-7a41-4453-b3e5-081249f7ba7c', '2d30582c-e92f-4f78-84ed-54b47b406f0c', '2cae2cd4-d572-4d1c-9316-2391ba14b1f7']
    with step("[Action] Tap Edit at (68.6%, 36.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 68.6, 36.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (76.6%, 40.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 76.6, 40.5)
    with step("[Action] Tap _AT at (7.2%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.2, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (45.4%, 60.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 45.4, 60.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap ic_crop at (48.5%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_crop', 48.5, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_crop_raotate at (57.6%, 39.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_crop_raotate', 57.6, 39.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap ic_original_size at (14.6%, 43.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_original_size', 14.6, 43.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"CropViewController\"]/XCUIElementTypeOther[2] (94.9%,30.3%) → //XCUIElementTypeOther[@name=\"CropViewController\"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage (14.6%,56.0%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]', 94.9, 30.3, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', 14.6, 56.0, duration=1.0)
    with step("[Verify] Capture 'crop___rotate_Step09' for GT comparison"):
        actions.capture_for_gt('crop___rotate_Step09', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Original at (55.7%, 8.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Original', 55.7, 8.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture 'crop___rotate_Step11' for GT comparison"):
        actions.capture_for_gt('crop___rotate_Step11', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_custom_size at (65.9%, 63.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_custom_size', 65.9, 63.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"CropViewController\"]/XCUIElementTypeOther[2] (94.9%,30.3%) → //XCUIElementTypeOther[@name=\"CropViewController\"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage (14.6%,56.0%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]', 94.9, 30.3, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', 14.6, 56.0, duration=1.0)
    with step("[Verify] Capture 'crop___rotate_Step13' for GT comparison"):
        actions.capture_for_gt('crop___rotate_Step13', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_custom_size at (48.8%, 82.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_custom_size', 48.8, 82.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Verify] Capture 'crop___rotate_Step15' for GT comparison"):
        actions.capture_for_gt('crop___rotate_Step15', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"CropViewController\"]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeSlider (49.5%,46.7%) → //XCUIElementTypeOther[@name=\"CropViewController\"]/XCUIElementTypeOther[4]/XCUIElementTypeOther (80.3%,50.0%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeSlider', 49.5, 46.7, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeOther', 80.3, 50.0, duration=1.0)
    with step("[Verify] 45° text equals '45°'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '45°', '45°')
    with step("[Verify] Capture 'crop___rotate_Step18' for GT comparison"):
        actions.capture_for_gt('crop___rotate_Step18', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"CropViewController\"]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeSlider (94.0%,57.8%) → //XCUIElementTypeOther[@name=\"CropViewController\"]/XCUIElementTypeOther[4]/XCUIElementTypeOther (0.3%,52.3%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeSlider', 94.0, 57.8, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeOther', 0.3, 52.3, duration=1.0)
    with step("[Verify] -45° text equals '-45°'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '-45°', '-45°')
    with step("[Verify] Capture 'crop___rotate_Step21' for GT comparison"):
        actions.capture_for_gt('crop___rotate_Step21', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_square at (67.5%, 56.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_square', 67.5, 56.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Action] Tap btn_ok_n at (71.4%, 65.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 71.4, 65.3)
    with step("[Verify] Capture 'crop___rotate_Step24' for GT comparison"):
        actions.capture_for_gt('crop___rotate_Step24', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (33.3%, 35.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 33.3, 35.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    
    elements = ['ic_4v5', 'ic_5v4', 'ic_3v4', 'ic_4v3', 'ic_2v3', 'ic_3v2', 'ic_9v16', 'ic_16v9']

    for ele in elements:
        with step("[Action] Tap ic_crop at (54.5%, 75.8%)"):
                actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_crop', 54.5, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
        with step("[Action] Tap ic_crop_raotate at (69.7%, 84.8%)"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_crop_raotate', 69.7, 84.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
        with step("[Action] Drag //XCUIElementTypeOther[@name=\"CropViewController\"]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeSlider (50.5%,55.6%) → //XCUIElementTypeOther[@name=\"CropViewController\"]/XCUIElementTypeOther[4]/XCUIElementTypeOther (80.3%,52.3%)"):
            actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeSlider', 50.5, 55.6, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="CropViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeOther', 80.3, 52.3, duration=1.0)
        with step(f"[Action] Tap {ele} at (61.0%, 73.2%)"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, ele, 61.0, 73.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=431, container_h=64)
        with step("[Action] Tap btn_ok_n at (87.8%, 36.7%)"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 87.8, 36.7)
        with step(f"[Verify] Capture 'crop___rotate_{ele}' for GT comparison"):
            actions.capture_for_gt(f'crop___rotate_{ele}', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
        with step("[Action] Tap ic edit undo n at (59.0%, 64.1%)"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 59.0, 64.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Action] Tap homeButton at (65.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.0, 52.5)
    with step("[Action] Tap Discard at (65.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 65.0, 52.5)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    with step("[Verify] test_00017 completion"):
        assert True
