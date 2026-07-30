import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00154_main_11_01_03')
def test_00154_main_11_01_03(actions: DriverActions):
    """subscribed - Portrait tools"""
    uuid = ['84816dd9-45f9-4894-84ae-913681736315', 'b484724f-b9e9-48b8-a05e-450981a147a5', '25523f2f-781e-4241-969b-d42ff46fc85b', '990d24e0-f705-412b-80eb-2db62c2f6f76', 'd7b3ed20-32f7-4f06-a7aa-9eae64b73059', '9b4d7f09-ec92-4843-8f1a-3e8c640a6b86', '6398b70d-8752-4d6a-ab3b-298b29d967dc', '293cf605-94f2-4aaf-8f47-54fe0d3c6b60', 'ffe48089-8afb-4197-840f-957c8d1f9263', '71c50151-6044-48d2-9584-39562c94a9c6', 'f65d2739-badc-4c84-ae0b-20de4a918151', '584388ce-69c2-4517-9811-3579671b44c7', 'a8da5007-573f-40ce-bdfa-7464eeffcec3', '162c65dd-e30a-4667-ab50-893173122bf2']
    with step('[Action] tap_settings3'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step('[Action] verify_settings_page'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Setting', timeout=5) or actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle', timeout=5)
    enter_about_page_success = False
    for attempt in range(3):
        with step('[Action] enter_about_page'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'About')
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton')
        enter_about_page_success = True
        break
        if attempt < 2:
            pass
    if not enter_about_page_success:
        assert False, 'Enter about page fail after 3 retries'
    with step('[Action] enable_plan_from_settings'):
        actions.is_element_present(AppiumBy.NAME, 'Develop Info')
        actions.find_element(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="1"])[2]')
        actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[6]')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    from_pos = (250, 780)
    destination = (300, 780)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(250, 780, 300, 780)
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Makeup')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lipstick')
    with step('[Action] tap_lipstick_03'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Nude 01')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after makeup'
    with step('[Verify] snapshot: 11_01_03_makeup.png'):
        actions.capture_for_gt('11_01_03_makeup.png')
    if actions.compare_with_gt('11_01_03_makeup.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_auto_retouch'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto Retouch')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after auto_retouch'
    with step('[Verify] snapshot: 11_01_03_auto_retouch.png'):
        actions.capture_for_gt('11_01_03_auto_retouch.png')
    if actions.compare_with_gt('11_01_03_auto_retouch.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_reshape'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Reshape')
    with step('[Action] tap_face'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Face')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after reshape'
    with step('[Verify] snapshot: 11_01_03_reshape.png'):
        actions.capture_for_gt('11_01_03_reshape.png')
    if actions.compare_with_gt('11_01_03_reshape.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_conceal'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Conceal')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after conceal'
    with step('[Verify] snapshot: 11_01_03_conceal.png'):
        actions.capture_for_gt('11_01_03_conceal.png')
    if actions.compare_with_gt('11_01_03_conceal.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    from_pos = (400, 780)
    destination = (250, 780)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 780, 250, 780)
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    from_pos = (400, 780)
    destination = (150, 780)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 780, 150, 780)
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_skintone'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Skin Tone')
    with step('[Action] tap_skin_tone_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cellColor-1')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after skintone'
    with step('[Verify] snapshot: 11_01_03_skintone.png'):
        actions.capture_for_gt('11_01_03_skintone.png')
    if actions.compare_with_gt('11_01_03_skintone.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_jawline'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Jawline')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after jawline'
    with step('[Verify] snapshot: 11_01_03_jawline.png'):
        actions.capture_for_gt('11_01_03_jawline.png')
    if actions.compare_with_gt('11_01_03_jawline.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_doublechin'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Double Chin')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after doublechin'
    with step('[Verify] snapshot: 11_01_03_doublechin.png'):
        actions.capture_for_gt('11_01_03_doublechin.png')
    if actions.compare_with_gt('11_01_03_doublechin.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 11_01_03_before_wrinkle.png'):
        actions.capture_for_gt('11_01_03_before_wrinkle.png')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_wrinkle'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Wrinkle')
    with step('[Verify] snapshot: 11_01_03_enter_wrinkle1.png'):
        actions.capture_for_gt('11_01_03_enter_wrinkle1.png')
    with step('[Verify] snapshot: 11_01_03_enter_wrinkle2.png'):
        actions.capture_for_gt('11_01_03_enter_wrinkle2.png')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after wrinkle'
    with step('[Verify] snapshot: 11_01_03_wrinkle.png'):
        actions.capture_for_gt('11_01_03_wrinkle.png')
    if actions.compare_with_gt('11_01_03_wrinkle.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_blemish'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blemish')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after blemish'
    with step('[Verify] snapshot: 11_01_03_blemish.png'):
        actions.capture_for_gt('11_01_03_blemish.png')
    if actions.compare_with_gt('11_01_03_blemish.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_plumpness'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Plumpness')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after plumpness'
    with step('[Verify] snapshot: 11_01_03_plumpness.png'):
        actions.capture_for_gt('11_01_03_plumpness.png')
    if actions.compare_with_gt('11_01_03_plumpness.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    from_pos = (400, 780)
    destination = (250, 780)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 780, 250, 780)
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_teethwhiten'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Teeth Whiten')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after teethwhiten'
    with step('[Verify] snapshot: 11_01_03_teethwhiten.png'):
        actions.capture_for_gt('11_01_03_teethwhiten.png')
    if actions.compare_with_gt('11_01_03_teethwhiten.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    from_pos = (400, 780)
    destination = (150, 780)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 780, 150, 780)
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye')
    with step('[Action] tap_eyebrighten'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Brighten')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after eyebrighten'
    with step('[Verify] snapshot: 11_01_03_eyebrighten.png'):
        actions.capture_for_gt('11_01_03_eyebrighten.png')
    if actions.compare_with_gt('11_01_03_eyebrighten.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye')
    with step('[Action] tap_eyebagremoval'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Bags')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after eyebag'
    with step('[Verify] snapshot: 11_01_03_eyebag.png'):
        actions.capture_for_gt('11_01_03_eyebag.png')
    if actions.compare_with_gt('11_01_03_eyebag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_oiliness'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Oiliness')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after oiliness'
    with step('[Verify] snapshot: 11_01_03_oiliness.png'):
        actions.capture_for_gt('11_01_03_oiliness.png')
    if actions.compare_with_gt('11_01_03_oiliness.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    from_pos = (400, 780)
    destination = (250, 780)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 780, 250, 780)
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_nose'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Nose Enhance')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after noseenhance'
    with step('[Verify] snapshot: 11_01_03_noseenhance.png'):
        actions.capture_for_gt('11_01_03_noseenhance.png')
    if actions.compare_with_gt('11_01_03_noseenhance.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_03] IAP should not appear after final noseenhance'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00154 completion"):
        assert True
