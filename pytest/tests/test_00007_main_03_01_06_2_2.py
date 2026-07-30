import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00007_main_03_01_06_2_2')
def test_00007_main_03_01_06_2_2(actions: DriverActions):
    """1. Enter Send Feedback page"""

    with step('Launch PHD and tap settings'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step('Tap Send feedback'):
        with step('[Action] tap_feedback_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Send Feedback')
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step('Tap Order problems tab'):
        with step('[Action] tap_order_problems_tab'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Order Problems')
    with step('Tap Still have qustions? contact us v'):
        with step('[Action] tap_contact_us_expand'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'contactArrowButton')
    with step('Verify panel is opened'):
        with step('[Action] verify_contact_us_panel_opened'):
            assert actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Still have") and contains(@name,"contact us") and (contains(@name,"^") or contains(@label,"^") or contains(@value,"^"))]')
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Privacy Policy')
        actions.scroll('up', distance=50 / actions.get_screen_size()[1])
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
    with step('Tap Contact infomation column and input invalid email'):
        with step('[Action] input_feedback_mail'):
            assert actions.type_text_by_locator(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField', TD.FEEDBACK_MAIL_INVALID)
    with step('Tap next of keyboard'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')
    with step('Verify invalid e-mail message'):
        with step('[Action] verify_invalid_email_label'):
            assert actions.is_element_present(AppiumBy.IOS_PREDICATE, 'name == "errorLabel" AND label == "Please input a valid e-mail address."')
    with step('Tap Contact infomation column again and input valid email'):
        with step('[Action] clear_feedback_mail'):
            actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'textField', '')
        with step('[Action] input_feedback_mail'):
            assert actions.type_text_by_locator(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField', TD.FEEDBACK_MAIL_VALID)
    with step('Tap next of keyboard for valid email'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')
    with step('Verify no invalid e-mail message'):
        if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'name == "errorLabel" AND label == "Please input a valid e-mail address."'):
            assert False, 'Please input a valid e-mail address message is still displayed'
    with step('Input feedback info'):
        with step('[Action] input_feedback_info'):
            assert actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'textViewBackground', 'CLT QA auto test order problems')
    with step('Verify no A description is required message'):
        if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'name == "errorLabel" AND label == "A description is required"'):
            assert False, 'A description is required message is still displayed'
        with step('[Action] tap_feedback_tab'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step('Tap import image button'):
        with step('[Action] tap_add_screen_shot'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'imageIconView')
    with step('Select an image'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collections')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Albums')
        with step('[Action] tap_system_albums_kobe'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'kobe')
        with step('[Action] tap_photo_kobe'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "PXGGridLayout-Info"`][1]')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Add')
    with step('Verify attached image thumbnail is listed'):
        with step('[Action] verify_feedback_attached_image'):
            assert actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="FeedbackScreenshotCell-1"]/XCUIElementTypeOther/XCUIElementTypeImage')
    with step('Tap Submit'):
        with step('[Action] submit_feedback'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'submitButton')
    with step('Verify Thank you dialog is displayed'):
        with step('[Action] verify_feedback_sent_dialog'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Thank you')
    with step("[Verify] test_00007 completion"):
        assert True
