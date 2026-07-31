import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00162_ai_hairstyle_custom')
def test_00162_ai_hairstyle_custom(actions: DriverActions):
    """AI hairstyle - custom"""
    first_prompt = 'Reinbow afro'
    second_prompt = 'Gold wave'
    with step('Action: Launch PHD, tap AI Photos, and tap AI Hairstyle'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
        with step('[Action] scroll_and_tap_vertical'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel')
    with step('Optional: Tap continue on intro page'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblDesc'):
            with step('[Action] tap_phd_btn'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Action: Tap Import and continue recommendation dialog if shown'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'):
            with step('[Action] tap_phd_btn'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Action: Expand album list, select AT album, and select single female photo'):
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('Action: Select custom style and edit style name'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Custom')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'describeClothingStyleButton')
        with step('[Action] tap_aihairstyle_custom_Style_field'):
            assert actions.tap_by_locator(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField')
        if actions.is_element_present(AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="clearButton"])[1]', timeout=3):
            with step('[Action] tap_phd_btn'):
                assert actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="clearButton"])[1]')
        with step('[Action] input_style_name'):
            assert actions.type_text_by_locator(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField', 'Custom style')
    with step('Verify: The style name can be modified'):
        style_name_field = actions.get_element(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField')
        if (not actions.is_element_present(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField', timeout=5)):
            assert False, '[G02_01_05_2] Style name field not found'
        style_name_value = style_name_field.get_attribute('value') or style_name_field.get_attribute('label') or style_name_field.text or ''
        if 'Custom style' not in style_name_value:
            assert False, '[G02_01_05_2] Style name was not modified'
    with step('Action: Tap prompt column and input prompt "aaaaaa"'):
        with step('[Action] tap_aiart_custom_prompt'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeTextView')
        with step('[Action] input_style_prompt2'):
            assert actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 'aaaaaa')
    with step('Verify: Prompt is modified'):
        prompt_field = actions.get_element(AppiumBy.XPATH, '//XCUIElementTypeTextView')
        if (not actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeTextView', timeout=5)):
            assert False, '[G02_01_05_2] Prompt field not found after input'
        prompt_value = prompt_field.get_attribute('value') or prompt_field.get_attribute('label') or prompt_field.text or ''
        if 'aaaaaa' not in prompt_value:
            assert False, '[G02_01_05_2] Prompt is not modified'
    with step('Action: Tap x button of prompt column'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'clearButton')
    with step('Verify: Prompt resets to default description'):
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel')
    with step('Action: Input prompt "Reinbow afro", tap Apply, then tap Generate'):
        with step('[Action] input_style_prompt2'):
            assert actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', 'Reinbow afro')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptApplyButton')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify: Go to artwork and thumbnail shows busy during generation'):
        with step('[Action] verify_artwork'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
        if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=10)):
            assert False, '[G02_01_05_2] Busy thumbnail is not shown during generation (first run)'
    with step('Action: Wait for generation finish and verify thumbnail updates to result'):
        with step('[Action] wait_process'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
        if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0', timeout=10)):
            assert False, '[G02_01_05_2] Result thumbnail is not updated (first run)'
    with step('Action: Tap back to feature page'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Action: Tap custom style displayed as prompt and verify previous prompt appears'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Prompt')
        if (not actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeTextView[@value="Reinbow afro"]', timeout=5)):
            assert False, '[G02_01_05_2] Previous prompt is not displayed in custom style'
    with step('Action: Edit prompt to "Gold wave", tap Apply, then tap Generate'):
        with step('[Action] tap_aiart_custom_prompt'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeTextView')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="clearButton"])[2]')
        with step('[Action] input_style_prompt2'):
            assert actions.type_text_by_locator(AppiumBy.XPATH, '//XCUIElementTypeTextView', 'Gold wave')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptApplyButton')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify: Go to artwork and thumbnail shows busy during generation again'):
        with step('[Action] verify_artwork'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
        if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=10)):
            assert False, '[G02_01_05_2] Busy thumbnail is not shown during generation (second run)'
    with step('Action: Wait for generation finish and verify thumbnail updates to result again'):
        with step('[Action] wait_process'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
        if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0', timeout=10)):
            assert False, '[G02_01_05_2] Result thumbnail is not updated (second run)'
    with step('Action: Tap back to feature page and tap x of custom style'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'clearButton')
    with step('Verify: Custom style thumbnail displays "Custom"'):
        if ((not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Custom', timeout=5)) and (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Custom', timeout=5))):
            assert False, '[G02_01_05_2] Custom style thumbnail does not display "Custom"'
    with step("[Verify] test_00162 completion"):
        assert True
