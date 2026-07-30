import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


PROMPT = "The train drive through"
SOUND_INFO = "Generate audio from video and prompt"


@pytest.mark.name("ai_image_to_video_happy_horse")
def test_ai_image_to_video_happy_horse(actions: DriverActions):
    with step("[Action] Launch PhotoDirector"):
        actions.launch_app("com.cyberlink.photodirector")
    with step("[Action] Recover the launcher after an interrupted earlier run"):
        # A first-use iOS Dictation alert is not exposed in the app hierarchy. Its
        # "Not Now" row overlays this otherwise inert point on the settings sheet.
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btn_cancel_n", timeout=2):
            actions.tap_by_coordinates(160, 432)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnAlbum", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "Kling 2.6", timeout=2):
            actions.tap_by_coordinates(160, 240)
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID, "ScrollableMenuViewCell-Image to Video", timeout=2
        ):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btn_cancel_n", timeout=2):
            actions.tap_by_coordinates(31, 646)
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID, "creditGenerateButton", timeout=2
        ):
            actions.tap_by_coordinates(28, 56)
    with step("[Action] Tap Image to Video"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Image to Video", 50.0, 50.0)
    with step("[Action] Dismiss optional intro and Steps pages"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "Try now", timeout=3):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Try now", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "Continue", timeout=3):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Continue", 50.0, 50.0)
    with step("[Action] Import the city photo from Sample Photos"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "imageIconView", 50.0, 50.0)
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID,
            "PhotoPickerRecommendDialog-continueButton",
            timeout=3,
        ):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID,
                "PhotoPickerRecommendDialog-continueButton",
                50.0,
                50.0,
            )
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnAlbum", 50.0, 50.0)
        sample_album = actions.scroll_to_element(
            AppiumBy.ACCESSIBILITY_ID, "Sample Photos", direction="up"
        )
        actions.tap(sample_album)
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "photoCell-5", 50.0, 50.0)
        actions.wait_for_visible(AppiumBy.ACCESSIBILITY_ID, "CMS-local_custom", timeout=30)
    with step("[Action] Open Custom and select Happy Horse"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "CMS-local_custom", 50.0, 50.0)
        actions.tap_by_coordinates(160, 230)
        actions.tap_by_coordinates(160, 240)
        actions.wait_for_visible(AppiumBy.ACCESSIBILITY_ID, "button_10", timeout=10)
    with step("[Verify] Happy Horse and 5s, 10s, 15s durations are listed"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "Happy Horse", "Happy Horse") is not False
        for duration in ("button_5", "button_10", "button_15"):
            assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, duration)
    with step("[Action] Select 10s"):
        actions.tap_by_coordinates(76, 464)
        assert actions.find_element(
            AppiumBy.ACCESSIBILITY_ID, "button_10"
        ).get_attribute("value") == "1"
    with step("[Verify] Standard and Pro quality are listed and selectable"):
        actions.tap_by_coordinates(47, 533)
        assert actions.find_element(
            AppiumBy.ACCESSIBILITY_ID, "button_Standard"
        ).get_attribute("value") == "1"
        actions.tap_by_coordinates(110, 533)
        assert actions.find_element(
            AppiumBy.ACCESSIBILITY_ID, "button_Pro"
        ).get_attribute("value") == "1"
    with step("[Verify] AI sound Off cannot be selected"):
        off_button = actions.find_element(AppiumBy.ACCESSIBILITY_ID, "button_Off")
        assert not off_button.is_enabled()
    with step("[Action] Show and dismiss the AI sound information bubble"):
        actions.tap_by_coordinates(168, 574)
        info = f"//*[contains(@name, '{SOUND_INFO}') or contains(@label, '{SOUND_INFO}')]"
        actions.verify_visible(AppiumBy.XPATH, info)
        actions.tap_by_coordinates(30, 190)
        actions.verify_not_visible(AppiumBy.XPATH, info)
    with step("[Action] Enter the custom prompt and apply settings"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, "textView", PROMPT)
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Next:", 50.0, 50.0)
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btn_ok_n", 50.0, 50.0)
    with step("[Action] Tap Generate"):
        generate = actions.find_element(AppiumBy.ACCESSIBILITY_ID, "creditGenerateButton")
        assert generate.is_enabled()
        actions.tap(generate)
    with step("[Verify] Artwork starts generation without an error"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblTitle", "My AI Artwork") is not False
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "ScrollableMenuViewCell-Image to Video")
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "processingLabel", "Processing...") is not False
