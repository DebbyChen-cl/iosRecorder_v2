import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_11_01_1")
def test_test_main_05_11_01_1(actions: DriverActions):
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
    with step("[Verify] photoCell-1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1'), 'element photoCell-1 should be visible'
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Verify] EditViewControllerBottomBarCollectionView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView'), 'element EditViewControllerBottomBarCollectionView should be visible'
    with step("[Action] Tap Add Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Verify] photoCell-1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1'), 'element photoCell-1 should be visible'
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Action] Drag (0,0) → (0,0)"):
        actions.drag_coordinates(0, 0, 0, 0, duration=1.0)
    with step("[Action] Tap btnFlip"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFlip')
    with step("[Action] Tap Opacity"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Opacity')
    with step("[Verify] Opacity is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Opacity'), 'element Opacity should not be visible'
    with step("[Verify] //*[@name=\"Opacity\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Opacity"]'), 'element //*[@name="Opacity"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap Add Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step("[Action] Tap btnCamera"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCamera')
    with step("[Action] Tap PhotoCapture"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoCapture')
    with step("[Action] Tap Use Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use Photo')
    assert True
