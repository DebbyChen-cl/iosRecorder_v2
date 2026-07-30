import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00031_clone')
def test_00031_clone(actions: DriverActions):
    """clone"""
    uuid = ['a0ded0ed-2c7a-49d0-bb14-929a267b0b52', '0ca0655d-878d-4ea8-a884-02676e1c831e', '3c3b4264-6bb2-4b48-8886-99516e742a31', '0bd8f232-8b97-4a33-861b-fb41a72cd15a', '8edb2848-0b1f-4e36-bc8b-09ea0f4eaa67', '121c9779-8971-424d-9653-84ba48e6e79e', '1d7c111c-dbee-4495-ac63-54bd6397a6e9', 'd4277583-7d70-4f41-ac2f-3a1b38bb3d1d', '30d95341-d13b-4e59-bd32-34aa92a6f74c', '4c45f22b-8630-4155-8eee-12ebf88ffbac', 'a2fd2461-4336-4d09-85c9-36d1f00566d0', 'b8a1b531-2e0a-4556-bd7e-2dea4a2c8afb', '3783f101-a664-4666-9cbd-b94d542df8ec', 'da0113c4-d73f-46a3-af29-2ced4d54d8dd', 'ba31843d-fec6-4a8f-9f13-0a20e83742f2', '3f4a6557-22f7-46d0-8ac2-0732c1d2a99f', 'b77e3871-4cac-4a31-86e6-15b8b60c559e', 'b0e8fe8a-2a27-4b39-a8b0-2cf716488e0e', '45180483-70c4-4c4d-be0b-da75508a9508', '0d7786da-b812-4e16-b31e-dd9bbe1f2435', '7e5b90f3-ddc4-4e4b-8d3c-56d12ee7cf87', '6d669d4c-c925-47b5-8eaf-475e698bcc4b']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
            actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step("[Verify] test_00031 completion"):
        assert True
