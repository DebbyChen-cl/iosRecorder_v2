import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_G02_02_06_2")
def test_test_main_G02_02_06_2(actions: DriverActions):
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap AI Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step("[Verify] lblTitle is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should not be visible'
    with step("[Action] Tap importLabel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importLabel')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap Realistic Art"):
        actions.tap_by_locator(AppiumBy.NAME, 'Realistic Art')
    with step("[Action] Tap Realistic Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Realistic Art')
    with step("[Action] Tap Sweet"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sweet')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Verify] btnSave is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnSave'), 'element btnSave should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Ok"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ok')
    with step("[Verify] Ok is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Ok'), 'element Ok should not be visible'
    with step("[Verify] //*[@name=\"Ok\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Ok"]'), 'element //*[@name="Ok"] should not be visible'
    with step("[Verify] //*[@label=\"Ok\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="Ok"]'), 'element //*[@label="Ok"] should not be visible'
    with step("[Verify] //*[@value=\"Ok\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="Ok"]'), 'element //*[@value="Ok"] should not be visible'
    with step("[Action] Tap Love"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Love')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Unlock premium features is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Unlock premium features'), 'element Unlock premium features should not be visible'
    with step("[Action] Tap Artistic Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Artistic Art')
    with step("[Action] Tap Oil Painting"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Oil Painting')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Verify] btnSave is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnSave'), 'element btnSave should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Intricate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Intricate')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Unlock premium features is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Unlock premium features'), 'element Unlock premium features should not be visible'
    with step("[Action] Tap Character"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Character')
    with step("[Action] Tap Swimsuit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Swimsuit')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Verify] btnSave is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnSave'), 'element btnSave should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Maid"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Maid')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Unlock premium features is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Unlock premium features'), 'element Unlock premium features should not be visible'
    with step("[Action] Tap Male"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Male')
    with step("[Action] Tap Fantasy 3D"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Fantasy 3D')
    with step("[Action] Tap Cowboy"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cowboy')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Verify] btnSave is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnSave'), 'element btnSave should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Prince"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Prince')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] Start 7-Day Free Trial is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Start 7-Day Free Trial'), 'element Start 7-Day Free Trial should not be visible'
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    assert True
