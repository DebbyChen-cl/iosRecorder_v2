import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("DrageMode3")
def test_DrageMode3(actions: DriverActions):
    with step("[Action] Drag (112,176) → (259,180)"):
        actions.drag_coordinates(112, 176, 259, 180, duration=1.0)
    with step("[Action] Tap btnBack at (64%, 48%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 64, 48)
    with step("[Action] Scroll until CMS-Optional(\"phdm_20230310_Golden_week_v2_02\")"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_20230310_Golden_week_v2_02")', direction='left')
    with step("[Action] Tap CMS-Optional(\"phdm_20230310_Golden_week_v2_02\") at (44%, 59.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_20230310_Golden_week_v2_02")', 44, 59.7)
