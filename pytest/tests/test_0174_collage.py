import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_collage")
def test_test_collage(actions: DriverActions):
    with step("[Action] Tap More"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'More')
    with step("[Action] Tap Collage"):
        actions.tap_by_locator(AppiumBy.NAME, 'Collage')
    with step("[Action] Tap Collage"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Collage"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step("[Action] Tap btn2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn2')
    with step("[Action] Tap at (70, 280)"):
        actions.tap_by_coordinates(70, 280)
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap btn FontDelete n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap CMS-Optional(\"phdm_20230710_Father\\\\\\'sDay_T_02_02\")"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_20230710_Father\\\'sDay_T_02_02")')
    with step("[Action] Tap btnWebstore"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnWebstore')
    with step("[Verify] btnAll is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnAll'), 'element btnAll should be visible'
    with step("[Action] Tap btn2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn2')
    with step("[Verify] btn2 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btn2'), 'element btn2 should be visible'
    with step("[Verify] btn2 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btn2'), 'element btn2 should be visible'
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Action] Tap btnWebstore"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnWebstore')
    with step("[Verify] btnAll is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnAll'), 'element btnAll should be visible'
    with step("[Action] Tap btnAll"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAll')
    with step("[Verify] btnAll is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnAll'), 'element btnAll should be visible'
    with step("[Verify] btnAll is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnAll'), 'element btnAll should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap at (395, 810)"):
        actions.tap_by_coordinates(395, 810)
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
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
    with step("[Verify] Your Photo Looks Perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your Photo Looks Perfect!'), 'element Your Photo Looks Perfect! should not be visible'
    with step("[Action] Tap More"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'More')
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap shareCell"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shareCell')
    with step("[Action] Tap at (48, 89)"):
        actions.tap_by_coordinates(48, 89)
    with step("[Action] Tap More"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'More')
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap shareCell"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shareCell')
    with step("[Verify] ConversationTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ConversationTitle'), 'element ConversationTitle should be visible'
    with step("[Action] Tap at (406, 105)"):
        actions.tap_by_coordinates(406, 105)
    with step("[Action] Tap at (63, 277)"):
        actions.tap_by_coordinates(63, 277)
    with step("[Action] Tap Instagram"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Instagram')
    with step("[Action] Tap Allow Paste"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
    with step("[Verify] Share to Instagram is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram'), 'element Share to Instagram should be visible'
    with step("[Action] Tap btnShareFB"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB')
    with step("[Action] Tap Allow Paste"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
    with step("[Verify] Post is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Post'), 'element Post should be visible'
    with step("[Action] Tap at (42, 41)"):
        actions.tap_by_coordinates(42, 41)
    with step("[Action] Tap Next Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next Edit')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Collage"):
        actions.tap_by_locator(AppiumBy.NAME, 'Collage')
    with step("[Action] Tap Collage"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step("[Action] Tap btn2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn2')
    with step("[Action] Tap at (70, 280)"):
        actions.tap_by_coordinates(70, 280)
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Action] Tap btnDone"):
        actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    with step("[Verify] btnDone is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnDone'), 'element btnDone should not be visible'
    with step("[Verify] //*[@name=\"btnDone\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btnDone"]'), 'element //*[@name="btnDone"] should not be visible'
    with step("[Verify] //*[@label=\"btnDone\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="btnDone"]'), 'element //*[@label="btnDone"] should not be visible'
    with step("[Verify] //*[@value=\"btnDone\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="btnDone"]'), 'element //*[@value="btnDone"] should not be visible'
    with step("[Action] Tap at (395, 810)"):
        actions.tap_by_coordinates(395, 810)
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
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
    with step("[Verify] Your Photo Looks Perfect! is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Your Photo Looks Perfect!'), 'element Your Photo Looks Perfect! should be visible'
    with step("[Action] Tap Later"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
    with step("[Verify] Your Photo Looks Perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your Photo Looks Perfect!'), 'element Your Photo Looks Perfect! should not be visible'
    with step("[Verify] Your Photo Looks Perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your Photo Looks Perfect!'), 'element Your Photo Looks Perfect! should not be visible'
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
    assert True
