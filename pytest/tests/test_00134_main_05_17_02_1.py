import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00134_main_05_17_02_1')
def test_00134_main_05_17_02_1(actions: DriverActions):
    """Live - auto add sparkle"""
    mode = 1
    uuid = ['24bf6587-0882-4189-9261-a27a6adc8f42', '64c45bde-bfa9-4998-97e6-e7c6cea17b4a', '0fc2db86-5768-40c8-9494-05a5ebb4aae0', '26982a3d-f87a-4271-a9d5-7853f6f9ab3c', '1499e577-d877-44b2-b80a-873b3e1334d0', '3b3f587f-5469-4fc5-9819-5c62dc3f2302', 'd5b8e722-c6e8-4b53-b09a-af0b8cfe9c03', '8dc58add-d4b2-4b10-aa12-2d57ffee2c76', '19df7db7-e84d-4d46-addf-9e8e30cf1361', '961f3304-b639-4ec7-9879-1d3b6ef388a9', '0eabc6a5-9b2a-49ce-a600-940ca70a0d0c', 'f6ac1a29-5d9c-4cbb-922f-7935686f25eb', 'be429969-0746-4fef-8a60-9cb7b2b1ae75', '333340c3-ee6c-410d-8b31-18beb0f78b28', 'c52b02cb-d6b2-4c70-9b35-1d239f37c5e7']
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
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sparkle')
    with step('[Verify] snapshot: 05_17_02_sparkle_default.png'):
        actions.capture_for_gt('05_17_02_sparkle_default.png')
    if actions.compare_with_gt('05_17_02_sparkle_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare sparkle default failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sparkle"`]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]')
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('98', '99', '100'))):
        pass
    else:
        assert False, 'adjust speed failed'
    if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'label == "photo animation btn pause n"'):
        pass
    else:
        assert False, 'verify playback failed'
    with step('[Action] tap_wraparound_pause'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sparkle"`]/XCUIElementTypeOther[2]/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]')):
        assert False, 'tap sparkle_template1_1 failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('98', '99', '100'))):
        pass
    else:
        assert False, 'adjust intensity failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Amount')):
        assert False, 'tap bokeh_amount failed'
    else:
        if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('99', '100'))):
            with step('[Action] adjust_bokeh_speed_slider'):
                actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')
        else:
            assert False, 'adjust amount failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')):
        assert False, 'tap bokeh_color failed'
    else:
        if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel') in ('179', '180'))):
            pass
        else:
            assert False, 'adjust hue failed'
        if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel') in ('99', '100'))):
            pass
        else:
            assert False, 'adjust saturation failed'
    with step("[Verify] test_00134 completion"):
        assert True
