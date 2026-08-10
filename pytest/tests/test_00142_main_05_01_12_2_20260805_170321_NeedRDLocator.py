import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00142_main_05_01_12_2_20260805_170321")
def test_00142_main_05_01_12_2_20260805_170321(actions: DriverActions):
    with step("[Action] Tap btnSettings at (63.6%, 61.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 63.6, 61.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap About at (45.1%, 0.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 45.1, 0.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (28.6%, 22.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 28.6, 22.0)
    with step("[Action] Tap Free at (32.4%, 85.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 32.4, 85.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (48.6%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 48.6, 69.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (60.0%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 60.0, 61.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap btnBack at (57.1%, 61.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 57.1, 61.7)
    with step("[Action] Tap btnBack at (39.3%, 61.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 39.3, 61.7)
    with step("[Action] Tap Edit at (45.7%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 45.7, 40.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (75.6%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 75.6, 47.6)
    with step("[Action] Tap _AT at (7.2%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.2, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (46.9%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 46.9, 46.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Quick Actions at (54.4%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions', 54.4, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_foreground at (61.8%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_foreground', 61.8, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step15' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step15', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag centerSlider (92.9%,40.0%) → //XCUIElementTypeOther[@name=\"photodirector.SubjectQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (25.3%,89.3%)"):
            actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 92.9, 40.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 25.3, 89.3, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00142_main_05_01_12_2_Step18' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step18', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag centerSlider (8.8%,50.0%) → //XCUIElementTypeOther[@name=\"photodirector.SubjectQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (76.0%,89.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.8, 50.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 76.0, 89.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00142_main_05_01_12_2_Step21' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step21', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag centerSlider (51.9%,42.0%) → //XCUIElementTypeOther[@name=\"photodirector.SubjectQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (23.3%,96.0%)"):
            actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.9, 42.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 23.3, 96.0, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00142_main_05_01_12_2_Step24' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step24', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag centerSlider (9.6%,62.0%) → valueLabel (12.3%,61.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 9.6, 62.0, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 12.3, 61.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00142_main_05_01_12_2_Step27' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step27', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Subject at (93.7%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Subject', 93.7, 42.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step29' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step29', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (64.1%, 43.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 64.1, 43.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step31' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step31', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit redo n at (59.0%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n', 59.0, 61.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step33' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step33', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_foreground at (58.8%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_foreground', 58.8, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Light at (54.9%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Light', 54.9, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step36' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step36', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (29.7%,48.0%) → //XCUIElementTypeOther[@name=\"photodirector.SubjectQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (25.3%,97.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 29.7, 48.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 25.3, 97.2, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00142_main_05_01_12_2_Step39' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step39', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (9.6%,54.0%) → //XCUIElementTypeOther[@name=\"photodirector.SubjectQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (75.3%,96.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 9.6, 54.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 75.3, 96.3, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00142_main_05_01_12_2_Step42' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step42', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Pop at (58.5%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pop', 58.5, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step44' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step44', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (31.4%,48.0%) → //XCUIElementTypeOther[@name=\"photodirector.SubjectQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (24.7%,97.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 31.4, 48.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 24.7, 97.1, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00142_main_05_01_12_2_Step47' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step47', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (8.4%,52.0%) → //XCUIElementTypeOther[@name=\"photodirector.SubjectQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (77.2%,97.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 8.4, 52.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 77.2, 97.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00142_main_05_01_12_2_Step50' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step50', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Cool at (64.6%, 35.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cool', 64.6, 35.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step52' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step52', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Warm at (35.4%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Warm', 35.4, 40.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step54' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step54', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Vibrant at (73.2%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Vibrant', 73.2, 70.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step56' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step56', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Glow at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Glow', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step58' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step58', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (69.2%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 69.2, 46.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step60' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step60', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic edit redo n at (74.4%, 56.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n', 74.4, 56.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step62' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step62', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (29.7%,60.0%) → //XCUIElementTypeOther[@name=\"photodirector.SubjectQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (75.6%,96.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 29.7, 60.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 75.6, 96.8, duration=1.0)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step64' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step64', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap intensityResetButton at (41.0%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton', 41.0, 53.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step66' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step66', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.SubjectQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Subject at (94.4%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Subject', 94.4, 46.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic edit undo n at (79.5%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 79.5, 61.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step69' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step69', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_foreground at (64.7%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_foreground', 64.7, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Light at (56.1%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Light', 56.1, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Subject at (7.4%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Subject', 7.4, 42.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Verify] Capture '00142_main_05_01_12_2_Step73' for GT comparison"):
        actions.capture_for_gt('00142_main_05_01_12_2_Step73', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (42.3%, 34.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 42.3, 34.6)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
