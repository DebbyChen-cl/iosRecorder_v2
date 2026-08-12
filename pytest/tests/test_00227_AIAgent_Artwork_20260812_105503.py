import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00227_AIAgent_Artwork_20260812_105503")
def test_00217_AIAgent_Artwork_20260812_105503(actions: DriverActions):
    with step("[Action] Tap AI Photos at (52.8%, 31.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 52.8, 31.8)
    with step("[Action] Tap My Artwork at (42.3%, 58.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Artwork', 42.3, 58.8)
    with step("[Action] Scroll until //XCUIElementTypeOther[@name=\"photodirector.AIStudioAIArtworkShortTaskPackPreviewViewController\"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuView', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AIStudioAIArtworkShortTaskPackPreviewViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]', direction='left', offset_start=(0.33, 0.548), offset_end=(0.237, 0.548), velocity=61)
    with step("[Action] Tap AI Edit Agent at (54.6%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', 54.6, 48.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=62)
    with step("[Action] Tap selectCheckBoxOverlay at (36.1%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'selectCheckBoxOverlay', 36.1, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Verify] AIArtworkPackPreviewCell-0 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackPreviewCell-0')
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackPreviewCell-0')
    with step("[Action] Swipe left on //XCUIElementTypeCell[@name=\"AIArtworkPackPreviewCell-1\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage"):
        actions.swipe_on_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="AIArtworkPackPreviewCell-1"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage', 'left', velocity=466.7, from_pct_x=88.1, from_pct_y=62.8, distance_pts=357.0)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackPreviewCell-1', expected_result='different', threshold=0.95)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackPreviewCell-1')
    with step("[Action] Swipe right on AIArtworkPackPreviewCell-1"):
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackPreviewCell-1', 'right', velocity=459.4, from_pct_x=9.3, from_pct_y=74.8, distance_pts=402.0)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackPreviewCell-0', expected_result='different', threshold=0.95)
    with step("[Action] Tap btnShare at (46.2%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShare', 46.2, 48.0)
    with step("[Verify] PopoverDismissRegion is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'PopoverDismissRegion')
    with step("[Action] Tap AIArtworkPackPreviewCell-0 at (51.6%, 16.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackPreviewCell-0', 51.6, 16.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=430, container_h=695)
    with step("[Action] Tap btnDownload at (29.2%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDownload', 29.2, 44.0)
    with step("[Action] Tap btnDelete at (61.5%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDelete', 61.5, 48.0)
    with step("[Verify] Delete this photo permanently? is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete this photo permanently?')
    with step("[Action] Tap Cancel at (80.0%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 80.0, 83.3)
    with step("[Action] Tap btnEdit at (73.1%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnEdit', 73.1, 52.0)
    with step("[Verify] EditingImageView_ImageView is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap homeButton at (65.4%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 69.2)
    with step("[Action] Tap My Artwork at (83.3%, 35.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Artwork', 83.3, 35.3)
    with step("[Action] Scroll until AI Edit Agent"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuView', AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', direction='left', offset_start=(0.291, 0.597), offset_end=(0.137, 0.597), velocity=151)
    with step("[Action] Tap AI Edit Agent at (66.1%, 53.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', 66.1, 53.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=431, container_h=62)
    with step("[Action] Tap Select at (38.8%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Select', 38.8, 54.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Action] Tap AIArtworkPackSelectionCell-0 at (48.3%, 67.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0', 48.3, 67.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-1 at (52.2%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-1', 52.2, 61.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-2 at (46.1%, 57.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-2', 46.1, 57.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-3 at (30.6%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-3', 30.6, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-4 at (52.8%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-4', 52.8, 51.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-5 at (50.6%, 51.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-5', 50.6, 51.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap shareButton at (73.1%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'shareButton', 73.1, 64.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Verify] PopoverDismissRegion is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'PopoverDismissRegion')
    with step("[Action] Tap cellTitleLabel at (1.2%, 18.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'cellTitleLabel', 1.2, 18.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeCollectionView[@name="activityCollectionView"]/XCUIElementTypeScrollView[1]', container_w=368, container_h=128)
    with step("[Action] Tap downloadButton at (96.0%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'downloadButton', 96.0, 44.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Action] Tap deleteButton at (53.8%, 72.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'deleteButton', 53.8, 72.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Verify] Delete 6 photos permanently? is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete 6 photos permanently?')
    with step("[Action] Tap Cancel at (71.7%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 71.7, 75.0)
    with step("[Action] Tap collageButton at (52.0%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'collageButton', 52.0, 56.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Verify] Capture '00217_AIAgent_Step41' for GT comparison"):
        actions.capture_for_gt('00217_AIAgent_Step41', AppiumBy.ACCESSIBILITY_ID, 'btn6', threshold=0.95)
    with step("[Action] Tap btnBack at (56.6%, 50.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 56.6, 50.9)
    with step("[Action] Tap Select at (67.3%, 45.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Select', 67.3, 45.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Action] Tap AIArtworkPackSelectionCell-0 at (64.4%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0', 64.4, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-1 at (48.9%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-1', 48.9, 58.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-2 at (53.9%, 59.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-2', 53.9, 59.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-3 at (55.0%, 56.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-3', 55.0, 56.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-4 at (51.1%, 47.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-4', 51.1, 47.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-5 at (42.2%, 51.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-5', 42.2, 51.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Scroll until AIArtworkPackSelectionCell-6"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'imageCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-6', direction='down', offset_start=(0.233, 0.452), offset_end=(0.233, 0.371), velocity=94)
    with step("[Action] Tap AIArtworkPackSelectionCell-6 at (54.4%, 4.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-6', 54.4, 4.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Verify] collageButton is not visible"):
        actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'collageButton')
    with step("[Action] Tap AIArtworkPackSelectionCell-6 at (57.8%, 6.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-6', 57.8, 6.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-5 at (48.9%, 30.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-5', 48.9, 30.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-4 at (43.3%, 35.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-4', 43.3, 35.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-3 at (67.2%, 44.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-3', 67.2, 44.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-2 at (38.3%, 49.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-2', 38.3, 49.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap AIArtworkPackSelectionCell-1 at (55.0%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-1', 55.0, 57.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='imageCollectionView', container_w=378, container_h=668)
    with step("[Action] Tap editButton at (73.1%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'editButton', 73.1, 60.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Verify] EditingImageView_ImageView is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap homeButton at (69.2%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 69.2, 65.4)
    with step("[Action] Tap My Artwork at (83.3%, 70.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Artwork', 83.3, 70.6)
    with step("[Action] Scroll until AI Edit Agent"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuView', AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', direction='left', offset_start=(0.279, 0.613), offset_end=(0.174, 0.613), velocity=90)
    with step("[Action] Tap AI Edit Agent at (58.0%, 53.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', 58.0, 53.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=62)
    with step("[Action] Tap Create More at (75.9%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Create More', 75.9, 56.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="AIStudioAIArtworkViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeScrollView', container_w=430, container_h=751)
    with step("[Verify] photodirector.ChatUIViewController is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'photodirector.ChatUIViewController')
    with step("[Action] Tap chatBackButton at (32.3%, 61.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatBackButton', 32.3, 61.3)
    with step("[Action] Tap btnHome at (46.1%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 46.1, 36.4)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
