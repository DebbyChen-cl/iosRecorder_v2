import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00045_main_05_04a_05')
def test_00045_main_05_04a_05(actions: DriverActions):
    """mirror"""
    mode = 1
    uuid = ['2b96b76b-283d-4bd6-bc3d-9ac66addccb0', '4a71dc4e-ea2a-4b84-8d93-93cbcad57dfd', '47fb9216-6972-4d40-b544-b219b736c0f8', '5f12c9c2-e650-4eb7-a8c1-4946145ef65f', 'ffa9908d-d2a4-49c2-b3a5-46bd688e4714', 'cb7a956c-aff3-4534-a67e-019b076cfffc', '3ee32229-d56c-4a3b-bbb2-6ccf1fcc32c0', '654a6900-c594-4121-88a5-d998e2b9a6f0', '55e9d90c-736c-4e59-ac40-75111b432f67']
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
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Verify] snapshot: 05_04a_05_before_mirror.png'):
        actions.capture_for_gt('05_04a_05_before_mirror.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')):
        assert False  # legacy raise
    from_pos = (380, 770)
    destination = (50, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 50, 770)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mirror')):
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[6]')
    with step('[Verify] snapshot: base05_04a_05_mirror5.png'):
        actions.capture_for_gt('base05_04a_05_mirror5.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn mirrorfilter n')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[1]')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_05_topleft.png'):
        actions.capture_for_gt('base05_04a_05_topleft.png', crop_rect=(0, 60, 276, 526))
    with step('[Verify] snapshot: base05_04a_05_effect_v.png'):
        actions.capture_for_gt('base05_04a_05_effect_v.png', crop_rect=(0, 60, 276, 526))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_05_effect_x.png'):
        actions.capture_for_gt('base05_04a_05_effect_x.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn mirrorfilter n')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[3]')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_05_topright.png'):
        actions.capture_for_gt('base05_04a_05_topright.png', crop_rect=(0, 60, 276, 526))
    with step('[Verify] snapshot: base05_04a_05_bottomright.png'):
        actions.capture_for_gt('base05_04a_05_bottomright.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn mirrorfilter n')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[4]')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_05_bottomleft.png'):
        actions.capture_for_gt('base05_04a_05_bottomleft.png', crop_rect=(0, 60, 276, 526))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn mirrorfilter n')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[5]')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_05_effect_v_final.png'):
        actions.capture_for_gt('base05_04a_05_effect_v_final.png', crop_rect=(0, 60, 276, 526))
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_04a_05_mirror_x.png'):
        actions.capture_for_gt('05_04a_05_mirror_x.png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_04a_05_mirror_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00045 completion"):
        assert True
