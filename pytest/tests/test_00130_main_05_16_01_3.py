import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00130_main_05_16_01_3')
def test_00130_main_05_16_01_3(actions: DriverActions):
    """Live - overlays"""
    mode = 1
    uuid = ['0ffc2635-065f-4bb4-9060-2053b578cbb1', '61aa8512-b36b-4f66-95c8-7f99a9761a2d', '928c872d-fa9d-43e3-a9db-aea83dcd3c72', '5ca21686-cdf4-4d67-9352-9dc4b8d961d3', 'fddc5da3-b667-46af-97d9-23e8159e3836', '16d76fa3-0790-47c1-b1cf-fc142bf2f50c', '49077bdb-9076-43eb-8007-a5689f4a8ec3', '9d6a282a-c966-40fe-a6f6-2d232e6000dd', '9c8ec1ce-4ebd-4a6d-a09a-a74e0cf25a84', '34806465-6886-4458-a309-a9f1eb32c388', '856202ae-6797-4940-ab40-bbeb01ed79ae', '1e85f5e4-0e87-44e6-a997-06dd0bbc39aa', '4de51ccf-dc3f-4c0b-83e1-cf87d74dbbe0', '2a61aa45-c09d-462f-bedb-2829feb5dd18', '9145befa-82f4-40e0-adf3-4924ce95d42f', 'cadd1fa2-edf4-4e60-b43b-2339886061a6', '8ee05833-007d-4b29-89cf-41bf2e5ea629', '16a2b91f-ff1e-4c06-bf9c-eb5950b584fc', '710c4480-fc0f-4c04-97c8-8afba6ffff2b', '10556b61-a279-4eb4-a311-09276ca2083b', 'c3bd05af-3dc3-44fd-abed-afa8e48a47c2', '812cb7fe-48e5-4ddd-9dc3-61b027d88eed']
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
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animated Overlays')
    with step('[Verify] snapshot: 05_16_01_no_overlay.png'):
        actions.capture_for_gt('05_16_01_no_overlay.png')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-Effect_2021_Angel_cloud_fly')):
        assert False, 'tap overlay template1 failed'
    with step('[Verify] snapshot: 05_16_01_after_overlay1.png'):
        actions.capture_for_gt('05_16_01_after_overlay1.png')
    if (not actions.compare_with_gt('05_16_01_after_overlay1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare add overlay template failed'
    if actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1') and actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "animated_overlay"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeStaticText') in '2x':
        pass
    else:
        assert False, 'adjust overlay speed to 2x failed'
    if actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0.5') and actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "animated_overlay"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeStaticText') in '1x':
        pass
    else:
        assert False, 'adjust overlay speed to 1x failed'
    if actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0') and actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "animated_overlay"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeStaticText') in '0.5x':
        pass
    else:
        assert False, 'adjust overlay speed to 0.5x failed'
    if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'label == "photo animation btn pause n"'):
        pass
    else:
        assert False, 'verify overlay playback failed'
    with step('[Action] tap_wraparound_pause'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Verify] snapshot: 05_16_01_overlay_before_mask.png'):
        actions.capture_for_gt('05_16_01_overlay_before_mask.png')
    with step('[Action] tap_phd_element'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-Effect_2021_Rainbow_A')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch')
    from_pos = (110, 214)
    destination = (110, 500)
    mode = 1
    with step('[Verify] snapshot: 05_16_01_before_brush-.png'):
        actions.capture_for_gt('05_16_01_before_brush-.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(110, 214, 110, 500)
    with step('[Verify] snapshot: 05_16_01_after_brush-.png'):
        actions.capture_for_gt('05_16_01_after_brush-.png')
    if (not actions.compare_with_gt('05_16_01_after_brush-.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare eraser brush failed'
    with step('[Action] tap_live_undo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step('[Verify] snapshot: 05_16_01_after_undo.png'):
        actions.capture_for_gt('05_16_01_after_undo.png')
    if actions.compare_with_gt('05_16_01_after_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare undo brush failed'
    with step('[Action] tap_live_redo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    with step('[Verify] snapshot: 05_16_01_after_redo.png'):
        actions.capture_for_gt('05_16_01_after_redo.png')
    if actions.compare_with_gt('05_16_01_after_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare redo brush failed'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn live brush n')
    from_pos = (110, 220)
    destination = (110, 430)
    mode = 1
    with step('[Verify] snapshot: 05_16_01_before1.png'):
        actions.capture_for_gt('05_16_01_before1.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(110, 220, 110, 430)
    with step('[Verify] snapshot: 05_16_01_after1.png'):
        actions.capture_for_gt('05_16_01_after1.png')
    if (not actions.compare_with_gt('05_16_01_after1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare eraser + brush failed'
    with step('[Verify] snapshot: 05_16_01_brushsize_before.png'):
        actions.capture_for_gt('05_16_01_brushsize_before.png')
    with step('[Action] adjust_harmonization_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_16_01_brushsize_after.png'):
        actions.capture_for_gt('05_16_01_brushsize_after.png')
    if (not actions.compare_with_gt('05_16_01_brushsize_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare brush size failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn mask switch n')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_wraparound_n')
    with step("[Verify] test_00130 completion"):
        assert True
