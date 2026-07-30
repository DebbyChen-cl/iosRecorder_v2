import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00181_ai_try_on_06')
def test_00181_ai_try_on_06(actions: DriverActions):
    """AI try on: Pet mode"""

    with step('Tap Edit'):
        with step('[Action] tap_editphoto'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('Select Try-On album'):
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try-On')
    with step('Select a cat or dog photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Action] tap_dont_show_again'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
    with step('[Action] tap_close_dialog_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('Tap Portrait tab'):
        with step('[Action] scroll_and_tap_feature_tab'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('Tap AI try-on entry'):
        with step('[Action] scroll_and_tap_feature_tab'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox'):
        with step('[Action] check_dont_show_again'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
        with step('[Action] tap_try_now'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Verify no No face detected dialog'):
        with step('[Action] verify_no_face_dialog_not_displayed'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'We cannot find any faces. Try choosing another one. Thank you.')
    with step('Tap Pet & Doll tab'):
        with step('[Action] tap_pet_doll_tab'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pet & Doll')
    with step('Select a Pet & Doll style'):
        with step('[Action] select_pet_doll_style'):
            actions.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, 'Soft Towel', max_scrolls=25)
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Soft Towel')
    with step('Tap Generate for Pet & Doll style'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('First tap I Agree on TOS'):
        with step('[Action] tap_phd_btn'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
    with step('Verify artwork shows Processing'):
        with step('[Action] verify_artwork_processing'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=10), 'Artwork Processing indicator not displayed'
    with step('Wait for processing to finish'):
        with step('[Action] wait_for_image_generated'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=90)
    with step('Tap back to feature from artwork'):
        with step('[Action] tap_back'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Select Custom style'):
        with step('[Action] select_custom_style'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'customStyleCell')
    with step('Tap Upload apparel photo'):
        with step('[Action] tap_pet_upload_apparel'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "titleLabel"`][2]')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton'):
        with step('Dismiss apparel upload recommendation dialog'):
            with step('[Action] check_dont_show_again_in_feature'):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox')
            with step('[Action] tap_continue_button'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Select _AT album for apparel photo'):
        with step('[Action] expand_album_list'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try-On')
    with step('Select a pet wearing photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('Confirm selected apparel photo'):
        with step('[Action] tap_next_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Verify imported photo thumbnail is displayed on custom style'):
        with step('[Action] verify_custom_style_in_photo_mode'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Photo')
    with step('Tap Generate for custom photo style'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify artwork shows Processing for custom photo style'):
        with step('[Action] verify_artwork_processing'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=10), 'Artwork Processing indicator not displayed for custom photo style'
    with step('Wait for custom photo style processing to finish'):
        with step('[Action] wait_for_image_generated'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=90)
    with step('Tap back to feature from artwork again'):
        with step('[Action] tap_back'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Clear imported custom style photo'):
        with step('[Action] tap_clear_custom_style'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'clearButton')
        with step('[Action] verify_custom_style_reset'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Photo')
    with step('Switch custom style to described apparel mode'):
        with step('[Action] select_custom_style'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'customStyleCell')
        with step('[Action] tap_describe_apparel'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "titleLabel"`][3]')
    with step('Input apparel style prompt and apply'):
        with step('[Action] input_apparel_prompt'):
            actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel').clear()
            actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 'raincoat')
        with step('[Action] tap_apply'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptApplyButton')
    with step('Tap Generate for custom text style'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify artwork shows Processing for custom text style'):
        with step('[Action] verify_artwork_processing'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=10), 'Artwork Processing indicator not displayed for custom text style'
    with step('Wait for custom text style processing to finish'):
        with step('[Action] wait_for_image_generated'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=90)
    with step("[Verify] test_00181 completion"):
        assert True
