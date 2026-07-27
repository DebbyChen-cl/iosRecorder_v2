import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_try_on_05")
def test_test_ai_try_on_05(actions: DriverActions):
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
    with step("[Action] Tap photoCell-3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3')
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Action] Tap btn FontDelete n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n')
    with step("[Verify] **/XCUIElementTypeOther[`name == \"photodirector.PHPhotoPickViewController\"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '**/XCUIElementTypeOther[`name == "photodirector.PHPhotoPickViewController"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage'), 'element **/XCUIElementTypeOther[`name == "photodirector.PHPhotoPickViewController"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage should not be visible'
    with step("[Action] Tap photoCell-3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3')
    with step("[Action] Tap photoCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Verify] **/XCUIElementTypeOther[`name == \"photodirector.PHPhotoPickViewController\"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeImage is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '**/XCUIElementTypeOther[`name == "photodirector.PHPhotoPickViewController"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeImage'), 'element **/XCUIElementTypeOther[`name == "photodirector.PHPhotoPickViewController"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeImage should not be visible'
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] 2 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '2'), 'element 2 should be visible'
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
    with step("[Verify] activityIndicator is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should not be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap customStyleCell"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'customStyleCell')
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Verify] Please pick up to 3 photos. is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Please pick up to 3 photos.'), 'element Please pick up to 3 photos. should not be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] 3 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '3'), 'element 3 should be visible'
    with step("[Action] Tap btnGenerate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate')
    with step("[Verify] activityIndicator is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator'), 'element activityIndicator should not be visible'
    assert False, "original pytest run failed — this recording reproduces a failing run"
