import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_12_01_1")
def test_test_main_05_12_01_1(actions: DriverActions):
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
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap Frame"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Frame')
    with step("[Action] Tap Frame"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Frame')
    with step("[Action] Tap Frame"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Frame')
    with step("[Action] Tap btn effect store n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn effect store n')
    with step("[Verify] New is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'New'), 'element New should be visible'
    with step("[Action] Tap at (68, 250)"):
        actions.tap_by_coordinates(68, 250)
    with step("[Action] Tap Download"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Download')
    with step("[Verify] Use is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Use'), 'element Use should be visible'
    with step("[Action] Tap btn webstore back n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn webstore back n')
    with step("[Action] Tap btn webstore back n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn webstore back n')
    assert True
