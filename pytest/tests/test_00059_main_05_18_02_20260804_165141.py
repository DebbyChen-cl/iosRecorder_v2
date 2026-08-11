import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00059_main_05_18_02_20260804_165141")
def test_00059_main_05_18_02_20260804_165141(actions: DriverActions):
    with step("[Action] Tap Edit at (68.6%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 68.6, 52.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (77.2%, 64.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 77.2, 64.3)
    with step("[Action] Tap _AT at (8.6%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.6, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (51.5%, 78.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 51.5, 78.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (53.3%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 53.3, 48.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_background at (39.4%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_background', 39.4, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_bgart_n at (42.4%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_bgart_n', 42.4, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap CMS-phdm_BG_Greenery_18_free_trending at (43.1%, 63.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_BG_Greenery_18_free_trending', 43.1, 63.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="backgroundItemPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=410, container_h=64)
    with step("[Verify] labelColorMatchValueHint text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'labelColorMatchValueHint', '50')
    with step("[Verify] Capture '00059_main_05_18_02_Step10' for GT comparison"):
        actions.capture_for_gt('00059_main_05_18_02_Step10', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="editRegionView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag colorMatchingSlider (50.8%,51.0%) → colorMatchAdjustView (6.3%,59.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'colorMatchingSlider', 50.8, 51.0, AppiumBy.ACCESSIBILITY_ID, 'colorMatchAdjustView', 6.3, 59.1, duration=1.0)
    with step("[Verify] labelColorMatchValueHint text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'labelColorMatchValueHint', '0')
    with step("[Verify] Capture '00059_main_05_18_02_Step13' for GT comparison"):
        actions.capture_for_gt('00059_main_05_18_02_Step13', AppiumBy.ACCESSIBILITY_ID, 'stickerImageEditingView', threshold=0.95)
    with step("[Action] Drag colorMatchingSlider (7.2%,46.9%) → colorMatchAdjustView (73.7%,56.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'colorMatchingSlider', 7.2, 46.9, AppiumBy.ACCESSIBILITY_ID, 'colorMatchAdjustView', 73.7, 56.8, duration=1.0)
    with step("[Verify] Capture '00059_main_05_18_02_Step15' for GT comparison"):
        actions.capture_for_gt('00059_main_05_18_02_Step15', AppiumBy.ACCESSIBILITY_ID, 'stickerImageEditingView', threshold=0.95)
    with step("[Verify] labelColorMatchValueHint text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'labelColorMatchValueHint', '100')
    with step("[Action] Tap ic_undo at (71.4%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 71.4, 51.0)
    with step("[Verify] Capture '00059_main_05_18_02_Step18' for GT comparison"):
        actions.capture_for_gt('00059_main_05_18_02_Step18', AppiumBy.ACCESSIBILITY_ID, 'stickerImageEditingView', threshold=0.95)
    with step("[Action] Tap ic_redo at (75.5%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 75.5, 40.8)
    with step("[Verify] Capture '00059_main_05_18_02_Step20' for GT comparison"):
        actions.capture_for_gt('00059_main_05_18_02_Step20', AppiumBy.ACCESSIBILITY_ID, 'stickerImageEditingView', threshold=0.95)
    with step("[Action] Tap btnMask at (65.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMask', 65.0, 52.5)
    with step("[Action] Tap btt_eraser_n at (47.5%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 47.5, 47.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] Capture '00059_main_05_18_02_Step23' for GT comparison"):
        actions.capture_for_gt('00059_main_05_18_02_Step23', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther (18.6%,32.5%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeImage (83.0%,67.8%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', 18.6, 32.5, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeImage', 83.0, 67.8, duration=1.0)
    with step("[Verify] Capture '00059_main_05_18_02_Step25' for GT comparison"):
        actions.capture_for_gt('00059_main_05_18_02_Step25', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_undo at (71.4%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 71.4, 49.0)
    with step("[Verify] Capture '00059_main_05_18_02_Step27' for GT comparison"):
        actions.capture_for_gt('00059_main_05_18_02_Step27', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_redo at (87.8%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 87.8, 42.9)
    with step("[Verify] Capture '00059_main_05_18_02_Step29' for GT comparison"):
        actions.capture_for_gt('00059_main_05_18_02_Step29', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther (90.0%,37.3%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeImage (30.7%,69.0%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', 90.0, 37.3, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeImage', 30.7, 69.0, duration=1.0)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeSlider (45.7%,60.0%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[3] (81.6%,61.2%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeSlider', 45.7, 60.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[3]', 81.6, 61.2, duration=1.0)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther (54.0%,32.1%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeImage (55.3%,69.1%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', 54.0, 32.1, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeImage', 55.3, 69.1, duration=1.0)
    with step("[Verify] Capture '00059_main_05_18_02_Step33' for GT comparison"):
        actions.capture_for_gt('00059_main_05_18_02_Step33', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (30.6%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 30.6, 32.7)
    with step("[Action] Tap btnMask at (57.5%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMask', 57.5, 67.5)
    with step("[Action] Tap btt_eraser_n at (50.0%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 50.0, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther (14.2%,37.2%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeImage (82.3%,63.9%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', 14.2, 37.2, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeImage', 82.3, 63.9, duration=1.0)
    with step("[Action] Tap btn_ok_n at (63.3%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 63.3, 49.0)
    with step("[Verify] Capture '00059_main_05_18_02_Step39' for GT comparison"):
        actions.capture_for_gt('00059_main_05_18_02_Step39', AppiumBy.ACCESSIBILITY_ID, 'stickerImageEditingView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (34.7%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 34.7, 46.9)
    with step("[Verify] Capture '00059_main_05_18_02_Step41' for GT comparison"):
        actions.capture_for_gt('00059_main_05_18_02_Step41', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_background at (39.4%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_background', 39.4, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_bgart_n at (54.5%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_bgart_n', 54.5, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap CMS-phdm_BG_Greenery_18_free_trending at (59.7%, 65.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_BG_Greenery_18_free_trending', 59.7, 65.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="backgroundItemPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=410, container_h=64)
    with step("[Action] Tap btn_ok_n at (83.7%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 83.7, 57.1)
    with step("[Verify] Capture '00059_main_05_18_02_Step46' for GT comparison"):
        actions.capture_for_gt('00059_main_05_18_02_Step46', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (65.4%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 73.1)
    with step("[Action] Tap Discard at (92.8%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 92.8, 75.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
