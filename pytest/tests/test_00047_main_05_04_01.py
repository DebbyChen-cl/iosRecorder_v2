import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00047_main_05_04_01')
def test_00047_main_05_04_01(actions: DriverActions):
    """look / filter"""
    mode = 1
    uuid = ['acc96758-525e-4fa5-8038-10a8ad09ffbb', 'ab1e6160-10af-4fce-9d23-534cad1d3ccf', '7d16a71c-24c9-44d2-995f-e62162afc39e', 'de8beb74-2bb6-4803-95a2-26771444152a', '9d516a63-9272-49de-9d6f-3b10181382e2', 'bebc7fd0-740d-4cbb-941b-6c0cbbf668c6']
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_04_01_no_look.png'):
        actions.capture_for_gt('05_04_01_no_look.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_effect_filter'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Filter')
    with step('[Action] close_filter_intro'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Select a source photo to extract its filter.'):
            actions.tap_by_coordinates(220, 220)
    with step('[Action] tap_filter_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Basic')
    with step('[Action] tap_filter_template'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Vlogger 01')
    with step('[Verify] snapshot: base05_04_01_apply_look.png'):
        actions.capture_for_gt('base05_04_01_apply_look.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_04_01_tap_x.png'):
        actions.capture_for_gt('05_04_01_tap_x.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_effect_filter'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Filter')
    with step('[Action] tap_filter_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Basic')
    with step('[Action] tap_filter_template'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Vlogger 01')
    with step('[Action] tap_done_btn'):
        assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])
    with step('[Verify] verify_IAP'):
        assert actions.is_element_present(AppiumBy.NAME, 'In-App Purchase') or actions.is_element_present(AppiumBy.NAME, 'Restore Purchase')
    with step('[Action] close_IAP'):
        actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'closeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnCancel')])
    with step('[Action] tap_filter_template'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Vlogger 02')
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_04_01_tap_x_free.png'):
        actions.capture_for_gt('05_04_01_tap_x_free.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_effect_filter'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Filter')
    with step('[Action] tap_filter_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Basic')
    with step('[Action] tap_filter_template'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Vlogger 02')
    with step('[Action] tap_done_btn'):
        assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])
    with step('[Verify] snapshot: 05_04_01_after_look_v.png'):
        actions.capture_for_gt('05_04_01_after_look_v.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_04_01_no_look.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00047 completion"):
        assert True
