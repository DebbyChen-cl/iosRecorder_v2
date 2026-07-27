import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_headshot")
def test_test_ai_headshot(actions: DriverActions):
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap AI Headshot"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Headshot')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap navArtworkButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navArtworkButton')
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap Create More"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Create More')
    with step("[Action] Tap Male"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Male')
    with step("[Verify] Office is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Office'), 'element Office should be visible'
    with step("[Action] Tap Shirt"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shirt')
    with step("[Verify] Building is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Building'), 'element Building should be visible'
    with step("[Action] Tap Building"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Building')
    with step("[Action] Tap continueButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'continueButton')
    with step("[Verify] recommendationLbl is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'recommendationLbl'), 'element recommendationLbl should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap BG"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'BG')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Verify] Please choose another photo. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Please choose another photo.'), 'element Please choose another photo. should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step("[Verify] iconImageView is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'iconImageView'), 'element iconImageView should not be visible'
    with step("[Verify] GET UP TO 30% OFF With Premium is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'GET UP TO 30% OFF With Premium'), 'element GET UP TO 30% OFF With Premium should not be visible'
    assert False, "original pytest run failed — this recording reproduces a failing run"
