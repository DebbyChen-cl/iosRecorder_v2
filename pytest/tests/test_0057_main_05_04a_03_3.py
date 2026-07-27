import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_04a_03_3")
def test_test_main_05_04a_03_3(actions: DriverActions):
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
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap Mosaic"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mosaic')
    with step("[Action] Tap Mosaic"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mosaic')
    with step("[Action] Tap Person"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Person')
    with step("[Action] Tap mosaic_blur"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_blur')
    with step("[Action] Tap mosaic_glass"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_glass')
    with step("[Action] Tap mosaic_brush"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_brush')
    with step("[Action] Tap mosaic_circle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_circle')
    with step("[Action] Tap mosaic_line"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_line')
    with step("[Action] Tap mosaic_glass_tile"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_glass_tile')
    with step("[Action] Tap mosaic_triangle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_triangle')
    with step("[Action] Tap mosaic_diamond"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_diamond')
    with step("[Action] Tap mosaic_tiles"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_tiles')
    assert True
