import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00055_main_05_04a_03')
def test_00055_main_05_04a_03(actions: DriverActions):
    """mosaic - manual"""
    mode = 1
    uuid = ['0aa795bd-3747-4359-83a7-838a72e407ea', '2a4fb191-fd20-4afb-aad8-af821f1616cc', '6bb6d30f-a4de-498d-b779-ca49dc9cf793', '568b99cc-0f30-4a45-b73a-5bb3674bca3c', 'c2485313-95ff-4dd7-b3e2-50751afb0b37', '9701fb15-b014-4ae4-8ae2-4a5efb646b30', 'dc672e8c-7dc9-4518-aad5-a3f02bbc576a', 'ae091058-b11a-4640-97fa-67eb401fa4ae', '5764be6c-c214-4e38-be5e-69d38151a24b', 'a1452613-b36e-451c-a13b-36a5bc721448', 'e65282d1-6df3-47ce-b5d0-7e5690557769', '0aa3d933-0647-492a-9f70-b55475f2795c', '75ead3da-5a9a-4005-9a0f-1f3801934292', '160fd9f9-0268-48e9-af9b-deeea2535700', 'f92751f5-12e5-44bb-a99b-2fabe388717c', 'd3736ee9-ce5e-412b-be8a-276a65b98c11', '097cc13d-f603-43ee-a9fe-b111df7ed695', 'fadd73f2-b6df-4d59-a94f-f9889d8683b2', 'c2873264-230d-4ea2-987a-5f1d524d9cfc', 'd0051567-0ec9-4db4-8f8b-273bf68b6b9f', 'e359ce4b-9f1e-41cb-8d37-315d8ff21d06', '0394473f-cd3a-48b9-b4f6-fd6300788824', '565efa75-618a-407d-a755-2cbaf4c6a82d', '162c65dd-e30a-4667-ab50-893173122bf2']
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
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mosaic')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Manual')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '30'):
        pass
    else:
        assert False, 'Default value error'
    with step('[Action] adjust_mosaic_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('95', '96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'Adjust max fail'
    with step('[Action] adjust_mosaic_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('5', '4', '3', '2', '1', '0')):
        pass
    else:
        assert False, 'Adjust min fail'
    with step('[Verify] snapshot: 05_04a_03_no_mask.png'):
        actions.capture_for_gt('05_04a_03_no_mask.png', crop_rect=(0, 60, 276, 597))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'tap v fail'
    with step('[Verify] snapshot: 05_04a_03_tap_v.png'):
        actions.capture_for_gt('05_04a_03_tap_v.png')
    if actions.compare_with_gt('05_04a_03_tap_v.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tap v fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_04a_03_before_enter_mosaic.png'):
        actions.capture_for_gt('05_04a_03_before_enter_mosaic.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mosaic')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Manual')
    with step('[Verify] snapshot: 05_04a_03_before_enter_brush.png'):
        actions.capture_for_gt('05_04a_03_before_enter_brush.png', crop_rect=(0, 60, 276, 597))
    with step('[Verify] snapshot: 05_04a_03_brush+_before.png'):
        actions.capture_for_gt('05_04a_03_brush+_before.png')
    with step('[Action] adjust_slider_1'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 05_04a_03_brush+_after.png'):
        actions.capture_for_gt('05_04a_03_brush+_after.png')
    if (not actions.compare_with_gt('05_04a_03_brush+_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust brush size fail'
    with step('[Action] adjust_slider_1'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    from_pos = (30, 90)
    destination = (390, 570)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 90, 390, 570)
    with step('[Verify] snapshot: 05_04a_03_after_brush+.png'):
        actions.capture_for_gt('05_04a_03_after_brush+.png')
    if actions.compare_with_gt('05_04a_03_after_brush+.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'eraser + fail'
    with step('[Verify] snapshot: 05_04a_03_undo_og.png'):
        actions.capture_for_gt('05_04a_03_undo_og.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n')
    with step('[Verify] snapshot: 05_04a_03_after_reset.png'):
        actions.capture_for_gt('05_04a_03_after_reset.png')
    if actions.compare_with_gt('05_04a_03_after_reset.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'reset fail'
    with step('[Verify] snapshot: 05_04a_03_redo_og.png'):
        actions.capture_for_gt('05_04a_03_redo_og.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_04a_03_after_undo.png'):
        actions.capture_for_gt('05_04a_03_after_undo.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_04a_03_after_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_04a_03_after_redo.png'):
        actions.capture_for_gt('05_04a_03_after_redo.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_04a_03_after_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step('[Verify] snapshot: 05_04a_03_brush-_before.png'):
        actions.capture_for_gt('05_04a_03_brush-_before.png')
    with step('[Action] adjust_slider_1'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Verify] snapshot: 05_04a_03_brush-_after.png'):
        actions.capture_for_gt('05_04a_03_brush-_after.png')
    if (not actions.compare_with_gt('05_04a_03_brush-_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust brush size fail'
    with step('[Action] adjust_slider_1'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    from_pos = (30, 90)
    destination = (390, 570)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 90, 390, 570)
    with step('[Verify] snapshot: 05_04a_03_after_brush-.png'):
        actions.capture_for_gt('05_04a_03_after_brush-.png')
    if actions.compare_with_gt('05_04a_03_after_brush-.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'eraser - fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'tap x fail'
    with step('[Verify] snapshot: 05_04a_03_leave_mosaic_x.png'):
        actions.capture_for_gt('05_04a_03_leave_mosaic_x.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_04a_03_leave_mosaic_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'exit mosaic fail'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00055 completion"):
        assert True
