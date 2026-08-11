import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00065_main_05_07_03_2_20260805_094552")
def test_00065_main_05_07_03_2_20260805_094552(actions: DriverActions):
    with step("[Action] Tap Edit at (60.0%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 60.0, 56.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (83.2%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 83.2, 42.9)
    with step("[Action] Tap _AT at (7.2%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.2, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-1 at (39.2%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 39.2, 58.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (33.8%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 33.8, 51.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (54.5%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 54.5, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_skin_smooth at (42.4%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_skin_smooth', 42.4, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Auto at (78.4%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Auto', 78.4, 56.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=110, container_h=46)
    with step("[Verify] No faces were detected. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'No faces were detected.')
    with step("[Action] Tap Add Face at (72.5%, 87.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Add Face', 72.5, 87.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SkinSmoothProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=680)
    with step("[Action] Tap tipsButton at (37.5%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'tipsButton', 37.5, 57.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=790)
    with step("[Verify] instructionLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'instructionLabel')
    with step("[Action] Tap topArea at (7.0%, 54.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'topArea', 7.0, 54.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeScrollView', container_w=430, container_h=790)
    with step("[Action] Tap //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeImage at (38.6%, 43.0%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeImage', 38.6, 43.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=790)
    with step("[Action] Tap btn_ok_n at (91.8%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 91.8, 51.0)
    with step("[Action] Tap btn_ok_n at (93.9%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 93.9, 42.9)
    with step("[Action] Tap Auto at (59.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Auto', 59.5, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=110, container_h=46)
    with step("[Action] Drag intensityCPSlider (50.1%,50.8%) → controlArea (84.7%,56.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'intensityCPSlider', 50.1, 50.8, AppiumBy.ACCESSIBILITY_ID, 'controlArea', 84.7, 56.2, duration=1.0)
    with step("[Verify] Capture '00065_main_05_07_03_2_Step19' for GT comparison"):
        actions.capture_for_gt('00065_main_05_07_03_2_Step19', AppiumBy.ACCESSIBILITY_ID, 'middleArea', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (32.7%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 32.7, 36.7)
    with step("[Verify] Capture '00065_main_05_07_03_2_Step21' for GT comparison"):
        actions.capture_for_gt('00065_main_05_07_03_2_Step21', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_skin_smooth at (54.5%, 78.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_skin_smooth', 54.5, 78.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Auto at (54.1%, 43.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Auto', 54.1, 43.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=110, container_h=46)
    with step("[Action] Tap btn_add_face_n at (42.9%, 62.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_add_face_n', 42.9, 62.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='faceSelectionMenuPanelVisualStyleCollectionView', container_w=430, container_h=57)
    with step("[Action] Tap //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeImage at (49.8%, 15.3%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeImage', 49.8, 15.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=790)
    with step("[Action] Tap btn_ok_n at (69.4%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 69.4, 55.1)
    with step("[Action] Tap btn_ok_n at (83.7%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 83.7, 44.9)
    with step("[Action] Drag intensityCPSlider (49.9%,55.4%) → controlArea (82.6%,54.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'intensityCPSlider', 49.9, 55.4, AppiumBy.ACCESSIBILITY_ID, 'controlArea', 82.6, 54.7, duration=1.0)
    with step("[Action] Tap btn_ok_n at (69.4%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 69.4, 46.9)
    with step("[Action] Tap btn_ok_n at (61.2%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 61.2, 38.8)
    with step("[Action] Tap homeButton at (53.8%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 53.8, 73.1)
    with step("[Action] Tap Discard at (50.7%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 50.7, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
