import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00163_ai_hairstyle_mystyle')
def test_00163_ai_hairstyle_mystyle(actions: DriverActions):
    """AI hairstyle - mystyle"""
    with step('Action: Launch PHD, tap AI Photos, and tap AI Hairstyle'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
        with step('[Action] scroll_and_tap_vertical'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel')
    with step('Optional: Tap continue on intro page'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblDesc'):
            with step('[Action] tap_phd_btn'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Action: Tap import and continue recommendation dialog if shown'):
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
    with step('Action: Tap My Style tab and verify custom style is listed'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Style')
        if (not actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeCell', timeout=10)):
            assert False, '[G02_01_05_3] No custom style is listed under My Style'
    with step('Action: Long press custom style and tap eye icon'):
        with step('[Action] long_press_element'):
            style_cell = actions.get_element(AppiumBy.XPATH, '//XCUIElementTypeCell')
            assert style_cell is not None
            actions.long_press(style_cell, duration=2)
        if (not actions.is_element_present(AppiumBy.NAME, 'Reuse', timeout=3)):
            with step('[Action] tap_phd_btn'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic view')
    with step('Verify: Style info page is displayed'):
        if (not actions.is_element_present(AppiumBy.NAME, 'Reuse', timeout=5)):
            assert False, '[G02_01_05_3] Style info page is not displayed'
    with step('Action: Tap reuse and verify prompt edit dialog is displayed'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Reuse')
        if (not actions.is_element_present(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField', timeout=5)):
            assert False, '[G02_01_05_3] Prompt edit dialog is not displayed'
    with step('Action: Tap Apply and tap Generate'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptApplyButton')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify: Go to artwork and thumbnail shows busy during generation'):
        with step('[Action] verify_artwork'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
        if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=10)):
            assert False, '[G02_01_05_3] Busy thumbnail is not shown during generation'
    with step('Action: Wait for generation finish'):
        with step('[Action] wait_process'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
    with step('Action: Tap back to feature page'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Action: Tap My Style tab, long press custom style, and tap delete icon'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Style')
        delete_style_label = actions.get_element(AppiumBy.ACCESSIBILITY_ID, 'Style 3')
        if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Style 3', timeout=5)):
            assert False, '[G02_01_05_3] Failed to get custom style label before deletion'
        delete_style_name = delete_style_label.get_attribute('name') or delete_style_label.get_attribute('label') or delete_style_label.text or ''
        if not delete_style_name:
            assert False, '[G02_01_05_3] Custom style label is empty before deletion'
        with step('[Action] long_press_element'):
            style_cell = actions.get_element(AppiumBy.XPATH, '//XCUIElementTypeCell')
            assert style_cell is not None
            actions.long_press(style_cell, duration=2)
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic delete')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Delete')
    with step('Verify: Custom style is deleted'):
        with step('[Verify] get_element'):
            assert not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, delete_style_name, timeout=5)
    with step("[Verify] test_00163 completion"):
        assert True
