import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_15_02")
def test_test_main_05_15_02(actions: DriverActions):
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
    with step("[Action] Tap btn_sky_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_sky_n')
    with step("[Action] Tap Aurora"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Aurora')
    with step("[Action] Tap 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')
    with step("[Action] Tap 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')
    with step("[Action] Tap Feather"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feather')
    with step("[Action] Tap Horizon"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Horizon')
    with step("[Action] Tap Land Ambient"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Land Ambient')
    with step("[Action] Tap Sky Fade"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sky Fade')
    with step("[Action] Tap Speed"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Speed')
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] 01 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '01'), 'element 01 should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Wraparound"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Wraparound')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap Still Image"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Still Image')
    with step("[Verify] btnSave is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnSave'), 'element btnSave should not be visible'
    with step("[Verify] exportButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'exportButton'), 'element exportButton should be visible'
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Action] Tap btn_sky_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_sky_n')
    with step("[Action] Tap Aurora"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Aurora')
    with step("[Action] Tap 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap Video"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Video')
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    assert True
