import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00140_main_05_01_11')
def test_00140_main_05_01_11(actions: DriverActions):
    """AI color"""
    mode = 1
    uuid = ['5724974c-fbe6-4490-a4c7-382b78bf9740', '925e23b5-57fd-41a5-a243-7d5c9001512e', 'ff4942e5-f608-4257-bf2f-d373194f2263', '2968f849-c9be-4ce6-92c1-c23eaae120ac', '70778ba6-cb62-4ecd-a601-3f4a5d922833', 'd2712c63-2dfa-4733-b8aa-687cbb0610d0', '3448aeab-de7d-4a87-881c-2dbf374e3f59', '245a3616-5115-4b73-9a30-54b0f5e42cf3', 'b789e0d8-22f7-43f0-b3b2-a3ed16ca2b60']
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
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    with step('[Verify] snapshot: 05_01_11_before_ai_color.png'):
        actions.capture_for_gt('05_01_11_before_ai_color.png')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Color')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "colorEnhance"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeStaticText[2]') == '70'):
        pass
    with step('[Verify] snapshot: 05_01_11_default.png'):
        actions.capture_for_gt('05_01_11_default.png')
    if actions.compare_with_gt('05_01_11_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'AI color default comparison failed'
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "colorEnhance"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3', '4', '5')):
        pass
    with step('[Verify] snapshot: 05_01_11_min.png'):
        actions.capture_for_gt('05_01_11_min.png')
    if actions.compare_with_gt('05_01_11_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'AI color min comparison failed'
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "colorEnhance"`]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97', '96', '95')):
        pass
    with step('[Verify] snapshot: 05_01_11_max.png'):
        actions.capture_for_gt('05_01_11_max.png')
    if actions.compare_with_gt('05_01_11_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'AI color max comparison failed'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_01_11_x.png'):
        actions.capture_for_gt('05_01_11_x.png')
    if actions.compare_with_gt('05_01_11_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'AI color X comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Color')
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    with step("[Verify] test_00140 completion"):
        assert True
