import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00047_main_05_04_01_20260804_111553")
def test_00047_main_05_04_01_20260804_111553(actions: DriverActions):
    with step("[Action] Tap Edit at (28.6%, 100.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 28.6, 100.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (90.9%, 69.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 90.9, 69.0)
    with step("[Action] Tap _AT at (7.2%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.2, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (55.4%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 55.4, 58.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Enhance at (67.9%, 73.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 67.9, 73.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap btn_filter_n at (36.4%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_filter_n', 36.4, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Select a source photo to extract its filter. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Select a source photo to extract its filter.')
    with step("[Action] Tap Basic at (50.0%, 38.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Basic', 50.0, 38.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='cmsCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap Vlogger 01 at (42.6%, 52.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Vlogger 01', 42.6, 52.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=94)
    with step("[Verify] Capture '00047_main_05_04_01_Step10' for GT comparison"):
        actions.capture_for_gt('00047_main_05_04_01_Step10', AppiumBy.ACCESSIBILITY_ID, 'gpuImageView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (30.6%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 30.6, 38.8)
    with step("[Verify] Capture '00047_main_05_04_01_Step12' for GT comparison"):
        actions.capture_for_gt('00047_main_05_04_01_Step12', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_filter_n at (72.7%, 84.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_filter_n', 72.7, 84.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Basic at (58.8%, 47.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Basic', 58.8, 47.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='cmsCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap Vlogger 01 at (79.4%, 52.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Vlogger 01', 79.4, 52.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=94)
    with step("[Action] Tap btn_ok_n at (83.7%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 83.7, 49.0)
    with step("[Action] Tap btnClose at (61.3%, 58.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 61.3, 58.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap Vlogger 02 at (53.6%, 76.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Vlogger 02', 53.6, 76.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=94)
    with step("[Action] Tap btn_cancel_n at (22.4%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 22.4, 44.9)
    with step("[Verify] Capture '00047_main_05_04_01_Step20' for GT comparison"):
        actions.capture_for_gt('00047_main_05_04_01_Step20', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_filter_n at (78.8%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_filter_n', 78.8, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Basic at (50.0%, 44.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Basic', 50.0, 44.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='cmsCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap Vlogger 02 at (63.2%, 76.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Vlogger 02', 63.2, 76.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=94)
    with step("[Action] Tap btn_ok_n at (81.6%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 42.9)
    with step("[Verify] Capture '00047_main_05_04_01_Step25' for GT comparison"):
        actions.capture_for_gt('00047_main_05_04_01_Step25', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (30.8%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 30.8, 53.8)
    with step("[Action] Tap Discard at (81.2%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 81.2, 83.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
