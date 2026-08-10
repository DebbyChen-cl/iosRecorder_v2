import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00161_ai_hairstyle_20260806_184225")
def test_00161_ai_hairstyle_20260806_184225(actions: DriverActions):
    with step("[Action] Tap btnStudio at (56.6%, 38.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnStudio', 56.6, 38.2)
    with step("[Action] Scroll until AI Hairstyle"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle', direction='down', offset_start=(0.255, 0.374), offset_end=(0.255, 0.315), velocity=72)
    with step("[Action] Tap AI Hairstyle at (70.5%, 57.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle', 70.5, 57.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Action] Tap notShowAgainCheckBox at (40.7%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox', 40.7, 53.8)
    with step("[Action] Tap btnNext at (76.5%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 76.5, 40.8)
    with step("[Action] Tap Male at (80.6%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Male', 80.6, 45.0)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CMS-Style_8027_Male-Classic-Side_Gemini\"]/XCUIElementTypeOther[1]/XCUIElementTypeImage at (68.2%, 76.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-Style_8027_Male-Classic-Side_Gemini"]/XCUIElementTypeOther[1]/XCUIElementTypeImage', 68.2, 76.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=358)
    with step("[Action] Tap importLabel at (50.0%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importLabel', 50.0, 57.5)
    with step("[Verify] descriptionLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel')
    with step("[Action] Tap PhotoPickerRecommendDialog-notShowAgainCheckBox at (77.8%, 63.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox', 77.8, 63.0)
    with step("[Action] Tap Continue at (36.5%, 13.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 36.5, 13.0)
    with step("[Action] Tap ic info n at (60.0%, 46.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic info n', 60.0, 46.3)
    with step("[Verify] descriptionLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel')
    with step("[Action] Tap Continue at (14.9%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 14.9, 52.2)
    with step("[Action] Tap btnAlbum at (77.7%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 77.7, 47.6)
    with step("[Action] Tap _AT at (8.6%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.6, 52.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-3 at (29.2%, 54.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3', 29.2, 54.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture '00161_ai_hairstyle_Step19' for GT comparison"):
        actions.capture_for_gt('00161_ai_hairstyle_Step19', AppiumBy.ACCESSIBILITY_ID, 'importButton', threshold=0.95)
    with step("[Action] Tap importButton at (45.9%, 53.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importButton', 45.9, 53.9)
    with step("[Verify] btnCamera is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnCamera')
    with step("[Action] Tap btnBack at (75.0%, 29.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 75.0, 29.3)
    with step("[Action] Tap Generate at (59.3%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 59.3, 50.0)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap selectCheckBoxOverlay at (27.2%, 21.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'selectCheckBoxOverlay', 27.2, 21.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap btnDownload at (75.0%, 32.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDownload', 75.0, 32.0)
    with step("[Action] Tap btnEdit at (69.2%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnEdit', 69.2, 80.0)
    with step("[Action] Tap Portrait at (44.6%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 44.6, 48.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_hair at (51.5%, 84.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_hair', 51.5, 84.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_hairstyle at (84.8%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_hairstyle', 84.8, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap importButton at (45.7%, 48.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importButton', 45.7, 48.7)
    with step("[Action] Tap Continue at (43.2%, 30.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 43.2, 30.4)
    with step("[Action] Tap btnAlbum at (82.2%, 40.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 82.2, 40.5)
    with step("[Action] Tap _AT at (8.6%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.6, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-1 at (19.2%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 19.2, 57.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Please choose another photo. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Please choose another photo.')
    with step("[Action] Tap OK at (60.7%, 39.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 60.7, 39.1)
    with step("[Action] Tap photoCell-4 at (32.3%, 43.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4', 32.3, 43.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] More than one person detected. Try choosing another one. Thank you. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'More than one person detected. Try choosing another one. Thank you.')
    with step("[Action] Tap OK at (85.7%, 87.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 85.7, 87.0)
    with step("[Action] Tap photoCell-2 at (71.5%, 43.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 71.5, 43.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Female at (87.0%, 90.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Female', 87.0, 90.0)
    with step("[Action] Tap Luxe Waves at (55.7%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Luxe Waves', 55.7, 30.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=358)
    with step("[Action] Tap Generate at (66.7%, 54.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 66.7, 54.2)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap selectCheckBoxOverlay at (57.8%, 53.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'selectCheckBoxOverlay', 57.8, 53.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap btnDownload at (45.8%, 32.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDownload', 45.8, 32.0)
    with step("[Action] Tap btnBack at (77.4%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 77.4, 48.4)
    with step("[Action] Tap btnBack at (38.7%, 32.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 38.7, 32.3)
    with step("[Action] Tap navBackButton at (52.5%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 52.5, 47.5)
    with step("[Action] Tap homeButton at (57.7%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 57.7, 69.2)
    with step("[Action] Tap btnHome at (59.2%, 41.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 59.2, 41.8)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
