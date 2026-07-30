import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00022_main_05_01_10')
def test_00022_main_05_01_10(actions: DriverActions):
    """AI enhance"""
    uuid = ['ea46eccc-8804-4339-b62c-3923cd684e1b', '93ef1a8f-9d69-42dc-b0f5-633803fbe328', '8ae9fb7e-e6fd-4239-8e35-da6298196d17', '65396ca6-7f1b-457b-ba5b-c85dc7fe0ba2', '0388da08-df16-42e9-940e-ae89841e9880']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Verify] snapshot: 05_01_10_before_aienhance.png'):
        before_aienhance_path = actions.capture_for_gt('05_01_10_before_aienhance.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_enhance1_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Enhance')
    with step('[Action] close_aienhance_iap_dialog'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
        assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
    with step('[Action] wait_enhance_process'):
        actions.wait_for_invisible(AppiumBy.NAME, 'Enhancing')
    with step('[Verify] snapshot: base_05_01_10_aienhance.png'):
        actions.capture_for_gt('base_05_01_10_aienhance.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiEnhanceStandardModeButton')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base_05_01_10_aienhance_off.png'):
        actions.capture_for_gt('base_05_01_10_aienhance_off.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    x_path = actions.capture_for_gt('05_01_10_aienhance_x.png', crop_rect=(0, 60, 276, 429))
    assert actions.compare_with_gt('05_01_10_before_aienhance.png', compare_path=x_path, gt_folder=TD.GT_FOLDER)[0]
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Enhance')):
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'generateButton')):
        assert False  # legacy raise
    with step('[Action] wait_enhance_process'):
        actions.wait_for_invisible(AppiumBy.NAME, 'Enhancing')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step("[Verify] test_00022 completion"):
        assert True
