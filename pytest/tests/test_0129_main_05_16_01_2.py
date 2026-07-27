import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_16_01_2")
def test_test_main_05_16_01_2(actions: DriverActions):
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
    with step("[Action] Tap Wraparound"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Wraparound')
    with step("[Action] Tap CMS-phdm_wraparound_vday01_220126"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_wraparound_vday01_220126')
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap CMS-phdm_wraparound_vday02_220126"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_wraparound_vday02_220126')
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap CMS-phdm_wraparound_vday01_220126"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_wraparound_vday01_220126')
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap btnFlip"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFlip')
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap btnDelete"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    assert True
