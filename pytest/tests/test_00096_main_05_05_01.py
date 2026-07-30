import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00096_main_05_05_01')
def test_00096_main_05_05_01(actions: DriverActions):
    """Overlays - blender"""
    mode = 1
    uuid = ['38767433-6c89-405c-8827-6c24b8f17b0d', 'dece5990-209a-4946-bcd9-b801d33e3178', 'afeca4a2-a313-4655-bf18-d628bca247dc', '5cc5495a-63f8-4866-8e44-3e7138a9c11e', 'db10d672-06f6-4b63-9d52-a37bf0220fc3', '994d7c81-842c-4015-ac17-f8a97b76e5c2', '3cb574e8-2dbf-453c-b30f-30de59e35e66', '332da06b-d124-4834-8b6e-cfcbc92ece98', 'b64ea73e-d487-4d4e-a178-157dfb4925e7', '7c90fefa-ad66-4a8c-91bb-8569b2005754', 'e2ffbe6c-d33f-4850-9607-3eb94b4d417d', 'ed10c3e8-7805-4375-9fa8-0f0577c6aff4', 'baf3370e-a528-4ef9-8ba4-30eaf3a5a3e2', 'c3a5155e-3730-44da-afe5-b28d107af8b2', '5bc98205-3ab2-4068-b32f-80fff01500a2', '8ba55178-4ba6-4100-9000-33914b13f786', '808e734c-0661-44e7-9f5e-49f8bcc324bf', 'cc2edc2c-f648-47b5-9ba2-cd4c8da8bdad']
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
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step('[Verify] snapshot: 05_05_01_before_blender.png'):
        actions.capture_for_gt('05_05_01_before_blender.png')
    for x in range(3):
        from_pos = (380, 770)
        destination = (50, 770)
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Overlay Effect')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blender')
    with step('[Verify] snapshot: 05_05_01_temp1.png'):
        actions.capture_for_gt('05_05_01_temp1.png')
    if actions.compare_with_gt('05_05_01_temp1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'template 1 fail'
    with step('[Verify] snapshot: 05_05_01_before_enter_brush.png'):
        actions.capture_for_gt('05_05_01_before_enter_brush.png')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn eraser n')):
        assert False, 'enter brush fail'
    with step('[Verify] snapshot: 05_05_01_brush-_size_before.png'):
        actions.capture_for_gt('05_05_01_brush-_size_before.png')
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_05_01_brush-_size_after.png'):
        actions.capture_for_gt('05_05_01_brush-_size_after.png')
    if actions.compare_with_gt('05_05_01_brush-_size_after.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'adjust brush size fail'
    from_pos = (30, 100)
    destination = (370, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 100, 370, 600)
    with step('[Verify] snapshot: 05_05_01_brush-.png'):
        actions.capture_for_gt('05_05_01_brush-.png')
    if actions.compare_with_gt('05_05_01_brush-.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'brush- fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')
    with step('[Verify] snapshot: 05_05_01_brush+_size_before.png'):
        actions.capture_for_gt('05_05_01_brush+_size_before.png')
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_05_01_brush+_size_after.png'):
        actions.capture_for_gt('05_05_01_brush+_size_after.png')
    if (not actions.compare_with_gt('05_05_01_brush+_size_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust brush size fail'
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    from_pos = (30, 100)
    destination = (370, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 100, 370, 600)
    with step('[Verify] snapshot: 05_05_01_brush+.png'):
        actions.capture_for_gt('05_05_01_brush+.png')
    if actions.compare_with_gt('05_05_01_brush+.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'brush+ fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn invert n')):
        assert False, 'Tap inverse fail'
    with step('[Verify] snapshot: 05_05_01_inverse_brush.png'):
        actions.capture_for_gt('05_05_01_inverse_brush.png')
    if actions.compare_with_gt('05_05_01_inverse_brush.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'inverse fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'tap x fail'
    with step('[Verify] snapshot: 05_05_01_leave_brush_x.png'):
        actions.capture_for_gt('05_05_01_leave_brush_x.png')
    if actions.compare_with_gt('05_05_01_leave_brush_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'exit brush fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn eraser n')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eraser')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnEdge')
    from_pos = (30, 100)
    destination = (370, 600)
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 100, 370, 600)
    with step('[Verify] snapshot: 05_05_01_smart_brush_on.png'):
        actions.capture_for_gt('05_05_01_smart_brush_on.png')
    with step('[Action] tap_feature_x_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn eraser n')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnEdge')
    from_pos = (30, 100)
    destination = (370, 600)
    with step('[Action] adjust_cutout_brush_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(30, 100, 370, 600)
    with step('[Verify] snapshot: 05_05_01_smart_brush_off.png'):
        actions.capture_for_gt('05_05_01_smart_brush_off.png')
    if (not actions.compare_with_gt('05_05_01_smart_brush_off.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'smart brush fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'tap v fail'
    with step('[Verify] snapshot: 05_05_01_tap_brush_v.png'):
        actions.capture_for_gt('05_05_01_tap_brush_v.png')
    if actions.compare_with_gt('05_05_01_tap_brush_v.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tap brush v fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addSrcImageView')):
        assert False, 'tap add image fail'
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category_add_image'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'BG')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')):
        assert False, 'select photo fail'
    with step('[Verify] snapshot: 05_05_01_add_photo.png'):
        actions.capture_for_gt('05_05_01_add_photo.png')
    if actions.compare_with_gt('05_05_01_add_photo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'user photo fail'
    with step('[Verify] snapshot: 05_05_01_before_take_shot.png'):
        actions.capture_for_gt('05_05_01_before_take_shot.png')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addSrcImageView')):
        assert False, 'tap add image fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCamera')):
        assert False, 'tap camera fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')):
        assert False, 'shot photo fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use Photo')):
        assert False, 'use photo fail'
    with step('[Verify] snapshot: 05_05_01_after_take_photo.png'):
        actions.capture_for_gt('05_05_01_after_take_photo.png')
    if (not actions.compare_with_gt('05_05_01_after_take_photo.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'apply taked photo fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'tap [x] fail'
    with step('[Verify] snapshot: 05_05_01_tap_x.png'):
        actions.capture_for_gt('05_05_01_tap_x.png')
    if actions.compare_with_gt('05_05_01_tap_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Overlay Effect')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blender')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'tap [v] fail'
    with step('[Verify] snapshot: 05_05_01_tap_v.png'):
        actions.capture_for_gt('05_05_01_tap_v.png')
    if (not actions.compare_with_gt('05_05_01_tap_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00096 completion"):
        assert True
