import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00147_main_G02_02_06_20260806_165340")
def test_00147_main_G02_02_06_20260806_165340(actions: DriverActions):
    with step("[Action] Tap btnStudio at (43.4%, 16.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnStudio', 43.4, 16.4)
    with step("[Action] Tap AI Art at (71.8%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Art', 71.8, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Action] Tap notShowAgainCheckBox at (59.3%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox', 59.3, 69.2)
    with step("[Action] Tap Try now at (75.7%, 26.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try now', 75.7, 26.1)
    with step("[Action] Tap CMS-Style_1024_Clean_Flux_Female at (63.6%, 54.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_1024_Clean_Flux_Female', 63.6, 54.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap Male at (47.2%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Male', 47.2, 70.0)
    with step("[Action] Tap CMS-Style_011_Character-Figure_Gemini_Male at (56.8%, 38.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_011_Character-Figure_Gemini_Male', 56.8, 38.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap importButton at (48.2%, 52.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importButton', 48.2, 52.6)
    with step("[Verify] descriptionLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel')
    with step("[Action] Tap Continue at (74.3%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 74.3, 52.2)
    with step("[Action] Tap btnAlbum at (77.2%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 77.2, 47.6)
    with step("[Action] Tap _AT at (10.4%, 82.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.4, 82.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (60.8%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 60.8, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap importLabel at (44.4%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importLabel', 44.4, 45.0)
    with step("[Action] Tap Continue at (79.7%, 13.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 79.7, 13.0)
    with step("[Action] Tap photoCell-6 at (66.2%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 66.2, 46.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Generate at (60.0%, 25.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 60.0, 25.0)
    with step("[Action] Tap I Agree at (54.0%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'I Agree', 54.0, 62.5)
    with step("[Verify] waitLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'waitLabel', appear_timeout=5, disappear_timeout=1200), 'waitLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnSave at (38.5%, 23.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSave', 38.5, 23.1)
    with step("[Action] Tap btnBack at (61.5%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 61.5, 61.5)
    with step("[Action] Tap Ok at (53.8%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Ok', 53.8, 75.0)
    with step("[Action] Tap Male at (72.2%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Male', 72.2, 75.0)
    with step("[Action] Tap Generate at (66.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 66.2, 50.0)
    with step("[Verify] In progress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'In progress', appear_timeout=5, disappear_timeout=1200), 'In progress did not appear within 5s or is still shown after 1200s'
    with step("[Verify] ArtisticAvatarResultCell-0 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-0')
    with step("[Verify] ArtisticAvatarResultCell-1 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-1')
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'imageView')
    with step("[Action] Tap ArtisticAvatarResultCell-0 at (57.3%, 46.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-0', 57.3, 46.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='resultCollectionView', container_w=430, container_h=110)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'imageView', expected_result='different', threshold=0.95)
    with step("[Action] Tap btnContinueEdit at (61.5%, 34.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnContinueEdit', 61.5, 34.6)
    with step("[Action] Tap photoPickerButton at (53.8%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton', 53.8, 61.5)
    with step("[Action] Tap btnAlbum at (69.0%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 69.0, 52.4)
    with step("[Action] Tap _AT at (10.0%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.0, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (42.3%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 42.3, 73.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (52.7%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 52.7, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until ic_artistic_avatar"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_artistic_avatar', direction='left', offset_start=(0.437, 0.454), offset_end=(0.181, 0.454), velocity=193)
    with step("[Action] Tap ic_artistic_avatar at (41.2%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_artistic_avatar', 41.2, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00147_main_G02_02_06_Step40' for GT comparison"):
        actions.capture_for_gt('00147_main_G02_02_06_Step40', AppiumBy.ACCESSIBILITY_ID, 'importButton', threshold=0.95)
    with step("[Action] Tap CMS-Style_1024_Clean_Flux_Female at (36.4%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_1024_Clean_Flux_Female', 36.4, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap importLabel at (16.7%, 27.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importLabel', 16.7, 27.5)
    with step("[Action] Tap Continue at (79.7%, 73.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 79.7, 73.9)
    with step("[Action] Tap photoCell-1 at (51.5%, 62.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 51.5, 62.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Generate at (53.8%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 53.8, 58.3)
    with step("[Verify] waitLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'waitLabel', appear_timeout=5, disappear_timeout=1200), 'waitLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnSave at (61.5%, 100.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSave', 61.5, 100.0)
    with step("[Action] Tap Generate More at (69.2%, 45.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate More', 69.2, 45.8)
    with step("[Verify] In progress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'In progress', appear_timeout=5, disappear_timeout=1200), 'In progress did not appear within 5s or is still shown after 1200s'
    with step("[Verify] ArtisticAvatarResultCell-0 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-0')
    with step("[Verify] ArtisticAvatarResultCell-1 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-1')
    with step("[Action] Tap btnSave at (38.5%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSave', 38.5, 76.9)
    with step("[Action] Tap btnBack at (42.3%, 34.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 42.3, 34.6)
    with step("[Action] Tap Generate at (62.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 62.5, 50.0)
    with step("[Verify] In progress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'In progress', appear_timeout=5, disappear_timeout=1200), 'In progress did not appear within 5s or is still shown after 1200s'
    with step("[Verify] ArtisticAvatarResultCell-0 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-0')
    with step("[Verify] ArtisticAvatarResultCell-1 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-1')
    with step("[Verify] ArtisticAvatarResultCell-2 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-2')
    with step("[Action] Tap btnContinueEdit at (69.2%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnContinueEdit', 69.2, 69.2)
    with step("[Action] Tap photoPickerButton at (76.9%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton', 76.9, 73.1)
    with step("[Action] Tap photoCell-1 at (27.7%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 27.7, 46.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Discard at (87.0%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 87.0, 70.8)
    with step("[Action] Tap ic_artistic_avatar at (67.6%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_artistic_avatar', 67.6, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap CMS-Style_1024_Clean_Flux_Female at (37.5%, 50.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_1024_Clean_Flux_Female', 37.5, 50.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap Generate at (43.8%, 45.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 43.8, 45.8)
    with step("[Verify] waitLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'waitLabel', appear_timeout=5, disappear_timeout=1200), 'waitLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnHome at (50.0%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 50.0, 42.3)
    with step("[Verify] Would you like to continue editing? is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Would you like to continue editing?')
    with step("[Action] Tap Cancel at (80.0%, 69.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 80.0, 69.6)
    with step("[Action] Tap btnStudio at (56.6%, 41.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnStudio', 56.6, 41.8)
    with step("[Action] Tap AI Art at (79.5%, 27.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Art', 79.5, 27.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap importLabel at (27.8%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importLabel', 27.8, 45.0)
    with step("[Action] Tap Continue at (47.3%, 30.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 47.3, 30.4)
    with step("[Action] Tap photoCell-1 at (50.8%, 47.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 50.8, 47.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Scroll until Avatar"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'titleCollectionViewCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Avatar', direction='left', offset_start=(0.693, 0.606), offset_end=(0.156, 0.606), velocity=316)
    with step("[Action] Tap Avatar at (50.7%, 40.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Avatar', 50.7, 40.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=33)
    with step("[Action] Scroll until CMS-Style_008_Female-African-American-02"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="styleContentView"]/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_008_Female-African-American-02', direction='down', offset_start=(0.419, 0.879), offset_end=(0.419, 0.191), velocity=369)
    with step("[Action] Tap CMS-Style_008_Female-African-American-02 at (48.9%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_008_Female-African-American-02', 48.9, 48.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=330)
    with step("[Action] Tap Generate at (62.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 62.5, 50.0)
    with step("[Verify] Please choose another photo is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Please choose another photo')
    with step("[Action] Tap OK at (96.7%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 96.7, 70.8)
    with step("[Action] Tap navBackButton at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 50.0, 50.0)
    with step("[Action] Tap btnHome at (46.1%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 46.1, 54.5)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
