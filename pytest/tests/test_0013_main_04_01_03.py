import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_04_01_03")
def test_test_main_04_01_03(actions: DriverActions):
    with step("[Verify] Would you like to continue editing? is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Would you like to continue editing?'), 'element Would you like to continue editing? should not be visible'
    with step("[Verify] closeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'closeButton'), 'element closeButton should not be visible'
    with step("[Verify] navCloseButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton'), 'element navCloseButton should not be visible'
    with step("[Action] Tap Camera"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Camera')
    with step("[Verify] btnMore is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnMore'), 'element btnMore should be visible'
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Verify] cameraShareButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton'), 'element cameraShareButton should be visible'
    with step("[Action] Tap cameraShareButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton')
    with step("[Verify] shareCell is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'shareCell'), 'element shareCell should be visible'
    with step("[Action] Tap shareCell"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shareCell')
    with step("[Action] Tap at (48, 89)"):
        actions.tap_by_coordinates(48, 89)
    with step("[Action] Tap cameraShareButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton')
    with step("[Verify] shareCell is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'shareCell'), 'element shareCell should be visible'
    with step("[Action] Tap shareCell"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shareCell')
    with step("[Verify] ConversationTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ConversationTitle'), 'element ConversationTitle should be visible'
    with step("[Action] Tap shareCell"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shareCell')
    with step("[Verify] ConversationTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ConversationTitle'), 'element ConversationTitle should be visible'
    with step("[Action] Tap at (406, 105)"):
        actions.tap_by_coordinates(406, 105)
    with step("[Action] Tap at (110, 115)"):
        actions.tap_by_coordinates(110, 115)
    with step("[Action] Tap editButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'editButton')
    with step("[Verify] settingButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'settingButton'), 'element settingButton should be visible'
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap Camera"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Camera')
    with step("[Verify] btnMore is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnMore'), 'element btnMore should be visible'
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Verify] cameraShareButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton'), 'element cameraShareButton should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] btnTakePhoto is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto'), 'element btnTakePhoto should be visible'
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Verify] cameraShareButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton'), 'element cameraShareButton should be visible'
    with step("[Action] Tap cameraAllPhotoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cameraAllPhotoButton')
    with step("[Verify] Select Photo is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Select Photo'), 'element Select Photo should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] btnTakePhoto is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto'), 'element btnTakePhoto should be visible'
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Verify] cameraShareButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton'), 'element cameraShareButton should be visible'
    with step("[Action] Tap cameraAllPhotoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cameraAllPhotoButton')
    with step("[Verify] Select Photo is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Select Photo'), 'element Select Photo should be visible'
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap Recents"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Recents')
    with step("[Action] Tap photoCell-14"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-14')
    with step("[Verify] editButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'editButton'), 'element editButton should be visible'
    with step("[Action] Tap cameraAllPhotoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cameraAllPhotoButton')
    with step("[Verify] Select Photo is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Select Photo'), 'element Select Photo should be visible'
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap BG"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'BG')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap Recents"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Recents')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] btnTakePhoto is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto'), 'element btnTakePhoto should be visible'
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Verify] cameraShareButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'cameraShareButton'), 'element cameraShareButton should be visible'
    with step("[Action] Tap deleteButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'deleteButton')
    with step("[Verify] Allow “PhotoDirector” to delete this photo? is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Allow “PhotoDirector” to delete this photo?'), 'element Allow “PhotoDirector” to delete this photo? should be visible'
    with step("[Action] Tap Delete"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Delete')
    assert True
