import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_G02_01_04")
def test_test_main_G02_01_04(actions: DriverActions):
    with step("[Action] Tap AI Videos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Videos')
    with step("[Action] Tap AI Anime Video"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Anime Video')
    with step("[Action] Tap Try Now"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try Now')
    with step("[Action] Tap navArtworkButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navArtworkButton')
    with step("[Action] Tap AIAnimeVideoHistoryCellView-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIAnimeVideoHistoryCellView-0')
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap Save"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Save')
    with step("[Action] Tap btnShareFB"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB')
    with step("[Action] Tap Allow Paste"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
    with step("[Verify] Post is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Post'), 'element Post should be visible'
    with step("[Action] Tap at (42, 41)"):
        actions.tap_by_coordinates(42, 41)
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
    with step("[Verify] shareCell is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'shareCell'), 'element shareCell should be visible'
    with step("[Action] Tap at (63, 277)"):
        actions.tap_by_coordinates(63, 277)
    with step("[Action] Tap ic play whiteCircleBg black"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic play whiteCircleBg black')
    with step("[Verify] ic play whiteCircleBg black is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'ic play whiteCircleBg black'), 'element ic play whiteCircleBg black should not be visible'
    with step("[Verify] //*[@name=\"ic play whiteCircleBg black\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="ic play whiteCircleBg black"]'), 'element //*[@name="ic play whiteCircleBg black"] should not be visible'
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap btnPlay"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step("[Action] Tap btnPlay"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step("[Action] Tap btn back n"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn back n')
    with step("[Verify] btn back n is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btn back n'), 'element btn back n should not be visible'
    with step("[Verify] //*[@name=\"btn back n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn back n"]'), 'element //*[@name="btn back n"] should not be visible'
    with step("[Verify] navBackButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navBackButton'), 'element navBackButton should be visible'
    with step("[Verify] Save & Share is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Save & Share'), 'element Save & Share should be visible'
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Action] Tap AI Videos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Videos')
    with step("[Action] Tap AI Anime Video"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Anime Video')
    with step("[Action] Tap Try Now"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try Now')
    with step("[Action] Tap Continue with the Vivid Style"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue with the Vivid Style')
    with step("[Verify] iconImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'iconImageView'), 'element iconImageView should be visible'
    with step("[Action] Tap iconImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'iconImageView')
    with step("[Verify] buyFlowLightButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Verify] Unlock premium features is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Unlock premium features'), 'element Unlock premium features should not be visible'
    with step("[Action] Tap Credits"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Credits')
    with step("[Verify] lblPlan is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblPlan'), 'element lblPlan should be visible'
    with step("[Action] Tap Select Video and Trim"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Select Video and Trim')
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap Collections"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collections')
    with step("[Action] Tap _Video"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_Video')
    with step("[Action] Tap PXGGridLayout-Info"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PXGGridLayout-Info')
    with step("[Action] Tap Choose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Choose')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] labelProcessing is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing'), 'element labelProcessing should be visible'
    with step("[Verify] Please keep the app open. is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Please keep the app open.'), 'element Please keep the app open. should not be visible'
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    assert True
