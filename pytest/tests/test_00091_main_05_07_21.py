import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00091_main_05_07_21')
def test_00091_main_05_07_21(actions: DriverActions):
    """jawline"""
    mode = 1
    uuid = ['b49a71e5-938e-4f5b-9924-eab51c5319ba', '3cb0d594-4b4f-403a-9074-a97f6f873a22', '849ca477-e67d-4d6a-a2ed-16873f48d2ba', 'c3622f5c-636e-4b50-baa7-916b1d75bd0e', 'be898b8f-1bc5-46c4-835e-454bcd4a429a', '2b5c15c2-16ee-44f5-8c91-25e28bfd1fd5', '80684918-ba9b-4a80-9ff8-6d32337d54d9', 'db9cff20-ef7b-4cca-9371-f98d9f655b6a', 'd0d0c81b-2dca-4e3b-b57d-733bbff3bf59', '175030af-c8b1-4557-bbd5-f60228e1db22']
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
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Verify] snapshot: 05_07_21_before_jawline.png'):
        actions.capture_for_gt('05_07_21_before_jawline.png')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    from_pos = (400, 780)
    destination = (10, 780)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 780, 10, 780)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Jawline')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') == '50'):
        pass
    else:
        assert False, 'default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_21_slider_min.png'):
        actions.capture_for_gt('05_07_21_slider_min.png')
    if actions.compare_with_gt('05_07_21_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Verify] snapshot: 05_07_21_undo_og.png'):
        actions.capture_for_gt('05_07_21_undo_og.png')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_21_slider_max.png'):
        actions.capture_for_gt('05_07_21_slider_max.png')
    if actions.compare_with_gt('05_07_21_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Verify] snapshot: 05_07_21_before_undo.png'):
        actions.capture_for_gt('05_07_21_before_undo.png')
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_21_undo.png'):
        actions.capture_for_gt('05_07_21_undo.png')
    if actions.compare_with_gt('05_07_21_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo comparison fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_21_redo.png'):
        actions.capture_for_gt('05_07_21_redo.png')
    if actions.compare_with_gt('05_07_21_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo comparison fail'
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, '[v] verification fail'
    with step("[Verify] test_00091 completion"):
        assert True
