import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00120_main_05_11_01_2')
def test_00120_main_05_11_01_2(actions: DriverActions):
    """add-image crop and rotate"""
    mode = 1
    uuid = ['2ca62fd8-1dc7-409d-882d-d67ac651764f', '2f7fa1bc-40a1-4484-83ea-7acbb1e2875d', 'c77c898a-463d-4122-a9ec-b4c367ab1dba', '2cde7ed6-dca7-4a6f-b77c-5eb78573c130', 'fa1856f0-b3ad-47bc-924b-2f50f0bc85e5', 'c505464f-2cb2-4b36-a8cb-6e5d232156c1', 'a3906e21-b017-4f63-852a-43782190e58c', 'c8cbad71-1c44-42d2-b874-9e71323621ad', '7c75148f-9766-4560-aa04-05ac5335cc83', 'ed13c21c-82eb-448e-823c-d6219f52a6d6', '8d8df0dd-0a32-4d5c-945b-9be04f2dfe8a', '370420e7-9d8f-452f-b8ec-4262de83af89', '2832eac2-d766-45c6-8772-a49ea874c911', 'ba10e01d-5734-4e09-912f-ce2eb02cc8bf', '40b9f62d-f489-44b0-ba7b-abc1fe805861', '1744fa75-2d7f-4a5d-ad33-7d10613c834c']
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
    with step('[Action] select_category_add_image'):
        assert actions.tap_by_locator(AppiumBy.NAME, '_AT')
    with step('[Action] add_image'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Verify] snapshot: 05_11_01_before_crop_rotate.png'):
        actions.capture_for_gt('05_11_01_before_crop_rotate.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_rotate90.png'):
        actions.capture_for_gt('05_11_01_rotate90.png')
    if actions.compare_with_gt('05_11_01_rotate90.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'rotate 90 deg comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Horizontally')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_flip_h.png'):
        actions.capture_for_gt('05_11_01_flip_h.png')
    if actions.compare_with_gt('05_11_01_flip_h.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'flip horizontal comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Vertically')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_flip_v.png'):
        actions.capture_for_gt('05_11_01_flip_v.png')
    if actions.compare_with_gt('05_11_01_flip_v.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'flip vertical comparison failed'
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_tilt45.png'):
        actions.capture_for_gt('05_11_01_tilt45.png')
    if actions.compare_with_gt('05_11_01_tilt45.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'tilt 45 degree comparison failed'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Square')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_square.png'):
        actions.capture_for_gt('05_11_01_square.png')
    if actions.compare_with_gt('05_11_01_square.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'square comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_4v3.png'):
        actions.capture_for_gt('05_11_01_4v3.png')
    if actions.compare_with_gt('05_11_01_4v3.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '4:3 comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:4')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_3v4.png'):
        actions.capture_for_gt('05_11_01_3v4.png')
    if actions.compare_with_gt('05_11_01_3v4.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '3:4 comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_3v2.png'):
        actions.capture_for_gt('05_11_01_3v2.png')
    if actions.compare_with_gt('05_11_01_3v2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '3:2 comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '2:3')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_2v3.png'):
        actions.capture_for_gt('05_11_01_2v3.png')
    if actions.compare_with_gt('05_11_01_2v3.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '2:3 comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_16v9.png'):
        actions.capture_for_gt('05_11_01_16v9.png')
    if actions.compare_with_gt('05_11_01_16v9.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '16:9 comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '9:16')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_9v16.png'):
        actions.capture_for_gt('05_11_01_9v16.png')
    if actions.compare_with_gt('05_11_01_9v16.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '9:16 comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feed')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_feed.png'):
        actions.capture_for_gt('05_11_01_feed.png')
    if actions.compare_with_gt('05_11_01_feed.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'feed comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Story')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_story.png'):
        actions.capture_for_gt('05_11_01_story.png')
    if actions.compare_with_gt('05_11_01_story.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'story comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Profile')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_profile.png'):
        actions.capture_for_gt('05_11_01_profile.png')
    if actions.compare_with_gt('05_11_01_profile.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'profile comparison failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cover')):
        assert False, 'test failed'
    with step('[Verify] snapshot: 05_11_01_cover.png'):
        actions.capture_for_gt('05_11_01_cover.png')
    if actions.compare_with_gt('05_11_01_cover.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'cover comparison failed'
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_11_01_after_crop_rotate.png'):
        actions.capture_for_gt('05_11_01_after_crop_rotate.png')
    if actions.compare_with_gt('05_11_01_after_crop_rotate.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'apply crop and rotate comparison failed'
    with step("[Verify] test_00120 completion"):
        assert True
