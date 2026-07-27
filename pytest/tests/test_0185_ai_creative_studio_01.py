import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_creative_studio_01")
def test_test_ai_creative_studio_01(actions: DriverActions):
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap My Artwork"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step("[Verify] AI Creative Studio is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio'), 'element AI Creative Studio should not be visible'
    with step("[Verify] AI Creative Studio is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio'), 'element AI Creative Studio should be visible'
    with step("[Action] Tap AI Creative Studio"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
    with step("[Action] Tap AIArtworkPackSelectionCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
    with step("[Action] Tap btnShare"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShare')
    with step("[Verify] shareCell is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'shareCell'), 'element shareCell should be visible'
    with step("[Action] Tap header.closeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'header.closeButton')
    with step("[Action] Tap at (207, 177)"):
        actions.tap_by_coordinates(207, 177)
    with step("[Action] Tap btnDownload"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDownload')
    with step("[Verify] Saved to photos. is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saved to photos.'), 'element Saved to photos. should not be visible'
    with step("[Verify] Saved to Photos is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Saved to Photos'), 'element Saved to Photos should not be visible'
    with step("[Verify] Your photo was saved is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your photo was saved'), 'element Your photo was saved should not be visible'
    with step("[Verify] btnDownload is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnDownload'), 'element btnDownload should be visible'
    with step("[Action] Tap btnDelete"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step("[Verify] Delete this photo permanently? is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete this photo permanently?'), 'element Delete this photo permanently? should be visible'
    with step("[Action] Tap **/XCUIElementTypeStaticText[`name == \"Cancel\"`][1]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeStaticText[`name == "Cancel"`][1]')
    with step("[Action] Tap btnEdit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnEdit')
    with step("[Verify] Portrait is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Portrait'), 'element Portrait should be visible'
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap My Artwork"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step("[Verify] AI Creative Studio is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio'), 'element AI Creative Studio should be visible'
    with step("[Action] Tap AI Creative Studio"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
    with step("[Action] Tap Select"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Select')
    with step("[Action] Tap AIArtworkPackSelectionCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
    with step("[Action] Tap AIArtworkPackSelectionCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-1')
    with step("[Action] Tap AIArtworkPackSelectionCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-2')
    with step("[Action] Tap AIArtworkPackSelectionCell-3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-3')
    with step("[Action] Tap AIArtworkPackSelectionCell-4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-4')
    with step("[Action] Tap AIArtworkPackSelectionCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-5')
    with step("[Action] Tap shareButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shareButton')
    with step("[Verify] shareCell is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'shareCell'), 'element shareCell should be visible'
    with step("[Action] Tap header.closeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'header.closeButton')
    with step("[Action] Tap at (207, 177)"):
        actions.tap_by_coordinates(207, 177)
    with step("[Action] Tap downloadButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'downloadButton')
    with step("[Verify] Saved to photos. is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Saved to photos.'), 'element Saved to photos. should not be visible'
    with step("[Verify] Saved to Photos is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Saved to Photos'), 'element Saved to Photos should not be visible'
    with step("[Verify] Your photo was saved is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your photo was saved'), 'element Your photo was saved should not be visible'
    with step("[Verify] btnDownload is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnDownload'), 'element btnDownload should not be visible'
    with step("[Verify] downloadButton is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'downloadButton'), 'element downloadButton should be visible'
    with step("[Action] Tap deleteButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'deleteButton')
    with step("[Verify] Delete 6 photos permanently? is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete 6 photos permanently?'), 'element Delete 6 photos permanently? should be visible'
    with step("[Action] Tap Cancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step("[Action] Tap collageButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'collageButton')
    with step("[Verify] Collage is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Collage'), 'element Collage should be visible'
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Select"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Select')
    with step("[Action] Tap AIArtworkPackSelectionCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
    with step("[Action] Tap AIArtworkPackSelectionCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-1')
    with step("[Action] Tap AIArtworkPackSelectionCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-2')
    with step("[Action] Tap AIArtworkPackSelectionCell-3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-3')
    with step("[Action] Tap AIArtworkPackSelectionCell-4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-4')
    with step("[Action] Tap AIArtworkPackSelectionCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-5')
    with step("[Action] Tap AIArtworkPackSelectionCell-6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-6')
    with step("[Verify] collageButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'collageButton'), 'element collageButton should not be visible'
    with step("[Action] Tap AIArtworkPackSelectionCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-1')
    with step("[Action] Tap AIArtworkPackSelectionCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-2')
    with step("[Action] Tap AIArtworkPackSelectionCell-3"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-3')
    with step("[Action] Tap AIArtworkPackSelectionCell-4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-4')
    with step("[Action] Tap AIArtworkPackSelectionCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-5')
    with step("[Action] Tap AIArtworkPackSelectionCell-6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-6')
    with step("[Action] Tap editButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'editButton')
    with step("[Verify] Portrait is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Portrait'), 'element Portrait should be visible'
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap My Artwork"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step("[Verify] AI Creative Studio is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio'), 'element AI Creative Studio should be visible'
    with step("[Action] Tap AI Creative Studio"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
    with step("[Action] Tap Create More"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Create More')
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] Collage is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Collage'), 'element Collage should be visible'
    assert True
