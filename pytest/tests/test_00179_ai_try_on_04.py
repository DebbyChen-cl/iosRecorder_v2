import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00179_ai_try_on_04')
def test_00179_ai_try_on_04(actions: DriverActions):
    """AI try on: Error handling"""
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
    with step('[Action] tap_import_button'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    category = '_AT'
    with step('[Action] expand_album_list'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Action] verify_no_face_dialog'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'We cannot find any faces. Try choosing another one. Thank you.')
    with step('[Action] tap_ok'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('[Action] verify_multi_face_dialog'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'More than one person detected. Try choosing another one. Thank you.')
    with step('[Action] tap_ok'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Verify] test_00179 completion"):
        assert True
