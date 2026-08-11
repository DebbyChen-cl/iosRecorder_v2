import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00010_main_05_01_06_2')
def test_00010_main_05_01_06_2(actions: DriverActions):
    """1. Tap Edit Photo button"""
    with step('Tap Edit Photo button'):
        with step('[Action] tap_editphoto'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('Select a photo'):
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
        with step('[Verify] snapshot: 05_01_06_2after_select_category.png'):
            actions.capture_for_gt('05_01_06_2after_select_category.png')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
        with step('[Verify] snapshot: 05_01_06_2after_select_photo.png'):
            actions.capture_for_gt('05_01_06_2after_select_photo.png')
    with step('Enter AI Art'):
        with step('[Action] tap_portrait1_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step("[Verify] test_00010 completion"):
        assert True
