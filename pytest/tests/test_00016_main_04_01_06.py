import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00016_main_04_01_06')
def test_00016_main_04_01_06(actions: DriverActions):
    """camera - makeup"""
    uuid = ['af368125-3c99-471b-a7c1-52a91e78b2ec', '98bcdbf5-22ee-4641-ab12-202e3a33c488', 'b04161cd-10e5-4f51-bb47-e0d08cb3d209', '04f6f5f7-0c38-406e-9844-a5aa8bdfb816', 'a0a535da-4bec-4d43-89b7-7a43817a8162', '6309a2f2-ce33-4ee7-9747-cfed0788cc62', '2acfaed8-9e83-4395-8eb3-ace1336b322c', 'b643ae43-89dc-4049-b8a2-41bc40a6b8a4', 'aa73d83d-80b5-4e08-a992-040c09ff41fe', '6322dbc7-3f97-473b-a4bb-c91733db5c66', 'e0c0184a-de8a-4b73-b0aa-ae52d4029c4e', 'ae1f074b-53c7-4590-a246-4aba72e50a27', '19522125-9274-4aee-90aa-f9cd1022dc56', 'b7c08a65-c558-434a-873f-00d04599047e', '25799d98-d4a7-4db8-970c-3578bf3db026']
    with step('[Action] tap_camera'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnMore')
    with step('[Action] tap_makeup_btn2'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMakeup')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lipstick')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dried Rose 01')
    with step('[Verify] snapshot: 04_01_06_lipstick_default.png'):
        actions.capture_for_gt('04_01_06_lipstick_default.png', crop_rect=(0, 60, 276, 429))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_lipstick_min.png'):
        actions.capture_for_gt('04_01_06_lipstick_min.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('04_01_06_lipstick_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Lipstick min comparison fail'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_lipstick_max.png'):
        actions.capture_for_gt('04_01_06_lipstick_max.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('04_01_06_lipstick_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyebrows')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_eyebrows_default.png'):
        actions.capture_for_gt('04_01_06_eyebrows_default.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_eyebrows_min.png'):
        actions.capture_for_gt('04_01_06_eyebrows_min.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.compare_with_gt('04_01_06_eyebrows_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_eyebrows_max.png'):
        actions.capture_for_gt('04_01_06_eyebrows_max.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.compare_with_gt('04_01_06_eyebrows_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Shadow')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_eyeshadow_default.png'):
        actions.capture_for_gt('04_01_06_eyeshadow_default.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_eyeshadow_min.png'):
        actions.capture_for_gt('04_01_06_eyeshadow_min.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.compare_with_gt('04_01_06_eyeshadow_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_eyeshadow_max.png'):
        actions.capture_for_gt('04_01_06_eyeshadow_max.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.compare_with_gt('04_01_06_eyeshadow_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyeliner')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_eyeliner_default.png'):
        actions.capture_for_gt('04_01_06_eyeliner_default.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_eyeliner_min.png'):
        actions.capture_for_gt('04_01_06_eyeliner_min.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.compare_with_gt('04_01_06_eyeliner_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_eyeliner_max.png'):
        actions.capture_for_gt('04_01_06_eyeliner_max.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.compare_with_gt('04_01_06_eyeliner_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyelashes')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_eyelashes_default.png'):
        actions.capture_for_gt('04_01_06_eyelashes_default.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_eyelashes_min.png'):
        actions.capture_for_gt('04_01_06_eyelashes_min.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.compare_with_gt('04_01_06_eyelashes_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_eyelashes_max.png'):
        actions.capture_for_gt('04_01_06_eyelashes_max.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.compare_with_gt('04_01_06_eyelashes_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Contour')
    with step('[Verify] snapshot: 04_01_06_contour_default.png'):
        actions.capture_for_gt('04_01_06_contour_default.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_contour_min.png'):
        actions.capture_for_gt('04_01_06_contour_min.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.compare_with_gt('04_01_06_contour_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_contour_max.png'):
        actions.capture_for_gt('04_01_06_contour_max.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.compare_with_gt('04_01_06_contour_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Blush')
    if (not actions.tap_by_locator(AppiumBy.NAME, 'Natural')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_blush_default.png'):
        actions.capture_for_gt('04_01_06_blush_default.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_blush_min.png'):
        actions.capture_for_gt('04_01_06_blush_min.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.compare_with_gt('04_01_06_blush_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_06_blush_max.png'):
        actions.capture_for_gt('04_01_06_blush_max.png', AppiumBy.ACCESSIBILITY_ID, 'cpSlider')
    if (not actions.compare_with_gt('04_01_06_blush_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_shot_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    with step("[Verify] test_00016 completion"):
        assert True
