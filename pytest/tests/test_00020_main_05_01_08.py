import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00020_main_05_01_08')
def test_00020_main_05_01_08(actions: DriverActions):
    """denoise"""
    uuid = ['37d2aa7f-3d80-41a6-98c9-5c8f89e8642a', 'a7a7acda-a4e2-4422-ab6c-cb99b4a95f4b', 'e9af9d16-31e8-4ab5-b343-737dc81fad5d', '19ef176e-17b8-4705-89fb-c238c783b0a9', '1caf590c-8338-4059-9b91-321591e963a3', '36ae7406-acec-40d5-b168-a8fb2ae806c8', '3ea73ba1-9771-41c2-88d4-d8526fd8e1ed']
    with step('[Action] close_continue_edit'):
        actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
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
    with step('[Verify] snapshot: 05_01_08_before_denoise.png'):
        actions.capture_for_gt('05_01_08_before_denoise.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')):
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'Denoise')):
        assert False  # legacy raise
    with step('[Action] close_denoise_daily_limit'):
        if actions.is_element_present(AppiumBy.NAME, 'Eliminate the noise in your low light or high-ISO photos with our latest AI technology.'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
            assert actions.wait_for_invisible(AppiumBy.NAME, 'Eliminate the noise in your low light or high-ISO photos with our latest AI technology.')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'downloadingAssetText', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'downloadingAssetText')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Applying Denoise', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Applying Denoise')
    with step('[Action] adjust_fisheye_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')):
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_01_08_denoise_x.png'):
        actions.capture_for_gt('05_01_08_denoise_x.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] denoise cancel state'):
        assert actions.compare_with_gt('05_01_08_denoise_x.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_enhance1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'Denoise')):
        assert False  # legacy raise
    with step('[Action] close_denoise_intro_dialog'):
        actions.is_element_present(AppiumBy.NAME, 'Eliminate the noise in your low light or high-ISO photos with our latest AI technology.')
        actions.tap_by_locator(AppiumBy.NAME, 'Denoise')
        actions.wait_for_invisible(AppiumBy.NAME, 'Eliminate the noise in your low light or high-ISO photos with our latest AI technology.')
    with step('[Action] close_denoise_daily_limit'):
        actions.is_element_present(AppiumBy.NAME, 'Eliminate the noise in your low light or high-ISO photos with our latest AI technology.')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.wait_for_invisible(AppiumBy.NAME, 'Eliminate the noise in your low light or high-ISO photos with our latest AI technology.')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Applying Denoise', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Applying Denoise')
    with step('[Action] adjust_fisheye_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    with step("[Verify] test_00020 completion"):
        assert True
