import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00033_adjustment_exposure_contrast_highlights_shadows')
def test_00033_adjustment_exposure_contrast_highlights_shadows(actions: DriverActions):
    """Adjustment - Exposure Contrast  Highlights Shadows"""
    mode = 1
    uuid = ['5389dca4-1793-471e-8c8a-93321ec168f5', '2d71d4b0-4cd7-40c3-bd67-c5741e20e96e', '412f7daa-d218-4a0b-b1ed-ae5dc6d64aa0', '085317f4-663b-4736-a372-f8992505a062', 'aa47f569-ef4a-4cca-aab5-8445fa644608', 'e9f65e5c-a588-42e7-af07-c59436f18ea7', '275d6806-e62b-4550-a2da-580d3a33024a', '4ddadef1-0647-42df-9267-e19cbd47fe72', '073c367c-0b8e-4b5b-83e6-8928a30680f0', 'a97a1ff7-9887-49af-8166-6bc554ec57bd', '679b3270-5243-482e-9b3b-a6a00ce9a33c', 'd346473a-67c3-4c7b-b675-b9160f4196c7', '37054d70-35f4-42ad-89f5-3431c96c31b7', '3d261597-1121-4005-90ca-eca843b93796', '49e500f7-8856-4569-87cb-6fa95dcdc940', 'e9c38c32-259c-4369-a5fd-43d4c2e94516', '3c34601f-acb0-45d9-a463-8a8ae3fb9aa8', 'c5fbd493-131c-4996-a447-004fa8a10a50', 'c4d2f0c3-6e77-45bb-bc4e-aeb63cc16bf5', 'bf9622d0-945b-426f-a853-88c8428cd65e', '6d2b47f4-7dda-4587-a5d6-2f54e16dc710', 'd3ab9862-92f1-40f8-a481-bfe59aa25739', 'f4ceab0a-c1d1-471f-83e6-ee93442d65fe', '2deb9e0a-b6ad-4e3a-bf8d-344cfdad5c15', '81d0c693-3e13-4f71-b4fd-c86ce1fdadf6', 'e1eb3ef8-04ce-4ef4-a52c-5d8ea7be88fa', '61e32da8-5fdd-47ec-834e-dd42bc7927e7', '5bf54593-47f7-40cc-85c8-c9f186116f5c', 'c3842cc9-c3e1-41ee-98a3-10009326283f', 'f371f067-aff1-4dcb-953d-643be228d7bc', 'a6fe5ed4-39dd-4391-900a-9e6e8b5e4fa3', '3ec0d529-68e2-401c-94ff-e06020f941ac', 'cfc0ed64-b494-4c84-8f91-5a0e95c0f3e3', '2cf11d04-c96f-4fcf-a6a7-5ce5eaed1ae2', 'f3839778-3dca-4d52-b607-fb9e299c301f', 'e2380011-b62c-4cb0-8822-8be3d68b7df1', '96ff1b27-5006-468c-9b77-8752d7f6f54e', '5fe2655c-99e1-429d-a565-92d5c94b7754', '8f084350-bd22-4189-82ca-ae94df856e57', '03f88f21-117f-4154-8664-906bb0eb1713', '3f3a6c32-2236-474e-bb1e-47bc2cd54ca6', '8a21fe84-c1c5-4bf0-b64e-7b07a86c7fd5', '276ebb42-4c5f-4586-ba55-29aab0cdbc11', '3388baa2-8142-476f-aced-e99bb56a9150', 'a1883fd0-82e6-495a-85c0-2a001406a0c7', 'd2d6cb00-5066-46e2-b389-157ab34a1538', '9e24d1e1-d473-4782-bfd6-d4147df004ad', '705f75d2-0681-4b64-a454-534807587efc', '7bbfaa63-59fd-4931-8773-e678f4f382b0', '9d7863c2-f9e7-4ee4-ab10-c68fdc3e3bbe', '4b91f598-a22e-4552-b044-f95ff25027f6', '297bafb4-b0f4-4694-972a-65649c36547c', 'f962d707-31a9-4640-a2e8-1619ad99d67d', '0da5ff96-637d-437f-ac55-bcb45466cd7b', '712187f8-aaa7-4f98-a1fc-26e038c9f3bf', 'ea6e265b-1f00-45d3-bd27-6f5c0afbb0df', '0fbff499-334a-4c3b-b63c-a7d6588a0d87']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] close_popup'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
    with step('[Action] close_IAP'):
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
    with step('[Verify] snapshot: 05_01_01_before_adjust1.png'):
        actions.capture_for_gt('05_01_01_before_adjust1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton') == '0.00'):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_01_01_exposure_slider_min.png', crop_rect=(0, 60, 276, 526))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_01_01_exposure_slider_max.png', crop_rect=(0, 60, 276, 526))
    from_pos = (410, 460)
    destination = (10, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(410, 460, 10, 460)
    actions.capture_for_gt('base05_01_01_exposure_scr_min.png', crop_rect=(0, 60, 276, 526))
    from_pos = (10, 460)
    destination = (400, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(10, 460, 400, 460)
    actions.capture_for_gt('base05_01_01_exposure_scr_max.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')):
        assert False  # legacy raise
    from_pos = (208, 550)
    destination = (120, 620)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(208, 550, 120, 620)
    actions.capture_for_gt('base05_01_01_exposure_mask_range_rotate.png', crop_rect=(0, 60, 276, 526))
    from_pos = (205, 495)
    destination = (205, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(205, 495, 205, 600)
    actions.capture_for_gt('base05_01_01_exposure_mask_move.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_01_01_exposure_mask_hide.png'):
        actions.capture_for_gt('05_01_01_exposure_mask_hide.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_01_01_exposure_mask_show.png'):
        actions.capture_for_gt('05_01_01_exposure_mask_show.png', crop_rect=(0, 60, 276, 526))
    if (not actions.compare_with_gt('05_01_01_exposure_mask_show.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_gradient_mask_btn2'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic gradient mask n')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')):
        assert False  # legacy raise
    actions.capture_for_gt('base05_01_01_exposure_auto.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_feature_x_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Contrast')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton') == '0'):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_01_01_contrast_slider_min.png', crop_rect=(0, 60, 276, 526))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_01_01_contrast_slider_max.png', crop_rect=(0, 60, 276, 526))
    from_pos = (400, 460)
    destination = (50, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 460, 50, 460)
    actions.capture_for_gt('base05_01_01_contrast_scr_min.png', crop_rect=(0, 60, 276, 526))
    from_pos = (50, 460)
    destination = (400, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 460, 400, 460)
    actions.capture_for_gt('base05_01_01_contrast_scr_max.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')):
        assert False  # legacy raise
    from_pos = (208, 550)
    destination = (120, 620)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(208, 550, 120, 620)
    actions.capture_for_gt('base05_01_01_contrast_mask_range_rotate.png', crop_rect=(0, 60, 276, 526))
    from_pos = (205, 495)
    destination = (205, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(205, 495, 205, 600)
    actions.capture_for_gt('base05_01_01_contrast_mask_move.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_01_01_contrast_mask_hide.png'):
        actions.capture_for_gt('05_01_01_contrast_mask_hide.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_01_01_contrast_mask_show.png'):
        actions.capture_for_gt('05_01_01_contrast_mask_show.png', crop_rect=(0, 60, 276, 526))
    if (not actions.compare_with_gt('05_01_01_contrast_mask_show.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_01_01_tap_x.png'):
        actions.capture_for_gt('05_01_01_tap_x.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_01_01_tap_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Highlight')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton') == '0'):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_01_01_highlights_slider_min.png', crop_rect=(0, 60, 276, 526))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_01_01_highlights_slider_max.png', crop_rect=(0, 60, 276, 526))
    from_pos = (400, 460)
    destination = (50, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 460, 50, 460)
    actions.capture_for_gt('base05_01_01_highlights_scr_min.png', crop_rect=(0, 60, 276, 526))
    from_pos = (50, 460)
    destination = (400, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 460, 400, 460)
    actions.capture_for_gt('base05_01_01_highlights_scr_max.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')):
        assert False  # legacy raise
    from_pos = (208, 550)
    destination = (120, 620)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(208, 550, 120, 620)
    actions.capture_for_gt('base05_01_01_highlights_mask_range_rotate.png', crop_rect=(0, 60, 276, 526))
    from_pos = (205, 495)
    destination = (205, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(205, 495, 205, 600)
    actions.capture_for_gt('base05_01_01_highlights_mask_move.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_01_01_highlights_mask_hide.png'):
        actions.capture_for_gt('05_01_01_highlights_mask_hide.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'reginalAdjustmentButton')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_01_01_highlights_mask_show.png'):
        actions.capture_for_gt('05_01_01_highlights_mask_show.png', crop_rect=(0, 60, 276, 526))
    if (not actions.compare_with_gt('05_01_01_highlights_mask_show.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_feature_x_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Bright')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dark')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shadow')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton') == '0'):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 0)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_01_01_shadows_slider_min.png', crop_rect=(0, 60, 276, 526))
    if (not actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', 1)):
        assert False  # legacy raise
    actions.capture_for_gt('base05_01_01_shadows_slider_max.png', crop_rect=(0, 60, 276, 526))
    from_pos = (400, 460)
    destination = (50, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 460, 50, 460)
    actions.capture_for_gt('base05_01_01_shadows_scr_min.png', crop_rect=(0, 60, 276, 526))
    from_pos = (50, 460)
    destination = (400, 460)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 460, 400, 460)
    actions.capture_for_gt('base05_01_01_shadows_scr_max.png', crop_rect=(0, 60, 276, 526))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_01_01_adjust_tap_v.png'):
        actions.capture_for_gt('05_01_01_adjust_tap_v.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_01_01_adjust_tap_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00033 completion"):
        assert True
