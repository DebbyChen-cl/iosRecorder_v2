import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00178_ai_try_on_03_20260807_142149")
def test_00178_ai_try_on_03_20260807_142149(actions: DriverActions):
    with step("[Action] Tap AI Photos at (69.4%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 69.4, 72.7)
    with step("[Action] Tap AI Try-On at (80.3%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', 80.3, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap thumbnailImageView at (70.7%, 86.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'thumbnailImageView', 70.7, 86.6)
    with step("[Action] Tap importLabel at (1.9%, 82.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importLabel', 1.9, 82.5)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (16.4%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 16.4, 28.6)
    with step("[Action] Tap btnAlbum at (69.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 69.0, 50.0)
    with step("[Action] Tap _AT at (9.7%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.7, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (42.3%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 42.3, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Custom at (51.1%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Custom', 51.1, 30.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Action] Tap titleLabel at (31.9%, 40.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'titleLabel', 31.9, 40.9)
    with step("[Action] Tap placeholderLabel at (18.6%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 18.6, 75.0)
    with step("[Action] Type 'Uniform of 7-11' into placeholderLabel"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 'Uniform of 7-11')
    with step("[Action] Tap promptApplyButton at (31.2%, 75.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptApplyButton', 31.2, 75.5)
    with step("[Action] Tap btnGenerate at (29.1%, 45.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 29.1, 45.2)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (61.3%, 41.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 61.3, 41.9)
    with step("[Action] Tap Prompt at (54.5%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Prompt', 54.5, 70.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Verify] promptField text equals 'Uniform Uniform of 7-11'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'promptField', 'Uniform Uniform of 7-11')
    with step("[Action] Tap clearButton at (77.8%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'clearButton', 77.8, 44.4)
    with step("[Verify] promptField text equals 'promptField'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'promptField', 'promptField')
    with step("[Action] Type 'Uniform of Famimart' into clearButton"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'clearButton', 'Uniform of Famimart')
    with step("[Action] Tap Apply at (66.7%, 47.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Apply', 66.7, 47.8)
    with step("[Action] Tap Generate at (43.2%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 43.2, 83.3)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (67.7%, 71.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 67.7, 71.0)
    with step("[Action] Tap navBackButton at (52.5%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 52.5, 47.5)
    with step("[Action] Tap navBackButton at (76.9%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 76.9, 42.3)
    with step("[Action] Tap btnHome at (56.6%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 56.6, 45.5)
    assert True
