import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("DragMode4")
def test_DragMode4(actions: DriverActions):
    with step("[Action] Drag (106,202) → (290,212)"):
        actions.drag_coordinates(106, 202, 290, 212, duration=1.0)
    with step("[Action] Tap btnBack at (68%, 44%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 68, 44)
    with step("[Action] Scroll until CMS-Optional(\"phdm_20230310_Golden_week_v2_02\")"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_230301_ChildrensDay_TW_B2_02")', AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_20230310_Golden_week_v2_02")', direction='left')
    with step("[Action] Tap CMS-Optional(\"phdm_20230310_Golden_week_v2_02\") at (30%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_20230310_Golden_week_v2_02")', 30, 30.6)
