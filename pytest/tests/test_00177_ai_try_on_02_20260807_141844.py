import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00177_ai_try_on_02_20260807_141844")
def test_00177_ai_try_on_02_20260807_141844(actions: DriverActions):
    with step("[Action] Tap AI Photos at (61.1%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 61.1, 72.7)
    with step("[Action] Scroll until AI Try-On"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', direction='down', offset_start=(0.72, 0.376), offset_end=(0.72, 0.338), velocity=50)
    with step("[Action] Tap AI Try-On at (12.1%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', 12.1, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap Try now at (75.7%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try now', 75.7, 52.2)
    with step("[Action] Tap importButton at (44.4%, 53.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importButton', 44.4, 53.4)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (21.2%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 21.2, 59.2)
    with step("[Action] Tap btnAlbum at (70.1%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 70.1, 57.1)
    with step("[Action] Tap _AT at (9.7%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.7, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (37.7%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 37.7, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Custom at (52.3%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Custom', 52.3, 70.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Action] Tap iconImageView at (80.0%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'iconImageView', 80.0, 60.0)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (34.9%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 34.9, 28.6)
    with step("[Action] Tap ic info n at (40.0%, 43.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic info n', 40.0, 43.9)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (23.8%, 61.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 23.8, 61.2)
    with step("[Action] Tap photoCell-3 at (58.5%, 44.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3', 58.5, 44.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap Next at (8.8%, 42.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next', 8.8, 42.1)
    with step("[Action] Tap Generate at (32.1%, 37.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 32.1, 37.5)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (48.4%, 32.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 48.4, 32.3)
    with step("[Action] Tap navBackButton at (40.0%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 40.0, 62.5)
    with step("[Action] Tap navBackButton at (69.2%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 69.2, 57.7)
    with step("[Action] Tap btnHome at (67.1%, 52.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 67.1, 52.7)
    assert True
