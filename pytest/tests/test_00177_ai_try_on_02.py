import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00177_ai_try_on_02')
def test_00177_ai_try_on_02(actions: DriverActions):
    """AI try on: Custom - photo"""
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
    with step('Step 4: Tap import'):
        with step('[Action] tap_import_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton'):
        with step('Check dont show again'):
            with step('[Action] check_dont_show_again_in_feature'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox')
        with step('Tap continue'):
            with step('[Action] tap_continue_button'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Select _AT album'):
        category = '_AT'
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('Select single female photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('Tap Custom style'):
        with step('[Action] select_custom_style'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'customStyleCell')
    with step('Tap Upload apparel photo'):
        with step('[Action] tap_upload_apparel'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "titleLabel"`][2]')
    with step('Tap Next button'):
        with step('[Action] tap_next_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Verify recommendation dialog'):
        with step('[Action] verify_recommendation_dialog'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Tap Continue'):
        with step('[Action] tap_continue_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Tap info button'):
        with step('[Action] tap_info_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic info n')
    with step('Verify recommendation dialog again'):
        with step('[Action] verify_recommendation_dialog'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Tap Continue'):
        with step('[Action] tap_continue_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Select _AT album'):
        category = '_AT'
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('Select single male photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3')
    with step('Tap Next button'):
        with step('[Action] tap_next_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Tap Generate'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify artwork thumbnail shows Processing'):
        with step('[Action] verify_artwork_processing'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=10), 'Artwork Processing indicator not displayed'
    with step('Wait for image generation'):
        with step('[Action] wait_for_image_generated'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=90)
    with step("[Verify] test_00177 completion"):
        assert True
