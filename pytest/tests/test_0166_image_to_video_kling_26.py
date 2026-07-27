import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_image_to_video_kling_26")
def test_test_image_to_video_kling_26(actions: DriverActions):
    with step("[Action] Tap Image to Video"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Image to Video')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap imageIconView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'imageIconView')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap Sample Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos')
    with step("[Action] Tap photoCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step("[Action] Tap Custom"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Custom')
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Action] Tap Kling 2.6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Kling 2.6')
    with step("[Verify] Kling 2.6 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Kling 2.6'), 'element Kling 2.6 should be visible'
    with step("[Verify] 5 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '5'), 'element 5 should be visible'
    with step("[Verify] 10 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '10'), 'element 10 should be visible'
    with step("[Action] Tap 10"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '10')
    with step("[Verify] 10 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '10'), 'element 10 should be visible'
    with step("[Verify] Pro is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Pro'), 'element Pro should be visible'
    with step("[Action] Tap Generate Sound by AI"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate Sound by AI')
    with step("[Verify] Generate Sound by AI is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Generate Sound by AI'), 'element Generate Sound by AI should be visible'
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Verify] Generate audio from video and prompt, supporting dialogue, sound effects, and music​. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Generate audio from video and prompt, supporting dialogue, sound effects, and music​.'), 'element Generate audio from video and prompt, supporting dialogue, sound effects, and music​. should be visible'
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Action] Type 'The train drive through' into textView"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'textView', 'The train drive through')
    with step("[Action] Tap Next:"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] processingLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'processingLabel'), 'element processingLabel should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    assert True
