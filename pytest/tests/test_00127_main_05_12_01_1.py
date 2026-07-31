import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00127_main_05_12_01_1')
def test_00127_main_05_12_01_1(actions: DriverActions):
    """frame download"""
    mode = 1
    uuid = ['b194d95b-453f-4306-a96c-4d89ecd1fc0c', '97de2600-c802-4f88-b282-431ccb87ced6', 'db471061-da08-4b08-ba98-d456575794dd', '33610960-a8c7-4256-9b50-c8ade4e58825']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Verify] snapshot: 05_12_01_before_frame.png'):
        actions.capture_for_gt('05_12_01_before_frame.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Frame')
    with step('[Verify] snapshot: 05_12_01_frame_default.png'):
        actions.capture_for_gt('05_12_01_frame_default.png')
    with step('[Action] tap_frame_add'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn effect store n')
        assert actions.is_element_present(AppiumBy.NAME, 'New')
    with step('[Action] select_frame_store_item'):
        assert actions.tap_by_coordinates(68, 250)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Download')):
        assert False, 'tap download button failed'
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Use'):
        pass
    else:
        assert False, 'verify store use button failed'
    with step('[Action] close_ad_if_present'):
        if actions.is_element_present(AppiumBy.NAME, 'ad present btn close', timeout=1):
            actions.tap_by_locator(AppiumBy.NAME, 'ad present btn close')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn webstore back n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn webstore back n')
    with step('[Verify] snapshot: 05_12_01_frame_after_download.png'):
        actions.capture_for_gt('05_12_01_frame_after_download.png')
    if (not actions.compare_with_gt('05_12_01_frame_after_download.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'downloaded frame not listed after download'
    with step("[Verify] test_00127 completion"):
        assert True
