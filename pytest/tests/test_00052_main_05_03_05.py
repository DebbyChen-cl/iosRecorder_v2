import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00052_main_05_03_05')
def test_00052_main_05_03_05(actions: DriverActions):
    """dehaze"""
    mode = 1
    uuid = ['e1e22b28-be16-4a89-9271-73638a48d33c', '7586e421-b251-445f-9922-2d00e4df1bea', '2697222b-7edf-43b4-b85e-0201f0146505', '0c8ddaf3-3911-47ae-9a11-6a42e8946ae2', '70744f76-a791-41e1-8be5-b4c2b0dff3ee', '096172fc-54f5-4a22-8892-31e61465d1cf', 'e131e308-1421-46dd-b4c1-cc0517b61ba1', '67ee221a-8acf-408f-8a31-bf65957a2500', 'ee3b9956-084b-4beb-a36c-69e31c3a5f50', '4a7ad28b-d08f-4af2-b892-ec0d699e6d00']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_enhance1_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    from_pos = (380, 770)
    destination = (50, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 50, 770)
    with step('[Verify] snapshot: 05-03-05_before_dehaze.png'):
        actions.capture_for_gt('05-03-05_before_dehaze.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dehaze')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '50'):
        pass
    else:
        assert False, 'default value error'
    with step('[Action] adjust_dehaze_slider'):
        assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'Adjust to min fail'
    with step('[Action] adjust_dehaze_slider'):
        assert actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'Adjust to max fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'Tap x fail'
    with step('[Verify] snapshot: 05-03-05_tap_x.png'):
        actions.capture_for_gt('05-03-05_tap_x.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05-03-05_tap_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Tap x fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dehaze')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap done button fail'
    with step('[Verify] snapshot: 05-03-05_tap_v.png'):
        actions.capture_for_gt('05-03-05_tap_v.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05-03-05_tap_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Tap v fail'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00052 completion"):
        assert True
