import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00072_main_05_07_09_1')
def test_00072_main_05_07_09_1(actions: DriverActions):
    """blemish, have face"""
    mode = 1
    uuid = ['31bfbf01-db16-4c8d-bdad-f4a97cd9009c', '2d999a48-dcd9-4b26-a0ce-b2a6174ee039', '7016e229-9596-4305-9bdd-2cfdfa426f4e', '5fc290e0-ed66-4c83-9736-a725c19bc542', '2928cbdd-9746-439c-80cd-f71b47e1e256', '35fb1e18-155c-4d7f-8901-1f7b315e7a25', 'f554fcfa-a313-48b5-ad73-d4a9218f2230']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Verify] snapshot: 05_07_09_before_blemish.png'):
        actions.capture_for_gt('05_07_09_before_blemish.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blemish')
    with step('[Verify] snapshot: base05_07_09_on.png'):
        actions.capture_for_gt('base05_07_09_on.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_09_on.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Blemish on fail'
    with step('[Verify] snapshot: 05_07_09_undo_og.png'):
        actions.capture_for_gt('05_07_09_undo_og.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Toggle on withoutText')
    with step('[Verify] snapshot: base05_07_09_off.png'):
        actions.capture_for_gt('base05_07_09_off.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_09_off.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Blemish off fail'
    with step('[Verify] snapshot: 05_07_09_before_undo.png'):
        actions.capture_for_gt('05_07_09_before_undo.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_09_undo.png'):
        actions.capture_for_gt('05_07_09_undo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_09_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_09_redo.png'):
        actions.capture_for_gt('05_07_09_redo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_09_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap [v] fail'
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, '[v] fail'
    with step("[Verify] test_00072 completion"):
        assert True
