import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_17_02_1")
def test_test_main_05_17_02_1(actions: DriverActions):
    with step("[Verify] Would you like to continue editing? is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Would you like to continue editing?'), 'element Would you like to continue editing? should not be visible'
    with step("[Verify] closeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'closeButton'), 'element closeButton should not be visible'
    with step("[Verify] navCloseButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton'), 'element navCloseButton should not be visible'
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Action] Tap Sparkle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sparkle')
    with step("[Action] Tap Sparkle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sparkle')
    with step("[Action] Tap SparkleCollectionViewCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'SparkleCollectionViewCell-1')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap SparkleCollectionViewCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'SparkleCollectionViewCell-1')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap Amount"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Amount')
    with step("[Verify] valueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'valueLabel'), 'element valueLabel should be visible'
    with step("[Action] Tap Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step("[Verify] hueValueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel'), 'element hueValueLabel should be visible'
    with step("[Verify] saturationValueLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel'), 'element saturationValueLabel should be visible'
    assert True
