import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00137_main_06_02_01_2_20260809_160221")
def test_00137_main_06_02_01_2_20260809_160221(actions: DriverActions):
    with step("[Action] Tap Edit at (45.7%, 72.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 45.7, 72.0)
    with step("[Action] Tap btnAlbum at (61.9%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 61.9, 47.6)
    with step("[Action] Tap _AT at (8.6%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.6, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (44.6%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 44.6, 70.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (53.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 53.5, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Live"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Live', direction='left', offset_start=(0.614, 0.392), offset_end=(0.237, 0.392), velocity=515)
    with step("[Action] Tap Live at (59.2%, 34.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Live', 59.2, 34.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Scroll until Animation"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'Animation', direction='left', offset_start=(0.358, 0.402), offset_end=(0.184, 0.402), velocity=73)
    with step("[Action] Tap Animation at (49.3%, 38.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Animation', 49.3, 38.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap Motion at (69.8%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Motion', 69.8, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationGPUPhotoAnimationMenuViewCollectionView', container_w=375, container_h=97)
    with step("[Action] Drag blackBackgroundView (36.5%,22.9%) → blackBackgroundView (73.7%,70.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 36.5, 22.9, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 73.7, 70.9, duration=1.0)
    with step("[Action] Tap btn_ok_n at (81.6%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 40.8)
    with step("[Verify] photodirector.AnimationPhotoExportViewController is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController')
    with step("[Action] Tap ic_gif_n at (73.3%, 69.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_gif_n', 73.3, 69.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoExportTypeViewCollectionView', container_w=430, container_h=80)
    with step("[Action] Tap navSaveButton at (63.6%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton', 63.6, 57.8)
    with step("[Action] Tap OK at (42.9%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 42.9, 66.7)
    with step("[Action] Dismiss subscription offer when present"):
        assert (
            actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=5)
            or not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=1)
        )
    with step("[Action] Tap //XCUIElementTypeScrollView[@name=\"animationScrollView\"]/XCUIElementTypeOther at (51.8%, 53.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="animationScrollView"]/XCUIElementTypeOther', 51.8, 53.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationScrollView', container_w=430, container_h=253)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step18' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step18', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="animationScrollView"]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeScrollView[@name=\"animationScrollView\"]/XCUIElementTypeOther at (54.8%, 53.8%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="animationScrollView"]/XCUIElementTypeOther', 54.8, 53.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationScrollView', container_w=430, container_h=253)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step20' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step20', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="animationScrollView"]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_16v9 at (53.6%, 49.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_16v9', 53.6, 49.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step22' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step22', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap navSaveButton at (61.4%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton', 61.4, 62.2)
    with step("[Action] Tap OK at (78.6%, 79.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 78.6, 79.2)
    with step("[Action] Dismiss promotional overlay when present"):
        assert (
            actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=5)
            or not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=1)
        )
    with step("[Action] Tap ic_square at (58.3%, 55.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_square', 58.3, 55.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step26' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step26', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap ic_3v4 at (58.3%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_3v4', 58.3, 70.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step28' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step28', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap ic_9v16 at (49.0%, 56.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_9v16', 49.0, 56.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=431, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step30' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step30', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap ic_4v3 at (51.5%, 52.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_4v3', 51.5, 52.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step32' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step32', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap Video at (55.4%, 26.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Video', 55.4, 26.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoExportTypeViewCollectionView', container_w=430, container_h=80)
    with step("[Action] Tap navSaveButton at (47.7%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton', 47.7, 55.6)
    with step("[Action] Dismiss subscription offer when present"):
        assert (
            actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=5)
            or not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=1)
        )
    with step("[Action] Tap navBackButton at (56.8%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 56.8, 55.6)
    with step("[Action] Tap //XCUIElementTypeScrollView[@name=\"animationScrollView\"]/XCUIElementTypeOther at (56.0%, 54.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="animationScrollView"]/XCUIElementTypeOther', 56.0, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationScrollView', container_w=430, container_h=253)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step38' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step38', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="animationScrollView"]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeScrollView[@name=\"animationScrollView\"]/XCUIElementTypeOther at (48.8%, 58.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="animationScrollView"]/XCUIElementTypeOther', 48.8, 58.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationScrollView', container_w=430, container_h=253)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step40' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step40', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="animationScrollView"]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_16v9 at (46.4%, 66.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_16v9', 46.4, 66.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step42' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step42', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap ic_square at (57.3%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_square', 57.3, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step44' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step44', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap navSaveButton at (45.5%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton', 45.5, 62.2)
    with step("[Action] Tap navHomeButton at (54.5%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton', 54.5, 55.6)
    with step("[Action] Tap Edit at (37.1%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 37.1, 64.0)
    with step("[Action] Tap photoCell-6 at (39.2%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 39.2, 53.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (52.1%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 52.1, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Live"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Live', direction='left', offset_start=(0.868, 0.32), offset_end=(0.186, 0.32), velocity=693)
    with step("[Action] Tap Live at (49.3%, 7.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Live', 49.3, 7.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Scroll until Animation"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'menuView', AppiumBy.ACCESSIBILITY_ID, 'Animation', direction='left', offset_start=(0.656, 0.443), offset_end=(0.214, 0.443), velocity=542)
    with step("[Action] Tap Animation at (39.1%, 17.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Animation', 39.1, 17.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap Motion at (50.8%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Motion', 50.8, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationGPUPhotoAnimationMenuViewCollectionView', container_w=375, container_h=97)
    with step("[Action] Drag blackBackgroundView (23.0%,33.8%) → blackBackgroundView (83.0%,62.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 23.0, 33.8, AppiumBy.ACCESSIBILITY_ID, 'blackBackgroundView', 83.0, 62.6, duration=1.0)
    with step("[Action] Tap btn_ok_n at (83.7%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 83.7, 49.0)
    with step("[Action] Dismiss promotional overlay when present"):
        assert (
            not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=2)
            or actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        )
    with step("[Action] Tap ic_square at (54.2%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_square', 54.2, 58.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Action] Tap 1080P at (71.4%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '1080P', 71.4, 71.4)
    with step("[Action] Tap navSaveButton at (72.7%, 28.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton', 72.7, 28.9)
    with step("[Action] Tap navBackButton at (52.3%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 52.3, 46.7)
    with step("[Action] Tap 2K at (9.5%, 81.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '2K', 9.5, 81.0)
    with step("[Action] Tap navSaveButton at (65.9%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton', 65.9, 57.8)
    with step("[Action] Dismiss promotional overlay when present"):
        assert (
            not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=2)
            or actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        )
    with step("[Action] Tap navBackButton at (40.9%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 40.9, 60.0)
    with step("[Action] Tap button_4K at (70.9%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_4K', 70.9, 33.3)
    with step("[Action] Tap navSaveButton at (63.6%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton', 63.6, 46.7)
    with step("[Action] Dismiss subscription offer when present"):
        assert (
            actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=5)
            or not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=1)
        )
    with step("[Action] Tap navBackButton at (54.5%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 54.5, 62.2)
    with step("[Verify] button_720P is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'button_720P')
    with step("[Action] Tap button_720P at (60.8%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'button_720P', 60.8, 83.3)
    with step("[Action] Tap navSaveButton at (72.7%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton', 72.7, 62.2)
    with step("[Action] Dismiss promotional overlay when present"):
        assert (
            not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=5)
            or (
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
                and actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=5)
            )
        )
    with step("[Action] Tap navBackButton at (52.3%, 22.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 52.3, 22.2)
    with step("[Action] Tap ic_16v9 at (61.5%, 56.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_16v9', 61.5, 56.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step70' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step70', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap ic_square at (56.2%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_square', 56.2, 53.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step72' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step72', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap ic_3v4 at (49.0%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_3v4', 49.0, 61.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step74' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step74', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap ic_9v16 at (56.2%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_9v16', 56.2, 67.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=431, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step76' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step76', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap ic_4v3 at (45.4%, 63.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_4v3', 45.4, 63.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step78' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step78', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap ic_ig_n at (55.6%, 60.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_ig_n', 55.6, 60.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoExportTypeViewCollectionView', container_w=430, container_h=80)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step80' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step80', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap ic_IG9v16 at (49.0%, 41.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_IG9v16', 49.0, 41.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step82' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step82', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap ic_IG4v5 at (51.5%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_IG4v5', 51.5, 40.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step84' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step84', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap ic_fb_n at (60.0%, 67.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_fb_n', 60.0, 67.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoExportTypeViewCollectionView', container_w=430, container_h=80)
    with step("[Action] Tap ic_FBCover at (41.7%, 64.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_FBCover', 41.7, 64.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step87' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step87', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap ic_FB1v1 at (36.5%, 33.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_FB1v1', 36.5, 33.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animationPhotoAspectRatioViewCollectionView', container_w=430, container_h=107)
    with step("[Verify] Capture '00137_main_06_02_01_2_Step89' for GT comparison"):
        actions.capture_for_gt('00137_main_06_02_01_2_Step89', AppiumBy.ACCESSIBILITY_ID, 'photodirector.AnimationPhotoExportViewController', threshold=0.95)
    with step("[Action] Tap 4K at (54.5%, 90.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '4K', 54.5, 90.5)
    with step("[Action] Tap navSaveButton at (50.0%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton', 50.0, 48.9)
    with step("[Action] Dismiss subscription offer when present"):
        assert (
            not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=5)
            or (
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
                and actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnClose', timeout=5)
            )
        )
    with step("[Action] Tap btnShareIG at (54.7%, 35.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareIG', 54.7, 35.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=786)
    with step("[Verify] Instagram is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="Instagram"]')
    with step("[Action] Tap //XCUIElementTypeApplication[@name=\"Instagram\"]/XCUIElementTypeWindow/XCUIElementTypeOther[1] at (5.1%, 4.2%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="Instagram"]/XCUIElementTypeWindow/XCUIElementTypeOther[1]', 5.1, 4.2)
    with step("[Action] Tap btnShareFB at (50.0%, 31.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB', 50.0, 31.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=786)
    with step("[Verify] New post is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'New post')
    with step("[Action] Tap composer-left-button at (68.2%, 36.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'composer-left-button', 68.2, 36.5)
    with step("[Action] Tap Discard at (61.5%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 61.5, 46.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Discard post?"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=270, container_h=45)
    with step("[Action] Tap btnShareMore at (52.1%, 42.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareMore', 52.1, 42.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=786)
    with step("[Action] Tap PopoverDismissRegion at (85.3%, 76.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PopoverDismissRegion', 85.3, 76.0)
    with step("[Action] Tap Cancel at (83.1%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 83.1, 45.5)
    with step("[Action] Tap navHomeButton at (77.3%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton', 77.3, 57.8)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
