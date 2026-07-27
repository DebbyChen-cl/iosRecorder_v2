import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_08_01_n6")
def test_test_main_05_08_01_n6(actions: DriverActions):
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
    with step("[Action] Tap Style"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step("[Action] Tap Border"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Border')
    with step("[Action] Tap leaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step("[Action] Tap at (205, 455)"):
        actions.tap_by_coordinates(205, 455)
    with step("[Action] Tap Style"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step("[Action] Tap Border"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Border')
    with step("[Action] Tap ColorSelectionViewColorCell-7"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-7')
    with step("[Action] Tap cellImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cellImageView')
    with step("[Action] Tap at (250, 720)"):
        actions.tap_by_coordinates(250, 720)
    with step("[Action] Tap colorPickerButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    with step("[Action] Tap cancelButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step("[Action] Tap cellImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cellImageView')
    with step("[Action] Tap at (250, 720)"):
        actions.tap_by_coordinates(250, 720)
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step("[Action] Tap Border 2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Border 2')
    with step("[Action] Tap ColorSelectionViewColorCell-9"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-9')
    with step("[Action] Tap cellImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cellImageView')
    with step("[Action] Tap at (331, 600)"):
        actions.tap_by_coordinates(331, 600)
    with step("[Action] Tap colorPickerButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorPickerButton')
    with step("[Action] Tap cancelButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step("[Action] Tap cellImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cellImageView')
    with step("[Action] Tap at (331, 600)"):
        actions.tap_by_coordinates(331, 600)
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    assert True
