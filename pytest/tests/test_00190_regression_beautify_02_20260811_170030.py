import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00190_regression_beautify_02_20260811_170030")
def test_00190_regression_beautify_02_20260811_170030(actions: DriverActions):
    with step("[Action] Tap Edit at (54.3%, 68.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 54.3, 68.0)
    with step("[Action] Tap btnAlbum at (80.7%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 80.7, 54.8)
    with step("[Action] Tap Regression at (15.8%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Regression', 15.8, 56.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-1 at (41.5%, 31.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 41.5, 31.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (64.9%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 64.9, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap Beautify at (71.8%, 28.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Beautify', 71.8, 28.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Auto Retouch at (83.6%, 21.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Auto Retouch', 83.6, 21.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Verify] //XCUIElementTypeCell[@name=\"CircleMenuCell-0\"]/XCUIElementTypeImage is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CircleMenuCell-0"]/XCUIElementTypeImage')
    with step("[Action] Tap btn_ok_n at (83.7%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 83.7, 49.0)
    with step("[Action] Dismiss subscription overlay via btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Action] Tap homeButton at (65.4%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 73.1)
    with step("[Action] Tap Discard at (59.4%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 59.4, 62.5)
    assert True
