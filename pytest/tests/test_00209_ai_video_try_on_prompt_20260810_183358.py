import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00209_ai_video_try_on_prompt_20260810_183358")
def test_00209_ai_video_try_on_prompt_20260810_183358(actions: DriverActions):
    with step("[Action] Scroll until AI Video Try-On"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'AI Video Try-On', direction='left', offset_start=(0.965, 0.493), offset_end=(0.021, 0.493), velocity=617)
    with step("[Action] Tap AI Video Try-On at (39.6%, 48.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Video Try-On', 39.6, 48.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"aiVideoTryOn_importView\"]/XCUIElementTypeOther at (48.6%, 42.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="aiVideoTryOn_importView"]/XCUIElementTypeOther', 48.6, 42.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=719)
    with step("[Action] Tap Collections at (70.5%, 52.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collections', 70.5, 52.1)
    with step("[Action] Tap _Video at (29.2%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_Video', 29.2, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albums-shelf-scrollView', container_w=430, container_h=120)
    with step("[Action] Tap photos_layout at (17.4%, 55.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photos_layout', 17.4, 55.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photosView_content_scroll_view', container_w=430, container_h=863)
    with step("[Action] Tap Next at (72.5%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next', 72.5, 45.5)
    with step("[Action] Tap Describe by Prompts at (63.5%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Describe by Prompts', 63.5, 45.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=719)
    with step("[Verify] aiVideoTryOn_promptInput text equals 'Describe your dream outfit, e.g. ’a futuristic silver techwear jacket' or 'a vintage 90s floral sundress''"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'aiVideoTryOn_promptInput', 'Describe your dream outfit, e.g. ’a futuristic silver techwear jacket\' or \'a vintage 90s floral sundress\'')
    with step("[Action] Tap aiVideoTryOn_promptInput at (35.8%, 34.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiVideoTryOn_promptInput', 35.8, 34.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=719)
    with step("[Action] Type 'aaa' into aiVideoTryOn_promptInput"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiVideoTryOn_promptInput', 'aaa')
    with step("[Verify] aiVideoTryOn_promptInput text equals 'aaa'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'aiVideoTryOn_promptInput', 'aaa')
    with step("[Action] Tap clearButton at (68.2%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'clearButton', 68.2, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=719)
    with step("[Verify] aiVideoTryOn_promptInput text equals 'Describe your dream outfit, e.g. ’a futuristic silver techwear jacket' or 'a vintage 90s floral sundress''"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'aiVideoTryOn_promptInput', 'Describe your dream outfit, e.g. ’a futuristic silver techwear jacket\' or \'a vintage 90s floral sundress\'')
    with step("[Action] Tap aiVideoTryOn_promptInput at (18.5%, 19.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiVideoTryOn_promptInput', 18.5, 19.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=719)
    with step("[Action] Type '7-11 uniform' into aiVideoTryOn_promptInput"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiVideoTryOn_promptInput', '7-11 uniform')
    with step("[Action] Tap Next: at (57.0%, 53.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 57.0, 53.6)
    with step("[Action] Tap Generate at (66.7%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 66.7, 52.2)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Verify] processingLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'processingLabel', appear_timeout=5, disappear_timeout=1200), 'processingLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (64.5%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 64.5, 64.5)
    with step("[Action] Tap My Prompts at (90.6%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Prompts', 90.6, 83.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=719)
    with step("[Verify] titleLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'titleLabel')
    with step("[Action] Tap Reuse at (43.2%, 72.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Reuse', 43.2, 72.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='listCollectionView', container_w=394, container_h=806)
    with step("[Verify] aiVideoTryOn_promptInput text equals '7-11 uniform'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'aiVideoTryOn_promptInput', '7-11 uniform')
    with step("[Action] Tap aiVideoTryOn_backButton at (53.8%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiVideoTryOn_backButton', 53.8, 33.3)
    assert True
