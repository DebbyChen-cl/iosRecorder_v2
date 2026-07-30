import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00074_main_05_07_10_1')
def test_00074_main_05_07_10_1(actions: DriverActions):
    """oiliness, have face"""
    mode = 1
    uuid = ['a8c0090f-d6bf-4989-aae1-9ab7add1ade2', '61d63799-4337-4ced-bfa7-4ca121dd0e66', '7b291735-dd6d-49e0-8167-9f01987d6981', '40d37590-4fac-4942-a3a9-7de59aaa8906', 'e9fb5545-a595-423f-9652-9c3aabc50384', 'bbb30f0a-eef2-4924-b762-57f7f2d67b1d', '32f1fd57-49ed-412a-a166-49fbe1597271', '45292113-a61e-416a-8db7-ab7588ba36f1', '7b3482d5-2c73-4c8c-9619-58687e67a5c7', 'bb9cb8b4-a907-44ed-8cda-1baf80dbef1b']
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
    with step('[Verify] snapshot: 05_07_10_before_oiliness.png'):
        actions.capture_for_gt('05_07_10_before_oiliness.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Oiliness')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[-2]') == '50'):
        pass
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'Min value fail'
    with step('[Verify] snapshot: base05_07_10_slider_min.png'):
        actions.capture_for_gt('base05_07_10_slider_min.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_10_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider left fail'
    with step('[Action] tap_image'):
        assert actions.tap_by_coordinates(250, 400)
    with step('[Verify] snapshot: 05_07_10_undo_og.png'):
        actions.capture_for_gt('05_07_10_undo_og.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[-2]') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'Max value fail'
    with step('[Verify] snapshot: base05_07_10_slider_max.png'):
        actions.capture_for_gt('base05_07_10_slider_max.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_10_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider right fail'
    with step('[Action] tap_image'):
        assert actions.tap_by_coordinates(250, 400)
    with step('[Verify] snapshot: 05_07_10_before_undo.png'):
        actions.capture_for_gt('05_07_10_before_undo.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_10_undo.png'):
        actions.capture_for_gt('05_07_10_undo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_10_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_10_redo.png'):
        actions.capture_for_gt('05_07_10_redo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_10_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap [v] fail'
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, '[v] fail'
    with step("[Verify] test_00074 completion"):
        assert True
