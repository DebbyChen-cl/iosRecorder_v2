import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00184_ai_creative_studio_01_20260807_144224")
def test_00184_ai_creative_studio_01_20260807_144224(actions: DriverActions):
    with step("[Action] Tap AI Photos at (70.8%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 70.8, 59.1)
    with step("[Action] Tap My Artwork at (80.8%, 64.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Artwork', 80.8, 64.7)
    with step("[Action] Scroll until AI Creative Studio"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuView', AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', direction='left', offset_start=(0.523, 0.516), offset_end=(0.37, 0.516), velocity=100)
    with step("[Action] Tap AI Creative Studio at (38.0%, 45.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', 38.0, 45.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=431, container_h=62)
    with step("[Action] Tap selectCheckBoxOverlay at (51.7%, 53.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'selectCheckBoxOverlay', 51.7, 53.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Verify] AIArtworkPackPreviewCell-0 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackPreviewCell-0')
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackPreviewCell-0')
    with step("[Action] Swipe left on //XCUIElementTypeCell[@name=\"AIArtworkPackPreviewCell-0\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage"):
        actions.swipe_on_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="AIArtworkPackPreviewCell-0"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage', 'left', velocity=680.6, from_pct_x=75.9, from_pct_y=88.1, distance_pts=341.0)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackPreviewCell-1', expected_result='different', threshold=0.95)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackPreviewCell-1')
    with step("[Action] Swipe right on //XCUIElementTypeCell[@name=\"AIArtworkPackPreviewCell-1\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage"):
        actions.swipe_on_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="AIArtworkPackPreviewCell-1"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage', 'right', velocity=527.6, from_pct_x=11.5, from_pct_y=90.7, distance_pts=325.0)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackPreviewCell-0', expected_result='different', threshold=0.95)
    with step("[Action] Tap btnShare at (76.9%, 68.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShare', 76.9, 68.0)
    with step("[Verify] PopoverDismissRegion is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'PopoverDismissRegion')
    with step("[Action] Tap PopoverDismissRegion at (49.5%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PopoverDismissRegion', 49.5, 49.0)
    with step("[Action] Tap btnDownload at (29.2%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDownload', 29.2, 44.0)
    with step("[Action] Tap btnDelete at (30.8%, 36.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDelete', 30.8, 36.0)
    with step("[Verify] Delete this photo permanently? is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete this photo permanently?')
    with step("[Action] Tap Cancel at (48.3%, 25.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 48.3, 25.0)
    with step("[Action] Tap btnEdit at (15.4%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnEdit', 15.4, 52.0)
    with step("[Action] Tap Portrait at (55.4%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 55.4, 51.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap homeButton at (69.2%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 69.2, 53.8)
    with step("[Action] Tap My Artwork at (37.2%, 70.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Artwork', 37.2, 70.6)
    with step("[Action] Scroll until AI Creative Studio"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuView', AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', direction='left', offset_start=(0.288, 0.516), offset_end=(0.181, 0.516), velocity=80)
    with step("[Action] Tap AI Creative Studio at (37.3%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', 37.3, 48.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=62)
    with step("[Action] Tap Select at (63.3%, 29.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Select', 63.3, 29.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Action] Tap AIArtworkPackSelectionCell-0 at (60.0%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0', 60.0, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-1 at (51.1%, 52.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-1', 51.1, 52.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-2 at (35.6%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-2', 35.6, 61.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-3 at (42.8%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-3', 42.8, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-4 at (42.8%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-4', 42.8, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-5 at (57.8%, 51.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-5', 57.8, 51.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap shareButton at (50.0%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'shareButton', 50.0, 60.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Verify] PopoverDismissRegion is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'PopoverDismissRegion')
    with step("[Action] Tap PopoverDismissRegion at (50.0%, 49.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PopoverDismissRegion', 50.0, 49.7)
    with step("[Action] Tap downloadButton at (52.0%, 32.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'downloadButton', 52.0, 32.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Action] Tap deleteButton at (26.9%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'deleteButton', 26.9, 60.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Verify] Delete 6 photos permanently? is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete 6 photos permanently?')
    with step("[Action] Tap Cancel at (77.8%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 77.8, 50.0)
    with step("[Action] Tap collageButton at (88.0%, 72.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'collageButton', 88.0, 72.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Verify] Collage is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step("[Action] Tap btnBack at (34.0%, 35.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 34.0, 35.8)
    with step("[Action] Tap Select at (95.9%, 61.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Select', 95.9, 61.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Action] Tap AIArtworkPackSelectionCell-0 at (47.8%, 48.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0', 47.8, 48.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-1 at (43.3%, 52.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-1', 43.3, 52.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-2 at (51.7%, 62.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-2', 51.7, 62.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-3 at (47.2%, 59.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-3', 47.2, 59.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-4 at (57.8%, 53.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-4', 57.8, 53.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-5 at (43.9%, 43.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-5', 43.9, 43.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Scroll until AIArtworkPackSelectionCell-6"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'imageCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-6', direction='down', offset_start=(0.513, 0.644), offset_end=(0.513, 0.543), velocity=156)
    with step("[Action] Tap AIArtworkPackSelectionCell-6 at (55.6%, 6.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-6', 55.6, 6.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Verify] collageButton is not visible"):
        actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'collageButton')
    with step("[Action] Tap AIArtworkPackSelectionCell-6 at (48.9%, 9.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-6', 48.9, 9.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-5 at (39.4%, 23.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-5', 39.4, 23.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-4 at (45.6%, 13.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-4', 45.6, 13.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-3 at (50.6%, 24.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-3', 50.6, 24.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-2 at (40.0%, 30.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-2', 40.0, 30.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-1 at (38.9%, 65.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-1', 38.9, 65.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Verify] collageButton is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'collageButton')
    with step("[Action] Tap editButton at (53.8%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'editButton', 53.8, 56.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Action] Tap Portrait at (54.1%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 54.1, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap homeButton at (38.5%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 38.5, 61.5)
    with step("[Action] Tap My Artwork at (21.8%, 23.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Artwork', 21.8, 23.5)
    with step("[Action] Scroll until AI Creative Studio"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuView', AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', direction='left', offset_start=(0.444, 0.258), offset_end=(0.353, 0.258), velocity=112)
    with step("[Action] Tap AI Creative Studio at (40.5%, 46.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', 40.5, 46.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=62)
    with step("[Action] Tap Create More at (35.7%, 88.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Create More', 35.7, 88.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Action] Tap btnNext at (10.6%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 10.6, 57.1)
    with step("[Action] Tap Collage at (61.1%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collage', 61.1, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=28)
    with step("[Action] Tap aiCreativeStudioRouter_backButton at (65.4%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton', 65.4, 44.4)
    with step("[Action] Tap navBackButton at (43.2%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 43.2, 54.5)
    with step("[Action] Tap btnHome at (53.9%, 21.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 53.9, 21.8)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
