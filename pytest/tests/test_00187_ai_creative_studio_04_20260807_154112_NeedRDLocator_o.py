import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00187_ai_creative_studio_04_20260807_154112")
def test_00187_ai_creative_studio_04_20260807_154112(actions: DriverActions):
    with step("[Action] Tap AI Creative Studio at (70.8%, 40.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', 70.8, 40.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Action] Tap NonScrollableMenuView-0 at (65.2%, 78.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'NonScrollableMenuView-0', 65.2, 78.3)
    with step("[Action] Tap My Prompts at (74.1%, 84.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Prompts', 74.1, 84.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=665)
    with step("[Verify] lblEmpty is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblEmpty')
    with step("[Action] Tap btnBack at (54.8%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 54.8, 51.6)
    with step("[Action] Tap promptInputView at (29.9%, 30.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptInputView', 29.9, 30.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=665)
    with step("[Action] Type 'A cat wearing sunglasses on a beach' into promptInputView"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptInputView', 'A cat wearing sunglasses on a beach')
    with step("[Action] Tap Next: at (56.1%, 53.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 56.1, 53.6)
    with step("[Verify] Capture '00187_ai_creative_studio_04_Step09' for GT comparison"):
        actions.capture_for_gt('00187_ai_creative_studio_04_Step09', AppiumBy.ACCESSIBILITY_ID, 'generateButton', threshold=0.95)
    with step("[Action] Tap clearButton at (72.7%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'clearButton', 72.7, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=665)
    with step("[Verify] promptInputView text equals 'Describe your idea and we will bring it to life.'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'promptInputView', 'Describe your idea and we will bring it to life.')
    with step("[Action] Tap referenceAddIcon at (40.0%, 48.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'referenceAddIcon', 40.0, 48.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=665)
    with step("[Action] Tap btnAlbum at (74.1%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 74.1, 54.8)
    with step("[Action] Tap _AT at (7.5%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.5, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=632)
    with step("[Action] Tap photoCell-2 at (29.2%, 71.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 29.2, 71.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap btnNext at (20.0%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 20.0, 61.1)
    with step("[Verify] Capture '00187_ai_creative_studio_04_Step17' for GT comparison"):
        actions.capture_for_gt('00187_ai_creative_studio_04_Step17', AppiumBy.ACCESSIBILITY_ID, 'generateButton', threshold=0.95)
    with step("[Action] Tap promptInputView at (32.2%, 23.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptInputView', 32.2, 23.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=665)
    with step("[Action] Type 'A cat wearing sunglasses on a beach' into promptInputView"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptInputView', 'A cat wearing sunglasses on a beach')
    with step("[Action] Tap Next: at (47.7%, 64.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 47.7, 64.3)
    with step("[Verify] Capture '00187_ai_creative_studio_04_Step21' for GT comparison"):
        actions.capture_for_gt('00187_ai_creative_studio_04_Step21', AppiumBy.ACCESSIBILITY_ID, 'generateButton', threshold=0.95)
    with step("[Action] Tap chevronView at (86.4%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevronView', 86.4, 56.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=665)
    with step("[Action] Tap Next-gen image generation with sharp text, pixel accuracy, and photorealistic detail at (76.5%, 40.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next-gen image generation with sharp text, pixel accuracy, and photorealistic detail', 76.5, 40.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeTable', container_w=394, container_h=177)
    with step("[Action] Tap generateButton at (18.8%, 67.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'generateButton', 18.8, 67.9)
    with step("[Verify] AI Creative Studio is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (38.7%, 38.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 38.7, 38.7)
    with step("[Action] Tap chevronView at (31.8%, 65.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevronView', 31.8, 65.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=665)
    with step("[Action] Tap Advanced generation with precise prompt control and strong text creation ability at (26.5%, 59.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Advanced generation with precise prompt control and strong text creation ability', 26.5, 59.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeTable', container_w=394, container_h=177)
    with step("[Action] Tap generateButton at (24.6%, 49.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'generateButton', 24.6, 49.1)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (58.1%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 58.1, 64.5)
    with step("[Action] Tap clearButton at (63.6%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'clearButton', 63.6, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=665)
    with step("[Verify] promptInputView text equals 'Describe your idea and we will bring it to life.'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'promptInputView', 'Describe your idea and we will bring it to life.')
    with step("[Action] Tap My Prompts at (40.0%, 52.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Prompts', 40.0, 52.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=665)
    with step("[Verify] titleLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'titleLabel')
    with step("[Action] Tap Reuse at (70.5%, 89.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Reuse', 70.5, 89.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='listCollectionView', container_w=394, container_h=806)
    with step("[Verify] promptInputView text equals 'A cat wearing sunglasses on a beach'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'promptInputView', 'A cat wearing sunglasses on a beach')
    with step("[Action] Tap My Prompts at (43.5%, 73.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Prompts', 43.5, 73.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=665)
    with step("[Action] Tap Select at (62.5%, 57.1%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeButton[@name="btnAction"]', 62.5, 57.1)
    with step("[Action] Tap containerView at (51.0%, 82.2%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="AICreativeStudioPromptCell-0"]', 51.0, 82.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='listCollectionView', container_w=394, container_h=806)
    with step("[Action] Tap containerView at (56.3%, 78.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="AICreativeStudioPromptCell-1"]', 56.3, 78.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='listCollectionView', container_w=394, container_h=806)
    with step("[Action] Tap Delete at (51.9%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Delete', 51.9, 81.8)
    with step("[Verify] lblEmpty is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblEmpty')
    with step("[Action] Tap btnBack at (87.1%, 58.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 87.1, 58.1)
    with step("[Action] Tap aiCreativeStudioRouter_backButton at (34.6%, 51.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton', 34.6, 51.9)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
