import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00013_main_04_01_03')
def test_00013_main_04_01_03(actions: DriverActions):
    """camera - preview"""
    uuid = ['14e99c96-cf13-413e-b9a1-72ecd1d79f26', '41554416-1934-4b42-a1a5-e90b97954ee3', 'e989cb3d-a3e2-4e97-9bae-6e736b051626', '1b906b3b-de59-4b4c-bebf-a05e42728d46', '1b222756-d350-4bad-ad01-4c292ce5f142', 'aed91d66-e468-4a32-afc6-1472ded02f47', '98655e6a-23af-4423-b277-3abbfe6b5ff5', '4d847cdd-117e-4301-aaae-661154ef543d', 'c5cd9d9a-861a-4da9-89c3-eb1c7aec3a2b', '9eb349dc-da6c-4687-bec4-3db095904b5c', '0427946d-a9f5-4e4c-97b9-dc4c59706bb9', '491e2e01-adb9-4487-b382-c9fe4d652141', '9f4ea468-829b-4a11-8ee7-28a09e9a7cdb', '849d967b-99b0-46ba-9deb-3f2eaf29fd25']
    with step('[Action] tap_camera'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Camera')
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
            assert actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_camera'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnMore')
    with step('[Action] tap_picker_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
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
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step('[Action] Tap Cancel Button'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step('[Action] tap_edit_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'editButton')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'settingButton')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_edit_home'):
        assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome')])
    with step('[Action] tap_camera'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Camera')
    with step("[Action] Tap btnAlbum at (60.0%, 62.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 60.0, 62.9)
    with step("[Action] Tap btnBack at (62.5%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 62.5, 58.5)
    with step("[Action] Tap btnAlbum at (77.1%, 34.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 77.1, 34.3)
    with step("[Action] Tap All Photos at (62.2%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'All Photos', 62.2, 56.5)
    with step("[Verify] Select Photo is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Select Photo')
    with step("[Action] Tap btnBack at (52.5%, 56.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 52.5, 56.1)
    with step("[Action] Tap btnAlbum at (37.1%, 37.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 37.1, 37.1)
    with step("[Action] Tap All Photos at (78.0%, 87.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'All Photos', 78.0, 87.0)
    with step("[Action] Tap btnAlbum at (80.7%, 45.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 80.7, 45.2)
    with step("[Action] Tap Recents at (18.6%, 86.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Recents', 18.6, 86.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (55.4%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 55.4, 70.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] editButton is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'editButton')
    with step("[Action] Tap All Photos at (76.8%, 65.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'All Photos', 76.8, 65.2)
    with step("[Action] Tap btnAlbum at (77.7%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 77.7, 42.9)
    with step("[Action] Tap BG at (45.9%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'BG', 45.9, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap btnAlbum at (82.2%, 23.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 82.2, 23.8)
    with step("[Action] Tap Recents at (28.3%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Recents', 28.3, 52.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap btnBack at (67.5%, 63.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 67.5, 63.4)
    with step("[Action] Tap btnAlbum at (71.4%, 48.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 71.4, 48.6)
    with step("[Action] Tap deleteButton at (35.8%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'deleteButton', 35.8, 50.0)
    with step("[Action] Tap Delete at (77.1%, 67.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Delete', 77.1, 67.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Allow “PhotoDirector” to delete this photo?"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=81)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    with step("[Verify] test_00013 completion"):
        assert True
