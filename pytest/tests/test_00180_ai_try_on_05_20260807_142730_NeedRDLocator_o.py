import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00180_ai_try_on_05_20260807_142730")
def test_00180_ai_try_on_05_20260807_142730(actions: DriverActions):
    with step("[Action] Tap AI Photos at (51.4%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 51.4, 45.5)
    with step("[Action] Tap AI Try-On at (71.2%, 72.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', 71.2, 72.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap Try now"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnNext', timeout=3):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap thumbnailImageView at (76.0%, 85.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importButton', 76.0, 85.5)
    with step("[Action] Tap importLabel at (85.2%, 47.5%)"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'importLabel', timeout=3):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importLabel', 85.2, 47.5)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (33.9%, 73.5%)"):
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', timeout=3
        ):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 33.9, 73.5
            )
    with step("[Action] Tap btnAlbum at (70.1%, 59.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 70.1, 59.5)
    with step("[Action] Tap _AT at (10.0%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.0, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (46.2%, 18.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 46.2, 18.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Custom at (48.9%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Custom', 48.9, 75.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Action] Tap titleLabel at (50.3%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'uploadClothingPhotoButton', 50.3, 59.1)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (19.6%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 19.6, 69.4)
    with step("[Action] Tap btnAlbum at (66.0%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 66.0, 66.7)
    with step("[Action] Tap _AT at (8.6%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.6, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=632)
    with step("[Action] Tap photoCell-3 at (66.9%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3', 66.9, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Verify] //XCUIElementTypeOther[@name=\"selectionContainerView\"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage')
    with step("[Action] Tap btn FontDelete n at (63.6%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n', 63.6, 63.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=430, container_h=74)
    with step("[Verify] //XCUIElementTypeOther[@name=\"selectionContainerView\"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage is not visible"):
        actions.verify_not_visible(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage')
    with step("[Action] Tap photoCell-3 at (60.0%, 33.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3', 60.0, 33.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap photoCell-5 at (45.4%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5', 45.4, 42.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Verify] //XCUIElementTypeOther[@name=\"selectionContainerView\"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeImage is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeImage')
    with step("[Verify] //XCUIElementTypeOther[@name=\"selectionContainerView\"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeImage is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeImage')
    with step("[Action] Tap Next at (0.0%, 42.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next', 0.0, 42.1)
    with step("[Action] Tap Generate at (46.9%, 12.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 46.9, 12.5)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (61.3%, 83.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 61.3, 83.9)
    with step("[Action] Tap Photo at (63.6%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Photo', 63.6, 75.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (6.1%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 6.1, 26.5)
    with step("[Action] Tap photoCell-6 at (55.4%, 49.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 55.4, 49.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Verify] //XCUIElementTypeOther[@name=\"selectionContainerView\"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeImage is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeImage')
    with step("[Verify] //XCUIElementTypeOther[@name=\"selectionContainerView\"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeImage is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeImage')
    with step("[Verify] //XCUIElementTypeOther[@name=\"selectionContainerView\"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeImage is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeImage')
    with step("[Action] Tap photoCell-1 at (46.2%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 46.2, 69.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Verify] Capture '00180_ai_try_on_05_Step33' for GT comparison"):
        actions.capture_for_gt('00180_ai_try_on_05_Step33', AppiumBy.ACCESSIBILITY_ID, 'selectionContainerView', threshold=0.95)
    with step("[Action] Tap Next at (70.6%, 5.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next', 70.6, 5.3)
    with step("[Action] Tap btnGenerate at (56.6%, 37.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 56.6, 37.1)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (64.5%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 64.5, 64.5)
    with step("[Action] Tap clearButton at (72.2%, 72.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'clearButton', 72.2, 72.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Action] Tap Custom at (31.8%, 20.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Custom', 31.8, 20.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Verify] containerView is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'containerView')
    with step("[Verify] titleLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'titleLabel')
    with step("[Action] Tap AITryOnStyleSelectionViewController at (9.5%, 10.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AITryOnStyleSelectionViewController', 9.5, 10.2)
    with step("[Action] Tap navBackButton at (60.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 60.0, 52.5)
    with step("[Action] Tap navBackButton at (46.2%, 50.0%)"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', timeout=3):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 46.2, 50.0)
    with step("[Action] Tap btnHome at (48.7%, 21.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 48.7, 21.8)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
