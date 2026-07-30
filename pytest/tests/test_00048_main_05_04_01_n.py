import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00048_main_05_04_01_n')
def test_00048_main_05_04_01_n(actions: DriverActions):
    """look / filter custom"""
    mode = 1
    uuid = ['9d516a63-9272-49de-9d6f-3b10181382e2', 'bebc7fd0-740d-4cbb-941b-6c0cbbf668c6', '354896a6-3d01-4251-b2d9-00988f631429', '398a6181-0e27-48d2-9d8c-06cdac297c4c', 'f9081a1b-1cce-4a21-b42b-30313ad583f3', '04c9b1d6-3132-4358-9fcc-8cea0a936f16', '9362b6c0-d8f0-490c-aee7-100636a633f2']
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_enhance1_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    with step('[Verify] snapshot: 05_04_01_no_look.png'):
        actions.capture_for_gt('05_04_01_no_look.png', crop_rect=(0, 60, 276, 400))
    with step('[Action] tap_effect_filter'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Filter')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-UserImageItem1')
    if actions.is_element_present(AppiumBy.NAME, 'Stock'):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step('[Verify] snapshot: base05_04_01_apply_custom.png'):
        actions.capture_for_gt('base05_04_01_apply_custom.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_fisheye_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)
    with step('[Action] adjust_fisheye_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)
    with step('[Verify] snapshot: base05_04_01_custom_min.png'):
        actions.capture_for_gt('base05_04_01_custom_min.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_fisheye_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)
    with step('[Verify] snapshot: base05_04_01_custom_max.png'):
        actions.capture_for_gt('base05_04_01_custom_max.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] snapshot: 05_04_01_custom_filter_list.png'):
        actions.capture_for_gt('05_04_01_custom_filter_list.png', crop_rect=(0, 700, 276, 850))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Filter')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-UserImageItem2')
    with step('[Verify] snapshot: 05_04_01_custom_filter_list_2.png'):
        actions.capture_for_gt('05_04_01_custom_filter_list_2.png', crop_rect=(0, 700, 276, 850))
    with step('[Verify] snapshot: 05_04_01_v.png'):
        actions.capture_for_gt('05_04_01_v.png', crop_rect=(0, 60, 276, 400))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04_01_v_undo.png'):
        actions.capture_for_gt('base05_04_01_v_undo.png', crop_rect=(0, 60, 276, 429))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04_01_v_redo.png'):
        actions.capture_for_gt('base05_04_01_v_redo.png', crop_rect=(0, 60, 276, 429))
    with step("[Verify] test_00048 completion"):
        assert True
