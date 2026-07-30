import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("ai_enhance_advanced_pro_plus_user")
def test_ai_enhance_advanced_pro_plus_user(actions: DriverActions):
    with step("[Action] Launch PhotoDirector"):
        actions.launch_app("com.cyberlink.photodirector")
    if not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnSettings", timeout=3):
        with step("[Action] Recover launcher after an interrupted earlier run"):
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "Discard", timeout=1):
                actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Discard", 50.0, 50.0)
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnClose", timeout=1):
                actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnClose", 50.0, 50.0)
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btn_cancel_n", timeout=1):
                actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btn_cancel_n", 50.0, 50.0)
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "homeButton", timeout=1):
                actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "homeButton", 50.0, 50.0)
                if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "Discard", timeout=2):
                    actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Discard", 50.0, 50.0)
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "chevron.left", timeout=1):
                actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "chevron.left", 50.0, 50.0)
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "developerButton", timeout=1):
                actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
            if not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnSettings", timeout=1):
                actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
    with step("[Action] Tap 'Settings'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnSettings", 52.0, 50.0)
    with step("[Action] Tap 'About'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "About", 51.3, 52.9)
    with step("[Action] Tap five times to enter debug mode"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, "developerButton", 50.0, 51.4)
    with step("[Action] Set subscription mode to Pro+"):
        actions.tap_within_element(
            AppiumBy.XPATH,
            "(//XCUIElementTypeStaticText[@name='Debug Subscription Plan']/following::XCUIElementTypeButton)[1]",
            50.0,
            50.0,
        )
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Pro+", 50.0, 48.9)
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "Pro+")
    with step("[Action] Return to launcher"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "chevron.left", 50.0, 48.4)
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 47.6, 51.4)
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 47.6, 51.4)
    with step("[Action] Tap 'Edit'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Launcher_main_edit", 51.9, 52.0)
    with step("[Action] Expand album list"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnAlbum", 50.0, 50.0)
    with step("[Action] Select 'Sample Photos'"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID,
            "Sample Photos",
            50.0,
            52.9,
            container_by=AppiumBy.ACCESSIBILITY_ID,
            container_value="albumCollectionView",
            container_w=294,
            container_h=557,
        )
    with step("[Action] Select a photo"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID,
            "PhDM_example_1",
            50.0,
            50.0,
            container_by=AppiumBy.ACCESSIBILITY_ID,
            container_value="photoCollectionView",
            container_w=320,
            container_h=557,
        )
    with step("[Action] Tap 'Enhance' tab"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID,
            "Enhance",
            50.0,
            51.5,
            container_by=AppiumBy.ACCESSIBILITY_ID,
            container_value="ScrollableMenuView",
            container_w=320,
            container_h=33,
        )
    with step("[Action] Tap 'AI Enhance'"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID,
            "icon_AIenhance_110",
            50.0,
            52.0,
            container_by=AppiumBy.ACCESSIBILITY_ID,
            container_value="EditViewControllerBottomBarCollectionView",
            container_w=320,
            container_h=72,
        )
    with step("[Action] Tap 'x' on the intro dialog"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID,
            "btn close outline n",
            50.0,
            52.4,
            container_by=AppiumBy.ACCESSIBILITY_ID,
            container_value="middleScrollView",
            container_w=320,
            container_h=476,
        )
    with step("[Verify] Default highlight is on Advanced mode"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "aiEnhanceAdvancedModeButton")
        assert actions.verify_text(
            AppiumBy.ACCESSIBILITY_ID,
            "infoLabel",
            "Maximize detail and clarity with advanced AI.",
        ) is not False
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "-5")
    with step("[Action] Tap 'Enhance'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Enhance", 50.0, 50.0)
    with step("[Verify] Show processing UI"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "advancedWaitLabel")
        assert actions.verify_text(
            AppiumBy.ACCESSIBILITY_ID,
            "advancedWaitLabel",
            "Creating Your AI Image",
        ) is not False
    with step("[Action] Wait for process to finish"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "resultImageView", timeout=120)
    with step("[Verify] Enhanced image is displayed"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "Enhanced")
        assert actions.capture_for_preview(
            "ai_enhance_pro_plus_compare",
            "before",
            AppiumBy.ACCESSIBILITY_ID,
            "resultImageView",
        )
    with step("[Action/Verify] Press Compare to display the original image, then release"):
        assert actions.long_press_capture_for_preview_within_element(
            AppiumBy.ACCESSIBILITY_ID,
            "compareButton",
            50.0,
            50.0,
            duration=1.0,
            capture_name="ai_enhance_pro_plus_compare",
            capture_by=AppiumBy.ACCESSIBILITY_ID,
            capture_value="resultImageView",
            expected_result="different",
            threshold=0.99,
            container_by=AppiumBy.ACCESSIBILITY_ID,
            container_value="middleScrollView",
            container_w=320,
            container_h=476,
        )
    with step("[Action] Tap 'v'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btn_ok_n", 50.0, 50.0)
    with step("[Verify] Apply to edit room"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "homeButton")
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "EditingImageView_ImageView")
    with step("[Verify] Preview comparisons pass"):
        assert actions.run_screenshot_comparisons() is not False
