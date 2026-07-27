import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_adjustment_exposure_contrast_highlights_shadows")
def test_test_adjustment_exposure_contrast_highlights_shadows(actions: DriverActions):
    with step("[Verify] Would you like to continue editing? is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Would you like to continue editing?'), 'element Would you like to continue editing? should not be visible'
    with step("[Verify] closeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'closeButton'), 'element closeButton should not be visible'
    with step("[Verify] navCloseButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton'), 'element navCloseButton should not be visible'
    with step("[Action] Tap closeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
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
    with step("[Action] Tap reginalAdjustmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')
    with step("[Action] Tap reginalAdjustmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')
    with step("[Action] Tap reginalAdjustmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')
    with step("[Action] Tap ic gradient mask n"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic gradient mask n')
    with step("[Action] Tap Auto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Adjustments"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')
    with step("[Action] Tap Contrast"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Contrast')
    with step("[Action] Tap reginalAdjustmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')
    with step("[Action] Tap reginalAdjustmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')
    with step("[Action] Tap reginalAdjustmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')
    with step("[Action] Tap reginalAdjustmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Adjustments"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')
    with step("[Action] Tap Highlight"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Highlight')
    with step("[Action] Tap reginalAdjustmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')
    with step("[Action] Tap reginalAdjustmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')
    with step("[Action] Tap reginalAdjustmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Adjustments"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')
    with step("[Action] Tap Bright"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Bright')
    with step("[Action] Tap Dark"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dark')
    with step("[Action] Tap Shadow"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
