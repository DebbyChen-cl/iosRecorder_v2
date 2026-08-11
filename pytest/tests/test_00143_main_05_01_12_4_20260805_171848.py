import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00143_main_05_01_12_4_20260805_171848")
def test_00143_main_05_01_12_4_20260805_171848(actions: DriverActions):
    with step("[Action] Tap btnSettings at (66.7%, 44.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 66.7, 44.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap //XCUIElementTypeImage[@name=\"SettingPageHelpCenterCell-1\"]/XCUIElementTypeOther[2] at (19.8%, 79.2%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="SettingPageHelpCenterCell-1"]/XCUIElementTypeOther[2]', 19.8, 79.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (16.3%, 34.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 16.3, 34.0)
    with step("[Action] Tap Free at (20.6%, 81.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 20.6, 81.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (52.4%, 73.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 52.4, 73.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (65.0%, 47.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 65.0, 47.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap btnBack at (53.6%, 61.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 53.6, 61.7)
    with step("[Action] Tap btnBack at (57.1%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 57.1, 48.9)
    with step("[Action] Tap Edit at (51.4%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 51.4, 56.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (71.1%, 59.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 71.1, 59.5)
    with step("[Action] Tap _AT at (6.5%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 6.5, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (53.1%, 83.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 53.1, 83.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Quick Actions at (50.4%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions', 50.4, 46.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_bg_blur at (47.1%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_bg_blur', 47.1, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap None at (68.3%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'None', 68.3, 45.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step16' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step16', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag centerSlider (56.1%,34.0%) → //XCUIElementTypeOther[@name=\"photodirector.BackgroundQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (26.0%,89.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 56.1, 34.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 26.0, 89.1, duration=1.0)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step18' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step18', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag centerSlider (11.7%,52.0%) → //XCUIElementTypeOther[@name=\"photodirector.BackgroundQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (77.2%,89.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 11.7, 52.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 77.2, 89.9, duration=1.0)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step20' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step20', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag centerSlider (52.3%,56.0%) → //XCUIElementTypeOther[@name=\"photodirector.BackgroundQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (24.7%,96.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 52.3, 56.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 24.7, 96.9, duration=1.0)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step22' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step22', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.90)
    with step("[Action] Drag centerSlider (8.4%,58.0%) → //XCUIElementTypeOther[@name=\"photodirector.BackgroundQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (75.8%,96.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.4, 58.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 75.8, 96.3, duration=1.0)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step24' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step24', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap exposureResetButton at (56.4%, 79.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'exposureResetButton', 56.4, 79.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Action] Tap saturationResetButton at (56.4%, 59.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'saturationResetButton', 56.4, 59.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step27' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step27', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Background at (93.5%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Background', 93.5, 40.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step29' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step29', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_bg_blur at (38.2%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_bg_blur', 38.2, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Blur at (53.7%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Blur', 53.7, 55.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Drag cpSlider (28.9%,50.0%) → //XCUIElementTypeOther[@name=\"photodirector.BackgroundQuickActionViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage (24.4%,96.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 28.9, 50.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', 24.4, 96.5, duration=1.0)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step33' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step33', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Drag cpSlider (9.2%,40.0%) → valueLabel (10.5%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 9.2, 40.0, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 10.5, 51.0, duration=1.0)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step35' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step35', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap intensityResetButton at (71.8%, 56.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton', 71.8, 56.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step37' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step37', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Circle at (46.3%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Circle', 46.3, 45.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step39' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step39', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Heart at (43.9%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Heart', 43.9, 75.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step41' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step41', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Sparkle at (61.0%, 35.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sparkle', 61.0, 35.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step43' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step43', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Star at (57.3%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Star', 57.3, 80.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step45' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step45', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Zoom at (40.2%, 35.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Zoom', 40.2, 35.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step47' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step47', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Radial at (64.6%, 20.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Radial', 64.6, 20.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step49' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step49', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (64.1%, 43.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 64.1, 43.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step51' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step51', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic edit redo n at (51.3%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n', 51.3, 53.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step53' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step53', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BackgroundQuickActionViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap Background at (7.4%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Background', 7.4, 30.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Verify] Capture '00143_main_05_01_12_4_Step55' for GT comparison"):
        actions.capture_for_gt('00143_main_05_01_12_4_Step55', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (88.5%, 30.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 88.5, 30.8)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
