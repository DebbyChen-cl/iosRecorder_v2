import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("Credit Buy Now")
def test_credit_buy_now(actions: DriverActions):
    with step("[Action] Launch PhotoDirector"):
        actions.launch_app('com.cyberlink.photodirector')
    with step("[Action] Tap Settings"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 48.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=320, container_h=623)
    with step("[Action] Tap 'About'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 50.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=320, container_h=521)
    with step("[Action] Tap the developer button 5 times to enter debug mode"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 50.0, 48.6)
    with step("[Action] Open the debug subscription plan selector"):
        actions.tap_within_element(
            AppiumBy.XPATH,
            "(//XCUIElementTypeStaticText[@name='Debug Subscription Plan']/following::XCUIElementTypeButton)[1]",
            50.0,
            50.0,
        )
    with step("[Action] Set subscription mode to Pro+"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 50.0, 48.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=270, container_h=222)
    with step("[Action] Return from Debug Info to About"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 50.0, 48.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=320, container_h=693)
    with step("[Action] Return from About to Settings"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 47.6, 48.6)
    with step("[Action] Return from Settings to Home"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 47.6, 48.6)
    with step("[Action] Tap 'Mine'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMyCredit', 50.0, 48.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='launcherTrendyViewConfigCollectionView', container_w=294, container_h=119)
    with step("[Verify] 'Hello VIP!' is displayed"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'vipTitleLabel', 'Hello VIP!') is not False
    with step("[Action] Tap 'Buy Now'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBuy', 50.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.MyCreditVIPViewController"]/XCUIElementTypeScrollView', container_w=320, container_h=541)
    with step("[Action] Tap the 500-credit brick"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CreditPurchasePlanCell-3', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='creditPurchaseViewControllerCollectionView', container_w=320, container_h=280)
    with step("[Verify] Purchase button displays 'Get 500 Credits'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'btnBuy', 'Get 500 Credits for NT$1190') is not False
    with step("[Action] Tap the 1000-credit brick"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CreditPurchasePlanCell-4', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='creditPurchaseViewControllerCollectionView', container_w=320, container_h=280)
    with step("[Verify] Purchase button displays 'Get 1000 Credits'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'btnBuy', 'Get 1000 Credits for NT$1990') is not False
    with step("[Action] Tap the 2000-credit brick"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CreditPurchasePlanCell-5', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='creditPurchaseViewControllerCollectionView', container_w=320, container_h=280)
    with step("[Verify] Purchase button displays 'Get 2000 Credits'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'btnBuy', 'Get 2000 Credits for NT$2990') is not False
    with step("[Action] Tap 'Detail'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDetail', 50.0, 50.0)
    with step("[Verify] 'Credit Details' is displayed"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblDetails', 'Credit Details') is not False
