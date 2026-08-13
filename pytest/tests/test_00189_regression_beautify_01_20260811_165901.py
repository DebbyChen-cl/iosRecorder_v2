import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00189_regression_beautify_01_20260811_165901")
def test_00189_regression_beautify_01_20260811_165901(actions: DriverActions):
    with step("[Action] Tap Edit at (62.9%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 62.9, 52.0)
    with step("[Action] Tap btnAlbum at (78.7%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 78.7, 57.1)
    with step("[Action] Tap Regression at (23.3%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Regression', 23.3, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-3 at (69.2%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3', 69.2, 59.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (56.8%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 56.8, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap Beautify at (63.4%, 31.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Beautify', 63.4, 31.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Auto Retouch at (65.8%, 23.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Auto Retouch', 65.8, 23.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Verify] //XCUIElementTypeCell[@name=\"CircleMenuCell-0\"]/XCUIElementTypeImage is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CircleMenuCell-0"]/XCUIElementTypeImage')
    with step("[Action] Tap btn_ok_n at (89.8%, 18.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 89.8, 18.4)
    with step("[Action] Dismiss subscription overlay via btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Action] Tap btn_cancel_n at (40.8%, 24.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 40.8, 24.5)
    with step("[Action] Exit portrait editing sub-flow via btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap homeButton at (69.2%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 69.2, 69.2)
    assert True
