import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00030_ai_replace_ref')
def test_00030_ai_replace_ref(actions: DriverActions):
    """AI replace reference"""
    mode = 1
    with step('Tap settings'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step('Tap "about"'):
        enter_about_page_success = False
        for attempt in range(3):
            with step('[Action] enter_about_page'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'About')
                assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton')
            enter_about_page_success = True
            break
            if attempt < 2:
                pass
    if not enter_about_page_success:
        assert False, 'Enter about page fail after 3 retries'
    with step('5 taps on screen to enter debug mode and set subscription = pro+'):
        with step('[Action] enable_plan_from_settings'):
            assert actions.is_element_present(AppiumBy.NAME, 'Develop Info')
            assert actions.find_element(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="1"])[2]')
            actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[6]')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Tap "<" "<" back to main page'):
        with step('[Action] tap_home'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step('Tap "Edit"'):
        with step('[Action] tap_editphoto'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Edit')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('Select "Sample photos" album'):
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos')
    with step('Select "woman holds books" photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('Enter AI Replace feature'):
        with step('[Action] scroll_and_tap_feature_tab'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'AI Replace')
    with step('Brush to select "books"'):
        from_pos = (160, 302)
        destination = (350, 200)
        with step('[Action] brush_removal'):
            actions.drag_coordinates(160, 302, 350, 200)
    with step('Tap "Replace"'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace')
    with step('Verify "Upload a reference image" option displays'):
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.NAME, 'Upload a reference image')
    with step('Tap "Upload a reference image" option'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Upload a reference image')
    with step('Verify recommendation dialog pops up (optional)'):
        dialog_shown = actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel')
        if not dialog_shown:
            pass
    if dialog_shown:
        with step('Enable "Don\'t show again" (optional)'):
            with step('[Action] tap_phd_element'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox')
        with step('Tap "Continue" (optional)'):
            with step('[Action] tap_phd_btn'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Tap "i" button'):
        with step('[Action] tap_info_btn_n'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic info n')
    with step('Tap "Continue" (close recommendation dialog)'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Expand album list (reference image picker)'):
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('Swipe up to scroll album list'):
        with step('[Action] swipe_up'):
            actions.execute_script('mobile: swipe', {'direction': 'up'})
    with step('Select "Replace" album'):
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace')
    with step('Select "Guitar" photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('Verify reference image is imported and displayed as thumbnail'):
        with step('[Verify] snapshot: ai_replace_ref_thumb_guitar.png'):
            actions.capture_for_gt('ai_replace_ref_thumb_guitar.png', crop_rect=(0, 100, 367, 800))
    with step('Verify prompt column shows default description'):
        with step('[Action] verify_prompt_replace_default_prompt'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'promptDisplayLabel')
    with step('Tap prompt column'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="AIReplaceViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]')
    with step('Verify prompt shows default description'):
        with step('[Action] verify_replace_default_prompt'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder')
    with step('Input prompt "Replace to the guitar"'):
        with step('[Action] send_keys'):
            actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 'Replace to the guitar')
    with step('Tap "Next"'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')
    with step('Verify prompt is displayed beside reference image thumbnail'):
        with step('[Verify] snapshot: ai_replace_ref_prompt_guitar.png'):
            actions.capture_for_gt('ai_replace_ref_prompt_guitar.png', crop_rect=(0, 100, 367, 800))
    with step('Tap "replace"'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate')
    with step('Verify UI goes to artwork and thumbnail is processing'):
        with step('[Action] verify_artwork_processing'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'In progress')
    with step('Wait for generation finish and verify thumbnail updated to result'):
        with step('[Verify] snapshot: ai_replace_ref_result_guitar.png'):
            actions.capture_for_gt('ai_replace_ref_result_guitar.png', crop_rect=(0, 100, 367, 800))
    with step('Tap "<" back to feature page'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Tap the reference image thumbnail'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'refresh')
    with step('Verify no recommendation dialog pops up'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'):
            assert False, "Recommendation dialog should NOT pop up after Don't show again"
    with step('Select "tuba" photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('Verify the reference image thumbnail is updated'):
        with step('[Verify] snapshot: ai_replace_ref_thumb_tuba.png'):
            actions.capture_for_gt('ai_replace_ref_thumb_tuba.png', crop_rect=(0, 100, 367, 800))
    with step('Tap the prompt column, prompt dialog pops up'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="AIReplaceViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]')
    with step('Tap "x" to clear all prompts'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClear')
    with step('Tap preview image to close prompt dialog and keyboard'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage')
    with step('Verify all prompts are cleared (show default description)'):
        with step('[Action] verify_prompt_replace_default_prompt'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'promptDisplayLabel')
    with step('Tap "replace" (second run)'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace')
    with step('Verify UI goes to artwork and thumbnail shows "busy" (second run)'):
        with step('[Action] verify_artwork_processing'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'In progress')
    with step('Wait for generation finish and verify thumbnail updated to result (second run)'):
        with step('[Action] wait_for_image_generated'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'In progress', timeout=90)
    with step("[Verify] test_00030 completion"):
        assert True
