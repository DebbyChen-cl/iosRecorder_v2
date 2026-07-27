import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_creative_studio_02")
def test_test_ai_creative_studio_02(actions: DriverActions):
    with step("[Verify] navCloseButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton'), 'element navCloseButton should not be visible'
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Verify] AI Creative Studio is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio'), 'element AI Creative Studio should be visible'
    with step("[Action] Tap AI Creative Studio"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap notShowAgainCheckBox"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] Collage is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Collage'), 'element Collage should be visible'
    with step("[Action] Tap Collage"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Verify] templateSectionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'templateSectionLabel'), 'element templateSectionLabel should be visible'
    with step("[Action] Tap aiCreativeStudioRouter_backButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton')
    with step("[Verify] Collage is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Collage'), 'element Collage should be visible'
    with step("[Action] Tap at (0, 0)"):
        actions.tap_by_coordinates(0, 0)
    with step("[Action] Tap addIconView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addIconView')
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Action] Tap photoCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap photoCell-4"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step("[Verify] element visible at (None,None)"):
        # verify_visible at (None,None) — no element matched
        assert False, "[Verify] element visible at (None,None) — step could not be generated; re-record this step"
    with step("[Action] Tap btn FontDelete n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n')
    with step("[Action] Tap icon photo enlarge n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'icon photo enlarge n')
    with step("[Action] Tap collageAddButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'collageAddButton')
    with step("[Verify] //XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage'), 'element //XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage should not be visible'
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] Generate is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Generate'), 'element Generate should not be visible'
    assert False, "original pytest run failed — this recording reproduces a failing run"
