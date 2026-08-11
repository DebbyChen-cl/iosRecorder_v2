import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00058_main_05_04a_07_20260804_164540")
def test_00058_main_05_04a_07_20260804_164540(actions: DriverActions):
    with step("[Action] Tap Edit at (45.7%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 45.7, 64.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (85.3%, 69.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 85.3, 69.0)
    with step("[Action] Tap _AT at (5.7%, 90.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 5.7, 90.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (26.2%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 26.2, 40.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (47.9%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 47.9, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_icon_invert_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_icon_invert_n', direction='left', offset_start=(0.621, 0.546), offset_end=(0.209, 0.546), velocity=369)
    with step("[Action] Tap btn_icon_invert_n at (88.2%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_icon_invert_n', 88.2, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Verify] Capture '00058_main_05_04a_07_Step08' for GT comparison"):
        actions.capture_for_gt('00058_main_05_04a_07_Step08', AppiumBy.ACCESSIBILITY_ID, 'zoomView', threshold=0.95)
    with step("[Action] Tap autoFocusButton at (80.0%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'autoFocusButton', 80.0, 30.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=670)
    with step("[Verify] Capture '00058_main_05_04a_07_Step10' for GT comparison"):
        actions.capture_for_gt('00058_main_05_04a_07_Step10', AppiumBy.ACCESSIBILITY_ID, 'zoomView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (75.5%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 32.7)
    with step("[Verify] Capture '00058_main_05_04a_07_Step12' for GT comparison"):
        actions.capture_for_gt('00058_main_05_04a_07_Step12', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (53.8%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 53.8, 76.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00058_main_05_04a_07_Step14' for GT comparison"):
        actions.capture_for_gt('00058_main_05_04a_07_Step14', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_icon_invert_n at (70.6%, 78.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_icon_invert_n', 70.6, 78.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Action] Tap maskInvertButton at (47.5%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'maskInvertButton', 47.5, 45.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=670)
    with step("[Verify] Capture '00058_main_05_04a_07_Step17' for GT comparison"):
        actions.capture_for_gt('00058_main_05_04a_07_Step17', AppiumBy.ACCESSIBILITY_ID, 'zoomView', threshold=0.95)
    with step("[Action] Tap btt_eraser_n at (50.0%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 50.0, 55.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="panelView"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag cpSlider (50.3%,45.2%) → slider (2.1%,61.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 50.3, 45.2, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.1, 61.0, duration=1.0)
    with step("[Action] Drag zoomView (50.9%,12.2%) → zoomView (53.7%,87.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'zoomView', 50.9, 12.2, AppiumBy.ACCESSIBILITY_ID, 'zoomView', 53.7, 87.8, duration=1.0)
    with step("[Verify] Capture '00058_main_05_04a_07_Step21' for GT comparison"):
        actions.capture_for_gt('00058_main_05_04a_07_Step21', AppiumBy.ACCESSIBILITY_ID, 'zoomView', threshold=0.95)
    with step("[Action] Drag cpSlider (5.4%,61.9%) → slider (99.0%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.4, 61.9, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.0, 56.1, duration=1.0)
    with step("[Action] Drag zoomView (10.2%,46.0%) → zoomView (88.4%,46.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'zoomView', 10.2, 46.0, AppiumBy.ACCESSIBILITY_ID, 'zoomView', 88.4, 46.1, duration=1.0)
    with step("[Verify] Capture '00058_main_05_04a_07_Step24' for GT comparison"):
        actions.capture_for_gt('00058_main_05_04a_07_Step24', AppiumBy.ACCESSIBILITY_ID, 'zoomView', threshold=0.95)
    with step("[Action] Tap maskInvertButton at (50.0%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'maskInvertButton', 50.0, 40.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=670)
    with step("[Verify] Capture '00058_main_05_04a_07_Step26' for GT comparison"):
        actions.capture_for_gt('00058_main_05_04a_07_Step26', AppiumBy.ACCESSIBILITY_ID, 'zoomView', threshold=0.95)
    with step("[Action] Tap ic_undo at (61.2%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 61.2, 49.0)
    with step("[Verify] Capture '00058_main_05_04a_07_Step28' for GT comparison"):
        actions.capture_for_gt('00058_main_05_04a_07_Step28', AppiumBy.ACCESSIBILITY_ID, 'zoomView', threshold=0.95)
    with step("[Action] Tap ic_redo at (73.5%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 73.5, 44.9)
    with step("[Verify] Capture '00058_main_05_04a_07_Step30' for GT comparison"):
        actions.capture_for_gt('00058_main_05_04a_07_Step30', AppiumBy.ACCESSIBILITY_ID, 'zoomView', threshold=0.95)
    with step("[Action] Tap btt_brush_n at (72.5%, 77.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 72.5, 77.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="panelView"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag zoomView (20.5%,17.5%) → zoomView (80.9%,78.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'zoomView', 20.5, 17.5, AppiumBy.ACCESSIBILITY_ID, 'zoomView', 80.9, 78.8, duration=1.0)
    with step("[Verify] Capture '00058_main_05_04a_07_Step33' for GT comparison"):
        actions.capture_for_gt('00058_main_05_04a_07_Step33', AppiumBy.ACCESSIBILITY_ID, 'zoomView', threshold=0.95)
    with step("[Action] Drag cpSlider (96.2%,59.5%) → slider (2.1%,61.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 96.2, 59.5, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.1, 61.0, duration=1.0)
    with step("[Action] Drag zoomView (91.4%,15.2%) → zoomView (18.4%,77.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'zoomView', 91.4, 15.2, AppiumBy.ACCESSIBILITY_ID, 'zoomView', 18.4, 77.9, duration=1.0)
    with step("[Verify] Capture '00058_main_05_04a_07_Step36' for GT comparison"):
        actions.capture_for_gt('00058_main_05_04a_07_Step36', AppiumBy.ACCESSIBILITY_ID, 'zoomView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (81.6%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 40.8)
    with step("[Action] Tap homeButton at (65.4%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 50.0)
    with step("[Action] Tap Discard at (49.3%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 49.3, 83.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
