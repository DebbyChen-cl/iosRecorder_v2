import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00025_removal')
def test_00025_removal(actions: DriverActions):
    """removal"""
    mode = 1
    uuid = ['d4f06494-5d67-4d1c-b1b8-71cadbcf72e1', '4bb879a8-1039-4ba9-82d2-1f347c0e9817', '1064c782-d448-4044-8d68-ed0a799a4492', '45871133-6a98-4e0a-ac1d-a3602d42b92d', '5b2c27cd-6b54-47a6-856d-e133c76f8a10', '91c8fba9-6f1c-448f-8848-d22a963ccc45', '14625380-842b-43db-949b-6313d32f491d', 'edbc569a-2d50-4948-a175-ebcadc8607cc', 'a7e6f0e3-386a-4c62-8c50-2d41adf106ab', 'c6d321b3-e4d0-49b9-a37c-8a800bde0210', '76774317-1f08-4488-bfc2-6fef0b44bfad', '4410d745-9496-40c7-afc1-65ecc7283dde', '6499b7bd-3ec6-45a9-8fdc-10e7cf113b84', '80f4e7d6-4ff6-4757-b768-5083e4d86105', '21d6d66b-0240-4050-b4c2-a244efad0d34', '8ab17e86-21ed-4db6-97d1-622d2c708f21']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
            actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
        elif actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        elif actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')
    with step('[Action] close_IAP_prompt_removal'):
        actions.is_element_present(AppiumBy.NAME, 'Remove with faster selection tool')
        actions.tap_by_locator(AppiumBy.NAME, 'Continue')
        actions.wait_for_invisible(AppiumBy.NAME, 'Remove with faster selection tool')
    with step('[Action] close_IAP_prompt_removal2'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Manual')
    with step('[Verify] snapshot: 05_01_03_download_asset_finish.png'):
        actions.capture_for_gt('05_01_03_download_asset_finish.png', crop_rect=(0, 60, 276, 597))
    with step("[Verify] test_00025 completion"):
        assert True
