import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00021_main_05_01_09')
def test_00021_main_05_01_09(actions: DriverActions):
    """deblur"""
    uuid = ['a8c4fb11-599f-4586-9ae4-1fa4b468d2a1', 'c7e78403-d4a9-46ac-9474-9831ca61b294', 'b16ecc8c-a1e9-4756-86ff-ae8423180013', 'eb53df65-ce3f-4fb3-8843-7a0b2858ce97', 'db53692c-821d-40be-9738-6f3bb06d3f4c', '36ae7406-acec-40d5-b168-a8fb2ae806c8', '3ea73ba1-9771-41c2-88d4-d8526fd8e1ed']
   
    with step("[Action] Tap Edit at (37.1%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 37.1, 44.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (91.4%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 91.4, 33.3)
    with step("[Action] Tap _AT at (8.2%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.2, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (60.0%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 60.0, 53.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Enhance at (47.6%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 47.6, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap icon_deblur at (36.4%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_deblur', 36.4, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Try First at (65.7%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try First', 65.7, 70.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='middleScrollView', container_w=430, container_h=741)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag cpSlider (91.5%,54.0%) → backgroundView (26.5%,88.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 91.5, 54.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 26.5, 88.6, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture 'Deblur_Step12' for GT comparison"):
        actions.capture_for_gt('Deblur_Step12', AppiumBy.ACCESSIBILITY_ID, 'gpuImageViewPlaceHolder', threshold=0.95)
    with step("[Action] Drag cpSlider (7.7%,54.0%) → backgroundView (85.6%,88.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.7, 54.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 85.6, 88.7, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture 'Deblur_Step15' for GT comparison"):
        actions.capture_for_gt('Deblur_Step15', AppiumBy.ACCESSIBILITY_ID, 'gpuImageViewPlaceHolder', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (18.4%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 18.4, 51.0)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='same', threshold=0.95)
    with step("[Action] Tap icon_deblur at (57.6%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_deblur', 57.6, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Try First at (72.9%, 45.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try First', 72.9, 45.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='middleScrollView', container_w=430, container_h=741)
    with step("[Action] Tap btn_ok_n at (85.7%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 85.7, 40.8)
    with step("[Verify] buyFlowLightButton is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step("[Action] Tap btnClose at (61.3%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 61.3, 54.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (32.7%, 24.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 32.7, 24.5)
    with step("[Action] Tap homeButton at (57.7%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 57.7, 73.1)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    with step("[Verify] test_00021 completion"):
        assert True
