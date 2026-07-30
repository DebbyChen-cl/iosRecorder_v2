import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00039_adjustment_temperature_and_tint')
def test_00039_adjustment_temperature_and_tint(actions: DriverActions):
    """Adjustment - temperature and tint"""
    mode = 1
    uuid = ['b6523058-3ecf-4578-937e-b358e4350e8c', 'c5170471-7f9f-431f-b677-bcfd300a5469', '49b29579-fc50-4710-9cc1-74b8cf0f68e5', '45f15b65-376c-4840-aa2f-179341c1f835', '0d945412-4031-4dcb-bfc2-1ded13a65530', '811b2c8a-5b5b-4f89-be07-e0f024d08f97', 'a397765d-3b1d-40d0-a88f-33b68fde16ee', '5dbe7ea3-aa52-4aa4-b11e-b23a8c0b1b43', '90cd6f43-3a06-49bd-a66a-4940c7b95eb7', '412f102e-15f4-438d-9277-5984f818ee89', '4d5b0b72-bb1a-4d28-b8e9-f281c992ef50', '6f319979-a7ea-42df-bcf6-273582b4fdb5', '069f0cf2-3fb5-4e02-abd8-fbe2659f8359', '74ccef08-6647-4de6-b915-e1e19b79661b', '45a68687-5f34-4f5e-9e28-77da539d46e8', '88cd955e-58d8-48a1-a8bb-c5454f4363f5', '7e78f681-56c8-41d4-89bd-d8eebf7c1a1b', '831f50ad-66a4-45d5-9c36-53a914483c98', '1bc3df6a-2afb-4875-87fa-6f3598df8f92', '46f19ae1-7710-4b46-8019-f061e6bd362d', 'bc1e68f9-6a3f-4a6b-867e-25ae9ba5a570', 'e7b1af17-e259-49ec-87dd-20e48d2be626']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
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
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_08_before_temp.png'):
        actions.capture_for_gt('05_03_08_before_temp.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto Color')):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_08_temperature_auto.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto Color')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Temperature')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton') == '0'):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_08_temp_slider_min.png', crop_rect=(0, 60, 276, 429))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_08_temp_slider_max.png', crop_rect=(0, 60, 276, 429))
    from_pos = (400, 460)
    destination = (50, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 460, 50, 460)
    actions.capture_for_gt('base05_03_08_temp_scr_min.png', crop_rect=(0, 60, 276, 429))
    from_pos = (50, 460)
    destination = (400, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 460, 400, 460)
    actions.capture_for_gt('base05_03_08_temp_scr_max.png', crop_rect=(0, 60, 276, 429))
    destination = (300, 200)
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'whiteBalanceDropperButton')):
        assert False  # legacy raise
    if (not actions.tap_by_coordinates(300, 230)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_08_temp_dropper.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_08_tap_x.png'):
        actions.capture_for_gt('05_03_08_tap_x.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_03_08_tap_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tint')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton') == '0'):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_08_tint_slider_min.png', crop_rect=(0, 60, 276, 429))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_08_tint_slider_max.png', crop_rect=(0, 60, 276, 429))
    from_pos = (400, 460)
    destination = (10, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 460, 10, 460)
    actions.capture_for_gt('base05_03_08_tint_scr_min.png', crop_rect=(0, 60, 276, 429))
    from_pos = (10, 460)
    destination = (400, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(10, 460, 400, 460)
    actions.capture_for_gt('base05_03_08_tint_scr_max.png', crop_rect=(0, 60, 276, 429))
    destination = (300, 200)
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'whiteBalanceDropperButton')):
        assert False  # legacy raise
    if (not actions.tap_by_coordinates(300, 230)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_08_tint_dropper.png', crop_rect=(0, 60, 276, 429))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_08_adjust_tap_v.png'):
        actions.capture_for_gt('05_03_08_adjust_tap_v.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_03_08_adjust_tap_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00039 completion"):
        assert True
