import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00048_main_05_04_01_n_20260804_112333")
def test_00048_main_05_04_01_n_20260804_112333(actions: DriverActions):
    with step("[Action] Tap Edit at (62.9%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 62.9, 52.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (78.7%, 59.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 78.7, 59.5)
    with step("[Action] Tap _AT at (9.0%, 86.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.0, 86.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (51.5%, 47.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 51.5, 47.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Enhance at (64.3%, 68.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 64.3, 68.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap btn_filter_n at (54.5%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_filter_n', 54.5, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap closeButton at (61.9%, 38.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'closeButton', 61.9, 38.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=94)
    with step("[Action] Tap Custom Filter at (79.4%, 17.6%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-UserImageItem1"]/XCUIElementTypeOther/XCUIElementTypeImage', 79.4, 17.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=94)
    with step("[Action] Tap Stock at (40.0%, 14.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Stock', 40.0, 14.3)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"stockContainer\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[2] at (61.2%, 54.7%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="stockContainer"]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[2]', 61.2, 54.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='gettyImagePickerViewCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap PexelsCollectionViewCell-0 at (62.4%, 63.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PexelsCollectionViewCell-0', 62.4, 63.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="stockContainer"]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture '00048_main_05_04_01_n_Step12' for GT comparison"):
        actions.capture_for_gt('00048_main_05_04_01_n_Step12', AppiumBy.ACCESSIBILITY_ID, 'gpuImageView', threshold=0.95)
    with step("[Action] Drag cpSlider (69.3%,61.9%) → slider (97.9%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 69.3, 61.9, AppiumBy.ACCESSIBILITY_ID, 'slider', 97.9, 56.1, duration=1.0)
    with step("[Verify] Capture '00048_main_05_04_01_n_Step14' for GT comparison"):
        actions.capture_for_gt('00048_main_05_04_01_n_Step14', AppiumBy.ACCESSIBILITY_ID, 'gpuImageView', threshold=0.95)
    with step("[Action] Drag cpSlider (93.9%,52.4%) → slider (0.6%,46.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 93.9, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 0.6, 46.3, duration=1.0)
    with step("[Verify] Capture '00048_main_05_04_01_n_Step16' for GT comparison"):
        actions.capture_for_gt('00048_main_05_04_01_n_Step16', AppiumBy.ACCESSIBILITY_ID, 'gpuImageView', threshold=0.95)
    with step("[Verify] Capture '00048_main_05_04_01_n_Step17' for GT comparison"):
        actions.capture_for_gt('00048_main_05_04_01_n_Step17', AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-UserImageItem2"]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (24.5%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 24.5, 46.9)
    with step("[Action] Tap btn_filter_n at (57.6%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_filter_n', 57.6, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CMS-UserImageItem2\"]/XCUIElementTypeOther/XCUIElementTypeImage at (49.3%, 41.1%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-UserImageItem2"]/XCUIElementTypeOther/XCUIElementTypeImage', 49.3, 41.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=94)
    with step("[Verify] Capture '00048_main_05_04_01_n_Step21' for GT comparison"):
        actions.capture_for_gt('00048_main_05_04_01_n_Step21', AppiumBy.ACCESSIBILITY_ID, 'gpuImageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (89.8%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 89.8, 40.8)
    with step("[Verify] Capture '00048_main_05_04_01_n_Step23' for GT comparison"):
        actions.capture_for_gt('00048_main_05_04_01_n_Step23', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (66.7%, 41.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 66.7, 41.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00048_main_05_04_01_n_Step25' for GT comparison"):
        actions.capture_for_gt('00048_main_05_04_01_n_Step25', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit redo n at (43.6%, 41.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n', 43.6, 41.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00048_main_05_04_01_n_Step27' for GT comparison"):
        actions.capture_for_gt('00048_main_05_04_01_n_Step27', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (57.7%, 30.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 57.7, 30.8)
    with step("[Action] Tap Discard at (72.5%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 72.5, 66.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
