import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_14_01")
def test_test_main_05_14_01(actions: DriverActions):
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
    with step("[Action] Tap Dispersion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dispersion')
    with step("[Action] Tap Dispersion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dispersion')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] Wraparound is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Wraparound'), 'element Wraparound should be visible'
    with step("[Action] Tap Dispersion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dispersion')
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap ic redo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap btn live eraser n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn live eraser n')
    with step("[Verify] btn live eraser n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btn live eraser n'), 'element btn live eraser n should not be visible'
    with step("[Verify] //*[@name=\"btn live eraser n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn live eraser n"]'), 'element //*[@name="btn live eraser n"] should not be visible'
    with step("[Verify] //*[@label=\"btn live eraser n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="btn live eraser n"]'), 'element //*[@label="btn live eraser n"] should not be visible'
    with step("[Verify] //*[@value=\"btn live eraser n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="btn live eraser n"]'), 'element //*[@value="btn live eraser n"] should not be visible'
    with step("[Action] Tap btnMaskSwitch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch')
    with step("[Verify] btn live eraser n is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btn live eraser n'), 'element btn live eraser n should not be visible'
    with step("[Action] Tap Shape"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shape')
    with step("[Action] Tap AnimationGPUDispersionShapeViewCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AnimationGPUDispersionShapeViewCell-1')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap btn_size_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_size_n')
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Direction"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Direction')
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Mode"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mode')
    with step("[Action] Tap Straight"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Straight')
    with step("[Action] Tap Shrink"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shrink')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Stretch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Stretch')
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Fade"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Fade')
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Speed"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Speed')
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap Still Image"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Still Image')
    with step("[Verify] btnSave is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnSave'), 'element btnSave should not be visible'
    with step("[Verify] exportButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'exportButton'), 'element exportButton should be visible'
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Dispersion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dispersion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap Video"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Video')
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap GIF"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'GIF')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Your GIF was exported is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your GIF was exported'), 'element Your GIF was exported should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your animation looks perfect!'), 'element Your animation looks perfect! should be visible'
    with step("[Action] Tap Later"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Action] Tap Video"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Video')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your animation looks perfect!'), 'element Your animation looks perfect! should be visible'
    with step("[Action] Tap Later"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    assert True
