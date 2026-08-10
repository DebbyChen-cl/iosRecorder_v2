import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00062_focus_20260808_191315")
def test_00062_focus_20260808_191315(actions: DriverActions):
    with step("[Action] Tap Edit at (22.9%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 22.9, 56.0)
    with step("[Action] Tap btnAlbum at (70.6%, 64.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 70.6, 64.3)
    with step("[Action] Tap _AT at (9.7%, 27.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.7, 27.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (33.1%, 44.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 33.1, 44.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (49.3%, 42.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 49.3, 42.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Focus"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Focus', direction='left', offset_start=(0.689, 0.361), offset_end=(0.49, 0.361), velocity=145)
    with step("[Action] Tap Focus at (52.1%, 18.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Focus', 52.1, 18.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00062_focus_Step08' for GT comparison"):
        actions.capture_for_gt('00062_focus_Step08', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="focus"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag cpSlider (18.7%,42.9%) → depthSlider (96.3%,44.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 18.7, 42.9, AppiumBy.ACCESSIBILITY_ID, 'depthSlider', 96.3, 44.9, duration=1.0)
    with step("[Verify] Capture '00062_focus_Step10' for GT comparison"):
        actions.capture_for_gt('00062_focus_Step10', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="focus"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag cpSlider (95.6%,50.0%) → slider (0.3%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 95.6, 50.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 0.3, 51.2, duration=1.0)
    with step("[Verify] Capture '00062_focus_Step12' for GT comparison"):
        actions.capture_for_gt('00062_focus_Step12', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="focus"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap menuButtonBlur at (47.2%, 32.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'menuButtonBlur', 47.2, 32.4)
    with step("[Verify] valueLabel text equals '30'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '30')
    with step("[Action] Drag cpSlider (33.3%,64.3%) → slider (2.5%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 33.3, 64.3, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.5, 56.1, duration=1.0)
    with step("[Verify] Capture '00062_focus_Step16' for GT comparison"):
        actions.capture_for_gt('00062_focus_Step16', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="focus"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Verify] valueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0')
    with step("[Action] Drag cpSlider (5.6%,59.5%) → valueLabel (0.0%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.6, 59.5, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 0.0, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00062_focus_Step20' for GT comparison"):
        actions.capture_for_gt('00062_focus_Step20', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="focus"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (26.5%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 26.5, 34.7)
    with step("[Verify] Capture '00062_focus_Step22' for GT comparison"):
        actions.capture_for_gt('00062_focus_Step22', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Focus at (56.3%, 18.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Focus', 56.3, 18.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_ok_n at (81.6%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 49.0)
    with step("[Action] Tap btnClose at (41.9%, 41.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 41.9, 41.9)
    with step("[Action] Tap btn_cancel_n at (26.5%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 26.5, 38.8)
    with step("[Action] Tap homeButton at (53.8%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 53.8, 61.5)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
