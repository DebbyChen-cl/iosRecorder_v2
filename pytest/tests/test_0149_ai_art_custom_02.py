import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_art_custom_02")
def test_test_ai_art_custom_02(actions: DriverActions):
    with step("[Verify] Close is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Close'), 'element Close should not be visible'
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap AI Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap importButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step("[Action] Tap My Style"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Style')
    with step("[Verify] //XCUIElementTypeCell is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//XCUIElementTypeCell'), 'element //XCUIElementTypeCell should not be visible'
    assert False, "original pytest run failed — this recording reproduces a failing run"
