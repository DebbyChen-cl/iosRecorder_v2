import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_06_02_01")
def test_test_main_06_02_01(actions: DriverActions):
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
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] Wraparound is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Wraparound'), 'element Wraparound should be visible'
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap ic redo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Action] Tap Anchor"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Anchor')
    with step("[Action] Tap at (223, 223)"):
        actions.tap_by_coordinates(223, 223)
    with step("[Action] Tap at (271, 305)"):
        actions.tap_by_coordinates(271, 305)
    with step("[Action] Tap at (163, 256)"):
        actions.tap_by_coordinates(163, 256)
    with step("[Action] Tap at (142, 284)"):
        actions.tap_by_coordinates(142, 284)
    with step("[Action] Tap at (126, 314)"):
        actions.tap_by_coordinates(126, 314)
    with step("[Action] Tap at (107, 444)"):
        actions.tap_by_coordinates(107, 444)
    with step("[Action] Tap at (179, 499)"):
        actions.tap_by_coordinates(179, 499)
    with step("[Action] Tap at (231, 710)"):
        actions.tap_by_coordinates(231, 710)
    with step("[Action] Tap at (329, 661)"):
        actions.tap_by_coordinates(329, 661)
    with step("[Action] Tap at (303, 586)"):
        actions.tap_by_coordinates(303, 586)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap ic redo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Action] Tap Freeze"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Freeze')
    with step("[Action] Tap btnPlay"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap ic redo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Action] Tap btnMaskSwitch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch')
    with step("[Action] Tap btnErase"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnErase')
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap ic redo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Action] Tap Speed"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Speed')
    with step("[Action] Tap Delete"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Delete')
    with step("[Action] Tap at (60, 300)"):
        actions.tap_by_coordinates(60, 300)
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap ic redo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Action] Tap at (107, 444)"):
        actions.tap_by_coordinates(107, 444)
    with step("[Action] Tap ic undo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap ic redo"):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap at (401, 723)"):
        actions.tap_by_coordinates(401, 723)
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    assert True
