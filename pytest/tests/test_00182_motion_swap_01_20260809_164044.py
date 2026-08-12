import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00182_motion_swap_01_20260809_164044")
def test_00182_motion_swap_01_20260809_164044(actions: DriverActions):
    with step("[Action] Tap Character Motion Swap at (66.7%, 59.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Character Motion Swap', 66.7, 59.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Action] Tap notShowAgainCheckBox at (92.6%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox', 92.6, 65.4)
    with step("[Action] Tap btnNext at (25.3%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 25.3, 51.0)
    with step("[Action] Tap btnInfo at (84.0%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnInfo', 84.0, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editScrollView', container_w=394, container_h=542)
    with step("[Verify] Use a photo with the same aspect ratio as your video. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Use a photo with the same aspect ratio as your video.')
    with step("[Action] Tap btnInfoMode at (83.3%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnInfoMode', 83.3, 62.5)
    with step("[Action] Tap Try now at (73.3%, 62.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try now', 73.3, 62.0)
    with step("[Action] Tap btnImportFace at (40.6%, 48.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace', 40.6, 48.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editScrollView', container_w=394, container_h=542)
    with step("[Action] Tap PhotoPickerRecommendDialog-notShowAgainCheckBox at (74.1%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox', 74.1, 48.1)
    with step("[Action] Tap Continue at (20.3%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 20.3, 52.2)
    with step("[Action] Tap btnAlbum at (73.6%, 69.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 73.6, 69.0)
    with step("[Action] Tap _AT at (8.2%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.2, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (68.5%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 68.5, 58.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture '00182_motion_swap_01_Step15' for GT comparison"):
        actions.capture_for_gt('00182_motion_swap_01_Step15', AppiumBy.ACCESSIBILITY_ID, 'btnImportFace', threshold=0.95)
    with step("[Action] Tap btnImportFace at (45.9%, 55.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace', 45.9, 55.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editScrollView', container_w=394, container_h=542)
    with step("[Action] Tap ic info n at (35.0%, 53.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic info n', 35.0, 53.7)
    with step("[Verify] descriptionLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel')
    with step("[Action] Tap Continue at (89.2%, 78.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 89.2, 78.3)
    with step("[Action] Tap photoCell-5 at (49.2%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5', 49.2, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture '00182_motion_swap_01_Step21' for GT comparison"):
        actions.capture_for_gt('00182_motion_swap_01_Step21', AppiumBy.ACCESSIBILITY_ID, 'btnImportFace', threshold=0.7)
    with step("[Action] Tap lblImportReference at (12.3%, 4.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lblImportReference', 12.3, 4.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editScrollView', container_w=394, container_h=542)
    with step("[Verify] recommendationLbl is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'recommendationLbl')
    with step("[Action] Tap btnNext at (50.5%, 73.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 50.5, 73.3)
    with step("[Action] Tap Collections at (65.3%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collections', 65.3, 66.7)
    with step("[Action] Tap _Video at (27.1%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_Video', 27.1, 61.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albums-shelf-scrollView', container_w=430, container_h=120)
    with step("[Action] Tap photos_layout at (51.6%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photos_layout', 51.6, 51.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photosView_content_scroll_view', container_w=430, container_h=863)
    with step("[Action] Tap Choose at (23.8%, 78.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Choose', 23.8, 78.3)
    with step("[Action] Drag startBarImageView (37.5%,61.1%) → //XCUIElementTypeOther[@name=\"slidingWindow\"]/XCUIElementTypeOther[3] (20.1%,65.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'startBarImageView', 37.5, 61.1, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="slidingWindow"]/XCUIElementTypeOther[3]', 20.1, 65.9, duration=1.0)
    with step("[Action] Drag endBarImageView (100.0%,66.7%) → thumbnailsView (80.8%,64.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'endBarImageView', 100.0, 66.7, AppiumBy.ACCESSIBILITY_ID, 'thumbnailsView', 80.8, 64.7, duration=1.0)
    with step("[Action] Tap btnNext at (27.2%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 27.2, 70.0)
    with step("[Verify] Capture '00182_motion_swap_01_Step32' for GT comparison"):
        actions.capture_for_gt('00182_motion_swap_01_Step32', AppiumBy.ACCESSIBILITY_ID, 'btnImportReference', threshold=0.85)
    with step("[Action] Tap Keep the photo background at (20.1%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Keep the photo background', 20.1, 56.5)
    with step("[Action] Tap Generate at (65.4%, 54.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 65.4, 54.2)
    with step("[Verify] labelProcessing is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing')
    with step("[Action] Tap btnBack at (58.1%, 61.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 58.1, 61.3)
    with step("[Action] Tap chevronView at (27.3%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevronView', 27.3, 56.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editScrollView', container_w=394, container_h=542)
    with step("[Action] Tap Kling Motion Control at (35.0%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Kling Motion Control', 35.0, 52.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeTable', container_w=394, container_h=176)
    with step("[Action] Tap Generate at (80.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 80.0, 50.0)
    with step("[Verify] labelProcessing disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing', appear_timeout=5, disappear_timeout=1200), 'labelProcessing did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (61.3%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 61.3, 64.5)
    with step("[Action] Tap navArtworkButton at (36.4%, 34.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navArtworkButton', 36.4, 34.1)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Verify] labelProcessing disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing', appear_timeout=5, disappear_timeout=1200), 'labelProcessing did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap Create More at (53.6%, 68.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Create More', 53.6, 68.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Action] Tap btnImportFace at (52.8%, 41.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace', 52.8, 41.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editScrollView', container_w=394, container_h=542)
    with step("[Action] Tap photoCell-3 at (59.2%, 37.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3', 59.2, 37.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap btnImportReference at (47.7%, 42.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference', 47.7, 42.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editScrollView', container_w=394, container_h=542)
    with step("[Action] Tap btnNext at (44.8%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 44.8, 30.0)
    with step("[Action] Tap Collections at (58.9%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collections', 58.9, 62.5)
    with step("[Action] Tap _Video at (66.7%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_Video', 66.7, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albums-shelf-scrollView', container_w=430, container_h=120)
    with step("[Action] Tap photos_layout at (49.8%, 43.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photos_layout', 49.8, 43.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photosView_content_scroll_view', container_w=430, container_h=863)
    with step("[Action] Tap Choose at (49.2%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Choose', 49.2, 52.2)
    with step("[Action] Tap Continue at (36.8%, 18.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 36.8, 18.2)
    with step("[Action] Tap btnImportReference at (46.4%, 33.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference', 46.4, 33.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editScrollView', container_w=394, container_h=542)
    with step("[Action] Tap Continue at (59.5%, 31.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 59.5, 31.8)
    with step("[Action] Tap Collections at (73.7%, 45.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collections', 73.7, 45.8)
    with step("[Action] Tap _Video at (31.2%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_Video', 31.2, 61.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albums-shelf-scrollView', container_w=430, container_h=120)
    with step("[Action] Tap photos_layout at (16.7%, 49.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photos_layout', 16.7, 49.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photosView_content_scroll_view', container_w=430, container_h=863)
    with step("[Action] Tap Choose at (68.3%, 82.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Choose', 68.3, 82.6)
    with step("[Action] Tap Continue at (36.8%, 86.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 36.8, 86.4)
    with step("[Verify] Capture '00182_motion_swap_01_Step57' for GT comparison"):
        actions.capture_for_gt('00182_motion_swap_01_Step57', AppiumBy.ACCESSIBILITY_ID, 'btnImportReference', threshold=0.55)
    with step("[Action] Tap btnHome at (63.3%, 73.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 63.3, 73.3)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
