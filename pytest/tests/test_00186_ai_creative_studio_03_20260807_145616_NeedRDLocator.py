import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00186_ai_creative_studio_03_20260807_145616")
def test_00186_ai_creative_studio_03_20260807_145616(actions: DriverActions):
    with step("[Action] Tap AI Photos at (43.1%, 27.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 43.1, 27.3)
    with step("[Action] Scroll until AI Creative Studio"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', direction='down', offset_start=(0.341, 0.169), offset_end=(0.341, 0.137), velocity=50)
    with step("[Action] Tap AI Creative Studio at (65.9%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', 65.9, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap Portrait at (38.9%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 38.9, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=28)
    with step("[Action] Scroll until CMS-CreativeStudio_Template_Portrait"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AICreativeStudioTemplateViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'CMS-CreativeStudio_Template_Portrait', direction='down', offset_start=(0.707, 0.635), offset_end=(0.707, 0.111), velocity=668)
    with step("[Action] Tap CMS-CreativeStudio_Template_Portrait at (43.5%, 60.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-CreativeStudio_Template_Portrait', 43.5, 60.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AICreativeStudioTemplatePageContentViewController', container_w=430, container_h=682)
    with step("[Action] Tap addIconView at (47.5%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'addIconView', 47.5, 45.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='aiCreativeStudioPhotoListPanelCollectionView', container_w=386, container_h=62)
    with step("[Action] Tap btnAlbum at (80.2%, 59.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 80.2, 59.5)
    with step("[Action] Tap _AT at (9.7%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.7, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=632)
    with step("[Action] Tap photoCell-4 at (56.9%, 33.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4', 56.9, 33.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap photoCell-2 at (53.8%, 39.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 53.8, 39.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap Next at (44.1%, 63.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next', 44.1, 63.2)
    with step("[Verify] Capture '00186_ai_creative_studio_03_Step13' for GT comparison"):
        actions.capture_for_gt('00186_ai_creative_studio_03_Step13', AppiumBy.ACCESSIBILITY_ID, 'photoListPanel', threshold=0.95)
    with step("[Action] Long press drag (//XCUIElementTypeImage[@name=\"imageView\"])[2] (69.7%,60.5%) → AICreativeStudioPhotoThumbnailCell-0 (7.9%,56.6%)"):
        actions.long_press_drag_within_elements(AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="imageView"])[2]', 69.7, 60.5, AppiumBy.ACCESSIBILITY_ID, 'AICreativeStudioPhotoThumbnailCell-0', 7.9, 56.6, duration=1.11, press_duration=1.45)
    with step("[Verify] Capture '00186_ai_creative_studio_03_Step15' for GT comparison"):
        actions.capture_for_gt('00186_ai_creative_studio_03_Step15', AppiumBy.ACCESSIBILITY_ID, 'photoListPanel', threshold=0.95)
    with step("[Action] Tap Generate at (66.7%, 60.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 66.7, 60.9)
    with step("[Verify] statusLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'statusLabel')
    with step("[Action] Tap btnBack at (71.0%, 19.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 71.0, 19.4)
    with step("[Action] Tap aiCreativeStudioRouter_backButton at (80.8%, 51.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton', 80.8, 51.9)
    with step("[Action] Tap CMS-CreativeStudio_Template_Portrait at (53.9%, 52.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-CreativeStudio_Template_Portrait', 53.9, 52.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AICreativeStudioTemplatePageContentViewController', container_w=430, container_h=682)
    with step("[Action] Tap addIconView at (70.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'addIconView', 70.0, 52.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='aiCreativeStudioPhotoListPanelCollectionView', container_w=386, container_h=62)
    with step("[Action] Tap photoCell-4 at (43.1%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4', 43.1, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap photoCell-2 at (33.1%, 56.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 33.1, 56.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap Next at (73.5%, 57.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next', 73.5, 57.9)
    with step("[Action] Tap generateButton at (54.5%, 24.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'generateButton', 54.5, 24.5)
    with step("[Verify] statusLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'statusLabel')
    with step("[Action] Tap btnBack at (54.8%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 54.8, 64.5)
    with step("[Action] Tap aiCreativeStudioRouter_backButton at (84.6%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton', 84.6, 44.4)
    with step("[Action] Tap Creative at (19.5%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Creative', 19.5, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=28)
    with step("[Action] Tap CMS-CreativeStudio_Template_Creative at (68.4%, 46.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-CreativeStudio_Template_Creative', 68.4, 46.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AICreativeStudioTemplatePageContentViewController', container_w=430, container_h=682)
    with step("[Action] Tap addIconView at (82.5%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'addIconView', 82.5, 57.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='aiCreativeStudioPhotoListPanelCollectionView', container_w=386, container_h=62)
    with step("[Action] Tap photoCell-2 at (58.5%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 58.5, 46.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap Next at (26.5%, 36.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next', 26.5, 36.8)
    with step("[Action] Tap Generate at (8.6%, 13.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 8.6, 13.0)
    with step("[Verify] statusLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'statusLabel')
    with step("[Action] Tap btnBack at (32.3%, 35.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 32.3, 35.5)
    with step("[Action] Tap aiCreativeStudioRouter_backButton at (34.6%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton', 34.6, 66.7)
    with step("[Action] Tap CMS-CreativeStudio_Template_Creative at (51.3%, 54.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-CreativeStudio_Template_Creative', 51.3, 54.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AICreativeStudioTemplatePageContentViewController', container_w=430, container_h=682)
    with step("[Action] Tap addIconView at (52.5%, 85.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'addIconView', 52.5, 85.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='aiCreativeStudioPhotoListPanelCollectionView', container_w=386, container_h=62)
    with step("[Action] Tap photoCell-2 at (21.5%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 21.5, 59.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap btnNext at (45.7%, 80.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 45.7, 80.6)
    with step("[Action] Tap generateButton at (24.1%, 43.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'generateButton', 24.1, 43.4)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (64.5%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 64.5, 64.5)
    with step("[Action] Tap aiCreativeStudioRouter_homeButton at (42.3%, 63.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_homeButton', 42.3, 63.0)
    with step("[Action] Tap btnHome at (43.4%, 23.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 43.4, 23.6)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
