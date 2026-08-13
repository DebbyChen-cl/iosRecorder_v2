import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00211_reshape_shape_preset_20260811_172501")
def test_00211_reshape_shape_preset_20260811_172501(actions: DriverActions):
    with step("[Action] Tap Edit at (68.6%, 32.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 68.6, 32.0)
    with step("[Action] Tap btnAlbum at (92.4%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 92.4, 57.1)
    with step("[Action] Tap Sample Photos at (3.2%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 3.2, 56.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap PhDM_example_3 at (40.8%, 63.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_3', 40.8, 63.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (56.8%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 56.8, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap Beautify at (49.3%, 21.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Beautify', 49.3, 21.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Reshape at (68.5%, 21.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Reshape', 68.5, 21.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Natural at (73.0%, 26.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Natural', 73.0, 26.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (52.4%,50.0%) → intensitySlider (1.6%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 52.4, 50.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 1.6, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00211_reshape_shape_preset_Step12' for GT comparison"):
        actions.capture_for_gt('00211_reshape_shape_preset_Step12', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.4%,58.0%) → intensitySlider (100.0%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.4, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 100.0, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00211_reshape_shape_preset_Step15' for GT comparison"):
        actions.capture_for_gt('00211_reshape_shape_preset_Step15', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Oval at (64.9%, 26.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Oval', 64.9, 26.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (52.7%,48.0%) → intensitySlider (0.9%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 52.7, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 0.9, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00211_reshape_shape_preset_Step20' for GT comparison"):
        actions.capture_for_gt('00211_reshape_shape_preset_Step20', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.8%,48.0%) → intensitySlider (99.7%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.8, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 99.7, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00211_reshape_shape_preset_Step23' for GT comparison"):
        actions.capture_for_gt('00211_reshape_shape_preset_Step23', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_face_vline at (73.5%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_vline', 73.5, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (51.8%,48.0%) → intensitySlider (0.6%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 51.8, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 0.6, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00211_reshape_shape_preset_Step28' for GT comparison"):
        actions.capture_for_gt('00211_reshape_shape_preset_Step28', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.0%,52.0%) → intensitySlider (98.5%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.0, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.5, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00211_reshape_shape_preset_Step31' for GT comparison"):
        actions.capture_for_gt('00211_reshape_shape_preset_Step31', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_face_baby at (64.7%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_baby', 64.7, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (51.2%,54.0%) → intensitySlider (1.2%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 51.2, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 1.2, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00211_reshape_shape_preset_Step36' for GT comparison"):
        actions.capture_for_gt('00211_reshape_shape_preset_Step36', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.0%,56.0%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1] (79.8%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.0, 56.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1]', 79.8, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00211_reshape_shape_preset_Step39' for GT comparison"):
        actions.capture_for_gt('00211_reshape_shape_preset_Step39', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_face_original at (52.9%, 87.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_original', 52.9, 87.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00211_reshape_shape_preset_Step41' for GT comparison"):
        actions.capture_for_gt('00211_reshape_shape_preset_Step41', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (42.9%, 63.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 42.9, 63.3)
    with step("[Action] Tap btn_cancel_n at (42.9%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 42.9, 32.7)
    with step("[Action] Tap homeButton at (65.4%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 53.8)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
