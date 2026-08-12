import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00212_makeup_looks_20260811_174734")
def test_00212_makeup_looks_20260811_174734(actions: DriverActions):
    with step("[Action] Tap Edit at (54.3%, 76.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 54.3, 76.0)
    with step("[Action] Tap btnAlbum at (94.4%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 94.4, 61.9)
    with step("[Action] Tap Sample Photos at (24.7%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 24.7, 56.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap PhDM_example_3 at (65.4%, 50.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_3', 65.4, 50.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (29.7%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 29.7, 44.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap Makeup at (42.3%, 34.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Makeup', 42.3, 34.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00212_makeup_looks_Step07' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step07', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Daily at (46.5%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Daily', 46.5, 47.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '71'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '71')
    with step("[Action] Drag cpSlider (69.7%,52.4%) → slider (3.1%,61.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 69.7, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 3.1, 61.0, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step12' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step12', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.9%,52.4%) → slider (98.3%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.9, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.3, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step15' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step15', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Chestnut at (67.6%, 38.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Chestnut', 67.6, 38.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '76'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '76')
    with step("[Action] Drag cpSlider (74.8%,57.1%) → slider (2.8%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 74.8, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.8, 53.7, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step20' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step20', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (4.5%,50.0%) → //XCUIElementTypeOther[@name=\"photodirector.MakeupViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5] (82.8%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 4.5, 50.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]', 82.8, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step23' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step23', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Neutral at (69.4%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Neutral', 69.4, 57.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '62'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '62')
    with step("[Action] Drag cpSlider (60.8%,52.4%) → slider (1.4%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 60.8, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.4, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step28' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step28', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.2%,57.1%) → slider (100.0%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.2, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 100.0, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step31' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step31', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Lavish at (43.1%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Lavish', 43.1, 42.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=431, container_h=88)
    with step("[Verify] valueLabel text equals '76'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '76')
    with step("[Action] Drag cpSlider (70.3%,45.2%) → slider (0.6%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 70.3, 45.2, AppiumBy.ACCESSIBILITY_ID, 'slider', 0.6, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step36' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step36', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.6%,54.8%) → slider (98.3%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.6, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.3, 53.7, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step39' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step39', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Peach at (47.2%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Peach', 47.2, 28.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '83'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '83')
    with step("[Action] Drag cpSlider (81.0%,54.8%) → slider (2.8%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 81.0, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.8, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step44' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step44', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.9%,54.8%) → slider (97.7%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.9, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 97.7, 58.5, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step47' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step47', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Charming at (38.9%, 76.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Charming', 38.9, 76.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=431, container_h=88)
    with step("[Verify] valueLabel text equals '83'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '83')
    with step("[Action] Drag cpSlider (80.7%,57.1%) → slider (3.1%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 80.7, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 3.1, 56.1, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step52' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step52', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.3%,54.8%) → slider (98.3%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.3, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.3, 53.7, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step55' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step55', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Tender at (56.9%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Tender', 56.9, 52.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '83'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '83')
    with step("[Action] Drag cpSlider (79.6%,42.9%) → slider (2.8%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 79.6, 42.9, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.8, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step60' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step60', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.4%,59.5%) → slider (97.5%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.4, 59.5, AppiumBy.ACCESSIBILITY_ID, 'slider', 97.5, 58.5, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step63' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step63', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Aesthetic at (76.4%, 81.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Aesthetic', 76.4, 81.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=431, container_h=88)
    with step("[Verify] valueLabel text equals '83'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '83')
    with step("[Action] Drag cpSlider (80.4%,57.1%) → slider (2.8%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 80.4, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.8, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step68' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step68', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (7.6%,50.0%) → slider (99.2%,46.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.6, 50.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.2, 46.3, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step71' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step71', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Bright at (59.7%, 76.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Bright', 59.7, 76.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '76'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '76')
    with step("[Action] Drag cpSlider (74.2%,50.0%) → slider (3.4%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 74.2, 50.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 3.4, 53.7, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step76' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step76', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.9%,38.1%) → slider (97.2%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.9, 38.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 97.2, 53.7, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step79' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step79', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Smoky at (63.9%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Smoky', 63.9, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '83'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '83')
    with step("[Action] Drag cpSlider (80.4%,54.8%) → slider (3.1%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 80.4, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 3.1, 53.7, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step84' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step84', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.4%,45.2%) → slider (96.3%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.4, 45.2, AppiumBy.ACCESSIBILITY_ID, 'slider', 96.3, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step87' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step87', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Orange at (83.3%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Orange', 83.3, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '76'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '76')
    with step("[Action] Drag cpSlider (73.4%,57.1%) → slider (2.5%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 73.4, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.5, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step92' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step92', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.4%,54.8%) → slider (99.7%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.4, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.7, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step95' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step95', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Glowy at (33.3%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Glowy', 33.3, 71.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '62'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '62')
    with step("[Action] Drag cpSlider (60.8%,57.1%) → slider (0.6%,43.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 60.8, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 0.6, 43.9, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step100' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step100', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (7.3%,42.9%) → slider (99.4%,43.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.3, 42.9, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.4, 43.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step103' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step103', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Elegant at (86.1%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Elegant', 86.1, 28.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '90'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '90')
    with step("[Verify] Capture '00212_makeup_looks_Step106' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step106', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (84.9%,54.8%) → slider (2.0%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 84.9, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.0, 58.5, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step109' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step109', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (7.3%,59.5%) → //XCUIElementTypeOther[@name=\"photodirector.MakeupViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5] (82.3%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.3, 59.5, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]', 82.3, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step112' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step112', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Spring at (50.0%, 38.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Spring', 50.0, 38.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '90'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '90')
    with step("[Action] Drag cpSlider (85.2%,47.6%) → slider (3.4%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 85.2, 47.6, AppiumBy.ACCESSIBILITY_ID, 'slider', 3.4, 53.7, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step117' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step117', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.7%,59.5%) → //XCUIElementTypeOther[@name=\"photodirector.MakeupViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5] (82.3%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.7, 59.5, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]', 82.3, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step120' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step120', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Vitality at (59.2%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Vitality', 59.2, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '90'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '90')
    with step("[Action] Drag cpSlider (88.0%,38.1%) → slider (2.3%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 88.0, 38.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.3, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step125' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step125', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.3%,47.6%) → //XCUIElementTypeOther[@name=\"photodirector.MakeupViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5] (83.0%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.3, 47.6, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]', 83.0, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step128' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step128', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Energetic at (84.7%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Energetic', 84.7, 61.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '90'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '90')
    with step("[Action] Drag cpSlider (88.0%,42.9%) → slider (3.4%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 88.0, 42.9, AppiumBy.ACCESSIBILITY_ID, 'slider', 3.4, 56.1, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step133' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step133', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.7%,50.0%) → slider (98.3%,39.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.7, 50.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.3, 39.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step136' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step136', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Alluring at (77.8%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Alluring', 77.8, 71.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '89'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '89')
    with step("[Action] Drag cpSlider (86.3%,57.1%) → slider (2.3%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 86.3, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.3, 58.5, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step141' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step141', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.3%,54.8%) → slider (99.2%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.3, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.2, 56.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step144' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step144', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Chic at (41.7%, 23.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Chic', 41.7, 23.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '83'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '83')
    with step("[Action] Drag cpSlider (79.8%,52.4%) → slider (3.1%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 79.8, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 3.1, 56.1, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step149' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step149', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.9%,54.8%) → slider (99.7%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.9, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.7, 56.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step152' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step152', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Party at (67.6%, 81.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Party', 67.6, 81.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '88'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '88')
    with step("[Action] Drag cpSlider (86.6%,59.5%) → slider (1.7%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 86.6, 59.5, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.7, 58.5, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00212_makeup_looks_Step157' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step157', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (7.0%,57.1%) → valueLabel (0.0%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.0, 57.1, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 0.0, 58.5, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step160' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step160', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Adorable at (39.4%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Adorable', 39.4, 57.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '90'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '90')
    with step("[Action] Drag cpSlider (86.8%,47.6%) → slider (2.5%,63.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 86.8, 47.6, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.5, 63.4, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Action] Drag cpSlider (5.9%,52.4%) → slider (98.6%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.9, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.6, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00212_makeup_looks_Step167' for GT comparison"):
        actions.capture_for_gt('00212_makeup_looks_Step167', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (91.8%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 91.8, 53.1)
    with step("[Action] Tap btn_ok_n at (79.6%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 79.6, 40.8)
    with step("[Action] Tap homeButton at (65.4%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 65.4)
    with step("[Action] Tap Discard at (60.9%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 60.9, 66.7)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
