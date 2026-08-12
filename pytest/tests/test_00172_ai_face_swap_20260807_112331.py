import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00172_ai_face_swap_20260807_112331")
def test_00172_ai_face_swap_20260807_112331(actions: DriverActions):
    with step("[Action] Tap btnStudio at (39.5%, 47.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnStudio', 39.5, 47.3)
    with step("[Action] Scroll until AI Face Swap"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap', direction='down', offset_start=(0.74, 0.405), offset_end=(0.74, 0.289), velocity=225)
    with step("[Action] Tap AI Face Swap at (59.8%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap', 59.8, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap btnNext at (89.9%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 89.9, 40.8)
    with step("[Action] Tap btnNext at (76.3%, 56.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 76.3, 56.7)
    with step("[Action] Tap maleButton at (79.5%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'maleButton', 79.5, 68.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="topBar"]/XCUIElementTypeScrollView', container_w=394, container_h=44)
    with step("[Action] Tap Muscular at (54.7%, 29.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Muscular', 54.7, 29.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='tagSelection_collectionView', container_w=412, container_h=44)
    with step("[Action] Tap CMS-Style_066_Muscular-Male-06 at (50.0%, 47.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_066_Muscular-Male-06', 50.0, 47.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='templateSelection_styleCollectionView', container_w=394, container_h=643)
    with step("[Action] Tap addSourceFaceButton at (19.7%, 49.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'addSourceFaceButton', 19.7, 49.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='addFaceCollectionView', container_w=394, container_h=79)
    with step("[Verify] descriptionLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel')
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (79.9%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 79.9, 40.8)
    with step("[Action] Tap btnAlbum at (91.4%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 91.4, 71.4)
    with step("[Action] Tap _AT at (15.8%, 86.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 15.8, 86.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-5 at (37.7%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5', 37.7, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] The face in this photo is too small or blurry, which may result in poorly generated results. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'The face in this photo is too small or blurry, which may result in poorly generated results.')
    with step("[Action] Tap AlertDialog-btnPositive at (32.0%, 36.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 32.0, 36.0)
    with step("[Action] Tap photoCell-1 at (24.6%, 47.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 24.6, 47.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] No face detected. A face is required for this feature. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'No face detected. A face is required for this feature.')
    with step("[Action] Tap AlertDialog-btnPositive at (67.4%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 67.4, 38.8)
    with step("[Action] Tap photoCell-5 at (42.3%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5', 42.3, 40.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Continue Anyway at (15.2%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway', 15.2, 52.0)
    with step("[Verify] faceValidationProgress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'faceValidationProgress', appear_timeout=5, disappear_timeout=1200), 'faceValidationProgress did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap multipleAddFace_generateButton at (17.3%, 28.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'multipleAddFace_generateButton', 17.3, 28.3)
    with step("[Verify] Turn it into video is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Turn it into video')
    with step("[Action] Tap btnSave at (62.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSave', 62.5, 60.0)
    with step("[Action] Tap Collage at (61.4%, 35.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collage', 61.4, 35.0)
    with step("[Action] Tap saveBtn at (61.1%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'saveBtn', 61.1, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=737)
    with step("[Action] Tap btnShareFB at (41.5%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB', 41.5, 51.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=737)
    with step("[Verify] FBComposerView is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'FBComposerView')
    with step("[Action] Tap composer-left-button at (40.9%, 44.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'composer-left-button', 40.9, 44.2)
    with step("[Action] Tap Discard at (61.5%, 46.7%)"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Discard'):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 61.5, 46.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Discard post?"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=270, container_h=45)
    with step("[Action] Tap btnShareIG at (59.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareIG', 59.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=737)
    with step("[Verify] Share to Instagram is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram')
    with step("[Action] Tap //XCUIElementTypeApplication[@name=\"Instagram\"]/XCUIElementTypeWindow/XCUIElementTypeOther[2] at (10.7%, 4.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="Instagram"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]', 10.7, 4.4)
    with step("[Action] Tap btnShareMore at (61.5%, 38.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareMore', 61.5, 38.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=737)
    with step("[Verify] //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[6]/XCUIElementTypePopover is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[6]/XCUIElementTypePopover')
    with step("[Action] Tap PopoverDismissRegion at (5.3%, 49.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PopoverDismissRegion', 5.3, 49.4)
    with step("[Action] Tap navHomeButton at (70.5%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton', 70.5, 55.6)
    with step("[Action] Tap Edit at (51.4%, 36.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 51.4, 36.0)
    with step("[Action] Tap btnAlbum at (79.2%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 79.2, 57.1)
    with step("[Action] Tap _AT at (10.0%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.0, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (26.2%, 60.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 26.2, 60.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (79.7%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 79.7, 51.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until ic_face_swap"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_face_swap', direction='left', offset_start=(0.616, 0.361), offset_end=(0.235, 0.361), velocity=171)
    with step("[Action] Tap ic_face_swap at (47.1%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_swap', 47.1, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btnNext at (77.3%, 38.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 77.3, 38.3)
    with step("[Verify] Crop to Continue is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Crop to Continue')
    with step("[Action] Tap AlertDialog-btnPositive at (69.0%, 75.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 69.0, 75.5)
    with step("[Action] Tap btn_ok_n at (73.5%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 53.1)
    with step("[Verify] Capture '00172_ai_face_swap_Step49' for GT comparison"):
        actions.capture_for_gt('00172_ai_face_swap_Step49', AppiumBy.ACCESSIBILITY_ID, 'referenceImageView', threshold=0.95)
    with step("[Action] Tap btnHome at (65.0%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 65.0, 57.5)
    with step("[Action] Tap Edit at (54.3%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 54.3, 56.0)
    with step("[Action] Tap btnAlbum at (80.7%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 80.7, 54.8)
    with step("[Action] Tap _AT at (8.2%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.2, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (35.4%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 35.4, 70.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (44.6%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 44.6, 46.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until ic_face_swap"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_face_swap', direction='left', offset_start=(0.772, 0.402), offset_end=(0.184, 0.402), velocity=602)
    with step("[Action] Tap ic_face_swap at (61.8%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_swap', 61.8, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Action] Tap btnNext at (89.2%, 56.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 89.2, 56.7)
    with step("[Action] Tap AlertDialog-btnPositive at (77.8%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 77.8, 53.1)
    with step("[Action] Tap btn_ok_n at (81.6%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 46.9)
    with step("[Action] Tap addSourceFaceButton at (32.4%, 97.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'addSourceFaceButton', 32.4, 97.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='addFaceCollectionView', container_w=394, container_h=79)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (78.3%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 78.3, 42.9)
    with step("[Action] Tap btnAlbum at (90.9%, 59.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 90.9, 59.5)
    with step("[Action] Tap _AT at (7.9%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-5 at (41.5%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5', 41.5, 76.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Continue Anyway at (26.4%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway', 26.4, 58.3)
    with step("[Verify] faceValidationProgress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'faceValidationProgress', appear_timeout=5, disappear_timeout=1200), 'faceValidationProgress did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap multipleAddFace_generateButton at (19.3%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'multipleAddFace_generateButton', 19.3, 46.7)
    with step("[Verify] Turn it into video is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Turn it into video')
    with step("[Action] Tap navBackButton at (60.0%, 72.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 60.0, 72.5)
    with step("[Verify] infoLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'infoLabel')
    with step("[Action] Tap sourceImageView at (25.4%, 53.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'sourceImageView', 25.4, 53.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='addFaceCollectionView', container_w=394, container_h=79)
    with step("[Action] Tap btnAlbum at (82.2%, 69.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 82.2, 69.0)
    with step("[Action] Tap Xsilva at (19.0%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Xsilva', 19.0, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-1 at (63.8%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 63.8, 46.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    # with step("[Verify] faceValidationProgress disappears within 1200s"):
    #     assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'faceValidationProgress', appear_timeout=5, disappear_timeout=1200), 'faceValidationProgress did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Celebrity face detected in the uploaded image and it may violate our terms. Please choose another one. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Celebrity face detected in the uploaded image and it may violate our terms. Please choose another one.')
    with step("[Action] Tap OK at (28.6%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 28.6, 50.0)
    with step("[Action] Tap btnBack at (65.0%, 56.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 65.0, 56.1)
    with step("[Action] Tap btnHome at (52.5%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 52.5, 67.5)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
