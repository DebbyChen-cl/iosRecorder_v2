import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_try_on_06")
def test_test_ai_try_on_06(actions: DriverActions):
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap Try-On"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try-On')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Action] Tap notShowAgainCheckBox"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
    with step("[Action] Tap btn close outline n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap ScrollableMenuViewCell-Portrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step("[Action] Tap AI Try-On"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On')
    with step("[Action] Tap AI Try-On"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On')
    with step("[Verify] notShowAgainCheckBox is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox'), 'element notShowAgainCheckBox should not be visible'
    with step("[Verify] We cannot find any faces. Try choosing another one. Thank you. is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'We cannot find any faces. Try choosing another one. Thank you.'), 'element We cannot find any faces. Try choosing another one. Thank you. should not be visible'
    with step("[Action] Tap Pet & Doll"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pet & Doll')
    with step("[Action] Tap Soft Towel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Soft Towel')
    with step("[Action] Tap btnGenerate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate')
    with step("[Action] Tap I Agree"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
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
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap customStyleCell"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'customStyleCell')
    with step("[Action] Tap titleLabel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'titleLabel')
    with step("[Verify] PhotoPickerRecommendDialog-continueButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton'), 'element PhotoPickerRecommendDialog-continueButton should be visible'
    with step("[Action] Tap PhotoPickerRecommendDialog-notShowAgainCheckBox"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox')
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap Try-On"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try-On')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] Photo is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Photo'), 'element Photo should be visible'
    with step("[Verify] 1 is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, '1'), 'element 1 should not be visible'
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
    with step("[Verify] activityIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should be visible'
    with step("[Verify] activityIndicator is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should not be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap clearButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'clearButton')
    with step("[Verify] Photo is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Photo'), 'element Photo should not be visible'
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
    assert True
