import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_vhs")
def test_test_vhs(actions: DriverActions):
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap VHS"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'VHS')
    with step("[Action] Tap VHS"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'VHS')
    with step("[Action] Tap VHS_1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'VHS_1')
    with step("[Action] Tap shapeMaskModeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskModeButton')
    with step("[Action] Tap SplashMaskCollectionViewCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'SplashMaskCollectionViewCell-1')
    with step("[Action] Tap SplashMaskCollectionViewCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'SplashMaskCollectionViewCell-2')
    with step("[Action] Tap shapeMaskInvertButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskInvertButton')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap reginalAdjustmentButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')
    with step("[Verify] reginalAdjustmentButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'reginalAdjustmentButton'), 'element reginalAdjustmentButton should not be visible'
    with step("[Verify] //*[@name=\"reginalAdjustmentButton\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="reginalAdjustmentButton"]'), 'element //*[@name="reginalAdjustmentButton"] should not be visible'
    with step("[Verify] //*[@label=\"reginalAdjustmentButton\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="reginalAdjustmentButton"]'), 'element //*[@label="reginalAdjustmentButton"] should not be visible'
    with step("[Verify] //*[@value=\"reginalAdjustmentButton\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="reginalAdjustmentButton"]'), 'element //*[@value="reginalAdjustmentButton"] should not be visible'
    with step("[Action] Tap VHSCollectionViewCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'VHSCollectionViewCell-2')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap VHS"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'VHS')
    with step("[Action] Tap brushModeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton')
    with step("[Action] Tap Eraser"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step("[Action] Tap Brush"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    with step("[Action] Tap invertButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'invertButton')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap brushModeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton')
    with step("[Action] Tap edgeDetectionButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'edgeDetectionButton')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap brushModeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton')
    with step("[Action] Tap edgeDetectionButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'edgeDetectionButton')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
