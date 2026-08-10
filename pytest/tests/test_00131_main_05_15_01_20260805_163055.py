import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00131_main_05_15_01_20260805_163055")
def test_00131_main_05_15_01_20260805_163055(actions: DriverActions):
    with step("[Action] Tap Edit at (74.3%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 74.3, 64.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (76.6%, 85.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 76.6, 85.7)
    with step("[Action] Tap _AT at (9.0%, 90.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.0, 90.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (23.1%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 23.1, 59.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (46.5%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 46.5, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_live_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', direction='left', offset_start=(0.888, 0.526), offset_end=(0.13, 0.526), velocity=601)
    with step("[Action] Tap btn_live_n at (45.5%, 90.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', 45.5, 90.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_sky_n at (61.0%, 90.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_sky_n', 61.0, 90.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap Cloudy 1 at (54.9%, 47.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cloudy 1', 54.9, 47.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='skyExpandCollectionViewCollectionView', container_w=374, container_h=101)
    with step("[Verify] Capture '00131_main_05_15_01_Step10' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step10', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap 01 at (63.4%, 73.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '01', 63.4, 73.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='skyExpandCollectionViewCollectionView', container_w=374, container_h=101)
    with step("[Verify] Capture '00131_main_05_15_01_Step12' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step12', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap btnMaskSwitch at (45.0%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch', 45.0, 30.0)
    with step("[Action] Scroll until btnMaskSwitch"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch', direction='right', offset_start=(0.133, 0.097), offset_end=(0.886, 0.097), velocity=216)
    with step("[Verify] Capture '00131_main_05_15_01_Step16' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step16', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (63.3%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 63.3, 32.7)
    with step("[Verify] Capture '00131_main_05_15_01_Step17' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step17', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_redo at (75.5%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 75.5, 53.1)
    with step("[Verify] Capture '00131_main_05_15_01_Step19' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step19', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnErase at (50.0%, 62.5%)"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnErase', 50.0, 62.5)
    with step("[Action] Drag blackBackgroundView (9.5%,23.4%) → blackBackgroundView (90.2%,23.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 9.5, 23.4, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 90.2, 23.3, duration=1.0)
    with step("[Verify] Capture '00131_main_05_15_01_Step23' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step23', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnMaskSwitch at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch', 50.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=667)
    with step("[Verify] Capture '00131_main_05_15_01_Step25' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step25', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap imgViewSelected at (61.8%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imgViewSelected', 61.8, 70.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='skyExpandCollectionViewCollectionView', container_w=374, container_h=101)
    with step("[Action] Tap btn_feather_n at (82.9%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_feather_n', 82.9, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Verify] Capture '00131_main_05_15_01_Step28' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step28', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Drag slider (49.8%,56.0%) → blackBackgroundView (72.8%,74.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 49.8, 56.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 72.8, 74.9, duration=1.0)
    with step("[Verify] Capture '00131_main_05_15_01_Step30' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step30', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Drag slider (93.4%,60.0%) → blackBackgroundView (14.4%,75.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 93.4, 60.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 14.4, 75.0, duration=1.0)
    with step("[Verify] Capture '00131_main_05_15_01_Step32' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step32', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap btn_horizon_n at (58.5%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_horizon_n', 58.5, 75.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Verify] lblVal text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '0')
    with step("[Action] Drag slider (7.0%,46.0%) → blackBackgroundView (73.0%,74.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 7.0, 46.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 73.0, 74.8, duration=1.0)
    with step("[Verify] Capture '00131_main_05_15_01_Step36' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step36', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap btn_ambient_n at (63.4%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ambient_n', 63.4, 52.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Verify] lblVal text equals '35'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '35')
    with step("[Action] Drag slider (41.0%,46.0%) → blackBackgroundView (12.8%,75.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 41.0, 46.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 12.8, 75.4, duration=1.0)
    with step("[Verify] lblVal text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '0')
    with step("[Verify] Capture '00131_main_05_15_01_Step41' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step41', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Drag slider (5.5%,52.0%) → blackBackgroundView (73.3%,75.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 5.5, 52.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 73.3, 75.0, duration=1.0)
    with step("[Verify] lblVal text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '100')
    with step("[Verify] Capture '00131_main_05_15_01_Step44' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step44', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap btn_hdr_glow_n at (68.3%, 35.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_hdr_glow_n', 68.3, 35.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Verify] lblVal text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '0')
    with step("[Action] Drag slider (7.0%,56.0%) → blackBackgroundView (73.3%,75.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 7.0, 56.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 73.3, 75.2, duration=1.0)
    with step("[Verify] lblVal text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '100')
    with step("[Verify] Capture '00131_main_05_15_01_Step49' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step49', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap btn_hdr_edge_n at (43.9%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_hdr_edge_n', 43.9, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Verify] lblVal text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '0')
    with step("[Action] Drag slider (25.8%,58.0%) → blackBackgroundView (16.3%,76.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 25.8, 58.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 16.3, 76.3, duration=1.0)
    with step("[Verify] lblVal text equals '-20'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '-20')
    with step("[Verify] Capture '00131_main_05_15_01_Step54' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step54', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Drag slider (7.4%,52.0%) → blackBackgroundView (72.1%,75.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 7.4, 52.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 72.1, 75.2, duration=1.0)
    with step("[Verify] lblVal text equals '80'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '80')
    with step("[Verify] Capture '00131_main_05_15_01_Step57' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step57', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Drag touchView (84.0%,83.1%) → blackBackgroundView (11.6%,66.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'touchView', 84.0, 83.1, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 11.6, 66.4, duration=1.0)
    with step("[Verify] Capture '00131_main_05_15_01_Step59' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step59', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Scroll until btn_sky_fade_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'btn_sky_fade_n', direction='left', offset_start=(0.723, 0.33), offset_end=(0.474, 0.33), velocity=138)
    with step("[Action] Tap btn_sky_fade_n at (58.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_sky_fade_n', 58.5, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Verify] lblVal text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '0')
    with step("[Action] Drag slider (7.0%,56.0%) → blackBackgroundView (72.6%,75.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 7.0, 56.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 72.6, 75.1, duration=1.0)
    with step("[Verify] lblVal text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '100')
    with step("[Verify] Capture '00131_main_05_15_01_Step65' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step65', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap btnBack at (59.1%, 57.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 59.1, 57.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Verify] Capture '00131_main_05_15_01_Step67' for GT comparison"):
        actions.capture_for_gt('00131_main_05_15_01_Step67', AppiumBy.ACCESSIBILITY_ID, 'touchView', threshold=0.95)
    with step("[Action] Tap btnBack at (56.8%, 61.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 56.8, 61.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap btn_sky_n at (51.2%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_sky_n', 51.2, 75.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap icon_Pack_close at (91.2%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_Pack_close', 91.2, 70.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='skyExpandCollectionViewCollectionView', container_w=374, container_h=101)
    with step("[Action] Tap Cloudy 2 at (57.3%, 31.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cloudy 2', 57.3, 31.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='skyExpandCollectionViewCollectionView', container_w=374, container_h=101)
    with step("[Action] Tap 01 at (78.0%, 26.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '01', 78.0, 26.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='skyExpandCollectionViewCollectionView', container_w=374, container_h=101)
    with step("[Verify] UNLOCK TO is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'UNLOCK TO')
    with step("[Action] Tap btn_ok_n at (89.8%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 89.8, 34.7)
    with step("[Action] Tap btnClose at (51.6%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 51.6, 48.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (32.7%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 32.7, 44.9)
    with step("[Action] Tap Discard at (50.7%, 37.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 50.7, 37.5)
    with step("[Action] Tap homeButton at (53.8%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 53.8, 42.3)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
