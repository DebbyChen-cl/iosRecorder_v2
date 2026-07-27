import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_swap_face")
def test_test_swap_face(actions: DriverActions):
    with step("[Verify] Would you like to continue editing? is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Would you like to continue editing?'), 'element Would you like to continue editing? should not be visible'
    with step("[Verify] closeButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'closeButton'), 'element closeButton should not be visible'
    with step("[Verify] navCloseButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton'), 'element navCloseButton should not be visible'
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap ScrollableMenuViewCell-Portrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step("[Action] Tap Beautify"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step("[Action] Tap Makeup"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Makeup')
    with step("[Action] Tap CircleMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-0')
    with step("[Action] Tap Lipstick"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lipstick')
    with step("[Action] Tap Dried Rose 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dried Rose 01')
    with step("[Action] Tap CircleMenuCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-1')
    with step("[Action] Tap Dried Rose 01"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dried Rose 01')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Auto Retouch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto Retouch')
    with step("[Action] Tap CircleMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-0')
    with step("[Action] Tap at (100, 90)"):
        actions.tap_by_coordinates(100, 90)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Retouch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step("[Action] Tap Jawline"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Jawline')
    with step("[Action] Tap CircleMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-0')
    with step("[Action] Tap at (100, 90)"):
        actions.tap_by_coordinates(100, 90)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Reshape"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Reshape')
    with step("[Action] Tap CircleMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-0')
    with step("[Action] Tap Face"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Face')
    with step("[Action] Tap at (100, 90)"):
        actions.tap_by_coordinates(100, 90)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Retouch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step("[Action] Tap Conceal"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Conceal')
    with step("[Verify] barImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'barImageView'), 'element barImageView should be visible'
    with step("[Verify] barImageView is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'barImageView'), 'element barImageView should not be visible'
    with step("[Action] Tap at (40, 100)"):
        actions.tap_by_coordinates(40, 100)
    with step("[Action] Tap at (100, 90)"):
        actions.tap_by_coordinates(100, 90)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Plumpness"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Plumpness')
    with step("[Action] Tap CircleMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-0')
    with step("[Action] Tap at (100, 90)"):
        actions.tap_by_coordinates(100, 90)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Smooth"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Smooth')
    with step("[Action] Tap Auto"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step("[Action] Tap CircleMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-0')
    with step("[Action] Tap at (100, 90)"):
        actions.tap_by_coordinates(100, 90)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Retouch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step("[Action] Tap Wrinkle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Wrinkle')
    with step("[Action] Tap CircleMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-0')
    with step("[Action] Tap at (100, 90)"):
        actions.tap_by_coordinates(100, 90)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Retouch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step("[Action] Tap Blemish"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blemish')
    with step("[Action] Tap CircleMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-0')
    with step("[Action] Tap at (100, 90)"):
        actions.tap_by_coordinates(100, 90)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Teeth Whiten"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Teeth Whiten')
    with step("[Action] Tap CircleMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-0')
    with step("[Action] Tap at (100, 90)"):
        actions.tap_by_coordinates(100, 90)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Eye"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye')
    with step("[Action] Tap Eye Brighten"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Brighten')
    with step("[Action] Tap CircleMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-0')
    with step("[Action] Tap at (100, 90)"):
        actions.tap_by_coordinates(100, 90)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Eye"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye')
    with step("[Action] Tap Eye Bags"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Bags')
    with step("[Action] Tap CircleMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-0')
    with step("[Action] Tap at (100, 90)"):
        actions.tap_by_coordinates(100, 90)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Retouch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step("[Action] Tap Oiliness"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Oiliness')
    with step("[Action] Tap CircleMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-0')
    with step("[Action] Tap at (100, 90)"):
        actions.tap_by_coordinates(100, 90)
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Retouch"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step("[Action] Tap Nose Enhance"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Nose Enhance')
    with step("[Action] Tap CircleMenuCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CircleMenuCell-0')
    with step("[Action] Tap at (100, 90)"):
        actions.tap_by_coordinates(100, 90)
    assert True
