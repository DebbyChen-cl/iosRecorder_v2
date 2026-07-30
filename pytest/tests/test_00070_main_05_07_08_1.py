import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00070_main_05_07_08_1')
def test_00070_main_05_07_08_1(actions: DriverActions):
    """nose enhance, have face"""
    uuid = ['889f4be9-e7f1-407c-8e5d-37567c559381', 'c1931400-359e-48cb-aa59-53b2f26c6170', '6b5c7775-d77f-4d7a-82c2-42da0ad1b5c2', '65f27d51-95f2-4fc1-bbbd-cd1fdc54ace1', '4a51e087-7e37-4cc9-9a5f-e5e31212b236', 'c81fee0d-3e2b-4169-98d2-8040c6b79ba9', '2c87fb9c-3573-416d-a46f-99f33f890e5c', '9b050ec4-ed11-4533-a8f4-a455a97dfc90', 'eae62203-9558-48b9-b786-802057120fa2', '9fd92b26-9c5c-4198-955d-f094d44f17d6']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Verify] snapshot: 05_07_08_before_nose.png'):
        actions.capture_for_gt('05_07_08_before_nose.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Nose Enhance')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[-2]') == '50'):
        pass
    else:
        assert False, 'Default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    get_face_value = actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False
    with step('[Verify] snapshot: 05_07_08_slider_min.png'):
        actions.capture_for_gt('05_07_08_slider_min.png')
    if actions.compare_with_gt('05_07_08_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider left fail'
    with step('[Action] tap_image'):
        assert actions.tap_by_coordinates(250, 400)
    with step('[Verify] snapshot: 05_07_08_undo_og.png'):
        actions.capture_for_gt('05_07_08_undo_og.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    get_face_value = actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel')
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False
    with step('[Verify] snapshot: 05_07_08_slider_max.png'):
        actions.capture_for_gt('05_07_08_slider_max.png')
    if actions.compare_with_gt('05_07_08_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Slider right fail'
    with step('[Action] tap_image'):
        assert actions.tap_by_coordinates(250, 400)
    with step('[Verify] snapshot: 05_07_08_before_undo.png'):
        actions.capture_for_gt('05_07_08_before_undo.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_08_undo.png'):
        actions.capture_for_gt('05_07_08_undo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_08_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_08_redo.png'):
        actions.capture_for_gt('05_07_08_redo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_08_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap [v] fail'
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, '[v] fail'
    with step("[Verify] test_00070 completion"):
        assert True
