import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_08_01_n3")
def test_test_main_05_08_01_n3(actions: DriverActions):
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
    with step("[Verify] xpromo btn close n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'xpromo btn close n'), 'element xpromo btn close n should not be visible'
    with step("[Action] Tap Text"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step("[Action] Tap Text"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step("[Action] Tap btnTextEdit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTextEdit')
    with step("[Action] Tap A"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'A')
    with step("[Action] Tap a"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'a')
    with step("[Action] Tap a"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'a')
    with step("[Action] Tap Return"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Return')
    with step("[Action] Tap A"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'A')
    with step("[Action] Tap btn top done n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn top done n')
    with step("[Verify] btn top done n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn top done n'), 'element btn top done n should not be visible'
    with step("[Verify] //*[@name=\"btn top done n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn top done n"]'), 'element //*[@name="btn top done n"] should not be visible'
    with step("[Verify] applyButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'applyButton'), 'element applyButton should be visible'
    with step("[Action] Tap Style"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step("[Action] Tap Format"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Format')
    with step("[Action] Tap leaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step("[Action] Tap at (205, 455)"):
        actions.tap_by_coordinates(205, 455)
    with step("[Action] Tap Style"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step("[Action] Tap Format"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Format')
    with step("[Action] Tap alignLeftButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'alignLeftButton')
    with step("[Action] Tap alignRightButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'alignRightButton')
    with step("[Action] Tap alignCenterButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'alignCenterButton')
    with step("[Action] Tap boldButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'boldButton')
    with step("[Action] Tap italicButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'italicButton')
    assert True
