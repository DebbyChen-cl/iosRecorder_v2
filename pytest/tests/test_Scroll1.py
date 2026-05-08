import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("Scroll1")
def test_Scroll1(actions: DriverActions):
    with step("[Action] Scroll until //XCUIElementTypeCollectionView"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', AppiumBy.XPATH, '//XCUIElementTypeCollectionView', direction='left')
    with step("[Action] Tap CMS-Optional(\"phdm_230310_SchoolEntranceCeremony_J1_02\") at (20%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_230310_SchoolEntranceCeremony_J1_02")', 20, 51.6)
