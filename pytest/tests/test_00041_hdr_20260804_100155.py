import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00041_hdr_20260804_100155")
def test_00041_hdr_20260804_100155(actions: DriverActions):
    with step("[Action] Tap Edit at (51.4%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 51.4, 60.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (86.8%, 78.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 86.8, 78.6)
    with step("[Action] Tap _AT at (9.7%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.7, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (50.0%, 50.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 50.0, 50.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (36.6%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 36.6, 62.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Verify] Capture '00041_hdr_Step06' for GT comparison"):
        actions.capture_for_gt('00041_hdr_Step06', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_2lv_HDR at (51.5%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_2lv_HDR', 51.5, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00041_hdr_Step08' for GT comparison"):
        actions.capture_for_gt('00041_hdr_Step08', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag EditingImageView_ImageView (4.9%,56.8%) → Vertical scroll bar, 1 page (56.7%,53.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 4.9, 56.8, AppiumBy.ACCESSIBILITY_ID, 'Vertical scroll bar, 1 page', 56.7, 53.0, duration=1.0)
    with step("[Verify] Capture '00041_hdr_Step10' for GT comparison"):
        actions.capture_for_gt('00041_hdr_Step10', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Verify] Capture '00041_hdr_Step11' for GT comparison"):
        actions.capture_for_gt('00041_hdr_Step11', AppiumBy.ACCESSIBILITY_ID, 'cpSlider', threshold=0.95)
    with step("[Verify] Capture '00041_hdr_Step12' for GT comparison"):
        actions.capture_for_gt('00041_hdr_Step12', AppiumBy.ACCESSIBILITY_ID, 'valueLabel', threshold=0.95)
    with step("[Action] Drag cpSlider (86.6%,57.1%) → slider (98.4%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 86.6, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.4, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture '00041_hdr_Step15' for GT comparison"):
        actions.capture_for_gt('00041_hdr_Step15', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (14.3%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 14.3, 28.6)
    with step("[Verify] Capture '00041_hdr_Step17' for GT comparison"):
        actions.capture_for_gt('00041_hdr_Step17', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_2lv_HDR at (84.8%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_2lv_HDR', 84.8, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_edge_n at (52.5%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_edge_n', 52.5, 75.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag centerSlider (24.0%,52.4%) → slider (95.9%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 24.0, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 95.9, 53.7, duration=1.0)
    with step("[Verify] valueLabel text equals '80'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '80')
    with step("[Verify] Capture '00041_hdr_Step22' for GT comparison"):
        actions.capture_for_gt('00041_hdr_Step22', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag centerSlider (93.1%,50.0%) → slider (3.2%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 93.1, 50.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 3.2, 58.5, duration=1.0)
    with step("[Verify] valueLabel text equals '-20'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-20')
    with step("[Verify] Capture '00041_hdr_Step25' for GT comparison"):
        actions.capture_for_gt('00041_hdr_Step25', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag centerSlider (6.9%,59.5%) → valueLabel (0.0%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.9, 59.5, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 0.0, 53.7, duration=1.0)
    with step("[Action] Tap btn_ok_n at (77.6%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 38.8)
    with step("[Verify] Capture '00041_hdr_Step28' for GT comparison"):
        actions.capture_for_gt('00041_hdr_Step28', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (69.2%, 84.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 69.2, 84.6)
    with step("[Action] Tap Discard at (79.7%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 79.7, 75.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
