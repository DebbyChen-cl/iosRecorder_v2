import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00135_main_05_17_02_2')
def test_00135_main_05_17_02_2(actions: DriverActions):
    """Live - manual add sparkle"""
    uuid = ['f93ca778-bc2c-45d3-8be4-5240a3da9343', '8787ca29-9473-4bc9-89e2-186d22c5647b', 'c0fc8f79-ae86-4553-959f-45b97236a047', 'c0decb7a-c952-4803-af67-03f5129393c7', 'b7502055-2131-4819-a64e-796576b8cb32', '173ba08f-dae6-4407-99ef-aafd8d3737d5', '3b8d0e02-c475-4131-9f3f-9c0967e9f824', '19259ad3-7bda-4f16-bfc9-67cb10a8ede3', '21974e87-b3f1-44b2-a071-a6bd755a1e9f', '4c133873-d65b-425c-9ba3-abeaccda14db', 'ef13e2d7-6d06-4b6c-9229-61c28b3fb0e4', 'b6bb4d29-06c4-4451-bebf-e1ded3d41dc0']
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
    with step('[Action] close_sparkle_intro'):
        actions.find_element(AppiumBy.NAME, 'Tap to apply sparkle style.')
        actions.tap_by_coordinates(220, 220)
        actions.find_element(AppiumBy.NAME, 'Tap to apply sparkle style.')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Manual add')):
        assert False, 'tap sparkle_manual failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sparkle"`]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]')
    from_pos = (34, 110)
    destination = (380, 620)
    mode = 1
    with step('[Verify] snapshot: 05_17_02_before_add.png'):
        actions.capture_for_gt('05_17_02_before_add.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(34, 110, 380, 620)
    with step('[Verify] snapshot: 05_17_02_after_add.png'):
        actions.capture_for_gt('05_17_02_after_add.png')
    if (not actions.compare_with_gt('05_17_02_after_add.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare manual add sparkle failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('98', '99', '100'))):
        pass
    else:
        assert False, 'adjust speed failed in test_05_17_02_2'
    if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'label == "photo animation btn pause n"'):
        pass
    else:
        assert False, 'verify playback failed in test_05_17_02_2'
    with step('[Action] tap_wraparound_pause'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sparkle"`]/XCUIElementTypeOther[2]/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]')):
        assert False, 'tap sparkle_template1_1 failed in test_05_17_02_2'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('98', '99', '100'))):
        pass
    else:
        assert False, 'adjust intensity failed in test_05_17_02_2'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')):
        assert False, 'tap bokeh_color failed in test_05_17_02_2'
    else:
        if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel') in ('179', '180'))):
            pass
        else:
            assert False, 'adjust hue failed in test_05_17_02_2'
        if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel') in ('99', '100'))):
            pass
        else:
            assert False, 'adjust saturation failed in test_05_17_02_2'
    with step("[Verify] test_00135 completion"):
        assert True
