import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00042_vignette')
def test_00042_vignette(actions: DriverActions):
    """Vignette"""
    mode = 1
    uuid = ['054940bc-ffbf-4fae-aaf1-d3df920e1089', 'fff777f9-abfd-46c3-a1bd-da97eed93b6c', ' ', '77ab387e-a618-4ad3-b6a8-1ff9fab25259', ' ', 'd9ffd760-7ce9-4eaf-8cdd-f7139aa754a8', '108f5725-efbe-427d-97b0-b3d45f9a2ca8', '1c4d357c-adb7-4af3-9f66-a992d2a20151', 'c3ff0314-f427-4f23-8861-dc40f254f8bc', '7b0a41a8-e7e3-4ee9-b7e8-e6952d28f1ca', 'b80fc384-f171-4eaa-8cde-ebe97c933bf1', '  ', 'db7ea93c-65fc-4e67-9f75-b3f23721c17d', 'f6c929cc-88b1-4eac-9233-7ae4caf0e6b8', '  ', '4917957d-b112-43eb-9189-5004df86c13c', 'b6a8b204-5758-4b9a-8200-582ba7d27535', '4fd2e0e0-1f2d-4236-8fc7-a93a0928dc34', '2fc2f848-6f47-4282-ac45-768208dec0c9', '26820bd0-b095-4d81-8ddf-59695a9a1188', '3460afc3-c1d3-40f2-a799-f242e8b793c4']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_09_before_vignette.png'):
        actions.capture_for_gt('05_03_09_before_vignette.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Vignette')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_03_09_vignette_default.png'):
        actions.capture_for_gt('base05_03_09_vignette_default.png', crop_rect=(0, 60, 276, 526))
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') == '-75'):
        pass
    with step('[Action] adjust_vignette_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100')):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] adjust_vignette_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)
    with step('[Verify] snapshot: base05_03_09_vignette_shade_min.png'):
        actions.capture_for_gt('base05_03_09_vignette_shade_min.png', crop_rect=(0, 60, 276, 526))
    from_pos = (206, 85)
    destination = (206, 160)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 85, 206, 160)
    with step('[Verify] snapshot: base05_03_09_adjust_top.png'):
        actions.capture_for_gt('base05_03_09_adjust_top.png', crop_rect=(0, 60, 276, 526))
    from_pos = (402, 374)
    destination = (372, 374)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(402, 374, 372, 374)
    with step('[Verify] snapshot: base05_03_09_adjust_right.png'):
        actions.capture_for_gt('base05_03_09_adjust_right.png', crop_rect=(0, 60, 276, 526))
    from_pos = (200, 450)
    destination = (236, 396)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(200, 450, 236, 396)
    with step('[Verify] snapshot: base05_03_09_move.png'):
        actions.capture_for_gt('base05_03_09_move.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    else:
        with step('[Verify] snapshot: 05_03_09_exit_vignette.png'):
            actions.capture_for_gt('05_03_09_exit_vignette.png', crop_rect=(0, 60, 276, 429))
        if actions.compare_with_gt('05_03_09_exit_vignette.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Vignette')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feather')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') == '30'):
        pass
    with step('[Action] adjust_vignette_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)
    with step('[Verify] snapshot: base05_03_09_vignette_feather_max.png'):
        actions.capture_for_gt('base05_03_09_vignette_feather_max.png', crop_rect=(0, 60, 276, 526))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('0', '1', '2')):
        pass
    else:
        assert False  # legacy raise
    from_pos = (206, 85)
    destination = (206, 160)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 85, 206, 160)
    with step('[Verify] snapshot: base05_03_09_adjust_top_f.png'):
        actions.capture_for_gt('base05_03_09_adjust_top_f.png', crop_rect=(0, 60, 276, 526))
    from_pos = (402, 378)
    destination = (372, 378)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(402, 378, 372, 378)
    with step('[Verify] snapshot: base05_03_09_adjust_right_f.png'):
        actions.capture_for_gt('base05_03_09_adjust_right_f.png', crop_rect=(0, 60, 276, 526))
    from_pos = (200, 450)
    destination = (236, 396)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(200, 450, 236, 396)
    with step('[Verify] snapshot: base05_03_09_move_f.png'):
        actions.capture_for_gt('base05_03_09_move_f.png', crop_rect=(0, 60, 276, 526))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    else:
        with step('[Verify] snapshot: 05_03_09_exit_vignette_v.png'):
            actions.capture_for_gt('05_03_09_exit_vignette_v.png', crop_rect=(0, 60, 276, 429))
        if (not actions.compare_with_gt('05_03_09_exit_vignette_v.png', gt_folder=TD.GT_FOLDER)[0]):
            pass
        else:
            assert False  # legacy raise
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00042 completion"):
        assert True
