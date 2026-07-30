import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name('00157_ai_artwork_renew')
def test_00157_ai_artwork_renew(actions: DriverActions):
    """Exercise the AI Artwork video, art, face-swap, hairstyle, and volume entries."""

    def close_share_panel():
        actions.tap_by_coordinates(42, 41)

    def close_more_panel():
        actions.tap_by_coordinates(63, 277)

    def open_artwork(feature: str):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, feature)

    def download_share_delete(download_id: str, share_id: str, delete_id: str):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, download_id)
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'In progress', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'In progress')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, share_id)
        assert actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="shareCell" and @label="AirDrop"]')
        close_share_panel()
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, delete_id)
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, delete_id)
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')

    with step('Go to AI videos - artwork > Image to Video'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Videos')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkImageToVideoCell-0')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkImageToVideoCell-0')
        assert actions.is_element_present(AppiumBy.NAME, 'Save & Share')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navBackButton')
        assert actions.tap_by_locator(AppiumBy.NAME, 'Select')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkImageToVideoCell-0')
        download_share_delete('downloadButton', 'shareButton', 'deleteButton')
        assert actions.tap_by_locator(AppiumBy.NAME, 'Cancel')
        assert actions.tap_by_locator(AppiumBy.NAME, 'Create More')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblDesc')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navBackButton')

    with step('Go to AI photos - artwork > AI Art'):
        open_artwork('AI Art')
        assert actions.tap_by_locator(AppiumBy.NAME, 'Select')
        for index in range(4):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, f'AIArtworkPackSelectionCell-{index}')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'collageButton')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Collage')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
        download_share_delete('btnDownload', 'btnShare', 'btnDelete')
        actions.capture_for_gt('05_01_12_full_ai_art_view1.png', crop_rect=(0, 60, 276, 429))
        actions.drag_coordinates(375, 450, 20, 450)
        actions.drag_coordinates(20, 450, 375, 450)
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnEdit')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')

    with step('Go to AI photos - artwork > AI Face Swap'):
        open_artwork('AI Face Swap')
        assert actions.tap_by_locator(AppiumBy.NAME, 'Select')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
        download_share_delete('downloadButton', 'shareButton', 'deleteButton')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'editButton')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')

    for feature, snapshot in (
        ('AI hairstyle', '05_01_12_full_hairstyle_view1.png'),
        ('Hair Volume', '05_01_12_full_hairvolume_view1.png'),
    ):
        with step(f'Go to AI photos - artwork > {feature}'):
            open_artwork(feature)
            assert actions.tap_by_locator(AppiumBy.NAME, 'Select')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIArtworkPackSelectionCell-0')
            download_share_delete('downloadButton', 'shareButton', 'deleteButton')
            actions.capture_for_gt(snapshot, crop_rect=(0, 60, 276, 429))
            actions.drag_coordinates(375, 450, 20, 450)
            actions.drag_coordinates(20, 450, 375, 450)
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'editButton')
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Verify] test_00157 completion"):
        assert True
