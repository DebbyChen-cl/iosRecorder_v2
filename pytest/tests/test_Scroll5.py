import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("Scroll5")
def test_Scroll5(actions: DriverActions):
    with step("[Action] Scroll until CMS-Optional(\"phdm_20230310_Golden_week_v2_02\")"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_20230310_Golden_week_v2_02")', direction='left', offset_start=(0.762, 0.45), offset_end=(0, 0.425))
    with step("[Action] Tap CMS-Optional(\"phdm_20230310_Golden_week_v2_02\") at (53.1%, 66.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_20230310_Golden_week_v2_02")', 53.1, 66.1)
