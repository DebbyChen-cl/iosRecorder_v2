import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00144_main_05_01_12_5')
def test_00144_main_05_01_12_5(actions: DriverActions):
    """quick action - retouch"""
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step('[Action] verify_settings_page'):
        assert (
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Setting')
            or actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
        )
    enter_about_page_success = False
    for attempt in range(3):
        with step('[Action] enter_about_page'):
            if actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'About') and actions.is_element_present(
                AppiumBy.ACCESSIBILITY_ID, 'developerButton'
            ):
                enter_about_page_success = True
                break
    if not enter_about_page_success:
        assert False, 'Enter about page fail after 3 retries'
    with step('[Action] enable_plan_from_settings'):
        assert actions.is_element_present(AppiumBy.NAME, 'Develop Info')
        assert actions.find_element(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="1"])[2]')
        actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[6]')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle')
    with step('[Verify] snapshot: 05_01_12_before_quick_retouch.png'):
        actions.capture_for_gt('05_01_12_before_quick_retouch.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    if actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') != '30':
        assert False, 'Smooth default value is not 30'
    with step('[Verify] snapshot: 05_01_12_smooth_default.png'):
        actions.capture_for_gt('05_01_12_smooth_default.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_smooth_default.png'):
        assert actions.compare_with_gt('05_01_12_smooth_default.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') not in ('0', '1', '2', '3'):
        assert False, 'Smooth min value error'
    with step('[Verify] snapshot: 05_01_12_smooth_min.png'):
        actions.capture_for_gt('05_01_12_smooth_min.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_smooth_min.png'):
        assert actions.compare_with_gt('05_01_12_smooth_min.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') not in ('100', '99', '98', '97'):
        assert False, 'Smooth max value error'
    with step('[Verify] snapshot: 05_01_12_bg_smooth_max.png'):
        actions.capture_for_gt('05_01_12_bg_smooth_max.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_bg_smooth_max.png'):
        assert actions.compare_with_gt('05_01_12_bg_smooth_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] reset_quick_intensity_value'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step('[Verify] snapshot: 05_01_12_bg_smooth_reset.png'):
        actions.capture_for_gt('05_01_12_bg_smooth_reset.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_bg_smooth_reset.png'):
        assert actions.compare_with_gt('05_01_12_bg_smooth_reset.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_01_12_smooth_v.png'):
        actions.capture_for_gt('05_01_12_smooth_v.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_01_12_smooth_v.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, '[v] fail'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Conceal')
    if actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') != '50':
        assert False, 'Conceal default value is not 50'
    with step('[Verify] snapshot: 05_01_12_conceal_default.png'):
        actions.capture_for_gt('05_01_12_conceal_default.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_conceal_default.png'):
        assert actions.compare_with_gt('05_01_12_conceal_default.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') not in ('0', '1', '2', '3'):
        assert False, 'Conceal min value error'
    with step('[Verify] snapshot: 05_01_12_conceal_min.png'):
        actions.capture_for_gt('05_01_12_conceal_min.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_conceal_min.png'):
        assert actions.compare_with_gt('05_01_12_conceal_min.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') not in ('100', '99', '98', '97'):
        assert False, 'Conceal max value error'
    with step('[Verify] snapshot: 05_01_12_bg_conceal_max.png'):
        actions.capture_for_gt('05_01_12_bg_conceal_max.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_bg_conceal_max.png'):
        assert actions.compare_with_gt('05_01_12_bg_conceal_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] reset_quick_intensity_value'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step('[Verify] snapshot: 05_01_12_bg_conceal_reset.png'):
        actions.capture_for_gt('05_01_12_bg_conceal_reset.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_bg_conceal_reset.png'):
        assert actions.compare_with_gt('05_01_12_bg_conceal_reset.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_01_12_retouch_x.png'):
        actions.capture_for_gt('05_01_12_retouch_x.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_retouch_x.png'):
        assert actions.compare_with_gt('05_01_12_retouch_x.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Bags')
    if actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') != '25':
        assert False, 'Eye bags default value is not 50'
    with step('[Verify] snapshot: 05_01_12_eyebag_default.png'):
        actions.capture_for_gt('05_01_12_eyebag_default.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_eyebag_default.png'):
        assert actions.compare_with_gt('05_01_12_eyebag_default.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') not in ('0', '1', '2', '3'):
        assert False, 'Eye bags min value error'
    with step('[Verify] snapshot: 05_01_12_eyebag_min.png'):
        actions.capture_for_gt('05_01_12_eyebag_min.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_eyebag_min.png'):
        assert actions.compare_with_gt('05_01_12_eyebag_min.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') not in ('100', '99', '98', '97'):
        assert False, 'Eye bags max value error'
    with step('[Verify] snapshot: 05_01_12_bg_eyebag_max.png'):
        actions.capture_for_gt('05_01_12_bg_eyebag_max.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_bg_eyebag_max.png'):
        assert actions.compare_with_gt('05_01_12_bg_eyebag_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] reset_quick_intensity_value'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step('[Verify] snapshot: 05_01_12_bg_eyebag_reset.png'):
        actions.capture_for_gt('05_01_12_bg_eyebag_reset.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_bg_eyebag_reset.png'):
        assert actions.compare_with_gt('05_01_12_bg_eyebag_reset.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Teeth Whiten')
    if actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') != '50':
        assert False, 'Teeth whiten default value is not 50'
    with step('[Verify] snapshot: 05_01_12_teeth_default.png'):
        actions.capture_for_gt('05_01_12_teeth_default.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_teeth_default.png'):
        assert actions.compare_with_gt('05_01_12_teeth_default.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') not in ('0', '1', '2', '3'):
        assert False, 'Teeth whiten min value error'
    with step('[Verify] snapshot: 05_01_12_teeth_min.png'):
        actions.capture_for_gt('05_01_12_teeth_min.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_teeth_min.png'):
        assert actions.compare_with_gt('05_01_12_teeth_min.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Verify] snapshot: 05_01_12_retouch_undo_og.png'):
        actions.capture_for_gt('05_01_12_retouch_undo_og.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') not in ('100', '99', '98', '97'):
        assert False, 'Teeth whiten max value error'
    with step('[Verify] snapshot: 05_01_12_bg_teeth_max.png'):
        actions.capture_for_gt('05_01_12_bg_teeth_max.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_bg_teeth_max.png'):
        assert actions.compare_with_gt('05_01_12_bg_teeth_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] reset_quick_intensity_value'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step('[Verify] snapshot: 05_01_12_bg_conceal_reset.png'):
        actions.capture_for_gt('05_01_12_bg_conceal_reset.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_bg_conceal_reset.png'):
        assert actions.compare_with_gt('05_01_12_bg_conceal_reset.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Verify] snapshot: 05_01_12_retouch_redo_og.png'):
        actions.capture_for_gt('05_01_12_retouch_redo_og.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_undo_btn_2'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step('[Verify] snapshot: 05_01_12_retouch_undo.png'):
        actions.capture_for_gt('05_01_12_retouch_undo.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_retouch_undo.png'):
        assert actions.compare_with_gt('05_01_12_retouch_undo.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_redo_btn_2'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n')
    with step('[Verify] snapshot: 05_01_12_retouch_redo.png'):
        actions.capture_for_gt('05_01_12_retouch_redo.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_retouch_redo.png'):
        assert actions.compare_with_gt('05_01_12_retouch_redo.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic reset n')
    with step('[Verify] snapshot: 05_01_12_retouch_reset.png'):
        actions.capture_for_gt('05_01_12_retouch_reset.png', crop_rect=(0, 60, 276, 429))
    with step('[Verify] compare: 05_01_12_retouch_reset.png'):
        assert actions.compare_with_gt('05_01_12_retouch_reset.png', gt_folder=TD.GT_FOLDER)[0]
    with step("[Verify] test_00144 completion"):
        assert True
