import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_11_01_2")
def test_test_main_05_11_01_2(actions: DriverActions):
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
    with step("[Action] Tap photoCell-6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap Add Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step("[Action] Tap Add Photo"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Add Photo')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Verify] photoCell-1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1'), 'element photoCell-1 should be visible'
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Action] Tap Crop & Rotate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop & Rotate')
    with step("[Verify] Crop & Rotate is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Crop & Rotate'), 'element Crop & Rotate should not be visible'
    with step("[Verify] //*[@name=\"Crop & Rotate\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Crop & Rotate"]'), 'element //*[@name="Crop & Rotate"] should not be visible'
    with step("[Verify] lblText is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblText'), 'element lblText should be visible'
    with step("[Action] Tap Rotate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rotate')
    with step("[Action] Tap Flip Horizontally"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Horizontally')
    with step("[Action] Tap Flip Vertically"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Flip Vertically')
    with step("[Action] Tap Original"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step("[Action] Tap Square"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Square')
    with step("[Action] Tap 4:3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step("[Action] Tap 3:4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:4')
    with step("[Action] Tap 3:2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')
    with step("[Action] Tap 2:3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '2:3')
    with step("[Action] Tap 16:9"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    with step("[Action] Tap 9:16"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '9:16')
    with step("[Action] Tap Feed"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feed')
    with step("[Action] Tap Story"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Story')
    with step("[Action] Tap Profile"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Profile')
    with step("[Action] Tap Cover"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cover')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    assert True
