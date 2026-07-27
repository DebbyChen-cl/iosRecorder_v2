import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_15_01")
def test_test_main_05_15_01(actions: DriverActions):
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
    with step("[Action] Tap Cloudy 1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cloudy 1')
    with step("[Action] Tap 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')
    with step("[Action] Tap at (220, 220)"):
        actions.tap_by_coordinates(220, 220)
    with step("[Action] Tap at (220, 220)"):
        actions.tap_by_coordinates(220, 220)
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
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap btnMaskSwitch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch')
    with step("[Action] Tap CMS-sky_static_cloudy1_01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-sky_static_cloudy1_01')
    with step("[Action] Tap Feather"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feather')
    with step("[Action] Tap Horizon"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Horizon')
    with step("[Action] Tap Land Ambient"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Land Ambient')
    with step("[Action] Tap HDR Glow"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HDR Glow')
    with step("[Action] Tap HDR Edge"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HDR Edge')
    with step("[Action] Tap Sky Fade"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sky Fade')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] 01 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '01'), 'element 01 should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] Wraparound is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Wraparound'), 'element Wraparound should be visible'
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Verify] Tap to draw motion arrows on areas that you want to animate. is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Tap to draw motion arrows on areas that you want to animate.'), 'element Tap to draw motion arrows on areas that you want to animate. should not be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap btn_sky_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_sky_n')
    with step("[Action] Tap CMS-static_sky_category_cloudy1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-static_sky_category_cloudy1')
    with step("[Action] Tap Cloudy 2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cloudy 2')
    with step("[Action] Tap 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')
    with step("[Verify] UNLOCK TO is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'UNLOCK TO'), 'element UNLOCK TO should be visible'
    with step("[Action] Tap Premium"):
        actions.tap_by_locator(AppiumBy.NAME, 'Premium')
    with step("[Action] Tap UNLOCK TO"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'UNLOCK TO')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    assert True
