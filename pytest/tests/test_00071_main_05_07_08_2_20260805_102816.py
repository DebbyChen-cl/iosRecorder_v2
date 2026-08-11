import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00071_main_05_07_08_2_20260805_102816")
def test_00071_main_05_07_08_2_20260805_102816(actions: DriverActions):
    with step("[Action] Tap Edit at (57.1%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 57.1, 64.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap photoCell-1 at (38.5%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 38.5, 67.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (63.5%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 63.5, 46.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (42.4%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 42.4, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_conceal_portrait at (66.7%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 66.7, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_nose_enhance at (52.9%, 78.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_nose_enhance', 52.9, 78.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Action] Tap OK at (39.3%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 39.3, 52.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView', container_w=430, container_h=694)
    with step("[Action] Tap homeButton at (65.4%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 53.8)
    assert True
