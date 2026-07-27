import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_16_01_1")
def test_test_main_05_16_01_1(actions: DriverActions):
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
    with step("[Verify] Complete your photo edits before applying animated effects. is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Complete your photo edits before applying animated effects.'), 'element Complete your photo edits before applying animated effects. should not be visible'
    with step("[Action] Tap Elements"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Elements')
    with step("[Action] Tap at (160, 666)"):
        actions.tap_by_coordinates(160, 666)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap **/XCUIElementTypeButton[`label == \"btnUndo\"`][2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeButton[`label == "btnUndo"`][2]')
    with step("[Action] Tap btnFlip"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFlip')
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap btnDelete"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step("[Action] Tap at (160, 750)"):
        actions.tap_by_coordinates(160, 750)
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap at (160, 666)"):
        actions.tap_by_coordinates(160, 666)
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap **/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton')
    with step("[Verify] **/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton'), 'element **/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton should not be visible'
    with step("[Verify] **/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton'), 'element **/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton should not be visible'
    with step("[Verify] //*[@name=\"**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton"]'), 'element //*[@name="**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton"] should not be visible'
    with step("[Verify] //*[@label=\"**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton"]'), 'element //*[@label="**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton"] should not be visible'
    with step("[Verify] //*[@value=\"**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton"]'), 'element //*[@value="**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton"] should not be visible'
    with step("[Action] Tap Wraparound"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Wraparound')
    assert True
