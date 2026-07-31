import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00057_main_05_04a_03_3')
def test_00057_main_05_04a_03_3(actions: DriverActions):
    """mosaic - style"""
    uuid = ['3eaea7ec-3eb9-4116-bca0-471a98bb4254', '76078378-1c50-41b8-a538-7fc84b785181', 'ffe0ffc7-4afe-49a5-ab8a-aeffe4b46e94', 'be5054fb-bb84-4601-bfeb-37af92aa7b17', '2dbc1a78-51bd-46bc-a1af-37fae3061aa6', '5763f4bf-56a9-4ff5-a7a8-30cc030578dd', 'e458a2ed-16bd-4eb8-b8b7-3469ddd7a64b', 'f0a388b7-72c5-4c58-b628-38d0d0cc3815', '288e850b-9ba2-42bf-b0ed-d8c8e0f8c2e5']
    with step('[Action] close_continue_edit'):
        actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mosaic')
    with step('[Action] tap_phd_element'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Person')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_blur')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_03_style1.png'):
        actions.capture_for_gt('base05_04a_03_style1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_glass')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_03_style2.png'):
        actions.capture_for_gt('base05_04a_03_style2.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_brush')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_03_style3.png'):
        actions.capture_for_gt('base05_04a_03_style3.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_circle')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_03_style4.png'):
        actions.capture_for_gt('base05_04a_03_style4.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_line')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_03_style5.png'):
        actions.capture_for_gt('base05_04a_03_style5.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_glass_tile')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_03_style6.png'):
        actions.capture_for_gt('base05_04a_03_style6.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_triangle')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_03_style7.png'):
        actions.capture_for_gt('base05_04a_03_style7.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_diamond')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_03_style8.png'):
        actions.capture_for_gt('base05_04a_03_style8.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'mosaic_tiles')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_03_style9.png'):
        actions.capture_for_gt('base05_04a_03_style9.png', crop_rect=(0, 60, 276, 429))
    with step("[Verify] test_00057 completion"):
        assert True
