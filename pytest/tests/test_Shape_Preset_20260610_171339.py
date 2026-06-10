import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("Shape_Preset_20260610_171339")
def test_Shape_Preset_20260610_171339(actions: DriverActions):
    with step("[Action] Tap Edit at (57.1%, 42.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 57.1, 42.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=320, container_h=539)
    with step("[Action] Tap btnAlbum at (61.9%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 61.9, 48.4)
    with step("[Action] Tap Sample Photos at (17.8%, 58.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 17.8, 58.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=294, container_h=557)
    with step("[Action] Tap PhDM_example_3 at (24.0%, 65.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_3', 24.0, 65.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=320, container_h=557)
    with step("[Action] Tap fit edge n at (70.4%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'fit edge n', 70.4, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=320, container_h=33)
    with step("[Action] Tap ic_beautify at (65.4%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 65.4, 64.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=320, container_h=72)
    with step("[Action] Tap ic_face_reshape_portrait at (72.0%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_reshape_portrait', 72.0, 56.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=320, container_h=72)
    with step("[Action] Tap ic_face_natural at (53.8%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_natural', 53.8, 80.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=320, container_h=72)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Verify] Capture 'Shape_Preset_Step10' for GT comparison"):
        actions.capture_for_gt('Shape_Preset_Step10', AppiumBy.XPATH, '//XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag cpSlider (51.2%,64.9%) → intensitySlider (3.3%,52.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 51.2, 64.9, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 3.3, 52.8, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture 'Shape_Preset_Step13' for GT comparison"):
        actions.capture_for_gt('Shape_Preset_Step13', AppiumBy.XPATH, '//XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag cpSlider (6.4%,54.1%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1] (80.3%,72.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.4, 54.1, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1]', 80.3, 72.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture 'Shape_Preset_Step16' for GT comparison"):
        actions.capture_for_gt('Shape_Preset_Step16', AppiumBy.XPATH, '//XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_face_oval at (46.2%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_oval', 46.2, 44.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=320, container_h=72)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Verify] Capture 'Shape_Preset_Step19' for GT comparison"):
        actions.capture_for_gt('Shape_Preset_Step19', AppiumBy.XPATH, '//XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag cpSlider (49.6%,54.1%) → intensitySlider (4.1%,55.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 49.6, 54.1, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.1, 55.6, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture 'Shape_Preset_Step22' for GT comparison"):
        actions.capture_for_gt('Shape_Preset_Step22', AppiumBy.XPATH, '//XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag cpSlider (5.2%,48.6%) → intensitySlider (97.6%,47.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.2, 48.6, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 97.6, 47.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture 'Shape_Preset_Step25' for GT comparison"):
        actions.capture_for_gt('Shape_Preset_Step25', AppiumBy.XPATH, '//XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_face_vline at (69.2%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_vline', 69.2, 44.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=320, container_h=72)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Verify] Capture 'Shape_Preset_Step28' for GT comparison"):
        actions.capture_for_gt('Shape_Preset_Step28', AppiumBy.XPATH, '//XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag cpSlider (49.2%,45.9%) → intensitySlider (2.8%,55.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 49.2, 45.9, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 2.8, 55.6, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture 'Shape_Preset_Step31' for GT comparison"):
        actions.capture_for_gt('Shape_Preset_Step31', AppiumBy.XPATH, '//XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag cpSlider (7.2%,48.6%) → intensitySlider (97.6%,52.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.2, 48.6, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 97.6, 52.8, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture 'Shape_Preset_Step34' for GT comparison"):
        actions.capture_for_gt('Shape_Preset_Step34', AppiumBy.XPATH, '//XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_face_baby at (76.9%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_baby', 76.9, 64.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=320, container_h=72)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Verify] Capture 'Shape_Preset_Step37' for GT comparison"):
        actions.capture_for_gt('Shape_Preset_Step37', AppiumBy.XPATH, '//XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag cpSlider (51.2%,56.8%) → intensitySlider (0.8%,61.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 51.2, 56.8, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 0.8, 61.1, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture 'Shape_Preset_Step40' for GT comparison"):
        actions.capture_for_gt('Shape_Preset_Step40', AppiumBy.XPATH, '//XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag cpSlider (7.2%,51.4%) → intensitySlider (99.6%,55.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.2, 51.4, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 99.6, 55.6, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture 'Shape_Preset_Step43' for GT comparison"):
        actions.capture_for_gt('Shape_Preset_Step43', AppiumBy.XPATH, '//XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_face_original at (73.1%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_original', 73.1, 44.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=320, container_h=72)
    with step("[Verify] Capture 'Shape_Preset_Step45' for GT comparison"):
        actions.capture_for_gt('Shape_Preset_Step45', AppiumBy.XPATH, '//XCUIElementTypeOther', threshold=0.95)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
