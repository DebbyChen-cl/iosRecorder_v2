import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_01_09")
def test_test_main_05_01_09(actions: DriverActions):
    with step("[Verify] Would you like to continue editing? is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Would you like to continue editing?'), 'element Would you like to continue editing? should not be visible'
    with step("[Verify] closeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'closeButton'), 'element closeButton should not be visible'
    with step("[Verify] navCloseButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton'), 'element navCloseButton should not be visible'
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
    with step("[Action] Tap Enhance"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Enhance')
    with step("[Action] Tap Deblur"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Deblur')
    with step("[Verify] Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur.'), 'element Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur. should be visible'
    with step("[Action] Tap Try First"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step("[Verify] Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur. is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur.'), 'element Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur. should not be visible'
    with step("[Verify] downloadingAssetText is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'downloadingAssetText'), 'element downloadingAssetText should not be visible'
    with step("[Verify] Applying Deblur is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Applying Deblur'), 'element Applying Deblur should not be visible'
    with step("[Action] Tap at (200, 450)"):
        actions.tap_by_coordinates(200, 450)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Deblur"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Deblur')
    with step("[Verify] Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur.'), 'element Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur. should be visible'
    with step("[Action] Tap Try First"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step("[Verify] Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur. is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur.'), 'element Enhance the clarity of your photos with our latest AI technology, eliminating defocus and motion blur. should not be visible'
    with step("[Verify] Applying Deblur is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Applying Deblur'), 'element Applying Deblur should not be visible'
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    assert True
