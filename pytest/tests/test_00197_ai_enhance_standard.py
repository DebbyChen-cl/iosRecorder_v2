import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("ai_enhance_standard")
def test_ai_enhance_standard(actions: DriverActions):
    with step("[Action] Launch PhotoDirector"):
        actions.launch_app('com.cyberlink.photodirector')
    with step("[Action] Tap 'Edit'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Launcher_main_edit', 51.9, 52.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=320, container_h=623)
    with step("[Action] Expand album list"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 50.0, 50.0)
    with step("[Action] Select 'Sample Photos'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 50.0, 52.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=294, container_h=557)
    with step("[Action] Select a photo"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_1', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=320, container_h=557)
    with step("[Verify] Capture the original edit-room preview"):
        assert actions.capture_for_preview('ai_enhance_cancel_original', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap 'Enhance' tab"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 50.0, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=320, container_h=33)
    with step("[Action] Tap 'AI Enhance'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_AIenhance_110', 50.0, 52.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=320, container_h=72)
    with step("[Verify] Intro dialog pops up"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AI Enhance')
    with step("[Action] Tap 'x' on the intro dialog"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n', 50.0, 52.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='middleScrollView', container_w=320, container_h=476)
    with step("[Action] Tap 'Enhance'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 50.0, 50.0)
    with step("[Action] Wait for enhancement to finish"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'resultImageView', timeout=120)
    with step("[Action/Verify] Press Compare and show the original image in preview"):
        assert actions.capture_for_preview('ai_enhance_compare_original', 'before', AppiumBy.ACCESSIBILITY_ID, 'resultImageView')
        assert actions.long_press_capture_for_preview_within_element(
            AppiumBy.ACCESSIBILITY_ID,
            'compareButton',
            50.0,
            50.0,
            duration=1.0,
            capture_name='ai_enhance_compare_original',
            capture_by=AppiumBy.ACCESSIBILITY_ID,
            capture_value='resultImageView',
            expected_result='different',
            threshold=0.95,
            container_by=AppiumBy.ACCESSIBILITY_ID,
            container_value='middleScrollView',
            container_w=320,
            container_h=476,
        )
    with step("[Action] Tap 'x'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 50.0, 50.0)
    with step("[Verify] Back in edit room with the original image in preview"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
        assert actions.capture_for_preview('ai_enhance_cancel_original', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='same', threshold=0.95)
    with step("[Verify] Preview comparisons pass"):
        assert actions.run_screenshot_comparisons() is not False
