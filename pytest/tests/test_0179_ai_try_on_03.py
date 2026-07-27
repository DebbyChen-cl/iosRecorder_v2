import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_try_on_03")
def test_test_ai_try_on_03(actions: DriverActions):
    with step("[Verify] Close is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Close'), 'element Close should not be visible'
    with step("[Verify] Would you like to continue editing? is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Would you like to continue editing?'), 'element Would you like to continue editing? should not be visible'
    with step("[Verify] closeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'closeButton'), 'element closeButton should not be visible'
    with step("[Verify] navCloseButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton'), 'element navCloseButton should not be visible'
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap AI Try-On"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On')
    with step("[Verify] notShowAgainCheckBox is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox'), 'element notShowAgainCheckBox should not be visible'
    with step("[Action] Tap importButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step("[Verify] PhotoPickerRecommendDialog-continueButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton'), 'element PhotoPickerRecommendDialog-continueButton should not be visible'
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step("[Action] Tap customStyleCell"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'customStyleCell')
    with step("[Action] Tap titleLabel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'titleLabel')
    with step("[Verify] placeholderLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel'), 'element placeholderLabel should be visible'
    with step("[Action] Tap promptApplyButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptApplyButton')
    with step("[Action] Tap btnGenerate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate')
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
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap customStyleCell"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'customStyleCell')
    with step("[Action] Tap clearButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'clearButton')
    with step("[Verify] placeholderLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'placeholderLabel'), 'element placeholderLabel should be visible'
    with step("[Action] Tap promptApplyButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptApplyButton')
    with step("[Action] Tap btnGenerate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate')
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
    assert True
