import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00061_main_05_18_03')
def test_00061_main_05_18_03(actions: DriverActions):
    """AI background"""
    mode = 1
    uuid = ['cda20f42-9430-4d87-8132-2b0db7021a88', '569d9310-c997-4f3a-8c75-a4eb452f38f2', '91b06f2f-85f9-48d7-92b5-43ef1510be46', 'a762593a-cc53-4c36-9658-a51854e4e721', '937b8fd2-7056-40cc-a861-ff4c933146b8', '5a892d3c-e766-4f24-b7e4-e5a01616b851', 'bcb80310-2821-42ec-8e27-e0965e77a97e', 'a9e78263-7223-44ab-b4a3-d0cff17ea2f8', '65490e78-b8cc-4d1f-939d-634c532ec17a', '98e27232-2b17-442e-88eb-524eaa71c375', '09bd867f-ad60-4868-ab06-ee9b4ae742c2', 'd82a39c7-d6ab-42df-b398-71f8cb339cb5', 'dd7ba79a-8f3c-4620-86f2-baca59750033', '90671473-9fbc-483a-8c67-668d2bc0724a', '53f25aa9-9c0f-4926-ab2d-014e8864b0d9', 'fe0c8eb8-8e2b-4bdf-ae65-472d83e64127']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Background')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic info n')
    elements = ['str_ai_bg_dialog', 'str_ai_bg_dialog2']
    if not any((actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel') for ele in elements)):
        assert False, 'verify info dialog fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Verify] snapshot: 05_18_03_no_style.png'):
        actions.capture_for_gt('05_18_03_no_style.png')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Azure')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    with step('[Verify] snapshot: 05_18_03_style1.png'):
        actions.capture_for_gt('05_18_03_style1.png')
    if (not actions.compare_with_gt('05_18_03_style1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'style 1 fail'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blue')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, '2nd style fail'
    with step('[Action] close_IAP'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        actions.wait_for_invisible(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Custom')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Custom')
    with step('[Action] tap_phd_element'):
        actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[`value == "Please provide a description of the background\'s appearance or characteristics."`]')
    text = 'party'
    with step('[Action] input_custom_prompt'):
        assert actions.type_text_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeTextView', text)
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    with step('[Verify] snapshot: 05_18_03_style_custom.png'):
        actions.capture_for_gt('05_18_03_style_custom.png')
    if (not actions.compare_with_gt('05_18_03_style1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'style custom fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_18_03_style_undo.png'):
        actions.capture_for_gt('05_18_03_style_undo.png')
    if actions.compare_with_gt('05_18_03_style1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo step fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_18_03_style_redo.png'):
        actions.capture_for_gt('05_18_03_style_redo.png')
    if actions.compare_with_gt('05_18_03_style_custom.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo step fail'
    with step('[Verify] snapshot: 05_18_03_background_OG.png'):
        actions.capture_for_gt('05_18_03_background_OG.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn eraser n')
    from_pos = (325, 300)
    destination = (325, 500)
    with step('[Verify] snapshot: 05_18_03_before1.png'):
        actions.capture_for_gt('05_18_03_before1.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(325, 300, 325, 500)
    with step('[Verify] snapshot: 05_18_03_after1.png'):
        actions.capture_for_gt('05_18_03_after1.png')
    if (not actions.compare_with_gt('05_18_03_after1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'eraser + fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_18_03_after1_undo.png'):
        actions.capture_for_gt('05_18_03_after1_undo.png')
    if actions.compare_with_gt('05_18_03_after1_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo brush fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_18_03_after1_redo.png'):
        actions.capture_for_gt('05_18_03_after1_redo.png')
    if actions.compare_with_gt('05_18_03_after1_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo brush fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n')
    from_pos = (125, 400)
    destination = (325, 400)
    with step('[Verify] snapshot: 05_18_03_before2.png'):
        actions.capture_for_gt('05_18_03_before2.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(125, 400, 325, 400)
    with step('[Verify] snapshot: 05_18_03_after2.png'):
        actions.capture_for_gt('05_18_03_after2.png')
    if (not actions.compare_with_gt('05_18_03_after2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'eraser - fail'
    with step('[Verify] snapshot: 05_18_03_background_before.png'):
        actions.capture_for_gt('05_18_03_background_before.png')
    with step('[Action] adjust_harmonization_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_18_03_background_after.png'):
        actions.capture_for_gt('05_18_03_background_after.png')
    if actions.compare_with_gt('05_18_03_background_after.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'adjust brush size fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'Tap x fail'
    else:
        with step('[Verify] snapshot: 05_18_03_background_exit_brush.png'):
            actions.capture_for_gt('05_18_03_background_exit_brush.png')
        if actions.compare_with_gt('05_18_03_background_OG.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'exit brush page fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn eraser n')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n')
    from_pos = (125, 400)
    destination = (325, 100)
    with step('[Verify] snapshot: 05_18_03_before3.png'):
        actions.capture_for_gt('05_18_03_before3.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(125, 400, 325, 100)
    with step('[Verify] snapshot: 05_18_03_after3.png'):
        actions.capture_for_gt('05_18_03_after3.png')
    with step('[Action] tap_done_btn'):
        if not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]):
            assert False, 'Tap v fail'
    with step('[Verify] snapshot: 05_18_03_background_apply_brush.png'):
        actions.capture_for_gt('05_18_03_background_apply_brush.png')
    if (not actions.compare_with_gt('05_18_03_background_OG.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'exit brush fail'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00061 completion"):
        assert True
