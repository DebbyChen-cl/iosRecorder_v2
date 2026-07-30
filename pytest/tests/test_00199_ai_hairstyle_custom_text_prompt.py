import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("ai_hairstyle_custom_text_prompt")
def test_ai_hairstyle_custom_text_prompt(actions: DriverActions):
    with step("[Action] Launch PhotoDirector"):
        actions.launch_app("com.cyberlink.photodirector")
    with step("[Action] Recover launcher after an interrupted earlier run"):
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID,
            "ScrollableMenuViewCell-AI Hairstyle",
            timeout=2,
        ):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "navDescriptionLabel", timeout=2):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID, "navBackButton", 50.0, 50.0
            )
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnHome", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnHome", 50.0, 50.0)
    with step("[Action] Tap 'AI Photos'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnStudio", 50.0, 50.0)
    with step("[Action] Tap 'AI Hairstyle'"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID,
            "CMS-PhDM_AIMagic_AIHairstyle_20257E",
            50.0,
            50.0,
        )
    with step("[Action] Tap 'Try now' on the optional intro page"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnNext", timeout=3):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0)
    with step("[Action] Tap 'Import'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "importButton", 50.0, 50.0)
    with step("[Action] Tap 'Continue' on the optional recommendation dialog"):
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
    with step("[Action] Expand album list"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnAlbum", 50.0, 50.0)
    with step("[Action] Select AT album"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "_AT", 50.0, 50.0)
    with step("[Action] Select a single female photo"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "photoCell-1", 50.0, 50.0)
        actions.wait_for_visible(AppiumBy.ACCESSIBILITY_ID, "navDescriptionLabel", timeout=30)
    with step("[Action] Select 'Custom' style"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "customStyleCell", 50.0, 50.0
        )
    with step("[Action] Select 'Describe hairstyle'"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "describeClothingStyleButton", 50.0, 50.0
        )
    with step("[Action] Replace the style name with 'Custom style'"):
        actions.type_text_by_locator(
            AppiumBy.CLASS_NAME,
            "XCUIElementTypeTextField",
            "Custom style",
            clear_first=True,
        )
    with step("[Verify] The style name can be modified"):
        assert actions.verify_text(
            AppiumBy.CLASS_NAME, "XCUIElementTypeTextField", "Custom style"
        ) is not False
    with step("[Action] Input prompt 'aaaaaa'"):
        actions.type_text_by_locator(
            AppiumBy.ACCESSIBILITY_ID, "textView", "aaaaaa", clear_first=True
        )
    with step("[Verify] Prompt is modified"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "counterLabel", "6/5000") is not False
    with step("[Action] Tap 'x' button of prompt column"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "clearButton", 50.0, 50.0)
    with step("[Verify] Prompt is reset to the default description"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "counterLabel", "0/5000") is not False
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "placeholderLabel")
    with step("[Action] Input prompt 'Reinbow afro'"):
        actions.type_text_by_locator(
            AppiumBy.ACCESSIBILITY_ID, "textView", "Reinbow afro", clear_first=True
        )
    with step("[Action] Tap 'Apply'"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "promptApplyButton", 50.0, 50.0
        )
    with step("[Action] Tap 'Generate'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnGenerate", 50.0, 50.0)
    with step("[Verify] Go to Artwork and show a busy thumbnail"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblTitle", "My AI Artwork") is not False
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "statusLabel", "Processing...") is not False
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "activityIndicator")
    with step("[Action] Wait for generation to finish"):
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, "statusLabel", timeout=180)
    with step("[Verify] The thumbnail is updated to the result"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "AIArtworkPackSelectionCell-0")
    with step("[Action] Tap '<' to return to the feature page"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
    with step("[Action] Tap the custom style displayed as 'Prompt'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "Prompt", "Prompt")
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "customStyleCell", 50.0, 50.0
        )
    with step("[Verify] The previous prompt is displayed"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "textView", "Reinbow afro") is not False
    with step("[Action] Edit prompt to 'Gold wave' and apply"):
        actions.type_text_by_locator(
            AppiumBy.ACCESSIBILITY_ID, "textView", "Gold wave", clear_first=True
        )
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "promptApplyButton", 50.0, 50.0
        )
    with step("[Action] Tap 'Generate'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnGenerate", 50.0, 50.0)
    with step("[Verify] Go to Artwork and show a busy thumbnail"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblTitle", "My AI Artwork") is not False
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "statusLabel", "Processing...") is not False
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "activityIndicator")
    with step("[Action] Wait for generation to finish"):
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, "statusLabel", timeout=180)
    with step("[Verify] The thumbnail is updated to the result"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "AIArtworkPackSelectionCell-0")
    with step("[Action] Tap '<' to return to the feature page"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
    with step("[Action] Tap 'x' of the custom Prompt style"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "clearButton", 50.0, 50.0)
    with step("[Verify] The custom style thumbnail displays 'Custom'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "Custom", "Custom") is not False
