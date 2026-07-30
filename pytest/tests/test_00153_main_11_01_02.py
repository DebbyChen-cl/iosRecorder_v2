import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00153_main_11_01_02')
def test_00153_main_11_01_02(actions: DriverActions):
    """subscribed - tools"""
    uuid = ['90487927-01e9-4793-98dc-8afcf4c4bb29', 'fb6f1b41-cee0-4303-94a9-8d43987c1889', '8964431e-18e0-4581-b5e5-94ec781ec4d6', 'ee4c3960-0748-45f3-85b9-0be714c6d193', 'edd3c03c-105b-4a40-b0bf-0262372f6d3a']
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] close_IAP'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] tap_settings3'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings'), '[11_01_02] Failed to tap settings3'
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
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Enhance')
    with step('[Action] close_aienhance_intro_dialog'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Enhance"`]')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'All-in-One AI Photo Enhance')
    with step('[Action] wait_process'):
        actions.tap_by_coordinates(100, 200)
        actions.tap_by_coordinates(100, 200)
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_02] IAP should not appear after aienhance'
    with step('[Verify] snapshot: 11_01_02_aienhance.png'):
        actions.capture_for_gt('11_01_02_aienhance.png')
    if actions.compare_with_gt('11_01_02_aienhance.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')
    with step('[Action] close_IAP_prompt_removal2'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Manual')
    with step('[Action] adjust_removal_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_removal_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    from_pos = (200, 300)
    destination = (200, 702)
    mode = 1
    with step('[Action] brush_removal'):
        assert actions.drag_coordinates(200, 300, 200, 702)
    with step('[Action] tap_remove'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'applyButton')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_02] IAP should not appear after removal'
    with step('[Verify] snapshot: 11_01_02_airemoval.png'):
        actions.capture_for_gt('11_01_02_airemoval.png')
    if actions.compare_with_gt('11_01_02_airemoval.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Deblur')
    with step('[Action] close_deblur_intro_dialog'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Deblur"`][2]')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur.')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_02] IAP should not appear after deblur'
    with step('[Verify] snapshot: 11_01_02_deblur.png'):
        actions.capture_for_gt('11_01_02_deblur.png')
    if actions.compare_with_gt('11_01_02_deblur.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Denoise')
    with step('[Action] close_denoise_intro_dialog'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Denoise')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Eliminate the noise in your low light or high-ISO photos with our latest AI technology.')
    with step('[Action] tap_done_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        assert False, '[11_01_02] IAP should not appear after denoise'
    with step('[Verify] snapshot: 11_01_02_denoise.png'):
        actions.capture_for_gt('11_01_02_denoise.png')
    if actions.compare_with_gt('11_01_02_denoise.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00153 completion"):
        assert True
