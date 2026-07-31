import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00133_main_05_17_03')
def test_00133_main_05_17_03(actions: DriverActions):
    """Live - bokeh"""
    mode = 1
    uuid = ['b16d2e64-5930-4339-8440-5d64f30d3018', '3599830c-1dd2-11b2-8001-080027b246c3', '3599830c-1dd2-11b2-8002-080027b246c3', '3599830c-1dd2-11b2-8003-080027b246c3', '3599830c-1dd2-11b2-8004-080027b246c3', '3599830c-1dd2-11b2-8005-080027b246c3', '3599830c-1dd2-11b2-8006-080027b246c3', '3599830c-1dd2-11b2-8007-080027b246c3', '3599830c-1dd2-11b2-8008-080027b246c3', '3599830c-1dd2-11b2-8009-080027b246c3', '3599830c-1dd2-11b2-800a-080027b246c3', '3599830c-1dd2-11b2-800b-080027b246c3', '3599830c-1dd2-11b2-800c-080027b246c3', '3599830c-1dd2-11b2-800d-080027b246c3', '3599830c-1dd2-11b2-800e-080027b246c3', '3599830c-1dd2-11b2-800f-080027b246c3', '3599830c-1dd2-11b2-8010-080027b246c3', '3599830c-1dd2-11b2-8011-080027b246c3', '3599830c-1dd2-11b2-8012-080027b246c3', '3599830c-1dd2-11b2-8013-080027b246c3', '3599830c-1dd2-11b2-8014-080027b246c3', '3599830c-1dd2-11b2-8015-080027b246c3', '3599830c-1dd2-11b2-8016-080027b246c3', '3599830c-1dd2-11b2-8017-080027b246c3', '3599830c-1dd2-11b2-8018-080027b246c3', '3599830c-1dd2-11b2-8019-080027b246c3', '3599830c-1dd2-11b2-801a-080027b246c3', '3599830c-1dd2-11b2-801b-080027b246c3', '3599830c-1dd2-11b2-801c-080027b246c3', '3599830c-1dd2-11b2-801d-080027b246c3', '17fa9b8c-4b50-4e0d-a0bc-13d319f5f86b', 'b1cb99aa-aeba-42c6-9314-77588d40d5c7', 'f8181a33-cd72-4c75-920b-2cc06ab4e396']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit')
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
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_bokeh_n')
    with step('[Action] tap_bokeh_template'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-SparkleBuildIn_0')
        assert actions.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider')
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('98', '99', '100'))):
        pass
    else:
        assert False, 'adjust speed failed'
    if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'label == "photo animation btn pause n"'):
        pass
    else:
        assert False, 'playback verification failed'
    with step('[Action] tap_wraparound_pause'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    from_pos = (206, 494)
    destination = (206, 550)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 494, 206, 550)
    with step('[Verify] snapshot: 5_17_03_outside_before.png'):
        actions.capture_for_gt('5_17_03_outside_before.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 494, 206, 550)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 494, 206, 550)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Verify] snapshot: 5_17_03_outside.png'):
        actions.capture_for_gt('5_17_03_outside.png')
    if (not actions.compare_with_gt('5_17_03_outside.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust outside compare failed'
    from_pos = (208, 485)
    destination = (208, 510)
    mode = 1
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Verify] snapshot: 5_17_03_inner_before.png'):
        actions.capture_for_gt('5_17_03_inner_before.png')
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(208, 485, 208, 510)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Verify] snapshot: 5_17_03_inner.png'):
        actions.capture_for_gt('5_17_03_inner.png')
    if (not actions.compare_with_gt('5_17_03_inner.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust inner compare failed'
    from_pos = (208, 391)
    destination = (208, 430)
    mode = 1
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Verify] snapshot: 5_17_03_position_before.png'):
        actions.capture_for_gt('5_17_03_position_before.png')
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(208, 391, 208, 430)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Verify] snapshot: 5_17_03_position.png'):
        actions.capture_for_gt('5_17_03_position.png')
    if (not actions.compare_with_gt('5_17_03_position.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust position compare failed'
    with step('[Action] tap_phd_element'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-SparkleBuildIn_0')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Intensity')):
        assert False, 'tap intensity button failed'
    else:
        with step('[Action] adjust_bokeh_speed_slider'):
            actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')
        if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('97', '98', '99', '100'))):
            pass
        else:
            assert False, 'adjust intensity slider failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Amount')):
        assert False, 'tap amount button failed'
    else:
        with step('[Action] adjust_bokeh_speed_slider'):
            actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')
        if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('97', '98', '99', '100'))):
            with step('[Action] adjust_bokeh_speed_slider'):
                actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')
        else:
            assert False, 'adjust amount slider failed'
    with step('[Action] adjust_bokeh_speed_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Color')):
        assert False, 'tap color button failed'
    with step('[Action] adjust_bokeh_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'hueValueLabel') in ('179', '180'))):
        pass
    else:
        assert False, 'adjust hue slider failed'
    with step('[Action] adjust_bokeh_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1') and (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'saturationValueLabel') in ('99', '100'))):
        pass
    else:
        assert False, 'adjust saturation slider failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blur type')):
        assert False, 'enter blur type failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "bokeh"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') == '70'):
        pass
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Linear')):
        assert False, 'enter linear blur type failed'
    else:
        if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "bokeh"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') == '70'):
            pass
        if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch')):
            assert False, 'enter brush blur type failed'
        else:
            with step('[Action] tap_phd_btn'):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch')
            if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "bokeh"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') == '70'):
                pass
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Circular')
        with step('[Action] adjust_bokeh_circular_slider'):
            actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "bokeh"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('0', '1'))):
            pass
        else:
            assert False, 'circular min value failed'
        if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "bokeh"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('99', '100'))):
            pass
        else:
            assert False, 'circular max value failed'
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Linear')
        with step('[Action] adjust_bokeh_linear_slider'):
            actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "bokeh"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('0', '1'))):
            pass
        else:
            assert False, 'linear min value failed'
        if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "bokeh"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('99', '100'))):
            pass
        else:
            assert False, 'linear max value failed'
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch')
        with step('[Action] adjust_bokeh_brush_slider'):
            actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "bokeh"`]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('8', '9'))):
            pass
        else:
            assert False, 'brush min value failed'
        if (actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "bokeh"`]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText') in ('99', '100'))):
            pass
        else:
            assert False, 'brush max value failed'
        with step('[Verify] snapshot: 5_17_03_before_brush.png'):
            actions.capture_for_gt('5_17_03_before_brush.png')
        from_pos = (75, 270)
        destination = (350, 500)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(75, 270, 350, 500)
        with step('[Verify] snapshot: 5_17_03_after_brush.png'):
            actions.capture_for_gt('5_17_03_after_brush.png')
        if (not actions.compare_with_gt('5_17_03_after_brush.png', gt_folder=TD.GT_FOLDER)[0]):
            pass
        else:
            assert False, 'brush compare failed'
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnErase')
        from_pos = (75, 270)
        destination = (350, 500)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(75, 270, 350, 500)
        with step('[Verify] snapshot: 5_17_03_after_erase.png'):
            actions.capture_for_gt('5_17_03_after_erase.png')
        if (not actions.compare_with_gt('5_17_03_after_erase.png', gt_folder=TD.GT_FOLDER)[0]):
            pass
        else:
            assert False, 'erase compare failed'
        with step('[Action] tap_phd_btn'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Circular')
        from_pos = (208, 430)
        destination = (208, 391)
        mode = 1
        with step('[Action] tap'):
            actions.tap_by_coordinates(220, 220)
        with step('[Verify] snapshot: 5_17_03_blur_position_before.png'):
            actions.capture_for_gt('5_17_03_blur_position_before.png')
        with step('[Action] tap'):
            actions.tap_by_coordinates(220, 220)
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(208, 430, 208, 391)
        with step('[Action] tap'):
            actions.tap_by_coordinates(220, 220)
        with step('[Verify] snapshot: 5_17_03_blur_position.png'):
            actions.capture_for_gt('5_17_03_blur_position.png')
        if (not actions.compare_with_gt('5_17_03_blur_position.png', gt_folder=TD.GT_FOLDER)[0]):
            pass
        else:
            assert False, 'blur position compare failed'
        from_pos = (208, 510)
        destination = (208, 485)
        mode = 1
        with step('[Action] tap'):
            actions.tap_by_coordinates(220, 220)
        with step('[Verify] snapshot: 5_17_03_blur_inner_before.png'):
            actions.capture_for_gt('5_17_03_blur_inner_before.png')
        with step('[Action] tap'):
            actions.tap_by_coordinates(220, 220)
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(208, 510, 208, 485)
        with step('[Action] tap'):
            actions.tap_by_coordinates(220, 220)
        with step('[Verify] snapshot: 5_17_03_blur_inner.png'):
            actions.capture_for_gt('5_17_03_blur_inner.png')
        if (not actions.compare_with_gt('5_17_03_blur_inner.png', gt_folder=TD.GT_FOLDER)[0]):
            pass
        else:
            assert False, 'blur inner compare failed'
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Circular')
        from_pos = (208, 550)
        destination = (310, 494)
        mode = 1
        with step('[Action] tap'):
            actions.tap_by_coordinates(220, 220)
        with step('[Verify] snapshot: 5_17_03_blur_rotate_before.png'):
            actions.capture_for_gt('5_17_03_blur_rotate_before.png')
        with step('[Action] tap'):
            actions.tap_by_coordinates(220, 220)
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(208, 550, 310, 494)
        with step('[Action] tap'):
            actions.tap_by_coordinates(220, 220)
        with step('[Verify] snapshot: 5_17_03_blur_rotate.png'):
            actions.capture_for_gt('5_17_03_blur_rotate.png')
        if (not actions.compare_with_gt('5_17_03_blur_rotate.png', gt_folder=TD.GT_FOLDER)[0]):
            pass
        else:
            assert False, 'rotate/outline compare failed'
    with step("[Verify] test_00133 completion"):
        assert True
