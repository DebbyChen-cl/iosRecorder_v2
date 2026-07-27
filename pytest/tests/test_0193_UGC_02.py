import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_UGC_02")
def test_test_UGC_02(actions: DriverActions):
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Verify] likeCountLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'likeCountLabel'), 'element likeCountLabel should be visible'
    with step("[Action] Tap likeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'likeButton')
    with step("[Verify] likeCountLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'likeCountLabel'), 'element likeCountLabel should be visible'
    with step("[Action] Tap backButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'backButton')
    with step("[Verify] likeCountLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'likeCountLabel'), 'element likeCountLabel should be visible'
    with step("[Verify] likeCountLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'likeCountLabel'), 'element likeCountLabel should be visible'
    assert False, "original pytest run failed — this recording reproduces a failing run"
