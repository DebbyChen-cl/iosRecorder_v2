import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_try_on_02")
def test_test_ai_try_on_02(actions: DriverActions):
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
    with step("[Verify] notShowAgainCheckBox is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox'), 'element notShowAgainCheckBox should be visible'
    with step("[Action] Tap notShowAgainCheckBox"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap importButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step("[Verify] PhotoPickerRecommendDialog-continueButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton'), 'element PhotoPickerRecommendDialog-continueButton should be visible'
    with step("[Action] Tap PhotoPickerRecommendDialog-notShowAgainCheckBox"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox')
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
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
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] PhotoPickerRecommendDialog-continueButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton'), 'element PhotoPickerRecommendDialog-continueButton should be visible'
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step("[Action] Tap ic info n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic info n')
    with step("[Verify] PhotoPickerRecommendDialog-continueButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton'), 'element PhotoPickerRecommendDialog-continueButton should be visible'
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
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
