import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00156_main_11_01_05_20260806_175017")
def test_00156_main_11_01_05_20260806_175017(actions: DriverActions):
    with step("[Action] Tap btnSettings at (69.7%, 41.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 69.7, 41.2)
    with step("[Action] Tap About at (80.4%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 80.4, 56.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (40.8%, 46.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 40.8, 46.0)
    with step("[Action] Tap Free at (73.5%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 73.5, 47.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (51.4%, 61.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 51.4, 61.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (70.0%, 52.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 70.0, 52.8)
    with step("[Action] Tap btnBack at (60.7%, 55.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 60.7, 55.3)
    with step("[Action] Tap btnBack at (64.3%, 57.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 64.3, 57.4)
    with step("[Action] Tap Edit at (62.9%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 62.9, 48.0)
    with step("[Action] Tap btnAlbum at (77.7%, 78.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 77.7, 78.6)
    with step("[Action] Tap _AT at (8.2%, 90.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.2, 90.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (40.0%, 74.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 40.0, 74.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap btn_text_n at (48.5%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_text_n', 48.5, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_text_sub_menu_n at (54.5%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_text_sub_menu_n', 54.5, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap btn_ok_n at (95.9%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 95.9, 46.9)
    with step("[Action] Tap OK at (100.0%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 100.0, 70.8)
    with step("[Verify] Capture '00156_main_11_01_05_Step17' for GT comparison"):
        actions.capture_for_gt('00156_main_11_01_05_Step17', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (69.2%, 48.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 69.2, 48.7)
    with step("[Action] Tap btn_text_n at (60.6%, 93.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_text_n', 60.6, 93.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap icon_textBB at (54.5%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_textBB', 54.5, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap btn_ok_n at (77.6%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 46.9)
    with step("[Action] Tap OK at (66.7%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 66.7, 62.5)
    with step("[Verify] Capture '00156_main_11_01_05_Step23' for GT comparison"):
        actions.capture_for_gt('00156_main_11_01_05_Step23', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (64.1%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 64.1, 46.2)
    with step("[Action] Scroll until btn_sticker_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_sticker_n', direction='left', offset_start=(0.609, 0.505), offset_end=(0.116, 0.505), velocity=528)
    with step("[Action] Tap btn_sticker_n at (44.1%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_sticker_n', 44.1, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_stickerin at (30.3%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_stickerin', 30.3, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Double tap CMS-phdm_sticker_text_220220519Thumbnail[11-fs8] at (67.5%, 59.0%)"):
        actions.double_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_sticker_text_220220519Thumbnail[11-fs8]', 67.5, 59.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView[2]', container_w=412, container_h=287)
    with step("[Action] Tap btn_ok_n at (81.6%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 32.7)
    with step("[Action] Tap OK at (23.3%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 23.3, 70.8)
    with step("[Verify] Capture '00156_main_11_01_05_Step31' for GT comparison"):
        actions.capture_for_gt('00156_main_11_01_05_Step31', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (64.1%, 59.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 64.1, 59.0)
    with step("[Action] Tap Effects at (35.2%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 35.2, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_live_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', direction='left', offset_start=(0.642, 0.412), offset_end=(0.105, 0.412), velocity=620)
    with step("[Action] Tap btn_live_n at (51.5%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', 51.5, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_ellements_n at (61.0%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n', 61.0, 55.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap blackBackgroundView at (17.2%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 17.2, 75.8)
    with step("[Action] Tap btn_ok_n at (73.5%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 32.7)
    with step("[Action] Tap Still Image at (68.1%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Still Image', 68.1, 62.5)
    with step("[Verify] Capture '00156_main_11_01_05_Step40' for GT comparison"):
        actions.capture_for_gt('00156_main_11_01_05_Step40', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (66.7%, 82.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 66.7, 82.1)
    with step("[Action] Tap btn_live_n at (69.7%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', 69.7, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_live_overlay_n at (53.7%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_overlay_n', 53.7, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap blackBackgroundView at (38.6%, 85.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 38.6, 85.6)
    with step("[Action] Tap btn_ok_n at (79.6%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 79.6, 36.7)
    with step("[Action] Tap AlertDialog-btnPositive at (53.2%, 78.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 53.2, 78.0)
    with step("[Verify] Capture '00156_main_11_01_05_Step47' for GT comparison"):
        actions.capture_for_gt('00156_main_11_01_05_Step47', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.92)
    with step("[Action] Tap ic edit undo n at (71.8%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 71.8, 66.7)
    with step("[Action] Tap btn_live_n at (72.7%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', 72.7, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_sky_n at (65.9%, 42.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_sky_n', 65.9, 42.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap Cloudy 2 at (59.8%, 84.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cloudy 2', 59.8, 84.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='skyExpandCollectionViewCollectionView', container_w=374, container_h=101)
    with step("[Action] Tap 01 at (63.4%, 84.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '01', 63.4, 84.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='skyExpandCollectionViewCollectionView', container_w=374, container_h=101)
    with step("[Action] Tap btn_ok_n at (75.5%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 44.9)
    with step("[Verify] Capture '00156_main_11_01_05_Step54' for GT comparison"):
        actions.capture_for_gt('00156_main_11_01_05_Step54', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (48.7%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 48.7, 61.5)
    with step("[Action] Tap btn_live_n at (27.3%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', 27.3, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Scroll until btn_live_sparkle_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'btn_live_sparkle_n', direction='left', offset_start=(0.642, 0.423), offset_end=(0.181, 0.423), velocity=436)
    with step("[Action] Tap btn_live_sparkle_n at (46.3%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_sparkle_n', 46.3, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap blackBackgroundView at (44.0%, 87.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 44.0, 87.0)
    with step("[Action] Tap btn_ok_n at (89.8%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 89.8, 38.8)
    with step("[Action] Tap AlertDialog-btnPositive at (55.4%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 55.4, 80.0)
    with step("[Verify] Capture '00156_main_11_01_05_Step62' for GT comparison"):
        actions.capture_for_gt('00156_main_11_01_05_Step62', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (38.5%, 56.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 38.5, 56.4)
    with step("[Action] Tap Edit at (67.4%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 67.4, 44.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_frame_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_frame_n', direction='left', offset_start=(0.698, 0.423), offset_end=(0.195, 0.423), velocity=664)
    with step("[Action] Tap btn_frame_n at (45.5%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_frame_n', 45.5, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Home Decor at (61.0%, 35.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Home Decor', 61.0, 35.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='frameBottomGroupBarCollectionView', container_w=366, container_h=97)
    with step("[Action] Tap 01 at (40.7%, 21.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '01', 40.7, 21.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='frameBottomGroupBarCollectionView', container_w=366, container_h=97)
    with step("[Action] Tap btn_ok_n at (75.5%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 46.9)
    with step("[Verify] Capture '00156_main_11_01_05_Step70' for GT comparison"):
        actions.capture_for_gt('00156_main_11_01_05_Step70', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (65.4%, 80.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 80.8)
    with step("[Action] Tap Discard at (69.6%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 69.6, 83.3)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
