import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_07_03_2")
def test_test_main_05_07_03_2(actions: DriverActions):
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap ScrollableMenuViewCell-Portrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step("[Action] Tap Beautify"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step("[Action] Tap Smooth"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Smooth')
    with step("[Action] Tap Auto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step("[Verify] No faces were detected. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'No faces were detected.'), 'element No faces were detected. should be visible'
    with step("[Action] Tap Add Face"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Face')
    with step("[Verify] Drag to move the crosses over the eyes and lips. is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Drag to move the crosses over the eyes and lips.'), 'element Drag to move the crosses over the eyes and lips. should not be visible'
    with step("[Action] Tap at (205, 401)"):
        actions.tap_by_coordinates(205, 401)
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Action] Tap Auto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Smooth"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Smooth')
    with step("[Action] Tap Auto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step("[Action] Tap Add Face"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Face')
    with step("[Verify] Add Face is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Add Face'), 'element Add Face should not be visible'
    with step("[Verify] //*[@name=\"Add Face\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Add Face"]'), 'element //*[@name="Add Face"] should not be visible'
    with step("[Verify] //*[@label=\"Add Face\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="Add Face"]'), 'element //*[@label="Add Face"] should not be visible'
    with step("[Verify] //*[@value=\"Add Face\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="Add Face"]'), 'element //*[@value="Add Face"] should not be visible'
    with step("[Action] Tap at (205, 401)"):
        actions.tap_by_coordinates(205, 401)
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeOther')
    with step("[Action] Tap **/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage/XCUIElementTypeOther"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage/XCUIElementTypeOther')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
