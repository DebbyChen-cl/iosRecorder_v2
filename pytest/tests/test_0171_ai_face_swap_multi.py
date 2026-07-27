import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_face_swap_multi")
def test_test_ai_face_swap_multi(actions: DriverActions):
    with step("[Action] Tap btnSettings"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step("[Verify] Setting is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Setting'), 'element Setting should not be visible'
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap About"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'About')
    with step("[Verify] developerButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'developerButton'), 'element developerButton should be visible'
    with step("[Verify] Develop Info is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Develop Info'), 'element Develop Info should be visible'
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Action] Tap Free"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Free')
    with step("[Action] Tap Pro+"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pro+')
    with step("[Action] Tap chevron.left"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Home"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Home')
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap at (210, 340)"):
        actions.tap_by_coordinates(210, 340)
    with step("[Verify] hintLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'hintLabel'), 'element hintLabel should be visible'
    with step("[Action] Tap faceSelectionCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'faceSelectionCell-0')
    with step("[Action] Tap faceSelectionCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'faceSelectionCell-1')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] titleLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'titleLabel'), 'element titleLabel should be visible'
    with step("[Action] Tap addSourceImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addSourceImageView')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step("[Verify] Import Photos... is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Import Photos...'), 'element Import Photos... should not be visible'
    with step("[Verify] hintLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'hintLabel'), 'element hintLabel should be visible'
    with step("[Action] Tap faceSelectionCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'faceSelectionCell-0')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap addSourceImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addSourceImageView')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step("[Action] Tap Continue Anyway"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway')
    with step("[Verify] Import Photos... is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Import Photos...'), 'element Import Photos... should not be visible'
    with step("[Verify] titleLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'titleLabel'), 'element titleLabel should be visible'
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] barImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'barImageView'), 'element barImageView should be visible'
    with step("[Verify] barImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'barImageView'), 'element barImageView should be visible'
    with step("[Verify] barImageView is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'barImageView'), 'element barImageView should not be visible'
    with step("[Verify] btnSave is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnSave'), 'element btnSave should be visible'
    with step("[Action] Tap btnSave"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSave')
    with step("[Action] Tap Next Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next Edit')
    with step("[Verify] Stock is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Stock'), 'element Stock should be visible'
    assert True
