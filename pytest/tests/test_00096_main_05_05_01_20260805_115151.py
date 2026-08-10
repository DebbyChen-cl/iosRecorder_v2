import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00096_main_05_05_01_20260805_115151")
def test_00096_main_05_05_01_20260805_115151(actions: DriverActions):
    with step("[Action] Tap Edit at (85.7%, 84.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 85.7, 84.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (73.6%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 73.6, 54.8)
    with step("[Action] Tap _AT at (7.9%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (43.1%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 43.1, 73.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (38.0%, 64.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 38.0, 64.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_overlay_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_overlay_n', direction='left', offset_start=(0.686, 0.351), offset_end=(0.247, 0.351), velocity=383)
    with step("[Action] Tap btn_overlay_n at (72.7%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_overlay_n', 72.7, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap icon_blender_s at (30.3%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_blender_s', 30.3, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=326, container_h=89)
    with step("[Verify] Capture '00096_main_05_05_01_Step09' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step09', AppiumBy.ACCESSIBILITY_ID, 'editArea', threshold=0.95)
    with step("[Verify] valueLabel text equals '75'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '75')
    with step("[Action] Tap brushButton at (41.7%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'brushButton', 41.7, 41.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectBlendingScrollView', container_w=430, container_h=651)
    with step("[Action] Drag cpSlider (46.2%,54.8%) → bottomPlaceHolderView (3.7%,27.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 46.2, 54.8, AppiumBy.ACCESSIBILITY_ID, 'bottomPlaceHolderView', 3.7, 27.7, duration=1.0)
    with step("[Verify] valueLabel text equals '8'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '8')
    with step("[Action] Drag effectBlendImageView (25.3%,18.9%) → effectBlendingScrollView (26.5%,86.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', 25.3, 18.9, AppiumBy.ACCESSIBILITY_ID, 'effectBlendingScrollView', 26.5, 86.0, duration=1.0)
    with step("[Verify] Capture '00096_main_05_05_01_Step15' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step15', AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', threshold=0.95)
    with step("[Action] Drag cpSlider (6.7%,57.1%) → bottomPlaceHolderView (80.5%,27.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.7, 57.1, AppiumBy.ACCESSIBILITY_ID, 'bottomPlaceHolderView', 80.5, 27.7, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag effectBlendImageView (3.0%,70.8%) → effectBlendingScrollView (84.9%,70.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', 3.0, 70.8, AppiumBy.ACCESSIBILITY_ID, 'effectBlendingScrollView', 84.9, 70.8, duration=1.0)
    with step("[Verify] Capture '00096_main_05_05_01_Step19' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step19', AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', threshold=0.95)
    with step("[Action] Tap btt_brush_n at (55.0%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 55.0, 70.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="menuView"]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag effectBlendImageView (7.7%,36.7%) → effectBlendingScrollView (78.4%,84.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', 7.7, 36.7, AppiumBy.ACCESSIBILITY_ID, 'effectBlendingScrollView', 78.4, 84.9, duration=1.0)
    with step("[Verify] Capture '00096_main_05_05_01_Step22' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step22', AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', threshold=0.95)
    with step("[Action] Drag cpSlider (93.9%,57.1%) → bottomPlaceHolderView (2.6%,27.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 93.9, 57.1, AppiumBy.ACCESSIBILITY_ID, 'bottomPlaceHolderView', 2.6, 27.1, duration=1.0)
    with step("[Verify] valueLabel text equals '8'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '8')
    with step("[Action] Drag effectBlendImageView (1.6%,70.8%) → effectBlendingScrollView (94.9%,70.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', 1.6, 70.8, AppiumBy.ACCESSIBILITY_ID, 'effectBlendingScrollView', 94.9, 70.4, duration=1.0)
    with step("[Verify] Capture '00096_main_05_05_01_Step26' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step26', AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', threshold=0.95)
    with step("[Action] Tap btnInvert at (62.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnInvert', 62.5, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectBlendingScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00096_main_05_05_01_Step28' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step28', AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', threshold=0.95)
    with step("[Action] Tap btnInvert at (65.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnInvert', 65.0, 52.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectBlendingScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00096_main_05_05_01_Step30' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step30', AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (24.5%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 24.5, 51.0)
    with step("[Verify] Capture '00096_main_05_05_01_Step32' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step32', AppiumBy.ACCESSIBILITY_ID, 'editArea', threshold=0.95)
    with step("[Action] Tap brushButton at (50.0%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'brushButton', 50.0, 44.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectBlendingScrollView', container_w=430, container_h=651)
    with step("[Action] Tap btt_eraser_n at (80.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 80.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="menuView"]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap btnEdge at (55.0%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnEdge', 55.0, 55.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectBlendingScrollView', container_w=430, container_h=651)
    with step("[Action] Drag cpSlider (6.7%,38.1%) → bottomPlaceHolderView (80.7%,23.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.7, 38.1, AppiumBy.ACCESSIBILITY_ID, 'bottomPlaceHolderView', 80.7, 23.9, duration=1.0)
    with step("[Action] Drag effectBlendImageView (47.7%,16.4%) → effectBlendingScrollView (47.4%,86.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', 47.7, 16.4, AppiumBy.ACCESSIBILITY_ID, 'effectBlendingScrollView', 47.4, 86.6, duration=1.0)
    with step("[Verify] Capture '00096_main_05_05_01_Step38' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step38', AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (24.5%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 24.5, 51.0)
    with step("[Action] Tap brushButton at (55.6%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'brushButton', 55.6, 61.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectBlendingScrollView', container_w=430, container_h=651)
    with step("[Action] Tap btnEdge at (52.5%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnEdge', 52.5, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectBlendingScrollView', container_w=430, container_h=651)
    with step("[Action] Drag effectBlendImageView (11.9%,30.4%) → effectBlendingScrollView (70.9%,88.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', 11.9, 30.4, AppiumBy.ACCESSIBILITY_ID, 'effectBlendingScrollView', 70.9, 88.3, duration=1.0)
    with step("[Verify] Capture '00096_main_05_05_01_Step43' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step43', AppiumBy.ACCESSIBILITY_ID, 'effectBlendImageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (83.7%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 83.7, 42.9)
    with step("[Verify] Capture '00096_main_05_05_01_Step45' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step45', AppiumBy.ACCESSIBILITY_ID, 'editArea', threshold=0.95)
    with step("[Action] Tap addSrcImageView at (55.0%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'addSrcImageView', 55.0, 57.8)
    with step("[Action] Tap btnAlbum at (69.5%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 69.5, 28.6)
    with step("[Action] Tap BG at (6.5%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'BG', 6.5, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-4 at (30.8%, 74.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4', 30.8, 74.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture '00096_main_05_05_01_Step50' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step50', AppiumBy.ACCESSIBILITY_ID, 'editArea', threshold=0.95)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'editArea')
    with step("[Action] Tap addSrcImageView at (47.5%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'addSrcImageView', 47.5, 53.1)
    with step("[Action] Tap btnCamera at (75.0%, 39.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnCamera', 75.0, 39.0)
    with step("[Action] Tap PhotoCapture at (55.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoCapture', 55.0, 52.5)
    with step("[Action] Tap Use Photo at (81.2%, 47.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Use Photo', 81.2, 47.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'editArea', expected_result='different', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (28.6%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 28.6, 34.7)
    with step("[Verify] Capture '00096_main_05_05_01_Step58' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step58', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_overlay_n at (63.6%, 93.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_overlay_n', 63.6, 93.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap icon_blender_s at (48.5%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_blender_s', 48.5, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=326, container_h=89)
    with step("[Action] Tap btn_ok_n at (59.2%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 59.2, 44.9)
    with step("[Verify] Capture '00096_main_05_05_01_Step62' for GT comparison"):
        actions.capture_for_gt('00096_main_05_05_01_Step62', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (53.8%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 53.8, 57.7)
    with step("[Action] Tap Discard at (69.6%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 69.6, 41.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
