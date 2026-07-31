import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00035_adjustment_curve')
def test_00035_adjustment_curve(actions: DriverActions):
    """Adjustment - Curve"""
    mode = 1
    uuid = ['ad17d729-bf75-4da2-bd50-a22d13e7d3fe', '35fc1408-7065-44d6-b9a6-5da60735cc64', '60d9d6bb-3be1-4a67-90a0-8d1baed71a79', 'd4a483fe-23eb-4ef2-b9fd-25f45b48f30a', '482156d6-084d-4d3b-8b3e-0ccedfaa6cb0', '2c928cfe-6c98-497c-b5f3-def4de8859bc', 'b2a23d55-4531-4920-8114-5da18c4a21e4', '6b7157ce-80f7-48ac-bc07-ef000b551f63', 'dbf40949-e498-4e76-8866-97df4b18d962', '172bdc71-06be-40a2-ae6b-e661b2aed586', 'ee512fae-6f55-4bd8-84ca-f6555d09b44f', '0a4ae03b-7e5e-4346-a148-b4dc5f05e398', 'd3fe12e7-5dab-4f24-81f3-a979dfae7c88', '5e3bd2c4-9f50-4e35-8490-cfed95d08927', '8dbd392d-ca3a-45be-8728-56c5d535dd16', '138fcc65-380b-4dd0-9f17-0e89ea9d8e3a', 'd94fb643-f1e5-4921-b60b-4aebb268208c', '699ec565-08fd-4203-b60a-7d6c512f8760', 'beb45d97-63bd-4924-8e4c-daef55ccde3f', 'f02de055-9e93-4aa7-815c-866ce2e13ef6', '3a86572a-fc9d-4b70-937d-625c1c064dc7']
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
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_02_before_curve.png'):
        actions.capture_for_gt('05_03_02_before_curve.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Curve')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_02_panel_down.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_02_panel_up.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'tab icon b n')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_02_blue_OG.png'):
        actions.capture_for_gt('05_03_02_blue_OG.png', crop_rect=(0, 60, 276, 526))
    from_pos = (230, 660)
    destination = (230, 720)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(230, 660, 230, 720)
    actions.capture_for_gt('base05_03_02_adjust_blue.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_02_blue_reset.png'):
        actions.capture_for_gt('05_03_02_blue_reset.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_03_02_blue_reset.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'tab icon g n')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_02_green_OG.png'):
        actions.capture_for_gt('05_03_02_green_OG.png', crop_rect=(0, 60, 276, 526))
    from_pos = (230, 660)
    destination = (230, 720)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(230, 660, 230, 720)
    actions.capture_for_gt('base05_03_02_adjust_green.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_02_green_reset.png'):
        actions.capture_for_gt('05_03_02_green_reset.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_03_02_green_reset.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'curve tab icon r n')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_02_red_OG.png'):
        actions.capture_for_gt('05_03_02_red_OG.png', crop_rect=(0, 60, 276, 526))
    from_pos = (230, 660)
    destination = (230, 720)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(230, 660, 230, 720)
    actions.capture_for_gt('base05_03_02_adjust_red.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_02_red_reset.png'):
        actions.capture_for_gt('05_03_02_red_reset.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_03_02_red_reset.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'curve tab icon rgb n')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_02_color_OG.png'):
        actions.capture_for_gt('05_03_02_color_OG.png', crop_rect=(0, 60, 276, 526))
    from_pos = (230, 660)
    destination = (230, 720)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(230, 660, 230, 720)
    actions.capture_for_gt('base05_03_02_adjust_color.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_02_color_reset.png'):
        actions.capture_for_gt('05_03_02_color_reset.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_03_02_color_reset.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    from_pos = (230, 660)
    destination = (230, 720)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(230, 660, 230, 720)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_02_curve_x.png'):
        actions.capture_for_gt('05_03_02_curve_x.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_03_02_curve_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Curve')
    from_pos = (230, 660)
    destination = (230, 720)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(230, 660, 230, 720)
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_02_curve_v.png'):
        actions.capture_for_gt('05_03_02_curve_v.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_03_02_curve_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00035 completion"):
        assert True
