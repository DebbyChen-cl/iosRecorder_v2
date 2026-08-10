import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00088_makeup_with_face_20260805_113751")
def test_00088_makeup_with_face_20260805_113751(actions: DriverActions):
    with step("[Action] Tap Edit at (28.6%, 84.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 28.6, 84.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (69.5%, 40.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 69.5, 40.5)
    with step("[Action] Tap _AT at (9.3%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.3, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (62.3%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 62.3, 70.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (55.4%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 55.4, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (51.5%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 51.5, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_makeup_portrait at (27.3%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_makeup_portrait', 27.3, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Lipstick at (48.9%, 41.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Lipstick', 48.9, 41.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='makeupCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap Dried Rose 01 at (46.5%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Dried Rose 01', 46.5, 47.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] Capture '00088_makeup_with_face_Step10' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step10', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (49.9%,47.6%) → slider (2.0%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 49.9, 47.6, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.0, 58.5, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00088_makeup_with_face_Step14' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step14', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.6%,57.1%) → //XCUIElementTypeOther[@name=\"photodirector.MakeupViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4] (83.0%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.6, 57.1, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]', 83.0, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00088_makeup_with_face_Step17' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step17', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Contour at (39.1%, 79.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Contour', 39.1, 79.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='makeupCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"MenuDescriptionCell-0\"]/XCUIElementTypeOther/XCUIElementTypeImage at (37.3%, 85.7%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="MenuDescriptionCell-0"]/XCUIElementTypeOther/XCUIElementTypeImage', 37.3, 85.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] Capture '00088_makeup_with_face_Step20' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step20', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Verify] valueLabel text equals '75'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '75')
    with step("[Action] Drag cpSlider (72.3%,52.4%) → slider (2.0%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 72.3, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.0, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00088_makeup_with_face_Step24' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step24', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (6.7%,52.4%) → valueLabel (5.8%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.7, 52.4, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 5.8, 58.5, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00088_makeup_with_face_Step27' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step27', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Eyelashes at (41.9%, 67.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Eyelashes', 41.9, 67.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='makeupCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"MenuDescriptionCell-0\"]/XCUIElementTypeOther/XCUIElementTypeImage at (34.7%, 55.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="MenuDescriptionCell-0"]/XCUIElementTypeOther/XCUIElementTypeImage', 34.7, 55.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Verify] Capture '00088_makeup_with_face_Step31' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step31', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (48.7%,52.4%) → slider (0.3%,61.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 48.7, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 0.3, 61.0, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00088_makeup_with_face_Step34' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step34', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.9%,45.2%) → //XCUIElementTypeOther[@name=\"photodirector.MakeupViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4] (83.0%,44.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.9, 45.2, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]', 83.0, 44.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00088_makeup_with_face_Step37' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step37', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap CMS-eyelash_color_orange at (62.3%, 44.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-eyelash_color_orange', 62.3, 44.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='circleMenuDescriptionViewCollectionView', container_w=430, container_h=71)
    with step("[Verify] Capture '00088_makeup_with_face_Step39' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step39', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Eyebrows at (48.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Eyebrows', 48.5, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='makeupCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"MenuDescriptionCell-0\"]/XCUIElementTypeOther/XCUIElementTypeImage at (61.3%, 67.9%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="MenuDescriptionCell-0"]/XCUIElementTypeOther/XCUIElementTypeImage', 61.3, 67.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (49.6%,50.0%) → slider (2.5%,61.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 49.6, 50.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.5, 61.0, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00088_makeup_with_face_Step45' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step45', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.3%,57.1%) → slider (99.7%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.3, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.7, 58.5, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00088_makeup_with_face_Step48' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step48', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap CMS-eyebrow_color_camel at (59.3%, 55.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-eyebrow_color_camel', 59.3, 55.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='circleMenuDescriptionViewCollectionView', container_w=430, container_h=71)
    with step("[Verify] Capture '00088_makeup_with_face_Step50' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step50', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Eyeliner at (41.8%, 32.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Eyeliner', 41.8, 32.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='makeupCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"MenuDescriptionCell-0\"]/XCUIElementTypeOther/XCUIElementTypeImage at (30.7%, 42.9%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="MenuDescriptionCell-0"]/XCUIElementTypeOther/XCUIElementTypeImage', 30.7, 42.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Verify] Capture '00088_makeup_with_face_Step54' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step54', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (50.4%,45.2%) → slider (3.4%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 50.4, 45.2, AppiumBy.ACCESSIBILITY_ID, 'slider', 3.4, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00088_makeup_with_face_Step57' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step57', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.9%,52.4%) → valueLabel (4.3%,61.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.9, 52.4, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 4.3, 61.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00088_makeup_with_face_Step60' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step60', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap CMS-eyeliner_color_magenta at (35.2%, 49.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-eyeliner_color_magenta', 35.2, 49.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='circleMenuDescriptionViewCollectionView', container_w=430, container_h=71)
    with step("[Verify] Capture '00088_makeup_with_face_Step62' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step62', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Eye Shadow at (58.3%, 70.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Eye Shadow', 58.3, 70.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='makeupCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"MenuDescriptionCell-0\"]/XCUIElementTypeOther/XCUIElementTypeImage at (53.3%, 51.8%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="MenuDescriptionCell-0"]/XCUIElementTypeOther/XCUIElementTypeImage', 53.3, 51.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] Capture '00088_makeup_with_face_Step65' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step65', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (50.1%,64.3%) → slider (0.8%,46.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 50.1, 64.3, AppiumBy.ACCESSIBILITY_ID, 'slider', 0.8, 46.3, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00088_makeup_with_face_Step69' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step69', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.3%,59.5%) → //XCUIElementTypeOther[@name=\"photodirector.MakeupViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5] (82.3%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.3, 59.5, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]', 82.3, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00088_makeup_with_face_Step72' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step72', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Blush at (62.7%, 70.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Blush', 62.7, 70.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='makeupCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"MenuDescriptionCell-0\"]/XCUIElementTypeOther/XCUIElementTypeImage at (60.0%, 60.7%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="MenuDescriptionCell-0"]/XCUIElementTypeOther/XCUIElementTypeImage', 60.0, 60.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '80'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '80')
    with step("[Verify] Capture '00088_makeup_with_face_Step76' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step76', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (76.2%,47.6%) → slider (0.6%,46.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 76.2, 47.6, AppiumBy.ACCESSIBILITY_ID, 'slider', 0.6, 46.3, duration=1.0)
    with step("[Verify] valueLabel text equals '2'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '2')
    with step("[Verify] Capture '00088_makeup_with_face_Step79' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step79', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (7.3%,47.6%) → valueLabel (14.5%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.3, 47.6, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 14.5, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00088_makeup_with_face_Step82' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step82', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap CMS-blush_color_Pink-Orange at (61.1%, 59.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-blush_color_Pink-Orange', 61.1, 59.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='circleMenuDescriptionViewCollectionView', container_w=431, container_h=71)
    with step("[Verify] Capture '00088_makeup_with_face_Step84' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step84', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap Foundation at (45.1%, 58.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Foundation', 45.1, 58.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='makeupCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"MenuDescriptionCell-0\"]/XCUIElementTypeOther/XCUIElementTypeImage at (52.0%, 87.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="MenuDescriptionCell-0"]/XCUIElementTypeOther/XCUIElementTypeImage', 52.0, 87.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (51.0%,59.5%) → slider (2.8%,63.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 51.0, 59.5, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.8, 63.4, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Verify] Capture '00088_makeup_with_face_Step90' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step90', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Drag cpSlider (4.8%,57.1%) → valueLabel (27.5%,61.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 4.8, 57.1, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 27.5, 61.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00088_makeup_with_face_Step93' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step93', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_undo at (46.9%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 46.9, 34.7)
    with step("[Verify] Capture '00088_makeup_with_face_Step95' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step95', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap ic_redo at (61.2%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 61.2, 49.0)
    with step("[Verify] Capture '00088_makeup_with_face_Step97' for GT comparison"):
        actions.capture_for_gt('00088_makeup_with_face_Step97', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.MakeupViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (87.8%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 87.8, 55.1)
    with step("[Action] Tap btn_ok_n at (87.8%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 87.8, 59.2)
    with step("[Action] Tap homeButton at (34.6%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 34.6, 46.2)
    with step("[Action] Tap Discard at (52.2%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 52.2, 41.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
