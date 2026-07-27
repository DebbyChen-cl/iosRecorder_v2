import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_01_12_6")
def test_test_main_05_01_12_6(actions: DriverActions):
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
    with step("[Action] Tap BG"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'BG')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap Quick Actions"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
    with step("[Verify] Try First is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Try First'), 'element Try First should not be visible'
    with step("[Verify] waitingTitle is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle'), 'element waitingTitle should not be visible'
    with step("[Action] Tap Presets"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Presets')
    with step("[Action] Tap Food"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Food')
    with step("[Action] Tap Food 02"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Food 02')
    with step("[Action] Tap Food 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Food 01')
    with step("[Action] Tap Food 03"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Food 03')
    with step("[Action] Tap Food 04"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Food 04')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap photoPickerButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton')
    with step("[Action] Tap photoCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step("[Verify] Try First is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Try First'), 'element Try First should be visible'
    with step("[Action] Tap Try First"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step("[Verify] Try First is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Try First'), 'element Try First should not be visible'
    with step("[Action] Tap Presets"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Presets')
    with step("[Action] Tap Indoor"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Indoor')
    with step("[Action] Tap Indoor 02"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Indoor 02')
    with step("[Action] Tap Indoor 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Indoor 01')
    with step("[Action] Tap Indoor 03"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Indoor 03')
    with step("[Action] Tap Indoor 05"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Indoor 05')
    with step("[Action] Tap Indoor 06"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Indoor 06')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap photoPickerButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton')
    with step("[Action] Tap photoCell-3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3')
    with step("[Verify] Try First is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Try First'), 'element Try First should not be visible'
    with step("[Action] Tap Presets"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Presets')
    with step("[Action] Tap Outdoor"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor')
    with step("[Action] Tap Outdoor 02"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 02')
    with step("[Action] Tap Outdoor 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 01')
    with step("[Action] Tap Outdoor 03"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 03')
    with step("[Action] Tap Outdoor 04"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 04')
    with step("[Action] Tap Outdoor 05"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 05')
    with step("[Action] Tap Outdoor 06"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 06')
    with step("[Action] Tap Outdoor 07"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 07')
    with step("[Action] Tap Outdoor 08"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 08')
    with step("[Action] Tap Outdoor 09"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 09')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap photoPickerButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Verify] Try First is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Try First'), 'element Try First should not be visible'
    with step("[Action] Tap Presets"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Presets')
    with step("[Action] Tap Scenery"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery')
    with step("[Action] Tap Scenery 02"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 02')
    with step("[Action] Tap Scenery 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 01')
    with step("[Action] Tap Scenery 03"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 03')
    with step("[Action] Tap Scenery 04"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 04')
    with step("[Action] Tap Scenery 05"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 05')
    with step("[Action] Tap Scenery 06"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 06')
    with step("[Action] Tap Scenery 07"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 07')
    with step("[Action] Tap Scenery 08"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 08')
    with step("[Action] Tap Scenery 09"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 09')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Presets"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Presets')
    with step("[Action] Tap General"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'General')
    with step("[Action] Tap General 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'General 01')
    with step("[Action] Tap General 02"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'General 02')
    with step("[Action] Tap General 03"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'General 03')
    assert True
