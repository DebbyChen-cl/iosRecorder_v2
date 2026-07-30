import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00013_main_04_01_03')
def test_00013_main_04_01_03(actions: DriverActions):
    """camera - preview"""
    uuid = ['14e99c96-cf13-413e-b9a1-72ecd1d79f26', '41554416-1934-4b42-a1a5-e90b97954ee3', 'e989cb3d-a3e2-4e97-9bae-6e736b051626', '1b906b3b-de59-4b4c-bebf-a05e42728d46', '1b222756-d350-4bad-ad01-4c292ce5f142', 'aed91d66-e468-4a32-afc6-1472ded02f47', '98655e6a-23af-4423-b277-3abbfe6b5ff5', '4d847cdd-117e-4301-aaae-661154ef543d', 'c5cd9d9a-861a-4da9-89c3-eb1c7aec3a2b', '9eb349dc-da6c-4687-bec4-3db095904b5c', '0427946d-a9f5-4e4c-97b9-dc4c59706bb9', '491e2e01-adb9-4487-b382-c9fe4d652141', '9f4ea468-829b-4a11-8ee7-28a09e9a7cdb', '849d967b-99b0-46ba-9deb-3f2eaf29fd25']
    with step('[Action] close_continue_edit'):
        actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_camera'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnMore')
    with step('[Action] tap_picker_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Album')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton')
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="shareCell" and @label="U"]')):
        assert False  # legacy raise
    with step('[Action] close_share_menu'):
        assert actions.tap_by_coordinates(150, 200)
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton')):
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.IOS_PREDICATE, 'name == "shareCell" AND label == "Messages"')):
        assert False  # legacy raise
    with step('[Action] tap_share_to_message_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_PREDICATE, 'name == "shareCell" AND label == "Messages"')
        assert actions.find_element(AppiumBy.IOS_PREDICATE, 'label == "New Message"')
    with step('[Action] Tap'):
        assert actions.tap_by_coordinates(406, 105)
    with step('[Action] tap'):
        assert actions.tap_by_coordinates(110, 115)
    with step('[Action] tap_edit_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'editButton')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'settingButton')
    with step('[Verify] snapshot: 04_01_03_edit.png'):
        actions.capture_for_gt('04_01_03_edit.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_edit_home'):
        assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome')])
    with step('[Verify] snapshot: 04_01_03_tap_home.png'):
        actions.capture_for_gt('04_01_03_tap_home.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] tap_camera'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnMore')
    with step('[Action] tap_picker_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Album')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton')
    with step('[Action] tap_picker_camera_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    with step('[Action] tap_picker_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Album')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton')
    with step('[Action] tap_allphoto_btn'):
        assert (actions.is_element_present(AppiumBy.NAME, 'Select Photo') or actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Recents'))
    with step('[Action] tap_picker_camera_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    with step('[Action] tap_picker_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Album')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton')
    with step('[Action] tap_allphoto_btn'):
        assert (actions.is_element_present(AppiumBy.NAME, 'Select Photo') or actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Recents'))
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Recents')
    with step('[Action] select_photo'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'editButton')
    with step('[Action] tap_allphoto_btn'):
        assert (actions.is_element_present(AppiumBy.NAME, 'Select Photo') or actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Recents'))
    with step('[Verify] snapshot: 04_01_03_before_change_category.png'):
        actions.capture_for_gt('04_01_03_before_change_category.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'BG')
    with step('[Verify] snapshot: 04_01_03_after_change_category.png'):
        actions.capture_for_gt('04_01_03_after_change_category.png', crop_rect=(0, 60, 276, 597))
    if actions.compare_with_gt('04_01_03_before_change_category.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'Change category fail'
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Recents')
    with step('[Action] tap_picker_camera_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_picker_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Album')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton')
    with step('[Verify] snapshot: 04_01_03_before_delete.png'):
        actions.capture_for_gt('04_01_03_before_delete.png', crop_rect=(0, 60, 276, 597))
    with step('[Action] tap_delete_btn2'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'deleteButton')
        assert actions.is_element_present(AppiumBy.NAME, 'Allow “PhotoDirector” to delete this photo?')
    if (not actions.tap_by_locator(AppiumBy.NAME, 'Delete')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_03_after_delete.png'):
        actions.capture_for_gt('04_01_03_after_delete.png', crop_rect=(0, 60, 276, 597))
    if (not actions.compare_with_gt('04_01_03_before_delete.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step("[Verify] test_00013 completion"):
        assert True
