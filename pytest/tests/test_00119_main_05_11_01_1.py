import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00119_main_05_11_01_1')
def test_00119_main_05_11_01_1(actions: DriverActions):
    """add image - move, boundary box operation, opacity"""
    mode = 1
    uuid = ['d537fd8a-95a0-438a-ba75-0ea4e30b83bb', '3ef0769b-143a-4b3e-9513-a4e36715adbd', '24d29e0e-e51a-4bb0-8446-1c0a7089cc9f', 'b517bf14-ade1-4121-8c26-d590c848005b', 'b8c87629-b008-4dd8-8209-317006103b42', 'c4cd54ef-c9b1-4692-b427-a1807e330b4f', '5bc6d4f1-c591-4e5d-8ec9-344ebda7c166', 'c3944fc1-76df-4195-8e23-87fe0037684f', '8fb2a71a-5067-4817-9d34-cd93ae00611b', '4660fe2c-4692-4e0d-8fb6-f20e6f3738ab', 'd0b33eb3-2d08-460e-bf12-7f6701f3bbdf', 'a006b8d6-e2b5-412c-ad5d-64b5a722488f', '3e6ad9fd-f529-4c89-a452-c1296975640a']
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
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    if (actions.tap_by_locator(AppiumBy.NAME, '_AT') and actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')):
        pass
    else:
        assert False, 'test failed'
    from_pos = (208, 430)
    destination = (170, 350)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(208, 430, 170, 350)
    with step('[Verify] snapshot: 05_11_01_move.png'):
        actions.capture_for_gt('05_11_01_move.png')
    if actions.compare_with_gt('05_11_01_move.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'move comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'test failed'
    with step('[Action] get_element'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category_add_image'):
        actions.tap_by_locator(AppiumBy.NAME, '_AT')
    with step('[Action] add_image'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    destination = (364, 624)
    with step('[Action] drag_add_image_rotate'):
        rotate_x, rotate_y, rotate_w, rotate_h = actions.get_element_bounds(
            AppiumBy.IOS_CLASS_CHAIN,
            '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]',
        )
        actions.drag_coordinates(rotate_x + rotate_w // 2, rotate_y + rotate_h // 2, destination[0], destination[1])
    with step('[Verify] snapshot: 05_11_01_rotate.png'):
        actions.capture_for_gt('05_11_01_rotate.png')
    if actions.compare_with_gt('05_11_01_rotate.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'resize/rotate comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFlip')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_flip.png'):
        actions.capture_for_gt('05_11_01_flip.png')
    if actions.compare_with_gt('05_11_01_flip.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'flip comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Opacity')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_opacity_min.png'):
        actions.capture_for_gt('05_11_01_opacity_min.png')
    if actions.compare_with_gt('05_11_01_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity_min comparison failed'
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0.5)):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_opacity_mid.png'):
        actions.capture_for_gt('05_11_01_opacity_mid.png')
    if actions.compare_with_gt('05_11_01_opacity_mid.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity_mid comparison failed'
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_opacity_max.png'):
        actions.capture_for_gt('05_11_01_opacity_max.png')
    if actions.compare_with_gt('05_11_01_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity_max comparison failed'
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Verify] snapshot: 05_11_01_after_addimg.png'):
        actions.capture_for_gt('05_11_01_after_addimg.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Verify] compare: 05_11_01_after_addimg.png'):
        assert actions.compare_with_gt('05_11_01_after_addimg.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCamera')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use Photo')
    with step("[Verify] test_00119 completion"):
        assert True
