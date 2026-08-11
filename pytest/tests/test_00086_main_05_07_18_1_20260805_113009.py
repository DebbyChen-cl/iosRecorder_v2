import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00086_main_05_07_18_1_20260805_113009")
def test_00086_main_05_07_18_1_20260805_113009(actions: DriverActions):
    with step("[Action] Tap Edit at (77.1%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 77.1, 64.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (69.0%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 69.0, 71.4)
    with step("[Action] Tap _AT at (7.5%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.5, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (33.1%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 33.1, 69.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (55.4%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 55.4, 51.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (60.6%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 60.6, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Scroll until ic_plumpness"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'photoEditFeatureCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_plumpness', direction='left', offset_start=(0.744, 0.402), offset_end=(0.2, 0.402), velocity=464)
    with step("[Action] Tap ic_plumpness at (39.4%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_plumpness', 39.4, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00086_main_05_07_18_1_Step09' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step09', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.79)
    with step("[Action] Tap Toggle_on_withoutText at (68.0%, 25.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Toggle_on_withoutText', 68.0, 25.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] Capture '00086_main_05_07_18_1_Step11' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step11', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Toggle_off_withoutText at (58.0%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Toggle_off_withoutText', 58.0, 41.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (51.0%,47.6%) → slider (1.4%,46.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 51.0, 47.6, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.4, 46.3, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step16' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step16', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.9%,50.0%) → slider (99.4%,46.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.9, 50.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.4, 46.3, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step19' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step19', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_tear_troughs_n at (27.5%, 42.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_tear_troughs_n', 27.5, 42.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '80'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '80')
    with step("[Action] Drag cpSlider (76.2%,50.0%) → slider (2.5%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 76.2, 50.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.5, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step24' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step24', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.7%,54.8%) → slider (98.9%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.7, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.9, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step27' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step27', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_Cheek_apple_n at (55.0%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_Cheek_apple_n', 55.0, 65.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '75'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '75')
    with step("[Action] Drag cpSlider (72.0%,59.5%) → slider (1.4%,61.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 72.0, 59.5, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.4, 61.0, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step32' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step32', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.6%,52.4%) → slider (99.4%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.6, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.4, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step35' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step35', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_Cheek_n at (65.0%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_Cheek_n', 65.0, 70.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '45'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '45')
    with step("[Action] Drag cpSlider (46.5%,57.1%) → slider (1.7%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 46.5, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.7, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step40' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step40', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.9%,66.7%) → slider (98.6%,65.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.9, 66.7, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.6, 65.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step43' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step43', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_nasal_base_n at (22.5%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_nasal_base_n', 22.5, 55.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '75'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '75')
    with step("[Action] Drag cpSlider (73.1%,69.0%) → slider (1.4%,63.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 73.1, 69.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.4, 63.4, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step48' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step48', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (4.8%,57.1%) → slider (98.9%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 4.8, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.9, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step51' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step51', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_eye_smile_n at (60.0%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_eye_smile_n', 60.0, 65.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (50.7%,52.4%) → slider (3.7%,61.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 50.7, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 3.7, 61.0, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step56' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step56', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.0%,57.1%) → slider (99.2%,61.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.0, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.2, 61.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step59' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step59', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_eye_sockets_n at (50.0%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_eye_sockets_n', 50.0, 70.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (49.6%,52.4%) → slider (2.5%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 49.6, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.5, 53.7, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step64' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step64', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (3.9%,54.8%) → slider (99.4%,65.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 3.9, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.4, 65.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step67' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step67', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_eyebrow_arch_n at (65.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_eyebrow_arch_n', 65.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '30'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '30')
    with step("[Action] Drag cpSlider (32.2%,59.5%) → slider (2.8%,63.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 32.2, 59.5, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.8, 63.4, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step72' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step72', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.4%,61.9%) → slider (98.6%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.4, 61.9, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.6, 58.5, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step75' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step75', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_chin_n at (47.5%, 32.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_chin_n', 47.5, 32.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '60'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '60')
    with step("[Action] Drag cpSlider (59.9%,59.5%) → //XCUIElementTypeOther[@name=\"photodirector.PlumpnessViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther (43.9%,34.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 59.9, 59.5, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther', 43.9, 34.8, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step80' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step80', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.2%,54.8%) → slider (99.4%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.2, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.4, 56.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step83' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step83', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_mouth_corner_n at (52.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_mouth_corner_n', 52.5, 60.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '70'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '70')
    with step("[Action] Drag cpSlider (69.2%,47.6%) → slider (2.5%,61.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 69.2, 47.6, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.5, 61.0, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step88' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step88', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.7%,54.8%) → slider (98.9%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.7, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.9, 53.7, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step91' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step91', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_undo at (63.3%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 63.3, 59.2)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step94' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step94', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_redo at (55.1%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 55.1, 49.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00086_main_05_07_18_1_Step97' for GT comparison"):
        actions.capture_for_gt('00086_main_05_07_18_1_Step97', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.PlumpnessViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (81.6%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 42.9)
    with step("[Action] Tap btnClose at (48.4%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 48.4, 51.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (26.5%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 26.5, 44.9)
    with step("[Action] Tap btn_cancel_n at (28.6%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 28.6, 28.6)
    with step("[Action] Tap homeButton at (65.4%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 76.9)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
