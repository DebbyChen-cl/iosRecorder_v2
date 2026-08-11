import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00181_1_ai_try_on_06_20260807_143101")
def test_00181_1_ai_try_on_06_20260807_143101(actions: DriverActions):
    with step("[Action] Tap Edit at (51.4%, 28.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 51.4, 28.0)
    with step("[Action] Tap btnAlbum at (69.5%, 26.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 69.5, 26.2)
    with step("[Action] Tap Try-On at (14.0%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try-On', 14.0, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-1 at (36.2%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 36.2, 46.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (40.5%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 40.5, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until AI Try-On"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', direction='left', offset_start=(0.77, 0.433), offset_end=(0.156, 0.433), velocity=349)
    with step("[Action] Tap AI Try-On at (38.0%, 21.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', 38.0, 21.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Try now at (21.4%, 26.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try now', 21.4, 26.1)
    with step("[Action] Tap Obsidian Siren at (53.4%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Obsidian Siren', 53.4, 45.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Action] Tap Generate at (86.4%, 20.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 86.4, 20.8)
    with step("[Verify] No face detected. A face is required for this style. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'No face detected. A face is required for this style.')
    with step("[Action] Tap AlertDialog-btnPositive at (60.4%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 60.4, 64.0)
    with step("[Action] Tap Pet & Doll at (86.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pet & Doll', 86.5, 50.0)
    with step("[Action] Tap Soft Towel at (85.2%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Soft Towel', 85.2, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=362)
    with step("[Action] Tap btnGenerate at (56.3%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 56.3, 54.8)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (61.3%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 61.3, 64.5)
    with step("[Action] Tap Custom at (80.7%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Custom', 80.7, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=362)
    with step("[Action] Tap titleLabel at (38.5%, 13.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'titleLabel', 38.5, 13.6)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (71.2%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 71.2, 30.6)
    with step("[Action] Tap photoCell-0 at (48.5%, 47.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 48.5, 47.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap Next at (61.8%, 68.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next', 61.8, 68.4)
    with step("[Action] Tap Generate at (50.6%, 54.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 50.6, 54.2)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (45.2%, 45.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 45.2, 45.2)
    with step("[Verify] Photo is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Photo')
    with step("[Action] Tap clearButton at (88.9%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'clearButton', 88.9, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=362)
    with step("[Verify] Photo is not visible"):
        actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Photo')
    with step("[Action] Tap Custom at (33.0%, 35.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Custom', 33.0, 35.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=362)
    with step("[Verify] containerView is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'containerView')
    with step("[Action] Tap titleLabel at (10.3%, 22.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'titleLabel', 10.3, 22.7)
    with step("[Action] Tap placeholderLabel at (8.9%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 8.9, 46.9)
    with step("[Action] Type 'raincoat' into placeholderLabel"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 'raincoat')
    with step("[Action] Tap promptApplyButton at (62.4%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptApplyButton', 62.4, 36.7)
    with step("[Action] Tap Generate at (39.5%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 39.5, 70.8)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (71.0%, 71.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 71.0, 71.0)
    with step("[Action] Tap navBackButton at (42.5%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 42.5, 75.0)
    with step("[Action] Tap navBackButton at (65.4%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 65.4, 76.9)
    with step("[Action] Tap homeButton at (69.2%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 69.2, 53.8)
    assert True
