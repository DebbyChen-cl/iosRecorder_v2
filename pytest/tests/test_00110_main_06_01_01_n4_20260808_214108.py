import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00110_main_06_01_01_n4_20260808_214108")
def test_00110_main_06_01_01_n4_20260808_214108(actions: DriverActions):
    with step("[Action] Tap Edit at (65.7%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 65.7, 56.0)
    with step("[Action] Tap btnAlbum at (78.7%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 78.7, 71.4)
    with step("[Action] Tap _AT at (9.3%, 31.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.3, 31.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (59.2%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 59.2, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (53.3%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 53.3, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Text"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Text', direction='left', offset_start=(0.423, 0.536), offset_end=(0.302, 0.536), velocity=92)
    with step("[Action] Tap Text at (54.2%, 26.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text', 54.2, 26.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Text Bubble at (74.0%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text Bubble', 74.0, 58.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Drag imageView (67.2%,60.89%) → backgroundView (87.9%,65.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'imageView', 67.2, 60.89, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 87.9, 65.9, duration=1.0)
    with step("[Verify] Capture '00110_main_06_01_01_n4_Step10' for GT comparison"):
        actions.capture_for_gt('00110_main_06_01_01_n4_Step10', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.89)
    with step("[Action] Tap Bubble at (42.9%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Bubble', 42.9, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textBubbleBottomBarCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap leaveButton at (52.9%, 78.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'leaveButton', 52.9, 78.8)
    with step("[Verify] Capture '00110_main_06_01_01_n4_Step13' for GT comparison"):
        actions.capture_for_gt('00110_main_06_01_01_n4_Step13', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.89)
    with step("[Action] Tap Bubble at (36.5%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Bubble', 36.5, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textBubbleBottomBarCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap shadowSwitch at (52.7%, 55.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'shadowSwitch', 52.7, 55.9)
    with step("[Verify] Capture '00110_main_06_01_01_n4_Step16' for GT comparison"):
        actions.capture_for_gt('00110_main_06_01_01_n4_Step16', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.89)
    with step("[Action] Drag opacitySlider (91.3%,47.6%) → backgroundView (30.89%,62.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'opacitySlider', 91.3, 47.6, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 30.89, 62.9, duration=1.0)
    with step("[Verify] Capture '00110_main_06_01_01_n4_Step18' for GT comparison"):
        actions.capture_for_gt('00110_main_06_01_01_n4_Step18', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.89)
    with step("[Action] Drag opacitySlider (7.4%,47.6%) → backgroundView (84.9%,63.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'opacitySlider', 7.4, 47.6, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 84.9, 63.0, duration=1.0)
    with step("[Verify] Capture '00110_main_06_01_01_n4_Step20' for GT comparison"):
        actions.capture_for_gt('00110_main_06_01_01_n4_Step20', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.89)
    with step("[Action] Tap CMS-phdm_202301_textbubble_Vday01 at (55.9%, 55.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_202301_textbubble_Vday01', 55.9, 55.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textBubblePageContentViewControllerCollectionView', container_w=422, container_h=172)
    with step("[Verify] Capture '00110_main_06_01_01_n4_Step22' for GT comparison"):
        actions.capture_for_gt('00110_main_06_01_01_n4_Step22', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.89)
    with step("[Action] Tap CMS-phdm_202301_textbubble_Vday02 at (57.4%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_202301_textbubble_Vday02', 57.4, 48.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textBubblePageContentViewControllerCollectionView', container_w=422, container_h=172)
    with step("[Verify] Capture '00110_main_06_01_01_n4_Step24' for GT comparison"):
        actions.capture_for_gt('00110_main_06_01_01_n4_Step24', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.89)
    with step("[Action] Tap CMS-phdm_202301_textbubble_Vday03 at (44.9%, 55.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_202301_textbubble_Vday03', 44.9, 55.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textBubblePageContentViewControllerCollectionView', container_w=422, container_h=172)
    with step("[Verify] Capture '00110_main_06_01_01_n4_Step26' for GT comparison"):
        actions.capture_for_gt('00110_main_06_01_01_n4_Step26', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.89)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"mainPanel\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1] (72.7%,20.0%) → backgroundView (50.7%,95.0%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="mainPanel"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]', 72.7, 20.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 50.7, 95.0, duration=1.0)
    with step("[Verify] Capture '00110_main_06_01_01_n4_Step28' for GT comparison"):
        actions.capture_for_gt('00110_main_06_01_01_n4_Step28', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.89)
    with step("[Action] Tap btn_ok_n at (55.1%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 55.1, 55.1)
    with step("[Action] Tap OK at (90.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 90.0, 50.0)
    with step("[Action] Tap homeButton at (57.7%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 57.7, 53.8)
    with step("[Action] Tap Discard at (79.7%, 29.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 79.7, 29.2)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.89)
    assert True
