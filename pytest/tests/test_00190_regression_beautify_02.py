import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00190_regression_beautify_02')
def test_00190_regression_beautify_02(actions: DriverActions):
    """regression - beautify - face smoother"""
    with step('Close any popups on main page'):
        with step('[Action] close_xmas'):
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Close', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Close')
        with step('[Action] close_continue_edit'):
            if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('Tap Edit button'):
        with step('[Action] tap_editphoto'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Edit')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('Expand album list > Select Regression album'):
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Regression')
    with step('Select multi-face photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('Tap Portrait tab'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Portrait')
    with step('Tap Beautify > Auto Retouch'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto Retouch')
    with step('Wait for detection finish'):
        with step('[Action] wait_process'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    with step('No face dialog does not appear'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'We cannot find any faces. Try choosing another one. Thank you.'):
            assert False, 'No face dialog appeared after Auto Retouch detection'
    num = 3
    with step(f'Verify face list appears. Previous build had {num} faces detected, current build should have same or more faces detected'):
        face_list = actions.get_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView')
        face_count = len(face_list.find_elements(AppiumBy.XPATH, './/XCUIElementTypeCell')) if face_list is not None else 0
        if (face_count - 1) < num:
            assert False, 'Face list detected fewer faces than previous build after Auto Retouch detection'
    with step("[Verify] test_00190 completion"):
        assert True
