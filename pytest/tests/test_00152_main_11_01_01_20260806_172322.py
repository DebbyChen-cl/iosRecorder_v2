import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00152_main_11_01_01_20260806_172322")
def test_00152_main_11_01_01_20260806_172322(actions: DriverActions):
    with step("[Action] Tap btnSettings at (48.5%, 52.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 48.5, 52.9)
    with step("[Action] Tap About at (66.7%, 65.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 66.7, 65.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (40.8%, 36.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 40.8, 36.0)
    with step("[Action] Tap Free at (76.5%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 76.5, 71.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (52.8%, 63.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 52.8, 63.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (60.0%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 60.0, 44.4)
    with step("[Action] Tap btnBack at (57.1%, 63.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 57.1, 63.8)
    with step("[Action] Tap btnBack at (50.0%, 55.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 50.0, 55.3)
    with step("[Action] Tap Camera at (33.3%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Camera', 33.3, 64.0)
    with step("[Action] Tap btnFilter at (58.2%, 39.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnFilter', 58.2, 39.7)
    with step("[Action] Tap Pure at (43.9%, 77.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pure', 43.9, 77.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='cmsCategoryCollectionViewCollectionView', container_w=421, container_h=33)
    with step("[Action] Tap Mellow Fade 02 at (57.4%, 41.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Mellow Fade 02', 57.4, 41.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=93)
    with step("[Action] Tap btnTakePhoto at (66.7%, 64.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 66.7, 64.2)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.CameraProViewController"]/XCUIElementTypeOther[4]')
    with step("[Action] Tap btnReset at (68.6%, 74.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnReset', 68.6, 74.3)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.CameraProViewController"]/XCUIElementTypeOther[4]', expected_result='different', threshold=0.98)
    with step("[Action] Tap BEAUTIFY at (57.3%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'BEAUTIFY', 57.3, 52.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=312, container_h=40)
    with step("[Action] Tap ic_conceal_portrait at (37.5%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 37.5, 52.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Drag cpSlider (27.1%,54.8%) → slider (98.4%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 27.1, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.4, 58.5, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap btnTakePhoto at (57.4%, 67.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 57.4, 67.9)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.CameraProViewController"]/XCUIElementTypeOther[4]')
    with step("[Action] Tap btnReset at (77.1%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnReset', 77.1, 57.1)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.CameraProViewController"]/XCUIElementTypeOther[4]', expected_result='different', threshold=0.98)
    with step("[Action] Tap ic_skintone_portrait at (60.0%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_skintone_portrait', 60.0, 45.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Drag centerSlider (49.7%,52.4%) → slider (98.4%,61.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 49.7, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.4, 61.0, duration=1.0)
    with step("[Action] Tap btnTakePhoto at (53.7%, 56.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 53.7, 56.6)
    with step("[Action] Tap btnReset at (71.4%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnReset', 71.4, 28.6)
    with step("[Action] Tap ic_teeth_whiten_portrait at (62.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_teeth_whiten_portrait', 62.5, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Drag cpSlider (6.5%,59.5%) → slider (99.7%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.5, 59.5, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.7, 58.5, duration=1.0)
    with step("[Action] Tap btnTakePhoto at (50.0%, 47.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 50.0, 47.2)
    with step("[Action] Tap btnReset at (71.4%, 68.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnReset', 71.4, 68.6)
    with step("[Action] Tap ic_eye_brighten_portrait at (80.0%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_eye_brighten_portrait', 80.0, 57.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Drag cpSlider (29.7%,57.1%) → slider (97.1%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 29.7, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 97.1, 51.2, duration=1.0)
    with step("[Action] Tap btnTakePhoto at (64.8%, 62.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 64.8, 62.3)
    with step("[Action] Tap btnReset at (68.6%, 51.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnReset', 68.6, 51.4)
    with step("[Action] Tap ic_eyebag_removal at (70.0%, 72.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_eyebag_removal', 70.0, 72.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Drag cpSlider (7.7%,52.4%) → slider (82.6%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.7, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 82.6, 57.1, duration=1.0)
    with step("[Action] Tap btnTakePhoto at (61.1%, 49.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 61.1, 49.1)
    with step("[Action] Tap btnReset at (71.4%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnReset', 71.4, 57.1)
    with step("[Action] Tap ic_oilness at (70.0%, 77.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_oilness', 70.0, 77.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Drag cpSlider (5.8%,45.2%) → slider (98.0%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.8, 45.2, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.0, 51.2, duration=1.0)
    with step("[Action] Tap btnTakePhoto at (66.7%, 66.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 66.7, 66.0)
    with step("[Action] Tap btnReset at (37.1%, 77.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnReset', 37.1, 77.1)
    with step("[Action] Tap MAKEUP at (45.8%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'MAKEUP', 45.8, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=312, container_h=40)
    with step("[Action] Tap Lipstick at (51.1%, 47.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Lipstick', 51.1, 47.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='makeupCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap Nude 01 at (52.1%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Nude 01', 52.1, 52.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Action] Tap btnTakePhoto at (51.9%, 71.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 51.9, 71.7)
    with step("[Action] Tap btnReset at (45.7%, 37.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnReset', 45.7, 37.1)
    with step("[Action] Tap btnHome at (50.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 50.0, 52.5)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.98)
    assert True
