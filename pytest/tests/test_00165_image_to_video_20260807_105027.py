import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00165_image_to_video_20260807_105027")
def test_00165_image_to_video_20260807_105027(actions: DriverActions):
    with step("[Action] Tap Image to Video at (54.2%, 35.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Image to Video', 54.2, 35.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Action] Tap btnNext at (19.3%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 19.3, 44.9)
    with step("[Action] Tap btnNext at (8.5%, 31.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 8.5, 31.7)
    with step("[Action] Tap navArtworkButton at (69.2%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navArtworkButton', 69.2, 48.1)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Action] Tap thumbnailImageView at (58.8%, 64.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'thumbnailImageView', 58.8, 64.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='packCollectionView', container_w=394, container_h=668)
    with step("[Action] Tap btnSave at (13.0%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSave', 13.0, 55.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.VideoExportViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=779)
    with step("[Action] Tap btnShareFB at (31.4%, 53.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB', 31.4, 53.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.VideoExportViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=779)
    with step("[Verify] New post is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'New post')
    with step("[Action] Tap composer-left-button at (43.2%, 44.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'composer-left-button', 43.2, 44.2)
    with step("[Action] Tap Discard at (55.6%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 55.6, 51.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Discard post?"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=270, container_h=45)
    with step("[Action] Tap btnShareIG at (44.4%, 46.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareIG', 44.4, 46.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.VideoExportViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=779)
    with step("[Verify] Share to Instagram is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram')
    with step("[Action] Tap //XCUIElementTypeApplication[@name=\"Instagram\"]/XCUIElementTypeWindow/XCUIElementTypeOther[2] at (5.6%, 4.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="Instagram"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]', 5.6, 4.5)
    with step("[Action] Tap btnShareMore at (48.7%, 36.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareMore', 48.7, 36.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.VideoExportViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=779)
    with step("[Verify] //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[5]/XCUIElementTypePopover is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[5]/XCUIElementTypePopover')
    with step("[Action] Tap PopoverDismissRegion at (6.5%, 33.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PopoverDismissRegion', 6.5, 33.4)
    with step("[Action] Tap btnPlay at (54.5%, 46.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 54.5, 46.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.VideoExportViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=779)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'photodirector.VideoFullSizePreviewViewController')
    with step("[Action] Tap btnPlay at (48.3%, 51.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 48.3, 51.7)
    with step("[Action] Tap btnPlay at (48.3%, 51.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 48.3, 51.7)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'photodirector.VideoFullSizePreviewViewController', expected_result='different', threshold=0.95)
    with step("[Action] Tap navBackButton at (59.1%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 59.1, 50.0)
    with step("[Action] Tap navHomeButton at (73.3%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton', 73.3, 53.3)
    with step("[Action] Tap Image to Video at (61.5%, 59.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Image to Video', 61.5, 59.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Action] Tap btnNext at (88.1%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 88.1, 42.9)
    with step("[Action] Tap btnNext at (85.8%, 56.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 85.8, 56.7)
    with step("[Action] Tap View All at (71.2%, 22.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'View All', 71.2, 22.2)
    with step("[Action] Tap Life at (58.3%, 52.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Life', 58.3, 52.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=44)
    with step("[Action] Scroll until High Five"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'imageToVideoSeeAllPageViewCollectionView', AppiumBy.ACCESSIBILITY_ID, 'High Five', direction='down', offset_start=(0.259, 0.749), offset_end=(0.259, 0.103), velocity=787)
    with step("[Action] Tap High Five at (22.3%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'High Five', 22.3, 48.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageToVideoSeeAllPageViewCollectionView', container_w=394, container_h=682)
    with step("[Action] Tap Try with Example at (68.8%, 100.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try with Example', 68.8, 100.0)
    with step("[Verify] Capture '00165_image_to_video_Step34' for GT comparison"):
        actions.capture_for_gt('00165_image_to_video_Step34', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="duoScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap replaceImageButton at (69.2%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'replaceImageButton', 69.2, 46.2)
    with step("[Action] Tap btnNext at (20.8%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 20.8, 53.1)
    with step("[Action] Tap btnAlbum at (85.8%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 85.8, 52.4)
    with step("[Action] Tap _AT at (12.9%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 12.9, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-4 at (48.5%, 43.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4', 48.5, 43.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture '00165_image_to_video_Step40' for GT comparison"):
        actions.capture_for_gt('00165_image_to_video_Step40', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="duoScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap 2 Solo Photos at (48.1%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '2 Solo Photos', 48.1, 71.4)
    with step("[Action] Tap Try with Example at (60.6%, 30.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try with Example', 60.6, 30.4)
    with step("[Verify] Capture '00165_image_to_video_Step43' for GT comparison"):
        actions.capture_for_gt('00165_image_to_video_Step43', AppiumBy.ACCESSIBILITY_ID, 'editArea', threshold=0.95)
    with step("[Action] Tap exampleImageView at (51.3%, 49.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'exampleImageView', 51.3, 49.6)
    with step("[Action] Tap btnAlbum at (92.9%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 92.9, 66.7)
    with step("[Action] Tap _AT at (11.1%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 11.1, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (56.2%, 47.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 56.2, 47.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture '00165_image_to_video_Step48' for GT comparison"):
        actions.capture_for_gt('00165_image_to_video_Step48', AppiumBy.ACCESSIBILITY_ID, 'editArea', threshold=0.95)
    with step("[Action] Tap replaceImageButton at (48.1%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'replaceImageButton', 48.1, 69.2)
    with step("[Action] Tap photoCell-5 at (33.1%, 63.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5', 33.1, 63.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap imageSettingView at (79.4%, 61.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageSettingView', 79.4, 61.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=110)
    with step("[Action] Tap button_5s at (70.0%, 72.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_5s', 70.0, 72.2)
    with step("[Action] Tap button_10s at (82.0%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_10s', 82.0, 61.1)
    with step("[Action] Tap Pro at (45.5%, 25.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro', 45.5, 25.0)
    with step("[Action] Tap button_Standard at (11.2%, 72.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_Standard', 11.2, 72.2)
    with step("[Action] Tap btn_cancel_n at (57.1%, 61.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 57.1, 61.2)
    with step("[Action] Tap creditGenerateButton at (65.5%, 66.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'creditGenerateButton', 65.5, 66.1)
    with step("[Verify] titleLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'titleLabel')
    with step("[Action] Tap btnBack at (58.1%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 58.1, 54.8)
    with step("[Action] Tap View All at (40.4%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'View All', 40.4, 33.3)
    with step("[Action] Tap Life at (77.1%, 52.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Life', 77.1, 52.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=44)
    with step("[Action] Tap Rich at (19.7%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Rich', 19.7, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageToVideoSeeAllPageViewCollectionView', container_w=394, container_h=682)
    with step("[Action] Tap Try with Example at (58.7%, 30.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try with Example', 58.7, 30.4)
    with step("[Verify] Capture '00165_image_to_video_Step65' for GT comparison"):
        actions.capture_for_gt('00165_image_to_video_Step65', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="singleScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap replaceImageButton at (42.3%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'replaceImageButton', 42.3, 69.2)
    with step("[Action] Tap btnNext at (16.0%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 16.0, 46.9)
    with step("[Action] Tap photoCell-2 at (60.0%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 60.0, 65.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture '00165_image_to_video_Step69' for GT comparison"):
        actions.capture_for_gt('00165_image_to_video_Step69', AppiumBy.ACCESSIBILITY_ID, 'singleScrollView', threshold=0.95)
    with step("[Action] Tap imageSettingView at (73.5%, 76.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageSettingView', 73.5, 76.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=110)
    with step("[Action] Tap button_10s at (76.0%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_10s', 76.0, 69.4)
    with step("[Verify] Capture '00165_image_to_video_Step72' for GT comparison"):
        actions.capture_for_gt('00165_image_to_video_Step72', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap button_5s at (74.0%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_5s', 74.0, 61.1)
    with step("[Action] Tap button_Pro at (78.4%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_Pro', 78.4, 58.3)
    with step("[Verify] Capture '00165_image_to_video_Step75' for GT comparison"):
        actions.capture_for_gt('00165_image_to_video_Step75', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Standard at (12.5%, 81.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Standard', 12.5, 81.2)
    with step("[Action] Tap btn_cancel_n at (10.2%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 10.2, 36.7)
    with step("[Action] Tap creditGenerateButton at (8.2%, 41.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'creditGenerateButton', 8.2, 41.9)
    with step("[Verify] titleLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'titleLabel')
    with step("[Verify] processingLabel disappears within 1200s"):
            assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'processingLabel', appear_timeout=5, disappear_timeout=1200), 'processingLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (35.5%, 58.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 35.5, 58.1)
    with step("[Action] Tap View All at (44.2%, 100.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'View All', 44.2, 100.0)
    with step("[Action] Tap Female at (54.9%, 58.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Female', 54.9, 58.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=388, container_h=46)
    with step("[Action] Tap All at (57.4%, 67.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'All', 57.4, 67.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=388, container_h=46)
    with step("[Action] Tap btnBack at (52.5%, 65.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 52.5, 65.9)
    with step("[Action] Tap navBackButton at (50.0%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 50.0, 58.5)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
