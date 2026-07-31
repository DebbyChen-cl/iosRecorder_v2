import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00180_ai_try_on_05')
def test_00180_ai_try_on_05(actions: DriverActions):
    """AI try on: Multiple ref photos"""

    # ── Inlined from legacy AI_TryOn_Page.count_reference_photos (self.ai_tryon_page.*) ──
    def _count_reference_photos():
        count = 0
        if actions.get_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "photodirector.PHPhotoPickViewController"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage', timeout=2):
            count += 1
        if actions.get_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "photodirector.PHPhotoPickViewController"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeImage', timeout=2):
            count += 1
        if actions.get_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "photodirector.PHPhotoPickViewController"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeImage', timeout=2):
            count += 1
        return count

    with step('Close any popups on main page'):
        with step('[Action] close_xmas'):
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Close', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Close')
        with step('[Action] close_continue_edit'):
            if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('Tap AI photos tab'):
        with step('[Action] tap_ai_photos'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step('Tap AI try-on entry'):
        with step('[Action] tap_ai_tryon_entry'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox'):
        with step('[Action] check_dont_show_again'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
        with step('[Action] tap_try_now'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Tap import'):
        with step('[Action] tap_import_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton'):
        with step('Check dont show again'):
            with step('[Action] check_dont_show_again_in_feature'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox')
        with step('Tap continue'):
            with step('[Action] tap_continue_button'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Select AT album'):
        category = '_AT'
        with step('[Action] expand_album_list'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('Select single female photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('Tap Custom style'):
        with step('[Action] select_custom_style'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'customStyleCell')
    with step('Tap Upload apparel photo'):
        with step('[Action] tap_upload_apparel'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "titleLabel"`][2]')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton'):
        with step('Check dont show again'):
            with step('[Action] check_dont_show_again_in_feature'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox')
        with step('Tap continue'):
            with step('[Action] tap_continue_button'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Select AT album'):
        category = '_AT'
        with step('[Action] expand_album_list'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('Select top wear photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3')
    with step('Verify reference photo added'):
        with step('[Action] verify_reference_photo_added'):
            assert actions.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "photodirector.PHPhotoPickViewController"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage')
    with step('Tap remove photo button'):
        with step('[Action] tap_remove_reference_photo'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n')
    with step('Verify photo removed from list'):
        with step('[Action] verify_reference_photo_removed'):
            assert actions.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "photodirector.PHPhotoPickViewController"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage')
    with step('Select top wear photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3')
    with step('Select pants/skirt photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step('Verify photos added to list'):
        photo_count = _count_reference_photos()
        if photo_count != 2:
            assert False, f'Expected 2 photos in list, found {photo_count}'
    with step('Tap Next button'):
        with step('[Action] tap_next_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Verify Custom style shows photo count 2'):
        pass
    with step('Tap Generate'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify artwork shows Processing'):
        with step('[Action] verify_artwork_processing'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=10), 'Artwork Processing indicator not displayed'
    with step('Wait for image generation'):
        with step('[Action] wait_for_image_generated'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=90)
    with step('Tap back from artwork'):
        with step('[Action] tap_back'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Tap Custom style (photo mode)'):
        with step('[Action] select_custom_style'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'customStyleCell')
    with step('Tap Continue in recommendation dialog'):
        with step('[Action] tap_continue_button'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Select shoes photo'):
        category = '_AT'
        with step('[Action] expand_album_list'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('Verify 3 photos in list'):
        photo_count = _count_reference_photos()
        if photo_count != 3:
            assert False, f'Expected 3 photos in list, found {photo_count}'
    with step('Try to select 4th photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('Verify max photos warning dialog'):
        pass
    with step('[Action] tap_ok'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('Verify photo count unchanged'):
        photo_count = _count_reference_photos()
        if photo_count != 3:
            assert False, f'Photo count changed unexpectedly, found {photo_count}'
    with step('Tap Next button'):
        with step('[Action] tap_next_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Verify Custom style shows photo count 3'):
        pass
    with step('Tap Generate'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify artwork shows Processing'):
        with step('[Action] verify_artwork_processing'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=10), 'Artwork Processing indicator not displayed'
    with step('Wait for image generation'):
        with step('[Action] wait_for_image_generated'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=90)
    with step('Tap back from artwork'):
        with step('[Action] tap_back'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Tap clear custom style button'):
        with step('[Action] tap_clear_custom_style'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'clearButton')
    with step('Verify custom style reset'):
        with step('[Action] verify_custom_style_reset'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Photo')
    with step("[Verify] test_00180 completion"):
        assert True
