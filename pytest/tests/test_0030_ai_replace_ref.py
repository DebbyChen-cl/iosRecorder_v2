import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_replace_ref")
def test_test_ai_replace_ref(actions: DriverActions):
    with step("[Action] Tap btnSettings"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
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
    with step("[Action] Tap Pro+"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pro+')
    with step("[Action] Tap chevron.left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Home"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Home')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap Sample Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap AI Replace"):
        actions.tap_by_locator(AppiumBy.NAME, 'AI Replace')
    with step("[Action] Tap AI Replace"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Replace')
    with step("[Action] Tap Replace"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace')
    with step("[Verify] Upload a reference image is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Upload a reference image'), 'element Upload a reference image should be visible'
    with step("[Action] Tap Upload a reference image"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Upload a reference image')
    with step("[Verify] descriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'), 'element descriptionLabel should be visible'
    with step("[Action] Tap PhotoPickerRecommendDialog-notShowAgainCheckBox"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap ic info n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic info n')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Swipe up"):
        # swipe up at (0,0)→(0,0) — no element matched
        assert False, "[Action] Swipe up — step could not be generated; re-record this step"
    with step("[Action] Tap Replace"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Verify] promptDisplayLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'promptDisplayLabel'), 'element promptDisplayLabel should be visible'
    with step("[Action] Tap promptTapView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptTapView')
    with step("[Verify] lblPlaceHolder is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder'), 'element lblPlaceHolder should be visible'
    with step("[Verify] lblPlaceHolder is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder'), 'element lblPlaceHolder should be visible'
    with step("[Action] Tap Next:"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')
    with step("[Action] Tap btnGenerate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate')
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap refresh"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'refresh')
    with step("[Verify] refresh is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'refresh'), 'element refresh should not be visible'
    with step("[Verify] //*[@name=\"refresh\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="refresh"]'), 'element //*[@name="refresh"] should not be visible'
    with step("[Verify] reSelectButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'reSelectButton'), 'element reSelectButton should be visible'
    with step("[Verify] descriptionLabel is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'), 'element descriptionLabel should not be visible'
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap promptTapView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptTapView')
    with step("[Action] Tap btnClear"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClear')
    with step("[Action] Tap mainImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mainImageView')
    with step("[Verify] promptDisplayLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'promptDisplayLabel'), 'element promptDisplayLabel should be visible'
    with step("[Action] Tap Replace"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Replace')
    with step("[Verify] Progress halted is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Progress halted'), 'element Progress halted should be visible'
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    assert True
