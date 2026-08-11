import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00020_main_05_01_08')
def test_00020_main_05_01_08(actions: DriverActions):
    """denoise"""
    uuid = ['37d2aa7f-3d80-41a6-98c9-5c8f89e8642a', 'a7a7acda-a4e2-4422-ab6c-cb99b4a95f4b', 'e9af9d16-31e8-4ab5-b343-737dc81fad5d', '19ef176e-17b8-4705-89fb-c238c783b0a9', '1caf590c-8338-4059-9b91-321591e963a3', '36ae7406-acec-40d5-b168-a8fb2ae806c8', '3ea73ba1-9771-41c2-88d4-d8526fd8e1ed']

    with step("[Action] Tap Edit at (20.0%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 20.0, 64.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (79.2%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 79.2, 52.4)
    with step("[Action] Tap _AT at (6.8%, 22.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 6.8, 22.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (56.2%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 56.2, 76.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Enhance at (81.0%, 64.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 81.0, 64.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap icon_denoise at (69.7%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_denoise', 69.7, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn close outline n at (59.3%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n', 59.3, 48.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='middleScrollView', container_w=430, container_h=741)
    with step("[Action] Drag cpSlider (8.1%,46.0%) → backgroundView (84.0%,88.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 8.1, 46.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 84.0, 88.5, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture 'Denoise_Step12' for GT comparison"):
        actions.capture_for_gt('Denoise_Step12', AppiumBy.ACCESSIBILITY_ID, 'gpuImageViewPlaceHolder', threshold=0.95)
    with step("[Action] Drag cpSlider (92.6%,56.0%) → backgroundView (23.7%,88.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 92.6, 56.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 23.7, 88.6, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture 'Denoise_Step15' for GT comparison"):
        actions.capture_for_gt('Denoise_Step15', AppiumBy.ACCESSIBILITY_ID, 'gpuImageViewPlaceHolder', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (32.7%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 32.7, 53.1)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='same', threshold=0.95)
    with step("[Action] Tap icon_denoise at (76.5%, 84.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_denoise', 76.5, 84.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Try First at (62.9%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try First', 62.9, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='middleScrollView', container_w=430, container_h=741)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap btn_ok_n at (77.6%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 49.0)
    with step("[Verify] Continue is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnClose at (45.2%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 45.2, 51.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (18.4%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 18.4, 57.1)
    with step("[Action] Tap homeButton at (65.4%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 50.0)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    with step("[Verify] test_00020 completion"):
        assert True
