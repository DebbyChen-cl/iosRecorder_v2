import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step
from driver.driver_actions import DriverActions


@pytest.mark.name("DragMode2")
def test_DragMode2(actions: DriverActions):
    with step("[Action] Drag (116,195) → (295,194)"):
        actions.drag_coordinates(116, 195, 295, 194, duration=1.0)
    with step("[Action] Tap btnBack at (48%, 3.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 48, 3.8)
    with step("[Action] Scroll until CMS-Optional(\"phdm_20230310_Golden_week_v2_02\")"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_20230310_Golden_week_v2_02")', direction='left')
    with step("[Action] Tap CMS-Optional(\"phdm_20230310_Golden_week_v2_02\") at (0%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_20230310_Golden_week_v2_02")', 0, 51.6)
