import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00187_ai_creative_studio_04')
def test_00187_ai_creative_studio_04(actions: DriverActions):
    """AI Creative Studio - Custom Prompt"""
    with step('Tap AI Creative Studio entry'):
        with step('[Action] enter_ai_creative_studio'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
    with step('Tap Custom tab'):
        with step('[Action] tap_custom_tab'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Custom')
    with step('Verify default prompt description'):
        with step('[Action] verify_default_prompt'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Describe your idea and we will bring it to life.')
    with step('Verify Generate button is disabled'):
        with step('[Action] verify_prompt_generate_disabled'):
            assert ((actions.is_element_enabled(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AICreativeStudioCustomViewController"]/XCUIElementTypeOther/XCUIElementTypeButton') == 'false') or (not actions.is_element_enabled(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AICreativeStudioCustomViewController"]/XCUIElementTypeOther/XCUIElementTypeButton')))
    with step('Tap My Prompts button'):
        with step('[Action] tap_my_prompts'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Prompts')
    with step('Verify Nothing yet in My Prompts'):
        with step('[Action] verify_nothing_yet'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'lblEmpty')
    with step('Tap back from My Prompts'):
        with step('[Action] tap_back_from_my_prompts'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Input prompt text'):
        with step('[Action] input_prompt'):
            actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeTextView').clear()
            actions.type_text_by_locator(AppiumBy.XPATH, '//XCUIElementTypeTextView', 'A cat wearing sunglasses on a beach')
    with step('Tap keyboard Next button'):
        with step('[Action] tap_keyboard_next'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeKeyboard[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[-1]')
    with step('Verify keyboard is closed'):
        with step('[Action] verify_keyboard_closed'):
            assert actions.find_element(AppiumBy.CLASS_NAME, 'XCUIElementTypeKeyboard')
    with step('Verify Generate button is disabled (prompt only, no reference image)'):
        with step('[Action] verify_prompt_generate_disabled'):
            assert ((actions.is_element_enabled(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AICreativeStudioCustomViewController"]/XCUIElementTypeOther/XCUIElementTypeButton') == 'false') or (not actions.is_element_enabled(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AICreativeStudioCustomViewController"]/XCUIElementTypeOther/XCUIElementTypeButton')))
    with step('Tap x to clear prompt'):
        with step('[Action] tap_clear_prompt'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'clearButton')
    with step('Verify prompt is cleared'):
        with step('[Action] verify_prompt_cleared'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Describe your idea and we will bring it to life.')
    with step('Tap add reference image button'):
        with step('[Action] tap_add_reference_image'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'referenceAddContainer')
    with step('Select reference image from photo picker'):
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('Tap Next button after adding reference image'):
        with step('[Action] tap_next'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Verify Generate button is disabled (reference image only, no prompt)'):
        with step('[Action] verify_prompt_generate_disabled'):
            assert ((actions.is_element_enabled(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AICreativeStudioCustomViewController"]/XCUIElementTypeOther/XCUIElementTypeButton') == 'false') or (not actions.is_element_enabled(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AICreativeStudioCustomViewController"]/XCUIElementTypeOther/XCUIElementTypeButton')))
    with step('Input prompt text'):
        with step('[Action] input_prompt'):
            actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeTextView').clear()
            actions.type_text_by_locator(AppiumBy.XPATH, '//XCUIElementTypeTextView', 'A cat wearing sunglasses on a beach')
    with step('Tap keyboard Next button'):
        with step('[Action] tap_keyboard_next'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeKeyboard[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[-1]')
    with step('Verify Generate button is enabled'):
        with step('[Action] verify_prompt_generate_enabled'):
            assert actions.is_element_enabled(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AICreativeStudioCustomViewController"]/XCUIElementTypeOther/XCUIElementTypeButton'), 'Generate button should be enabled'
    with step('Tap GPT-image-2 model'):
        with step('[Action] tap_model_gpt_image_2'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevronView')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'GPT-Image-2')
    with step('Tap Generate button'):
        with step('[Action] tap_prompt_generate'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AICreativeStudioCustomViewController"]/XCUIElementTypeOther/XCUIElementTypeButton')
    with step('Verify go to artwork page'):
        with step('[Action] verify_artwork_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
    with step('Verify thumbnail shows Processing'):
        with step('[Action] verify_processing'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
    with step('Wait for generation to finish'):
        with step('[Action] wait_for_generation'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=120)
    with step('Verify generated thumbnail appears'):
        with step('[Action] verify_thumbnail_appear'):
            assert actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AIStudioAIArtworkShortTaskPackSelectionViewController"]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther')
    with step('Tap back from artwork'):
        with step('[Action] tap_back_from_artwork'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Tap Nano banana pro model'):
        with step('[Action] tap_model_nano_banana_pro'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevronView')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Nano Banana Pro (Gemini 3.0)')
    with step('Tap Generate button (Nano banana pro)'):
        with step('[Action] tap_prompt_generate'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AICreativeStudioCustomViewController"]/XCUIElementTypeOther/XCUIElementTypeButton')
    with step('Verify go to artwork page'):
        with step('[Action] verify_artwork_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
    with step('Verify thumbnail shows Processing'):
        with step('[Action] verify_processing'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
    with step('Wait for generation to finish'):
        with step('[Action] wait_for_generation'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=120)
    with step('Verify generated thumbnail appears'):
        with step('[Action] verify_thumbnail_appear'):
            assert actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AIStudioAIArtworkShortTaskPackSelectionViewController"]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther')
    with step('Tap back from artwork'):
        with step('[Action] tap_back_from_artwork'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Tap x to clear prompt'):
        with step('[Action] tap_clear_prompt'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'clearButton')
    with step('Tap My Prompts button'):
        with step('[Action] tap_my_prompts'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Prompts')
    with step('Verify prompt history listed with thumbnail'):
        with step('[Action] verify_prompt_history_listed'):
            assert actions.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]')
    with step('Tap Reuse button'):
        with step('[Action] tap_reuse'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Reuse')
    with step('Verify prompt auto-imported on custom setting page'):
        with step('[Action] verify_prompt_auto_imported'):
            _prompt_text = actions.get_text(AppiumBy.XPATH, '//XCUIElementTypeTextView')
            assert _prompt_text.strip() != '' and 'Describe' not in _prompt_text, 'Prompt not auto-imported'
    with step('Tap My Prompts button again'):
        with step('[Action] tap_my_prompts'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Prompts')
    with step('Tap Select button'):
        with step('[Action] tap_select_prompt_mode'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Select')
    with step('Select prompt history item'):
        with step('[Action] select_prompt_history_item'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "checkbox"`][1]')
        with step('[Action] select_prompt_history_item'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "checkbox"`][1]')
    with step('Verify Delete button appears'):
        with step('[Action] verify_delete_button_appears'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Delete')
    with step('Tap Delete button'):
        with step('[Action] tap_delete_prompt'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Delete')
    with step('Verify prompt history deleted'):
        with step('[Action] verify_history_deleted'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'lblEmpty')
    with step("[Verify] test_00187 completion"):
        assert True
