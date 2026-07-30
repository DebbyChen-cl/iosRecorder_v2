import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00082_conceal_with_face')
def test_00082_conceal_with_face(actions: DriverActions):
    """conceal, have face"""
    uuid = ['ec9a6251-140e-4d67-ae45-799d720b009d', 'bbc5fc1c-39dd-48c1-a435-67ac39d0a972', '0911a4a1-d2c9-4818-a34e-22f5e67ee307', '88efd5c0-8470-4acd-a769-a1a99a1e965f', '78dd9748-f7c4-45ad-9478-4cee3ae1335f', '964f8789-bcf7-4caf-98fb-1876b1daaf3c', 'ca2d5207-bfee-42a6-b550-ea38ae3004bc', '426d4914-4248-46f4-a2e9-64ed560b11f6', '857bcd27-dfa2-410d-b708-b9c2eca77ce4', '76473793-3fca-43f2-869a-9f797c408216']
    with step('[Action] close_continue_edit'):
        actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Conceal')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[-2]') == '50'):
        pass
    if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('0', '1', '2', '3', '4'))):
        pass
    else:
        assert False  # legacy raise
    if mode == 1:
        with step('[Verify] snapshot: base05_07_16_slider_min.png'):
            actions.capture_for_gt('base05_07_16_slider_min.png', crop_rect=(0, 60, 276, 526))
    else:
        with step('[Verify] snapshot: 05_07_16_slider_min.png'):
            actions.capture_for_gt('05_07_16_slider_min.png', crop_rect=(0, 60, 276, 526))
        if actions.compare_with_gt('05_07_16_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Slider left verification failed'
    with step('[Action] tap_by_coordinates'):
        actions.tap_by_coordinates(250, 400)
    with step('[Verify] snapshot: 05_07_16_undo_og.png'):
        actions.capture_for_gt('05_07_16_undo_og.png', crop_rect=(0, 60, 276, 526))
    if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[-2]') in ('96', '97', '98', '99', '100'))):
        pass
    else:
        assert False  # legacy raise
    if mode == 1:
        with step('[Verify] snapshot: base05_07_16_slider_max.png'):
            actions.capture_for_gt('base05_07_16_slider_max.png', crop_rect=(0, 60, 276, 526))
    else:
        with step('[Verify] snapshot: 05_07_16_slider_max.png'):
            actions.capture_for_gt('05_07_16_slider_max.png', crop_rect=(0, 60, 276, 526))
        if actions.compare_with_gt('05_07_16_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Slider right verification failed'
    with step('[Verify] snapshot: 05_07_16_before_undo.png'):
        actions.capture_for_gt('05_07_16_before_undo.png', crop_rect=(0, 60, 276, 526))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_07_16_undo.png'):
        actions.capture_for_gt('05_07_16_undo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_16_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo verification failed'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_07_16_redo.png'):
        actions.capture_for_gt('05_07_16_redo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_16_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo verification failed'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    with step("[Verify] test_00082 completion"):
        assert True
