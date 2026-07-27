import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_04a_06_n")
def test_test_main_05_04a_06_n(actions: DriverActions):
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap InstaFill"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'InstaFill')
    with step("[Action] Tap InstaFill"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'InstaFill')
    with step("[Action] Tap InstaFill"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'InstaFill')
    with step("[Action] Tap 4:3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step("[Action] Tap 3:2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:2')
    with step("[Action] Tap 16:9"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    with step("[Action] Tap Feed"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feed')
    with step("[Action] Tap Story"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Story')
    with step("[Action] Tap Profile"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Profile')
    with step("[Action] Tap Cover"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cover')
    with step("[Action] Tap Background"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step("[Action] Tap colorWheelImgView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'colorWheelImgView')
    with step("[Action] Tap at (315, 708)"):
        actions.tap_by_coordinates(315, 708)
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step("[Action] Tap btn_addimg_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap BG"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'BG')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap CMS-"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-')
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Action] Tap CMS-phdm_BG_Wall_03_free_trending"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_BG_Wall_03_free_trending')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap InstaFill"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'InstaFill')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    assert True
