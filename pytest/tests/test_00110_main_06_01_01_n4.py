import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00110_main_06_01_01_n4')
def test_00110_main_06_01_01_n4(actions: DriverActions):
    """Text bubble - new - bubble style"""
    mode = 1
    uuid = ['3615ab50-298f-4a9b-bc55-ead20a930127', '7643c6ef-75db-4f44-88bc-d6208cf2eaae', 'ba88260c-3295-4280-8bcd-ee50211ad9e3', 'd10c4057-a7da-437c-a5b9-237aa4cb3105', 'd1c9ed28-9643-4edb-af74-a5f5ea6c9151', '99b4cd63-3823-4e7d-9843-3f5400320cd0', 'a45e71ac-8d0e-40ff-a8ca-c6403086561f', '8bfea3e3-86fb-4406-b8ae-0e031dd294fa', '901a159d-dba6-41f1-9399-67342e3c9ee4', '775ca12e-5cfb-47c2-8aa2-9183ea61c63b', 'dbf7951f-5ffb-4642-ade8-60f2e476d3f7']
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
    with step('[Action] tap_edit1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    from_pos = (380, 770)
    destination = (50, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text Bubble')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Bubble')
    with step('[Verify] snapshot: 06_01_01_bubble_default.png'):
        actions.capture_for_gt('06_01_01_bubble_default.png')
    if actions.compare_with_gt('06_01_01_bubble_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'default bubble panel 0 fail'
    with step('[Verify] snapshot: 06_01_01_bubble_default_size.png'):
        actions.capture_for_gt('06_01_01_bubble_default_size.png')
    from_pos = (215, 500)
    destination = (215, 100)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(215, 500, 215, 100)
    with step('[Verify] snapshot: 06_01_01_bubble_extend.png'):
        actions.capture_for_gt('06_01_01_bubble_extend.png')
    if not actions.compare_with_gt('06_01_01_bubble_extend.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'extended panel fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 06_01_01_no_bubble_panel.png'):
        actions.capture_for_gt('06_01_01_no_bubble_panel.png')
    if actions.compare_with_gt('06_01_01_no_bubble_panel.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'no bubble panel 0 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Bubble')
    with step('[Verify] snapshot: 06_01_01_bubble_shadow_off.png'):
        actions.capture_for_gt('06_01_01_bubble_shadow_off.png', crop_rect=(0, 60, 276, 400))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Toggle off withoutText')
    with step('[Verify] snapshot: 06_01_01_bubble_shadow_on.png'):
        actions.capture_for_gt('06_01_01_bubble_shadow_on.png', crop_rect=(0, 60, 276, 400))
    if (not actions.compare_with_gt('06_01_01_bubble_shadow_on.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'shadow on fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Toggle on withoutText')
    with step('[Verify] snapshot: 06_01_01_bubble_shadow_on_to_off.png'):
        actions.capture_for_gt('06_01_01_bubble_shadow_on_to_off.png', crop_rect=(0, 60, 276, 400))
    if actions.compare_with_gt('06_01_01_bubble_shadow_on_to_off.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'shadow off fail'
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 06_01_01_bubble_opacity_min.png'):
        actions.capture_for_gt('06_01_01_bubble_opacity_min.png')
    if actions.compare_with_gt('06_01_01_bubble_opacity_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity min 0 fail'
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_color_solid_opacity_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 06_01_01_bubble_opacity_max.png'):
        actions.capture_for_gt('06_01_01_bubble_opacity_max.png')
    if actions.compare_with_gt('06_01_01_bubble_opacity_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'opacity max 0 fail'
    with step('[Verify] snapshot: 06_01_01_bubble_og.png'):
        actions.capture_for_gt('06_01_01_bubble_og.png', crop_rect=(0, 60, 276, 400))
    with step('[Action] select_bubble_style_1'):
        actions.tap_by_coordinates(70, 700)
    with step('[Verify] snapshot: 06_01_01_bubble_style1.png'):
        actions.capture_for_gt('06_01_01_bubble_style1.png', crop_rect=(0, 60, 276, 400))
    if (not actions.compare_with_gt('06_01_01_bubble_style1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'style 1 fail'
    with step('[Action] select_bubble_style_2'):
        actions.tap_by_coordinates(200, 700)
    with step('[Verify] snapshot: 06_01_01_bubble_style2.png'):
        actions.capture_for_gt('06_01_01_bubble_style2.png', crop_rect=(0, 60, 276, 400))
    if (not actions.compare_with_gt('06_01_01_bubble_style2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'style 2 fail'
    with step('[Action] select_bubble_style_3'):
        actions.tap_by_coordinates(340, 700)
    with step('[Verify] snapshot: 06_01_01_bubble_style3.png'):
        actions.capture_for_gt('06_01_01_bubble_style3.png', crop_rect=(0, 60, 276, 400))
    if (not actions.compare_with_gt('06_01_01_bubble_style3.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'style 3 fail'
    with step('[Verify] snapshot: 06_01_01_before_close_style_drag.png'):
        actions.capture_for_gt('06_01_01_before_close_style_drag.png')
    from_pos = (206, 504)
    destination = (206, 830)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 504, 206, 830)
    with step('[Verify] snapshot: 06_01_01_after_close_style_drag.png'):
        actions.capture_for_gt('06_01_01_after_close_style_drag.png')
    if not actions.compare_with_gt('06_01_01_after_close_style_drag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'drag down close panel fail'
    with step("[Verify] test_00110 completion"):
        assert True
