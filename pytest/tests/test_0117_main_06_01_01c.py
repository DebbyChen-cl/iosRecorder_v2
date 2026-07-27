import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_06_01_01c")
def test_test_main_06_01_01c(actions: DriverActions):
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
    with step("[Verify] Auto is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Auto'), 'element Auto should be visible'
    with step("[Action] Tap btn_reset_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n')
    with step("[Action] Tap Circle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Circle')
    with step("[Action] Tap Brush"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Action] Tap Eraser"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step("[Action] Tap Auto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step("[Action] Tap Cutout"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step("[Action] Tap btn edit n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn edit n')
    with step("[Verify] Auto is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Auto'), 'element Auto should be visible'
    with step("[Action] Tap Eraser"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap Cutout"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step("[Action] Tap Auto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step("[Action] Tap Cutout"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cutout')
    with step("[Action] Tap **/XCUIElementTypeOther[`name == \"cutout_with_design\"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]')
    with step("[Verify] **/XCUIElementTypeOther[`name == \"cutout_with_design\"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5] is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, '**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]'), 'element **/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5] should not be visible'
    with step("[Verify] **/XCUIElementTypeOther[`name == \"cutout_with_design\"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5] is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, '**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]'), 'element **/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5] should not be visible'
    with step("[Verify] //*[@name=\"**/XCUIElementTypeOther[`name == \"cutout_with_design\"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]"]'), 'element //*[@name="**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]"] should not be visible'
    with step("[Verify] //*[@label=\"**/XCUIElementTypeOther[`name == \"cutout_with_design\"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]"]'), 'element //*[@label="**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]"] should not be visible'
    with step("[Verify] //*[@value=\"**/XCUIElementTypeOther[`name == \"cutout_with_design\"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]"]'), 'element //*[@value="**/XCUIElementTypeOther[`name == "cutout_with_design"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell[5]"] should not be visible'
    assert False, "original pytest run failed — this recording reproduces a failing run"
