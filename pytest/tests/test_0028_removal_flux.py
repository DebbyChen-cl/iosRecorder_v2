import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_removal_flux")
def test_test_removal_flux(actions: DriverActions):
    with step("[Verify] btnIAP is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should be visible'
    with step("[Action] Tap btnIAP"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Verify] Would you like to continue editing? is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Would you like to continue editing?'), 'element Would you like to continue editing? should not be visible'
    with step("[Verify] closeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'closeButton'), 'element closeButton should not be visible'
    with step("[Verify] navCloseButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton'), 'element navCloseButton should not be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Unlock premium features is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Unlock premium features'), 'element Unlock premium features should not be visible'
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
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap AI Removal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')
    with step("[Verify] Remove with faster selection tool is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Remove with faster selection tool'), 'element Remove with faster selection tool should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Verify] Remove with faster selection tool is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Remove with faster selection tool'), 'element Remove with faster selection tool should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Verify] Try First is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Try First'), 'element Try First should be visible'
    with step("[Action] Tap Try First"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step("[Verify] Try First is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Try First'), 'element Try First should not be visible'
    with step("[Action] Tap proPlusToggle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'proPlusToggle')
    with step("[Verify] Generative AI Removal is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Generative AI Removal'), 'element Generative AI Removal should be visible'
    with step("[Action] Tap Upgrade to Pro+ Premium"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Upgrade to Pro+ Premium')
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
    with step("[Action] Tap settingButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'settingButton')
    with step("[Verify] Setting is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Setting'), 'element Setting should not be visible'
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap About"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'About')
    with step("[Verify] developerButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'developerButton'), 'element developerButton should be visible'
    with step("[Verify] Develop Info is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Develop Info'), 'element Develop Info should be visible'
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Action] Tap Free"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Free')
    with step("[Action] Tap Pro"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pro')
    with step("[Action] Tap chevron.left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap AI Removal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Try First is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Try First'), 'element Try First should not be visible'
    with step("[Action] Tap proPlusToggle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'proPlusToggle')
    with step("[Verify] Generative AI Removal is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Generative AI Removal'), 'element Generative AI Removal should be visible'
    with step("[Action] Tap Upgrade to Pro+ Premium"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Upgrade to Pro+ Premium')
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
    with step("[Action] Tap settingButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'settingButton')
    with step("[Verify] Setting is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Setting'), 'element Setting should not be visible'
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap About"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'About')
    with step("[Verify] developerButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'developerButton'), 'element developerButton should be visible'
    with step("[Verify] Develop Info is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Develop Info'), 'element Develop Info should be visible'
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Action] Tap Pro"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pro')
    with step("[Action] Tap Pro+"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pro+')
    with step("[Action] Tap chevron.left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap AI Removal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Removal')
    with step("[Verify] proPlusToggle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'proPlusToggle'), 'element proPlusToggle should be visible'
    with step("[Action] Tap Manual"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Manual')
    with step("[Action] Tap applyButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'applyButton')
    with step("[Verify] magicText is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'magicText'), 'element magicText should not be visible'
    assert True
