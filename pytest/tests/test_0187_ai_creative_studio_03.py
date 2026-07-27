import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_creative_studio_03")
def test_test_ai_creative_studio_03(actions: DriverActions):
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Verify] AI Creative Studio is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio'), 'element AI Creative Studio should be visible'
    with step("[Action] Tap AI Creative Studio"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
    with step("[Verify] notShowAgainCheckBox is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox'), 'element notShowAgainCheckBox should not be visible'
    with step("[Verify] Collage is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Collage'), 'element Collage should be visible'
    with step("[Action] Tap Portrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Portrait')
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Action] Tap addIconView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addIconView')
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step("[Action] Tap photoCell-4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step("[Action] Tap photoCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] Long press to adjust order is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Long press to adjust order'), 'element Long press to adjust order should not be visible'
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Action] Tap I Agree"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap aiCreativeStudioRouter_backButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton')
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Action] Tap addIconView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addIconView')
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step("[Action] Tap photoCell-4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step("[Action] Tap photoCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Action] Tap I Agree"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
    with step("[Verify] AI Creative Studio is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio'), 'element AI Creative Studio should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should not be visible'
    with step("[Verify] activityIndicator is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should not be visible'
    with step("[Verify] selectCheckBoxOverlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'selectCheckBoxOverlay'), 'element selectCheckBoxOverlay should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap aiCreativeStudioRouter_backButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton')
    with step("[Action] Tap Creative"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Creative')
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Action] Tap addIconView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addIconView')
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step("[Action] Tap photoCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Action] Tap I Agree"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap aiCreativeStudioRouter_backButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton')
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Action] Tap addIconView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addIconView')
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step("[Action] Tap photoCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should not be visible'
    with step("[Verify] activityIndicator is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should not be visible'
    with step("[Verify] selectCheckBoxOverlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'selectCheckBoxOverlay'), 'element selectCheckBoxOverlay should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap aiCreativeStudioRouter_homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_homeButton')
    with step("[Verify] AI Photos is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AI Photos'), 'element AI Photos should be visible'
    assert True
