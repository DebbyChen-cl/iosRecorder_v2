import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_hairstyle_mystyle")
def test_test_ai_hairstyle_mystyle(actions: DriverActions):
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap AI Hairstyle"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle')
    with step("[Verify] lblDesc is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'lblDesc'), 'element lblDesc should not be visible'
    with step("[Action] Tap importButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importButton')
    with step("[Verify] descriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'), 'element descriptionLabel should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-2"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step("[Action] Tap My Style"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Style')
    with step("[Verify] category_my_style_photos_selected is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'category_my_style_photos_selected'), 'element category_my_style_photos_selected should be visible'
    with step("[Action] Long press category_my_style_photos_selected"):
        actions.long_press(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'category_my_style_photos_selected'), duration=2.0)
    with step("[Verify] Reuse is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Reuse'), 'element Reuse should not be visible'
    with step("[Action] Tap ic view"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic view')
    with step("[Verify] ic view is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'ic view'), 'element ic view should not be visible'
    with step("[Verify] //*[@name=\"ic view\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="ic view"]'), 'element //*[@name="ic view"] should not be visible'
    with step("[Verify] //*[@label=\"ic view\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="ic view"]'), 'element //*[@label="ic view"] should not be visible'
    with step("[Verify] //*[@value=\"ic view\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="ic view"]'), 'element //*[@value="ic view"] should not be visible'
    assert False, "original pytest run failed — this recording reproduces a failing run"
