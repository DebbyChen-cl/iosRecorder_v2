import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_image_fusion_style_transfer")
def test_test_image_fusion_style_transfer(actions: DriverActions):
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Swipe up"):
        # swipe up at (0,0)→(0,0) — no element matched
        assert False, "[Action] Swipe up — step could not be generated; re-record this step"
    with step("[Action] Tap Style Transfer"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style Transfer')
    assert False, "original pytest run failed — this recording reproduces a failing run"
