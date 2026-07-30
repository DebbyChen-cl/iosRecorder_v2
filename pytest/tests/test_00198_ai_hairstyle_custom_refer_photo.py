import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("ai_hairstyle_custom_refer_photo")
def test_ai_hairstyle_custom_refer_photo(actions: DriverActions):
    with step("[Action] Launch PhotoDirector"):
        actions.launch_app("com.cyberlink.photodirector")
    with step("[Action] Recover launcher after an interrupted earlier run"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnAlbum", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "Select Photo", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID, "ScrollableMenuViewCell-AI Hairstyle", timeout=2
        ):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "navDescriptionLabel", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "navBackButton", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnHome", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnHome", 50.0, 50.0)
    with step("[Action] Open AI Photos > AI Hairstyle"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnStudio", 50.0, 50.0)
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID,
            "CMS-PhDM_AIMagic_AIHairstyle_20257E",
            50.0,
            50.0,
        )
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnNext", timeout=3):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0)
    with step("[Action] Import the third Sample Photos image"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "importButton", 50.0, 50.0)
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
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "PhDM_example_3", 50.0, 50.0)
        actions.wait_for_visible(AppiumBy.ACCESSIBILITY_ID, "navDescriptionLabel", timeout=30)
    with step("[Action] Tap Custom > Upload a hairstyle photo"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "customStyleCell", 50.0, 50.0)
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "uploadClothingPhotoButton", 50.0, 50.0
        )
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "PhotoPickerRecommendDialog", timeout=3):
        with step("[Verify] Recommendation dialog pops up"):
            assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "PhotoPickerRecommendDialog")
        with step("[Action] Enable Don't show again and continue"):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID,
                "PhotoPickerRecommendDialog-notShowAgainCheckBox",
                50.0,
                50.0,
            )
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID,
                "PhotoPickerRecommendDialog-continueButton",
                50.0,
                50.0,
            )
    with step("[Action] Tap 'i'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "ic info n", 50.0, 50.0)
    with step("[Verify] Recommendation dialog pops up"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "PhotoPickerRecommendDialog")
    with step("[Action] Tap Continue"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID,
            "PhotoPickerRecommendDialog-continueButton",
            50.0,
            50.0,
        )
    with step("[Action] Select the second single-female photo"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "photoCell-1", 50.0, 50.0)
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "btnNext")
    with step("[Action] Attempt to select the fourth photo"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "photoCell-3", 50.0, 50.0)
    with step("[Verify] At most one reference photo remains selected"):
        toast = "//*[contains(@name, 'at most 1 photo') or contains(@label, 'at most 1 photo')]"
        if actions.is_element_present(AppiumBy.XPATH, toast, timeout=2):
            assert actions.verify_visible(AppiumBy.XPATH, toast)
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "btnNext")
    with step("[Action] Tap Next"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0)
    with step("[Verify] Custom style displays Photo with a 1 icon"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "Photo", "Photo") is not False
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "1", "1") is not False
    with step("[Action] Clear the Photo custom style"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "clearButton", 50.0, 50.0)
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "Custom", "Custom")
    with step("[Action] Reopen Upload a hairstyle photo"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "customStyleCell", 50.0, 50.0)
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "uploadClothingPhotoButton", 50.0, 50.0
        )
    with step("[Verify] No recommendation dialog is displayed"):
        assert not actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID, "PhotoPickerRecommendDialog", timeout=2
        )
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "btnNext")
    with step("[Action] Select the second photo and tap Next"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "photoCell-1", 50.0, 50.0)
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0)
    with step("[Action] Tap Generate"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnGenerate", 50.0, 50.0)
    with step("[Verify] Artwork shows the image under processing"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblTitle", "My AI Artwork") is not False
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "statusLabel", "Processing...") is not False
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "activityIndicator")
    with step("[Action] Wait for processing to finish"):
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, "statusLabel", timeout=180)
    with step("[Verify] The thumbnail is updated to the generated image"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "AIArtworkPackSelectionCell-0")
