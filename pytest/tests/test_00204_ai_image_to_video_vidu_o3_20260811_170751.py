import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00204_ai_image_to_video_vidu_o3_20260811_170751")
def test_00204_ai_image_to_video_vidu_o3_20260811_170751(actions: DriverActions):
    with step("[Action] Tap Image to Video at (60.4%, 48.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Image to Video', 60.4, 48.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Action] Tap Try now at (75.7%, 82.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try now', 75.7, 82.6)
    with step("[Action] Tap Continue at (22.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 22.5, 50.0)
    with step("[Action] Tap Custom at (63.6%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Custom', 63.6, 30.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=110)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"ImageToVideoCustomModelDetailViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton at (58.1%, 55.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="ImageToVideoCustomModelDetailViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton', 58.1, 55.4)
    with step("[Action] Tap Vidu Q3 at (66.7%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Vidu Q3', 66.7, 61.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="ImageToVideoCustomModelDetailViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView', container_w=394, container_h=606)
    with step("[Action] Tap 4 at (55.6%, 87.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '4', 55.6, 87.5)
    with step("[Action] Tap button_8 at (34.0%, 72.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_8', 34.0, 72.2)
    with step("[Action] Tap 16 at (86.7%, 56.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '16', 86.7, 56.2)
    with step("[Action] Tap 4 at (100.0%, 56.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '4', 100.0, 56.2)
    with step("[Action] Tap Pro at (50.0%, 68.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro', 50.0, 68.8)
    with step("[Action] Tap Standard at (57.1%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Standard', 57.1, 75.0)
    with step("[Action] Tap Off at (70.0%, 58.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Off', 70.0, 58.8)
    with step("[Action] Tap On at (44.4%, 100.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'On', 44.4, 100.0)
    with step("[Action] Tap promptTextView at (17.5%, 27.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 17.5, 27.0)
    with step("[Action] Type 'The train drive through' into promptTextView"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 'The train drive through')
    with step("[Action] Tap Next: at (56.1%, 37.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 56.1, 37.5)
    with step("[Action] Tap btn_ok_n at (81.6%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 30.6)
    with step("[Action] Tap imageIconView at (80.0%, 61.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageIconView', 80.0, 61.0)
    with step("[Action] Tap btnAlbum at (92.4%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 92.4, 54.8)
    with step("[Action] Tap Sample Photos at (26.5%, 39.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 26.5, 39.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap PhDM_example_8 at (40.8%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_8', 40.8, 57.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Generate at (50.6%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 50.6, 50.0)
    with step("[Verify] processingLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'processingLabel', appear_timeout=5, disappear_timeout=1200), 'processingLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (45.2%, 71.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 45.2, 71.0)
    with step("[Action] Tap navBackButton at (37.5%, 65.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 37.5, 65.9)
    assert True
