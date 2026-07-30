import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00149_ai_art_custom_02')
def test_00149_ai_art_custom_02(actions: DriverActions):
    """AI art - Custom Mode"""

    custom_style_name = None
    style_prompt_name = None
    with step('Precondition: close popups'):
        with step('[Action] close_xmas'):
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Close', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Close')
                actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Close')
    with step('Tap AI Photos tab'):
        with step('[Action] tap_ai_photos'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step('Scroll to AI Art and tap'):
        with step('[Action] scroll_and_tap_vertical'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step('Optional: Tap Try Now on intro'):
        with step('[Action] tap_try_now'):
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnNext', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Tap Import photo'):
        with step('[Action] tap_import_photo'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step('Optional: Continue recommendation dialog'):
        with step('[Action] tap_continue_button'):
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Continue', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Expand album list and select _AT album'):
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('Select a single person photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('Tap My Style tab'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Style')
    with step('Verify custom styles are listed'):
        if (not actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeCell', timeout=10)):
            assert False, 'No custom style is listed under My Style'
    with step('Tap a custom style'):
        with step('[Action] tap_element'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeCell')
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
    with step('Tap back button'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Long tap on a custom style'):
        with step('[Action] long_press_element'):
            style_cell = actions.get_element(AppiumBy.XPATH, '//XCUIElementTypeCell')
            assert style_cell is not None
            actions.long_press(style_cell, duration=2)
    with step('Verify info page is displayed'):
        if (not actions.is_element_present(AppiumBy.NAME, 'Reuse', timeout=5)):
            assert False, 'Reuse button not shown on custom style info page'
        if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnDelete', timeout=5)):
            assert False, 'Delete button not shown on custom style info page'
    with step('Tap x button'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step('Verify leave info page and return to custom style list'):
        if (not actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeCell', timeout=5)):
            assert False, 'Did not return to custom style list page'
    with step('Long tap on a custom style again'):
        with step('[Action] long_press_element'):
            style_cell = actions.get_element(AppiumBy.XPATH, '//XCUIElementTypeCell')
            assert style_cell is not None
            actions.long_press(style_cell, duration=2)
    with step('Tap Reuse'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Reuse')
    with step('Verify prompt edit dialog pops up'):
        style_name_field = actions.get_element(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField')
        if (not actions.is_element_present(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField', timeout=5)):
            assert False, 'Style name field not shown on prompt edit dialog'
        if (not actions.is_element_present(AppiumBy.NAME, 'Apply', timeout=5)):
            assert False, 'Apply button not shown on prompt edit dialog'
        custom_style_name = style_name_field.get_attribute('value') or style_name_field.get_attribute('label') or style_name_field.text
        if custom_style_name:
            custom_style_name = custom_style_name.strip()
        if custom_style_name:
            style_prompt_name = custom_style_name if custom_style_name.startswith('Style') else f'Style{custom_style_name}'
    with step('Tap Apply'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'submitButton')
    with step('Verify UI returns to style page and custom style is ready'):
        if (not actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeCell', timeout=5)):
            assert False, 'Custom style list is not shown after Apply'
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
    with step('Tap back button again'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Tap My Style tab again'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Style')
    with step('Long tap on a custom style to delete'):
        with step('[Action] long_press_element'):
            style_cell = actions.get_element(AppiumBy.XPATH, '//XCUIElementTypeCell')
            assert style_cell is not None
            actions.long_press(style_cell, duration=2)
    with step('Tap Delete'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step('Verify the custom style is gone'):
        with step('[Action] get_element'):
            assert not actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeCell', timeout=5)
    with step("[Verify] test_00149 completion"):
        assert True
