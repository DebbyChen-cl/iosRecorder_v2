import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00051_lightray_20260804_115641")
def test_00051_lightray_20260804_115641(actions: DriverActions):
    with step("[Action] Tap Edit at (60.0%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 60.0, 44.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (83.8%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 83.8, 42.9)
    with step("[Action] Tap _AT at (7.2%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.2, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (43.1%, 56.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 43.1, 56.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (49.3%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 49.3, 46.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_live_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', direction='left', offset_start=(0.793, 0.371), offset_end=(0.24, 0.371), velocity=212)
    with step("[Action] Tap btn_live_n at (63.6%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', 63.6, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Scroll until btn_live_lightray_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'btn_live_lightray_n', direction='left', offset_start=(0.619, 0.412), offset_end=(0.314, 0.412), velocity=215)
    with step("[Action] Tap btn_live_lightray_n at (65.9%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_lightray_n', 65.9, 47.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=431, container_h=97)
    with step("[Action] Tap Single source at (45.1%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Single source', 45.1, 42.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='itemView', container_w=257, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step11' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step11', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag redDot (31.2%,47.1%) → blackBackgroundView (20.2%,36.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'redDot', 31.2, 47.1, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 20.2, 36.8, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step13' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step13', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap toolView at (52.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'toolView', 52.2, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='itemView', container_w=257, container_h=97)
    with step("[Action] Tap lightray_btn_intensity_n at (65.9%, 37.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lightray_btn_intensity_n', 65.9, 37.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step16' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step16', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (46.7%,54.8%) → blackBackgroundView (5.1%,76.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 46.7, 54.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 5.1, 76.7, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step18' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step18', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (8.6%,50.0%) → blackBackgroundView (71.4%,76.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 8.6, 50.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 71.4, 76.6, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step20' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step20', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (51.0%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 51.0, 32.7)
    with step("[Action] Tap ic_undo at (67.3%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 67.3, 42.9)
    with step("[Verify] Capture '00051_lightray_Step23' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step23', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap lightray_btn_length_n at (61.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lightray_btn_length_n', 61.0, 52.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step25' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step25', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (56.3%,54.8%) → blackBackgroundView (5.3%,77.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 56.3, 54.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 5.3, 77.0, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step27' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step27', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (6.6%,69.0%) → blackBackgroundView (73.7%,76.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.6, 69.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 73.7, 76.9, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step29' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step29', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (40.8%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 40.8, 42.9)
    with step("[Action] Tap ic_undo at (61.2%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 61.2, 55.1)
    with step("[Verify] Capture '00051_lightray_Step32' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step32', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap lightray_btn_color_n at (56.1%, 72.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lightray_btn_color_n', 56.1, 72.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step34' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step34', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag hueSlider (50.7%,59.6%) → blackBackgroundView (21.6%,73.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 50.7, 59.6, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 21.6, 73.5, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step36' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step36', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag hueSlider (8.5%,48.9%) → blackBackgroundView (79.1%,72.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 8.5, 48.9, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 79.1, 72.9, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step38' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step38', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag saturationSlider (50.7%,42.6%) → blackBackgroundView (21.2%,78.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 50.7, 42.6, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 21.2, 78.4, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step40' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step40', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag saturationSlider (7.4%,59.6%) → blackBackgroundView (83.0%,78.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 7.4, 59.6, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 83.0, 78.3, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step42' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step42', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (53.1%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 53.1, 32.7)
    with step("[Action] Tap ic_undo at (53.1%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 53.1, 32.7)
    with step("[Action] Tap ic_undo at (55.1%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 55.1, 38.8)
    with step("[Action] Tap ic_undo at (55.1%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 55.1, 38.8)
    with step("[Verify] Capture '00051_lightray_Step47' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step47', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Scroll until btn_softness_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'btn_softness_n', direction='left', offset_start=(0.538, 0.485), offset_end=(0.342, 0.485), velocity=75)
    with step("[Action] Tap btn_softness_n at (61.0%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_softness_n', 61.0, 47.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step50' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step50', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (8.3%,54.8%) → blackBackgroundView (72.3%,76.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 8.3, 54.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 72.3, 76.8, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step52' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step52', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (67.3%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 67.3, 42.9)
    with step("[Verify] Capture '00051_lightray_Step54' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step54', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Scroll until lightray_btn_expansion_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'lightray_btn_expansion_n', direction='left', offset_start=(0.533, 0.33), offset_end=(0.13, 0.33), velocity=180)
    with step("[Action] Tap lightray_btn_expansion_n at (70.7%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lightray_btn_expansion_n', 70.7, 45.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step57' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step57', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (92.7%,47.6%) → blackBackgroundView (0.9%,77.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 92.7, 47.6, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 0.9, 77.0, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step59' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step59', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (69.4%, 24.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 69.4, 24.5)
    with step("[Verify] Capture '00051_lightray_Step61' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step61', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Scroll menuView left to reveal Range"):
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'menuView', 'left', velocity=180, from_pct_x=53.3, from_pct_y=33.0, distance_pts=148.3)
    with step("[Action] Tap Range"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Range')
    with step("[Verify] Capture '00051_lightray_Step63' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step63', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (76.2%,61.9%) → blackBackgroundView (71.2%,76.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 76.2, 61.9, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 71.2, 76.8, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step65' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step65', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (93.7%,54.8%) → blackBackgroundView (5.6%,77.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 93.7, 54.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 5.6, 77.5, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step67' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step67', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (61.2%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 61.2, 44.9)
    with step("[Action] Tap ic_undo at (61.2%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 61.2, 44.9)
    with step("[Verify] Capture '00051_lightray_Step70' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step70', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    # with step("[Action] Scroll until ic_undo"):
    #     actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'ic_undo', direction='left', offset_start=(0.622, 0.433), offset_end=(0.0, 0.433), velocity=409)
    with step("[Action] Tap lightray_btn_direction_n at (24.4%, 77.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lightray_btn_direction_n', 24.4, 77.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step73' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step73', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (22.0%,64.3%) → blackBackgroundView (74.9%,76.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 22.0, 64.3, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 74.9, 76.7, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step75' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step75', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (92.3%,52.4%) → blackBackgroundView (16.3%,76.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 92.3, 52.4, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 16.3, 76.9, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step77' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step77', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (77.6%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 77.6, 42.9)
    with step("[Action] Tap ic_undo at (79.6%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 79.6, 49.0)
    with step("[Verify] Capture '00051_lightray_Step80' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step80', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btn_LightRayMode_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_LightRayMode_n')
    with step("[Verify] Capture '00051_lightray_Step82' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step82', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btn_hue_n at (48.8%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_hue_n', 48.8, 55.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step84' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step84', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (41.1%,57.1%) → blackBackgroundView (4.7%,77.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 41.1, 57.1, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 4.7, 77.1, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step86' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step86', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (7.0%,59.5%) → blackBackgroundView (71.6%,76.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.0, 59.5, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 71.6, 76.7, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step88' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step88', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btn_swaying_n at (68.3%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_swaying_n', 68.3, 80.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step90' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step90', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btnBack at (50.9%, 49.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 50.9, 49.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap btnBack at (58.2%, 54.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 58.2, 54.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap btn_directional at (55.2%, 49.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_directional', 55.2, 49.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='itemView', container_w=257, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step94' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step94', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (42.4%,64.3%) → blackBackgroundView (4.4%,77.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 42.4, 64.3, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 4.4, 77.4, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step96' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step96', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (7.9%,61.9%) → blackBackgroundView (69.8%,76.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.9, 61.9, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 69.8, 76.4, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step98' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step98', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap toolView at (52.2%, 29.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'toolView', 52.2, 29.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='itemView', container_w=257, container_h=97)
    with step("[Action] Scroll menuView right to reveal Intensity"):
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'menuView', 'right', velocity=180, from_pct_x=46.7, from_pct_y=33.0, distance_pts=148.3)
    with step("[Action] Tap Intensity"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Intensity')
    with step("[Verify] Capture '00051_lightray_Step101' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step101', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (47.0%,47.6%) → blackBackgroundView (4.2%,76.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 47.0, 47.6, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 4.2, 76.4, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step103' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step103', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (7.0%,50.0%) → blackBackgroundView (74.2%,76.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 74.2, 76.4, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step105' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step105', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (77.6%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 77.6, 42.9)
    with step("[Action] Tap ic_undo at (73.5%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 73.5, 55.1)
    with step("[Verify] Capture '00051_lightray_Step108' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step108', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap lightray_btn_length_n at (53.7%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lightray_btn_length_n', 53.7, 55.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step110' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step110', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (55.6%,54.8%) → blackBackgroundView (4.0%,76.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 55.6, 54.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 4.0, 76.9, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step112' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step112', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (7.3%,61.9%) → blackBackgroundView (69.1%,76.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.3, 61.9, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 69.1, 76.5, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step114' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step114', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.93)
    with step("[Action] Tap ic_undo at (69.4%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 69.4, 55.1)
    with step("[Action] Tap ic_undo at (69.4%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 69.4, 55.1)
    with step("[Verify] Capture '00051_lightray_Step117' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step117', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap lightray_btn_direction_n at (75.6%, 77.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lightray_btn_direction_n', 75.6, 77.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step119' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step119', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (19.3%,50.0%) → blackBackgroundView (14.9%,77.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 19.3, 50.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 14.9, 77.1, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step121' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step121', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (7.3%,54.8%) → blackBackgroundView (73.3%,76.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.3, 54.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 73.3, 76.6, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step123' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step123', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (75.5%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 75.5, 53.1)
    with step("[Action] Tap ic_undo at (75.5%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 75.5, 53.1)
    with step("[Verify] Capture '00051_lightray_Step126' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step126', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Scroll until lightray_btn_color_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'lightray_btn_color_n', direction='left', offset_start=(0.538, 0.474), offset_end=(0.168, 0.474), velocity=138)
    with step("[Action] Tap lightray_btn_color_n at (56.1%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lightray_btn_color_n', 56.1, 57.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step129' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step129', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag hueSlider (51.8%,48.9%) → blackBackgroundView (19.1%,73.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 51.8, 48.9, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 19.1, 73.9, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step131' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step131', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag hueSlider (7.0%,66.0%) → blackBackgroundView (80.2%,73.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'hueSlider', 7.0, 66.0, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 80.2, 73.4, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step133' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step133', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag saturationSlider (51.5%,55.3%) → blackBackgroundView (18.6%,78.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 51.5, 55.3, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 18.6, 78.2, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step135' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step135', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag saturationSlider (7.4%,59.6%) → blackBackgroundView (81.4%,77.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'saturationSlider', 7.4, 59.6, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 81.4, 77.6, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step137' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step137', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (67.3%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 67.3, 40.8)
    with step("[Action] Tap ic_undo at (67.3%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 67.3, 40.8)
    with step("[Action] Tap ic_undo at (67.3%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 67.3, 40.8)
    with step("[Action] Tap ic_undo at (67.3%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 67.3, 40.8)
    with step("[Verify] Capture '00051_lightray_Step142' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step142', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btn_softness_n at (51.2%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_softness_n', 51.2, 30.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step144' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step144', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (7.0%,59.5%) → blackBackgroundView (73.3%,77.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.0, 59.5, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 73.3, 77.0, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step146' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step146', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap ic_undo at (81.6%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 81.6, 59.2)
    with step("[Verify] Capture '00051_lightray_Step148' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step148', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Scroll menuView left to reveal Mode"):
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'menuView', 'left', velocity=180, from_pct_x=53.3, from_pct_y=33.0, distance_pts=148.3)
    with step("[Action] Tap btn_LightRayMode_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_LightRayMode_n')
    with step("[Action] Tap btn_hue_n at (73.2%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_hue_n', 73.2, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step151' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step151', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (93.7%,64.3%) → blackBackgroundView (1.9%,76.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 93.7, 64.3, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 1.9, 76.9, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step153' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step153', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btn_swaying_n at (75.6%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_swaying_n', 75.6, 30.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=368, container_h=97)
    with step("[Verify] Capture '00051_lightray_Step155' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step155', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Drag cpSlider (8.9%,57.1%) → blackBackgroundView (78.4%,76.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 8.9, 57.1, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 78.4, 76.8, duration=1.0)
    with step("[Verify] Capture '00051_lightray_Step157' for GT comparison"):
        actions.capture_for_gt('00051_lightray_Step157', AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (83.7%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 83.7, 44.9)
    with step("[Action] Tap btnClose at (71.0%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 71.0, 51.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btnBack at (63.6%, 58.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 63.6, 58.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap btnBack at (61.8%, 55.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 61.8, 55.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap btnBack at (50.9%, 53.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 50.9, 53.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap btn_cancel_n at (36.7%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 36.7, 30.6)
    with step("[Action] Tap Discard at (40.8%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 40.8, 41.7)
    with step("[Action] Tap homeButton at (69.2%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 69.2, 76.9)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.94)
    assert True
