import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00183_motion_swap_02')
def test_00183_motion_swap_02(actions: DriverActions):
    """Motion Swap"""
    with step('Close any popups'):
        with step('[Action] close_xmas'):
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Close', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Close')
        with step('[Action] close_continue_edit'):
            if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_character_motion_swap_entry'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Character Motion Swap')
    with step('[Action] tap_import_photo'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step('[Action] tap_continue'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    category = '_AT'
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step('[Action] tap_import_video'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference')
    with step('[Action] tap_continue'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] select_video'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collections')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_Video')
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "PXGGridLayout-Info"`][1]')
    with step('[Action] tap_choose_video'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Choose')
    with step('[Action] adjust_trim_edges'):
        _sx, _sy, _sw, _sh = actions.get_element_bounds(AppiumBy.ACCESSIBILITY_ID, 'startBarImageView')
        _ex, _ey, _ew, _eh = actions.get_element_bounds(AppiumBy.ACCESSIBILITY_ID, 'endBarImageView')
        actions.drag_coordinates(_sx + _sw // 2, _sy + _sh // 2, _sx + _sw // 2 + 20, _sy + _sh // 2)
        actions.drag_coordinates(_ex + _ew // 2, _ey + _eh // 2, _ex + _ew // 2 - 50, _ey + _eh // 2)
    with step('[Action] move_trim_range'):
        _tx, _ty, _tw, _th = actions.get_element_bounds(AppiumBy.ACCESSIBILITY_ID, 'slidingWindow')
        actions.drag_coordinates(_tx + _tw // 2, _ty + _th // 2, _tx + _tw // 2 + 15, _ty + _th // 2)
    with step('[Action] tap_continue'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] tap_keep_photo_background'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Keep the photo background')
    with step('[Action] tap_generate'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] verify_my_artwork_processing'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Character Motion Swap')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing')
    with step("[Verify] test_00183 completion"):
        assert True
