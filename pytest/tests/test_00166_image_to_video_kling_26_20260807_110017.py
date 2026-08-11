import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00166_image_to_video_kling_26_20260807_110017")
def test_00166_image_to_video_kling_26_20260807_110017(actions: DriverActions):
    with step("[Action] Tap Image to Video at (61.5%, 29.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Image to Video', 61.5, 29.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Action] Tap btnNext at (72.7%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 72.7, 34.7)
    with step("[Action] Tap btnNext at (79.9%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 79.9, 60.0)
    with step("[Action] Tap itv_example_single at (64.5%, 47.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'itv_example_single', 64.5, 47.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="singleScrollView"]/XCUIElementTypeScrollView', container_w=394, container_h=430)
    with step("[Action] Tap btnAlbum at (82.7%, 78.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 82.7, 78.6)
    with step("[Action] Tap Sample Photos at (32.6%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 32.6, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step('[Action] Tap photoCell-5'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step("[Action] Tap Custom at (43.2%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Custom', 43.2, 30.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=110)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"ImageToVideoCustomModelDetailViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton at (87.8%, 32.1%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="ImageToVideoCustomModelDetailViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton', 87.8, 32.1)
    with step("[Action] Tap Kling 2.6 at (34.8%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Kling 2.6', 34.8, 42.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="ImageToVideoCustomModelDetailViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView', container_w=394, container_h=606)
    with step("[Verify] Capture '00166_image_to_video_kling_26_Step11' for GT comparison"):
        actions.capture_for_gt('00166_image_to_video_kling_26_Step11', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="ImageToVideoCustomModelDetailViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton', threshold=0.95)
    with step("[Action] Tap button_10 at (86.0%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_10', 86.0, 61.1)
    with step("[Action] Tap button_5 at (82.0%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_5', 82.0, 69.4)
    with step("[Action] Tap button_Pro at (24.0%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_Pro', 24.0, 44.4)
    with step("[Action] Tap button_Off at (18.0%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_Off', 18.0, 71.4)
    with step("[Action] Tap button_On at (80.0%, 48.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_On', 80.0, 48.6)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"ImageToVideoCustomModelDetailViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[5]/XCUIElementTypeButton[1] at (58.6%, 56.7%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="ImageToVideoCustomModelDetailViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[5]/XCUIElementTypeButton[1]', 58.6, 56.7)
    with step("[Verify] Generate audio from video and prompt, supporting dialogue, sound effects, and music​. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Generate audio from video and prompt, supporting dialogue, sound effects, and music​.')
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"ImageToVideoCustomModelDetailViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3] at (72.1%, 74.2%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="ImageToVideoCustomModelDetailViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]', 72.1, 74.2)
    with step("[Action] Tap promptTextView at (17.3%, 19.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 17.3, 19.9)
    with step("[Action] Type 'The train drive through' into promptTextView"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 'The train drive through')
    with step("[Action] Tap Next: at (44.9%, 46.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 44.9, 46.4)
    with step("[Action] Tap btn_ok_n at (79.6%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 79.6, 28.6)
    with step("[Action] Tap creditGenerateButton at (17.0%, 33.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'creditGenerateButton', 17.0, 33.9)
    with step("[Verify] processingLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'processingLabel', appear_timeout=5, disappear_timeout=1200), 'processingLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (41.9%, 87.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 41.9, 87.1)
    with step("[Action] Tap navBackButton at (50.0%, 75.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 50.0, 75.6)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True


