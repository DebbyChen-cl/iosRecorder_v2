import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00214_AnimatedSticker_Favorites_20260812_163110")
def test_00214_AnimatedSticker_Favorites_20260812_163110(actions: DriverActions):
    with step("[Action] Tap Edit at (80.0%, 68.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 80.0, 68.0)
    with step("[Action] Tap btnAlbum at (82.2%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 82.2, 52.4)
    with step("[Action] Tap _AT at (7.9%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 52.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (46.9%, 82.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 46.9, 82.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (37.8%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 37.8, 48.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Sticker"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Sticker', direction='left', offset_start=(0.693, 0.381), offset_end=(0.244, 0.381), velocity=500)
    with step("[Action] Tap Sticker at (43.1%, 34.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sticker', 43.1, 34.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Action] Tap Animated Sticker at (54.5%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Animated Sticker', 54.5, 58.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap Favorites at (39.2%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Favorites', 39.2, 48.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=426, container_h=33)
    with step("[Verify] You haven\\'t added any favorite elements yet.\\nLong press an element to add it to your favorites! is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'You haven\'t added any favorite elements yet.\nLong press an element to add it to your favorites!')
    with step("[Action] Tap Trending at (61.0%, 88.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Trending', 61.0, 88.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=426, container_h=33)
    with step("[Action] Long press blackBackgroundView at (16.5%, 75.3%)"):
        actions.long_press_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 16.5, 75.3, duration=1.0)
    with step("[Verify] Capture 'test_00214_AnimatedSticker_Favorites_Step13' for GT comparison"):
        actions.capture_for_gt('test_00214_AnimatedSticker_Favorites_Step13', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap Favorites at (46.1%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Favorites', 46.1, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=426, container_h=33)
    with step("[Verify] Capture 'test_00214_AnimatedSticker_Favorites_Step15' for GT comparison"):
        actions.capture_for_gt('test_00214_AnimatedSticker_Favorites_Step15', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap blackBackgroundView at (17.7%, 75.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 17.7, 75.5)
    with step("[Verify] Capture 'test_00214_AnimatedSticker_Favorites_Step17' for GT comparison"):
        actions.capture_for_gt('test_00214_AnimatedSticker_Favorites_Step17', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Long press blackBackgroundView at (17.4%, 74.8%)"):
        actions.long_press_within_element(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 17.4, 74.8, duration=1.0)
    with step("[Verify] You haven\\'t added any favorite elements yet.\\nLong press an element to add it to your favorites! is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'You haven\'t added any favorite elements yet.\nLong press an element to add it to your favorites!')
    with step("[Action] Tap Trending at (63.0%, 59.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Trending', 63.0, 59.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=426, container_h=33)
    with step("[Verify] Capture 'test_00214_AnimatedSticker_Favorites_Step21' for GT comparison"):
        actions.capture_for_gt('test_00214_AnimatedSticker_Favorites_Step21', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (49.0%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 49.0, 49.0)
    with step("[Action] Tap AlertDialog-btnPositive at (18.4%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 18.4, 60.0)
    with step("[Action] Tap homeButton at (73.1%, 38.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 73.1, 38.5)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
