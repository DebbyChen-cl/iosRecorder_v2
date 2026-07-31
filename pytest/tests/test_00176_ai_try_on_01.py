import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00176_ai_try_on_01')
def test_00176_ai_try_on_01(actions: DriverActions):
    """AI try on"""
    with step('Close any popups on main page'):
        with step('[Action] close_xmas'):
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Close', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Close')
        with step('[Action] close_continue_edit'):
            if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('Tap Edit'):
        with step('[Action] tap_editphoto'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Edit')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('Select _AT album'):
        category = '_AT'
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('Select single female photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('[Action] tap_dont_show_again'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
    with step('[Action] tap_close_dialog_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('Tap Portrait tab'):
        with step('[Action] tap_portrait1_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('Tap AI try-on entry'):
        with step('[Action] tap_ai_tryon_entry'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On')
    with step('Verify intro page'):
        if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')):
            pass
        else:
            with step('Check dont show again'):
                with step('[Action] check_dont_show_again'):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
            with step('Tap Try now'):
                with step('[Action] tap_try_now'):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Verify photo loaded as source'):
        with step('[Verify] snapshot: ai_tryon_source_loaded.png'):
            actions.capture_for_gt('ai_tryon_source_loaded.png')
        if actions.compare_with_gt('ai_tryon_source_loaded.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Verify photo loaded as source: Source photo verification failed - screenshot does not match ground truth'
    with step('Select premium style'):
        with step('[Action] select_female_premium_style'):
            actions.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, 'Beige', max_scrolls=25)
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beige')
    with step('Tap Generate'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('First tap I Agree on TOS'):
        with step('[Action] tap_phd_btn'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
    with step('Tap Back button'):
        with step('[Action] tap_back'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Select free style'):
        with step('[Action] select_female_free_style'):
            actions.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, 'Ruby Muse', max_scrolls=25)
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ruby Muse')
    with step('Tap Generate'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify artwork thumbnail shows Processing'):
        with step('[Action] verify_artwork_processing'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=10), 'Artwork Processing indicator not displayed'
    with step('Wait for image generatiosn'):
        with step('[Action] wait_for_image_generated'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=90)
    with step('Tap Back button'):
        with step('[Action] tap_back'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Verify back to AI try-on main feature page'):
        with step('[Action] verify_back_to_main_feature'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel')
    with step('Tap Male tab'):
        with step('[Action] tap_male_tab'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Male')
    with step('Tap source photo preview'):
        with step('[Action] tap_source_preview'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step('Verify recommendation dialog'):
        if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')):
            assert False, 'Recommendation dialog not displayed'
        else:
            with step('Check dont show again'):
                with step('[Action] check_dont_show_again_in_feature'):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox')
            with step('Tap continue'):
                with step('[Action] tap_continue_button'):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Tap info button'):
        with step('[Action] tap_info_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic info n')
    with step('Verify recommendation dialog again'):
        with step('[Action] verify_recommendation_dialog'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Tap continue'):
        with step('[Action] tap_continue_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Select single male photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3')
    with step('Select premium style for male'):
        with step('[Action] select_male_premium_style'):
            actions.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, 'Taupe', max_scrolls=25)
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Taupe')
    with step('Tap Generate'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Tap Back button'):
        with step('[Action] tap_back'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Select free style for male'):
        with step('[Action] select_male_free_style'):
            actions.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, 'Green Ease', max_scrolls=25)
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Green Ease')
    with step('Tap Generate'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify artwork thumbnail shows Processing'):
        with step('[Action] verify_artwork_processing'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=10), 'Artwork Processing indicator not displayed'
    with step('Wait for image generation'):
        with step('[Action] wait_for_image_generated'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=90)
    with step("[Verify] test_00176 completion"):
        assert True
