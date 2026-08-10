import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00005_main_03_01_06_2')
def test_00005_main_03_01_06_2(actions: DriverActions):
    """1. Enter setting page"""
    with step('Enter setting page'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step('Enter camera setting page'):
        with step('[Action] tap_camera_setting_btn_1'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Camera Settings')
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Save GPS Location')
    with step('Back from camera setting page to setting page'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Enter about page'):
        enter_about_page_success = False
        for attempt in range(3):
            with step('[Action] enter_about_page'):
                if actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'About') and actions.is_element_present(
                    AppiumBy.ACCESSIBILITY_ID, 'developerButton', timeout=3
                ):
                    enter_about_page_success = True
                    break
        if not enter_about_page_success:
            assert False, 'Enter about page fail after 3 retries'
    with step('Check SR number'):
        with step('[Action] check_sr'):
            assert actions.verify_text(AppiumBy.NAME, 'PHI260623-02', 'PHI260623-02') is not False
    with step('Check version'):
        with step('[Action] check_version'):
            assert actions.verify_text(AppiumBy.NAME, '20.15.0', '20.15.0') is not False
    with step('Check build number'):
        with step('[Action] check_buildnumber'):
            assert actions.verify_text(AppiumBy.NAME, '2607211827 (64)', '2607211827 (64)') is not False
    with step('Back to setting page'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Enter feedback'):
        with step('[Action] tap_feedback_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Send Feedback')
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step('Tap Privacy Policy hyperlink'):
        with step('[Action] tap_privacy_policy_link'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Privacy Policy')
    with step('Verify Privacy Policy web page is displayed'):
        with step('[Action] verify_privacy_policy_web_page'):
            assert actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="CyberLink Corporation Privacy Policy for Mobile App"]')
    with step('Back to PHD'):
        with step('[Action] activate_app'):
            actions.activate_app('com.cyberlink.photodirector')
        with step('[Action] verify_feedback_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step('Input invalid feedback email'):
        with step('[Action] input_feedback_mail'):
            assert actions.type_text_by_locator(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField', TD.FEEDBACK_MAIL_INVALID)
    with step('Tap keyboard next for invalid email'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')
    with step('Verify invalid e-mail message'):
        with step('[Action] verify_invalid_email_label'):
            assert actions.is_element_present(AppiumBy.IOS_PREDICATE, 'name == "errorLabel" AND label == "Please input a valid e-mail address."')
    with step('Clear old email and input valid email'):
        with step('[Action] clear_feedback_mail'):
            actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'textField', '')
        with step('[Action] input_feedback_mail'):
            assert actions.type_text_by_locator(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField', TD.FEEDBACK_MAIL_VALID)
    with step('Tap keyboard next for valid email'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')
    with step('Verify no invalid e-mail message'):
        if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'name == "errorLabel" AND label == "Please input a valid e-mail address."'):
            assert False, 'Invalid e-mail message is still displayed'
    with step('Input feedback info'):
        with step('[Action] input_feedback_info'):
            assert actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'textViewBackground', 'CLT QA auto test, please ignore')
    with step('Verify no description required message'):
        if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'name == "errorLabel" AND label == "A description is required"'):
            assert False, 'Description required message is still displayed'
        with step('[Action] tap_feedback_tab'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step('Tap import image button'):
        with step('[Action] tap_add_screen_shot'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'imageIconView')
    with step('Tap sys_picker_collection'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collections')
    with step('Tap sys_picker_albums'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Albums')
    with step('Tap system_albums_kobe'):
        with step('[Action] tap_system_albums_kobe'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'kobe')
    with step('Tap photo_kobe'):
        with step('[Action] tap_photo_kobe'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "PXGGridLayout-Info"`][1]')
    with step('Confirm image selection'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Add')
    with step('Verify attached image thumbnail is listed'):
        with step('[Action] verify_feedback_attached_image'):
            assert actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="FeedbackScreenshotCell-1"]/XCUIElementTypeOther/XCUIElementTypeImage')
    with step('Tap Submit button'):
        with step('[Action] submit_feedback'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'submitButton')
    with step('Verify Thank you dialog is displayed'):
        with step('[Action] verify_feedback_sent_dialog'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Thank you')
    with step("[Verify] test_00005 completion"):
        assert True
