import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00220_AIArt_CustomStyle_20260812_115158")
def test_00220_AIArt_CustomStyle_20260812_115158(actions: DriverActions):
    with step("[Action] Tap AI Photos at (61.1%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 61.1, 54.5)
    with step("[Action] Scroll until AI Art"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Art', direction='down', offset_start=(0.255, 0.276), offset_end=(0.255, 0.162), velocity=151)
    with step("[Action] Tap AI Art at (69.2%, 68.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Art', 69.2, 68.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap importButton at (49.5%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importButton', 49.5, 75.0)
    with step("[Action] Tap PhotoPickerRecommendDialog-notShowAgainCheckBox at (33.3%, 59.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox', 33.3, 59.3)
    with step("[Action] Tap Continue at (44.6%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 44.6, 56.5)
    with step("[Action] Tap btnAlbum at (79.2%, 78.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 79.2, 78.6)
    with step("[Action] Tap _AT at (7.2%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.2, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (50.8%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 50.8, 57.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Custom at (67.0%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Custom', 67.0, 75.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap placeholderLabel at (25.7%, 86.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 25.7, 86.1)
    with step("[Action] Type 'abacc' into placeholderLabel"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 'abacc')
    with step("[Verify] promptTextView text equals 'abacc'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 'abacc')
    with step("[Action] Tap clearButton at (66.7%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'clearButton', 66.7, 66.7)
    with step("[Verify] placeholderLabel text equals 'Please provide a description of the anime's appearance or characteristics.'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 'Please provide a description of the anime\'s appearance or characteristics.')
    with step("[Action] Tap placeholderLabel at (17.5%, 63.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 17.5, 63.9)
    with step("[Action] Type 'Initial D's style' into placeholderLabel"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 'Initial D\'s style')
    with step("[Action] Tap Apply at (76.5%, 87.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Apply', 76.5, 87.5)
    with step("[Action] Tap btnGenerate at (20.4%, 74.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 20.4, 74.2)
    with step("[Verify] waitLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'waitLabel', appear_timeout=5, disappear_timeout=1200), 'waitLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (34.6%, 19.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 34.6, 19.2)
    with step("[Action] Tap Prompt at (50.0%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Prompt', 50.0, 55.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Verify] promptTextView text equals 'Initial D's style'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 'Initial D\'s style')
    with step("[Action] Tap clearButton at (83.3%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'clearButton', 83.3, 61.1)
    with step("[Action] Tap placeholderLabel at (20.2%, 72.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 20.2, 72.2)
    with step("[Action] Type 'American comic's style' into placeholderLabel"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 'American comic\'s style')
    with step("[Action] Tap Save Changes at (76.4%, 81.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Save Changes', 76.4, 81.0)
    with step("[Action] Tap btnGenerate at (19.6%, 53.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 19.6, 53.2)
    with step("[Verify] In progress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'In progress', appear_timeout=5, disappear_timeout=1200), 'In progress did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnHome at (84.6%, 88.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 84.6, 88.5)
    assert True
