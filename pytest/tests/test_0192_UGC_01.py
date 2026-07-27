import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_UGC_01")
def test_test_UGC_01(actions: DriverActions):
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Verify] promptsTextView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'promptsTextView'), 'element promptsTextView should be visible'
    with step("[Action] Tap promptsCollapseIndicatorImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptsCollapseIndicatorImageView')
    with step("[Action] Tap promptsCollapseIndicatorImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptsCollapseIndicatorImageView')
    with step("[Verify] promptsCollapseIndicatorImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'promptsCollapseIndicatorImageView'), 'element promptsCollapseIndicatorImageView should be visible'
    with step("[Action] Tap Use This Template"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use This Template')
    with step("[Verify] lblTitle is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should not be visible'
    with step("[Verify] Custom is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Custom'), 'element Custom should be visible'
    with step("[Verify] textView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'textView'), 'element textView should be visible'
    with step("[Action] Tap aiCreativeStudioRouter_backButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton')
    with step("[Action] Tap navBackButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navBackButton')
    with step("[Verify] navBackButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'navBackButton'), 'element navBackButton should not be visible'
    with step("[Verify] //*[@name=\"navBackButton\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="navBackButton"]'), 'element //*[@name="navBackButton"] should not be visible'
    with step("[Verify] //*[@label=\"navBackButton\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="navBackButton"]'), 'element //*[@label="navBackButton"] should not be visible'
    with step("[Verify] //*[@value=\"navBackButton\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="navBackButton"]'), 'element //*[@value="navBackButton"] should not be visible'
    with step("[Verify] Discover is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Discover'), 'element Discover should be visible'
    with step("[Verify] videoPlayerView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'videoPlayerView'), 'element videoPlayerView should be visible'
    with step("[Verify] lblTime is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTime'), 'element lblTime should be visible'
    with step("[Action] Tap videoPlayerView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'videoPlayerView')
    with step("[Verify] playIconImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'playIconImageView'), 'element playIconImageView should be visible'
    with step("[Action] Tap videoPlayerView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'videoPlayerView')
    with step("[Verify] playIconImageView is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'playIconImageView'), 'element playIconImageView should not be visible'
    with step("[Action] Tap Use This Template"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use This Template')
    with step("[Verify] AIFeatureDemoViewController is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'AIFeatureDemoViewController'), 'element AIFeatureDemoViewController should not be visible'
    with step("[Verify] btnImportReference is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference'), 'element btnImportReference should be visible'
    with step("[Verify] btnMuteToggle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnMuteToggle'), 'element btnMuteToggle should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap Discover"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discover')
    with step("[Verify] Discover is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Discover'), 'element Discover should be visible'
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Verify] DiscoverDetailTryOnRefImageCell-0 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'DiscoverDetailTryOnRefImageCell-0'), 'element DiscoverDetailTryOnRefImageCell-0 should be visible'
    with step("[Action] Tap Use This Template"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use This Template')
    with step("[Verify] notShowAgainCheckBox is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox'), 'element notShowAgainCheckBox should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Verify] Photo is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Photo'), 'element Photo should be visible'
    assert True
