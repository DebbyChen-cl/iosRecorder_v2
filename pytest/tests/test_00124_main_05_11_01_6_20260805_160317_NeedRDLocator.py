import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00124_main_05_11_01_6_20260805_160317")
def test_00124_main_05_11_01_6_20260805_160317(actions: DriverActions):
    with step("[Action] Tap Edit at (48.6%, 68.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 48.6, 68.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (72.6%, 73.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 72.6, 73.8)
    with step("[Action] Tap _AT at (6.5%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 6.5, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (39.2%, 92.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 39.2, 92.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (57.8%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 57.8, 51.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_addimg_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', direction='left', offset_start=(0.6, 0.474), offset_end=(0.24, 0.474), velocity=412)
    with step("[Action] Tap btn_addimg_n at (39.4%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', 39.4, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap photoCell-1 at (61.5%, 66.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 61.5, 66.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Pinch imageView scale=3.627"):
        actions.pinch(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'imageView'), scale=3.627, velocity=1.596)
    with step("[Action] Rotate imageView 41.6°"):
        actions.rotate(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'imageView'), rotation=41.6)
    with step("[Action] Scroll until lblText"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', AppiumBy.ACCESSIBILITY_ID, 'lblText', direction='left', offset_start=(0.67, 0.451), offset_end=(0.288, 0.451), velocity=303)
    with step("[Action] Tap lblText at (48.4%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lblText', 48.4, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap ic_foreground at (42.5%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_foreground', 42.5, 52.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] Capture '00124_main_05_11_01_6_Step14' for GT comparison"):
        actions.capture_for_gt('00124_main_05_11_01_6_Step14', AppiumBy.ACCESSIBILITY_ID, 'CLViewContainer', threshold=0.95)
    with step("[Action] Tap btt_eraser_n at (62.5%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 62.5, 75.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag cpSlider (22.1%,58.0%) → slider (97.8%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 22.1, 58.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 97.8, 55.1, duration=1.0)
    with step("[Action] Drag EditingImageView_ImageView (17.4%,11.1%) → EditingImageView_ImageView (64.2%,90.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 17.4, 11.1, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 64.2, 90.5, duration=1.0)
    with step("[Verify] Capture '00124_main_05_11_01_6_Step18' for GT comparison"):
        actions.capture_for_gt('00124_main_05_11_01_6_Step18', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btt_brush_n at (45.0%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 45.0, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag EditingImageView_ImageView (76.0%,16.9%) → EditingImageView_ImageView (25.8%,84.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 76.0, 16.9, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 25.8, 84.4, duration=1.0)
    with step("[Verify] Capture '00124_main_05_11_01_6_Step21' for GT comparison"):
        actions.capture_for_gt('00124_main_05_11_01_6_Step21', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_foreground at (70.0%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_foreground', 70.0, 65.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap Cutout at (49.1%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cutout', 49.1, 42.9)
    with step("[Action] Tap stroke_thumb_6 at (42.4%, 63.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_6', 42.4, 63.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='strokeCollection', container_w=337, container_h=71)
    with step("[Verify] Capture '00124_main_05_11_01_6_Step25' for GT comparison"):
        actions.capture_for_gt('00124_main_05_11_01_6_Step25', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Drag cpSlider (51.2%,61.0%) → valueLabel (21.5%,62.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 51.2, 61.0, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 21.5, 62.5, duration=1.0)
    with step("[Verify] Capture '00124_main_05_11_01_6_Step27' for GT comparison"):
        actions.capture_for_gt('00124_main_05_11_01_6_Step27', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="cutout_with_design"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (91.8%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 91.8, 44.9)
    with step("[Verify] Capture '00124_main_05_11_01_6_Step29' for GT comparison"):
        actions.capture_for_gt('00124_main_05_11_01_6_Step29', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap maskButton at (62.5%, 42.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'maskButton', 62.5, 42.5)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther (23.4%,7.9%) → //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage (41.9%,79.6%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther', 23.4, 7.9, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', 41.9, 79.6, duration=1.0)
    with step("[Action] Tap btt_brush_n at (50.0%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 50.0, 65.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="menuView"]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (47.1%,52.4%) → sliderArea (4.2%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 47.1, 52.4, AppiumBy.ACCESSIBILITY_ID, 'sliderArea', 4.2, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '8'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '8')
    with step("[Action] Drag cpSlider (3.8%,54.8%) → sliderArea (78.1%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 3.8, 54.8, AppiumBy.ACCESSIBILITY_ID, 'sliderArea', 78.1, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther (28.5%,7.6%) → //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage (35.1%,69.5%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther', 28.5, 7.6, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', 35.1, 69.5, duration=1.0)
    with step("[Verify] Capture '00124_main_05_11_01_6_Step39' for GT comparison"):
        actions.capture_for_gt('00124_main_05_11_01_6_Step39', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (55.1%, 61.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 55.1, 61.2)
    with step("[Verify] Capture '00124_main_05_11_01_6_Step41' for GT comparison"):
        actions.capture_for_gt('00124_main_05_11_01_6_Step41', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_redo at (69.4%, 22.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 69.4, 22.4)
    with step("[Verify] Capture '00124_main_05_11_01_6_Step43' for GT comparison"):
        actions.capture_for_gt('00124_main_05_11_01_6_Step43', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (24.5%, 24.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 24.5, 24.5)
    with step("[Action] Tap btn_ok_n at (34.7%, 20.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 34.7, 20.4)
    with step("[Action] Tap AlertDialog-btnPositive at (61.4%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 61.4, 56.0)
    with step("[Action] Tap homeButton at (65.4%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 65.4)
    with step("[Action] Tap Discard at (55.1%, 45.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 55.1, 45.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
