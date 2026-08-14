import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00200_ai_image_to_video_happy_horse_20260811_170440")
def test_00200_ai_image_to_video_happy_horse_20260811_170440(actions: DriverActions):
    with step("[Action] Tap Image to Video at (44.8%, 37.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Image to Video', 44.8, 37.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Action] Tap Try now at (30.0%, 26.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try now', 30.0, 26.1)
    with step("[Action] Tap Continue at (88.8%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 88.8, 50.0)
    with step("[Action] Tap imageIconView at (77.5%, 73.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageIconView', 77.5, 73.2)
    with step("[Action] Tap optional Continue if the recommendation dialog is shown"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Continue', timeout=3):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 66.2, 43.5)
    with step("[Action] Tap btnAlbum at (88.8%, 59.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 88.8, 59.5)
    with step("[Action] Scroll until Sample Photos"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'albumCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', direction='up', offset_start=(0.31, 0.257), offset_end=(0.31, 0.725), velocity=724)
    with step("[Action] Tap Sample Photos at (34.1%, 73.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 34.1, 73.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap PhDM_example_8 at (40.0%, 32.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_8', 40.0, 32.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Custom at (43.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Custom', 43.2, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=110)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"ImageToVideoCustomModelDetailViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton at (92.9%, 64.3%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="ImageToVideoCustomModelDetailViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton', 92.9, 64.3)
    with step("[Action] Tap Happy Horse 1.1 at (61.9%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Happy Horse 1.1', 61.9, 52.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="ImageToVideoCustomModelDetailViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView', container_w=394, container_h=606)
    with step("[Action] Tap 10 at (93.3%, 87.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '10', 93.3, 87.5)
    with step("[Action] Tap 15 at (64.3%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '15', 64.3, 62.5)
    with step("[Action] Tap 5 at (0.0%, 81.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '5', 0.0, 81.2)
    with step("[Action] Tap button_Pro at (72.5%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_Pro', 72.5, 41.7)
    with step("[Action] Tap Standard at (48.2%, 81.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Standard', 48.2, 81.2)
    with step("[Action] Tap promptTextView at (35.3%, 32.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 35.3, 32.6)
    with step("[Action] Type 'The train drive through' into promptTextView"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 'The train drive through')
    with step("[Action] Tap Next: at (40.2%, 44.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 40.2, 44.6)
    with step("[Action] Tap btn_ok_n at (75.5%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 38.8)
    with step("[Action] Tap Generate at (42.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 42.5, 50.0)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Verify] processingLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'processingLabel', appear_timeout=5, disappear_timeout=1200), 'processingLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (48.4%, 16.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 48.4, 16.1)
    with step("[Action] Tap navBackButton at (40.0%, 63.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 40.0, 63.4)
    assert True
