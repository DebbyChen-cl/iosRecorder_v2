import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00021_main_05_01_09')
def test_00021_main_05_01_09(actions: DriverActions):
    """deblur"""
    uuid = ['a8c4fb11-599f-4586-9ae4-1fa4b468d2a1', 'c7e78403-d4a9-46ac-9474-9831ca61b294', 'b16ecc8c-a1e9-4756-86ff-ae8423180013', 'eb53df65-ce3f-4fb3-8843-7a0b2858ce97', 'db53692c-821d-40be-9738-6f3bb06d3f4c', '36ae7406-acec-40d5-b168-a8fb2ae806c8', '3ea73ba1-9771-41c2-88d4-d8526fd8e1ed']
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
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Verify] snapshot: 05_01_09_before_deblur.png'):
        before_deblur_path = actions.capture_for_gt('05_01_09_before_deblur.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Deblur')):
        assert False  # legacy raise
    with step('[Action] close_deblur_daily_limit'):
        assert actions.is_element_present(AppiumBy.NAME, 'Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur.')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur.')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'downloadingAssetText', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'downloadingAssetText')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Applying Deblur', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Applying Deblur')
    actions.tap_by_coordinates(200, 450)
    with step('[Action] adjust_fisheye_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')
    actions.capture_for_gt('base_05_01_09_deblur_min.png', crop_rect=(0, 60, 276, 429))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')):
        assert False  # legacy raise
    actions.capture_for_gt('base_05_01_09_deblur_max.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    x_path = actions.capture_for_gt('05_01_09_deblur_x.png', crop_rect=(0, 60, 276, 429))
    assert actions.compare_with_gt('05_01_09_before_deblur.png', compare_path=x_path, gt_folder=TD.GT_FOLDER)[0]
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Deblur')):
        assert False  # legacy raise
    with step('[Action] close_deblur_daily_limit'):
        actions.is_element_present(AppiumBy.NAME, 'Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur.')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.wait_for_invisible(AppiumBy.NAME, 'Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur.')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Applying Deblur', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Applying Deblur')
    with step('[Action] adjust_fisheye_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    with step("[Verify] test_00021 completion"):
        assert True
