import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_11_01_4")
def test_test_main_05_11_01_4(actions: DriverActions):
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
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap Add Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step("[Action] Tap Add Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Verify] photoCell-0 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0'), 'element photoCell-0 should be visible'
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Drag (0,0) → (0,0)"):
        actions.drag_coordinates(0, 0, 0, 0, duration=1.0)
    with step("[Action] Tap Blending mode"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blending mode')
    with step("[Verify] Blending mode is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Blending mode'), 'element Blending mode should not be visible'
    with step("[Verify] //*[@name=\"Blending mode\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Blending mode"]'), 'element //*[@name="Blending mode"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
    with step("[Action] Tap Overlay"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Overlay')
    with step("[Action] Tap Multiply"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Multiply')
    with step("[Action] Tap Screen"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Screen')
    with step("[Action] Tap Hardlight"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hardlight')
    with step("[Verify] Screen is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Screen'), 'element Screen should be visible'
    with step("[Verify] Multiply is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Multiply'), 'element Multiply should be visible'
    with step("[Action] Drag Screen (50.0%,50.0%) → Multiply (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Screen', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Multiply', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Softlight"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Softlight')
    assert True
