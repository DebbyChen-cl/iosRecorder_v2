import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00061_main_05_18_03_20260804_172246")
def test_00061_main_05_18_03_20260804_172246(actions: DriverActions):
    with step("[Action] Tap Edit at (42.9%, 84.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 42.9, 84.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (75.6%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 75.6, 66.7)
    with step("[Action] Tap _AT at (10.0%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.0, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (45.4%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 45.4, 59.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (53.3%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 53.3, 51.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_background at (48.5%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_background', 48.5, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_ai_bg at (60.6%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_ai_bg', 60.6, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap btnInfo at (57.5%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnInfo', 57.5, 58.5)
    with step("[Action] Tap Continue at (74.3%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 74.3, 52.2)
    with step("[Action] Tap CMS-Style_001_Simple-Color_Morandi-Blue at (79.0%, 97.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_001_Simple-Color_Morandi-Blue', 79.0, 97.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=84)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'backgroundImageView')
    with step("[Action] Tap Generate at (58.8%, 37.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 58.8, 37.5)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'backgroundImageView', expected_result='different', threshold=0.95)
    with step("[Action] Scroll until CMS-Style_008_Balloon_Blue"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'styleCollectionView', AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_008_Balloon_Blue', direction='left', offset_start=(0.547, 0.512), offset_end=(0.293, 0.512), velocity=169)
    with step("[Action] Tap CMS-Style_008_Balloon_Blue at (58.7%, 87.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_008_Balloon_Blue', 58.7, 87.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=84)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'backgroundImageView')
    with step("[Action] Tap Generate at (81.2%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 81.2, 70.8)
    with step("[Action] Tap btnClose at (61.3%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 61.3, 48.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'backgroundImageView', expected_result='same', threshold=0.95)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'backgroundImageView')
    with step("[Action] Scroll until Custom"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'styleCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Custom', direction='right', offset_start=(0.172, 0.452), offset_end=(0.742, 0.452), velocity=497)
    with step("[Action] Tap Custom at (48.4%, 46.2%)"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Custom', 48.4, 46.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=84)
    with step("[Action] Tap promptTextView at (19.8%, 31.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 19.8, 31.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textView', container_w=359, container_h=121)
    with step("[Action] Type 'Party' into promptTextView"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 'Party')
    with step("[Action] Tap Next: at (49.5%, 51.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 49.5, 51.8)
    with step("[Action] Tap btnGenerate at (70.6%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 70.6, 30.6)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'backgroundImageView', expected_result='different', threshold=0.95)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'backgroundImageView')
    with step("[Action] Tap ic_undo at (81.6%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 81.6, 55.1)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'backgroundImageView', expected_result='different', threshold=0.95)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'backgroundImageView')
    with step("[Action] Tap ic_redo at (53.1%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 53.1, 49.0)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'backgroundImageView', expected_result='different', threshold=0.95)
    with step("[Action] Tap btnMask at (45.0%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMask', 45.0, 47.5)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther (13.0%,36.7%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeImage (81.2%,69.1%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', 13.0, 36.7, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeImage', 81.2, 69.1, duration=1.0)
    with step("[Verify] Capture '00061_main_05_18_03_Step36' for GT comparison"):
        actions.capture_for_gt('00061_main_05_18_03_Step36', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_undo at (63.3%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 63.3, 44.9)
    with step("[Verify] Capture '00061_main_05_18_03_Step38' for GT comparison"):
        actions.capture_for_gt('00061_main_05_18_03_Step38', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_redo at (85.7%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 85.7, 49.0)
    with step("[Verify] Capture '00061_main_05_18_03_Step40' for GT comparison"):
        actions.capture_for_gt('00061_main_05_18_03_Step40', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btt_eraser_n at (62.5%, 77.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 62.5, 77.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther (76.3%,34.0%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeImage (13.5%,67.5%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', 76.3, 34.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeImage', 13.5, 67.5, duration=1.0)
    with step("[Verify] Capture '00061_main_05_18_03_Step43' for GT comparison"):
        actions.capture_for_gt('00061_main_05_18_03_Step43', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeSlider (47.0%,58.0%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[3] (81.6%,53.1%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeSlider', 47.0, 58.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[3]', 81.6, 53.1, duration=1.0)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther (11.2%,32.7%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeImage (61.9%,67.3%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', 11.2, 32.7, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeImage', 61.9, 67.3, duration=1.0)
    with step("[Verify] Capture '00061_main_05_18_03_Step46' for GT comparison"):
        actions.capture_for_gt('00061_main_05_18_03_Step46', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (36.7%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 36.7, 53.1)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'backgroundImageView')
    with step("[Action] Tap btnMask at (75.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMask', 75.0, 52.5)
    with step("[Action] Tap btt_eraser_n at (32.5%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 32.5, 65.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther (13.0%,34.8%) → //XCUIElementTypeOther[@name=\"photodirector.SurrealArtEraserViewController\"]/XCUIElementTypeOther/XCUIElementTypeImage (84.4%,68.5%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', 13.0, 34.8, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SurrealArtEraserViewController"]/XCUIElementTypeOther/XCUIElementTypeImage', 84.4, 68.5, duration=1.0)
    with step("[Action] Tap btn_ok_n at (81.6%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 42.9)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'backgroundImageView', expected_result='different', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (91.8%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 91.8, 32.7)
    with step("[Action] Tap homeButton at (73.1%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 73.1, 69.2)
    with step("[Action] Tap Discard at (71.0%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 71.0, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
