import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


MODEL = "Kling O3"
DURATIONS = ("5", "10", "15")
SELECTED_DURATION = "10"
DISABLED_SOUND = None
PROMPT = "The train drive through"
SOUND_INFO = "Generate audio from video and prompt"


@pytest.mark.name("ai_image_to_video_kling_o3")
def test_ai_image_to_video_kling_o3(actions: DriverActions):
    with step("[Action] Launch PhotoDirector"):
        actions.launch_app("com.cyberlink.photodirector")
    with step("[Action] Recover the launcher after an interrupted earlier run"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnAlbum", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "Kling 2.6", timeout=2):
            actions.tap_by_coordinates(160, 240)
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID, "ScrollableMenuViewCell-Image to Video", timeout=2
        ):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnHome", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnHome", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btn_cancel_n", timeout=2):
            actions.tap_by_coordinates(31, 646)
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID, "creditGenerateButton", timeout=2
        ):
            for _ in range(2):
                actions.tap_within_element(
                    AppiumBy.ACCESSIBILITY_ID, "navBackButton", 50.0, 50.0
                )
                if actions.is_element_present(
                    AppiumBy.ACCESSIBILITY_ID, "Image to Video", timeout=5
                ):
                    break
            actions.wait_for_visible(
                AppiumBy.ACCESSIBILITY_ID, "Image to Video", timeout=30
            )
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
        album = actions.scroll_to_element(
            AppiumBy.ACCESSIBILITY_ID, "Sample Photos", direction="up"
        )
        actions.tap(album)
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "photoCell-5", 50.0, 50.0)
        actions.wait_for_visible(AppiumBy.ACCESSIBILITY_ID, "CMS-local_custom", timeout=30)
    with step(f"[Action] Open Custom and select {MODEL}"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "CMS-local_custom", 50.0, 50.0)
        actions.tap_by_coordinates(160, 230)
        model_text = actions.scroll_to_element(
            AppiumBy.ACCESSIBILITY_ID, MODEL, direction="up"
        )
        for _ in range(3):
            if int(model_text.rect["y"]) <= 560:
                break
            actions.swipe_on_element(
                AppiumBy.XPATH,
                "(//XCUIElementTypeScrollView)[2]",
                "up",
                distance_pts=250,
            )
            model_text = actions.find_element(AppiumBy.ACCESSIBILITY_ID, MODEL)
        model_rect = model_text.rect
        actions.tap_by_coordinates(160, int(model_rect["y"]) + 30)
        actions.wait_for_visible(
            AppiumBy.ACCESSIBILITY_ID, f"button_{SELECTED_DURATION}", timeout=10
        )
    with step(f"[Verify] {MODEL} is selected and DURATIONS are listed"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, MODEL, MODEL)
        for duration in DURATIONS:
            actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, f"button_{duration}")
    with step(f"[Action] Select {SELECTED_DURATION}s"):
        duration_button = actions.find_element(
            AppiumBy.ACCESSIBILITY_ID, f"button_{SELECTED_DURATION}"
        )
        duration_rect = duration_button.rect
        actions.tap_by_coordinates(
            int(duration_rect["x"] + duration_rect["width"] / 2),
            int(duration_rect["y"] + duration_rect["height"] / 2),
        )
        assert actions.find_element(
            AppiumBy.ACCESSIBILITY_ID, f"button_{SELECTED_DURATION}"
        ).get_attribute("value") == "1"
    with step("[Verify] Standard and Pro quality are listed and selectable"):
        actions.tap_by_coordinates(47, 533)
        assert actions.find_element(
            AppiumBy.ACCESSIBILITY_ID, "button_Standard"
        ).get_attribute("value") == "1"
        actions.tap_by_coordinates(110, 533)
        pro_id = (
            "button_Pro"
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "button_Pro", timeout=2)
            else "button_Professional"
        )
        assert actions.find_element(
            AppiumBy.ACCESSIBILITY_ID, pro_id
        ).get_attribute("value") == "1"
    with step("[Action] Exercise the MODEL's AI sound control"):
        target = DISABLED_SOUND or "On"
        actions.tap_by_coordinates(33 if target == "Off" else 80, 602)
        if DISABLED_SOUND:
            if actions.is_element_present(
                AppiumBy.ACCESSIBILITY_ID, f"button_{target}", timeout=2
            ):
                sound = actions.find_element(
                    AppiumBy.ACCESSIBILITY_ID, f"button_{target}"
                )
                assert not sound.is_enabled()
            else:
                assert not actions.is_element_present(
                    AppiumBy.ACCESSIBILITY_ID, f"button_{target}", timeout=1
                )
        else:
            sound = actions.find_element(AppiumBy.ACCESSIBILITY_ID, f"button_{target}")
            assert sound.is_enabled()
            assert sound.get_attribute("value") == "1"
    with step("[Action] Show and dismiss the AI sound information bubble"):
        actions.tap_by_coordinates(168, 574)
        info = f"//*[contains(@name, '{SOUND_INFO}') or contains(@label, '{SOUND_INFO}')]"
        actions.verify_visible(AppiumBy.XPATH, info)
        actions.tap_by_coordinates(30, 190)
        actions.verify_not_visible(AppiumBy.XPATH, info)
    with step("[Action] Enter the prompt and apply Custom settings"):
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
