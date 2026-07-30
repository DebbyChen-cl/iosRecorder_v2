import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00116_main_05_13_01_1n')
def test_00116_main_05_13_01_1n(actions: DriverActions):
    """sticker renew"""
    mode = 1
    uuid = ['4871262e-b110-438a-a617-aa45776176cf', '27a9229e-2819-44d6-b87c-72e9d42eccd3', 'ea2a7430-367c-40e9-b2c5-b630140051a7', '30420d7a-13b0-4588-9dfe-b05664bfa61e', '461dfca5-2061-4463-a740-9939889248da', '565a5505-22b7-47d6-a1da-121efcbe0f61', 'aea3702d-eecb-432a-a966-20f3836be247', '15271efe-229f-45e9-b66e-6ebeb283546c', '2a5e7804-c296-46c2-b4cc-c8e143f45d14', '0aa23e3c-855a-496d-b47a-10655a4719fd', 'd06fef5d-4d17-4138-834e-218fe442aa74', 'c5041816-ff17-43e3-a77d-a6c688192913', 'e5cdd950-1da9-4240-9bfa-299880676de7', '3fd3c20e-f9f3-4080-bd4a-16fd9d865131', '2801a489-5789-4a11-8d9d-595586d69794', 'd600af39-a3f8-4f5f-bab1-d7c7f870836f', '85d97ec9-a6db-4ab0-b555-d6532708c3b4', '25b98e25-19be-436b-860a-12d90088e063', '324aa461-3dcd-42a9-8c8e-5f25cf5d6dcd', '323e1d22-70f5-4d69-af5a-46f0b9969255', 'f5a0073d-13b2-4406-af0d-d6cd5626c4d7', '4f0271d6-e4fb-4772-86e2-7959dd0793b9', '9b58ef5c-8ad7-4a16-9d6d-b12f06bcaa53', '81d26af9-86f1-40ad-aabd-f5e9fd18b111', 'bfa87272-afa3-4ee1-be7d-4d0ba1641ff4', '1a3a5009-c69c-44ae-bdd3-642f5253b64d', '80f8a3a3-3a8b-45d7-af54-4a904877adcd', 'fb13609c-f69f-47b4-9670-5a6270dfd396', '9868fd04-d5b5-4bb7-abb3-1279bb195f9c', 'f2a77b1a-14a9-4158-a748-e8b9c981d0bd', '445ad034-4892-4bfe-a9a6-c7aaf655d9af', '075c0015-eca3-4933-94e3-62f141b18461', 'f7255742-bb90-4125-8587-e0389db61ed9', 'f7255742-bb90-4125-8587-e0389db61ed9', 'f924d993-73ec-4c80-8d21-00dc40a4d901', 'fe75ef74-e7f2-48c4-a18b-a52615a44b9c', '6d9648d8-d9a0-4cb4-886a-9ac373427a12', '30f8971f-6ff2-489d-b3be-b491aa7e01db', '84b4e024-c0d3-4391-af41-48544e9929a1', '8682d821-f754-46ff-9973-507aa62ee216']
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
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Verify] snapshot: 05_13_01_before_sticker.png'):
        actions.capture_for_gt('05_13_01_before_sticker.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sticker')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Static Sticker')
    with step('[Verify] snapshot: 05_13_01_no_sticker.png'):
        actions.capture_for_gt('05_13_01_no_sticker.png')
    with step('[Action] tap_sticker_rotate_handle'):
        assert actions.tap_by_coordinates(360, 790)
    with step('[Verify] snapshot: 05_13_01_after_sticker.png'):
        actions.capture_for_gt('05_13_01_after_sticker.png', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage')
    if (not actions.compare_with_gt('05_13_01_after_sticker.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'apply sticker fail'
    from_pos = (208, 430)
    destination = (170, 350)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(208, 430, 170, 350)
    with step('[Verify] snapshot: 05_13_01_after_move.png'):
        actions.capture_for_gt('05_13_01_after_move.png', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage')
    if (not actions.compare_with_gt('05_13_01_after_move.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'move fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'tap x fail'
    with step('[Action] get_element'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sticker')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Static Sticker')
    with step('[Action] tap_sticker_rotate_handle'):
        assert actions.tap_by_coordinates(360, 790)
    with step('[Verify] snapshot: 05_13_01_before_rotate.png'):
        actions.capture_for_gt('05_13_01_before_rotate.png')
    destination = (120, 430)
    with step('[Action] drag_add_image_rotate'):
        rotate_x, rotate_y, rotate_w, rotate_h = actions.get_element_bounds(
            AppiumBy.IOS_CLASS_CHAIN,
            '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]',
        )
        actions.drag_coordinates(rotate_x + rotate_w // 2, rotate_y + rotate_h // 2, destination[0], destination[1])
    with step('[Verify] snapshot: 05_13_01_after_rotate.png'):
        actions.capture_for_gt('05_13_01_after_rotate.png')
    if (not actions.compare_with_gt('05_13_01_after_rotate.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'rotate fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFlip')):
        assert False, 'tap flip fail'
    with step('[Verify] snapshot: 05_13_01_flip.png'):
        actions.capture_for_gt('05_13_01_flip.png')
    if (not actions.compare_with_gt('05_13_01_flip.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'flip fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0.5')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[2]') in ('47', '48', '49', '50', '51', '52', '53', '54', '55', '56')):
        pass
    else:
        assert False, 'shadow mid value error'
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[2]') in ('97', '98', '99', '100')):
        pass
    else:
        assert False, 'shadow max value error'
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    else:
        assert False, 'shadow min value error'
    with step('[Verify] snapshot: 05_13_01_shadow_off.png'):
        actions.capture_for_gt('05_13_01_shadow_off.png')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Opacity')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False, 'adjust opacity fail'
    with step('[Verify] snapshot: 05_13_01_adjust_opacity_min.png'):
        actions.capture_for_gt('05_13_01_adjust_opacity_min.png')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4', '5')):
        pass
    else:
        assert False, 'adjust opacity to min fail'
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0.5)):
        assert False, 'adjust opacity fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('47', '48', '49', '50', '51', '52', '53', '54', '55', '56')):
        pass
    else:
        assert False, 'adjust opacity to mid fail'
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False, 'adjust opacity fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('97', '98', '99', '100')):
        pass
    else:
        assert False, 'adjust opacity to max fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')):
        assert False, 'tap delete sticker fail'
    with step('[Verify] snapshot: 05_13_01_delete_Sticker.png'):
        actions.capture_for_gt('05_13_01_delete_Sticker.png')
    if (not actions.compare_with_gt('05_13_01_delete_Sticker.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'delete sticker fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] focus_sticker'):
        assert actions.tap_by_coordinates(205, 400)
    with step('[Verify] snapshot: 05_13_01_before_copy.png'):
        actions.capture_for_gt('05_13_01_before_copy.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDuplicate')
    with step('[Verify] snapshot: 05_13_01_after_copy.png'):
        actions.capture_for_gt('05_13_01_after_copy.png')
    if (not actions.compare_with_gt('05_13_01_after_copy.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'duplicate fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] focus_sticker'):
        assert actions.tap_by_coordinates(205, 400)
    with step('[Verify] snapshot: 05_13_01_after_undo.png'):
        actions.capture_for_gt('05_13_01_after_undo.png')
    if actions.compare_with_gt('05_13_01_after_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] focus_sticker'):
        assert actions.tap_by_coordinates(205, 480)
    with step('[Verify] snapshot: 05_13_01_after_redo.png'):
        actions.capture_for_gt('05_13_01_after_redo.png')
    if actions.compare_with_gt('05_13_01_after_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'tap v fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Verify] snapshot: 05_13_01_v.png'):
        actions.capture_for_gt('05_13_01_v.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if actions.compare_with_gt('05_13_01_v.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tap v fail'
    element = ['save_to_file4', 'save_to_file3', 'save_to_file2', 'save_to_file']
    if not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'exportButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnSave')]):
        assert False, 'tap save fail'
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=3)
    with step('[Action] close_rate_us_photo'):
        if actions.is_element_present(AppiumBy.NAME, 'Your Photo Looks Perfect!', timeout=5):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
    with step('[Action] tap_share_to_more_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'More')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="shareCell" and @label="U"]')
    with step('[Verify] snapshot: 05_13_01_share_U.png'):
        actions.capture_for_gt('05_13_01_share_U.png')
    if actions.compare_with_gt('05_13_01_share_U.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'share to U fail'
    with step('[Action] tap_share_to_more_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'More')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step('[Action] tap_share_to_message_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_PREDICATE, 'name == "shareCell" AND label == "Messages"')
        assert actions.find_element(AppiumBy.IOS_PREDICATE, 'label == "New Message"')
    with step('[Action] Tap'):
        assert actions.tap_by_coordinates(406, 105)
    with step('[Action] Tap'):
        assert actions.tap_by_coordinates(48, 89)
    with step('[Action] tap_share_to_IG_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Instagram')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram')
    with step('[Action] back_to_phd_from_sns'):
        actions.activate_app('com.cyberlink.photodirector')
    with step('[Action] tap_share_to_FB_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Post')
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Verify] snapshot: 05_13_01_tap_back_to_home.png'):
        actions.capture_for_gt('05_13_01_tap_back_to_home.png')
    with step("[Verify] test_00116 completion"):
        assert True
