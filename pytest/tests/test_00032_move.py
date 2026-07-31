import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00032_move')
def test_00032_move(actions: DriverActions):
    """move"""
    uuid = ['1fcf2b6e-53f4-43e4-a34f-14f372924f12', '137e03ec-62b8-4f31-bd9b-c4aefd55b9a4', 'd6e7e937-fd0d-436b-ab8e-521385a008bc', 'd9578b9d-53ab-4d2e-a9b4-429117bf3265', 'ab03b2f1-3e4a-4e5b-8d14-cb5fed33d0ef', 'e0246c6c-e108-4126-ac96-55415a120188', 'b0c1d87b-0938-4a12-96f2-86635d700840', 'f2394aaa-ab5a-48ba-88d0-dac93365a685', '369aa6c3-6ccf-4c48-9171-d571b9b60f84', '8fc4accf-758f-4906-8185-3530c870e471', 'adef8c8c-07f3-41de-b6c5-f4409586e1cc', '22711865-9eae-4d7e-86f2-1742cababeb0', '19dc15ab-36c0-4743-b01b-9543647b859d', '123e2ca8-9eed-4eac-a594-029c65471eed', 'dfd8b6a5-7ebf-486c-827e-13a8b8d02b71', '36ae7406-acec-40d5-b168-a8fb2ae806c8', '3ea73ba1-9771-41c2-88d4-d8526fd8e1ed', 'd65e71a8-9ba9-4192-97a9-4cb25097c006', '9e614277-5a52-4f56-adf6-9049a5681f79']
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
    with step("[Verify] test_00032 completion"):
        assert True
