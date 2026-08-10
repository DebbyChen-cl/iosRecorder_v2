import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00076_reshape_with_face_20260805_110104")
def test_00076_reshape_with_face_20260805_110104(actions: DriverActions):
    with step("[Action] Tap Edit at (51.4%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 51.4, 60.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (75.6%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 75.6, 33.3)
    with step("[Action] Tap _AT at (7.2%, 90.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.2, 90.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (44.6%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 44.6, 67.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (31.1%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 31.1, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (33.3%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 33.3, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_face_reshape_portrait at (30.3%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_reshape_portrait', 30.3, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Face at (56.8%, 41.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Face', 56.8, 41.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=40)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.5%,54.0%) → intensitySlider (3.3%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.5, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 3.3, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step12' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step12', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (4.5%,50.0%) → intensitySlider (96.1%,42.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 4.5, 50.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 96.1, 42.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step15' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step15', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_FaceJaw_n at (66.7%, 93.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_FaceJaw_n', 66.7, 93.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.4%,54.0%) → intensitySlider (5.3%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.4, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 5.3, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step20' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step20', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.0%,60.0%) → intensitySlider (98.8%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.0, 60.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.8, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step23' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step23', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (68.1%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 68.1, 64.5)
    with step("[Action] Tap Left at (49.7%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 49.7, 52.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.6%,54.0%) → intensitySlider (4.0%,61.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.6, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.0, 61.2, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step29' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step29', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (9.6%,64.0%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1] (60.9%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 9.6, 64.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1]', 60.9, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step32' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step32', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Left at (55.6%, 74.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 55.6, 74.2)
    with step("[Action] Tap Right at (47.9%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Right', 47.9, 67.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.0%,44.0%) → intensitySlider (4.5%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.0, 44.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.5, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step38' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step38', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (9.2%,50.0%) → intensitySlider (97.6%,42.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 9.2, 50.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 97.6, 42.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step41' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step41', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_FaceForehead_n at (69.7%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_FaceForehead_n', 69.7, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.3%,48.0%) → intensitySlider (4.2%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.3, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.2, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step46' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step46', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (6.2%,58.0%) → intensitySlider (97.6%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.2, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 97.6, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step49' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step49', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_FaceChin_n at (47.1%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_FaceChin_n', 47.1, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.2%,46.0%) → intensitySlider (4.2%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.2, 46.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.2, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step54' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step54', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (7.7%,58.0%) → intensitySlider (98.8%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 7.7, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.8, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step57' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step57', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_EyeEnlarge_n at (41.2%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_EyeEnlarge_n', 41.2, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=431, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.0%,40.0%) → intensitySlider (3.2%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.0, 40.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 3.2, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step62' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step62', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (7.6%,58.0%) → intensitySlider (98.0%,44.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 7.6, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.0, 44.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step65' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step65', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (87.5%, 32.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 87.5, 32.3)
    with step("[Action] Tap Left at (20.6%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 20.6, 52.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.4%,46.0%) → intensitySlider (7.3%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.4, 46.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 7.3, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step71' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step71', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.4%,56.0%) → intensitySlider (98.4%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.4, 56.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.4, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step74' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step74', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Left at (61.1%, 38.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 61.1, 38.7)
    with step("[Action] Tap Right at (53.9%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Right', 53.9, 70.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.8%,48.0%) → intensitySlider (4.9%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.8, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.9, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step80' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step80', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (9.6%,58.0%) → valueLabel (4.6%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 9.6, 58.0, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 4.6, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step83' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step83', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_EyeHeight_n at (38.2%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_EyeHeight_n', 38.2, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.4%,56.0%) → intensitySlider (1.2%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.4, 56.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 1.2, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step88' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step88', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.4%,46.0%) → intensitySlider (97.6%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.4, 46.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 97.6, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step91' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step91', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (79.2%, 71.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 79.2, 71.0)
    with step("[Action] Tap Left at (52.7%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 52.7, 52.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.0%,48.0%) → intensitySlider (3.6%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.0, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 3.6, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step97' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step97', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (6.0%,50.0%) → intensitySlider (96.4%,46.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 96.4, 46.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step100' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step100', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Left at (51.4%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 51.4, 54.8)
    with step("[Action] Tap Right at (52.7%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Right', 52.7, 57.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (54.2%,58.0%) → intensitySlider (4.0%,63.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 54.2, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.0, 63.3, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step106' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step106', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.0%,48.0%) → intensitySlider (99.2%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.0, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 99.2, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step109' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step109', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_EyeLift_n at (23.5%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_EyeLift_n', 23.5, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=431, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (53.4%,54.0%) → intensitySlider (4.9%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 53.4, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.9, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step114' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step114', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.0%,56.0%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1] (59.5%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.0, 56.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1]', 59.5, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step117' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step117', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (30.6%, 41.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 30.6, 41.9)
    with step("[Action] Tap Left at (35.2%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 35.2, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.2%,38.0%) → intensitySlider (4.5%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.2, 38.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.5, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step123' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step123', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.4%,62.0%) → intensitySlider (99.6%,61.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.4, 62.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 99.6, 61.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step126' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step126', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Left at (69.4%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 69.4, 67.7)
    with step("[Action] Tap Right at (47.9%, 92.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Right', 47.9, 92.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.2%,52.0%) → intensitySlider (4.0%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.2, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.0, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step132' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step132', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (7.6%,58.0%) → intensitySlider (98.8%,42.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 7.6, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.8, 42.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step135' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step135', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_EyeAngle_n at (47.1%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_EyeAngle_n', 47.1, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.0%,54.0%) → intensitySlider (3.2%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.0, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 3.2, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step140' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step140', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.0%,48.0%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1] (60.5%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.0, 48.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1]', 60.5, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step143' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step143', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (40.3%, 71.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 40.3, 71.0)
    with step("[Action] Tap Left at (40.6%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 40.6, 57.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (52.2%,54.0%) → intensitySlider (2.0%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 52.2, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 2.0, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step149' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step149', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (7.6%,62.0%) → intensitySlider (100.0%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 7.6, 62.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 100.0, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step152' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step152', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Left at (83.3%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 83.3, 48.4)
    with step("[Action] Tap Right at (58.8%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Right', 58.8, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (53.4%,58.0%) → intensitySlider (4.9%,63.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 53.4, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.9, 63.3, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step158' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step158', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.0%,52.0%) → intensitySlider (97.2%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.0, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 97.2, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step161' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step161', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_EyeWidth_n at (52.9%, 78.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_EyeWidth_n', 52.9, 78.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=431, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.2%,58.0%) → intensitySlider (4.5%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.2, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.5, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step166' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step166', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (5.6%,54.0%) → intensitySlider (99.6%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 5.6, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 99.6, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step169' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step169', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (79.2%, 41.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 79.2, 41.9)
    with step("[Action] Tap Left at (50.9%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 50.9, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.4%,48.0%) → intensitySlider (3.6%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.4, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 3.6, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step175' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step175', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.8%,56.0%) → intensitySlider (99.2%,44.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.8, 56.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 99.2, 44.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step178' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step178', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Left at (58.3%, 58.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 58.3, 58.1)
    with step("[Action] Tap Right at (49.7%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Right', 49.7, 65.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.4%,52.0%) → intensitySlider (5.7%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.4, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 5.7, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step184' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step184', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (7.6%,58.0%) → intensitySlider (98.0%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 7.6, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.0, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step187' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step187', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_EyeDistance_n at (58.8%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_EyeDistance_n', 58.8, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.0%,54.0%) → intensitySlider (4.0%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.0, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.0, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step192' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step192', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.4%,50.0%) → intensitySlider (95.5%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.4, 50.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 95.5, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step195' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step195', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (38.9%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 38.9, 54.8)
    with step("[Action] Tap Left at (43.0%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 43.0, 47.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (49.8%,66.0%) → intensitySlider (0.4%,67.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 49.8, 66.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 0.4, 67.3, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step201' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step201', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (7.6%,52.0%) → intensitySlider (98.8%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 7.6, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.8, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step204' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step204', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Left at (48.6%, 29.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 48.6, 29.0)
    with step("[Action] Tap Right at (47.3%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Right', 47.3, 57.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.8%,52.0%) → intensitySlider (1.6%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.8, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 1.6, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step210' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step210', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.4%,50.0%) → intensitySlider (96.8%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.4, 50.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 96.8, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step213' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step213', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_EyePupil_n at (82.4%, 39.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_EyePupil_n', 82.4, 39.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=431, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (52.6%,52.0%) → intensitySlider (5.3%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 52.6, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 5.3, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step218' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step218', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (7.2%,46.0%) → intensitySlider (97.6%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 7.2, 46.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 97.6, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step221' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step221', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (41.7%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 41.7, 51.6)
    with step("[Action] Tap Left at (43.0%, 42.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 43.0, 42.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (52.6%,52.0%) → intensitySlider (3.6%,61.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 52.6, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 3.6, 61.2, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step227' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step227', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (7.6%,52.0%) → intensitySlider (98.8%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 7.6, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.8, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step230' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step230', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Left at (22.2%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 22.2, 48.4)
    with step("[Action] Tap Right at (45.5%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Right', 45.5, 52.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.0%,48.0%) → intensitySlider (4.5%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.0, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.5, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step236' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step236', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.0%,56.0%) → intensitySlider (99.2%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.0, 56.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 99.2, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step239' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step239', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_BrowsLift_n at (64.7%, 30.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_BrowsLift_n', 64.7, 30.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=431, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (53.8%,58.0%) → intensitySlider (3.2%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 53.8, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 3.2, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step244' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step244', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (9.2%,50.0%) → intensitySlider (95.1%,46.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 9.2, 50.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 95.1, 46.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step247' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step247', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (75.0%, 35.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 75.0, 35.5)
    with step("[Action] Tap Left at (46.7%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 46.7, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.4%,48.0%) → intensitySlider (0.4%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.4, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 0.4, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step253' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step253', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (6.8%,44.0%) → intensitySlider (97.2%,40.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.8, 44.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 97.2, 40.8, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step256' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step256', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Left at (83.3%, 74.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 83.3, 74.2)
    with step("[Action] Tap Right at (46.1%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Right', 46.1, 55.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.4%,62.0%) → intensitySlider (2.0%,65.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.4, 62.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 2.0, 65.3, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step262' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step262', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (9.2%,56.0%) → intensitySlider (96.0%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 9.2, 56.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 96.0, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step265' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step265', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_BrowsDistance_n at (35.3%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_BrowsDistance_n', 35.3, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=431, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.6%,56.0%) → intensitySlider (4.9%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.6, 56.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.9, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step270' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step270', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (6.8%,50.0%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1] (59.8%,44.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.8, 50.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1]', 59.8, 44.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step273' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step273', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (43.1%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 43.1, 64.5)
    with step("[Action] Tap Left at (50.3%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 50.3, 55.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (49.8%,52.0%) → intensitySlider (0.4%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 49.8, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 0.4, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step279' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step279', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.0%,50.0%) → intensitySlider (98.4%,46.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.0, 50.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.4, 46.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step282' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step282', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Left at (26.4%, 35.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 26.4, 35.5)
    with step("[Action] Tap Right at (48.5%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Right', 48.5, 55.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.6%,56.0%) → intensitySlider (2.4%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.6, 56.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 2.4, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step288' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step288', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.4%,60.0%) → intensitySlider (98.4%,44.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.4, 60.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.4, 44.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step291' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step291', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_BrowsThickness_n at (44.1%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_BrowsThickness_n', 44.1, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=431, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.4%,48.0%) → intensitySlider (2.0%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.4, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 2.0, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step296' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step296', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.8%,50.0%) → valueLabel (0.0%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.8, 50.0, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 0.0, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step299' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step299', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (38.9%, 19.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 38.9, 19.4)
    with step("[Action] Tap Left at (49.7%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 49.7, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.0%,54.0%) → intensitySlider (2.0%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.0, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 2.0, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step305' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step305', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.8%,52.0%) → intensitySlider (98.8%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.8, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.8, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step308' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step308', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Left at (59.7%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 59.7, 67.7)
    with step("[Action] Tap Right at (48.5%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Right', 48.5, 52.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.4%,58.0%) → intensitySlider (2.4%,61.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.4, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 2.4, 61.2, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step314' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step314', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (9.6%,64.0%) → intensitySlider (97.6%,61.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 9.6, 64.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 97.6, 61.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step317' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step317', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_BrowsAngle_n at (8.8%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_BrowsAngle_n', 8.8, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=431, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.0%,56.0%) → intensitySlider (0.8%,67.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.0, 56.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 0.8, 67.3, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step322' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step322', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (9.6%,58.0%) → intensitySlider (98.8%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 9.6, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.8, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step325' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step325', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (65.3%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 65.3, 67.7)
    with step("[Action] Tap Left at (57.6%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 57.6, 52.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (49.0%,52.0%) → intensitySlider (1.2%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 49.0, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 1.2, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step331' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step331', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.8%,44.0%) → intensitySlider (98.0%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.8, 44.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.0, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step334' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step334', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Left at (38.9%, 80.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 38.9, 80.6)
    with step("[Action] Tap Right at (43.0%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Right', 43.0, 67.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.8%,40.0%) → intensitySlider (5.7%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.8, 40.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 5.7, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step340' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step340', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (6.4%,62.0%) → intensitySlider (98.4%,46.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.4, 62.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.4, 46.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step343' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step343', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_NoseEnlarge_n at (50.0%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_NoseEnlarge_n', 50.0, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.6%,50.0%) → intensitySlider (3.0%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.6, 50.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 3.0, 49.0, duration=1.0)
    with step("[Verify] Capture '00076_reshape_with_face_Step347' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step347', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (6.5%,60.0%) → intensitySlider (99.1%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.5, 60.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 99.1, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step350' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step350', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_NoseHeight_n at (64.7%, 90.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_NoseHeight_n', 64.7, 90.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.9%,46.0%) → intensitySlider (3.0%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.9, 46.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 3.0, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step355' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step355', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (6.5%,58.0%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1] (79.8%,44.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.5, 58.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1]', 79.8, 44.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step358' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step358', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_NoseBridge_n at (44.1%, 39.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_NoseBridge_n', 44.1, 39.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (52.1%,50.0%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1] (1.6%,44.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 52.1, 50.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1]', 1.6, 44.9, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step363' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step363', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (7.1%,52.0%) → intensitySlider (98.5%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 7.1, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.5, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step366' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step366', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_NoseAla_n at (76.5%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_NoseAla_n', 76.5, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.8%,56.0%) → intensitySlider (2.0%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.8, 56.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 2.0, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step371' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step371', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.8%,60.0%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1] (60.5%,44.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.8, 60.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1]', 60.5, 44.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step374' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step374', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (68.1%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 68.1, 67.7)
    with step("[Action] Tap Left at (49.7%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 49.7, 40.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.6%,48.0%) → intensitySlider (2.4%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.6, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 2.4, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step380' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step380', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.4%,44.0%) → intensitySlider (99.2%,40.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.4, 44.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 99.2, 40.8, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step383' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step383', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Left at (70.8%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Left', 70.8, 67.7)
    with step("[Action] Tap Right at (49.7%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Right', 49.7, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.0%,62.0%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1] (1.6%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.0, 62.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1]', 1.6, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step389' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step389', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.0%,60.0%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1] (60.7%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.0, 60.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1]', 60.7, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step392' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step392', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_NoseTip_n at (41.2%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_NoseTip_n', 41.2, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.3%,54.0%) → intensitySlider (1.2%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.3, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 1.2, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step397' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step397', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (6.2%,56.0%) → intensitySlider (100.0%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.2, 56.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 100.0, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step400' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step400', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_LipsEnlarge_n at (47.1%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_LipsEnlarge_n', 47.1, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (49.1%,50.0%) → intensitySlider (1.2%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 49.1, 50.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 1.2, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step405' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step405', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (6.8%,54.0%) → intensitySlider (100.0%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.8, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 100.0, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step408' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step408', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_LipsSmile_n at (52.9%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_LipsSmile_n', 52.9, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag cpSlider (6.2%,54.0%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1] (79.5%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.2, 54.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther[1]', 79.5, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step413' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step413', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_LipsLift_n at (76.5%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_LipsLift_n', 76.5, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=431, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.5%,54.0%) → intensitySlider (1.8%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.5, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 1.8, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step418' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step418', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (6.8%,58.0%) → intensitySlider (99.4%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.8, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 99.4, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step421' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step421', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_LipsThickness_n at (69.7%, 87.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_LipsThickness_n', 69.7, 87.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=430, container_h=97)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (53.0%,52.0%) → intensitySlider (4.0%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 53.0, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.0, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step426' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step426', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (8.8%,50.0%) → intensitySlider (97.6%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 8.8, 50.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 97.6, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step429' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step429', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Both at (36.1%, 35.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Both', 36.1, 35.5)
    with step("[Action] Tap Upper at (28.5%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Upper', 28.5, 70.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.6%,50.0%) → intensitySlider (4.0%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.6, 50.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 4.0, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step435' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step435', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (9.2%,58.0%) → intensitySlider (96.8%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 9.2, 58.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 96.8, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step438' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step438', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Upper at (51.4%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Upper', 51.4, 54.8)
    with step("[Action] Tap Lower at (45.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Lower', 45.5, 60.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTable', container_w=165, container_h=119)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.8%,50.0%) → intensitySlider (0.4%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.8, 50.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 0.4, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00076_reshape_with_face_Step444' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step444', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag centerSlider (9.6%,48.0%) → intensitySlider (100.0%,42.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 9.6, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 100.0, 42.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00076_reshape_with_face_Step447' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step447', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_undo at (69.4%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 69.4, 51.0)
    with step("[Verify] Capture '00076_reshape_with_face_Step449' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step449', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_redo at (55.1%, 18.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 55.1, 18.4)
    with step("[Verify] Capture '00076_reshape_with_face_Step451' for GT comparison"):
        actions.capture_for_gt('00076_reshape_with_face_Step451', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (89.8%, 22.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 89.8, 22.4)
    with step("[Action] Tap btnClose at (61.3%, 41.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 61.3, 41.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (34.7%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 34.7, 36.7)
    with step("[Action] Tap btn_cancel_n at (30.6%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 30.6, 44.9)
    with step("[Action] Tap homeButton at (61.5%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 73.1)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
