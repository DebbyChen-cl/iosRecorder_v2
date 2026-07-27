import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_artwork_renew")
def test_test_ai_artwork_renew(actions: DriverActions):
    with step("[Action] Tap AI Videos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Videos')
    with step("[Action] Tap My Artwork"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step("[Verify] My AI Artwork is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'My AI Artwork'), 'element My AI Artwork should not be visible'
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap AIArtworkImageToVideoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkImageToVideoCell-0')
    with step("[Verify] Save & Share is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Save & Share'), 'element Save & Share should be visible'
    with step("[Action] Tap navBackButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navBackButton')
    with step("[Action] Tap Select"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Select')
    with step("[Action] Tap AIArtworkImageToVideoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkImageToVideoCell-0')
    with step("[Action] Tap downloadButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'downloadButton')
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap shareButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shareButton')
    with step("[Verify] shareCell is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'shareCell'), 'element shareCell should be visible'
    with step("[Action] Tap at (207, 177)"):
        actions.tap_by_coordinates(207, 177)
    with step("[Action] Tap deleteButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'deleteButton')
    with step("[Verify] Delete is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete'), 'element Delete should be visible'
    with step("[Action] Tap Cancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step("[Action] Tap Cancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step("[Action] Tap Create More"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Create More')
    with step("[Verify] lblDesc is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblDesc'), 'element lblDesc should be visible'
    with step("[Action] Tap navBackButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navBackButton')
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap My Artwork"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step("[Action] Tap AI Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step("[Action] Tap AI Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step("[Action] Tap AI Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
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
    with step("[Action] Tap Cancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step("[Action] Tap AIArtworkPackSelectionCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
    with step("[Action] Tap btnDownload"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDownload')
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap btnShare"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShare')
    with step("[Verify] shareCell is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'shareCell'), 'element shareCell should be visible'
    with step("[Action] Tap at (207, 177)"):
        actions.tap_by_coordinates(207, 177)
    with step("[Action] Tap btnDelete"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step("[Verify] Delete is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete'), 'element Delete should be visible'
    with step("[Action] Tap Cancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step("[Action] Tap btnEdit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnEdit')
    with step("[Verify] Quick Actions is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions'), 'element Quick Actions should be visible'
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap My Artwork"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step("[Action] Tap AI Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step("[Action] Tap AI Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step("[Action] Tap AI Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step("[Action] Tap Create More"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Create More')
    with step("[Verify] lblTitle is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should not be visible'
    with step("[Action] Tap navBackButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navBackButton')
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap My Artwork"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap Select"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Select')
    with step("[Action] Tap AIArtworkPackSelectionCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
    with step("[Action] Tap downloadButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'downloadButton')
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap shareButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shareButton')
    with step("[Verify] shareCell is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'shareCell'), 'element shareCell should be visible'
    with step("[Action] Tap at (207, 177)"):
        actions.tap_by_coordinates(207, 177)
    with step("[Action] Tap deleteButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'deleteButton')
    with step("[Verify] Delete is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete'), 'element Delete should be visible'
    with step("[Action] Tap Cancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step("[Action] Tap editButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'editButton')
    with step("[Verify] Quick Actions is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions'), 'element Quick Actions should be visible'
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap My Artwork"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
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
    with step("[Action] Tap Cancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step("[Action] Tap AIArtworkPackSelectionCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap btnDownload"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDownload')
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap btnShare"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShare')
    with step("[Verify] shareCell is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'shareCell'), 'element shareCell should be visible'
    with step("[Action] Tap at (207, 177)"):
        actions.tap_by_coordinates(207, 177)
    with step("[Action] Tap btnDelete"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step("[Verify] Delete is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete'), 'element Delete should be visible'
    with step("[Action] Tap Cancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step("[Action] Tap btnEdit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnEdit')
    with step("[Verify] Quick Actions is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions'), 'element Quick Actions should be visible'
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap My Artwork"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap Create More"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Create More')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Verify] Seamlessly swap in your face on your favorite photos or poster with friends and family. is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Seamlessly swap in your face on your favorite photos or poster with friends and family.'), 'element Seamlessly swap in your face on your favorite photos or poster with friends and family. should not be visible'
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap My Artwork"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step("[Action] Tap AI Hairstyle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle')
    with step("[Action] Tap AI Hairstyle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle')
    with step("[Action] Tap Select"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Select')
    with step("[Action] Tap AIArtworkPackSelectionCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap downloadButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'downloadButton')
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap shareButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shareButton')
    with step("[Verify] shareCell is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'shareCell'), 'element shareCell should be visible'
    with step("[Action] Tap at (207, 177)"):
        actions.tap_by_coordinates(207, 177)
    with step("[Action] Tap deleteButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'deleteButton')
    with step("[Verify] Delete is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete'), 'element Delete should be visible'
    with step("[Action] Tap Cancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step("[Action] Tap editButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'editButton')
    with step("[Verify] Quick Actions is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions'), 'element Quick Actions should be visible'
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap My Artwork"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step("[Action] Tap AI Hairstyle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle')
    with step("[Action] Tap AI Hairstyle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle')
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
    with step("[Action] Tap collageButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'collageButton')
    assert False, "original pytest run failed — this recording reproduces a failing run"
