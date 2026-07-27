import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_06_02_01_2")
def test_test_main_06_02_01_2(actions: DriverActions):
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap GIF"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'GIF')
    with step("[Action] Tap animationPlayIcon"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'animationPlayIcon')
    with step("[Verify] animationPlayIcon is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'animationPlayIcon'), 'element animationPlayIcon should not be visible'
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Verify] animationPlayIcon is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'animationPlayIcon'), 'element animationPlayIcon should be visible'
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] Your GIF was exported is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your GIF was exported'), 'element Your GIF was exported should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Action] Tap 16:9"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] Your GIF was exported is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your GIF was exported'), 'element Your GIF was exported should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Action] Tap 1:1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1:1')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] Your GIF was exported is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your GIF was exported'), 'element Your GIF was exported should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your animation looks perfect!'), 'element Your animation looks perfect! should be visible'
    with step("[Action] Tap Later"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Action] Tap 3:4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:4')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] Your GIF was exported is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your GIF was exported'), 'element Your GIF was exported should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] 3:4 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '3:4'), 'element 3:4 should be visible'
    with step("[Verify] Original is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Original'), 'element Original should not be visible'
    with step("[Action] Tap 4:3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] Your GIF was exported is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your GIF was exported'), 'element Your GIF was exported should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your animation looks perfect!'), 'element Your animation looks perfect! should be visible'
    with step("[Action] Tap Later"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Action] Tap 9:16"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '9:16')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] Your GIF was exported is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your GIF was exported'), 'element Your GIF was exported should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Action] Tap Video"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Video')
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Verify] animationPlayIcon is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'animationPlayIcon'), 'element animationPlayIcon should not be visible'
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Verify] animationPlayIcon is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'animationPlayIcon'), 'element animationPlayIcon should be visible'
    with step("[Verify] 1:1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '1:1'), 'element 1:1 should be visible'
    with step("[Verify] 9:16 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '9:16'), 'element 9:16 should be visible'
    with step("[Action] Drag 1:1 (50.0%,50.0%) → 9:16 (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, '1:1', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, '9:16', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap 16:9"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    with step("[Action] Tap 1:1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1:1')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap 1:1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1:1')
    with step("[Action] Tap 1080P"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1080P')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap 1:1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1:1')
    with step("[Action] Tap 2K"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '2K')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap 1:1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1:1')
    with step("[Action] Tap 4K"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4K')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] 1:1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '1:1'), 'element 1:1 should be visible'
    with step("[Verify] Original is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Original'), 'element Original should be visible'
    with step("[Action] Drag 1:1 (50.0%,50.0%) → Original (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, '1:1', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Original', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap 4:3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your animation looks perfect!'), 'element Your animation looks perfect! should be visible'
    with step("[Action] Tap Later"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] 1:1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '1:1'), 'element 1:1 should be visible'
    with step("[Verify] Original is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Original'), 'element Original should be visible'
    with step("[Action] Drag 1:1 (50.0%,50.0%) → Original (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, '1:1', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Original', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap 4:3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step("[Action] Tap 1080P"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1080P')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] 1:1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '1:1'), 'element 1:1 should be visible'
    with step("[Verify] Original is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Original'), 'element Original should be visible'
    with step("[Action] Drag 1:1 (50.0%,50.0%) → Original (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, '1:1', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Original', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap 4:3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step("[Action] Tap 2K"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '2K')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] 1:1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '1:1'), 'element 1:1 should be visible'
    with step("[Verify] Original is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Original'), 'element Original should be visible'
    with step("[Action] Drag 1:1 (50.0%,50.0%) → Original (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, '1:1', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Original', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap 4:3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    with step("[Action] Tap 4K"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4K')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] 1:1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '1:1'), 'element 1:1 should be visible'
    with step("[Verify] Original is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Original'), 'element Original should be visible'
    with step("[Action] Drag 1:1 (50.0%,50.0%) → Original (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, '1:1', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Original', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap 9:16"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '9:16')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] 1:1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '1:1'), 'element 1:1 should be visible'
    with step("[Verify] Original is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Original'), 'element Original should be visible'
    with step("[Action] Drag 1:1 (50.0%,50.0%) → Original (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, '1:1', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Original', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap 9:16"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '9:16')
    with step("[Action] Tap 1080P"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1080P')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your animation looks perfect!'), 'element Your animation looks perfect! should be visible'
    with step("[Action] Tap Later"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] 1:1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '1:1'), 'element 1:1 should be visible'
    with step("[Verify] Original is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Original'), 'element Original should be visible'
    with step("[Action] Drag 1:1 (50.0%,50.0%) → Original (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, '1:1', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Original', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap 9:16"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '9:16')
    with step("[Action] Tap 2K"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '2K')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap 3:4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:4')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
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
    with step("[Action] Tap Effects"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step("[Action] Tap btn_live_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step("[Verify] Bokeh is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), 'element Bokeh should be visible'
    with step("[Verify] Elements is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Elements'), 'element Elements should be visible'
    with step("[Action] Drag Bokeh (50.0%,50.0%) → Elements (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Bokeh', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Elements', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap Animation"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step("[Action] Tap Motion"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Verify] 1:1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '1:1'), 'element 1:1 should be visible'
    with step("[Verify] Original is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Original'), 'element Original should be visible'
    with step("[Action] Drag 1:1 (50.0%,50.0%) → Original (50.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, '1:1', 50.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'Original', 50.0, 50.0, duration=1.0)
    with step("[Action] Tap 9:16"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '9:16')
    with step("[Action] Tap 4K"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4K')
    with step("[Action] Tap navSaveButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step("[Verify] Saving... is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should be visible'
    with step("[Verify] Saving... is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saving...'), 'element Saving... should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your animation looks perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your animation looks perfect!'), 'element Your animation looks perfect! should not be visible'
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap Instagram"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Instagram')
    with step("[Action] Tap Allow Paste"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
    with step("[Verify] Share to Instagram is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram'), 'element Share to Instagram should be visible'
    with step("[Action] Tap More"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'More')
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap shareCell"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shareCell')
    with step("[Action] Tap at (48, 89)"):
        actions.tap_by_coordinates(48, 89)
    assert True
