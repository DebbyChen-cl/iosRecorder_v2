import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_08_01_n4")
def test_test_main_05_08_01_n4(actions: DriverActions):
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
    with step("[Verify] xpromo btn close n is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'xpromo btn close n'), 'element xpromo btn close n should not be visible'
    with step("[Action] Tap Text"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step("[Action] Tap Text"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step("[Action] Tap Colorful"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Colorful')
    with step("[Action] Tap leaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step("[Action] Tap at (205, 455)"):
        actions.tap_by_coordinates(205, 455)
    with step("[Action] Tap Colorful"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Colorful')
    with step("[Action] Tap CMS-phdm_text_style_yellow_12_new"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_yellow_12_new')
    with step("[Action] Tap CMS-phdm_text_style_yellow_18_new"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_yellow_18_new')
    with step("[Action] Tap CMS-phdm_text_style_yellow_20_new"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_yellow_20_new')
    with step("[Action] Tap Background"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step("[Action] Tap CMS-phdm_text_style_202212_004"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_202212_004')
    with step("[Action] Tap CMS-phdm_text_style_202508_011"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_202508_011')
    with step("[Action] Tap CMS-phdm_text_style_202302_002"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_202302_002')
    with step("[Action] Tap CMS-phdm_text_style_202302_011"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_202302_011')
    assert True
