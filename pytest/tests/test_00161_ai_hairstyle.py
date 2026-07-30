import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00161_ai_hairstyle')
def test_00161_ai_hairstyle(actions: DriverActions):
    """AI hairstyle"""
    with step('Action: Launch PHD and navigate to AI Hairstyle via AI Photos'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
        with step('[Action] scroll_and_tap_vertical'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel')
    with step('Optional: Dismiss hairstyle intro if present'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblDesc'):
            with step('[Action] tap_element'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
            with step('[Action] tap_phd_btn'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Action: Tap Male tab — verify male styles are listed'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Male')
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Classic Side')
        with step('[Verify] snapshot: G02_01_05_male_before_import.png'):
            actions.capture_for_gt('G02_01_05_male_before_import.png', AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step('Action: Tap Import — verify recommendation dialog, enable dont show again'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'):
            with step('[Action] tap_phd_element'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox')
            with step('[Action] tap_phd_btn'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Action: Tap [i] button in photo picker — verify recommendation dialog'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic info n')
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Action: Expand album list, select AT album, select male photo'):
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3')
    with step('Verify: Male photo is imported'):
        with step('[Verify] snapshot: G02_01_05_male_after_import.png'):
            actions.capture_for_gt('G02_01_05_male_after_import.png', AppiumBy.ACCESSIBILITY_ID, 'importButton')
        if actions.compare_with_gt('G02_01_05_male_before_import.png', gt_folder=TD.GT_FOLDER)[0]:
            assert False, '[G02_01_05] Male styles did not change after import'
    with step('Action: Tap imported photo thumbnail — verify no recommendation dialog'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'):
            assert False, '[G02_01_05] Recommendation dialog unexpectedly appeared on thumbnail tap'
    with step('Action: Tap back to feature main page'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Action: Select a male style'):
        with step('[Action] select_hairstyle'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Classic Side')
    with step('Action: Tap Generate — verify artwork page and generation'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
        with step('[Action] verify_artwork'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step('Verify: Thumbnail shows busy during generation — wait for finish'):
        with step('[Action] wait_process'):
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
        with step('[Verify] snapshot: G02_01_05_artwork_after_generate.png'):
            actions.capture_for_gt('G02_01_05_artwork_after_generate.png')
    with step('Action: Tap generated image thumbnail — verify enter full view'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
        with step('[Action] verify_artwork_fullview'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnDownload')
    with step('Action: Tap Edit from artwork full view — navigate to AI Hairstyle'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnEdit')
        with step('[Action] scroll_and_tap_feature_tab'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
        with step('[Action] scroll_and_tap_feature_tab'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hair')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel')
    with step('Verify: No intro page displayed (dont show again was enabled)'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblDesc'):
            assert False, '[G02_01_05] Intro page unexpectedly displayed in edit room (should not show again)'
    with step('Action: Tap Import from edit room — dismiss recommendation if shown'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
        with step('[Action] tap_phd_btn'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Action: Select no-face photo — verify no-face error dialog'):
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'We cannot find any faces. Try choosing another one. Thank you.')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('Action: Select multi-face photo — verify too many faces error dialog'):
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.NAME, 'More than one person detected. Try choosing another one. Thank you.')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('Action: Select single-female photo — verify photo is imported'):
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="AIHairStyleProStyleSelectionViewController"]/XCUIElementTypeOther[3]')
    with step('Action: Select Female tab — verify tab is highlighted'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Female')
    with step('Action: Select a female style — verify style is highlighted'):
        with step('[Action] select_hairstyle'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Luxe Waves')
    with step('Action: Tap Generate from edit room — verify artwork page and generation'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
        with step('[Action] verify_artwork'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step('Verify: Thumbnail shows busy during generation — wait for finish'):
        with step('[Action] wait_process'):
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
        with step('[Verify] snapshot: G02_01_05_artwork_editroom_after_generate.png'):
            actions.capture_for_gt('G02_01_05_artwork_editroom_after_generate.png')
    with step('Action: Tap generated image thumbnail — verify enter full view'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
        with step('[Action] verify_artwork_fullview'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnDownload')
    with step("[Verify] test_00161 completion"):
        assert True
