import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_03_01_06_2_2")
def test_test_main_03_01_06_2_2(actions: DriverActions):
    with step("[Action] Tap btnSettings"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step("[Action] Tap Send Feedback"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Send Feedback')
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap Order Problems"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Order Problems')
    with step("[Action] Tap contactArrowButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'contactArrowButton')
    with step("[Verify] //XCUIElementTypeStaticText[contains(@name,\"Still have\") and contains(@name,\"contact us\") and (contains(@name,\"^\") or contains(@label,\"^\") or contains(@value,\"^\"))] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Still have") and contains(@name,"contact us") and (contains(@name,"^") or contains(@label,"^") or contains(@value,"^"))]'), 'element //XCUIElementTypeStaticText[contains(@name,"Still have") and contains(@name,"contact us") and (contains(@name,"^") or contains(@label,"^") or contains(@value,"^"))] should not be visible'
    with step("[Verify] Privacy Policy is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Privacy Policy'), 'element Privacy Policy should be visible'
    with step("[Action] Tap Privacy Policy"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Privacy Policy')
    with step("[Verify] CyberLink Corporation Privacy Policy for Mobile App is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'CyberLink Corporation Privacy Policy for Mobile App'), 'element CyberLink Corporation Privacy Policy for Mobile App should be visible'
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Type 'aaa' into textField"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'textField', 'aaa')
    with step("[Action] Tap Next:"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')
    with step("[Verify] errorLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'errorLabel'), 'element errorLabel should be visible'
    with step("[Verify] textField is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'textField'), 'element textField should be visible'
    with step("[Action] Type 'CLTQAATtest@CLT.com' into textField"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'textField', 'CLTQAATtest@CLT.com')
    with step("[Action] Tap Next:"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')
    with step("[Verify] name == \"errorLabel\" AND label == \"Please input a valid e-mail address.\" is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, 'name == "errorLabel" AND label == "Please input a valid e-mail address."'), 'element name == "errorLabel" AND label == "Please input a valid e-mail address." should not be visible'
    with step("[Action] Type 'CLT QA auto test order problems' into textViewBackground"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'textViewBackground', 'CLT QA auto test order problems')
    with step("[Verify] name == \"errorLabel\" AND label == \"A description is required\" is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, 'name == "errorLabel" AND label == "A description is required"'), 'element name == "errorLabel" AND label == "A description is required" should not be visible'
    with step("[Action] Tap lblTitle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Action] Tap imageIconView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'imageIconView')
    with step("[Action] Tap Collections"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collections')
    with step("[Action] Tap Albums"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Albums')
    with step("[Action] Tap kobe"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'kobe')
    with step("[Action] Tap PXGGridLayout-Info"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PXGGridLayout-Info')
    with step("[Action] Tap Add"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add')
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Action] Tap submitButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'submitButton')
    with step("[Verify] Thank you is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Thank you'), 'element Thank you should be visible'
    assert True
