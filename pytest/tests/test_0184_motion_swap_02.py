import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_motion_swap_02")
def test_test_motion_swap_02(actions: DriverActions):
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
    with step("[Action] Tap btnImportFace"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step("[Action] Tap btnImportReference"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference')
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
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap Keep the photo background"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Keep the photo background')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] Character Motion Swap is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Character Motion Swap'), 'element Character Motion Swap should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    assert True
