import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00164_ai_hair_volume_20260807_103910")
def test_00164_ai_hair_volume_20260807_103910(actions: DriverActions):
    with step("[Action] Tap Edit at (42.9%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 42.9, 52.0)
    with step("[Action] Tap btnAlbum at (90.4%, 59.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 90.4, 59.5)
    with step("[Action] Tap _AT at (6.8%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 6.8, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (29.2%, 63.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 29.2, 63.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (60.8%, 64.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 60.8, 64.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until ic_hair"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_hair', direction='left', offset_start=(0.595, 0.515), offset_end=(0.291, 0.515), velocity=169)
    with step("[Action] Tap ic_hair at (51.5%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_hair', 51.5, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_hair_volume at (69.7%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_hair_volume', 69.7, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Verify] The face in this photo is too small or blurry, which may result in poorly generated results. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'The face in this photo is too small or blurry, which may result in poorly generated results.')
    with step("[Action] Tap OK at (46.7%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 46.7, 41.7)
    with step("[Action] Tap ic_hair at (57.6%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_hair', 57.6, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_hair_volume at (60.6%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_hair_volume', 60.6, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap Continue Anyway at (53.2%, 37.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway', 53.2, 37.5)
    with step("[Verify] Capture '00164_ai_hair_volume_Step14' for GT comparison"):
        actions.capture_for_gt('00164_ai_hair_volume_Step14', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView', threshold=0.95)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView')
    with step("[Action] Tap Subtle at (68.2%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Subtle', 68.2, 55.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=117)
    with step("[Action] Tap generateButton at (14.0%, 83.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'generateButton', 14.0, 83.9)
    with step("[Verify] barImageView disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'barImageView', appear_timeout=5, disappear_timeout=1200), 'barImageView did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView', expected_result='different', threshold=0.999)
    with step("[Action] Tap Natural at (30.7%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Natural', 30.7, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=117)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView')
    with step("[Action] Tap generateButton at (63.5%, 46.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'generateButton', 63.5, 46.8)
    with step("[Verify] barImageView disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'barImageView', appear_timeout=5, disappear_timeout=1200), 'barImageView did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'editAreaView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView')
    with step("[Action] Tap ic_undo at (62.0%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 62.0, 34.7)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView')
    with step("[Action] Tap ic_redo at (62.0%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 62.0, 30.6)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView', expected_result='different', threshold=0.999)
    with step("[Action] Tap Western_v3 at (31.8%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Western_v3', 31.8, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=117)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView')
    with step("[Action] Tap generateButton at (19.0%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'generateButton', 19.0, 64.5)
    with step("[Verify] barImageView disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'barImageView', appear_timeout=5, disappear_timeout=1200), 'barImageView did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="editAnchorView"]/XCUIElementTypeOther/XCUIElementTypeImage', expected_result='different', threshold=0.999)
    with step("[Action] Tap Western_v4 at (52.3%, 58.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Western_v4', 52.3, 58.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=117)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView')
    with step("[Action] Tap generateButton at (23.9%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'generateButton', 23.9, 51.6)
    with step("[Verify] barImageView disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'barImageView', appear_timeout=5, disappear_timeout=1200), 'barImageView did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView', expected_result='different', threshold=0.999)
    with step("[Action] Tap Maximized at (45.5%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Maximized', 45.5, 40.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=117)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView')
    with step("[Action] Tap generateButton at (19.8%, 80.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'generateButton', 19.8, 80.6)
    with step("[Verify] barImageView disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'barImageView', appear_timeout=5, disappear_timeout=1200), 'barImageView did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="editAnchorView"]/XCUIElementTypeOther/XCUIElementTypeImage', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView')
    with step("[Action] Tap btn_reset_n at (72.0%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n', 72.0, 40.8)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView')
    with step("[Action] Tap ic_undo at (64.0%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 64.0, 51.0)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView', expected_result='different', threshold=0.999)
    with step("[Action] Tap btn_cancel_n at (46.9%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 46.9, 59.2)
    with step("[Action] Tap ic_hair at (66.7%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_hair', 66.7, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_hair_volume at (66.7%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_hair_volume', 66.7, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap Continue Anyway at (56.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway', 56.5, 50.0)
    with step("[Action] Tap High at (54.5%, 35.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'High', 54.5, 35.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=117)
    with step("[Action] Tap generateButton at (12.4%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'generateButton', 12.4, 67.7)
    with step("[Verify] barImageView disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'barImageView', appear_timeout=5, disappear_timeout=1200), 'barImageView did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btn_ok_n at (77.6%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 36.7)
    with step("[Action] Tap homeButton at (61.5%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 76.9)
    with step("[Action] Tap Discard at (69.6%, 54.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 69.6, 54.2)
    with step("[Action] Tap btnStudio at (52.6%, 47.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnStudio', 52.6, 47.3)
    with step("[Action] Scroll until Hair Volume"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Hair Volume', direction='down', offset_start=(0.245, 0.496), offset_end=(0.245, 0.323), velocity=83)
    with step("[Action] Tap Hair Volume at (66.3%, 72.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Hair Volume', 66.3, 72.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (27.5%, 61.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 27.5, 61.2)
    with step("[Action] Tap photoCell-4 at (39.2%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4', 39.2, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"MenuCell-0\"]/XCUIElementTypeImage[1] at (54.3%, 55.6%)"):
            actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="MenuCell-0"]/XCUIElementTypeImage[1]', 54.3, 55.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="topPanelAreaView"]/XCUIElementTypeCollectionView', container_w=237, container_h=49)
    with step("[Action] Tap High at (33.0%, 25.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'High', 33.0, 25.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=117)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView')
    with step("[Action] Tap generateButton at (27.9%, 83.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'generateButton', 27.9, 83.9)
    with step("[Verify] barImageView disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'barImageView', appear_timeout=5, disappear_timeout=1200), 'barImageView did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'editAreaView', expected_result='different', threshold=0.999)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"MenuCell-1\"]/XCUIElementTypeImage at (50.0%, 58.3%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="MenuCell-1"]/XCUIElementTypeImage', 50.0, 58.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="topPanelAreaView"]/XCUIElementTypeCollectionView', container_w=240, container_h=49)
    with step("[Action] Tap Continue Anyway at (28.6%, 79.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway', 28.6, 79.2)
    with step("[Action] Tap AlertDialog-btnPositive at (8.2%, 72.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 8.2, 72.0)
    with step("[Action] Tap Western_v4 at (54.5%, 80.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Western_v4', 54.5, 80.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=117)
    with step("[Action] Tap generateButton at (12.7%, 85.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'generateButton', 12.7, 85.5)
    with step("[Verify] barImageView disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'barImageView', appear_timeout=5, disappear_timeout=1200), 'barImageView did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'editAreaView')
    with step("[Action] Tap ic_undo at (68.0%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 68.0, 59.2)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'faceOverlayBorderView', expected_result='different', threshold=0.999)
    with step("[Action] Tap ic_redo at (54.0%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 54.0, 42.9)
    with step("[Action] Tap btn_ok_n at (73.5%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 44.9)
    with step("[Action] Tap homeButton at (61.5%, 80.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 80.8)
    with step("[Action] Tap Discard at (84.8%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 84.8, 30.0)
    with step("[Action] Tap btnHome at (55.3%, 47.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 55.3, 47.3)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.999)
    assert True
