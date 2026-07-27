import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_03_01_06_3")
def test_test_main_03_01_06_3(actions: DriverActions):
    with step("[Verify] Would you like to continue editing? is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Would you like to continue editing?'), 'element Would you like to continue editing? should not be visible'
    with step("[Verify] closeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'closeButton'), 'element closeButton should not be visible'
    with step("[Verify] navCloseButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton'), 'element navCloseButton should not be visible'
    with step("[Action] Tap btnSettings"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step("[Action] Tap Image Quality Setting"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Image Quality Setting')
    with step("[Verify] Image Quality Setting is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Image Quality Setting'), 'element Image Quality Setting should not be visible'
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Verify] Efficient (Long Side = 800 Pixels) is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Efficient (Long Side = 800 Pixels)'), 'element Efficient (Long Side = 800 Pixels) should be visible'
    with step("[Action] Tap Efficient (Long Side = 800 Pixels)"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Efficient (Long Side = 800 Pixels)')
    with step("[Verify] Good (Long Side = 1600 Pixels) is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Good (Long Side = 1600 Pixels)'), 'element Good (Long Side = 1600 Pixels) should be visible'
    with step("[Action] Tap Good (Long Side = 1600 Pixels)"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Good (Long Side = 1600 Pixels)')
    with step("[Verify] HD (Long Side = 2560 Pixels) is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'HD (Long Side = 2560 Pixels)'), 'element HD (Long Side = 2560 Pixels) should be visible'
    with step("[Action] Tap HD (Long Side = 2560 Pixels)"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HD (Long Side = 2560 Pixels)')
    with step("[Verify] Ultra HD (Long Side = 3264 Pixels) is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Ultra HD (Long Side = 3264 Pixels)'), 'element Ultra HD (Long Side = 3264 Pixels) should be visible'
    with step("[Action] Tap Ultra HD (Long Side = 3264 Pixels)"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ultra HD (Long Side = 3264 Pixels)')
    with step("[Verify] creditTipsLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'creditTipsLabel'), 'element creditTipsLabel should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Image Quality Setting is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Image Quality Setting'), 'element Image Quality Setting should not be visible'
    with step("[Verify] Maximum (Long Side = 4000 Pixels) is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Maximum (Long Side = 4000 Pixels)'), 'element Maximum (Long Side = 4000 Pixels) should be visible'
    with step("[Action] Tap Maximum (Long Side = 4000 Pixels)"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Maximum (Long Side = 4000 Pixels)')
    with step("[Verify] creditTipsLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'creditTipsLabel'), 'element creditTipsLabel should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Image Quality Setting is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Image Quality Setting'), 'element Image Quality Setting should not be visible'
    with step("[Action] Tap img tryout back n"):
        actions.tap_by_locator(AppiumBy.NAME, 'img tryout back n')
    assert True
