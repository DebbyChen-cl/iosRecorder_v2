import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


FIRST_LIBRARY_OUTFIT = (
    "(//XCUIElementTypeStaticText[@name='Outfit Library']/following::"
    "XCUIElementTypeCollectionView[1]/XCUIElementTypeCell)[1]"
)


@pytest.mark.name("ai_video_try_on_template")
def test_ai_video_try_on_template(actions: DriverActions):
    with step("[Action] Launch PhotoDirector"):
        actions.launch_app("com.cyberlink.photodirector")
    with step("[Action] Recover launcher after an interrupted earlier run"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "processingLabel", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnBack", 50.0, 50.0)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_backButton", timeout=2):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_backButton", 50.0, 50.0)
    with step("[Action] Tap 'AI Video Try-On'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "AI Video Try-On", 50.0, 50.0)
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "btnNext", timeout=3):
        with step("[Verify] Show intro page"):
            assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblTitle", "AI Video Try-On") is not False
        with step("[Action] Enable 'Don't show again'"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "notShowAgainCheckBox", 50.0, 50.0)
        with step("[Action] Tap 'Try now'"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0)
    with step("[Action] Tap 'Import' on the video preview"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_importView", 50.0, 50.0)
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, "recommendTitleLabel", timeout=3):
        with step("[Verify] Show recommendation page"):
            assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "recommendTitleLabel", "Recommendation") is not False
        with step("[Action] Enable 'Don't show again'"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "notShowAgainCheckBox", 50.0, 50.0)
        with step("[Action] Tap 'Continue'"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "continueButton", 50.0, 50.0)
    with step("[Action] Select a video longer than ten seconds"):
        actions.tap_within_element(
            AppiumBy.XPATH,
            "(//XCUIElementTypeImage[contains(@label, 'two minutes, twenty seconds')])[1]",
            50.0,
            50.0,
        )
    with step("[Action] Adjust duration to minimum"):
        actions.drag_within_elements(
            AppiumBy.ACCESSIBILITY_ID,
            "endBarImageView",
            50.0,
            50.0,
            AppiumBy.ACCESSIBILITY_ID,
            "trimmerPanel",
            16.3,
            49.4,
            duration=0.7,
        )
    with step("[Verify] Length is three seconds"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblDesc", "Selected Length: 00:03") is not False
    with step("[Verify] Current build credit cost is 21"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblCreditPrice", "21") is not False
    with step("[Action] Adjust duration to maximum"):
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
    with step("[Verify] Length is ten seconds"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblDesc", "Selected Length: 00:10") is not False
    with step("[Verify] Current build credit cost is 70"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblCreditPrice", "70") is not False
    with step("[Action/Verify] Move the trim frame"):
        assert actions.capture_for_preview(
            "ai_video_try_on_trim_range",
            "before",
            AppiumBy.ACCESSIBILITY_ID,
            "thumbnailsView",
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
        assert actions.capture_for_preview(
            "ai_video_try_on_trim_range",
            "after",
            AppiumBy.ACCESSIBILITY_ID,
            "thumbnailsView",
            expected_result="different",
            threshold=0.99,
        )
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblDesc", "Selected Length: 00:10") is not False
    with step("[Action] Tap 'Playback'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnPlay", 50.0, 50.0)
    with step("[Verify] Preview starts playback"):
        assert actions.verify_visible(
            AppiumBy.XPATH,
            "//XCUIElementTypeButton[@name='btnPlay' and @label='ic pause noBg white']",
        )
    with step("[Action] Tap 'Pause'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnPlay", 50.0, 50.0)
    with step("[Verify] Preview stops and sound is muted"):
        assert actions.verify_visible(
            AppiumBy.XPATH,
            "//XCUIElementTypeButton[@name='btnPlay' and @label='ic play noBg white']",
        )
        assert actions.verify_visible(
            AppiumBy.XPATH,
            "//XCUIElementTypeButton[@name='btnMuteToggle' and @label='ic volume off']",
        )
    with step("[Action] Tap the sound button"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnMuteToggle", 50.0, 50.0)
    with step("[Verify] Mute is off"):
        assert actions.verify_visible(
            AppiumBy.XPATH,
            "//XCUIElementTypeButton[@name='btnMuteToggle' and @label='ic volume']",
        )
    with step("[Action] Tap 'Next'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "btnNext", 50.0, 50.0)
    with step("[Verify] Video is imported, muted, and ten seconds long"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_importView")
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "ic volume off")
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "00:10", "00:10") is not False
    with step("[Action] Turn imported-preview mute off"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "ic volume off", 50.0, 50.0)
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "ic volume")
    with step("[Action] Select an outfit template"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID,
            "imageView",
            50.0,
            50.0,
            container_by=AppiumBy.ACCESSIBILITY_ID,
            container_value="carouselCollectionView",
            container_w=294,
            container_h=92,
        )
    with step("[Verify] Thumbnail is highlighted and template is imported"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "selectedBorderView")
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "photoImageView")
    with step("[Action] Tap 'Outfit Library'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "iconView", 50.0, 50.0)
    with step("[Verify] Enter Outfit Library"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "Outfit Library")
        assert actions.capture_for_preview(
            "ai_video_try_on_male_library",
            "before",
            AppiumBy.XPATH,
            FIRST_LIBRARY_OUTFIT,
        )
    with step("[Action] Tap 'Male'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Male", 50.0, 50.0)
    with step("[Verify] Male library is displayed"):
        assert actions.capture_for_preview(
            "ai_video_try_on_male_library",
            "after",
            AppiumBy.XPATH,
            FIRST_LIBRARY_OUTFIT,
            expected_result="different",
            threshold=0.99,
        )
        assert actions.capture_for_preview(
            "ai_video_try_on_female_library",
            "before",
            AppiumBy.XPATH,
            FIRST_LIBRARY_OUTFIT,
        )
    with step("[Action] Tap 'Female'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "Female", 50.0, 50.0)
    with step("[Verify] Female library is displayed"):
        assert actions.capture_for_preview(
            "ai_video_try_on_female_library",
            "after",
            AppiumBy.XPATH,
            FIRST_LIBRARY_OUTFIT,
            expected_result="different",
            threshold=0.99,
        )
    with step("[Action] Select an outfit from the library"):
        actions.tap_within_element(AppiumBy.XPATH, FIRST_LIBRARY_OUTFIT, 50.0, 50.0)
    with step("[Verify] Library template is imported"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "photoImageView")
    with step("[Action] Tap 'Generate'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, "aiVideoTryOn_generateButton", 50.0, 50.0)
    with step("[Verify] Go to Artwork and process the video"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "lblTitle", "My AI Artwork") is not False
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, "ScrollableMenuViewCell-AI Video Try-On")
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, "processingLabel", "Processing...") is not False
    with step("[Verify] Visual comparisons pass"):
        assert actions.run_screenshot_comparisons() is not False
