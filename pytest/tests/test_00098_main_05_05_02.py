import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00098_main_05_05_02')
def test_00098_main_05_05_02(actions: DriverActions):
    """Overlays - light leak"""
    mode = 1
    uuid = ['5c221155-2952-4fb7-bb9a-5dfdf8ac15f0', '6b501129-0f85-4d2f-83ce-9ddd126dfbcd', 'a4dc8d0a-4b99-4906-ae68-493a6fe5f7f4', 'dcce1044-d6b6-48d1-b902-f6804b933f7a', 'c388d4b2-48a4-4b99-9616-18adfb2bf9e5', 'ce301e0d-5486-4026-bfea-1ab465bb438e', '4c2b8469-14c3-48e7-b2e8-a7736bf8a8af', '63072a38-cb20-4786-9c6c-393ccc507b0e', '25faceb4-926b-44b2-afd2-c9e4ceae2925', '1c6a069d-9e8b-4396-898d-458e75e86eaa', '41997812-aff1-4211-b6b1-e0853d3252ea', '3a613be5-50f0-4095-8542-bdd9fb5b819f', 'a1803b3e-5785-4418-8f57-04264abbded7', '69497f8c-1ec1-41fb-8e63-a7657c30f02e', 'b878f711-849f-4dc9-a0de-3b57a5f2d6b4', '2f9b58d8-5b1a-4766-a7bf-e41f05062369', '013ab4ab-7af5-4bc4-be08-d9f91df63c38', 'd507d81a-0fab-4bea-beff-e2295c3cb99d', 'be36eb66-6e14-42fc-b71a-e9c3de67e76c', 'f6a9ac6f-8a36-4a44-8e27-9911cd74752b']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit')
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
    for x in range(3):
        from_pos = (380, 770)
        destination = (50, 770)
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Verify] snapshot: 05_05_02_before_lightleak.png'):
        actions.capture_for_gt('05_05_02_before_lightleak.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Overlay Effect')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light Leak')
    with step('[Verify] snapshot: 05_05_02_temp1.png'):
        actions.capture_for_gt('05_05_02_temp1.png')
    if actions.compare_with_gt('05_05_02_temp1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'template 1 fail'
    with step('[Action] adjust_overlays_slider'):
        assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)
    with step('[Verify] snapshot: 05_05_02_slider_left.png'):
        actions.capture_for_gt('05_05_02_slider_left.png')
    if actions.compare_with_gt('05_05_02_slider_left.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_overlays_slider'):
        assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)
    with step('[Verify] snapshot: 05_05_02_slider_right.png'):
        actions.capture_for_gt('05_05_02_slider_right.png')
    if actions.compare_with_gt('05_05_02_slider_right.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'max fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')):
        assert False, 'tap rotate fail'
    with step('[Verify] snapshot: 05_05_02_rotate_90.png'):
        actions.capture_for_gt('05_05_02_rotate_90.png')
    if actions.compare_with_gt('05_05_02_rotate_90.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'rotate 90 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')):
        assert False, 'tap rotate fail'
    with step('[Verify] snapshot: 05_05_02_rotate_180.png'):
        actions.capture_for_gt('05_05_02_rotate_180.png')
    if actions.compare_with_gt('05_05_02_rotate_180.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'rotate 180 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')):
        assert False, 'tap rotate fail'
    with step('[Verify] snapshot: 05_05_02_rotate_270.png'):
        actions.capture_for_gt('05_05_02_rotate_270.png')
    if actions.compare_with_gt('05_05_02_rotate_270.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'rotate 270 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')):
        assert False, 'tap rotate fail'
    with step('[Verify] snapshot: 05_05_02_rotate_360.png'):
        actions.capture_for_gt('05_05_02_rotate_360.png')
    if actions.compare_with_gt('05_05_02_rotate_360.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'rotate 360 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_flipH_n')):
        assert False, 'tap flip h fail'
    with step('[Verify] snapshot: 05_05_02_flip_H.png'):
        actions.capture_for_gt('05_05_02_flip_H.png')
    if actions.compare_with_gt('05_05_02_flip_H.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'flip h fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_flipV_n')):
        assert False, 'tap flip h 2 fail'
    with step('[Verify] snapshot: 05_05_02_flip_H2.png'):
        actions.capture_for_gt('05_05_02_flip_H2.png')
    if actions.compare_with_gt('05_05_02_flip_H2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'flip h 2 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_flipV_n')):
        assert False, 'tap flip v fail'
    with step('[Verify] snapshot: 05_05_02_flip_v.png'):
        actions.capture_for_gt('05_05_02_flip_v.png')
    if actions.compare_with_gt('05_05_02_flip_v.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'flip v fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_flipV_n')):
        assert False, 'tap flip v 2 fail'
    with step('[Verify] snapshot: 05_05_02_flip_v2.png'):
        actions.capture_for_gt('05_05_02_flip_v2.png')
    if actions.compare_with_gt('05_05_02_flip_v2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'flip v 2 fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'tap [x] fail'
    with step('[Verify] snapshot: 05_05_02_tap_x.png'):
        actions.capture_for_gt('05_05_02_tap_x.png')
    if actions.compare_with_gt('05_05_02_tap_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Overlay Effect')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light Leak')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'tap [v] fail'
    with step('[Verify] snapshot: 05_05_02_tap_v.png'):
        actions.capture_for_gt('05_05_02_tap_v.png')
    if (not actions.compare_with_gt('05_05_02_tap_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00098 completion"):
        assert True
