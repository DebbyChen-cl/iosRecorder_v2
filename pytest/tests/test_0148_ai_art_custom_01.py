import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_art_custom_01")
def test_test_ai_art_custom_01(actions: DriverActions):
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap AI Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step("[Verify] lblTitle is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should not be visible'
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
    with step("[Action] Tap Start"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Start')
    with step("[Action] Tap promptTextView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptTextView')
    with step("[Action] Type 'custom001' into XCUIElementTypeTextField"):
        actions.type_text_by_locator(AppiumBy.XPATH, 'XCUIElementTypeTextField', 'custom001')
    assert False, "original pytest run failed — this recording reproduces a failing run"
