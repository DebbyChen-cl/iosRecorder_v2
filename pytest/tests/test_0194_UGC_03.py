import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_UGC_03")
def test_test_UGC_03(actions: DriverActions):
    with step("[Action] Tap Discover"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discover')
    with step("[Verify] Discover is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Discover'), 'element Discover should be visible'
    with step("[Verify] verifiedBadgeImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'verifiedBadgeImageView'), 'element verifiedBadgeImageView should be visible'
    with step("[Verify] verifiedBadgeImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'verifiedBadgeImageView'), 'element verifiedBadgeImageView should be visible'
    with step("[Verify] socialLinkImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'socialLinkImageView'), 'element socialLinkImageView should be visible'
    with step("[Action] Tap socialLinkImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'socialLinkImageView')
    with step("[Verify] Instagram is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Instagram'), 'element Instagram should be visible'
    assert True
