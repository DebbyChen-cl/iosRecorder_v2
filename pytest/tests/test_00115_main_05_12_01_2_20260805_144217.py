import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00115_main_05_12_01_2_20260805_144217")
def test_00115_main_05_12_01_2_20260805_144217(actions: DriverActions):
    with step("[Action] Tap Edit at (85.7%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 85.7, 48.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (83.2%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 83.2, 61.9)
    with step("[Action] Tap _AT at (7.9%, 90.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 90.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (27.7%, 78.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 27.7, 78.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (53.3%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 53.3, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_frame_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_frame_n', direction='left', offset_start=(0.795, 0.412), offset_end=(0.414, 0.412), velocity=455)
    with step("[Action] Tap btn_frame_n at (57.6%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_frame_n', 57.6, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Home Decor at (55.9%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Home Decor', 55.9, 28.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='frameBottomGroupBarCollectionView', container_w=366, container_h=97)
    with step("[Action] Tap 01 at (78.0%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '01', 78.0, 28.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='frameBottomGroupBarCollectionView', container_w=366, container_h=97)
    with step("[Verify] Capture '00115_main_05_12_01_2_Step10' for GT comparison"):
        actions.capture_for_gt('00115_main_05_12_01_2_Step10', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="EditFrameViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (36.7%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 36.7, 40.8)
    with step("[Verify] Capture '00115_main_05_12_01_2_Step12' for GT comparison"):
        actions.capture_for_gt('00115_main_05_12_01_2_Step12', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_frame_n at (36.4%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_frame_n', 36.4, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"frameBottomGroupBarCollectionView\"]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage at (69.5%, 42.6%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="frameBottomGroupBarCollectionView"]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage', 69.5, 42.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='frameBottomGroupBarCollectionView', container_w=366, container_h=97)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"frameBottomGroupBarCollectionView\"]/XCUIElementTypeCell/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage at (84.7%, 68.9%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="frameBottomGroupBarCollectionView"]/XCUIElementTypeCell/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage', 84.7, 68.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='frameBottomGroupBarCollectionView', container_w=366, container_h=97)
    with step("[Action] Tap btn_ok_n at (77.6%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 51.0)
    with step("[Action] Tap btnClose at (54.8%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 54.8, 54.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap icon_Pack_close at (66.7%, 74.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_Pack_close', 66.7, 74.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='frameBottomGroupBarCollectionView', container_w=366, container_h=97)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"frameBottomGroupBarCollectionView\"]/XCUIElementTypeCell[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage at (55.9%, 39.3%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="frameBottomGroupBarCollectionView"]/XCUIElementTypeCell[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage', 55.9, 39.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='frameBottomGroupBarCollectionView', container_w=366, container_h=97)
    with step("[Action] Tap 01 at (59.3%, 7.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '01', 59.3, 7.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='frameBottomGroupBarCollectionView', container_w=366, container_h=97)
    with step("[Action] Tap btn_ok_n at (73.5%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 30.6)
    with step("[Action] Tap homeButton at (61.5%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 61.5)
    with step("[Action] Tap Discard at (65.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 65.2, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
