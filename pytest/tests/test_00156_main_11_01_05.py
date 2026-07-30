import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00156_main_11_01_05')
def test_00156_main_11_01_05(actions: DriverActions):
    """subscribed - text, text bubble, ticker, live, frame"""
    uuid = ['4da3f878-bff5-4ca6-b624-5aef34380eeb', 'f8afcbe4-7485-4c28-b5a7-b5cd9a1638e7', 'f51a7539-3cbb-49b7-95b1-70ee47a547cc', '7118a351-f62c-415f-92f4-f840b809a40f', 'c97ff4f5-8d4e-4678-a372-00d2cdb2185d', '6fac0181-0d5c-4f27-83d0-64a4c3e15b8c', '22029da7-a2ef-44ee-99dd-d0c35dfe58da', 'a8a4d58c-5f6b-4b33-b253-e46d3a1d6be3', '77df9728-57e3-4a01-af83-bb22a882cb28']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_texttools_text'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
        assert actions.tap_by_coordinates(350, 700)
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    with step('[Action] tap_OK'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Verify] snapshot: 11_01_05_text.png'):
        actions.capture_for_gt('11_01_05_text.png')
    if actions.compare_with_gt('11_01_05_text.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[11_01_05] text compare fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_text_bubble'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text Bubble')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text Bubble')
        assert actions.tap_by_coordinates(350, 770)
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    with step('[Action] tap_OK'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Verify] snapshot: 11_01_05_textb.png'):
        actions.capture_for_gt('11_01_05_textb.png')
    if actions.compare_with_gt('11_01_05_textb.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[11_01_05] text bubble compare fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sticker')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Static Sticker')
    with step('[Action] Tap'):
        assert actions.tap_by_coordinates(80, 580)
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_05] IAP should not appear after sticker'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'CMS-tw_cartoon_smile'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-tw_cartoon_smile')
    else:
        tapped = False
        for i in range(3):
            with step('[Action] brush_surrealart'):
                actions.drag_coordinates(200, 820, 200, 780)
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'CMS-tw_cartoon_smile'):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-tw_cartoon_smile')
                tapped = True
                break
        assert tapped, '[11_01_05] Failed to find and tap template for elements after scrolling'
    with step('[Action] tap_live_done_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_05] IAP should not appear after element'
    with step('[Action] tap_save_still_img'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Still Image')
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_live_overlays'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animated Overlays')
        assert actions.tap_by_coordinates(215, 770)
    with step('[Action] tap_live_done_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_05] IAP should not appear after overlays'
    with step('[Action] tap_save_still_img'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Still Image')
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_wraparound'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_wraparound_n')
        assert actions.tap_by_coordinates(355, 770)
    with step('[Action] tap_live_done_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_05] IAP should not appear after wraparound'
    with step('[Action] tap_save_still_img'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Still Image')
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_sky'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_sky_n')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cloudy 2')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')
        assert actions.tap_by_coordinates(180, 770)
    with step('[Action] tap_live_done_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_05] IAP should not appear after sky'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_sparkle'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sparkle')
    with step('[Verify] snapshot: 11_01_05_before_sparkle.png'):
        actions.capture_for_gt('11_01_05_before_sparkle.png')
    with step('[Action] tap_sparkle_template'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sparkle"`]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]')
        assert actions.tap_by_coordinates(230, 770)
    with step('[Verify] snapshot: 11_01_05_add_sparkle.png'):
        actions.capture_for_gt('11_01_05_add_sparkle.png')
    with step('[Action] tap_live_done_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Verify] snapshot: 11_01_05_sparkle_v.png'):
        actions.capture_for_gt('11_01_05_sparkle_v.png')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_05] IAP should not appear after sparkle'
    with step('[Action] tap_save_still_img'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Still Image')
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Frame')
    with step('[Action] Tap'):
        assert actions.tap_by_coordinates(100, 770)
    with step('[Action] tap_frame_option'):
        assert actions.tap_by_coordinates(150, 770)
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_05] IAP should not appear after frame'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00156 completion"):
        assert True
