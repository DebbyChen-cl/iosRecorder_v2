import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00148_ai_art_custom_01')
def test_00148_ai_art_custom_01(actions: DriverActions):
    """AI art - Custom Mode"""

    first_style_name = 'custom001'
    second_style_name = 'custom002'
    first_prompt = "Initial D's style"
    second_prompt = "American comic's style"
    with step('Tap AI Photos tab'):
        with step('[Action] tap_ai_photos'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step('Tap AI Art entry'):
        with step('[Action] scroll_and_tap_vertical'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step('Check if intro page displays'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'):
            with step('[Action] tap_element'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Tap Import source photo'):
        with step('[Action] tap_import_photo'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
        with step('[Action] tap_continue_button'):
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Continue', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Expand album list and select _AT album'):
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('Select single person photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('Tap Custom style and enter edit dialog'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Style')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Start')
    with step('Tap style name area and input style name'):
        with step('[Action] tap_aiart_custom_Style_field'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="ArtisticAvatarStyleSelectionViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]')
        with step('[Action] input_style_name'):
            assert actions.type_text_by_locator(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField', 'custom001')
    with step('Tap prompt area and input prompt'):
        with step('[Action] tap_aiart_custom_prompt'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeTextView')
        with step('[Action] input_style_prompt2'):
            assert actions.type_text_by_locator(AppiumBy.XPATH, '//XCUIElementTypeTextView', 'temporary prompt')
    with step('Verify prompt is displayed'):
        prompt_field = actions.get_element(AppiumBy.XPATH, '//XCUIElementTypeTextView')
        if (not actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeTextView', timeout=5)):
            assert False, 'Prompt field is not displayed after input'
        prompt_value = prompt_field.get_attribute('value') or prompt_field.get_attribute('label') or prompt_field.text or ''
        if 'temporary prompt' not in prompt_value:
            assert False, 'Prompt is not displayed after input'
    with step('Tap x button of prompt area'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="clearButton"])[2]')
    with step('Verify prompt is cleared and default description displays'):
        if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel', timeout=5)):
            assert False, 'Prompt is not cleared to default description'
    with step('Input prompt again and apply'):
        with step('[Action] input_style_prompt2'):
            assert actions.type_text_by_locator(AppiumBy.XPATH, '//XCUIElementTypeTextView', "Initial D's style")
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'submitButton')
    with step('Tap Generate'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify go to result page'):
        with step('[Action] verify_artwork_processing'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'In progress')
    with step('Wait for process finish'):
        with step('[Action] wait_for_image_generated'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'In progress', timeout=90)
    with step('Verify image is generated'):
        with step('[Action] verify_artistic_avatar_result'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_element'):
        actions.tap_by_locator(AppiumBy.NAME, 'Ok')
    with step('Tap back button'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Tap Custom style again and enter edit dialog'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'buildIn_custom_female')
    with step('Verify previous prompt exists'):
        prompt_field = actions.get_element(AppiumBy.XPATH, '//XCUIElementTypeTextView[@value="Initial D\'s style"]')
        if (not actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeTextView[@value="Initial D\'s style"]', timeout=5)):
            assert False, 'Prompt field is not displayed when reopening Custom style'
        prompt_value = prompt_field.get_attribute('value') or prompt_field.get_attribute('label') or prompt_field.text or ''
        if first_prompt not in prompt_value:
            assert False, 'Previous prompt is not preserved in Custom style dialog'
    with step('Tap style name area and edit style name'):
        with step('[Action] tap_aihairstyle_custom_Style_field'):
            assert actions.tap_by_locator(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField')
        with step('[Action] input_style_name'):
            assert actions.type_text_by_locator(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField', 'custom002')
    with step('Tap prompt area, clear prompt, and input new prompt'):
        with step('[Action] tap_aiart_custom_prompt'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeTextView')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="clearButton"])[2]')
        with step('[Action] input_style_prompt2'):
            assert actions.type_text_by_locator(AppiumBy.XPATH, '//XCUIElementTypeTextView', "American comic's style")
    with step('Tap Apply'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'submitButton')
    with step('Tap Generate again'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify go to result page again'):
        with step('[Action] verify_artwork_processing'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'In progress')
    with step('Wait for process finish again'):
        with step('[Action] wait_for_image_generated'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'In progress', timeout=90)
    with step('Verify image is generated again'):
        with step('[Action] verify_artistic_avatar_result'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] test_00148 completion"):
        assert True
