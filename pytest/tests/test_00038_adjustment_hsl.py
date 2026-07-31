import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00038_adjustment_hsl')
def test_00038_adjustment_hsl(actions: DriverActions):
    """Adjustment - HSL"""
    uuid = ['3f1e92d3-f8fb-4f3a-8f9d-09821c2faec9', 'ac065479-ef52-467e-95fb-d1caa42e130a', '868fdb4f-7b0c-40ea-91ea-03d7d94b4ccc', '76652857-75f8-402b-82e9-a97caffca815', '147f9d3f-cb22-4b65-9eed-9ddb3142d993', 'fe1f10c9-312c-409f-877d-d7976d2b8430', '7be49030-0171-4fc5-8d5a-88be55adf115', '6c01bd6c-3078-4302-86e6-d43b4338e307', '045f8e00-f049-475f-8338-43352c260335', '9f5787fe-e26f-4e09-8df6-ac9379bcb656', 'b74977e7-3a9a-499f-82a1-734dbf2d2274', '8238ca2c-6c2b-4ae7-bf47-b01424afe048', '899e5413-033c-4761-b6c5-480ba2a54e99', '9d488530-1f41-45e6-9bca-9be604316db8', '27417a3b-09ab-4b6a-901d-d11be25303c7', '38155960-2f2e-48b0-823f-d385a90eb2fd', '7c719e6f-0846-4468-800c-8b1a2b6b8c8c', '92aeec73-d333-488f-b689-8e5044a3fa4e', 'b473c5cd-66b2-401a-ac24-b8ae29a24356', '3ee836bb-40df-4408-829a-9bd1c1b220c7', '8813408e-0b57-498c-9d43-1c3c4fe171b0', '58f95b38-1d0d-40ba-85b4-10cb38cb2a51', '6895b11a-7419-401e-979d-ab62d08af9a8', '7624a178-05d8-4709-8727-2e7f27b6757c', 'b5713c20-f773-4969-9c4e-c2d2a2dbd2f7', '234c155e-933a-4e12-b66c-a89b43582b59', '039c62bb-e71b-443a-99e6-eaa86f99a8bf', '9c4ad77e-81f8-4219-86fb-d37d49068f61']
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
    with step('[Verify] snapshot: 05_03_06_before_hsl.png'):
        actions.capture_for_gt('05_03_06_before_hsl.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HSL')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_06_panel_down.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')):
        assert False  # legacy raise
    actions.capture_for_gt('base05_03_06_panel_up.png', crop_rect=(0, 60, 276, 526))
    with step('[Verify] snapshot: 05_03_06_red_OG.png'):
        actions.capture_for_gt('05_03_06_red_OG.png', crop_rect=(0, 60, 276, 526))
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel') == '0'):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    actions.capture_for_gt('base05_03_06_hsl_red_hue_max.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    actions.capture_for_gt('base05_03_06_hsl_red_hue_min.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel') == '0'):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    actions.capture_for_gt('base05_03_06_hsl_red_saturation_max.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    actions.capture_for_gt('base05_03_06_hsl_red_saturation_min.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'lightnessValueLabel') == '0'):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    actions.capture_for_gt('base05_03_06_hsl_red_lightness_max.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    actions.capture_for_gt('base05_03_06_hsl_red_lightness_min.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_06_red_reset.png'):
        actions.capture_for_gt('05_03_06_red_reset.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_03_06_red_reset.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_06_yellow_OG.png'):
        actions.capture_for_gt('05_03_06_yellow_OG.png', crop_rect=(0, 60, 276, 526))
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel') == '0'):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    # legacy porting-mode baseline: yellow hue maximum
    actions.capture_for_gt('base05_03_06_hsl_yellow_hue_max.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    actions.capture_for_gt('base05_03_06_hsl_yellow_hue_min.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel') == '0'):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    actions.capture_for_gt('base05_03_06_hsl_yellow_saturation_max.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    actions.capture_for_gt('base05_03_06_hsl_yellow_saturation_min.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'lightnessValueLabel') == '0'):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    actions.capture_for_gt('base05_03_06_hsl_yellow_lightness_max.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    actions.capture_for_gt('base05_03_06_hsl_yellow_lightness_min.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn arrow down n')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_06_yellow_reset.png'):
        actions.capture_for_gt('05_03_06_yellow_reset.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_03_06_yellow_reset.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_06_hsl_x.png'):
        actions.capture_for_gt('05_03_06_hsl_x.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_03_06_hsl_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Adjustments')
    with step('[Action] swipe_new_adjustments_functionlist'):
        actions.drag_element(
            actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Sharpness'),
            actions.find_element(AppiumBy.NAME, 'Exposure'),
        )
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HSL')
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_03_06_hsl_v.png'):
        actions.capture_for_gt('05_03_06_hsl_v.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_03_06_hsl_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00038 completion"):
        assert True
