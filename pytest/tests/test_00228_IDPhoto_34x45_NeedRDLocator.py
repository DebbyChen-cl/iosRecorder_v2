import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00228_IDPhoto_34x45_20260812_162719")
def test_00228_IDPhoto_34x45_20260812_162719(actions: DriverActions):
    with step("[Action] Scroll until btnMain"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'btnMain', direction='down', offset_start=(0.421, 0.851), offset_end=(0.421, 0.0), velocity=238)
    with step("[Action] Tap btnMain at (7.9%, 59.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMain', 7.9, 59.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (80.0%, 70.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 80.0, 70.9)
    with step("[Action] Tap Collections at (43.2%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collections', 43.2, 58.3)
    with step("[Action] Tap albums-shelf-details-disclosure at (30.9%, 52.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'albums-shelf-details-disclosure', 30.9, 52.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=863)
    with step("[Action] Tap _AT at (67.9%, 63.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 67.9, 63.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albums-shelf-details-scrollView', container_w=430, container_h=863)
    with step("[Action] Tap photos_layout at (50.0%, 49.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photos_layout', 50.0, 49.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photosView_content_scroll_view', container_w=430, container_h=863)
    with step("[Action] Tap btnNext at (81.0%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 81.0, 40.0)
    with step("[Action] Tap btnNext at (75.5%, 87.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 75.5, 87.8)
    with step("[Action] Tap btnNext to continue to ID photo editor"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 50.0, 50.0)
    with step("[Action] Tap Size at (36.2%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Size', 36.2, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='idPhotoEditMainPanelCollectionView', container_w=308, container_h=97)
    with step("[Action] Tap 35 x 45mm at (21.4%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '35 x 45mm', 21.4, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='idPhotoSizePanelCollectionView', container_w=386, container_h=97)
    with step("[Verify] Capture '00228_IDPhoto_34x45_Step12' for GT comparison"):
        actions.capture_for_gt('00228_IDPhoto_34x45_Step12', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.IDPhotoEditViewController"]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap btnApply at (65.3%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnApply', 65.3, 55.1)
    with step("[Action] Tap btnBack at (59.2%, 63.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 59.2, 63.3)
    with step("[Action] Tap AlertDialog-btnPositive at (18.4%, 54.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 18.4, 54.0)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
