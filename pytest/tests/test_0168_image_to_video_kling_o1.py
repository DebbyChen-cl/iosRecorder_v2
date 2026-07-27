import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_image_to_video_kling_o1")
def test_test_image_to_video_kling_o1(actions: DriverActions):
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
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"ImageToVideoCustomModelDetailViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton"):
        actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="ImageToVideoCustomModelDetailViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton')
    with step("[Action] Tap Kling O1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Kling O1')
    with step("[Verify] Kling O1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Kling O1'), 'element Kling O1 should be visible'
    with step("[Verify] 5 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '5'), 'element 5 should be visible'
    with step("[Verify] 10 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '10'), 'element 10 should be visible'
    with step("[Action] Tap 10"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '10')
    with step("[Verify] 10 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '10'), 'element 10 should be visible'
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
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Verify] AI-generated sound isn’t available for this model. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AI-generated sound isn’t available for this model.'), 'element AI-generated sound isn’t available for this model. should be visible'
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
