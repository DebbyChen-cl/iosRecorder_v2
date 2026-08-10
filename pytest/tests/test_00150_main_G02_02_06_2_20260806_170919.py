import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00150_main_G02_02_06_2_20260806_170919")
def test_00150_main_G02_02_06_2_20260806_170919(actions: DriverActions):
    with step("[Action] Tap btnStudio at (52.6%, 27.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnStudio', 52.6, 27.3)
    with step("[Action] Tap AI Art at (66.7%, 72.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Art', 66.7, 72.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap importLabel at (59.3%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importLabel', 59.3, 45.0)
    with step("[Action] Tap Continue at (71.6%, 43.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 71.6, 43.5)
    with step("[Action] Tap btnAlbum at (67.5%, 69.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 67.5, 69.0)
    with step("[Action] Tap _AT at (9.7%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.7, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (62.3%, 22.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 62.3, 22.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Scroll until Realistic Art"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'titleCollectionViewCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Realistic Art', direction='left', offset_start=(0.851, 0.606), offset_end=(0.258, 0.606), velocity=432)
    with step("[Action] Tap Realistic Art at (70.1%, 74.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Realistic Art', 70.1, 74.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=33)
    with step("[Action] Tap CMS-Realistic_Style_020_Sweet1_Female at (55.7%, 36.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Realistic_Style_020_Sweet1_Female', 55.7, 36.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap Generate at (37.5%, 45.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 37.5, 45.8)
    with step("[Verify] waitLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'waitLabel', appear_timeout=5, disappear_timeout=1200), 'waitLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnSave at (53.8%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSave', 53.8, 61.5)
    with step("[Action] Tap btnBack at (50.0%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 50.0, 69.2)
    with step("[Action] Tap CMS-Realistic_Style_001_Love1_Female at (52.3%, 51.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Realistic_Style_001_Love1_Female', 52.3, 51.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap Generate at (72.5%, 54.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 72.5, 54.2)
    with step("[Action] Tap btnClose at (54.8%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 54.8, 54.8)
    with step("[Action] Tap Artistic Art at (51.5%, 29.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Artistic Art', 51.5, 29.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=33)
    with step("[Action] Tap CMS-Style_008_Oil-Painting_Female at (55.7%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_008_Oil-Painting_Female', 55.7, 61.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap Generate at (67.5%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 67.5, 75.0)
    with step("[Verify] In progress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'In progress', appear_timeout=5, disappear_timeout=1200), 'In progress did not appear within 5s or is still shown after 1200s'
    with step("[Verify] ArtisticAvatarResultCell-0 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-0')
    with step("[Verify] ArtisticAvatarResultCell-1 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-1')
    with step("[Action] Tap btnSave at (76.9%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSave', 76.9, 61.5)
    with step("[Action] Tap btnBack at (38.5%, 38.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 38.5, 38.5)
    with step("[Action] Tap CMS-Style_007_Intricate_Female at (54.5%, 62.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_007_Intricate_Female', 54.5, 62.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap Generate at (93.8%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 93.8, 83.3)
    with step("[Action] Tap btnClose at (67.7%, 74.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 67.7, 74.2)
    with step("[Action] Tap Character at (63.4%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Character', 63.4, 44.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=33)
    with step("[Action] Tap CMS-Style_025_Swimsuit_Female at (64.8%, 57.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_025_Swimsuit_Female', 64.8, 57.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap Generate at (72.5%, 91.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 72.5, 91.7)
    with step("[Verify] In progress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'In progress', appear_timeout=5, disappear_timeout=1200), 'In progress did not appear within 5s or is still shown after 1200s'
    with step("[Verify] ArtisticAvatarResultCell-0 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-0')
    with step("[Verify] ArtisticAvatarResultCell-1 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-1')
    with step("[Verify] ArtisticAvatarResultCell-2 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-2')
    with step("[Action] Tap btnBack at (42.3%, 34.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 42.3, 34.6)
    with step("[Action] Tap CMS-Style_027_Maid_Female at (59.1%, 35.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_027_Maid_Female', 59.1, 35.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap Generate at (82.5%, 79.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 82.5, 79.2)
    with step("[Action] Tap btnClose at (64.5%, 61.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 64.5, 61.3)
    with step("[Action] Tap Male at (72.2%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Male', 72.2, 75.0)
    with step("[Action] Tap Fantasy 3D at (56.3%, 51.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Fantasy 3D', 56.3, 51.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=431, container_h=33)
    with step("[Action] Tap CMS-Style_007_Cowboy_Male at (50.0%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_007_Cowboy_Male', 50.0, 61.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap Generate at (31.2%, 16.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 31.2, 16.7)
    with step("[Verify] In progress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'In progress', appear_timeout=5, disappear_timeout=1200), 'In progress did not appear within 5s or is still shown after 1200s'
    with step("[Verify] ArtisticAvatarResultCell-0 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-0')
    with step("[Verify] ArtisticAvatarResultCell-1 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-1')
    with step("[Verify] ArtisticAvatarResultCell-2 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-2')
    with step("[Verify] ArtisticAvatarResultCell-3 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-3')
    with step("[Action] Tap btnSave at (65.4%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSave', 65.4, 57.7)
    with step("[Action] Tap btnBack at (30.8%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 30.8, 42.3)
    with step("[Action] Tap CMS-Style_006_Prince_Male at (55.7%, 59.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_006_Prince_Male', 55.7, 59.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap Generate at (80.0%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 80.0, 41.7)
    with step("[Action] Tap btnClose at (45.2%, 41.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 45.2, 41.9)
    with step("[Action] Tap navBackButton at (80.0%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 80.0, 65.0)
    with step("[Action] Tap btnHome at (48.7%, 30.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 48.7, 30.9)
    assert True
