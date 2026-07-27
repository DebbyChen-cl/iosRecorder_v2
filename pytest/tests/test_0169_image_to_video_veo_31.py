import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_image_to_video_veo_31")
def test_test_image_to_video_veo_31(actions: DriverActions):
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
    with step("[Verify] Continue is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Continue'), 'element Continue should not be visible'
    with step("[Verify] //*[@name=\"Continue\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Continue"]'), 'element //*[@name="Continue"] should not be visible'
    with step("[Verify] //*[@label=\"Continue\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="Continue"]'), 'element //*[@label="Continue"] should not be visible'
    with step("[Verify] //*[@value=\"Continue\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="Continue"]'), 'element //*[@value="Continue"] should not be visible'
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
    with step("[Action] Tap Veo 3.1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Veo 3.1')
    with step("[Verify] Veo 3.1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Veo 3.1'), 'element Veo 3.1 should be visible'
    with step("[Verify] 4 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '4'), 'element 4 should be visible'
    with step("[Verify] 6 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '6'), 'element 6 should be visible'
    with step("[Verify] 8 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '8'), 'element 8 should be visible'
    with step("[Action] Tap 8"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '8')
    with step("[Verify] 8 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '8'), 'element 8 should be visible'
    with step("[Verify] Standard is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Standard'), 'element Standard should be visible'
    with step("[Verify] Pro is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Pro'), 'element Pro should be visible'
    with step("[Action] Tap Standard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Standard')
    with step("[Verify] Standard is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Standard'), 'element Standard should be visible'
    with step("[Action] Tap Generate Sound by AI"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate Sound by AI')
    with step("[Verify] Generate Sound by AI is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Generate Sound by AI'), 'element Generate Sound by AI should be visible'
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Verify] Generate audio from video and prompt, supporting dialogue, sound effects, and music. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Generate audio from video and prompt, supporting dialogue, sound effects, and music.'), 'element Generate audio from video and prompt, supporting dialogue, sound effects, and music. should be visible'
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
