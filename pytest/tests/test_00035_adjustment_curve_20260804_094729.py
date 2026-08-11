import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00035_adjustment_curve_20260804_094729")
def test_00035_adjustment_curve_20260804_094729(actions: DriverActions):
    with step("[Action] Tap Edit at (48.6%, 84.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 48.6, 84.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (85.3%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 85.3, 57.1)
    with step("[Action] Tap _AT at (10.8%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.8, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (70.0%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 70.0, 70.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Enhance at (57.1%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 57.1, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap btn_adjustment_n at (60.6%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_adjustment_n', 60.6, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Color at (42.1%, 58.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Color', 42.1, 58.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=206, container_h=46)
    with step("[Action] Tap ic_curve at (66.7%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_curve', 66.7, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Tap btn arrow down n at (55.0%, 42.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n', 55.0, 42.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Verify] Capture '00035_adjustment_curve_Step11' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step11', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AdjustmentsProViewController"]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn arrow down n at (57.5%, 17.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n', 57.5, 17.5)
    with step("[Verify] Capture '00035_adjustment_curve_Step13' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step13', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AdjustmentsProViewController"]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Verify] Capture '00035_adjustment_curve_Step14' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step14', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap tab icon b n at (64.4%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'tab icon b n', 64.4, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Action] Drag CurveView (74.0%,30.9%) → PhotoDirector (75.8%,73.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'CurveView', 74.0, 30.9, AppiumBy.ACCESSIBILITY_ID, 'PhotoDirector', 75.8, 73.1, duration=1.0)
    with step("[Verify] Capture '00035_adjustment_curve_Step17' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step17', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Verify] Capture '00035_adjustment_curve_Step18' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step18', AppiumBy.ACCESSIBILITY_ID, 'CurveView', threshold=0.95)
    with step("[Action] Tap btnHSLCurveReset at (72.5%, 72.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset', 72.5, 72.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Verify] Capture '00035_adjustment_curve_Step20' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step20', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Verify] Capture '00035_adjustment_curve_Step21' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step21', AppiumBy.ACCESSIBILITY_ID, 'CurveView', threshold=0.95)
    with step("[Action] Tap tab icon g n at (48.9%, 41.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'tab icon g n', 48.9, 41.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Action] Drag CurveView (73.2%,28.4%) → editingImageView (75.8%,99.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'CurveView', 73.2, 28.4, AppiumBy.ACCESSIBILITY_ID, 'editingImageView', 75.8, 99.8, duration=1.0)
    with step("[Verify] Capture '00035_adjustment_curve_Step24' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step24', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Verify] Capture '00035_adjustment_curve_Step25' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step25', AppiumBy.ACCESSIBILITY_ID, 'CurveView', threshold=0.95)
    with step("[Action] Tap btnHSLCurveReset at (72.5%, 32.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset', 72.5, 32.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Verify] Capture '00035_adjustment_curve_Step27' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step27', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Verify] Capture '00035_adjustment_curve_Step28' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step28', AppiumBy.ACCESSIBILITY_ID, 'CurveView', threshold=0.95)
    with step("[Action] Tap curve tab icon r n at (40.0%, 58.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'curve tab icon r n', 40.0, 58.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Action] Drag CurveView (74.0%,25.9%) → PhotoDirector (75.8%,73.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'CurveView', 74.0, 25.9, AppiumBy.ACCESSIBILITY_ID, 'PhotoDirector', 75.8, 73.1, duration=1.0)
    with step("[Verify] Capture '00035_adjustment_curve_Step31' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step31', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Verify] Capture '00035_adjustment_curve_Step32' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step32', AppiumBy.ACCESSIBILITY_ID, 'CurveView', threshold=0.95)
    with step("[Action] Tap btnHSLCurveReset at (72.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset', 72.5, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Verify] Capture '00035_adjustment_curve_Step34' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step34', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Verify] Capture '00035_adjustment_curve_Step35' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step35', AppiumBy.ACCESSIBILITY_ID, 'CurveView', threshold=0.95)
    with step("[Action] Tap curve tab icon rgb n at (68.9%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'curve tab icon rgb n', 68.9, 51.1)
    with step("[Action] Drag CurveView (77.8%,25.3%) → editingImageView (78.6%,99.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'CurveView', 77.8, 25.3, AppiumBy.ACCESSIBILITY_ID, 'editingImageView', 78.6, 99.7, duration=1.0)
    with step("[Verify] Capture '00035_adjustment_curve_Step38' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step38', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Verify] Capture '00035_adjustment_curve_Step39' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step39', AppiumBy.ACCESSIBILITY_ID, 'CurveView', threshold=0.95)
    with step("[Action] Tap btnHSLCurveReset at (52.5%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset', 52.5, 40.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=620)
    with step("[Verify] Capture '00035_adjustment_curve_Step41' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step41', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Verify] Capture '00035_adjustment_curve_Step42' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step42', AppiumBy.ACCESSIBILITY_ID, 'CurveView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (24.5%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 24.5, 51.0)
    with step("[Verify] Capture '00035_adjustment_curve_Step44' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step44', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_adjustment_n at (60.6%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_adjustment_n', 60.6, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Color at (68.4%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Color', 68.4, 56.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=206, container_h=46)
    with step("[Action] Tap ic_curve at (15.2%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_curve', 15.2, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='AdjustmentEffectBottomBar', container_w=430, container_h=71)
    with step("[Action] Drag CurveView (73.7%,26.5%) → editingImageView (76.0%,97.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'CurveView', 73.7, 26.5, AppiumBy.ACCESSIBILITY_ID, 'editingImageView', 76.0, 97.9, duration=1.0)
    with step("[Action] Tap btn_ok_n at (71.4%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 71.4, 38.8)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.95)
    with step("[Verify] Capture '00035_adjustment_curve_Step51' for GT comparison"):
        actions.capture_for_gt('00035_adjustment_curve_Step51', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (42.3%, 92.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 42.3, 92.3)
    with step("[Action] Tap Discard at (40.6%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 40.6, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
