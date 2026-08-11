import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00081_main_05_07_15_20260805_111520")
def test_00081_main_05_07_15_20260805_111520(actions: DriverActions):
    with step("[Action] Tap Edit at (57.1%, 28.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 57.1, 28.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (86.8%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 86.8, 66.7)
    with step("[Action] Tap _AT at (10.4%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.4, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (26.2%, 63.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 26.2, 63.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (40.5%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 40.5, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap btn_reshape_n at (66.7%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_reshape_n', 66.7, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_leg_width_n at (85.4%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_leg_width_n', 85.4, 47.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='bodyPartCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Verify] Capture '00081_main_05_07_15_Step09' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step09', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag centerSlider (50.1%,54.0%) → intensitySlider (1.9%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.1, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 1.9, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00081_main_05_07_15_Step12' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step12', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag centerSlider (5.4%,54.0%) → intensitySlider (98.6%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 5.4, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.6, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00081_main_05_07_15_Step15' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step15', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btn_LegLength_n at (31.7%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_LegLength_n', 31.7, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='bodyPartCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag cpSlider (5.2%,52.0%) → intensitySlider (98.6%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.2, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.6, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00081_main_05_07_15_Step20' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step20', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btn_waist_n at (65.9%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_waist_n', 65.9, 80.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='bodyPartCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.4%,50.0%) → //XCUIElementTypeOther[@name=\"photodirector.BodyReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[1] (1.9%,44.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.4, 50.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]', 1.9, 44.9, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00081_main_05_07_15_Step25' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step25', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag centerSlider (6.3%,60.0%) → intensitySlider (98.3%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.3, 60.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.3, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00081_main_05_07_15_Step28' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step28', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btn_bust_n at (57.5%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_bust_n', 57.5, 67.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='bodyPartCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag cpSlider (5.7%,54.0%) → //XCUIElementTypeOther[@name=\"photodirector.BodyReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[1] (87.2%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.7, 54.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]', 87.2, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00081_main_05_07_15_Step33' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step33', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btn_arms_n at (46.3%, 77.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_arms_n', 46.3, 77.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='bodyPartCollectionView', container_w=431, container_h=71)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.7%,46.0%) → intensitySlider (1.9%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.7, 46.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 1.9, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00081_main_05_07_15_Step38' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step38', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag centerSlider (5.7%,56.0%) → intensitySlider (98.6%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 5.7, 56.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.6, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00081_main_05_07_15_Step41' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step41', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btn_shoulder_n at (45.0%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_shoulder_n', 45.0, 47.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='bodyPartCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.4%,52.0%) → intensitySlider (3.0%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.4, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 3.0, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00081_main_05_07_15_Step46' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step46', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag centerSlider (5.2%,58.0%) → //XCUIElementTypeOther[@name=\"photodirector.BodyReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[1] (87.2%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 5.2, 58.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]', 87.2, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00081_main_05_07_15_Step49' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step49', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btn_width_n at (46.3%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_width_n', 46.3, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='bodyPartCollectionView', container_w=431, container_h=71)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (49.6%,56.0%) → intensitySlider (1.9%,63.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 49.6, 56.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 1.9, 63.3, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00081_main_05_07_15_Step54' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step54', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag centerSlider (6.5%,64.0%) → intensitySlider (98.6%,63.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.5, 64.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.6, 63.3, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00081_main_05_07_15_Step57' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step57', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btn_hip_n at (78.0%, 90.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_hip_n', 78.0, 90.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='bodyPartCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (51.0%,54.0%) → intensitySlider (0.3%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.0, 54.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 0.3, 51.0, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00081_main_05_07_15_Step62' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step62', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag centerSlider (6.5%,56.0%) → intensitySlider (99.7%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.5, 56.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 99.7, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00081_main_05_07_15_Step65' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step65', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeImage/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btn_BodyHeight_n at (53.7%, 87.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_BodyHeight_n', 53.7, 87.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='bodyPartCollectionView', container_w=430, container_h=71)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag centerSlider (50.7%,48.0%) → intensitySlider (2.5%,55.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.7, 48.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 2.5, 55.1, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Verify] Capture '00081_main_05_07_15_Step70' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step70', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag centerSlider (4.9%,52.0%) → intensitySlider (99.7%,59.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 4.9, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 99.7, 59.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00081_main_05_07_15_Step73' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step73', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_undo at (55.1%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 55.1, 53.1)
    with step("[Verify] Capture '00081_main_05_07_15_Step75' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step75', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_redo at (71.4%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 71.4, 30.6)
    with step("[Verify] Capture '00081_main_05_07_15_Step77' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step77', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (98.0%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 98.0, 51.0)
    with step("[Action] Tap btnClose at (61.3%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 61.3, 54.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (22.4%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 22.4, 30.6)
    with step("[Action] Tap photoPickerButton at (57.7%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton', 57.7, 42.3)
    with step("[Action] Tap btnAlbum at (76.6%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 76.6, 66.7)
    with step("[Action] Tap _AT at (7.2%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.2, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-1 at (50.8%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 50.8, 40.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap btn_reshape_n at (33.3%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_reshape_n', 33.3, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00081_main_05_07_15_Step86' for GT comparison"):
        actions.capture_for_gt('00081_main_05_07_15_Step86', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.BodyReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (38.8%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 38.8, 49.0)
    with step("[Action] Tap homeButton at (76.9%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 76.9, 73.1)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
