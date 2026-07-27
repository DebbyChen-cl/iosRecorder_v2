import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_04_01_02")
def test_test_main_04_01_02(actions: DriverActions):
    with step("[Action] Tap Camera"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Camera')
    with step("[Verify] btnMore is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnMore'), 'element btnMore should be visible'
    with step("[Action] Tap btnRotate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRotate')
    with step("[Action] Tap btnRatio"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRatio')
    with step("[Verify] btnRatio is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnRatio'), 'element btnRatio should be visible'
    with step("[Action] Tap btnTakePhoto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    with step("[Action] Tap btnRatio"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRatio')
    with step("[Verify] btnRatio is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnRatio'), 'element btnRatio should be visible'
    with step("[Action] Tap btnRatio"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRatio')
    with step("[Verify] btnRatio is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnRatio'), 'element btnRatio should be visible'
    with step("[Action] Tap btnMore"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMore')
    with step("[Action] Tap btnDate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDate')
    with step("[Verify] btnDate is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnDate'), 'element btnDate should be visible'
    with step("[Verify] 07/24/2026 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '07/24/2026'), 'element 07/24/2026 should be visible'
    with step("[Action] Tap btnDate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDate')
    with step("[Verify] btnDate is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnDate'), 'element btnDate should be visible'
    with step("[Action] Tap btnGrid"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnGrid')
    with step("[Verify] btnGrid is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnGrid'), 'element btnGrid should be visible'
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Action] Tap btnGrid"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnGrid')
    with step("[Verify] btnGrid is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnGrid'), 'element btnGrid should be visible'
    with step("[Action] Tap btnBlur"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBlur')
    with step("[Verify] btnBlur is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnBlur'), 'element btnBlur should be visible'
    with step("[Action] Tap btnBlur"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBlur')
    with step("[Verify] btnBlur is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnBlur'), 'element btnBlur should be visible'
    with step("[Action] Tap btnSetting"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSetting')
    with step("[Action] Tap SettingPageGeneralCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'SettingPageGeneralCell-0')
    with step("[Action] Tap Ultra High"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ultra High')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap SettingPageGeneralCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'SettingPageGeneralCell-0')
    with step("[Action] Tap Normal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Normal')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap SettingPageGeneralCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'SettingPageGeneralCell-0')
    with step("[Action] Tap High"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'High')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] Save GPS Location is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Save GPS Location'), 'element Save GPS Location should be visible'
    with step("[Verify] Launch with Camera is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Launch with Camera'), 'element Launch with Camera should be visible'
    with step("[Verify] Auto Save Photo is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Auto Save Photo'), 'element Auto Save Photo should be visible'
    with step("[Verify] Front Camera Mirror is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Front Camera Mirror'), 'element Front Camera Mirror should be visible'
    with step("[Verify] Countdown Sound Effect is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Countdown Sound Effect'), 'element Countdown Sound Effect should be visible'
    with step("[Verify] Time Stamp is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Time Stamp'), 'element Time Stamp should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] btnShutterMode is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnShutterMode'), 'element btnShutterMode should be visible'
    with step("[Action] Tap btnShutterMode"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShutterMode')
    with step("[Verify] btnShutterMode is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnShutterMode'), 'element btnShutterMode should be visible'
    with step("[Verify] 3 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '3'), 'element 3 should be visible'
    with step("[Verify] btnShutterMode is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnShutterMode'), 'element btnShutterMode should be visible'
    with step("[Action] Tap btnShutterMode"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShutterMode')
    with step("[Verify] btnShutterMode is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnShutterMode'), 'element btnShutterMode should be visible'
    with step("[Verify] 3 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '3'), 'element 3 should be visible'
    with step("[Verify] Press capture button to detect faces is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Press capture button to detect faces'), 'element Press capture button to detect faces should be visible'
    with step("[Verify] btnShutterMode is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnShutterMode'), 'element btnShutterMode should be visible'
    with step("[Action] Tap btnShutterMode"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShutterMode')
    with step("[Verify] btnShutterMode is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnShutterMode'), 'element btnShutterMode should be visible'
    with step("[Action] Tap btnNight"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNight')
    with step("[Verify] btnNight is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnNight'), 'element btnNight should be visible'
    with step("[Verify] Night mode on is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Night mode on'), 'element Night mode on should be visible'
    with step("[Action] Tap btnNight"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNight')
    with step("[Verify] btnNight is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnNight'), 'element btnNight should be visible'
    with step("[Action] Tap btnCounter"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCounter')
    with step("[Verify] 3 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '3'), 'element 3 should be visible'
    with step("[Verify] 3 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '3'), 'element 3 should be visible'
    with step("[Action] Tap btnCounter"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCounter')
    with step("[Verify] 5 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '5'), 'element 5 should be visible'
    with step("[Verify] 5 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '5'), 'element 5 should be visible'
    with step("[Action] Tap btnCounter"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCounter')
    with step("[Verify] 10 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '10'), 'element 10 should be visible'
    with step("[Verify] 10 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '10'), 'element 10 should be visible'
    with step("[Action] Tap btnCounter"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCounter')
    with step("[Action] Tap btnRotate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRotate')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    assert True
