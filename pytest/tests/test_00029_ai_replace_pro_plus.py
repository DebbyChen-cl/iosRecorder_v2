import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00029_ai_replace_pro_plus')
def test_00029_ai_replace_pro_plus(actions: DriverActions):
    """AI replace pro+"""
    mode = 1
    uuid = ['4f988d5c-7fd1-4e42-a08b-ba517b5dcf94', '3ed803b2-57ec-46b7-b2f3-777f1816c3b0', '79dde802-fd3a-4beb-8b42-00be86006852', 'da9b013e-c9a0-444e-a2ed-5bc4d7b426a6', 'df42629d-cc4b-41c6-95cc-198c8377bf01', 'aded34a5-bb61-425d-9513-03899bcee3d8', '4e36bf76-7dc0-4f5b-8f39-0f82d9a832fc', 'a2e20fcf-c15e-4d8f-8f06-7077fde29890', 'd042cd4c-edb3-4f6e-939b-d0be62efd9b8', '59a65bb3-0ed7-435f-bafb-9b3b5cd2704e', 'a987ee08-11e6-4d55-992f-d8bfdd158286', '5f743ee5-b304-4e4a-8e20-9aaee7209d9a', 'c10afb92-de67-41b7-b870-d0e87febcfb8', '89f6bd08-a61d-4048-a71a-0ae74139997a', '0df234ab-291a-47b5-a172-5f946103b2f8', '88cc36fe-3a05-4aca-879e-a0abc2883aef', 'e0883a57-b8b1-4413-9111-feb9d44ab0df', 'edd3c03c-105b-4a40-b0bf-0262372f6d3a', 'da6b7171-0bce-404a-87bf-92a322196ae4', '606b59f7-62b2-4ca6-80cb-c6886dc46f07']
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step('[Action] verify_settings_page'):
        assert (actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Setting') or
                actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'))
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
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')):
        assert False  # legacy raise
    with step('[Action] scroll_and_tap_vertical'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'AI Replace')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] expand_album_list'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Verify] snapshot: 08_04_01_no_replace.png'):
        actions.capture_for_gt('08_04_01_no_replace.png', crop_rect=(0, 60, 276, 429))
    actions.capture_for_gt('base08_04_01_default.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 08_04_01_brushsize_before.png'):
        actions.capture_for_gt('08_04_01_brushsize_before.png', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="AIReplaceViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]')
    with step('[Action] adjust_removal_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_removal_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 08_04_01_brushsize_after.png'):
        actions.capture_for_gt('08_04_01_brushsize_after.png', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="AIReplaceViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]')
    if (not actions.compare_with_gt('08_04_01_brushsize_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Verify] snapshot: 08_04_01_undo_OG.png'):
        actions.capture_for_gt('08_04_01_undo_OG.png', crop_rect=(0, 100, 367, 800))
    from_pos = (160, 302)
    destination = (350, 200)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(160, 302, 350, 200)
    actions.capture_for_gt('base08_04_01_brush.png', crop_rect=(0, 100, 367, 800))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')):
        pass
    from_pos = (160, 302)
    destination = (350, 500)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(160, 302, 350, 500)
    actions.capture_for_gt('base08_04_01_erase.png', crop_rect=(0, 100, 367, 800))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: 08_04_01_after_undo.png'):
        actions.capture_for_gt('08_04_01_after_undo.png', crop_rect=(0, 100, 367, 800))
    if actions.compare_with_gt('08_04_01_after_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'undo compare fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace')):
        assert False  # legacy raise
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Describe with Text')
    with step('[Action] verify_replace_default_prompt'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder')
    with step('[Action] send_keys'):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 'nba')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')):
        assert False  # legacy raise
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'topView_backButton')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: 08_04_01_redo_replace.png'):
        actions.capture_for_gt('08_04_01_redo_replace.png', crop_rect=(0, 100, 367, 800))
    if actions.compare_with_gt('08_04_01_redo_replace.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'redo replace verification failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Describe with Text')
    with step('[Action] send_keys'):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 'nba')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')):
        assert False  # legacy raise
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    if (not actions.tap_by_locator(AppiumBy.NAME, 'Replace More')):
        assert False  # legacy raise
    from_pos = (100, 500)
    destination = (250, 450)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(100, 500, 250, 450)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace')):
        assert False  # legacy raise
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Describe with Text')
    with step('[Action] verify_replace_default_prompt'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder')
    with step('[Action] send_keys'):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 'basketball')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')):
        assert False  # legacy raise
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'topView_backButton')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'topView_backButton')
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Verify] snapshot: 08_04_01_before_replace.png'):
        actions.capture_for_gt('08_04_01_before_replace.png', crop_rect=(0, 100, 367, 800))
    enter_ai_replace_from_edit = actions.try_tap(AppiumBy.NAME, 'AI Replace')
    for _ in range(5):
        if enter_ai_replace_from_edit:
            break
        with step('[Action] _swipe_feature_tab_left'):
            actions.swipe_on_element(
                AppiumBy.ACCESSIBILITY_ID,
                'EditViewControllerBottomBarCollectionView',
                'left',
                from_pct_x=95,
                from_pct_y=50,
                distance_pts=150,
            )
        enter_ai_replace_from_edit = actions.try_tap(AppiumBy.NAME, 'AI Replace')
    if not enter_ai_replace_from_edit:
        assert False  # legacy raise
    with step('[Verify] snapshot: base08_04_01_from_edit.png'):
        actions.capture_for_gt('base08_04_01_from_edit.png', crop_rect=(0, 100, 367, 800))
    with step('[Action] adjust_removal_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    from_pos = (160, 550)
    destination = (350, 500)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(160, 550, 350, 500)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace')):
        assert False  # legacy raise
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Describe with Text')
    with step('[Action] send_keys'):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 'ba')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')):
        assert False  # legacy raise
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'topView_backButton')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'topView_backButton')):
        assert False  # legacy raise
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.NAME, 'AI Replace')):
        assert False  # legacy raise
    from_pos = (110, 300)
    destination = (330, 600)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(110, 300, 330, 600)
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Circle')):
        assert False  # legacy raise
    from_pos = (110, 300)
    destination = (330, 600)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(110, 300, 330, 600)
    with step('[Action] tap_feature_x_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00029 completion"):
        assert True
