import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00215_Buy_Now_Credit_20260811_180148")
def test_00215_Buy_Now_Credit_20260811_180148(actions: DriverActions):
    with step("[Action] Tap btnSettings at (63.6%, 38.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 63.6, 38.2)
    with step("[Action] Tap About at (54.9%, 78.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 54.9, 78.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (36.7%, 72.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 36.7, 72.0)
    with step("[Action] Tap Free at (58.8%, 85.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 58.8, 85.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (53.1%, 63.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 53.1, 63.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (55.0%, 47.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 55.0, 47.2)
    with step("[Action] Tap btnBack at (53.6%, 57.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 53.6, 57.4)
    with step("[Action] Tap btnBack at (32.1%, 68.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 32.1, 68.1)
    with step("[Action] Tap Mine at (56.9%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Mine', 56.9, 68.2)
    with step("[Verify] vipTitleLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'vipTitleLabel')
    with step("[Action] Tap Buy Now at (62.0%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Buy Now', 62.0, 61.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.MyCreditVIPViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=724)
    with step("[Action] Tap CreditPurchasePlanCell-3 at (8.8%, 45.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CreditPurchasePlanCell-3', 8.8, 45.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='creditPurchaseViewControllerCollectionView', container_w=430, container_h=383)
    with step("[Verify] Get 500 Credits for $34.99 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Get 500 Credits for $34.99')
    with step("[Action] Tap CreditPurchasePlanCell-4 at (11.4%, 20.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CreditPurchasePlanCell-4', 11.4, 20.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='creditPurchaseViewControllerCollectionView', container_w=430, container_h=383)
    with step("[Verify] Get 1000 Credits for $59.99 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Get 1000 Credits for $59.99')
    with step("[Action] Tap CreditPurchasePlanCell-5 at (8.8%, 21.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CreditPurchasePlanCell-5', 8.8, 21.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='creditPurchaseViewControllerCollectionView', container_w=430, container_h=383)
    with step("[Verify] Get 2000 Credits for $99.99 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Get 2000 Credits for $99.99')
    with step("[Action] Tap Detail at (44.0%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Detail', 44.0, 52.2)
    with step("[Verify] photodirector.CreditDetailsViewController is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'photodirector.CreditDetailsViewController')
    assert True
