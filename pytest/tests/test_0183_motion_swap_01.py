import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_motion_swap_01")
def test_test_motion_swap_01(actions: DriverActions):
    with step("[Verify] Close is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Close'), 'element Close should not be visible'
    with step("[Verify] Would you like to continue editing? is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Would you like to continue editing?'), 'element Would you like to continue editing? should not be visible'
    with step("[Verify] closeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'closeButton'), 'element closeButton should not be visible'
    with step("[Verify] navCloseButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton'), 'element navCloseButton should not be visible'
    with step("[Action] Tap Character Motion Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Character Motion Swap')
    with step("[Verify] AIFeatureDemoViewController is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AIFeatureDemoViewController'), 'element AIFeatureDemoViewController should be visible'
    with step("[Action] Tap notShowAgainCheckBox"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap btnInfoMode"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnInfoMode')
    with step("[Verify] Character Motion Swap is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Character Motion Swap'), 'element Character Motion Swap should be visible'
    with step("[Action] Tap Try now"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try now')
    with step("[Action] Tap btnImportFace"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace')
    with step("[Verify] descriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'), 'element descriptionLabel should be visible'
    with step("[Action] Tap PhotoPickerRecommendDialog-notShowAgainCheckBox"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step("[Verify] btnImportFace is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace'), 'element btnImportFace should be visible'
    with step("[Action] Tap btnImportFace"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace')
    with step("[Action] Tap ic info n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic info n')
    with step("[Verify] descriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'), 'element descriptionLabel should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step("[Verify] btnImportFace is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace'), 'element btnImportFace should be visible'
    with step("[Action] Tap btnImportReference"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference')
    with step("[Verify] recommendationLbl is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'recommendationLbl'), 'element recommendationLbl should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap Collections"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collections')
    with step("[Action] Tap _Video"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_Video')
    with step("[Action] Tap PXGGridLayout-Info"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PXGGridLayout-Info')
    with step("[Action] Tap Choose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Choose')
    with step("[Verify] startBarImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'startBarImageView'), 'element startBarImageView should be visible'
    with step("[Verify] endBarImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'endBarImageView'), 'element endBarImageView should be visible'
    with step("[Verify] slidingWindow is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'slidingWindow'), 'element slidingWindow should be visible'
    with step("[Verify] lblDesc is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblDesc'), 'element lblDesc should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Verify] btnImportReference is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference'), 'element btnImportReference should be visible'
    with step("[Action] Tap Keep the photo background"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Keep the photo background')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] Character Motion Swap is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Character Motion Swap'), 'element Character Motion Swap should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap navArtworkButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navArtworkButton')
    with step("[Verify] Character Motion Swap is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Character Motion Swap'), 'element Character Motion Swap should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Action] Tap ic_artwork_error_thumbnail"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic_artwork_error_thumbnail')
    with step("[Action] Tap Create More"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Create More')
    with step("[Action] Tap btnImportFace"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace')
    assert False, "original pytest run failed — this recording reproduces a failing run"
