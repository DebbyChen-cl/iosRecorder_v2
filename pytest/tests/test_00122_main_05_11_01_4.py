import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00122_main_05_11_01_4')
def test_00122_main_05_11_01_4(actions: DriverActions):
    """add-image Blending mode"""
    mode = 1
    uuid = ['ef059dd2-4336-4781-b68b-f61c5d4a72e9', '9bdd7e43-7676-4d77-a344-c985ab2f25e5', '9cab9de4-85bc-4a98-989a-7a539ff5c2cc', '64776ee6-f1ec-4286-85d2-3a74706b6dec', '16ad9c6c-aadd-422b-a784-8a088f6f9076', 'a995bc99-b7e4-4f61-a73c-cb777fdefc13']
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
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Verify] snapshot: 05_11_01_before_blend.png'):
        actions.capture_for_gt('05_11_01_before_blend.png')
    destination = (364, 624)
    with step('[Action] drag_add_image_rotate'):
        actions.long_press_drag_from_element_to_coordinates(
            AppiumBy.IOS_CLASS_CHAIN,
            '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]',
            50.0,
            50.0,
            destination[0],
            destination[1],
        )
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blending mode')
    with step('[Verify] snapshot: 05_11_01_blend_normal.png'):
        actions.capture_for_gt('05_11_01_blend_normal.png')
    if actions.compare_with_gt('05_11_01_blend_normal.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'blend_normal comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Overlay')
    with step('[Verify] snapshot: 05_11_01_blend_overlay.png'):
        actions.capture_for_gt('05_11_01_blend_overlay.png')
    if actions.compare_with_gt('05_11_01_blend_overlay.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'blend_overlay comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Multiply')
    with step('[Verify] snapshot: 05_11_01_blend_multiply.png'):
        actions.capture_for_gt('05_11_01_blend_multiply.png')
    if actions.compare_with_gt('05_11_01_blend_multiply.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'blend_multiply comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Screen')
    with step('[Verify] snapshot: 05_11_01_blend_screen.png'):
        actions.capture_for_gt('05_11_01_blend_screen.png')
    if actions.compare_with_gt('05_11_01_blend_screen.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'blend_screen comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hardlight')
    with step('[Verify] snapshot: 05_11_01_blend_hardlight.png'):
        actions.capture_for_gt('05_11_01_blend_hardlight.png')
    if actions.compare_with_gt('05_11_01_blend_hardlight.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'blend_hardlight comparison failed'
    with step('[Action] swipe_functionlist'):
        actions.drag_within_elements(
            AppiumBy.ACCESSIBILITY_ID, 'Screen', 50.0, 50.0,
            AppiumBy.ACCESSIBILITY_ID, 'Multiply', 50.0, 50.0,
            duration=1.0,
        )
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Softlight')
    with step('[Verify] snapshot: 05_11_01_blend_softlight.png'):
        actions.capture_for_gt('05_11_01_blend_softlight.png')
    if actions.compare_with_gt('05_11_01_blend_softlight.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'blend_softlight comparison failed'
    with step("[Verify] test_00122 completion"):
        assert True
