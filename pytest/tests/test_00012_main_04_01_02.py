import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00012_main_04_01_02')
def test_00012_main_04_01_02(actions: DriverActions):
    """camera - front"""
    uuid = ['13fce17e-c596-4fc3-860c-e3e7f4dfefde', 'f787d033-94bd-4bbe-a89b-8fbfcebb96a7', '3445f3e7-384a-4800-a019-ce55f29721be', '32244357-375f-421f-a6ac-5277f3343079', '6dc50612-c01d-4b52-930e-38d5e2d83d82', '231cee77-dd4a-4778-ae87-edd5e8b14a5f', '448c7d7e-3f83-4cd7-8b11-0781db28561f', '277ea3ba-f120-4fda-b7ee-412ad15be425', 'b40913d5-981b-4515-b806-477d06bc7cc2', '23762309-676d-48e8-ba58-688c1fc7a856', '95009fd1-cdb7-4018-9e04-fa790d316d83', '8c50878a-5edc-4287-b492-09e3b7babece', '05b5103c-edc2-4d8a-b971-b82fecf62caa', 'cf5cea72-017a-4700-96ee-92e9133a2128', '7f332269-71a6-4287-b5f5-89ab75620a48', '42e35611-41bd-4f5d-9f53-7ec9052fa0a0', '927b5846-3f1c-4fe4-bfb6-c5fc2a750fb0', 'a53d94e4-a960-4aff-b4a5-a5bb9babee72', '99dd0486-4ecc-4771-9431-dab4889b6b4e', '1021d13b-3a8e-4df4-a945-844fb8561a55', '36a01a97-d62d-4078-9309-e18ccb34cc13', '886a1ed0-af29-4e50-97c5-b8221d1484ee', 'be261842-8ced-4b39-be78-3bd0f0b136d8', '69353e44-98a4-4487-a684-93bf02cc622d', 'df0e1f70-99bb-423d-9152-705f439e6362', '6d43b5c6-552b-47a5-a62e-174472601020', 'ef5b91da-9687-4640-a610-7312663b43e2', '433abe98-ff4d-4b29-9cbb-9a06f9a5c97a', '3a62e055-8d6e-4be4-b745-224629b8bf8f', '068e1201-3361-43ae-9057-c1c959c5d12f', '03ef6730-afe5-4f3e-aeca-7515ba2e1ee2', 'e3ffb2d0-7853-4333-85a1-51eda5967814', '326b00ea-9024-4355-bfad-5929e16f77e0']
    current_date = time.strftime('%m/%d/%Y')
    with step('[Action] tap_camera'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnMore')
    if ('front' == 'front'):
        with step('[Action] tap_cameraswitch_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRotate')
    with step('[Action] tap_3v4_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRatio')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnRatio')
    with step('[Action] tap_shot_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    with step('[Action] tap_1v1_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRatio')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnRatio')
    with step('[Action] tap_9v16_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRatio')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnRatio')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMore')):
        assert False, 'Enter camera setting menu fail'

    with step('[Action] tap_time_stamp_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDate')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, current_date):
        pass
    else:
        assert False, 'Enable time stamp fail'
    with step('[Action] tap_time_stamp_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDate')
    with step('[Action] tap_grid_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnGrid')
    if actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.CameraProViewController"]/XCUIElementTypeOther[5]/XCUIElementTypeOther'):
        pass
    else:
        assert False, 'Enable grid fail'
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnGrid')):
        assert False, 'Disable grid fail'
    with step('[Action] tap_blur_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBlur')
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnBlur')):
        assert False, 'Disable blur effect fail'
    if (not actions.tap_by_locator(AppiumBy.NAME, 'ic settings')):
        assert False, 'Enter advanced camera setting page fail'
    else:
        with step('[Action] check_camera_quality'):
            assert actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'SettingPageGeneralCell-0')
        with step('[Action] select_camera_quality'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'SettingPageGeneralCell-0')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ultra High')
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        with step('[Action] select_camera_quality'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'SettingPageGeneralCell-0')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Normal')
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        with step('[Action] select_camera_quality'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'SettingPageGeneralCell-0')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'High')
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        with step('[Action] verify_switch_change'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Save GPS Location')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Save GPS Location')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Save GPS Location')
        with step('[Action] verify_switch_change'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Launch with Camera')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Launch with Camera')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Launch with Camera')
        with step('[Action] verify_switch_change'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Auto Save Photo')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto Save Photo')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto Save Photo')
        with step('[Action] verify_switch_change'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Front Camera Mirror')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Front Camera Mirror')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Front Camera Mirror')
        with step('[Action] verify_switch_change'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Countdown Sound Effect')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Countdown Sound Effect')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Countdown Sound Effect')
        with step('[Action] verify_switch_change'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Time Stamp')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Time Stamp')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Time Stamp')
        with step('[Action] tap_back_from_camera_advanced'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    result = True
    if not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'ic mobile touch on'):
        result = False
        assert False, 'Shutter mode switch fail'
    if not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'ic smile detec'):
        result = False
        assert False, 'Shutter mode switch fail'
    if not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'ic shutter normal'):
        result = False
        assert False, 'Shutter mode switch fail'
    if result:
        pass
    else:
        assert False, 'Shutter mode switch fail'
    with step('[Action] tap_night_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNight')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Night mode on')
    with step('[Action] tap_night_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNight')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Night mode on')
    if ('front' == 'rear'):
        with step('[Action] tap_flash_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFlash')
        if not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'ic flash on'):
            assert False, 'Flash mode switch from Auto back to On fail'
        with step('[Action] tap_flash_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFlash')
        if not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'ic flash off'):
            assert False, 'Flash mode switch from On to Off fail'
        with step('[Action] tap_flash_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFlash')
        if not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'ic flash permament'):
            assert False, 'Flash mode switch from Off to Permanent On fail'
        with step('[Action] tap_flash_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFlash')
        if not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'ic flash auto'):
            assert False, 'Flash mode switch from Permanent On to Auto fail'
    with step('[Action] tap_timer_off_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCounter')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, '3')
    with step('[Action] tap_timer_3_btn'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, '3')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCounter')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, '5')
    with step('[Action] tap_timer_5_btn'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, '5')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCounter')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, '10')
    with step('[Action] tap_timer_10_btn'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, '10')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCounter')
    if ('front' == 'front'):
        with step('[Action] tap_cameraswitch_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRotate')
    if actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnBack'):
        pass
    else:
        assert False  # legacy raise
    with step("[Verify] test_00012 completion"):
        assert True
