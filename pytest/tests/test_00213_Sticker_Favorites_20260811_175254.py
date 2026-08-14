import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00213_Sticker_Favorites_20260811_175254")
def test_00213_Sticker_Favorites_20260811_175254(actions: DriverActions):
    with step("[Action] Tap Edit at (57.1%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 57.1, 60.0)
    with step("[Action] Tap btnAlbum at (93.9%, 50.0%)"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Verify] _AT is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap _AT at (10.0%, 39.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.0, 39.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (50.8%, 56.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 50.8, 56.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (46.7%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 46.7, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Sticker"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Sticker', direction='left', offset_start=(0.795, 0.412), offset_end=(0.047, 0.412), velocity=587)
    with step("[Action] Tap Sticker at (46.5%, 28.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sticker', 46.5, 28.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Static Sticker at (29.9%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Static Sticker', 29.9, 58.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Scroll until Favorites"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'categoryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Favorites', direction='right', offset_start=(0.088, 0.647), offset_end=(0.735, 0.647), velocity=499)
    with step("[Action] Tap Favorites at (56.9%, 53.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Favorites', 56.9, 53.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=422, container_h=34)
    with step("[Verify] Capture '00213_Sticker_Favorites_Step11' for GT comparison"):
        actions.capture_for_gt('00213_Sticker_Favorites_Step11', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]', threshold=0.95)
    with step("[Action] Tap Trending at (72.0%, 67.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Trending', 72.0, 67.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=422, container_h=34)
    with step("[Action] Long press CMS-phdm_sticker_text_220220519Thumbnail[11-fs8] at (42.9%, 52.6%)"):
        actions.long_press_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_sticker_text_220220519Thumbnail[11-fs8]', 42.9, 52.6, duration=1.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView[2]', container_w=412, container_h=287)
    with step("[Action] Tap Favorites at (74.5%, 53.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Favorites', 74.5, 53.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=422, container_h=34)
    with step("[Verify] Capture '00213_Sticker_Favorites_Step15' for GT comparison"):
        actions.capture_for_gt('00213_Sticker_Favorites_Step15', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]', threshold=0.95)
    with step("[Action] Tap CMS-phdm_sticker_text_220220519Thumbnail[11-fs8] at (49.4%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_sticker_text_220220519Thumbnail[11-fs8]', 49.4, 42.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView[2]', container_w=412, container_h=287)
    with step("[Verify] Capture '00213_Sticker_Favorites_Step17' for GT comparison"):
        actions.capture_for_gt('00213_Sticker_Favorites_Step17', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap btn_add_n at (72.0%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n', 72.0, 46.9)
    with step("[Action] Tap lblText at (81.4%, 43.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lblText', 81.4, 43.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Scroll until Favorites"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'categoryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Favorites', direction='right', offset_start=(0.277, 0.559), offset_end=(0.671, 0.559), velocity=430)
    with step("[Action] Tap Favorites at (49.0%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Favorites', 49.0, 57.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=422, container_h=34)
    with step("[Action] Long press CMS-phdm_sticker_text_220220519Thumbnail[11-fs8] at (54.5%, 51.3%)"):
        actions.long_press_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_sticker_text_220220519Thumbnail[11-fs8]', 54.5, 51.3, duration=1.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView[2]', container_w=412, container_h=287)
    with step("[Verify] Capture '00213_Sticker_Favorites_Step23' for GT comparison"):
        actions.capture_for_gt('00213_Sticker_Favorites_Step23', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]', threshold=0.95)
    with step("[Action] Tap Trending at (70.0%, 64.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Trending', 70.0, 64.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=422, container_h=34)
    with step("[Verify] Capture '00213_Sticker_Favorites_Step25' for GT comparison"):
        actions.capture_for_gt('00213_Sticker_Favorites_Step25', AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_sticker_text_220220519Thumbnail[11-fs8]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (87.8%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 87.8, 26.5)
    with step("[Action] Tap OK at (60.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 60.0, 50.0)
    with step("[Action] Tap homeButton at (69.2%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 69.2, 65.4)
    with step("[Action] Tap Discard at (84.1%, 79.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 84.1, 79.2)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
