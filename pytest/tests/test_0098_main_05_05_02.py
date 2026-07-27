import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_05_02")
def test_test_main_05_05_02(actions: DriverActions):
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
    with step("[Action] Tap Overlay Effect"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Overlay Effect')
    with step("[Action] Tap Light Leak"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light Leak')
    with step("[Action] Tap Rotate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')
    with step("[Action] Tap Rotate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')
    with step("[Action] Tap Rotate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')
    with step("[Action] Tap Rotate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')
    with step("[Action] Tap btn_flipH_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_flipH_n')
    with step("[Action] Tap btn_flipV_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_flipV_n')
    with step("[Action] Tap btn_flipV_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_flipV_n')
    with step("[Action] Tap btn_flipV_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_flipV_n')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Overlay Effect"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Overlay Effect')
    with step("[Action] Tap Light Leak"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light Leak')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
