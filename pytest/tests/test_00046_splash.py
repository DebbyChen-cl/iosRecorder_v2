import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00046_splash')
def test_00046_splash(actions: DriverActions):
    """splash"""
    mode = 1
    uuid = ['f55068cd-4cac-4d61-ac04-723d50729a98', 'f6d6c935-16cb-4785-95f4-6268da9ddf10', '7777c890-7df1-4275-b05a-75999ec0526b', '81aa0661-ee85-4a41-8316-f8cd3c037e99', '9b18ab99-562d-4103-825f-b7e3cc157429', '538555ac-f0af-4bf6-8564-4173cbf17f44', '50dfbc66-c132-46bd-bc6c-4d4678f4cbbb', 'de972794-0a23-4bfd-99c7-d4acea024fde', 'f90e4b4e-d4f1-4189-84d4-3927b29e7a34', 'f99a6439-a998-45eb-84dc-f701562830b8', '1a75b2fc-61ef-453b-a26c-dbbbce490a7e', '08f53a32-96d9-4118-965f-1a4ca74a7f8a', '131d2f86-1c07-4724-accc-965f40f4ef0d', 'b10770f3-043c-4416-a62f-d6b9daae8ad0', '64b55196-26a1-436f-9171-5d3690a88f4f', '6e2361a1-aac1-43a7-a70b-7f535b21f397', '69ad37fd-96e7-40a3-9493-5a589d9094e2', '662a4960-6165-4817-99b2-e02ee73b606a', 'e1c59d39-81c0-4832-9784-6c7c6dfe9abc', '1227e3b0-f595-46d2-95f6-553a764c3463', '89a810f7-db44-414b-8427-e1fe6d1d9d65', '157d0845-6345-4541-9a96-b2fc5558b930', '7a628dfb-0ced-42e2-88a9-84b87e828d16', '1a592d9c-a881-4ade-8bea-4fd9a7c72063', '36ac99b3-01c6-4a08-bf83-2fd4601b8ac1', 'ca444738-3d89-4697-967b-b14ed81e890f', '6d68b216-29e4-4404-98e7-d68d3bd9baf9', '7ee5cf74-e22c-4b9c-88a0-d279d6387586', 'a68aa621-ea03-4cf5-8459-9cb4f6cee26e', '00f5c7a9-c5c9-4137-84e2-f4bf230bf53e', '37f9b4dd-9215-4f07-b4ac-ec5f2c17a261', '794b186c-f87d-4786-8c67-96754a68393c']
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
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')):
        assert False  # legacy raise
    from_pos = (380, 770)
    destination = (280, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 280, 770)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Splash')):
        assert False  # legacy raise
    if (not actions.tap_by_coordinates(205, 300)):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage/XCUIElementTypeStaticText') == '20'):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4', '5')):
        pass
    else:
        assert False, 'Min value fail'
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False, 'Adjust slider to max fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_04_04_no_mask.png'):
        actions.capture_for_gt('05_04_04_no_mask.png', crop_rect=(0, 60, 276, 597))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn shape mask n')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'original_thumb')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04_04_dled_mask.png'):
        actions.capture_for_gt('base05_04_04_dled_mask.png', crop_rect=(0, 60, 276, 597))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'circle_thumb')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04_04_og_mask.png'):
        actions.capture_for_gt('base05_04_04_og_mask.png', crop_rect=(0, 60, 276, 597))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn invert n')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04_04_inverse_mask.png'):
        actions.capture_for_gt('base05_04_04_inverse_mask.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn invert n')
    with step('[Action] tap_phd_element'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'circle_thumb')
    from_pos = (410, 599)
    destination = (315, 627)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Verify] snapshot: 05_04_04_before_rotate.png'):
        actions.capture_for_gt('05_04_04_before_rotate.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(410, 599, 315, 627)
    with step('[Verify] snapshot: 05_04_04_after_rotate.png'):
        actions.capture_for_gt('05_04_04_after_rotate.png', crop_rect=(0, 60, 276, 597))
    if (not actions.compare_with_gt('05_04_04_after_rotate.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_04_04_leave_mask_x.png'):
        actions.capture_for_gt('05_04_04_leave_mask_x.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_04_04_leave_mask_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Exit mask fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn shape mask n')
    with step('[Action] tap_phd_element'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'circle_thumb')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap v fail'
    with step('[Verify] snapshot: base05_04_04_tap_maskv.png'):
        actions.capture_for_gt('base05_04_04_tap_maskv.png', crop_rect=(0, 60, 276, 597))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04_04_tap_v.png'):
        actions.capture_for_gt('base05_04_04_tap_v.png', crop_rect=(0, 60, 276, 597))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_04_04_before_enter_splash.png'):
        actions.capture_for_gt('05_04_04_before_enter_splash.png', crop_rect=(0, 725, 367, 783))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Splash')):
        assert False  # legacy raise
    if (not actions.tap_by_coordinates(205, 300)):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_04_04_before_enter_brush.png'):
        actions.capture_for_gt('05_04_04_before_enter_brush.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn mask switch n')
    with step('[Verify] snapshot: 05_04_04_brush-size_before.png'):
        actions.capture_for_gt('05_04_04_brush-size_before.png', crop_rect=(0, 725, 367, 783))
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0.5')
    with step('[Verify] snapshot: 05_04_04_brush-size_after.png'):
        actions.capture_for_gt('05_04_04_brush-size_after.png', crop_rect=(0, 725, 367, 783))
    if (not actions.compare_with_gt('05_04_04_brush-size_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Adjust brush size fail'
    from_pos = (205, 100)
    destination = (205, 510)
    with step('[Verify] snapshot: 05_04_04_before_brush-.png'):
        actions.capture_for_gt('05_04_04_before_brush-.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(205, 100, 205, 510)
    with step('[Verify] snapshot: 05_04_04_after_brush-.png'):
        actions.capture_for_gt('05_04_04_after_brush-.png', crop_rect=(0, 60, 276, 597))
    if (not actions.compare_with_gt('05_04_04_after_brush-.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Eraser - fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_04_04_brush+size_before.png'):
        actions.capture_for_gt('05_04_04_brush+size_before.png', crop_rect=(0, 725, 367, 783))
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_04_04_brush+size_after.png'):
        actions.capture_for_gt('05_04_04_brush+size_after.png', crop_rect=(0, 725, 367, 783))
    if (not actions.compare_with_gt('05_04_04_brush+size_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    from_pos = (205, 100)
    destination = (205, 510)
    with step('[Verify] snapshot: 05_04_04_before_brush+.png'):
        actions.capture_for_gt('05_04_04_before_brush+.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(205, 100, 205, 510)
    with step('[Verify] snapshot: 05_04_04_after_brush+.png'):
        actions.capture_for_gt('05_04_04_after_brush+.png', crop_rect=(0, 60, 276, 597))
    if (not actions.compare_with_gt('05_04_04_after_brush+.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn invert n')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04_04_inverse_brush.png'):
        actions.capture_for_gt('base05_04_04_inverse_brush.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_04_04_leave_brush_x.png'):
        actions.capture_for_gt('05_04_04_leave_brush_x.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_04_04_leave_brush_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn mask switch n')
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnEdge')
    from_pos = (205, 100)
    destination = (205, 510)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(205, 100, 205, 510)
    with step('[Verify] snapshot: 05_04_04_smart_brush_on.png'):
        actions.capture_for_gt('05_04_04_smart_brush_on.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] tap_feature_x_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn mask switch n')
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    from_pos = (205, 100)
    destination = (205, 510)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(205, 100, 205, 510)
    with step('[Verify] snapshot: 05_04_04_smart_brush_off.png'):
        actions.capture_for_gt('05_04_04_smart_brush_off.png', crop_rect=(0, 60, 276, 597))
    if (not actions.compare_with_gt('05_04_04_smart_brush_off.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04_04_tap_brush_v.png'):
        actions.capture_for_gt('base05_04_04_tap_brush_v.png', crop_rect=(0, 60, 276, 597))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_04_04_leave_splash_x.png'):
        actions.capture_for_gt('05_04_04_leave_splash_x.png', crop_rect=(0, 725, 367, 783))
    if actions.compare_with_gt('05_04_04_leave_splash_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Splash')):
        assert False  # legacy raise
    if (not actions.tap_by_coordinates(205, 300)):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_04_04_before_colorshift_x.png'):
        actions.capture_for_gt('05_04_04_before_colorshift_x.png', crop_rect=(0, 60, 276, 597))
    if (not actions.tap_by_locator(AppiumBy.NAME, 'ic color tint n')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeStaticText') == '0'):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0.5)):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04_04_colorshift_mid.png'):
        actions.capture_for_gt('base05_04_04_colorshift_mid.png', crop_rect=(0, 60, 276, 526))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeStaticText') in ('98', '99', '100')):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic reset n')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeStaticText') == '0'):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] adjust_vignette_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0.5)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_04_04_leave_colorshift_x.png'):
        actions.capture_for_gt('05_04_04_leave_colorshift_x.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('05_04_04_leave_colorshift_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic color tint n')
    with step('[Action] adjust_vignette_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0.5)
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04_04_tap_colorshift_v.png'):
        actions.capture_for_gt('base05_04_04_tap_colorshift_v.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00046 completion"):
        assert True
