import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_glow_up")
def test_test_ai_glow_up(actions: DriverActions):
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap ScrollableMenuViewCell-Portrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step("[Action] Tap AI Glow Up"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Glow Up')
    with step("[Action] Tap AI Glow Up"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Glow Up')
    with step("[Verify] Glow up your portraits in one tap! is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Glow up your portraits in one tap!'), 'element Glow up your portraits in one tap! should be visible'
    with step("[Action] Tap Try First"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step("[Verify] The face in the chosen photo is either too small or blurry. This may result in a poor face swap or unexpected defects in the photo. We recommended using a larger photo where the face is clearer. is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'The face in the chosen photo is either too small or blurry. This may result in a poor face swap or unexpected defects in the photo. We recommended using a larger photo where the face is clearer.'), 'element The face in the chosen photo is either too small or blurry. This may result in a poor face swap or unexpected defects in the photo. We recommended using a larger photo where the face is clearer. should not be visible'
    with step("[Verify] The face in this photo is too small or blurry, which may result in poorly generated results. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'The face in this photo is too small or blurry, which may result in poorly generated results.'), 'element The face in this photo is too small or blurry, which may result in poorly generated results. should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Verify] Edit is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Edit'), 'element Edit should be visible'
    with step("[Action] Tap AI Glow Up"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Glow Up')
    with step("[Action] Tap Try First"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step("[Action] Tap Continue Anyway"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway')
    with step("[Action] Tap Natural Cool"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Natural Cool')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] barImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'barImageView'), 'element barImageView should be visible'
    with step("[Verify] barImageView is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'barImageView'), 'element barImageView should not be visible'
    with step("[Action] Tap Natural Warm"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Natural Warm')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] barImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'barImageView'), 'element barImageView should be visible'
    with step("[Verify] barImageView is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'barImageView'), 'element barImageView should not be visible'
    with step("[Action] Tap undoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'undoButton')
    with step("[Action] Tap ic edit undo n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step("[Action] Tap ic_undo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_undo')
    with step("[Action] Tap btnRedo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRedo')
    with step("[Action] Tap redoButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'redoButton')
    with step("[Action] Tap ic_redo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_redo')
    with step("[Action] Tap Intense Cool"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Intense Cool')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Unlock premium features is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Unlock premium features'), 'element Unlock premium features should not be visible'
    with step("[Action] Tap Intense Warm"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Intense Warm')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Unlock premium features is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Unlock premium features'), 'element Unlock premium features should not be visible'
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    assert False, "original pytest run failed — this recording reproduces a failing run"
