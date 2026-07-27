import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_adjustment_temperature_and_tint")
def test_test_adjustment_temperature_and_tint(actions: DriverActions):
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
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap Enhance"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    with step("[Action] Tap Adjustments"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')
    with step("[Action] Tap Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step("[Action] Tap Auto Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto Color')
    with step("[Action] Tap Auto Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto Color')
    with step("[Action] Tap Temperature"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Temperature')
    with step("[Action] Tap whiteBalanceDropperButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'whiteBalanceDropperButton')
    with step("[Action] Tap Show this tip next time"):
        actions.tap_by_locator(AppiumBy.NAME, 'Show this tip next time')
    with step("[Action] Tap at (300, 200)"):
        actions.tap_by_coordinates(300, 200)
    with step("[Action] Tap at (300, 230)"):
        actions.tap_by_coordinates(300, 230)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Adjustments"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')
    with step("[Action] Tap Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step("[Action] Tap Tint"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tint')
    with step("[Action] Tap whiteBalanceDropperButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'whiteBalanceDropperButton')
    with step("[Action] Tap Show this tip next time"):
        actions.tap_by_locator(AppiumBy.NAME, 'Show this tip next time')
    with step("[Action] Tap at (300, 200)"):
        actions.tap_by_coordinates(300, 200)
    with step("[Action] Tap at (300, 230)"):
        actions.tap_by_coordinates(300, 230)
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
