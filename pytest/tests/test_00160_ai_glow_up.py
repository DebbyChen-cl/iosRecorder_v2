import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00160_ai_glow_up')
def test_00160_ai_glow_up(actions: DriverActions):
    """AI glow up"""
    uuid = ['5f9de67c-8ef2-40b0-a9d8-8d2267188861', '3a615761-3449-4183-8aad-760727f2e6ca', 'cf6e1619-6138-4f44-9c6a-a1ebd29070c6', '2abc3706-e519-4ecf-9968-4a5fa2b4d1cf', '7e76a806-ba4d-4709-b6f6-8fcdd41e068a', '375d4b78-2f73-4dbb-86ce-74cab3d7df93', '4bddbca1-2090-444c-8c2f-218c069ff95a', 'abb79a3f-5e58-48ba-8ecc-8a4259eb7c66', 'c19d90b5-c9e5-450a-b173-13cba1b84893', 'c538a24c-5fdd-4b81-b599-67c757ffd94f', 'c10f421c-0349-4034-97a8-009e7fa73b2f', '7e3368b0-b0ec-46b2-97b9-6c7a407a2109', '8a219c87-b753-4e0d-9973-adacd231a8d9', 'a0911329-9bee-4030-8207-4f106e049d19']
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
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Glow Up')
    assert actions.is_element_present(AppiumBy.NAME, 'Glow up your portraits in one tap!')
    with step('[Action] tap_tryout'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    assert actions.is_element_present(AppiumBy.NAME, 'The face in the chosen photo is either too small or blurry. This may result in a poor face swap or unexpected defects in the photo.')
    with step('[Action] tap_ok2_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Continue')
    assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Glow Up')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway')
    with step('[Verify] snapshot: G02_02_08_no_style.png'):
        actions.capture_for_gt('G02_02_08_no_style.png')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Natural Cool')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    actions.capture_for_gt('G02_02_08_natural_cool.png')
    if (not actions.compare_with_gt('G02_02_08_natural_cool.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, '[G02_02_08] Compare fail for natural_cool'
    assert actions.tap_by_locator(AppiumBy.NAME, 'Natural Warm')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    actions.capture_for_gt('G02_02_08_natural_warm.png')
    if (not actions.compare_with_gt('G02_02_08_natural_warm.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, '[G02_02_08] Compare fail for natural_warm'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnUndo')
    actions.capture_for_gt('G02_02_08_undo.png')
    if actions.compare_with_gt('G02_02_08_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[G02_02_08] Compare fail for undo'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRedo')
    actions.capture_for_gt('G02_02_08_redo.png')
    if actions.compare_with_gt('G02_02_08_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[G02_02_08] Compare fail for redo'
    assert actions.tap_by_locator(AppiumBy.NAME, 'Intense Cool')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    assert actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1) or actions.is_element_present(AppiumBy.NAME, 'Unlock premium features', timeout=1)
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    assert actions.tap_by_locator(AppiumBy.NAME, 'Intense Warm')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    assert actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1) or actions.is_element_present(AppiumBy.NAME, 'Unlock premium features', timeout=1)
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    actions.capture_for_gt('G02_02_08_x.png')
    if actions.compare_with_gt('G02_02_08_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[G02_02_08] Compare fail for x'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Glow Up')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.NAME, 'Natural Warm')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    actions.capture_for_gt('G02_02_08_v.png')
    if actions.compare_with_gt('G02_02_08_v.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[G02_02_08] Compare fail for v'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Glow Up')
    assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblDesc')
    with step("[Verify] test_00160 completion"):
        assert True
