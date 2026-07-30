import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


LONG_VIDEO = "(//XCUIElementTypeImage[contains(@label, 'two minutes, twenty seconds')])[1]"
SHORT_VIDEO = "(//XCUIElementTypeImage[contains(@label, 'Video, three seconds')])[1]"


@pytest.mark.name("motion_swap_move_mode")
def test_motion_swap_move_mode(actions: DriverActions):
    with step("[Action] Launch PhotoDirector"):
        actions.launch_app("com.cyberlink.photodirector")
    with step("[Action] Recover the launcher after an interrupted run"):
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID, "navCloseButton", timeout=2
        ):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID, "navCloseButton", 50.0, 50.0
            )
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID, "interstitialCloseButton", timeout=2
        ):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID,
                "interstitialCloseButton",
                50.0,
                50.0,
            )
        for _ in range(3):
            if not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "Cancel", timeout=2):
                break
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Cancel", 50.0, 50.0)
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID, "recommendationLbl", timeout=2
        ):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID, "btn back n", 50.0, 50.0
            )
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "Continue Anyway", timeout=2):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID, "Continue Anyway", 50.0, 50.0
            )
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID,
            "PhotoPickerRecommendDialog-continueButton",
            timeout=2,
        ):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID,
                "PhotoPickerRecommendDialog-continueButton",
                50.0,
                50.0,
            )
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnAlbum", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID,
            "ScrollableMenuViewCell-Character Motion Swap",
            timeout=2,
        ):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnHome", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnHome", 50.0, 50.0)
    with step("[Action] Tap Character Motion Swap"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "Character Motion Swap", 50.0, 50.0
        )
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "notShowAgainCheckBox", timeout=3):
        with step("[Verify] The intro page is displayed"):
            assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "btnNext")
        with step("[Action] Enable Don't show again and tap Try now"):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID, "notShowAgainCheckBox", 50.0, 50.0
            )
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0)
    with step("[Action/Verify] Show the photo hint bubble"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnInfo", 50.0, 50.0)
        assert actions.verify_text(
            AppiumBy.ACCESSIBILITY_ID,
            "Use a photo with the same aspect ratio as your video.",
            "Use a photo with the same aspect ratio as your video.",
        ) is not False
        actions.tap_by_coordinates(300, 100)
    with step("[Action] Import a full-body photo from the AT album"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnImportFace", 50.0, 50.0)
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID, "PhotoPickerRecommendDialog", timeout=3
        ):
            actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "PhotoPickerRecommendDialog")
            if actions.is_element_present(
                AppiumBy.ACCESSIBILITY_ID,
                "PhotoPickerRecommendDialog-notShowAgainCheckBox",
                timeout=2,
            ):
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
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnAlbum", 50.0, 50.0)
        album = actions.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "_AT", direction="up")
        actions.tap(album)
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "photoCell-2", 50.0, 50.0)
        actions.wait_for_visible(AppiumBy.ACCESSIBILITY_ID, "btnImportFace", timeout=30)
    with step("[Verify] The imported photo thumbnail is displayed"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "btnImportFace")
    with step("[Action] Replace the photo with another AT photo"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnImportFace", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnInfo", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnInfo", 50.0, 50.0)
            if actions.is_element_present(
                AppiumBy.ACCESSIBILITY_ID,
                "PhotoPickerRecommendDialog-continueButton",
                timeout=2,
            ):
                actions.tap_within_element(
                    AppiumBy.ACCESSIBILITY_ID,
                    "PhotoPickerRecommendDialog-continueButton",
                    50.0,
                    50.0,
                )
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnAlbum", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnAlbum", 50.0, 50.0)
            album = actions.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "_AT", direction="up")
            actions.tap(album)
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "photoCell-3", 50.0, 50.0)
        actions.wait_for_visible(AppiumBy.ACCESSIBILITY_ID, "btnImportFace", timeout=30)
    with step("[Action] Import a reference video"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "btnImportReference", 50.0, 50.0
        )
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "recommendationLbl", timeout=3):
            actions.verify_text(
                AppiumBy.ACCESSIBILITY_ID, "recommendationLbl", "Recommendation"
            )
            if actions.is_element_present(
                AppiumBy.ACCESSIBILITY_ID, "notShowAgainCheckBox", timeout=2
            ):
                actions.tap_within_element(
                    AppiumBy.ACCESSIBILITY_ID,
                    "notShowAgainCheckBox",
                    50.0,
                    50.0,
                )
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0
            )
        actions.tap_within_element(AppiumBy.XPATH, LONG_VIDEO, 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "Done", timeout=3):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Done", 50.0, 50.0)
    with step("[Action/Verify] Adjust and move the trim range"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "trimmerPanel", timeout=5):
            actions.drag_within_elements(
                AppiumBy.ACCESSIBILITY_ID,
                "endBarImageView",
                50.0,
                50.0,
                AppiumBy.ACCESSIBILITY_ID,
                "trimmerPanel",
                23.1,
                49.4,
                duration=0.7,
            )
            actions.drag_within_elements(
                AppiumBy.ACCESSIBILITY_ID,
                "topSlidingBarTouchArea",
                49.1,
                24.0,
                AppiumBy.ACCESSIBILITY_ID,
                "trimmerPanel",
                46.6,
                77.1,
                duration=0.7,
            )
            assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "lblDesc")
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0)
        actions.wait_for_visible(AppiumBy.ACCESSIBILITY_ID, "btnImportReference", timeout=30)
    with step("[Verify] The imported video thumbnail is displayed"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "btnImportReference")
    with step("[Action] Keep the photo background and Generate"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "Keep the photo background", 50.0, 50.0
        )
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0)
    with step("[Verify] Artwork shows Character Motion Swap processing"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblTitle", "My AI Artwork") is not False
        assert actions.verify_visible(
            AppiumBy.ACCESSIBILITY_ID, "ScrollableMenuViewCell-Character Motion Swap"
        )
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "labelProcessing", "Processing...") is not False
    with step("[Action] Back, select Kling Motion Control, and Generate"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID,
            "btnCharacterMotionSwapModelSelector",
            50.0,
            50.0,
        )
        kling = actions.scroll_to_element(
            AppiumBy.XPATH,
            "//*[contains(@name, 'Kling') and contains(@name, 'Motion')]",
            direction="up",
        )
        actions.tap(kling)
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0)
    with step("[Verify] The second video is processing in Artwork"):
        assert actions.verify_visible(
            AppiumBy.ACCESSIBILITY_ID, "ScrollableMenuViewCell-Character Motion Swap"
        )
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "labelProcessing", "Processing...") is not False
    with step("[Action] Return and replace the reference video"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, "btnImportReference", 50.0, 50.0
        )
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "continueButton", timeout=2):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID, "continueButton", 50.0, 50.0
            )
        actions.tap_within_element(AppiumBy.XPATH, SHORT_VIDEO, 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "Done", timeout=3):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Done", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnNext", timeout=3):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0)
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "btnImportReference")
    with step("[Action] Tap Home"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnHome", 50.0, 50.0)
    with step("[Verify] Back to the launcher"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "Character Motion Swap")
