import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_collage_edit")
def test_test_collage_edit(actions: DriverActions):
    with step("[Action] Tap More"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'More')
    with step("[Action] Tap Collage"):
        actions.tap_by_locator(AppiumBy.NAME, 'Collage')
    with step("[Action] Tap Collage"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step("[Action] Tap btn2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn2')
    with step("[Action] Tap at (70, 280)"):
        actions.tap_by_coordinates(70, 280)
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap at (390, 767)"):
        actions.tap_by_coordinates(390, 767)
    with step("[Action] Tap at (384, 781)"):
        actions.tap_by_coordinates(384, 781)
    with step("[Action] Tap at (205, 300)"):
        actions.tap_by_coordinates(205, 300)
    with step("[Action] Tap Replace"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace')
    with step("[Verify] Replace is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Replace'), 'element Replace should not be visible'
    with step("[Verify] //*[@name=\"Replace\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Replace"]'), 'element //*[@name="Replace"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
    with step("[Action] Tap btnCamera"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCamera')
    with step("[Action] Tap PhotoCapture"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoCapture')
    with step("[Action] Tap Use Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use Photo')
    with step("[Action] Tap Replace"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace')
    with step("[Verify] Replace is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Replace'), 'element Replace should not be visible'
    with step("[Verify] //*[@name=\"Replace\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Replace"]'), 'element //*[@name="Replace"] should not be visible'
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
    with step("[Action] Tap AddImageCollagePhotoPanelCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AddImageCollagePhotoPanelCell-1')
    with step("[Action] Tap AddImageCollagePhotoPanelCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AddImageCollagePhotoPanelCell-2')
    with step("[Action] Tap AddImageCollagePhotoPanelCell-3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AddImageCollagePhotoPanelCell-3')
    with step("[Action] Tap Auto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step("[Action] Tap Auto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Contrast"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Contrast')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Highlight"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Highlight')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Bright"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Bright')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Midtone"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Midtone')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Dark"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dark')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Shadow"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step("[Action] Tap Auto Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto Color')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Saturation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Saturation')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Details"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Details')
    with step("[Action] Tap Sharpness"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sharpness')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Color"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step("[Action] Tap Temperature"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Temperature')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap btnUndo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnUndo')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap Curve"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Curve')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap HSL"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HSL')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap Filter"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Filter')
    with step("[Verify] Filter is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Filter'), 'element Filter should not be visible'
    with step("[Verify] //*[@name=\"Filter\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Filter"]'), 'element //*[@name="Filter"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
    with step("[Action] Tap at (180, 779)"):
        actions.tap_by_coordinates(180, 779)
    assert True
