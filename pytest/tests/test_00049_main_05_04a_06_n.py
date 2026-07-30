import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00049_main_05_04a_06_n')
def test_00049_main_05_04a_06_n(actions: DriverActions):
    """Instafill renew"""
    mode = 1
    uuid = ['10d744ed-3801-4b02-8153-f941c4058b47', '499d7f2f-6bf3-41dd-ab95-ee1571040d38', '589d7e54-6743-4418-89dd-e70a16e8e2f3', '16d6ea3b-d159-4ee2-b584-3145a44b6fe9', 'b767be20-89ef-476d-8ebd-b06d0afca8ac', '94bf7118-967d-4503-b906-b0ebed5de2d8', 'bfd0a019-39aa-46be-8e89-8d0add30fe39', '37ee7408-51e2-4c8f-9e01-9c715b7277ba', '2e2d3583-af39-4bfe-a483-90d586c05a85', '8659cdf7-01d8-4f7e-b338-b16b805831b7', 'f2b67f8d-7d1e-43bf-8679-553c00cd22cd', 'af861fc4-a47c-40b5-a562-685b7c9e60f8', 'cf9b67d4-c31c-4455-ab43-dbac2197ebf4', '51ee0867-895d-4d73-a3da-dc647ddb3928', '5e5b1469-375f-4547-b24f-ee6f05231658', '0f895bd8-1380-4f0e-8ab5-6a255af66ea7', '95fc9cf9-3709-408f-87c2-090b23d4569b']
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Verify] snapshot: 05_04a_06_before_enter_instafill.png'):
        actions.capture_for_gt('05_04a_06_before_enter_instafill.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'InstaFill')
    with step('[Verify] snapshot: base05_04a_06_square.png'):
        actions.capture_for_gt('base05_04a_06_square.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step('[Verify] snapshot: base05_04a_06_4_3.png'):
        actions.capture_for_gt('base05_04a_06_4_3.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_04a_06_4_3.png'):
        assert actions.compare_with_gt('05_04a_06_4_3.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')
    with step('[Verify] snapshot: base05_04a_06_3_2.png'):
        actions.capture_for_gt('base05_04a_06_3_2.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_04a_06_4_3.png'):
        assert actions.compare_with_gt('05_04a_06_4_3.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    with step('[Verify] snapshot: base05_04a_06_16_9.png'):
        actions.capture_for_gt('base05_04a_06_16_9.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_04a_06_16_9.png'):
        assert actions.compare_with_gt('05_04a_06_16_9.png', gt_folder=TD.GT_FOLDER)[0]
    from_pos = (400, 777)
    destination = (20, 777)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 777, 20, 777)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feed')
    with step('[Verify] snapshot: base05_04a_06_feed.png'):
        actions.capture_for_gt('base05_04a_06_feed.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_04a_06_feed.png'):
        assert actions.compare_with_gt('05_04a_06_feed.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Story')
    with step('[Verify] snapshot: base05_04a_06_story.png'):
        actions.capture_for_gt('base05_04a_06_story.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_04a_06_story.png'):
        assert actions.compare_with_gt('05_04a_06_story.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Profile')
    with step('[Verify] snapshot: base05_04a_06_profile.png'):
        actions.capture_for_gt('base05_04a_06_profile.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_04a_06_profile.png'):
        assert actions.compare_with_gt('05_04a_06_profile.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cover')
    with step('[Verify] snapshot: base05_04a_06_cover.png'):
        actions.capture_for_gt('base05_04a_06_cover.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_04a_06_cover.png'):
        assert actions.compare_with_gt('05_04a_06_cover.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: base05_04a_06_blur_min.png'):
        actions.capture_for_gt('base05_04a_06_blur_min.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: base05_04a_06_blur_max.png'):
        actions.capture_for_gt('base05_04a_06_blur_max.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_04a_06_blur_max.png'):
        assert actions.compare_with_gt('05_04a_06_blur_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step('[Action] tap_instafill_bg_color_picker'):
        assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'colorWheelImgView'), (AppiumBy.ACCESSIBILITY_ID, 'pickedColorView')]), 'tap instafill bg color picker button fail'
    with step('[Action] select_color'):
        actions.tap_by_coordinates(315, 708)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step('[Verify] snapshot: 05_04a_06_bg_picker.png'):
        actions.capture_for_gt('05_04a_06_bg_picker.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'BG')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Verify] snapshot: 05_04a_06_bg_user.png'):
        actions.capture_for_gt('05_04a_06_bg_user.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeCell[@name="CMS-"])[2]')
    with step('[Verify] snapshot: 05_04a_06_bg_solid.png'):
        actions.capture_for_gt('05_04a_06_bg_solid.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] snapshot: 05_04a_06_bg_solid1.png'):
        actions.capture_for_gt('05_04a_06_bg_solid1.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell[2]')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_BG_Wall_03_free_trending')
    with step('[Verify] snapshot: 05_04a_06_bg_temp1.png'):
        actions.capture_for_gt('05_04a_06_bg_temp1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'tap [x] button fail'
    with step('[Verify] snapshot: 05_04a_06_x.png'):
        actions.capture_for_gt('05_04a_06_x.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if actions.compare_with_gt('05_04a_06_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tap [x] button fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'InstaFill')
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_04a_06_v.png'):
        actions.capture_for_gt('05_04a_06_v.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    if (not actions.compare_with_gt('05_04a_06_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'tap done button fail'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00049 completion"):
        assert True
