import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00140_main_05_01_11_20260805_164855")
def test_00140_main_05_01_11_20260805_164855(actions: DriverActions):
    with step("[Action] Tap Edit at (42.9%, 76.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 42.9, 76.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (63.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 63.5, 50.0)
    with step("[Action] Tap _AT at (9.0%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.0, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (30.8%, 63.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 30.8, 63.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Enhance at (57.1%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 57.1, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_ai_color at (27.3%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_ai_color', 27.3, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '70'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '70')
    with step("[Action] Drag cpSlider (67.9%,54.0%) → backgroundView (26.0%,86.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 67.9, 54.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 26.0, 86.5, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00140_main_05_01_11_Step10' for GT comparison"):
        actions.capture_for_gt('00140_main_05_01_11_Step10', AppiumBy.ACCESSIBILITY_ID, 'gpuImageViewPlaceHolder', threshold=0.95)
    with step("[Action] Drag cpSlider (6.6%,52.0%) → backgroundView (87.4%,87.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.6, 52.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 87.4, 87.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00140_main_05_01_11_Step13' for GT comparison"):
        actions.capture_for_gt('00140_main_05_01_11_Step13', AppiumBy.ACCESSIBILITY_ID, 'gpuImageViewPlaceHolder', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (34.7%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 34.7, 34.7)
    with step("[Verify] Capture '00140_main_05_01_11_Step15' for GT comparison"):
        actions.capture_for_gt('00140_main_05_01_11_Step15', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_ai_color at (54.5%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_ai_color', 54.5, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_ok_n at (89.8%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 89.8, 46.9)
    with step("[Action] Tap btnClose at (71.0%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 71.0, 48.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (36.7%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 36.7, 53.1)
    with step("[Action] Tap homeButton at (61.5%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 76.9)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
