import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00114_main_06_01_01a_20260809_135233")
def test_00114_main_06_01_01a_20260809_135233(actions: DriverActions):
    with step("[Action] Tap Edit at (28.6%, 84.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 28.6, 84.0)
    with step("[Action] Tap btnAlbum at (89.3%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 89.3, 47.6)
    with step("[Action] Tap _AT at (10.0%, 90.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.0, 90.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (30.0%, 77.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 30.0, 77.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (64.4%, 42.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 64.4, 42.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Brush"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Brush', direction='left', offset_start=(0.674, 0.526), offset_end=(0.079, 0.526), velocity=206)
    with step("[Action] Tap Brush at (32.4%, 10.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Brush', 32.4, 10.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Brush at (55.8%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Brush', 55.8, 83.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"BrushEffectCell-4\"]/XCUIElementTypeOther/XCUIElementTypeImage at (26.4%, 61.1%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="BrushEffectCell-4"]/XCUIElementTypeOther/XCUIElementTypeImage', 26.4, 61.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='brushCollectionView', container_w=404, container_h=72)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeOther[1] (14.1%,12.0%) → //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeImage (84.7%,95.5%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', 14.1, 12.0, AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeImage', 84.7, 95.5, duration=1.0)
    with step("[Verify] Capture '00114_main_06_01_01a_Step11' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step11', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag cpSlider (52.1%,66.7%) → slider (2.0%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 52.1, 66.7, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.0, 58.5, duration=1.0)
    with step("[Verify] valueLabel text equals '1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1')
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeOther[1] (6.2%,30.5%) → //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeImage (57.4%,92.2%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', 6.2, 30.5, AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeImage', 57.4, 92.2, duration=1.0)
    with step("[Verify] Capture '00114_main_06_01_01a_Step15' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step15', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.6%,59.5%) → brushSizeSlider (83.0%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.6, 59.5, AppiumBy.ACCESSIBILITY_ID, 'brushSizeSlider', 83.0, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeOther[1] (42.8%,14.9%) → //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeImage (90.1%,72.6%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', 42.8, 14.9, AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeImage', 90.1, 72.6, duration=1.0)
    with step("[Verify] Capture '00114_main_06_01_01a_Step19' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step19', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap ic_undo at (50.0%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 50.0, 32.7)
    with step("[Verify] Capture '00114_main_06_01_01a_Step21' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step21', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap ic_redo at (44.0%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 44.0, 32.7)
    with step("[Verify] Capture '00114_main_06_01_01a_Step23' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step23', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap NonScrollableMenuView-1 at (73.2%, 60.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'NonScrollableMenuView-1', 73.2, 60.9)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"BrushColorCellEx-3\"]/XCUIElementTypeOther at (26.5%, 67.6%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="BrushColorCellEx-3"]/XCUIElementTypeOther', 26.5, 67.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='colorCollectionView', container_w=404, container_h=76)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeOther[1] (85.9%,25.6%) → //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeImage (18.3%,73.6%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', 85.9, 25.6, AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeImage', 18.3, 73.6, duration=1.0)
    with step("[Verify] Capture '00114_main_06_01_01a_Step27' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step27', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_reset_n at (36.0%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n', 36.0, 30.6)
    with step("[Verify] Capture '00114_main_06_01_01a_Step29' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step29', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeOther[1] (24.0%,16.2%) → //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeImage (77.0%,85.6%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', 24.0, 16.2, AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeImage', 77.0, 85.6, duration=1.0)
    with step("[Action] Tap btn_cancel_n at (28.6%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 28.6, 57.1)
    with step("[Action] Tap Brush at (33.8%, 18.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Brush', 33.8, 18.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Brush at (44.2%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Brush', 44.2, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"BrushEffectCell-3\"]/XCUIElementTypeOther/XCUIElementTypeImage at (60.4%, 64.8%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="BrushEffectCell-3"]/XCUIElementTypeOther/XCUIElementTypeImage', 60.4, 64.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='brushCollectionView', container_w=404, container_h=72)
    with step("[Action] Drag cpSlider (49.3%,47.6%) → slider (99.2%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 49.3, 47.6, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.2, 53.7, duration=1.0)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeOther[1] (19.8%,12.5%) → //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeImage (76.0%,87.6%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', 19.8, 12.5, AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeImage', 76.0, 87.6, duration=1.0)
    with step("[Verify] Capture '00114_main_06_01_01a_Step37' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step37', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap brushEraseButton at (42.5%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'brushEraseButton', 42.5, 70.0)
    with step("[Action] Drag cpSlider (51.3%,52.4%) → slider (0.6%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 51.3, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 0.6, 58.5, duration=1.0)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeOther[1] (52.7%,24.3%) → //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeImage (16.1%,36.1%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', 52.7, 24.3, AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeImage', 16.1, 36.1, duration=1.0)
    with step("[Verify] Capture '00114_main_06_01_01a_Step41' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step41', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag cpSlider (5.9%,57.1%) → brushSizeSlider (82.6%,51.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.9, 57.1, AppiumBy.ACCESSIBILITY_ID, 'brushSizeSlider', 82.6, 51.0, duration=1.0)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeOther[1] (91.1%,59.1%) → //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeImage (45.5%,79.5%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', 91.1, 59.1, AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeImage', 45.5, 79.5, duration=1.0)
    with step("[Verify] Capture '00114_main_06_01_01a_Step44' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step44', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (71.4%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 71.4, 59.2)
    with step("[Verify] Capture '00114_main_06_01_01a_Step46' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step46', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (64.1%, 51.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 64.1, 51.3)
    with step("[Verify] Capture '00114_main_06_01_01a_Step48' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step48', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Brush at (60.6%, 18.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Brush', 60.6, 18.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Magic Brush at (46.8%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Magic Brush', 46.8, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap Neon at (79.3%, 92.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Neon', 79.3, 92.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='brushCollectionView', container_w=404, container_h=71)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeOther[1] (9.3%,17.2%) → //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeImage (75.5%,89.3%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', 9.3, 17.2, AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeImage', 75.5, 89.3, duration=1.0)
    with step("[Verify] Capture '00114_main_06_01_01a_Step53' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step53', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap ic_undo at (46.0%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 46.0, 34.7)
    with step("[Verify] Capture '00114_main_06_01_01a_Step55' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step55', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap ic_redo at (76.0%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 76.0, 57.1)
    with step("[Verify] Capture '00114_main_06_01_01a_Step57' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step57', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap magicBrushEraseButton at (72.5%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'magicBrushEraseButton', 72.5, 80.0)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeOther[1] (66.2%,51.5%) → //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeImage (38.2%,73.8%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', 66.2, 51.5, AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeImage', 38.2, 73.8, duration=1.0)
    with step("[Verify] Capture '00114_main_06_01_01a_Step60' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step60', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_reset_n at (62.0%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_reset_n', 62.0, 59.2)
    with step("[Verify] Capture '00114_main_06_01_01a_Step62' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step62', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeOther[1] (22.7%,13.6%) → //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeImage (72.2%,83.6%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', 22.7, 13.6, AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeImage', 72.2, 83.6, duration=1.0)
    with step("[Action] Tap btn_cancel_n at (53.1%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 53.1, 69.4)
    with step("[Verify] Capture '00114_main_06_01_01a_Step65' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step65', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Brush at (47.9%, 13.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Brush', 47.9, 13.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Magic Brush at (66.2%, 91.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Magic Brush', 66.2, 91.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap Neon at (72.4%, 14.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Neon', 72.4, 14.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='brushCollectionView', container_w=404, container_h=71)
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeOther[1] (22.7%,17.2%) → //XCUIElementTypeScrollView[@name=\"overlaysEffectView\"]/XCUIElementTypeImage (69.7%,89.5%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeOther[1]', 22.7, 17.2, AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="overlaysEffectView"]/XCUIElementTypeImage', 69.7, 89.5, duration=1.0)
    with step("[Action] Tap btn_ok_n at (85.7%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 85.7, 38.8)
    with step("[Verify] Capture '00114_main_06_01_01a_Step71' for GT comparison"):
        actions.capture_for_gt('00114_main_06_01_01a_Step71', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (61.5%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 61.5)
    with step("[Action] Tap Discard at (91.3%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 91.3, 66.7)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
