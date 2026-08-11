import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00185_ai_creative_studio_02_20260807_145017")
def test_00185_ai_creative_studio_02_20260807_145017(actions: DriverActions):
    with step("[Action] Tap AI Photos at (66.7%, 86.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 66.7, 86.4)
    with step("[Action] Scroll until AI Creative Studio"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', direction='down', offset_start=(0.396, 0.192), offset_end=(0.396, 0.162), velocity=50)
    with step("[Action] Tap AI Creative Studio at (73.2%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', 73.2, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Action] Tap notShowAgainCheckBox at (77.8%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox', 77.8, 65.4)
    with step("[Action] Tap btnNext at (25.5%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 25.5, 32.7)
    with step("[Action] Tap Collage at (36.1%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collage', 36.1, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=28)
    with step("[Action] Tap CMS-CreativeStudio_Template_Collage at (41.5%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-CreativeStudio_Template_Collage', 41.5, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AICreativeStudioTemplatePageContentViewController', container_w=430, container_h=682)
    with step("[Verify] uploadSectionLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'uploadSectionLabel')
    with step("[Action] Tap aiCreativeStudioRouter_backButton at (76.9%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton', 76.9, 44.4)
    with step("[Action] Tap Collage at (36.1%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collage', 36.1, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=28)
    with step("[Action] Tap CMS-CreativeStudio_Template_Collage at (37.3%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-CreativeStudio_Template_Collage', 37.3, 44.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AICreativeStudioTemplatePageContentViewController', container_w=430, container_h=682)
    with step("[Action] Tap addIconView at (65.0%, 22.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'addIconView', 65.0, 22.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='aiCreativeStudioPhotoListPanelCollectionView', container_w=386, container_h=62)
    with step("[Action] Tap PhotoPickerRecommendDialog-notShowAgainCheckBox at (74.1%, 70.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox', 74.1, 70.4)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (82.8%, 8.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 82.8, 8.2)
    with step("[Action] Tap btnAlbum at (74.1%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 74.1, 61.9)
    with step("[Action] Tap _AT at (9.0%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.0, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=632)
    with step("[Action] Tap photoCell-1 at (56.2%, 72.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 56.2, 72.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap photoCell-2 at (50.8%, 47.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 50.8, 47.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap photoCell-0 at (43.8%, 52.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 43.8, 52.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap photoCell-3 at (52.3%, 66.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3', 52.3, 66.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Verify] Capture '00185_ai_creative_studio_02_Step22' for GT comparison"):
        actions.capture_for_gt('00185_ai_creative_studio_02_Step22', AppiumBy.ACCESSIBILITY_ID, 'selectionContainerView', threshold=0.95)
    with step("[Action] Tap btn FontDelete n at (50.0%, 22.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n', 50.0, 22.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=430, container_h=74)
    with step("[Action] Tap btn FontDelete n at (63.6%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n', 63.6, 63.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=430, container_h=74)
    with step("[Action] Tap btn FontDelete n at (59.1%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n', 59.1, 68.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=430, container_h=74)
    with step("[Action] Tap btn FontDelete n at (59.1%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n', 59.1, 54.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=430, container_h=74)
    with step("[Verify] //XCUIElementTypeOther[@name=\"selectionContainerView\"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeImage is not visible"):
        actions.verify_not_visible(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeImage')
    with step("[Action] Tap icon photo enlarge n at (38.5%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon photo enlarge n', 38.5, 53.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Verify] Capture '00185_ai_creative_studio_02_Step29' for GT comparison"):
        actions.capture_for_gt('00185_ai_creative_studio_02_Step29', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.ImageFullSizeViewController"]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap collageAddButton at (46.9%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'collageAddButton', 46.9, 46.9)
    with step("[Action] Tap btnBack at (55.0%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 55.0, 58.5)
    with step("[Action] Tap photoCell-1 at (26.9%, 49.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 26.9, 49.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap photoCell-2 at (58.5%, 62.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 58.5, 62.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap photoCell-3 at (36.2%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3', 36.2, 46.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap btnNext at (17.1%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 17.1, 69.4)
    with step("[Verify] Capture '00185_ai_creative_studio_02_Step37' for GT comparison"):
        actions.capture_for_gt('00185_ai_creative_studio_02_Step37', AppiumBy.ACCESSIBILITY_ID, 'photoListPanel', threshold=0.95)
    with step("[Action] Long press drag (//XCUIElementTypeImage[@name=\"imageView\"])[2] (34.2%,59.2%) → AICreativeStudioPhotoThumbnailCell-0 (48.7%,61.8%)"):
        actions.long_press_drag_within_elements(AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="imageView"])[2]', 34.2, 59.2, AppiumBy.ACCESSIBILITY_ID, 'AICreativeStudioPhotoThumbnailCell-0', 48.7, 61.8, duration=0.81, press_duration=1.89)
    with step("[Verify] Capture '00185_ai_creative_studio_02_Step38' for GT comparison"):
        actions.capture_for_gt('00185_ai_creative_studio_02_Step38', AppiumBy.ACCESSIBILITY_ID, 'photoListPanel', threshold=0.95)
    with step("[Action] Tap aiCreativeStudioRouter_creditButton at (87.9%, 58.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_creditButton', 87.9, 58.1)
    with step("[Action] Tap btnBack at (40.0%, 45.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 40.0, 45.7)
    with step("[Action] Tap Generate at (59.3%, 60.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 59.3, 60.9)
    with step("[Verify] AI Creative Studio is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (51.6%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 51.6, 48.4)
    with step("[Verify] templateSectionLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'templateSectionLabel')
    with step("[Action] Tap aiCreativeStudioRouter_artworkButton at (53.8%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_artworkButton', 53.8, 48.1)
    with step("[Verify] AI Creative Studio is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
    with step("[Action] Tap selectCheckBoxOverlay at (58.9%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'selectCheckBoxOverlay', 58.9, 44.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap btnShare at (57.7%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShare', 57.7, 48.0)
    with step("[Verify] PopoverDismissRegion is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'PopoverDismissRegion')
    with step("[Action] Tap UIActivityContentView at (6.8%, 88.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'UIActivityContentView', 6.8, 88.8)
    with step("[Action] Tap btnBack at (48.4%, 58.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 48.4, 58.1)
    with step("[Action] Tap btnBack at (48.4%, 58.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 48.4, 58.1)
    with step("[Action] Tap aiCreativeStudioRouter_homeButton at (46.2%, 40.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_homeButton', 46.2, 40.7)
    with step("[Action] Tap btnHome at (68.4%, 29.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 68.4, 29.1)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
