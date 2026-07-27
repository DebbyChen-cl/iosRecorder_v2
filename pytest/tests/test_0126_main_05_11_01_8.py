import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_11_01_8")
def test_test_main_05_11_01_8(actions: DriverActions):
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
    with step("[Action] Tap btn_add_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n')
    with step("[Action] Tap Add Text"):
        actions.tap_by_locator(AppiumBy.NAME, 'Add Text')
    with step("[Verify] Add Text is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Add Text'), 'element Add Text should not be visible'
    with step("[Verify] //*[@name=\"Add Text\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Add Text"]'), 'element //*[@name="Add Text"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
    with step("[Action] Drag rotateImageView (50.0%,50.0%) → 350 (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'rotateImageView', 50.0, 50.0, AppiumBy.XPATH, '350', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Font"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Font')
    with step("[Action] Tap TextFontCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'TextFontCell-1')
    with step("[Action] Tap Style"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step("[Action] Tap Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step("[Action] Tap ColorSelectionViewColorCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-5')
    with step("[Action] Tap Style"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style')
    with step("[Action] Tap Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step("[Action] Tap Gradient"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Gradient')
    with step("[Action] Tap ColorSelectionViewGradientCell-4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewGradientCell-4')
    with step("[Action] Tap Format"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Format')
    with step("[Action] Tap boldButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'boldButton')
    with step("[Action] Tap Border"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Border')
    with step("[Action] Tap ColorSelectionViewColorCell-7"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-7')
    with step("[Action] Tap Shadow"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')
    with step("[Action] Tap ColorSelectionViewColorCell-8"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-8')
    with step("[Action] Tap leaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step("[Action] Tap btn_add_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n')
    with step("[Action] Tap Add Text Bubble"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Text Bubble')
    with step("[Verify] Add Text Bubble is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Add Text Bubble'), 'element Add Text Bubble should not be visible'
    with step("[Verify] //*[@name=\"Add Text Bubble\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Add Text Bubble"]'), 'element //*[@name="Add Text Bubble"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
    with step("[Action] Tap Font"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Font')
    with step("[Action] Tap TextFontCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'TextFontCell-1')
    with step("[Action] Tap leaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step("[Action] Tap Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step("[Action] Tap ColorSelectionViewColorCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-5')
    with step("[Action] Tap leaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    assert True
