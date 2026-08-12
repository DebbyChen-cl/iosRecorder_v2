import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00208_ai_video_try_on_photo_20260810_183134")
def test_00208_ai_video_try_on_photo_20260810_183134(actions: DriverActions):
    with step("[Action] Scroll until AI Video Try-On"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'AI Video Try-On', direction='left', offset_start=(0.937, 0.502), offset_end=(0.007, 0.502), velocity=583)
    with step("[Action] Tap AI Video Try-On at (57.3%, 75.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Video Try-On', 57.3, 75.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"aiVideoTryOn_importView\"]/XCUIElementTypeOther at (46.2%, 53.1%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="aiVideoTryOn_importView"]/XCUIElementTypeOther', 46.2, 53.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=719)
    with step("[Action] Tap notShowAgainCheckBox at (70.4%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox', 70.4, 57.7)
    with step("[Action] Tap Continue at (62.2%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 62.2, 68.2)
    with step("[Action] Tap Collections at (57.9%, 52.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collections', 57.9, 52.1)
    with step("[Action] Tap _Video at (25.0%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_Video', 25.0, 83.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albums-shelf-scrollView', container_w=430, container_h=120)
    with step("[Action] Tap photos_layout at (19.1%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photos_layout', 19.1, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photosView_content_scroll_view', container_w=430, container_h=863)
    with step("[Action] Tap Next at (65.0%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next', 65.0, 54.5)
    with step("[Verify] Capture '00208_ai_video_try_on_photo_Step10' for GT comparison"):
        actions.capture_for_gt('00208_ai_video_try_on_photo_Step10', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="aiVideoTryOn_importView"]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"aiVideoTryOn_importView\"]/XCUIElementTypeOther/XCUIElementTypeOther at (40.5%, 44.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="aiVideoTryOn_importView"]/XCUIElementTypeOther/XCUIElementTypeOther', 40.5, 44.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=719)
    with step("[Action] Tap Cancel at (63.9%, 38.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 63.9, 38.9)
    with step("[Action] Tap mainArea at (60.7%, 65.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'mainArea', 60.7, 65.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=719)
    with step("[Action] Tap PhotoPickerRecommendDialog-notShowAgainCheckBox at (55.6%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox', 55.6, 48.1)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (39.4%, 65.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 39.4, 65.3)
    with step("[Action] Tap btnAlbum at (80.7%, 64.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 80.7, 64.3)
    with step("[Action] Tap Sample Photos at (26.2%, 39.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 26.2, 39.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap PhDM_example_3 at (39.2%, 54.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_3', 39.2, 54.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap photoImageView at (48.0%, 55.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoImageView', 48.0, 55.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=719)
    with step("[Action] Tap btnBack at (65.0%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 65.0, 58.5)
    with step("[Action] Tap Generate at (76.5%, 47.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 76.5, 47.8)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Verify] processingLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'processingLabel', appear_timeout=5, disappear_timeout=1200), 'processingLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (38.7%, 25.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 38.7, 25.8)
    with step("[Action] Tap aiVideoTryOn_backButton at (65.4%, 59.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiVideoTryOn_backButton', 65.4, 59.3)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
