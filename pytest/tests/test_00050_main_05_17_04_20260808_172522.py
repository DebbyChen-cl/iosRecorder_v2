import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00050_main_05_17_04_20260808_172522")
def test_00050_main_05_17_04_20260808_172522(actions: DriverActions):
    with step("[Action] Tap Edit at (17.1%, 28.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 17.1, 28.0)
    with step("[Action] Tap btnAlbum at (78.7%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 78.7, 71.4)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2] at (10.4%, 54.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', 10.4, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (39.2%, 45.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 39.2, 45.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (53.5%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 53.5, 62.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Light Hits"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Light Hits', direction='left', offset_start=(0.619, 0.412), offset_end=(0.026, 0.412), velocity=367)
    with step("[Action] Tap Light Hits at (33.8%, 28.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Light Hits', 33.8, 28.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"LightHitCell-0\"]/XCUIElementTypeImage at (65.7%, 58.2%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="LightHitCell-0"]/XCUIElementTypeImage', 65.7, 58.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=354, container_h=79)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeSlider (93.0%,49.0%) → //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3] (18.4%,50.0%)"):
            actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeSlider', 93.0, 49.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', 18.4, 50.0, duration=1.0)
    with step("[Verify] Capture '00050_main_05_17_04_Step10' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step10', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeSlider (7.0%,51.0%) → //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3] (84.9%,47.5%)"):
            actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeSlider', 7.0, 51.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', 84.9, 47.5, duration=1.0)
    with step("[Verify] Capture '00050_main_05_17_04_Step12' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step12', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_undo at (55.1%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 55.1, 28.6)
    with step("[Verify] Capture '00050_main_05_17_04_Step14' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step14', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_redo at (57.1%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 57.1, 32.7)
    with step("[Verify] Capture '00050_main_05_17_04_Step16' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step16', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_1lv_adjustment_s at (60.6%, 84.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_1lv_adjustment_s', 60.6, 84.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=354, container_h=79)
    with step("[Action] Tap btn_flipH_n at (60.5%, 60.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_flipH_n', 60.5, 60.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=380, container_h=79)
    with step("[Verify] Capture '00050_main_05_17_04_Step19' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step19', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_flipH_n at (60.5%, 60.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_flipH_n', 60.5, 60.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=380, container_h=79)
    with step("[Verify] Capture '00050_main_05_17_04_Step21' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step21', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_flipV_n at (46.5%, 44.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_flipV_n', 46.5, 44.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=380, container_h=79)
    with step("[Verify] Capture '00050_main_05_17_04_Step23' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step23', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_flipV_n at (62.8%, 62.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_flipV_n', 62.8, 62.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=380, container_h=79)
    with step("[Verify] Capture '00050_main_05_17_04_Step25' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step25', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Scroll until Softness"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Softness', direction='right', offset_start=(0.261, 0.316), offset_end=(0.476, 0.316), velocity=150)
    with step("[Action] Drag ic_exposure (53.5%,67.4%) → LightHitParamCell-5 (22.5%,40.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'ic_exposure', 53.5, 67.4, AppiumBy.ACCESSIBILITY_ID, 'LightHitParamCell-5', 22.5, 40.8, duration=1.0)
    with step("[Action] Scroll until Softness"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Softness', direction='right', offset_start=(0.147, 0.43), offset_end=(0.932, 0.43), velocity=265)
    with step("[Action] Tap Softness at (63.5%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Softness', 63.5, 59.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=380, container_h=79)
    with step("[Verify] 0 text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '0', '0')
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2] (17.7%,96.6%) → 0 (0.0%,57.5%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', 17.7, 96.6, AppiumBy.ACCESSIBILITY_ID, '0', 0.0, 57.5, duration=1.0)
    with step("[Verify] 100 text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '100', '100')
    with step("[Verify] Capture '00050_main_05_17_04_Step31' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step31', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2] (84.2%,97.3%) → //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeSlider (5.8%,51.0%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', 84.2, 97.3, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeSlider', 5.8, 51.0, duration=1.0)
    with step("[Verify] 0 text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '0', '0')
    with step("[Verify] Capture '00050_main_05_17_04_Step34' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step34', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2] (18.8%,98.0%) → 0 (10.0%,60.0%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', 18.8, 98.0, AppiumBy.ACCESSIBILITY_ID, '0', 10.0, 60.0, duration=1.0)
    with step("[Action] Tap Contrast at (46.0%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Contrast', 46.0, 72.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=380, container_h=79)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2] (51.4%,97.3%) → 0 (20.0%,67.5%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', 51.4, 97.3, AppiumBy.ACCESSIBILITY_ID, '0', 20.0, 67.5, duration=1.0)
    with step("[Verify] 100 text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '100', '100')
    with step("[Verify] Capture '00050_main_05_17_04_Step39' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step39', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2] (83.3%,97.3%) → //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3] (1.4%,52.5%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', 83.3, 97.3, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]', 1.4, 52.5, duration=1.0)
    with step("[Verify] -100 text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '-100', '-100')
    with step("[Verify] Capture '00050_main_05_17_04_Step42' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step42', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap Color at (63.5%, 86.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Color', 63.5, 86.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=380, container_h=79)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2] (54.2%,91.4%) → 0 (7.5%,50.0%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', 54.2, 91.4, AppiumBy.ACCESSIBILITY_ID, '0', 7.5, 50.0, duration=1.0)
    with step("[Verify] Capture '00050_main_05_17_04_Step45' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step45', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2] (83.5%,91.4%) → Hue (92.5%,46.7%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', 83.5, 91.4, AppiumBy.ACCESSIBILITY_ID, 'Hue', 92.5, 46.7, duration=1.0)
    with step("[Verify] Capture '00050_main_05_17_04_Step47' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step47', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2] (54.0%,96.8%) → 0 (0.0%,52.5%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', 54.0, 96.8, AppiumBy.ACCESSIBILITY_ID, '0', 0.0, 52.5, duration=1.0)
    with step("[Verify] Capture '00050_main_05_17_04_Step49' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step49', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2] (84.9%,97.0%) → //XCUIElementTypeOther[@name=\"light_hits\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSlider (2.3%,40.8%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', 84.9, 97.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeSlider', 2.3, 40.8, duration=1.0)
    with step("[Verify] Capture '00050_main_05_17_04_Step51' for GT comparison"):
        actions.capture_for_gt('00050_main_05_17_04_Step51', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (30.6%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 30.6, 46.9)
    with step("[Action] Tap Light Hits at (84.5%, 10.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Light Hits', 84.5, 10.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"LightHitCell-0\"]/XCUIElementTypeImage at (65.7%, 49.3%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="LightHitCell-0"]/XCUIElementTypeImage', 65.7, 49.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=354, container_h=79)
    with step("[Action] Tap btn_ok_n at (67.3%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 67.3, 46.9)
    with step("[Action] Tap homeButton at (65.4%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 76.9)
    with step("[Action] Tap Discard at (53.6%, 70.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 53.6, 70.8)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
