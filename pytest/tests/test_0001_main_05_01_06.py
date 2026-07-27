import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_05_01_06")
def test_test_main_05_01_06(actions: DriverActions):
    # with step("[Verify] Close is not visible"):
    #     assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Close'), 'element Close should not be visible'
    with step("[Action] Tap closeButton"):
        if actions.is_element_present(
            AppiumBy.ACCESSIBILITY_ID,
            "closeButton",
            timeout=3,
        ):
            actions.tap_by_locator(
                AppiumBy.ACCESSIBILITY_ID,
                "closeButton",
            )
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Verify] “PhotoDirector” would like full access to your Photo Library. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '“PhotoDirector” would like full access to your Photo Library.'), 'element “PhotoDirector” would like full access to your Photo Library. should be visible'
    with step("[Action] Tap Allow Full Access"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Full Access')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] Edit is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Edit'), 'element Edit should be visible'
    assert True
