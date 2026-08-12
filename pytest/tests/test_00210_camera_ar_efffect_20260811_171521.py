import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00210_camera_ar_efffect_20260811_171521")
def test_00210_camera_ar_efffect_20260811_171521(actions: DriverActions):
    with step("[Action] Tap Camera at (78.3%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Camera', 78.3, 48.0)
    with step("[Action] Tap featureTitleLabel at (50.6%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'featureTitleLabel', 50.6, 60.0)
    with step("[Action] Tap CMS-04_Cute_Kitty_01 at (62.1%, 46.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-04_Cute_Kitty_01', 62.1, 46.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='cameraAREffectPanelCollectionView', container_w=430, container_h=232)
    with step("[Action] Tap MAKEUP at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'MAKEUP', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=312, container_h=40)
    with step("[Verify] Unable to customize makeup when an effect is applied. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Unable to customize makeup when an effect is applied.')
    with step("[Action] Tap EFFECTS at (62.2%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'EFFECTS', 62.2, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=312, container_h=40)
    with step("[Action] Drag cpSlider (27.0%,64.3%) → slider (2.7%,68.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 27.0, 64.3, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.7, 68.3, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.CameraProViewController"]/XCUIElementTypeOther[4]')
    with step("[Action] Drag cpSlider (7.7%,64.3%) → slider (82.9%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.7, 64.3, AppiumBy.ACCESSIBILITY_ID, 'slider', 82.9, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.CameraProViewController"]/XCUIElementTypeOther[4]', expected_result='different', threshold=0.99)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.CameraProViewController"]/XCUIElementTypeOther[4]')
    with step("[Action] Tap btnReset at (19.2%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnReset', 19.2, 40.0)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.CameraProViewController"]/XCUIElementTypeOther[4]', expected_result='different', threshold=0.99)
    with step("[Action] Tap MAKEUP at (43.1%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'MAKEUP', 43.1, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=312, container_h=40)
    with step("[Verify] Looks is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Looks')
    with step("[Action] Tap EFFECTS at (51.4%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'EFFECTS', 51.4, 70.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=312, container_h=40)
    with step("[Action] Tap btnClose at (42.3%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 42.3, 57.5)
    with step("[Verify] Capture '00210_camera_ar_efffect_Step24' for GT comparison"):
        actions.capture_for_gt('00210_camera_ar_efffect_Step24', AppiumBy.ACCESSIBILITY_ID, 'btnEffects', threshold=0.95)
    with step("[Action] Tap btnHome at (67.5%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 67.5, 65.0)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
