import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00029_ai_replace_pro_plus')
def test_00029_ai_replace_pro_plus(actions: DriverActions):
    """AI replace pro+"""
    mode = 1
    uuid = ['4f988d5c-7fd1-4e42-a08b-ba517b5dcf94', '3ed803b2-57ec-46b7-b2f3-777f1816c3b0', '79dde802-fd3a-4beb-8b42-00be86006852', 'da9b013e-c9a0-444e-a2ed-5bc4d7b426a6', 'df42629d-cc4b-41c6-95cc-198c8377bf01', 'aded34a5-bb61-425d-9513-03899bcee3d8', '4e36bf76-7dc0-4f5b-8f39-0f82d9a832fc', 'a2e20fcf-c15e-4d8f-8f06-7077fde29890', 'd042cd4c-edb3-4f6e-939b-d0be62efd9b8', '59a65bb3-0ed7-435f-bafb-9b3b5cd2704e', 'a987ee08-11e6-4d55-992f-d8bfdd158286', '5f743ee5-b304-4e4a-8e20-9aaee7209d9a', 'c10afb92-de67-41b7-b870-d0e87febcfb8', '89f6bd08-a61d-4048-a71a-0ae74139997a', '0df234ab-291a-47b5-a172-5f946103b2f8', '88cc36fe-3a05-4aca-879e-a0abc2883aef', 'e0883a57-b8b1-4413-9111-feb9d44ab0df', 'edd3c03c-105b-4a40-b0bf-0262372f6d3a', 'da6b7171-0bce-404a-87bf-92a322196ae4', '606b59f7-62b2-4ca6-80cb-c6886dc46f07']
    with step("[Action] Tap btnSettings at (57.6%, 70.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 57.6, 70.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap About at (74.5%, 82.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 74.5, 82.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (28.6%, 24.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 28.6, 24.0)
    with step("[Action] Tap Free at (47.1%, 85.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 47.1, 85.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (56.9%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 56.9, 69.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (40.0%, 63.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 40.0, 63.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap btnBack at (67.9%, 59.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 67.9, 59.6)
    with step("[Action] Tap btnBack at (67.9%, 59.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 67.9, 59.6)
    with step("[Action] Tap btnStudio at (59.2%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnStudio', 59.2, 32.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='launcherTrendyViewConfigCollectionView', container_w=394, container_h=160)
    with step("[Action] Scroll until CMS-PhDM_AIMagic_AIReplace_20255E"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'CMS-PhDM_AIMagic_AIReplace_20255E', direction='down', offset_start=(0.354, 0.811), offset_end=(0.354, 0.135), velocity=902)
    with step("[Action] Tap CMS-PhDM_AIMagic_AIReplace_20255E at (57.4%, 20.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-PhDM_AIMagic_AIReplace_20255E', 57.4, 20.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap btnNext at (74.2%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 74.2, 36.7)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (76.2%, 79.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 76.2, 79.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap btnAlbum at (84.8%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 84.8, 66.7)
    with step("[Action] Tap _AT at (7.9%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (33.1%, 83.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 33.1, 83.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView')
    with step("[Action] Tap btt_brush_n at (65.0%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 65.0, 80.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushEraserView"]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag cpSlider (24.0%,46.0%) → brushSizeSliderView (23.7%,46.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 24.0, 46.0, AppiumBy.ACCESSIBILITY_ID, 'brushSizeSliderView', 23.7, 46.9, duration=1.0)
    with step("[Verify] valueLabel text equals '8'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '8')
    with step("[Action] Drag cpSlider (7.7%,50.0%) → slider (98.1%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.7, 50.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.1, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag instanceSegmentationGestureReceiverView (56.3%,22.2%) → instanceSegmentationGestureReceiverView (55.1%,91.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 56.3, 22.2, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 55.1, 91.4, duration=1.0)
    with step("[Verify] Capture 'AI_Replace_Pro_Plus_Step24' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_Plus_Step24', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap undoButton at (72.5%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 72.5, 52.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=591)
    with step("[Verify] Capture 'AI_Replace_Pro_Plus_Step26' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_Plus_Step26', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap redoButton at (67.5%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'redoButton', 67.5, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=591)
    with step("[Verify] Capture 'AI_Replace_Pro_Plus_Step28' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_Plus_Step28', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap btt_eraser_n at (45.0%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 45.0, 30.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushEraserView"]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag instanceSegmentationGestureReceiverView (20.7%,59.9%) → instanceSegmentationGestureReceiverView (85.1%,56.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 20.7, 59.9, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 85.1, 56.6, duration=1.0)
    with step("[Verify] Capture 'AI_Replace_Pro_Plus_Step31' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_Plus_Step31', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap undoButton at (47.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 47.5, 60.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=591)
    with step("[Verify] Capture 'AI_Replace_Pro_Plus_Step33' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_Plus_Step33', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap btnGenerate at (14.7%, 60.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 14.7, 60.7)
    with step("[Action] Tap Describe with Text at (61.8%, 40.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Describe with Text', 61.8, 40.9)
    with step("[Action] Tap lblPlaceHolder at (18.8%, 82.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 18.8, 82.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textView', container_w=394, container_h=71)
    with step("[Action] Type 'nba' into lblPlaceHolder"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 'nba')
    with step("[Action] Tap Next: at (55.1%, 53.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 55.1, 53.6)
    with step("[Verify] Replace More is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Replace More')
    with step("[Action] Tap topView_backButton at (60.0%, 65.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'topView_backButton', 60.0, 65.9)
    with step("[Action] Tap undoButton at (75.0%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 75.0, 80.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=591)
    with step("[Verify] Capture 'AI_Replace_Pro_Plus_Step42' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_Plus_Step42', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap redoButton at (67.5%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'redoButton', 67.5, 55.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=591)
    with step("[Verify] Capture 'AI_Replace_Pro_Plus_Step44' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_Plus_Step44', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap Replace at (97.1%, 43.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Replace', 97.1, 43.5)
    with step("[Action] Tap btnDescribeOption at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDescribeOption', 50.0, 50.0)
    with step("[Action] Tap lblPlaceHolder at (13.2%, 55.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 13.2, 55.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textView', container_w=394, container_h=71)
    with step("[Action] Type 'basketball' into lblPlaceHolder"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 'basketball')
    with step("[Action] Tap Next: at (54.2%, 53.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 54.2, 53.6)
    with step("[Verify] Replace More is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Replace More')
    with step("[Action] Tap topView_backButton at (45.0%, 61.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'topView_backButton', 45.0, 61.0)
    with step("[Action] Tap topView_backButton at (57.5%, 68.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'topView_backButton', 57.5, 68.3)
    with step("[Verify] Capture 'AI_Replace_Pro_Plus_Step52' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_Plus_Step52', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Edit at (44.4%, 42.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 44.4, 42.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until ic_ai_replace"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_ai_replace', direction='left', offset_start=(0.788, 0.371), offset_end=(0.121, 0.371), velocity=440)
    with step("[Action] Tap ic_ai_replace at (61.8%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_ai_replace', 61.8, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture 'AI_Replace_Pro_Plus_Step56' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_Plus_Step56', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap btt_brush_n at (20.0%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 20.0, 65.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushEraserView"]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag cpSlider (23.6%,48.0%) → slider (96.6%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 23.6, 48.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 96.6, 57.1, duration=1.0)
    with step("[Action] Drag instanceSegmentationGestureReceiverView (54.7%,22.9%) → instanceSegmentationGestureReceiverView (54.7%,89.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 54.7, 22.9, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 54.7, 89.2, duration=1.0)
    with step("[Action] Tap Replace at (98.6%, 91.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Replace', 98.6, 91.3)
    with step("[Action] Tap Describe with Text at (34.2%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Describe with Text', 34.2, 81.8)
    with step("[Action] Type 'ba' into lblPlaceHolder"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 'ba')
    with step("[Action] Tap Next: at (57.9%, 44.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 57.9, 44.6)
    with step("[Verify] Replace More is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Replace More')
    with step("[Action] Tap topView_backButton at (55.0%, 48.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'topView_backButton', 55.0, 48.8)
    with step("[Action] Tap topView_backButton at (55.0%, 48.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'topView_backButton', 55.0, 48.8)
    with step("[Action] Tap ic_ai_replace at (35.3%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_ai_replace', 35.3, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Drag instanceSegmentationGestureReceiverView (38.6%,17.3%) → instanceSegmentationGestureReceiverView (70.5%,96.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 38.6, 17.3, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 70.5, 96.0, duration=1.0)
    with step("[Verify] Capture 'AI_Replace_Pro_Plus_Step69' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_Plus_Step69', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap undoButton at (55.0%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 55.0, 80.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=640)
    with step("[Action] Tap ic_circle at (52.5%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_circle', 52.5, 55.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushEraserView"]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Paint on instanceSegmentationGestureReceiverView (28 points)"):
        actions.paint_in_element(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', [(59.3, 19.1, 0), (49.3, 22.3, 219), (42.1, 25.9, 320), (39.8, 28.8, 353), (35.3, 37.8, 403), (30.7, 51.1, 453), (28.4, 60.8, 487), (28.6, 71.2, 553), (31.2, 84.2, 687), (32.6, 87.4, 753), (43.3, 94.6, 1020), (50.9, 97.5, 1103), (59.5, 98.6, 1187), (69.1, 95.0, 1304), (74.4, 91.7, 1336), (78.8, 86.7, 1369), (81.2, 82.4, 1387), (82.6, 78.8, 1403), (83.7, 74.1, 1420), (85.6, 61.5, 1470), (85.6, 56.1, 1503), (83.7, 49.3, 1553), (74.9, 29.9, 1720), (70.2, 25.9, 1886), (67.7, 25.9, 2003), (63.0, 24.1, 2137), (59.1, 21.9, 2237), (58.8, 21.2, 2320)], duration_ms=2336)
    with step("[Verify] Capture 'AI_Replace_Pro_Plus_Step73' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_Plus_Step73', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap topView_backButton at (55.0%, 41.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'topView_backButton', 55.0, 41.5)
    with step("[Action] Tap homeButton at (73.1%, 92.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 73.1, 92.3)
    with step("[Action] Tap btnHome at (60.5%, 52.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 60.5, 52.7)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    with step("[Verify] test_00029 completion"):
        assert True
