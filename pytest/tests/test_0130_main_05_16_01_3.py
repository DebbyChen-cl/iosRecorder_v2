import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_16_01_3")
def test_test_main_05_16_01_3(actions: DriverActions):
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
    with step("[Action] Tap Animated Overlays"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animated Overlays')
    with step("[Action] Tap CMS-Effect_2021_Angel_cloud_fly"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-Effect_2021_Angel_cloud_fly')
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap CMS-Effect_2021_Rainbow_A"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-Effect_2021_Rainbow_A')
    with step("[Action] Tap btnMaskSwitch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch')
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap ic redo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Action] Tap btn live brush n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn live brush n')
    with step("[Verify] btn live brush n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn live brush n'), 'element btn live brush n should not be visible'
    with step("[Verify] //*[@name=\"btn live brush n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn live brush n"]'), 'element //*[@name="btn live brush n"] should not be visible'
    with step("[Verify] //*[@label=\"btn live brush n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="btn live brush n"]'), 'element //*[@label="btn live brush n"] should not be visible'
    with step("[Verify] //*[@value=\"btn live brush n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="btn live brush n"]'), 'element //*[@value="btn live brush n"] should not be visible'
    with step("[Action] Tap btn mask switch n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn mask switch n')
    with step("[Verify] btn mask switch n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn mask switch n'), 'element btn mask switch n should not be visible'
    with step("[Verify] //*[@name=\"btn mask switch n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn mask switch n"]'), 'element //*[@name="btn mask switch n"] should not be visible'
    with step("[Verify] btnMaskSwitch is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch'), 'element btnMaskSwitch should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Wraparound"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Wraparound')
    assert True
