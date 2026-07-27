import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_06_01_01c_2")
def test_test_main_06_01_01c_2(actions: DriverActions):
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
    with step("[Action] Tap Cutout"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step("[Action] Tap Auto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step("[Action] Tap Cutout"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step("[Action] Tap **/XCUIElementTypeOther[`name == \"cutout_with_design\"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[1]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[1]')
    with step("[Action] Tap Stroke"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Stroke')
    with step("[Action] Tap stroke_thumb_6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_6')
    with step("[Action] Tap ColorSelectionViewColorCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-2')
    with step("[Action] Tap stroke_thumb_2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_2')
    with step("[Action] Tap ColorSelectionViewColorCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-5')
    with step("[Action] Tap stroke_thumb_3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_3')
    with step("[Action] Tap ColorSelectionViewColorCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-5')
    with step("[Action] Tap stroke_thumb_1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_1')
    with step("[Action] Tap ColorSelectionViewColorCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-5')
    with step("[Action] Tap stroke_thumb_4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_4')
    with step("[Action] Tap ColorSelectionViewColorCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-5')
    with step("[Action] Tap stroke_thumb_7"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_7')
    with step("[Action] Tap ColorSelectionViewColorCell-6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-6')
    with step("[Action] Tap stroke_thumb_5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_5')
    with step("[Action] Tap ColorSelectionViewColorCell-7"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ColorSelectionViewColorCell-7')
    with step("[Action] Tap btn edit n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn edit n')
    with step("[Action] Tap Eraser"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step("[Action] Tap Brush"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    assert True
