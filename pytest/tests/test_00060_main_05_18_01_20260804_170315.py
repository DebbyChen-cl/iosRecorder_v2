import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00060_main_05_18_01_20260804_170315")
def test_00060_main_05_18_01_20260804_170315(actions: DriverActions):
    with step("[Action] Tap Edit at (65.7%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 65.7, 64.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (83.2%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 83.2, 52.4)
    with step("[Action] Tap _AT at (10.8%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.8, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (36.2%, 83.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 36.2, 83.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (37.8%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 37.8, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_background at (39.4%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_background', 39.4, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_bgart_n at (21.2%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_bgart_n', 21.2, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap Template at (65.2%, 54.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Template', 65.2, 54.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=216, container_h=46)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"SurrealArtCell-1\"]/XCUIElementTypeImage at (34.5%, 47.6%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="SurrealArtCell-1"]/XCUIElementTypeImage', 34.5, 47.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='surrealArtItemsAreaCollectionView', container_w=430, container_h=104)
    with step("[Verify] 50 text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '50', '50')
    with step("[Verify] Capture '00060_main_05_18_01_Step11' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step11', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="surreal_art"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"surreal_art\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeSlider (50.3%,56.0%) → //XCUIElementTypeOther[@name=\"surreal_art\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3] (19.5%,57.1%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="surreal_art"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeSlider', 50.3, 56.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="surreal_art"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', 19.5, 57.1, duration=1.0)
    with step("[Verify] Capture '00060_main_05_18_01_Step13' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step13', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="surreal_art"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"surreal_art\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeSlider (6.6%,64.0%) → //XCUIElementTypeOther[@name=\"surreal_art\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3] (81.9%,53.1%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="surreal_art"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeSlider', 6.6, 64.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="surreal_art"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', 81.9, 53.1, duration=1.0)
    with step("[Verify] Capture '00060_main_05_18_01_Step15' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step15', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="surreal_art"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap ic_undo at (73.5%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 73.5, 53.1)
    with step("[Verify] Capture '00060_main_05_18_01_Step17' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step17', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="surreal_art"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap ic_redo at (30.6%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 30.6, 59.2)
    with step("[Verify] Capture '00060_main_05_18_01_Step19' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step19', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="surreal_art"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btnMask at (37.5%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMask', 37.5, 45.0)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther (4.0%,44.2%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeImage (96.0%,43.4%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', 4.0, 44.2, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeImage', 96.0, 43.4, duration=1.0)
    with step("[Verify] Capture '00060_main_05_18_01_Step22' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step22', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_undo at (93.9%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 93.9, 44.9)
    with step("[Verify] Capture '00060_main_05_18_01_Step24' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step24', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_redo at (46.9%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 46.9, 34.7)
    with step("[Verify] Capture '00060_main_05_18_01_Step26' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step26', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btt_eraser_n at (60.0%, 90.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 60.0, 90.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeSlider (45.7%,50.0%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[3] (20.7%,57.1%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeSlider', 45.7, 50.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[3]', 20.7, 57.1, duration=1.0)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther (51.2%,32.2%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeImage (51.4%,65.5%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', 51.2, 32.2, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeImage', 51.4, 65.5, duration=1.0)
    with step("[Verify] Capture '00060_main_05_18_01_Step30' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step30', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeSlider (8.6%,62.0%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[3] (81.2%,55.1%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeSlider', 8.6, 62.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[3]', 81.2, 55.1, duration=1.0)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther (4.7%,55.7%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeImage (86.5%,55.1%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', 4.7, 55.7, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeImage', 86.5, 55.1, duration=1.0)
    with step("[Verify] Capture '00060_main_05_18_01_Step33' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step33', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (26.5%, 24.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 26.5, 24.5)
    with step("[Verify] Capture '00060_main_05_18_01_Step35' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step35', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="surreal_art"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btnMask at (67.5%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMask', 67.5, 67.5)
    with step("[Action] Tap btt_eraser_n at (62.5%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 62.5, 80.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther (86.5%,33.4%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeImage (15.3%,64.3%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', 86.5, 33.4, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeImage', 15.3, 64.3, duration=1.0)
    with step("[Action] Tap btn_ok_n at (63.3%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 63.3, 38.8)
    with step("[Verify] Capture '00060_main_05_18_01_Step40' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step40', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="surreal_art"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (38.8%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 38.8, 32.7)
    with step("[Verify] Capture '00060_main_05_18_01_Step42' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step42', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_background at (51.5%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_background', 51.5, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_bgart_n at (63.6%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_bgart_n', 63.6, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap Template at (55.1%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Template', 55.1, 56.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=216, container_h=46)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"SurrealArtCell-1\"]/XCUIElementTypeImage at (42.9%, 40.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="SurrealArtCell-1"]/XCUIElementTypeImage', 42.9, 40.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='surrealArtItemsAreaCollectionView', container_w=430, container_h=104)
    with step("[Action] Tap btn_ok_n at (75.5%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 40.8)
    with step("[Verify] Capture '00060_main_05_18_01_Step48' for GT comparison"):
        actions.capture_for_gt('00060_main_05_18_01_Step48', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (73.1%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 73.1, 61.5)
    with step("[Action] Tap Discard at (68.1%, 29.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 68.1, 29.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
