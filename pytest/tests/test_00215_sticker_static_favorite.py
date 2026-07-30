import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


DEFAULT_FAVORITES_DESCRIPTION = (
    "You haven’t added any favorite stickers yet.\n"
    "Long press the sticker to add it to your favorites!"
)
FAVORITE_STICKER = "CMS-phdm_shape[10-fs8]"
HEART_ICON = "ico_ycp_heart_s.png"


@pytest.mark.name("Sticker Static Favorite")
def test_sticker_static_favorite(actions: DriverActions, reset_app):
    # --- Open Static Sticker ---
    with step("[Action] Tap 'Edit'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Launcher_main_edit', 51.9, 52.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=320, container_h=623)
    with step("[Action] Expand album list"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Select '_AT' album"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 50.0, 52.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=294, container_h=557)
    with step("[Action] Select a photo"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=320, container_h=557)
    with step("[Action] Tap 'Sticker'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_sticker_n', 50.0, 52.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=320, container_h=72)
    with step("[Action] Tap 'Static Sticker'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_stickerin', 52.0, 52.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=124, container_h=65)

    # --- Add to Favorites ---
    with step("[Action] Tap 'Favorites' category"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Favorites', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=314, container_h=26)
    with step("[Verify] The default description appears"):
        assert actions.verify_text(
            AppiumBy.ACCESSIBILITY_ID,
            DEFAULT_FAVORITES_DESCRIPTION,
            DEFAULT_FAVORITES_DESCRIPTION,
        ) is not False
    with step("[Action] Tap 'Trending' category"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Trending', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=314, container_h=26)
    with step("[Action] Long tap one sticker"):
        actions.long_press_within_element(AppiumBy.ACCESSIBILITY_ID, FAVORITE_STICKER, 50.0, 50.0, duration=1.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView[2]', container_w=306, container_h=242)
    with step("[Verify] 'Heart' icon appears on the sticker thumbnail"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, HEART_ICON)
    with step("[Action] Tap 'Favorites' category"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Favorites', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=314, container_h=26)
    with step("[Verify] The same sticker is listed"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, FAVORITE_STICKER)
    with step("[Verify] The favorite sticker has 'Heart' icon"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, HEART_ICON)
    with step("[Action] Tap the favorite sticker"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, FAVORITE_STICKER, 50.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView[2]', container_w=306, container_h=242)
    with step("[Verify] The sticker is added to preview"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')

    # --- Remove from Favorites through Add Object ---
    with step("[Action] Tap '+' button; add object menu appears"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n', 51.4, 50.0)
    with step("[Action] Tap 'Add Sticker'"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AddImageMainPanelCell-3')
    with step("[Action] Tap 'Favorites' category"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Favorites', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=314, container_h=26)
    with step("[Action] Long tap the favorite sticker"):
        actions.long_press_within_element(AppiumBy.ACCESSIBILITY_ID, FAVORITE_STICKER, 50.0, 50.0, duration=1.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView[2]', container_w=306, container_h=242)
    with step("[Verify] The sticker is removed from Favorites category"):
        assert actions.verify_text(
            AppiumBy.ACCESSIBILITY_ID,
            DEFAULT_FAVORITES_DESCRIPTION,
            DEFAULT_FAVORITES_DESCRIPTION,
        ) is not False
    with step("[Verify] Default description is displayed"):
        assert actions.verify_text(
            AppiumBy.ACCESSIBILITY_ID,
            DEFAULT_FAVORITES_DESCRIPTION,
            DEFAULT_FAVORITES_DESCRIPTION,
        ) is not False
    with step("[Action] Tap 'Trending' category"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Trending', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=314, container_h=26)
    with step("[Verify] No 'Heart' icon is displayed on the sticker"):
        screen_width, screen_height = actions.get_screen_size()
        visible_hearts = []
        for heart in actions.find_elements(AppiumBy.ACCESSIBILITY_ID, HEART_ICON, timeout=1):
            rect = heart.rect
            if (
                rect["x"] < screen_width
                and rect["x"] + rect["width"] > 0
                and rect["y"] < screen_height
                and rect["y"] + rect["height"] > 0
            ):
                visible_hearts.append(rect)
        assert not visible_hearts, f"Heart icon is still visible: {visible_hearts}"
