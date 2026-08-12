import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00145_main_05_01_12_6_20260805_173349")
def test_00145_main_05_01_12_6_20260805_173349(actions: DriverActions):
    with step("[Action] Tap Edit at (60.0%, 28.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 60.0, 28.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (67.5%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 67.5, 47.6)
    with step("[Action] Tap BG at (6.8%, 78.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'BG', 6.8, 78.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (12.3%, 79.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 12.3, 79.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Quick Actions at (55.2%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions', 55.2, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_preset at (57.6%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_preset', 57.6, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Food at (38.1%, 47.8%)"):
        actions.tap_within_element(
            AppiumBy.ACCESSIBILITY_ID, 'Food', 38.1, 47.8,
            container_by=AppiumBy.XPATH,
            container_value='//XCUIElementTypeOther[@name="menuView"]/XCUIElementTypeCollectionView[@name="ScrollableMenuView"]',
            container_w=332, container_h=46)
    with step("[Action] Tap Food 01 at (53.2%, 73.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Food 01', 53.2, 73.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step09' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step09', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Verify] valueLabel text equals '70'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '70')
    with step("[Action] Drag cpSlider (66.8%,48.0%) → slider (98.9%,46.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 66.8, 48.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.9, 46.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00145_main_05_01_12_6_Step13' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step13', AppiumBy.ACCESSIBILITY_ID, 'Food 01, Scenery, Food, Background, Auto', threshold=0.95)
    with step("[Action] Drag cpSlider (94.1%,46.0%) → sliderView (24.2%,46.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 94.1, 46.0, AppiumBy.ACCESSIBILITY_ID, 'sliderView', 24.2, 46.9, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00145_main_05_01_12_6_Step16' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step16', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Food 02 at (49.5%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Food 02', 49.5, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step18' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step18', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"PresetQuickActionFilterCell-2\"]/XCUIElementTypeImage at (21.0%, 63.1%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="PresetQuickActionFilterCell-2"]/XCUIElementTypeImage', 21.0, 63.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step20' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step20', AppiumBy.ACCESSIBILITY_ID, 'Food 04, Food 02, General, Outdoor, Food', threshold=0.95)
    with step("[Action] Tap Food 04 at (38.7%, 73.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Food 04', 38.7, 73.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step22' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step22', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Presets at (7.7%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Presets', 7.7, 46.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap photoPickerButton at (65.4%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton', 65.4, 53.8)
    with step("[Action] Tap photoCell-2 at (14.6%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 14.6, 59.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Try First at (55.7%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try First', 55.7, 66.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Action] Tap ic_preset at (76.5%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_preset', 76.5, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Indoor at (72.2%, 58.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Indoor', 72.2, 58.7)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step29' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step29', AppiumBy.ACCESSIBILITY_ID, 'Outdoor 04, Outdoor 02, General, Indoor, Presets, Auto', threshold=0.95)
    with step("[Action] Tap Indoor 01 at (55.9%, 73.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Indoor 01', 55.9, 73.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Drag cpSlider (67.2%,56.0%) → valueLabel (12.3%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 67.2, 56.0, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 12.3, 53.1, duration=1.0)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step32' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step32', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (93.4%,60.0%) → slider (1.1%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 93.4, 60.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.1, 55.1, duration=1.0)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step34' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step34', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Indoor 02 at (45.0%, 63.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Indoor 02', 45.0, 63.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step36' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step36', AppiumBy.ACCESSIBILITY_ID, 'Indoor 04, Indoor 02, General, Outdoor, Food', threshold=0.95)
    with step("[Action] Tap Indoor 03 at (36.0%, 56.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Indoor 03', 36.0, 56.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step38' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step38', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Indoor 04 at (57.1%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Indoor 04', 57.1, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step40' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step40', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Indoor 05 at (26.8%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Indoor 05', 26.8, 36.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step42' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step42', AppiumBy.ACCESSIBILITY_ID, 'General, Outdoor, Food', threshold=0.95)
    with step("[Action] Tap Indoor 06 at (43.2%, 63.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Indoor 06', 43.2, 63.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step44' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step44', AppiumBy.ACCESSIBILITY_ID, 'Indoor 05, Indoor 06, Indoor 04, General, Outdoor, Food', threshold=0.95)
    with step("[Action] Tap Presets at (6.7%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Presets', 6.7, 40.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap photoPickerButton at (30.8%, 34.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton', 30.8, 34.6)
    with step("[Action] Tap photoCell-3 at (56.9%, 31.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3', 56.9, 31.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap ic_preset at (39.4%, 84.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_preset', 39.4, 84.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Outdoor at (61.8%, 58.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Outdoor', 61.8, 58.7)
    with step("[Action] Tap Outdoor 01 at (59.5%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 01', 59.5, 40.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Drag cpSlider (67.5%,52.0%) → slider (1.5%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 67.5, 52.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.5, 49.0, duration=1.0)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step52' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step52', AppiumBy.ACCESSIBILITY_ID, 'General, Indoor, Presets, Subject', threshold=0.95)
    with step("[Action] Drag cpSlider (7.4%,60.0%) → slider (98.5%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.4, 60.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.5, 57.1, duration=1.0)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step54' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step54', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Outdoor 02 at (64.9%, 73.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 02', 64.9, 73.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step56' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step56', AppiumBy.ACCESSIBILITY_ID, 'Outdoor 04, Outdoor 02, General, Outdoor, Food', threshold=0.95)
    with step("[Action] Tap Outdoor 03 at (66.7%, 86.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 03', 66.7, 86.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step58' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step58', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Outdoor 04 at (30.4%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 04', 30.4, 70.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step60' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step60', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Outdoor 05 at (46.4%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 05', 46.4, 46.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step62' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step62', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Outdoor 06 at (58.9%, 56.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 06', 58.9, 56.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step64' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step64', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Outdoor 07 at (60.7%, 23.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 07', 60.7, 23.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step66' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step66', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Outdoor 08 at (46.4%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 08', 46.4, 70.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step68' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step68', AppiumBy.ACCESSIBILITY_ID, 'Outdoor 09, Outdoor 07, General, Outdoor, Food', threshold=0.95)
    with step("[Action] Tap Outdoor 09 at (54.1%, 63.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 09', 54.1, 63.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step70' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step70', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Presets at (6.5%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Presets', 6.5, 46.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap photoPickerButton at (65.4%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton', 65.4, 65.4)
    with step("[Action] Tap photoCell-1 at (23.1%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 23.1, 80.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap ic_preset at (39.4%, 84.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_preset', 39.4, 84.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Scenery at (66.2%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Scenery', 66.2, 56.5)
    with step("[Action] Tap Scenery 01 at (58.6%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Scenery 01', 58.6, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Drag cpSlider (69.4%,54.0%) → slider (1.9%,63.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 69.4, 54.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.9, 63.3, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00145_main_05_01_12_6_Step79' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step79', AppiumBy.ACCESSIBILITY_ID, 'General, Indoor, Presets, Subject', threshold=0.95)
    with step("[Action] Drag cpSlider (6.6%,50.0%) → slider (98.9%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.6, 50.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.9, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00145_main_05_01_12_6_Step82' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step82', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Scenery 02 at (59.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Scenery 02', 59.5, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step84' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step84', AppiumBy.ACCESSIBILITY_ID, 'Scenery 04, Scenery 02, General, Outdoor, Food', threshold=0.95)
    with step("[Action] Tap Scenery 03 at (50.5%, 86.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Scenery 03', 50.5, 86.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step86' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step86', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Scenery 04 at (46.4%, 63.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Scenery 04', 46.4, 63.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step88' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step88', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Scenery 05 at (27.7%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Scenery 05', 27.7, 36.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step90' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step90', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Scenery 06 at (58.9%, 73.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Scenery 06', 58.9, 73.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step92' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step92', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Scenery 07 at (41.1%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Scenery 07', 41.1, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step94' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step94', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Scenery 08 at (44.6%, 73.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Scenery 08', 44.6, 73.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step96' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step96', AppiumBy.ACCESSIBILITY_ID, 'Scenery 09, Scenery 07, General, Outdoor, Food', threshold=0.95)
    with step("[Action] Tap Scenery 09 at (31.5%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Scenery 09', 31.5, 36.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step98' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step98', AppiumBy.ACCESSIBILITY_ID, 'Scenery 09, Scenery 07, General, Outdoor, Food', threshold=0.95)
    with step("[Action] Tap Presets at (8.8%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Presets', 8.8, 34.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_preset at (64.7%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_preset', 64.7, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap General 01 at (66.7%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'General 01', 66.7, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Drag cpSlider (68.6%,50.0%) → slider (1.9%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 68.6, 50.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.9, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00145_main_05_01_12_6_Step104' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step104', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (7.7%,48.0%) → slider (98.9%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.7, 48.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.9, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00145_main_05_01_12_6_Step107' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step107', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap General 02 at (48.6%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'General 02', 48.6, 36.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step109' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step109', AppiumBy.ACCESSIBILITY_ID, 'General 02, General, Outdoor, Food', threshold=0.95)
    with step("[Action] Tap General 03 at (59.5%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'General 03', 59.5, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00145_main_05_01_12_6_Step111' for GT comparison"):
        actions.capture_for_gt('00145_main_05_01_12_6_Step111', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PresetQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Presets at (94.0%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Presets', 94.0, 40.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap btnClose at (61.3%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 61.3, 64.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap Presets at (7.4%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Presets', 7.4, 40.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap homeButton at (88.5%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 88.5, 76.9)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
