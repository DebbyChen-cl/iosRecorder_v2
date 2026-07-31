import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00125_main_05_11_01_7')
def test_00125_main_05_11_01_7(actions: DriverActions):
    """add-image 2nd image/layer adjust"""
    mode = 1
    uuid = ['49fc1a6f-a9aa-43c5-a893-814708593a2a', '3c85b34c-1a2b-422d-8fa5-0e6eba1699b2', 'b9fcd64a-3666-4276-8f36-88ba1fa06bd7', '4a12253b-cce4-4bd0-9b95-60a4d20576d7', '10e2d6a8-1b62-4a01-a365-cf5968e859c9']
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
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category_add_image'):
        assert actions.tap_by_locator(AppiumBy.NAME, '_AT')
    with step('[Action] add_image'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Verify] snapshot: 05_11_01_add_1_photo.png'):
        actions.capture_for_gt('05_11_01_add_1_photo.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category_add_image'):
        assert actions.tap_by_locator(AppiumBy.NAME, '_AT')
    with step('[Action] add_image'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Verify] snapshot: 05_11_01_add_2nd_photo.png'):
        actions.capture_for_gt('05_11_01_add_2nd_photo.png')
    if not actions.compare_with_gt('05_11_01_add_2nd_photo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Fail to verify second photo was added'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btn layer n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnLayerDown')
    with step('[Verify] snapshot: 05_11_01_layer_down.png'):
        actions.capture_for_gt('05_11_01_layer_down.png')
    if actions.compare_with_gt('05_11_01_layer_down.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Fail to verify layer down operation'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnLayerUp')
    with step('[Verify] snapshot: 05_11_01_layer_up.png'):
        actions.capture_for_gt('05_11_01_layer_up.png')
    if actions.compare_with_gt('05_11_01_layer_up.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Fail to verify layer up operation'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCamera')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoCapture')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use Photo')
    with step('[Verify] snapshot: 05_11_01_before_sticker.png'):
        actions.capture_for_gt('05_11_01_before_sticker.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_add_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Sticker')
    with step('[Action] select_sticker'):
        assert actions.tap_by_coordinates(45, 680), 'Fail to select sticker from panel'
    with step('[Verify] snapshot: 05_11_01_after_sticker.png'):
        actions.capture_for_gt('05_11_01_after_sticker.png')
    if (not actions.compare_with_gt('05_11_01_after_sticker.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Fail to verify sticker was added'
    with step("[Verify] test_00125 completion"):
        assert True
