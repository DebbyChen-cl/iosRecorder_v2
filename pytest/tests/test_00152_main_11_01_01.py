import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00152_main_11_01_01')
def test_00152_main_11_01_01(actions: DriverActions):
    """subscribed - camera"""
    mode = 1
    uuid = ['9f9eb1d2-7ebb-4063-82f7-b6d483bb49fd', 'e68ebf96-bab1-4440-9c84-e80f26e086b4', '0da24195-e7ce-4b13-8a0b-ed95851fa803', '934dac1d-c26e-45bd-a966-1f818c7f9a92', '574a385e-bf8c-4b7b-8c83-fb23c605b4a5', '30ef68cd-3356-4b46-a0f3-77354afe8565', '57ac7839-d204-45ea-8b78-9d572c144eff', 'b0551f5d-56b1-40ed-8648-5416b3a7afbd', '44cb8db8-ed1b-4aa8-aa59-0a77a3a62836', '4a5a584b-7115-465a-baa1-79037e329591']
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step('[Action] verify_settings_page'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Setting', timeout=5) or actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle', timeout=5)
    enter_about_page_success = False
    for attempt in range(3):
        with step('[Action] enter_about_page'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'About')
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton')
        enter_about_page_success = True
        break
        if attempt < 2:
            pass
    if not enter_about_page_success:
        assert False, 'Enter about page fail after 3 retries'
    with step('[Action] enable_plan_from_settings'):
        assert actions.is_element_present(AppiumBy.NAME, 'Develop Info')
        assert actions.find_element(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="1"])[2]')
        actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[6]')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_camera'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnMore')
    with step('[Action] tap_filter_btn2'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnFilter')
    with step('[Action] tap_look_pure_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pure')
    with step('[Action] tap_camera_filter_position'):
        assert actions.tap_by_coordinates(100, 730)
    with step('[Action] tap_shot_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    if (not actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1)):
        pass
    else:
        assert False, 'IAP displays, filter fail (uuid[5])'
    with step('[Action] tap_filter_reset_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step('[Action] tap_beautify_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Conceal')
    with step('[Action] adjust_camera_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')
    with step('[Action] tap_shot_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    if (not actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1)):
        pass
    else:
        assert False, 'IAP displays, conceal fail (uuid[1])'
    with step('[Action] tap_retouch_reset_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Skin Tone')
    with step('[Action] adjust_camera_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')
    with step('[Action] tap_shot_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    if (not actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1)):
        pass
    else:
        assert False, 'IAP displays, skin tone fail (uuid[2])'
    with step('[Action] tap_retouch_reset_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Teeth Whiten')
    with step('[Action] adjust_camera_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')
    with step('[Action] tap_shot_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    if (not actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1)):
        pass
    else:
        assert False, 'IAP displays, teeth whiten fail (uuid[3])'
    with step('[Action] tap_retouch_reset_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Brighten')
    with step('[Action] adjust_camera_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')
    with step('[Action] tap_shot_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    if (not actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1)):
        pass
    else:
        assert False, 'IAP displays, eye brighten fail (uuid[4])'
    with step('[Action] tap_retouch_reset_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Bags')
    with step('[Action] adjust_camera_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')
    with step('[Action] tap_shot_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    if (not actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1)):
        pass
    else:
        assert False, 'IAP displays, eye bags fail (uuid[8])'
    with step('[Action] tap_retouch_reset_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Oiliness')
    with step('[Action] adjust_camera_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')
    with step('[Action] tap_shot_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    if (not actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1)):
        pass
    else:
        assert False, 'IAP displays, oiliness fail (uuid[9])'
    with step('[Action] tap_retouch_reset_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnReset')
    with step('[Action] tap_makeup_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Makeup')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lipstick')
    with step('[Action] tap_lipstick_03'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Nude 01')
    with step('[Action] tap_shot_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    if (not actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1)):
        pass
    else:
        assert False, 'IAP displays, makeup fail (uuid[7])'
    with step("[Verify] test_00152 completion"):
        assert True
