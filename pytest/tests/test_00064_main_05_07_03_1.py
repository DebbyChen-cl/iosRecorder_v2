import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00064_main_05_07_03_1')
def test_00064_main_05_07_03_1(actions: DriverActions):
    """face smoother, have face"""
    mode = 1
    uuid = ['22b74bf7-8d4a-4217-808b-0a4a80e5760d', '68080dd6-816e-4278-b1ff-c85a31c22f4c', '6c625e75-02f6-46b5-9133-9b8eafd471d7', '0af592b2-1ca1-4ccd-8be2-447fc0dcc232', '5d5f644e-1c1a-44a2-92e4-0bf6c290e2cb', '92e35b5e-3f56-4021-adb8-d0ad42705c81', '8f3a0f5a-b71e-4efb-b253-765351656951', 'f616b85a-6cbb-4d2d-a7c4-030becc9c1e0', '0fa45d43-9b54-482f-acd0-dd24c30bb7d5', '046b269d-e3ec-45b8-9ed6-25fa3448047a', '99128785-9f0e-4629-b489-fc6538c04326']
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
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Smooth')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "skintools.facesmoothener"`]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') == '50'):
        pass
    else:
        assert False, 'Default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "skintools.facesmoothener"`]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('0', '1', '2')):
        pass
    else:
        assert False, 'Min value fail'
    with step('[Verify] snapshot: base05_07_03_slider_min.png'):
        actions.capture_for_gt('base05_07_03_slider_min.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_03_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider left fail'
    with step('[Verify] snapshot: 05_07_03_undo_OG.png'):
        actions.capture_for_gt('05_07_03_undo_OG.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "skintools.facesmoothener"`]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('98', '99', '100')):
        pass
    else:
        assert False, 'Max value fail'
    with step('[Verify] snapshot: base05_07_03_slider_max.png'):
        actions.capture_for_gt('base05_07_03_slider_max.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_03_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider right fail'
    with step('[Verify] snapshot: 05_07_03_before_undo.png'):
        actions.capture_for_gt('05_07_03_before_undo.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_03_undo.png'):
        actions.capture_for_gt('05_07_03_undo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_03_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_03_redo.png'):
        actions.capture_for_gt('05_07_03_redo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_03_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap v fail'
    with step('[Verify] snapshot: base05_07_03_[v].png'):
        actions.capture_for_gt('base05_07_03_[v].png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_07_03_[v].png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[v] fail'
    with step("[Verify] test_00064 completion"):
        assert True
