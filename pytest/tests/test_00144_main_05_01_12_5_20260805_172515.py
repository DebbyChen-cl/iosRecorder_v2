import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00144_main_05_01_12_5_20260805_172515")
def test_00144_main_05_01_12_5_20260805_172515(actions: DriverActions):
    with step("[Action] Tap btnSettings at (42.4%, 38.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 42.4, 38.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap About at (51.0%, 39.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 51.0, 39.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (34.7%, 30.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 34.7, 30.0)
    with step("[Action] Tap Free at (67.6%, 76.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 67.6, 76.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (52.8%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 52.8, 57.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (55.0%, 63.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 55.0, 63.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap btnBack at (64.3%, 63.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 64.3, 63.8)
    with step("[Action] Tap btnBack at (60.7%, 59.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 60.7, 59.6)
    with step("[Action] Tap Edit at (40.0%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 40.0, 48.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (76.1%, 45.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 76.1, 45.2)
    with step("[Action] Tap _AT at (8.2%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.2, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-4 at (37.7%, 36.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4', 37.7, 36.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Quick Actions at (48.8%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions', 48.8, 62.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (70.6%, 39.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 70.6, 39.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '30'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '30')
    with step("[Verify] Capture '00144_main_05_01_12_5_Step16' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step16', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (31.6%,53.5%) → //XCUIElementTypeOther[@name=\"photodirector.RetouchQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (77.0%,96.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 31.6, 53.5, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 77.0, 96.8, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00144_main_05_01_12_5_Step19' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step19', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (93.4%,67.4%) → //XCUIElementTypeOther[@name=\"photodirector.RetouchQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (21.4%,97.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 93.4, 67.4, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 21.4, 97.1, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00144_main_05_01_12_5_Step22' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step22', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap intensityResetButton at (43.6%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton', 43.6, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] valueLabel text equals '30'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '30')
    with step("[Verify] Capture '00144_main_05_01_12_5_Step25' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step25', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (32.8%,46.5%) → valueLabel (6.9%,45.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 32.8, 46.5, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 6.9, 45.2, duration=1.0)
    with step("[Action] Tap Retouch at (93.5%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Retouch', 93.5, 38.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Verify] Capture '00144_main_05_01_12_5_Step28' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step28', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_beautify at (50.0%, 21.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 50.0, 21.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_conceal_portrait at (60.6%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 60.6, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Verify] Capture '00144_main_05_01_12_5_Step32' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step32', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (53.7%,48.8%) → //XCUIElementTypeOther[@name=\"photodirector.RetouchQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (25.1%,97.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 53.7, 48.8, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 25.1, 97.4, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00144_main_05_01_12_5_Step35' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step35', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (7.4%,79.1%) → valueLabel (17.2%,59.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.4, 79.1, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 17.2, 59.5, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00144_main_05_01_12_5_Step38' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step38', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap intensityResetButton at (43.6%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton', 43.6, 65.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Verify] Capture '00144_main_05_01_12_5_Step41' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step41', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Retouch at (9.1%, 24.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Retouch', 9.1, 24.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Verify] Capture '00144_main_05_01_12_5_Step43' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step43', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_beautify at (35.3%, 21.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 35.3, 21.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_eyebag_removal at (48.5%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_eyebag_removal', 48.5, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '25'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '25')
    with step("[Action] Drag cpSlider (30.7%,53.5%) → titleLabel (100.0%,52.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 30.7, 53.5, AppiumBy.ACCESSIBILITY_ID, 'titleLabel', 100.0, 52.4, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00144_main_05_01_12_5_Step49' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step49', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (7.8%,55.8%) → //XCUIElementTypeOther[@name=\"photodirector.RetouchQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (76.3%,97.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.8, 55.8, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 76.3, 97.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00144_main_05_01_12_5_Step52' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step52', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap intensityResetButton at (46.2%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton', 46.2, 70.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] valueLabel text equals '25'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '25')
    with step("[Verify] Capture '00144_main_05_01_12_5_Step55' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step55', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Retouch at (8.6%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Retouch', 8.6, 38.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (38.2%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 38.2, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_teeth_whiten_portrait at (57.6%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_teeth_whiten_portrait', 57.6, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (53.3%,41.9%) → //XCUIElementTypeOther[@name=\"photodirector.RetouchQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (22.8%,97.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 53.3, 41.9, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 22.8, 97.1, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00144_main_05_01_12_5_Step62' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step62', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (7.0%,51.2%) → //XCUIElementTypeOther[@name=\"photodirector.RetouchQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (76.7%,96.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.0, 51.2, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 76.7, 96.8, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00144_main_05_01_12_5_Step65' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step65', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap intensityResetButton at (56.4%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton', 56.4, 57.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Tap ic edit undo n at (59.0%, 41.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 59.0, 41.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00144_main_05_01_12_5_Step69' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step69', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic edit redo n at (61.5%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n', 61.5, 61.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00144_main_05_01_12_5_Step71' for GT comparison"):
        actions.capture_for_gt('00144_main_05_01_12_5_Step71', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.RetouchQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Retouch at (93.0%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Retouch', 93.0, 40.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap homeButton at (65.4%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 42.3)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
