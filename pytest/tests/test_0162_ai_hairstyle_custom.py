import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_hairstyle_custom")
def test_test_ai_hairstyle_custom(actions: DriverActions):
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap AI Hairstyle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle')
    with step("[Verify] lblDesc is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'lblDesc'), 'element lblDesc should not be visible'
    with step("[Action] Tap importButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step("[Verify] descriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'), 'element descriptionLabel should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step("[Action] Tap Custom"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Custom')
    with step("[Action] Tap describeClothingStyleButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'describeClothingStyleButton')
    with step("[Action] Tap XCUIElementTypeTextField"):
        actions.tap_by_locator(AppiumBy.XPATH, 'XCUIElementTypeTextField')
    assert False, "original pytest run failed — this recording reproduces a failing run"
