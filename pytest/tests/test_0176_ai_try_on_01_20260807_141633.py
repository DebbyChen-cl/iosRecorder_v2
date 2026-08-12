import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00176_ai_try_on_01_20260807_141633")
def test_00176_ai_try_on_01_20260807_141633(actions: DriverActions):
    with step("[Action] Tap Edit at (25.7%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 25.7, 56.0)
    with step("[Action] Tap btnAlbum at (72.6%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 72.6, 52.4)
    with step("[Action] Tap _AT at (9.0%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.0, 56.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (29.2%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 29.2, 46.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (74.3%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 74.3, 40.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until ic_aiTryOn"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_aiTryOn', direction='left', offset_start=(0.719, 0.443), offset_end=(0.221, 0.443), velocity=450)
    with step("[Action] Tap ic_aiTryOn at (55.9%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_aiTryOn', 55.9, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Action] Tap Try now at (64.3%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try now', 64.3, 52.2)
    with step("[Verify] Capture '0176_ai_try_on_01_Step09' for GT comparison"):
        actions.capture_for_gt('0176_ai_try_on_01_Step09', AppiumBy.ACCESSIBILITY_ID, 'importButton', threshold=0.95)
    with step("[Action] Scroll until Beige"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="stylePageView"]/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'Beige', direction='down', offset_start=(0.395, 0.582), offset_end=(0.395, 0.217), velocity=78)
    with step("[Action] Tap Beige at (64.8%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Beige', 64.8, 52.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Action] Tap btnGenerate at (21.2%, 66.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 21.2, 66.1)
    with step("[Verify] statusLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'statusLabel')
    with step("[Action] Tap btnBack at (51.6%, 83.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 51.6, 83.9)
    with step("[Action] Scroll until Ruby Breeze"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="stylePageView"]/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'Ruby Breeze', direction='down', offset_start=(0.537, 0.316), offset_end=(0.537, 0.13), velocity=50)
    with step("[Action] Tap Ruby Breeze at (77.3%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Ruby Breeze', 77.3, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Action] Tap Generate at (58.0%, 79.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 58.0, 79.2)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (61.3%, 45.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 61.3, 45.2)
    with step("[Action] Tap Male at (73.0%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Male', 73.0, 60.0)
    with step("[Action] Tap importButton at (46.7%, 53.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importButton', 46.7, 53.4)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (78.6%, 65.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 78.6, 65.3)
    with step("[Action] Tap ic info n at (50.0%, 43.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic info n', 50.0, 43.9)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (23.5%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 23.5, 46.9)
    with step("[Action] Tap photoCell-3 at (71.5%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3', 71.5, 53.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Scroll until Taupe"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="stylePageView"]/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'Taupe', direction='down', offset_start=(0.619, 0.644), offset_end=(0.619, 0.223), velocity=93)
    with step("[Action] Tap Taupe at (45.5%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Taupe', 45.5, 57.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Action] Tap btnGenerate at (28.6%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 28.6, 67.7)
    with step("[Verify] statusLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'statusLabel')
    with step("[Action] Tap btnBack at (25.8%, 74.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 25.8, 74.2)
    with step("[Action] Scroll until Green Ease"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="stylePageView"]/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'Green Ease', direction='up', offset_start=(0.433, 0.461), offset_end=(0.433, 0.604), velocity=50)
    with step("[Action] Tap Green Ease at (76.1%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Green Ease', 76.1, 42.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Action] Tap btnGenerate at (14.0%, 72.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 14.0, 72.6)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (41.9%, 45.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 41.9, 45.2)
    with step("[Action] Tap navBackButton at (45.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 45.0, 52.5)
    with step("[Action] Tap navBackButton at (57.7%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 57.7, 61.5)
    with step("[Action] Tap homeButton at (65.4%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 57.7)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
