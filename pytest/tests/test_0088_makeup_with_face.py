import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_makeup_with_face")
def test_test_makeup_with_face(actions: DriverActions):
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
    with step("[Action] Tap ScrollableMenuViewCell-Portrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step("[Action] Tap Beautify"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step("[Action] Tap Makeup"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Makeup')
    with step("[Action] Tap Lipstick"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lipstick')
    with step("[Action] Tap Dried Rose 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dried Rose 01')
    with step("[Action] Tap CMS-Gloss"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-Gloss')
    with step("[Action] Tap Contour"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Contour')
    with step("[Action] Tap Highlight"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Highlight')
    with step("[Action] Tap Eyelashes"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyelashes')
    with step("[Action] Tap Daily"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')
    with step("[Action] Tap CMS-eyelash_color_orange"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-eyelash_color_orange')
    with step("[Action] Tap Eyebrows"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyebrows')
    with step("[Action] Tap Daily"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')
    with step("[Action] Tap CMS-eyebrow_color_dusty_pink"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-eyebrow_color_dusty_pink')
    with step("[Action] Tap Eyeliner"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyeliner')
    with step("[Action] Tap Daily"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')
    with step("[Action] Tap CMS-eyeliner_color_pink"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-eyeliner_color_pink')
    with step("[Action] Tap Eye Shadow"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Shadow')
    with step("[Action] Tap Daily"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')
    with step("[Action] Tap Blush"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blush')
    with step("[Action] Tap Natural"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Natural')
    with step("[Action] Tap Foundation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Foundation')
    with step("[Action] Tap White 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'White 01')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap btnRedo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRedo')
    with step("[Action] Tap redoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'redoButton')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] Discard is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Discard'), 'element Discard should not be visible'
    with step("[Verify] //*[@name=\"Discard\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Discard"]'), 'element //*[@name="Discard"] should not be visible'
    with step("[Verify] //*[@label=\"Discard\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="Discard"]'), 'element //*[@label="Discard"] should not be visible'
    with step("[Verify] //*[@value=\"Discard\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="Discard"]'), 'element //*[@value="Discard"] should not be visible'
    assert True
