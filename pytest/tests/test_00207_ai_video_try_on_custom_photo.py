import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("ai_video_try_on_custom_photo")
def test_ai_video_try_on_custom_photo(actions: DriverActions):
    with step("[Action] Launch PhotoDirector"):
        actions.launch_app("com.cyberlink.photodirector")
    with step("[Action] Recover launcher after an interrupted earlier run"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "processingLabel", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_backButton", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_backButton", 50.0, 50.0)
    with step("[Action] Tap 'AI Video Try-On'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "AI Video Try-On", 50.0, 50.0)
    with step("[Verify] No intro page is displayed"):
        assert not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnNext", timeout=2)
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "videoSectionLabel")
    with step("[Action] Tap 'Import' on the video preview"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_importView", 50.0, 50.0)
    with step("[Verify] No source-video recommendation page is displayed"):
        assert not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "recommendTitleLabel", timeout=2)
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "Videos")
    with step("[Action] Select a video"):
        actions.tap_within_element(
            AppiumBy.XPATH,
            "(//XCUIElementTypeImage[contains(@label, 'Video, three seconds')])[1]",
            50.0,
            50.0,
        )
    with step("[Action] Tap 'Next'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0)
    with step("[Verify] Video is imported in preview"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_importView")
    with step("[Action] Tap 'Import' in the reference outfit area"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "mainArea", 50.0, 50.0)
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "Recommendation", timeout=3):
        with step("[Verify] Recommendation dialog pops up"):
            assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "PhotoPickerRecommendDialog")
        with step("[Action] Enable 'Don't show again'"):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID,
                "PhotoPickerRecommendDialog-notShowAgainCheckBox",
                50.0,
                50.0,
            )
        with step("[Action] Tap 'Continue'"):
            actions.tap_within_element(
                AppiumBy.ACCESSIBILITY_ID,
                "PhotoPickerRecommendDialog-continueButton",
                50.0,
                50.0,
            )
    with step("[Action] Select an outfit photo"):
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
    with step("[Verify] Outfit photo is imported to preview"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "photoImageView")
    with step("[Action] Tap the reference outfit preview"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "photoImageView", 50.0, 50.0)
    with step("[Verify] No recommendation dialog is displayed"):
        assert not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "PhotoPickerRecommendDialog", timeout=2)
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "btnAlbum")
    with step("[Action] Tap '<'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
    with step("[Action] Tap 'Generate'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_generateButton", 50.0, 50.0)
    with step("[Verify] Go to Artwork and process the video"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblTitle", "My AI Artwork") is not False
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "ScrollableMenuViewCell-AI Video Try-On")
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "processingLabel", "Processing...") is not False
