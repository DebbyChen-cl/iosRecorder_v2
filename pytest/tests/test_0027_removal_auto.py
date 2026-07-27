import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_removal_auto")
def test_test_removal_auto(actions: DriverActions):
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Verify] Undo / Redo is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Undo / Redo'), 'element Undo / Redo should not be visible'
    with step("[Verify] Find Animated Decor, Sky, Light rays, Bokeh, Sparkle, Animation & Dispersion effects here. is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Find Animated Decor, Sky, Light rays, Bokeh, Sparkle, Animation & Dispersion effects here.'), 'element Find Animated Decor, Sky, Light rays, Bokeh, Sparkle, Animation & Dispersion effects here. should not be visible'
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap AI Removal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')
    with step("[Verify] Remove with faster selection tool is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Remove with faster selection tool'), 'element Remove with faster selection tool should be visible'
    with step("[Verify] Remove with faster selection tool is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Remove with faster selection tool'), 'element Remove with faster selection tool should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Verify] Remove with faster selection tool is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Remove with faster selection tool'), 'element Remove with faster selection tool should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Verify] Try First is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Try First'), 'element Try First should be visible'
    with step("[Action] Tap Try First"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step("[Verify] Try First is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Try First'), 'element Try First should not be visible'
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap redoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'redoButton')
    with step("[Action] Tap applyButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'applyButton')
    with step("[Verify] magicText is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'magicText'), 'element magicText should not be visible'
    with step("[Action] Tap redoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'redoButton')
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap resetButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'resetButton')
    with step("[Action] Tap Circle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Circle')
    with step("[Action] Tap applyButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'applyButton')
    with step("[Verify] magicText is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'magicText'), 'element magicText should not be visible'
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap resetButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'resetButton')
    with step("[Action] Tap Swipe"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Swipe')
    with step("[Action] Tap applyButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'applyButton')
    with step("[Verify] magicText is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'magicText'), 'element magicText should not be visible'
    assert True
