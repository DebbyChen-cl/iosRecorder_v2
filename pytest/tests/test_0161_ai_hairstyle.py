import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_hairstyle")
def test_test_ai_hairstyle(actions: DriverActions):
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap AI Hairstyle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle')
    with step("[Verify] lblDesc is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblDesc'), 'element lblDesc should be visible'
    with step("[Action] Tap notShowAgainCheckBox"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap Male"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Male')
    with step("[Verify] Classic Side is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Classic Side'), 'element Classic Side should be visible'
    with step("[Action] Tap importButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step("[Verify] descriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'), 'element descriptionLabel should be visible'
    with step("[Action] Tap PhotoPickerRecommendDialog-notShowAgainCheckBox"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap ic info n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic info n')
    with step("[Verify] descriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'), 'element descriptionLabel should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3')
    with step("[Action] Tap importButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step("[Verify] descriptionLabel is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'), 'element descriptionLabel should not be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Classic Side"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Classic Side')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should not be visible'
    with step("[Action] Tap AIArtworkPackSelectionCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
    with step("[Verify] btnDownload is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnDownload'), 'element btnDownload should be visible'
    with step("[Action] Tap btnEdit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnEdit')
    with step("[Action] Tap ScrollableMenuViewCell-Portrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step("[Action] Tap Hair"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hair')
    with step("[Action] Tap AI Hairstyle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle')
    with step("[Verify] lblDesc is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'lblDesc'), 'element lblDesc should not be visible'
    with step("[Action] Tap importButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Verify] We cannot find any faces. Try choosing another one. Thank you. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'We cannot find any faces. Try choosing another one. Thank you.'), 'element We cannot find any faces. Try choosing another one. Thank you. should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step("[Verify] More than one person detected. Try choosing another one. Thank you. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'More than one person detected. Try choosing another one. Thank you.'), 'element More than one person detected. Try choosing another one. Thank you. should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step("[Verify] contentView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'contentView'), 'element contentView should be visible'
    with step("[Action] Tap Female"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Female')
    with step("[Action] Tap Luxe Waves"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Luxe Waves')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should not be visible'
    with step("[Action] Tap AIArtworkPackSelectionCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
    with step("[Verify] btnDownload is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnDownload'), 'element btnDownload should be visible'
    assert True
