import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_image_to_video")
def test_test_image_to_video(actions: DriverActions):
    with step("[Action] Tap Image to Video"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Image to Video')
    with step("[Verify] lblDesc is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblDesc'), 'element lblDesc should be visible'
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap navArtworkButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navArtworkButton')
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap AIArtworkImageToVideoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkImageToVideoCell-1')
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
    with step("[Action] Tap btnPlay"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step("[Verify] btnPlay is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'), 'element btnPlay should be visible'
    with step("[Action] Tap btnPlay"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step("[Action] Tap btnPlay"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step("[Action] Tap navBackButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navBackButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
    with step("[Action] Tap Image to Video"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Image to Video')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap View All"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'View All')
    with step("[Action] Tap Life"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Life')
    with step("[Action] Tap High Five"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'High Five')
    with step("[Action] Tap Try with Example"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try with Example')
    with step("[Action] Tap btn refresh n"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn refresh n')
    with step("[Verify] btn refresh n is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btn refresh n'), 'element btn refresh n should not be visible'
    with step("[Verify] //*[@name=\"btn refresh n\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btn refresh n"]'), 'element //*[@name="btn refresh n"] should not be visible'
    with step("[Verify] replaceImageButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'replaceImageButton'), 'element replaceImageButton should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step("[Action] Tap 2 Solo Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '2 Solo Photos')
    with step("[Action] Tap Try with Example"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try with Example')
    with step("[Action] Tap Try with Example"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try with Example')
    with step("[Action] Tap replaceImageButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'replaceImageButton')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Verify] Continue is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Continue'), 'element Continue should not be visible'
    with step("[Verify] //*[@name=\"Continue\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Continue"]'), 'element //*[@name="Continue"] should not be visible'
    with step("[Verify] //*[@label=\"Continue\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="Continue"]'), 'element //*[@label="Continue"] should not be visible'
    with step("[Verify] //*[@value=\"Continue\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="Continue"]'), 'element //*[@value="Continue"] should not be visible'
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step("[Action] Tap replaceImageButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'replaceImageButton')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Verify] Continue is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Continue'), 'element Continue should not be visible'
    with step("[Verify] //*[@name=\"Continue\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Continue"]'), 'element //*[@name="Continue"] should not be visible'
    with step("[Verify] //*[@label=\"Continue\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="Continue"]'), 'element //*[@label="Continue"] should not be visible'
    with step("[Verify] //*[@value=\"Continue\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="Continue"]'), 'element //*[@value="Continue"] should not be visible'
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step("[Action] Tap imageSettingView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'imageSettingView')
    with step("[Action] Tap 5s"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '5s')
    with step("[Action] Tap 10s"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '10s')
    with step("[Action] Tap Pro"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pro')
    with step("[Action] Tap Standard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Standard')
    with step("[Action] Tap btnCancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step("[Action] Tap btn_cancel_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Action] Tap I Agree"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
    with step("[Verify] Generate for $3.99 is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Generate for $3.99'), 'element Generate for $3.99 should not be visible'
    with step("[Verify] processingLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'processingLabel'), 'element processingLabel should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap View All"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'View All')
    with step("[Action] Tap Life"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Life')
    with step("[Action] Tap Rich"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rich')
    with step("[Verify] Rich is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Rich'), 'element Rich should not be visible'
    with step("[Verify] //*[@name=\"Rich\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Rich"]'), 'element //*[@name="Rich"] should not be visible'
    with step("[Verify] //*[@label=\"Rich\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="Rich"]'), 'element //*[@label="Rich"] should not be visible'
    with step("[Verify] //*[@value=\"Rich\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="Rich"]'), 'element //*[@value="Rich"] should not be visible'
    assert False, "original pytest run failed — this recording reproduces a failing run"
