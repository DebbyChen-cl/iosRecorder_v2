import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00100_main_05_08_01_n2_20260808_201138")
def test_00100_main_05_08_01_n2_20260808_201138(actions: DriverActions):
    with step("[Action] Tap Edit at (62.9%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 62.9, 56.0)
    with step("[Action] Tap btnAlbum at (74.6%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 74.6, 47.6)
    with step("[Action] Tap _AT at (8.6%, 13.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.6, 13.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (61.5%, 52.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 61.5, 52.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (66.7%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 66.7, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Text"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Text', direction='left', offset_start=(0.423, 0.371), offset_end=(0.351, 0.371), velocity=50)
    with step("[Action] Tap Text at (59.2%, 15.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text', 59.2, 15.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Text at (40.3%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text', 40.3, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap Font at (46.9%, 26.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Font', 46.9, 26.3)
    with step("[Action] Drag imageView (49.6%,49.2%) → backgroundView (50.0%,17.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'imageView', 49.6, 49.2, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 50.0, 17.7, duration=1.0)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step11' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step11', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Drag Join PhotoDirector Premium to unlock the current effect. (45.7%,31.1%) → backgroundView (47.7%,90.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'Join PhotoDirector Premium to unlock the current effect.', 45.7, 31.1, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 47.7, 90.8, duration=1.0)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step13' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step13', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap imageView at (51.6%, 27.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 51.6, 27.6)
    with step("[Action] Tap Font at (68.8%, 57.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Font', 68.8, 57.9)
    with step("[Action] Tap languageButton at (88.0%, 52.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'languageButton', 88.0, 52.9)
    with step("[Action] Tap All Languages at (58.8%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'All Languages', 58.8, 57.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=324)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step18' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step18', AppiumBy.ACCESSIBILITY_ID, 'mainPanel', threshold=0.95)
    with step("[Action] Tap languageButton at (94.9%, 44.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'languageButton', 94.9, 44.1)
    with step("[Action] Tap Traditional Chinese at (37.0%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Traditional Chinese', 37.0, 53.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=324)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step21' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step21', AppiumBy.ACCESSIBILITY_ID, 'mainPanel', threshold=0.95)
    with step("[Action] Tap languageButton at (95.1%, 38.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'languageButton', 95.1, 38.2)
    with step("[Action] Tap Simplified Chinese at (68.0%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Simplified Chinese', 68.0, 53.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=324)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step24' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step24', AppiumBy.ACCESSIBILITY_ID, 'mainPanel', threshold=0.95)
    with step("[Action] Tap languageButton at (97.2%, 44.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'languageButton', 97.2, 44.1)
    with step("[Action] Tap Japanese at (82.1%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Japanese', 82.1, 53.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=324)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step27' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step27', AppiumBy.ACCESSIBILITY_ID, 'mainPanel', threshold=0.95)
    with step("[Action] Tap languageButton at (95.1%, 47.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'languageButton', 95.1, 47.1)
    with step("[Action] Tap Korean at (61.4%, 51.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Korean', 61.4, 51.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=324)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step30' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step30', AppiumBy.ACCESSIBILITY_ID, 'mainPanel', threshold=0.95)
    with step("[Action] Tap languageButton at (96.3%, 47.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'languageButton', 96.3, 47.1)
    with step("[Action] Tap All Languages at (91.2%, 59.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'All Languages', 91.2, 59.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=324)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step33' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step33', AppiumBy.ACCESSIBILITY_ID, 'mainPanel', threshold=0.95)
    with step("[Action] Tap styleButton at (92.0%, 58.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'styleButton', 92.0, 58.8)
    with step("[Action] Tap Handwriting at (66.3%, 59.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Handwriting', 66.3, 59.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=324)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step36' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step36', AppiumBy.ACCESSIBILITY_ID, 'mainPanel', threshold=0.95)
    with step("[Action] Tap styleButton at (91.9%, 52.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'styleButton', 91.9, 52.9)
    with step("[Action] Tap Calligraphy at (50.0%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Calligraphy', 50.0, 53.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=324)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step39' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step39', AppiumBy.ACCESSIBILITY_ID, 'mainPanel', threshold=0.95)
    with step("[Action] Tap styleButton at (98.3%, 58.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'styleButton', 98.3, 58.8)
    with step("[Action] Tap Monospace at (43.6%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Monospace', 43.6, 53.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=324)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step42' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step42', AppiumBy.ACCESSIBILITY_ID, 'mainPanel', threshold=0.95)
    with step("[Action] Tap styleButton at (97.5%, 58.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'styleButton', 97.5, 58.8)
    with step("[Action] Tap All Styles at (64.9%, 67.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'All Styles', 64.9, 67.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=324)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step45' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step45', AppiumBy.ACCESSIBILITY_ID, 'mainPanel', threshold=0.95)
    with step("[Action] Tap favoriteButton at (62.5%, 53.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'favoriteButton', 62.5, 53.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='fontCollectionView', container_w=430, container_h=241)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step47' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step47', AppiumBy.ACCESSIBILITY_ID, 'TextFontCell-0', threshold=0.95)
    with step("[Action] Tap favoriteButton at (37.5%, 43.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'favoriteButton', 37.5, 43.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='fontCollectionView', container_w=430, container_h=241)
    with step("[Verify] Capture '00100_main_05_08_01_n2_Step49' for GT comparison"):
        actions.capture_for_gt('00100_main_05_08_01_n2_Step49', AppiumBy.ACCESSIBILITY_ID, 'TextFontCell-0', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (81.6%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 26.5)
    with step("[Action] Tap OK at (96.7%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 96.7, 50.0)
    with step("[Action] Tap homeButton at (53.8%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 53.8, 73.1)
    with step("[Action] Tap Discard at (69.6%, 54.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 69.6, 54.2)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
