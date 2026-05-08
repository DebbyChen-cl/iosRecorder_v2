import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("DragMode")
def test_DragMode(actions: DriverActions):
    with step("[Action] Drag (128,222) → (299,191)"):
        actions.stability_check = True
        actions.drag_coordinates(128, 222, 299, 191, duration=1.0)
        actions.stability_check = False
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Scroll until CMS-Optional(\"phdm_230310_SchoolEntranceCeremony_J2_02\")"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_230310_SchoolEntranceCeremony_J2_02")', direction='left')
    with step("[Action] Tap CMS-Optional(\"phdm_230310_SchoolEntranceCeremony_J2_02\") at (4.1%, 66.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_230310_SchoolEntranceCeremony_J2_02")', 4.1, 66.1)
