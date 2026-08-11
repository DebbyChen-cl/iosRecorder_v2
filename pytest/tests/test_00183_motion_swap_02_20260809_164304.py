import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00183_motion_swap_02_20260809_164304")
def test_00183_motion_swap_02_20260809_164304(actions: DriverActions):
    with step("[Action] Tap Character Motion Swap at (40.6%, 59.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Character Motion Swap', 40.6, 59.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Action] Tap btnImportFace at (47.5%, 53.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace', 47.5, 53.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editScrollView', container_w=394, container_h=542)
    with step("[Action] Tap btnAlbum at (79.7%, 19.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 79.7, 19.0)
    with step("[Action] Tap _AT at (6.8%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 6.8, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-5 at (58.5%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5', 58.5, 46.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap lblImportReference at (52.6%, 34.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lblImportReference', 52.6, 34.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editScrollView', container_w=394, container_h=542)
    with step("[Action] Tap Continue at (87.8%, 27.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 87.8, 27.3)
    with step("[Action] Tap Collections at (60.0%, 39.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collections', 60.0, 39.6)
    with step("[Action] Tap _Video at (22.9%, 72.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_Video', 22.9, 72.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albums-shelf-scrollView', container_w=430, container_h=120)
    with step("[Action] Tap photos_layout at (16.0%, 58.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photos_layout', 16.0, 58.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photosView_content_scroll_view', container_w=430, container_h=863)
    with step("[Action] Tap Choose at (39.7%, 69.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Choose', 39.7, 69.6)
    with step("[Action] Drag startBarImageView (75.0%,77.8%) → //XCUIElementTypeOther[@name=\"slidingWindow\"]/XCUIElementTypeOther[3] (41.8%,52.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'startBarImageView', 75.0, 77.8, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="slidingWindow"]/XCUIElementTypeOther[3]', 41.8, 52.3, duration=1.0)
    with step("[Verify] lblDesc text equals 'Selected Length: 00:07'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblDesc', 'Selected Length: 00:07')
    with step("[Action] Tap Continue at (84.2%, 9.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 84.2, 9.1)
    with step("[Action] Tap Keep the video background at (5.3%, 30.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Keep the video background', 5.3, 30.4)
    with step("[Action] Tap Generate at (90.1%, 45.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 90.1, 45.8)
    with step("[Verify] labelProcessing disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing', appear_timeout=5, disappear_timeout=1200), 'labelProcessing did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (77.4%, 71.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 77.4, 71.0)
    with step("[Action] Tap btnHome at (50.0%, 56.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 50.0, 56.7)
    assert True
