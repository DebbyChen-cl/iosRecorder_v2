import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00179_ai_try_on_04_20260807_142335")
def test_00179_ai_try_on_04_20260807_142335(actions: DriverActions):
    with step("[Action] Tap AI Photos at (63.9%, 86.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 63.9, 86.4)
    with step("[Action] Tap AI Try-On at (66.7%, 72.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', 66.7, 72.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap thumbnailImageView at (60.0%, 85.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'thumbnailImageView', 60.0, 85.6)
    with step("[Action] Tap importLabel at (59.3%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importLabel', 59.3, 80.0)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (14.0%, 91.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 14.0, 91.8)
    with step("[Action] Tap btnAlbum at (80.2%, 69.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 80.2, 69.0)
    with step("[Action] Tap _AT at (7.9%, 86.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 86.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-1 at (31.5%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 31.5, 53.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] We cannot find any faces. Try choosing another one. Thank you. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'We cannot find any faces. Try choosing another one. Thank you.')
    with step("[Action] Tap AlertDialog-btnPositive at (57.6%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 57.6, 30.6)
    with step("[Action] Tap photoCell-4 at (27.7%, 52.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4', 27.7, 52.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] More than one person detected. Try choosing another one. Thank you. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'More than one person detected. Try choosing another one. Thank you.')
    with step("[Action] Tap AlertDialog-btnPositive at (58.9%, 77.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 58.9, 77.6)
    with step("[Action] Tap btnBack at (52.5%, 48.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 52.5, 48.8)
    with step("[Action] Tap navBackButton at (32.5%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 32.5, 45.0)
    with step("[Action] Tap navBackButton at (34.6%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 34.6, 65.4)
    with step("[Action] Tap Home at (52.8%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Home', 52.8, 77.3)
    assert True
