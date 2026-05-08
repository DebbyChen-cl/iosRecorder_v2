import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("Scroll2")
def test_Scroll2(actions: DriverActions):
    with step("[Action] Scroll until CMS-Optional(\"phdm_20230310_Golden_week_v2_02\")"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_20230310_Golden_week_v2_02")', direction='left')
    with step("[Action] Tap CMS-Optional(\"phdm_20230310_Golden_week_v2_02\") at (60%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_20230310_Golden_week_v2_02")', 60, 56.5)
