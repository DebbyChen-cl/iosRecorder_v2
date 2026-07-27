import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_11_01_7")
def test_test_main_05_11_01_7(actions: DriverActions):
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
    with step("[Action] Tap btn_add_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n')
    with step("[Action] Tap Add Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step("[Verify] Add Photo is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Add Photo'), 'element Add Photo should not be visible'
    with step("[Verify] //*[@name=\"Add Photo\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Add Photo"]'), 'element //*[@name="Add Photo"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Verify] photoCell-6 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6'), 'element photoCell-6 should be visible'
    with step("[Action] Tap photoCell-6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step("[Action] Tap btn layer n"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn layer n')
    with step("[Verify] btn layer n is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btn layer n'), 'element btn layer n should not be visible'
    with step("[Verify] //*[@name=\"btn layer n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn layer n"]'), 'element //*[@name="btn layer n"] should not be visible'
    with step("[Verify] layerButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'layerButton'), 'element layerButton should be visible'
    with step("[Action] Tap btnLayerDown"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnLayerDown')
    with step("[Action] Tap btnLayerUp"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnLayerUp')
    with step("[Action] Tap btnDelete"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step("[Action] Tap btn_add_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n')
    with step("[Action] Tap Add Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step("[Verify] Add Photo is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Add Photo'), 'element Add Photo should not be visible'
    with step("[Verify] //*[@name=\"Add Photo\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Add Photo"]'), 'element //*[@name="Add Photo"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
    with step("[Action] Tap btnCamera"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCamera')
    with step("[Action] Tap PhotoCapture"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoCapture')
    with step("[Action] Tap Use Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use Photo')
    with step("[Action] Tap btn_add_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n')
    with step("[Action] Tap Add Sticker"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Sticker')
    with step("[Verify] Add Sticker is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Add Sticker'), 'element Add Sticker should not be visible'
    with step("[Verify] //*[@name=\"Add Sticker\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Add Sticker"]'), 'element //*[@name="Add Sticker"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
    with step("[Action] Tap at (45, 680)"):
        actions.tap_by_coordinates(45, 680)
    assert True
