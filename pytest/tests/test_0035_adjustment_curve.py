import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_adjustment_curve")
def test_test_adjustment_curve(actions: DriverActions):
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
    with step("[Action] Tap Curve"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Curve')
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Action] Tap btn arrow down n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step("[Action] Tap tab icon b n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'tab icon b n')
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap btn_reset_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n')
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap btnHSLCurveReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset')
    with step("[Action] Tap tab icon g n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'tab icon g n')
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap btn_reset_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n')
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap btnHSLCurveReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset')
    with step("[Action] Tap curve tab icon r n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'curve tab icon r n')
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap btn_reset_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n')
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap btnHSLCurveReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset')
    with step("[Action] Tap curve tab icon rgb n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'curve tab icon rgb n')
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap btn_reset_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n')
    with step("[Action] Tap btnReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step("[Action] Tap btnHSLCurveReset"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHSLCurveReset')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Adjustments"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')
    with step("[Action] Tap Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step("[Action] Tap Curve"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Curve')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
