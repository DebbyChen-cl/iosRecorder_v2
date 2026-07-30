import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("ai_video_try_on_custom_prompt")
def test_ai_video_try_on_custom_prompt(actions: DriverActions):
    with step("[Action] Launch PhotoDirector"):
        actions.launch_app("com.cyberlink.photodirector")
    with step("[Action] Recover launcher after an interrupted earlier run"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "reuseButton", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID,
            "ScrollableMenuViewCell-AI Video Try-On",
            timeout=2,
        ):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_backButton", timeout=2):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_backButton", 50.0, 50.0
            )
    with step("[Action] Tap 'AI Video Try-On'"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "AI Video Try-On", 50.0, 50.0
        )
    with step("[Action] Tap 'Import' on the video preview"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_importView", 50.0, 50.0
        )
    with step("[Action] Select a video"):
        actions.tap_within_element(
            AppiumBy.XPATH,
            "(//XCUIElementTypeImage[contains(@label, 'two minutes, twenty seconds')])[1]",
            50.0,
            50.0,
        )
    with step("[Action] Tap 'Next'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0)
    with step("[Verify] The video is imported in preview"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_importView")
    with step("[Action] Tap 'Describe by Prompts'"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_inputMode_prompt", 50.0, 50.0
        )
    with step("[Verify] The default description is displayed"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_promptInput")
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "clearButton", timeout=1):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID, "clearButton", 50.0, 50.0
            )
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "textCountLabel", "0/2000") is not False
    with step("[Action] Input 'aaaa'"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_promptInput", 30.0, 35.0
        )
        actions.type_text_by_locator(
            AppiumBy.ACCESSIBILITY_ID, "textView", "aaaa", clear_first=False
        )
    with step("[Verify] Default description is replaced with 'aaaa'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "textCountLabel", "4/2000") is not False
    with step("[Action] Tap 'x'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "clearButton", 50.0, 50.0)
    with step("[Verify] Prompt is gone and the default description is shown"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "textCountLabel", "0/2000") is not False
    with step("[Action] Input prompt '7-11 uniform'"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_promptInput", 30.0, 35.0
        )
        actions.type_text_by_locator(
            AppiumBy.ACCESSIBILITY_ID,
            "textView",
            "7-11 uniform",
            clear_first=False,
        )
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "textCountLabel", "12/2000")
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "Next:", timeout=1):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Next:", 50.0, 50.0)
        else:
            actions.hide_keyboard()
    with step("[Action] Tap 'Generate'"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_generateButton", 50.0, 50.0
        )
    with step("[Verify] Go to Artwork and process the video"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblTitle", "My AI Artwork") is not False
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "processingLabel", "Processing...") is not False
    with step("[Action] Wait for generation to finish"):
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, "processingLabel", timeout=300)
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "generateButton")
    with step("[Action] Tap '<'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if not actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_myPromptsButton", timeout=3
        ):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID, "generateButton", 50.0, 50.0
            )
    with step("[Action] Tap 'My Prompts'"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_myPromptsButton", 50.0, 50.0
        )
    with step("[Verify] Successful generated prompt and thumbnail are listed"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "listCollectionView")
        assert actions.verify_visible(
            AppiumBy.XPATH,
            "//XCUIElementTypeStaticText[@name='7-11 uniform' or @label='7-11 uniform']",
        )
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "reuseButton")
    with step("[Action] Tap 'Reuse'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "reuseButton", 50.0, 50.0)
    with step("[Verify] The prompt is imported"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "textCountLabel", "12/2000") is not False
