import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00056_main_05_04a_03_2_20260804_164032")
def test_00056_main_05_04a_03_2_20260804_164032(actions: DriverActions):
    with step("[Action] Tap Edit at (40.0%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 40.0, 60.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (80.7%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 80.7, 57.1)
    with step("[Action] Tap _AT at (4.7%, 100.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 4.7, 100.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (56.9%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 56.9, 53.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (71.1%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 71.1, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until ic_mosaic"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_mosaic', direction='left', offset_start=(0.788, 0.505), offset_end=(0.212, 0.505), velocity=508)
    with step("[Action] Tap ic_mosaic at (38.2%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_mosaic', 38.2, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step08' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step08', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag cpSlider (30.6%,46.0%) → valueLabel (4.6%,46.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 30.6, 46.0, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 4.6, 46.9, duration=1.0)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step10' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step10', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag cpSlider (91.5%,46.0%) → strengthSlider (23.7%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 91.5, 46.0, AppiumBy.ACCESSIBILITY_ID, 'strengthSlider', 23.7, 49.0, duration=1.0)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step12' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step12', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Person at (63.7%, 67.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Person', 63.7, 67.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step14' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step14', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Background at (66.1%, 64.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Background', 66.1, 64.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step16' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step16', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (56.0%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 56.0, 30.6)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step18' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step18', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_redo at (76.0%, 18.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 76.0, 18.4)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step20' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step20', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Off at (38.9%, 64.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Off', 38.9, 64.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step22' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step22', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (36.7%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 36.7, 38.8)
    with step("[Action] Tap photoPickerButton at (19.2%, 80.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton', 19.2, 80.8)
    with step("[Action] Tap btnAlbum at (78.7%, 64.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 78.7, 64.3)
    with step("[Action] Tap _AT at (8.2%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.2, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-4 at (30.8%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4', 30.8, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap ic_mosaic at (50.0%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_mosaic', 50.0, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step29' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step29', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CircleCheckMenuCell-0\"]/XCUIElementTypeImage at (50.0%, 37.1%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CircleCheckMenuCell-0"]/XCUIElementTypeImage', 50.0, 37.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='enableMenuItemCollectionView', container_w=430, container_h=57)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step31' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step31', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Person at (52.5%, 55.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Person', 52.5, 55.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step33' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step33', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CircleCheckMenuCell-0\"]/XCUIElementTypeImage at (63.9%, 85.7%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CircleCheckMenuCell-0"]/XCUIElementTypeImage', 63.9, 85.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='enableMenuItemCollectionView', container_w=430, container_h=57)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step35' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step35', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Background at (60.0%, 76.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Background', 60.0, 76.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step37' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step37', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Person at (53.8%, 67.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Person', 53.8, 67.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step39' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step39', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CircleCheckMenuCell-1\"]/XCUIElementTypeImage[1] at (41.7%, 51.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CircleCheckMenuCell-1"]/XCUIElementTypeImage[1]', 41.7, 51.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='enableMenuItemCollectionView', container_w=430, container_h=57)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step41' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step41', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CircleCheckMenuCell-0\"]/XCUIElementTypeImage[1] at (50.0%, 71.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CircleCheckMenuCell-0"]/XCUIElementTypeImage[1]', 50.0, 71.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='enableMenuItemCollectionView', container_w=430, container_h=57)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step43' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step43', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CircleCheckMenuCell-0\"]/XCUIElementTypeImage at (58.3%, 60.0%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CircleCheckMenuCell-0"]/XCUIElementTypeImage', 58.3, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='enableMenuItemCollectionView', container_w=430, container_h=57)
    with step("[Action] Tap btn_ok_n at (81.6%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 42.9)
    with step("[Verify] Capture '00056_main_05_04a_03_2_Step46' for GT comparison"):
        actions.capture_for_gt('00056_main_05_04a_03_2_Step46', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (84.6%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 84.6, 73.1)
    with step("[Action] Tap Discard at (52.2%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 52.2, 58.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
