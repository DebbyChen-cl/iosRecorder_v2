import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00080_main_05_07_14_20260805_110635")
def test_00080_main_05_07_14_20260805_110635(actions: DriverActions):
    with step("[Action] Tap Edit at (42.9%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 42.9, 44.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (76.1%, 69.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 76.1, 69.0)
    with step("[Action] Tap _AT at (9.0%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.0, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (46.2%, 76.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 46.2, 76.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (41.9%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 41.9, 48.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (60.6%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 60.6, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_conceal_portrait at (54.5%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 54.5, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_skintone_portrait at (61.8%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_skintone_portrait', 61.8, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Verify] Capture '00080_main_05_07_14_Step09' for GT comparison"):
        actions.capture_for_gt('00080_main_05_07_14_Step09', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="contentView"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap cellColor-1 at (71.0%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'cellColor-1', 71.0, 54.8)
    with step("[Verify] Capture '00080_main_05_07_14_Step11' for GT comparison"):
        actions.capture_for_gt('00080_main_05_07_14_Step11', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="contentView"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap cellColor-2 at (26.7%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'cellColor-2', 26.7, 64.5)
    with step("[Verify] Capture '00080_main_05_07_14_Step13' for GT comparison"):
        actions.capture_for_gt('00080_main_05_07_14_Step13', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="contentView"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap cellColor-3 at (67.7%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'cellColor-3', 67.7, 64.5)
    with step("[Verify] Capture '00080_main_05_07_14_Step15' for GT comparison"):
        actions.capture_for_gt('00080_main_05_07_14_Step15', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="contentView"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap cellColor-4 at (63.3%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'cellColor-4', 63.3, 54.8)
    with step("[Verify] Capture '00080_main_05_07_14_Step17' for GT comparison"):
        actions.capture_for_gt('00080_main_05_07_14_Step17', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="contentView"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag centerSlider (50.4%,52.0%) → backgroundView (19.8%,79.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.4, 52.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 19.8, 79.4, duration=1.0)
    with step("[Verify] Capture '00080_main_05_07_14_Step19' for GT comparison"):
        actions.capture_for_gt('00080_main_05_07_14_Step19', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="contentView"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag centerSlider (7.0%,52.0%) → backgroundView (82.1%,79.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 7.0, 52.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 82.1, 79.6, duration=1.0)
    with step("[Verify] Capture '00080_main_05_07_14_Step21' for GT comparison"):
        actions.capture_for_gt('00080_main_05_07_14_Step21', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="contentView"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag centerSlider (89.4%,52.0%) → backgroundView (16.3%,85.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 89.4, 52.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 16.3, 85.1, duration=1.0)
    with step("[Verify] Capture '00080_main_05_07_14_Step23' for GT comparison"):
        actions.capture_for_gt('00080_main_05_07_14_Step23', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="contentView"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag centerSlider (7.4%,54.0%) → backgroundView (81.9%,85.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 7.4, 54.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 81.9, 85.0, duration=1.0)
    with step("[Verify] Capture '00080_main_05_07_14_Step25' for GT comparison"):
        actions.capture_for_gt('00080_main_05_07_14_Step25', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="contentView"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (49.0%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 49.0, 34.7)
    with step("[Verify] Capture '00080_main_05_07_14_Step27' for GT comparison"):
        actions.capture_for_gt('00080_main_05_07_14_Step27', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="contentView"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_redo at (44.9%, 22.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 44.9, 22.4)
    with step("[Verify] Capture '00080_main_05_07_14_Step29' for GT comparison"):
        actions.capture_for_gt('00080_main_05_07_14_Step29', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="contentView"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (79.6%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 79.6, 26.5)
    with step("[Action] Tap btnClose at (54.8%, 61.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 54.8, 61.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (36.7%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 36.7, 49.0)
    with step("[Action] Tap btn_cancel_n at (42.9%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 42.9, 49.0)
    with step("[Action] Tap Edit at (80.4%, 64.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 80.4, 64.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_crop at (63.6%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_crop', 63.6, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_crop_raotate at (75.8%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_crop_raotate', 75.8, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Scroll until ic_square"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'croppingRotationCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_square', direction='left', offset_start=(0.735, 0.234), offset_end=(0.228, 0.234), velocity=145)
    with step("[Action] Tap ic_square at (57.5%, 68.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_square', 57.5, 68.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Action] Scroll until ic_4v3"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'croppingRotationCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_4v3', direction='left', offset_start=(0.722, 0.25), offset_end=(0.309, 0.25), velocity=303)
    with step("[Action] Tap ic_4v3 at (41.5%, 65.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_4v3', 41.5, 65.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Action] Tap ic_3v2 at (32.5%, 61.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_3v2', 32.5, 61.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Action] Tap ic_16v9 at (19.5%, 63.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_16v9', 19.5, 63.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='croppingRotationCollectionView', container_w=430, container_h=64)
    with step("[Action] Tap btn_ok_n at (79.6%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 79.6, 34.7)
    with step("[Action] Tap Portrait at (50.0%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 50.0, 44.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (66.7%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 66.7, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_conceal_portrait at (27.3%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 27.3, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_skintone_portrait at (50.0%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_skintone_portrait', 50.0, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Verify] No bodies were detected. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'No bodies were detected.')
    with step("[Action] Tap OK at (53.6%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 53.6, 41.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView', container_w=430, container_h=694)
    with step("[Action] Tap btn_cancel_n at (32.7%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 32.7, 36.7)
    with step("[Action] Tap homeButton at (61.5%, 88.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 88.5)
    with step("[Action] Tap Discard at (60.9%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 60.9, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
