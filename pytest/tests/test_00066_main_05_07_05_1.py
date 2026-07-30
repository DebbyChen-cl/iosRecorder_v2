import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00066_main_05_07_05_1')
def test_00066_main_05_07_05_1(actions: DriverActions):
    """eye bag removal, have face"""
    mode = 1
    uuid = ['d1b617b2-eb96-4cf7-884e-273b7bde9820', 'b4765c2d-28ae-469a-a6c6-57f66cc53723', '8188991e-4bf6-48c2-bd22-1d9669387512', '22c397d0-91ad-49b4-a4fa-5448cd0c414c', 'ce23872f-0be4-4617-86d2-4a7e8ac54626', '7f8e1411-11dd-4b14-ba17-487dd1fdae45', '8eeae7d8-01c0-4a03-bd9e-fd4e90ce166a', '5dbc0a61-0286-434c-8bd2-6e8ec5452939', '92b336b9-6d58-4023-acb9-930b6b584b8b', '1da52a66-89bb-456e-ad99-e0a9e6a3f77c', '68d21830-222d-4aa1-9d5b-6ac25d02cd02']
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
    with step('[Verify] snapshot: 05_07_05_before_eyebagremoval.png'):
        actions.capture_for_gt('05_07_05_before_eyebagremoval.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    from_pos = (400, 780)
    destination = (50, 780)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 780, 50, 780)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Bags')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    get_face_value = actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '50'):
        pass
    else:
        assert False
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'Min value fail'
    with step('[Verify] snapshot: base05_07_05_slider_min.png'):
        actions.capture_for_gt('base05_07_05_slider_min.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_05_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider left fail'
    with step('[Action] tap_image'):
        assert actions.tap_by_coordinates(250, 400)
    with step('[Verify] snapshot: 05_07_05_undo_og.png'):
        actions.capture_for_gt('05_07_05_undo_og.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    get_face_value = actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'Max value fail'
    with step('[Verify] snapshot: base05_07_05_slider_max.png'):
        actions.capture_for_gt('base05_07_05_slider_max.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_05_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider right fail'
    with step('[Action] tap_image'):
        assert actions.tap_by_coordinates(250, 400)
    with step('[Verify] snapshot: 05_07_05_before_undo.png'):
        actions.capture_for_gt('05_07_05_before_undo.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_05_undo.png'):
        actions.capture_for_gt('05_07_05_undo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_05_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_05_redo.png'):
        actions.capture_for_gt('05_07_05_redo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_05_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap [v] fail'
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, 'IAP does not show up, [v] fail'
    with step("[Verify] test_00066 completion"):
        assert True
