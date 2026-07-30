import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00041_hdr')
def test_00041_hdr(actions: DriverActions):
    """HDR"""
    mode = 1
    uuid = ['be1a555e-f91e-4019-8dc0-79964d2b0d32', '32ba61a2-ec2a-4a37-b265-b8a46c9eec55', ' ', 'ed320495-6e9d-4bbc-beaf-b8ad1d585e80', ' ', 'b7a263d6-edb2-4095-890c-fea6eb4810b5', 'd5c4326d-42d8-47a2-a7a3-c5e3d3330d45', '  ', '54eed312-d840-44ca-8400-47c2ddc24cf5', '755b3113-a753-4291-be6e-ad95edde646a', '58603370-21cc-4ec7-8f38-4962279c4e81', ' ', '65892b9d-2a51-49c3-86f0-26ae8d4fcc88', '24daf13a-4da3-44e9-8bd5-4b2c04f10b7b', ' ', ' ', 'dadbd090-fa1e-470e-bc7c-d16201e6a648', '  ', '608507fc-2f26-4782-91b4-548f92b2ce3c', '890660f8-33d5-46e8-9326-3954b1a700d2', 'd2ad0bde-1e7e-4c7b-a66c-62ba907803bc', ' ', '79cb107a-b66e-43f5-9566-8cffae578eef', 'ac73689c-800f-476b-adba-2d10d94564d4']
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
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_07_before_hdr.png'):
        actions.capture_for_gt('05_03_07_before_hdr.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HDR')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_03_07_HDR_default.png'):
        actions.capture_for_gt('base05_03_07_HDR_default.png', crop_rect=(0, 60, 276, 526))
    if (actions.get_text(AppiumBy.XPATH, '//XCUIElementTypeSlider/../following-sibling::XCUIElementTypeStaticText') == '0'):
        pass
    else:
        assert False  # legacy raise
    from_pos = (0, 460)
    destination = (420, 460)
    with step('[Verify] snapshot: 05_03_07_before_scr_right.png'):
        actions.capture_for_gt('05_03_07_before_scr_right.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(0, 460, 420, 460)
    with step('[Verify] snapshot: 05_03_07_after_scr_right.png'):
        actions.capture_for_gt('05_03_07_after_scr_right.png', crop_rect=(0, 60, 276, 526))
    if (not actions.compare_with_gt('05_03_07_after_scr_right.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.XPATH, '//XCUIElementTypeSlider/../following-sibling::XCUIElementTypeStaticText') in ('98', '99', '100')):
        pass
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_07_after_slider_left.png'):
        actions.capture_for_gt('05_03_07_after_slider_left.png', crop_rect=(0, 60, 276, 526))
    if (not actions.compare_with_gt('05_03_07_after_scr_right.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.XPATH, '//XCUIElementTypeSlider/../following-sibling::XCUIElementTypeStaticText') in ('98', '99', '100')):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    else:
        with step('[Verify] snapshot: 05_03_07_exit_hdr.png'):
            actions.capture_for_gt('05_03_07_exit_hdr.png', crop_rect=(0, 60, 276, 429))
        if actions.compare_with_gt('05_03_07_exit_hdr.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HDR')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edge')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.XPATH, '//XCUIElementTypeSlider/../following-sibling::XCUIElementTypeStaticText') == '0'):
        pass
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.XPATH, '//XCUIElementTypeSlider/../following-sibling::XCUIElementTypeStaticText') in ('78', '79', '80')):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.XPATH, '//XCUIElementTypeSlider/../following-sibling::XCUIElementTypeStaticText') in ('-18', '-19', '-20')):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] adjust_hdr_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    else:
        with step('[Verify] snapshot: 05_03_07_exit_hdr_v.png'):
            actions.capture_for_gt('05_03_07_exit_hdr_v.png', crop_rect=(0, 60, 276, 429))
        if (not actions.compare_with_gt('05_03_07_exit_hdr_v.png', gt_folder=TD.GT_FOLDER)[0]):
            pass
        else:
            assert False  # legacy raise
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00041 completion"):
        assert True
