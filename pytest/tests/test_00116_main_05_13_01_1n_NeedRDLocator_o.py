import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00116_main_05_13_01_1n_20260805_145011")
def test_00116_main_05_13_01_1n_20260805_145011(actions: DriverActions):
    with step("[Action] Tap Edit at (48.6%, 28.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 48.6, 28.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (83.2%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 83.2, 42.9)
    with step("[Action] Tap _AT at (10.8%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.8, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (34.6%, 73.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 34.6, 73.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (71.1%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 71.1, 51.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_sticker_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_sticker_n', direction='left', offset_start=(0.744, 0.423), offset_end=(0.174, 0.423), velocity=470)
    with step("[Action] Tap btn_sticker_n at (54.5%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_sticker_n', 54.5, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_stickerin at (36.4%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_stickerin', 36.4, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap CMS-phdm_Paper[01-fs8] at (45.5%, 52.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_Paper[01-fs8]', 45.5, 52.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView[2]', container_w=412, container_h=287)
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step10' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step10', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Drag imageView (53.0%,50.5%) → backgroundView (51.4%,60.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'imageView', 53.0, 50.5, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 51.4, 60.0, duration=1.0)
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step12' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step12', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (38.8%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 38.8, 40.8)
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step14' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step14', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_sticker_n at (100.0%, 39.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_sticker_n', 100.0, 39.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_stickerin at (57.6%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_stickerin', 57.6, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap CMS-phdm_Shadow[34-fs8] at (51.9%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_Shadow[34-fs8]', 51.9, 53.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView[2]', container_w=412, container_h=287)
    with step("[Action] Rotate imageView 48.9°"):
        actions.rotate(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'imageView'), rotation=48.9)
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step19' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step19', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Drag rotateImageView (51.9%,44.4%) → backgroundView (19.1%,46.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'rotateImageView', 51.9, 44.4, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 19.1, 46.1, duration=1.0)
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step21' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step21', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (26.5%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 26.5, 40.8)
    with step("[Action] Tap btn_sticker_n at (57.6%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_sticker_n', 57.6, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_stickerin at (45.5%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_stickerin', 45.5, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap CMS-phdm_sticker_text_220220519Thumbnail[11-fs8] at (58.4%, 56.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_sticker_text_220220519Thumbnail[11-fs8]', 58.4, 56.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView[2]', container_w=412, container_h=287)
    with step("[Action] Rotate imageView 38.1°"):
        actions.rotate(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'imageView'), rotation=38.1)
    with step("[Action] Tap btnFlip at (55.6%, 29.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnFlip', 55.6, 29.6)
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step28' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step28', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap imageView at (53.7%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 53.7, 52.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] lblOpacityVal text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '0')
    with step("[Verify] lblBlurVal text equals '40'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblBlurVal', '40')
    with step("[Action] Drag sliderOpacity (9.1%,58.0%) → backgroundView (78.8%,76.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'sliderOpacity', 9.1, 58.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 78.8, 76.1, duration=1.0)
    with step("[Verify] lblOpacityVal text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '100')
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step34' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step34', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Drag sliderBlur (43.4%,60.0%) → backgroundView (24.0%,81.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'sliderBlur', 43.4, 60.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 24.0, 81.1, duration=1.0)
    with step("[Verify] lblBlurVal text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblBlurVal', '0')
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step37' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step37', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Drag sliderBlur (7.9%,56.0%) → backgroundView (77.7%,81.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'sliderBlur', 7.9, 56.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 77.7, 81.3, duration=1.0)
    with step("[Verify] lblBlurVal text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblBlurVal', '100')
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step40' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step40', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap imageView at (58.5%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 58.5, 80.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap imageView at (61.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 61.0, 52.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] lblVal text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '100')
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step44' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step44', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Drag slider (91.3%,48.0%) → backgroundView (24.4%,80.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 91.3, 48.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 24.4, 80.8, duration=1.0)
    with step("[Verify] lblVal text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '0')
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step47' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step47', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Drag slider (9.5%,48.0%) → backgroundView (77.9%,80.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'slider', 9.5, 48.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 77.9, 80.7, duration=1.0)
    with step("[Verify] lblVal text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblVal', '100')
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step50' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step50', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap btnDelete at (55.6%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDelete', 55.6, 55.6)
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step52' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step52', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (52.0%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 52.0, 28.6)
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step54' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step54', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_redo at (70.0%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 70.0, 53.1)
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step56' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step56', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (68.0%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 68.0, 46.9)
    with step("[Action] Tap imageView at (53.0%, 50.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 53.0, 50.3)
    with step("[Action] Tap btnDuplicate at (59.3%, 51.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDuplicate', 59.3, 51.9)
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step60' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step60', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (72.0%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 72.0, 44.9)
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step62' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step62', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_redo at (74.0%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 74.0, 53.1)
    with step("[Verify] Capture '00116_main_05_13_01_1n_Step64' for GT comparison"):
        actions.capture_for_gt('00116_main_05_13_01_1n_Step64', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (71.4%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 71.4, 44.9)
    with step("[Action] Tap OK at (96.7%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 96.7, 66.7)
    with step("[Action] Tap exportButton at (30.8%, 34.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'exportButton', 30.8, 34.6)
    with step("[Action] Tap btnShareMore at (41.9%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareMore', 41.9, 44.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=786)
    with step("[Action] Tap //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[6]/XCUIElementTypePopover at (85.9%, 43.0%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[6]/XCUIElementTypePopover', 85.9, 43.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=786)
    with step("[Verify] U Team is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'U Team')
    with step("[Action] Tap Cancel at (73.8%, 65.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 73.8, 65.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='activityCollectionView', container_w=412, container_h=377)
    with step("[Action] Tap btnShareIG at (47.0%, 35.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareIG', 47.0, 35.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=786)
    with step("[Verify] Share to Instagram is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram')
    with step("[Action] Tap //XCUIElementTypeApplication[@name=\"Instagram\"]/XCUIElementTypeWindow/XCUIElementTypeOther[2] at (8.8%, 4.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="Instagram"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]', 8.8, 4.5)
    with step("[Action] Tap btnShareFB at (59.3%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB', 59.3, 44.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=786)
    with step("[Verify] New post is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'New post')
    with step("[Action] Tap composer-left-button at (50.0%, 30.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'composer-left-button', 50.0, 30.8)
    with step("[Action] Tap navHomeButton at (54.5%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton', 54.5, 51.1)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
