import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00182_motion_swap_01')
def test_00182_motion_swap_01(actions: DriverActions):
    """Motion Swap"""

    with step('Close any popups'):
        with step('[Action] close_xmas'):
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Close', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Close')
        with step('[Action] close_continue_edit'):
            if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('Tap Character motion swap entry'):
        with step('[Action] tap_character_motion_swap_entry'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Character Motion Swap')
    with step('Verify intro page displays'):
        with step('[Action] verify_intro_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'AIFeatureDemoViewController')
    with step('Check Dont show again'):
        with step('[Action] check_intro_dont_show_again'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
    with step('Tap Try now'):
        with step('[Action] tap_try_now'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Tap ? button'):
        if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnInfoMode')):
            assert False, 'Failed to tap ? button'
    with step('Verify intro dialog displays'):
        with step('[Action] verify_intro_dialog'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Character Motion Swap')
    with step('Tap Try now'):
        with step('[Action] tap_dlg_try_now'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Tap Import of photo'):
        with step('[Action] tap_import_photo'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step('Verify recommendation dialog pops up'):
        if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel', timeout=5)):
            assert False, 'Recommendation dialog not displayed'
        else:
            with step('Check Dont show again'):
                with step('[Action] check_dont_show_again'):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox')
            with step('Tap continue'):
                with step('[Action] tap_continue'):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Expand album list'):
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('Select _AT album'):
        category = '_AT'
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('Select a full body photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('Verify imported photo thumbnail is displayed'):
        with step('[Action] get_element'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace')
        with step('[Verify] snapshot: motion_swap_photo_thumbnail.png'):
            actions.capture_for_gt('motion_swap_photo_thumbnail.png')
        with step('[Verify] compare: motion_swap_photo_thumbnail.png'):
            assert actions.compare_with_gt('motion_swap_photo_thumbnail.png', gt_folder=TD.GT_FOLDER)[0]
    with step('Tap the thumbnail of photo'):
        with step('[Action] tap_photo_thumbnail'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace')
    with step('Tap i button'):
        with step('[Action] tap_info_photo'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic info n')
    with step('Verify recommendation dialog pops up'):
        with step('[Action] verify_recommendation_dialog'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel')
    with step('Tap continue'):
        with step('[Action] tap_continue'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Expand album list'):
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('Select _AT album'):
        category = '_AT'
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('Select another photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step('Verify photo thumbnail is updated'):
        with step('[Action] get_element'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace')
        with step('[Verify] snapshot: motion_swap_photo_thumbnail_updated.png'):
            actions.capture_for_gt('motion_swap_photo_thumbnail_updated.png')
        with step('[Verify] compare: motion_swap_photo_thumbnail_updated.png'):
            assert actions.compare_with_gt('motion_swap_photo_thumbnail_updated.png', gt_folder=TD.GT_FOLDER)[0]
    with step('Tap import of reference video'):
        with step('[Action] tap_import_video'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference')
    with step('Verify recommendation page displays'):
        if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'recommendationLbl', timeout=20)):
            assert False, 'Recommendation page not displayed - may have been dismissed before'
        else:
            with step('Step 28: Tap continue'):
                with step('[Action] tap_continue'):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Select a video'):
        with step('[Action] select_video'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collections')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_Video')
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "PXGGridLayout-Info"`][2]')
    with step('Tap choose of video preview'):
        with step('[Action] tap_choose_video'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Choose')
    with step('Adjust trim start/end edge'):
        with step('[Action] adjust_trim_edges'):
            _sx, _sy, _sw, _sh = actions.get_element_bounds(AppiumBy.ACCESSIBILITY_ID, 'startBarImageView')
            _ex, _ey, _ew, _eh = actions.get_element_bounds(AppiumBy.ACCESSIBILITY_ID, 'endBarImageView')
            actions.drag_coordinates(_sx + _sw // 2, _sy + _sh // 2, _sx + _sw // 2 + 20, _sy + _sh // 2)
            actions.drag_coordinates(_ex + _ew // 2, _ey + _eh // 2, _ex + _ew // 2 - 50, _ey + _eh // 2)
    with step('Move trim range'):
        with step('[Action] move_trim_range'):
            _tx, _ty, _tw, _th = actions.get_element_bounds(AppiumBy.ACCESSIBILITY_ID, 'slidingWindow')
            actions.drag_coordinates(_tx + _tw // 2, _ty + _th // 2, _tx + _tw // 2 + 15, _ty + _th // 2)
    with step('Verify duration length info'):
        with step('[Action] verify_duration_info'):
            assert actions.get_text(AppiumBy.NAME, 'lblDesc') == 'Selected Length: 00:05', 'Duration info verification failed'
    with step('Tap continue'):
        with step('[Action] tap_continue'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Verify imported video thumbnail is displayed'):
        with step('[Action] get_element'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference')
        with step('[Verify] snapshot: motion_swap_video_thumbnail_updated.png'):
            actions.capture_for_gt('motion_swap_video_thumbnail_updated.png')
        with step('[Verify] compare: motion_swap_video_thumbnail_updated.png'):
            assert actions.compare_with_gt('motion_swap_video_thumbnail_updated.png', gt_folder=TD.GT_FOLDER)[0]
    with step('Tap Keep the photo background'):
        with step('[Action] tap_keep_photo_background'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Keep the photo background')
    with step('Tap Generate'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify new video is under processing in My artwork'):
        with step('[Action] verify_my_artwork_processing'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Character Motion Swap')
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing')
    with step('Tap back'):
        with step('[Action] tap_back'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Tap artwork entry'):
        with step('[Action] tap_artwork'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navArtworkButton')
    with step('Verify My artwork highlights Character motion swap category'):
        with step('[Action] verify_my_artwork_category'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Character Motion Swap')
    with step('Tap thumbnail of reference video'):
        for _ in range(40):
            if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing', timeout=10)):
                break
        with step('[Action] show_video_thumbnail'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_artwork_error_thumbnail')
    with step('Tap Create more'):
        with step('[Action] tap_create_more'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Create More')
    with step('Select another video'):
        with step('[Action] tap_import_photo'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step('[Action] tap_import_video'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference')
    if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'recommendationLbl', timeout=20)):
        assert False, 'Recommendation page not displayed - may have been dismissed before'
    else:
        with step('[Action] tap_continue'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] select_video'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collections')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_Video')
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "PXGGridLayout-Info"`][2]')
    with step('[Action] tap_choose_video'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Choose')
    with step('[Action] tap_continue'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] tap_import_video'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference')
    if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'recommendationLbl', timeout=20)):
        pass
    else:
        with step('[Action] tap_continue'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] select_video'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collections')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_Video')
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "PXGGridLayout-Info"`][1]')
    with step('Tap choose of video preview'):
        with step('[Action] tap_choose_video'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Choose')
    with step('[Action] tap_continue'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] get_element'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference')
    with step('[Verify] snapshot: motion_swap_video_thumbnail_updated.png'):
        actions.capture_for_gt('motion_swap_video_thumbnail_updated.png')
    if actions.compare_with_gt('motion_swap_video_thumbnail_updated.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'Video thumbnail update verification failed - screenshot does not match ground truth'
    with step('[Action] tap_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step('[Action] verify_back_to_launcher'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Verify] test_00182 completion"):
        assert True
