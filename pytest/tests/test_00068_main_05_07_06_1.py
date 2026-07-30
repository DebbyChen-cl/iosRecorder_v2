import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00068_main_05_07_06_1')
def test_00068_main_05_07_06_1(actions: DriverActions):
    """teeth whiten, have face"""
    mode = 1
    uuid = ['771a54d3-cd5c-4955-88bc-662c2681b8cb', '80dd02df-a65b-480c-9827-e114ba289d96', 'c9d15668-c38a-40a5-b08b-02c5495ac0f3', 'ea7e58d4-b7b5-4a51-a6ce-c56431f140b9', '1723acee-2809-4dd7-bbe7-693dee6635f9', '9dd7d6cf-d1cd-43e3-a7d9-37853e1cd2b4', '0d26bd06-04b2-44f2-bc9b-7958885e0c99', '6705edce-cae2-48de-961f-aed909f2af42', 'f45b45fb-f47d-496e-82db-2b5dff622b52', '0d7776d2-864b-4a65-9221-704884c05971', '3f0dfce8-ca1f-4934-9505-e282902c5ed4']
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
    with step('[Verify] snapshot: 05_07_06_before_teethwhiten.png'):
        actions.capture_for_gt('05_07_06_before_teethwhiten.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    from_pos = (400, 780)
    destination = (10, 780)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 780, 10, 780)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Teeth Whiten')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[-2]') == '50'):
        pass
    else:
        assert False, 'Default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'Min value fail'
    with step('[Verify] snapshot: base05_07_06_slider_min.png'):
        actions.capture_for_gt('base05_07_06_slider_min.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_06_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider left fail'
    with step('[Action] tap_image'):
        assert actions.tap_by_coordinates(250, 400)
    with step('[Verify] snapshot: 05_07_06_undo_og.png'):
        actions.capture_for_gt('05_07_06_undo_og.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[-2]') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'Max value fail'
    with step('[Verify] snapshot: base05_07_06_slider_max.png'):
        actions.capture_for_gt('base05_07_06_slider_max.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_06_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider right fail'
    with step('[Action] tap_image'):
        assert actions.tap_by_coordinates(250, 400)
    with step('[Verify] snapshot: 05_07_06_before_undo.png'):
        actions.capture_for_gt('05_07_06_before_undo.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_06_undo.png'):
        actions.capture_for_gt('05_07_06_undo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_06_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_06_redo.png'):
        actions.capture_for_gt('05_07_06_redo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_06_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap [v] fail'
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, '[v] fail'
    with step("[Verify] test_00068 completion"):
        assert True
