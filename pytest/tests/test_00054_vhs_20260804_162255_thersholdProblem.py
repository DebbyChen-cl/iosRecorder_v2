import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00054_vhs_20260804_162255")
def test_00054_vhs_20260804_162255(actions: DriverActions):
    with step("[Action] Tap Edit at (54.3%, 76.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 54.3, 76.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (92.9%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 92.9, 66.7)
    with step("[Action] Tap _AT at (7.2%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.2, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (47.7%, 63.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 47.7, 63.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (32.4%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 32.4, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until btn_VHS"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_VHS', direction='left', offset_start=(0.784, 0.454), offset_end=(0.337, 0.454), velocity=484)
    with step("[Action] Tap btn_VHS at (61.8%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_VHS', 61.8, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap titleLabel at (67.6%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'titleLabel', 67.6, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='VHSStyleCollectionView', container_w=418, container_h=94)
    with step("[Verify] Capture '00054_vhs_Step11' before"):
        assert actions.capture_for_preview('00054_vhs_Step11', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Drag noiseSlider (50.0%,57.8%) → //XCUIElementTypeOther[@name=\"parametersStackVIew\"]/XCUIElementTypeOther[1] (83.0%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'noiseSlider', 50.0, 57.8, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="parametersStackVIew"]/XCUIElementTypeOther[1]', 83.0, 50.0, duration=1.0)
    with step("[Verify] noiseValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'noiseValueLabel', '100')
    with step("[Verify] Capture '00054_vhs_Step11' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step11', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step14' before"):
        assert actions.capture_for_preview('00054_vhs_Step14', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Drag noiseSlider (93.6%,53.3%) → //XCUIElementTypeOther[@name=\"parametersStackVIew\"]/XCUIElementTypeOther[1] (24.9%,52.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'noiseSlider', 93.6, 53.3, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="parametersStackVIew"]/XCUIElementTypeOther[1]', 24.9, 52.3, duration=1.0)
    with step("[Verify] noiseValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'noiseValueLabel', '0')
    with step("[Verify] Capture '00054_vhs_Step14' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step14', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step17' before"):
        assert actions.capture_for_preview('00054_vhs_Step17', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Drag distortionSlider (7.6%,55.6%) → //XCUIElementTypeOther[@name=\"parametersStackVIew\"]/XCUIElementTypeOther[2] (80.9%,61.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'distortionSlider', 7.6, 55.6, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="parametersStackVIew"]/XCUIElementTypeOther[2]', 80.9, 61.4, duration=1.0)
    with step("[Verify] distortionValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'distortionValueLabel', '100')
    with step("[Verify] Capture '00054_vhs_Step17' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step17', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step20' before"):
        assert actions.capture_for_preview('00054_vhs_Step20', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Drag distortionSlider (92.8%,48.9%) → //XCUIElementTypeOther[@name=\"parametersStackVIew\"]/XCUIElementTypeOther[2] (24.9%,54.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'distortionSlider', 92.8, 48.9, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="parametersStackVIew"]/XCUIElementTypeOther[2]', 24.9, 54.5, duration=1.0)
    with step("[Verify] distortionValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'distortionValueLabel', '0')
    with step("[Verify] Capture '00054_vhs_Step20' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step20', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step23' before"):
        assert actions.capture_for_preview('00054_vhs_Step23', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Drag positionSlider (33.7%,62.2%) → //XCUIElementTypeOther[@name=\"parametersStackVIew\"]/XCUIElementTypeOther[3] (80.5%,65.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'positionSlider', 33.7, 62.2, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="parametersStackVIew"]/XCUIElementTypeOther[3]', 80.5, 65.9, duration=1.0)
    with step("[Verify] positionValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'positionValueLabel', '100')
    with step("[Verify] Capture '00054_vhs_Step23' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step23', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.9999)
    with step("[Verify] Capture '00054_vhs_Step25' before"):
        assert actions.capture_for_preview('00054_vhs_Step25', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Drag positionSlider (93.6%,60.0%) → //XCUIElementTypeOther[@name=\"parametersStackVIew\"]/XCUIElementTypeOther[3] (24.9%,61.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'positionSlider', 93.6, 60.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="parametersStackVIew"]/XCUIElementTypeOther[3]', 24.9, 61.4, duration=1.0)
    with step("[Verify] Capture '00054_vhs_Step25' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step25', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.9999)
    with step("[Verify] positionValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'positionValueLabel', '0')
    with step("[Verify] Capture '00054_vhs_Step29' before"):
        assert actions.capture_for_preview('00054_vhs_Step29', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Drag fadeSlider (8.0%,55.6%) → //XCUIElementTypeOther[@name=\"parametersStackVIew\"]/XCUIElementTypeOther[4] (82.3%,56.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'fadeSlider', 8.0, 55.6, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="parametersStackVIew"]/XCUIElementTypeOther[4]', 82.3, 56.8, duration=1.0)
    with step("[Verify] fadeValueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'fadeValueLabel', '100')
    with step("[Verify] Capture '00054_vhs_Step29' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step29', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step32' before"):
        assert actions.capture_for_preview('00054_vhs_Step32', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Drag fadeSlider (91.7%,66.7%) → //XCUIElementTypeOther[@name=\"parametersStackVIew\"]/XCUIElementTypeOther[4] (24.0%,59.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'fadeSlider', 91.7, 66.7, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="parametersStackVIew"]/XCUIElementTypeOther[4]', 24.0, 59.1, duration=1.0)
    with step("[Verify] fadeValueLabel text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'fadeValueLabel', '0')
    with step("[Verify] Capture '00054_vhs_Step32' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step32', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Action] Drag distortionSlider (8.7%,57.8%) → //XCUIElementTypeOther[@name=\"parametersStackVIew\"]/XCUIElementTypeOther[2] (83.5%,56.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'distortionSlider', 8.7, 57.8, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="parametersStackVIew"]/XCUIElementTypeOther[2]', 83.5, 56.8, duration=1.0)
    with step("[Action] Tap shapeMaskModeButton at (67.5%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskModeButton', 67.5, 57.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=682)
    with step("[Verify] Capture '00054_vhs_Step36' before"):
        assert actions.capture_for_preview('00054_vhs_Step36', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[2]')
    with step("[Action] Tap drop_thumb at (44.4%, 56.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'drop_thumb', 44.4, 56.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='shapeMaskCollectionView', container_w=366, container_h=108)
    with step("[Verify] Capture '00054_vhs_Step36' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step36', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[2]', expected_result='different', threshold=0.9999)
    with step("[Verify] Capture '00054_vhs_Step38' before"):
        assert actions.capture_for_preview('00054_vhs_Step38', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[2]')
    with step("[Action] Tap film_thumb at (58.0%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'film_thumb', 58.0, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='shapeMaskCollectionView', container_w=366, container_h=108)
    with step("[Verify] Capture '00054_vhs_Step38' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step38', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[2]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step40' before"):
        assert actions.capture_for_preview('00054_vhs_Step40', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[2]')
    with step("[Action] Tap shapeMaskInvertButton at (55.0%, 37.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskInvertButton', 55.0, 37.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=682)
    with step("[Verify] Capture '00054_vhs_Step40' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step40', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[2]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step42' before"):
        assert actions.capture_for_preview('00054_vhs_Step42', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[2]')
    with step("[Action] Rotate //XCUIElementTypeScrollView[@name=\"editingImageView\"]/XCUIElementTypeOther[1]/XCUIElementTypeImage[2] 57.3°"):
        actions.rotate(actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]/XCUIElementTypeImage[2]'), rotation=57.3)
    with step("[Verify] Capture '00054_vhs_Step42' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step42', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[2]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step44' before"):
        assert actions.capture_for_preview('00054_vhs_Step44', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Pinch //XCUIElementTypeScrollView[@name=\"editingImageView\"]/XCUIElementTypeOther[2] scale=0.489"):
        actions.pinch(actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[2]'), scale=0.489, velocity=-0.626)
    with step("[Verify] Capture '00054_vhs_Step44' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step44', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step46' before"):
        assert actions.capture_for_preview('00054_vhs_Step46', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Tap btn_cancel_n at (32.7%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 32.7, 46.9)
    with step("[Verify] Capture '00054_vhs_Step46' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step46', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Action] Tap shapeMaskModeButton at (52.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'shapeMaskModeButton', 52.5, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=682)
    with step("[Action] Tap film_thumb at (58.0%, 40.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'film_thumb', 58.0, 40.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='shapeMaskCollectionView', container_w=366, container_h=108)
    with step("[Verify] Capture '00054_vhs_Step50' before"):
        assert actions.capture_for_preview('00054_vhs_Step50', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Tap btn_ok_n at (77.6%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 49.0)
    with step("[Verify] Capture '00054_vhs_Step50' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step50', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step52' before"):
        assert actions.capture_for_preview('00054_vhs_Step52', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap btn_ok_n at (83.7%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 83.7, 44.9)
    with step("[Verify] Capture '00054_vhs_Step52' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step52', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step54' before"):
        assert actions.capture_for_preview('00054_vhs_Step54', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap ic edit undo n at (71.8%, 51.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 71.8, 51.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00054_vhs_Step54' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step54', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Action] Tap btn_VHS at (38.2%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_VHS', 38.2, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Drag distortionSlider (8.7%,60.0%) → //XCUIElementTypeOther[@name=\"parametersStackVIew\"]/XCUIElementTypeOther[2] (80.2%,54.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'distortionSlider', 8.7, 60.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="parametersStackVIew"]/XCUIElementTypeOther[2]', 80.2, 54.5, duration=1.0)
    with step("[Action] Tap brushModeButton at (50.0%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton', 50.0, 45.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=682)
    with step("[Action] Tap btt_brush_n at (55.0%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 55.0, 62.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap btt_eraser_n at (62.5%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 62.5, 80.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] Capture '00054_vhs_Step61' before"):
        assert actions.capture_for_preview('00054_vhs_Step61', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"editingImageView\"]/XCUIElementTypeOther[1] (16.5%,50.7%) → EditingImageView_ImageView (93.0%,51.1%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', 16.5, 50.7, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 93.0, 51.1, duration=1.0)
    with step("[Verify] Capture '00054_vhs_Step61' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step61', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Action] Tap btt_brush_n at (50.0%, 95.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 50.0, 95.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag cpSlider (43.6%,54.8%) → slider (97.8%,68.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 43.6, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 97.8, 68.3, duration=1.0)
    with step("[Verify] Capture '00054_vhs_Step65' before"):
        assert actions.capture_for_preview('00054_vhs_Step65', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"editingImageView\"]/XCUIElementTypeOther[1] (47.9%,6.1%) → EditingImageView_ImageView (47.9%,93.9%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', 47.9, 6.1, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 47.9, 93.9, duration=1.0)
    with step("[Verify] Capture '00054_vhs_Step65' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step65', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Action] Drag cpSlider (93.6%,52.4%) → slider (2.5%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 93.6, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.5, 48.8, duration=1.0)
    with step("[Verify] Capture '00054_vhs_Step68' before"):
        assert actions.capture_for_preview('00054_vhs_Step68', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"editingImageView\"]/XCUIElementTypeOther[1] (20.0%,22.9%) → EditingImageView_ImageView (20.9%,85.0%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', 20.0, 22.9, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 20.9, 85.0, duration=1.0)
    with step("[Verify] Capture '00054_vhs_Step68' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step68', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step70' before"):
        assert actions.capture_for_preview('00054_vhs_Step70', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Tap invertButton at (70.0%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'invertButton', 70.0, 67.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=682)
    with step("[Verify] Capture '00054_vhs_Step70' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step70', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step72' before"):
        assert actions.capture_for_preview('00054_vhs_Step72', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Tap btn_cancel_n at (28.6%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 28.6, 38.8)
    with step("[Verify] Capture '00054_vhs_Step72' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step72', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Action] Tap brushModeButton at (62.5%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'brushModeButton', 62.5, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=682)
    with step("[Action] Tap edgeDetectionButton at (40.0%, 42.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'edgeDetectionButton', 40.0, 42.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='editingImageView', container_w=430, container_h=682)
    with step("[Action] Tap btt_eraser_n at (65.0%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 65.0, 57.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Verify] Capture '00054_vhs_Step77' before"):
        assert actions.capture_for_preview('00054_vhs_Step77', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Drag //XCUIElementTypeScrollView[@name=\"editingImageView\"]/XCUIElementTypeOther[1] (48.8%,7.5%) → EditingImageView_ImageView (52.3%,92.9%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', 48.8, 7.5, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 52.3, 92.9, duration=1.0)
    with step("[Verify] Capture '00054_vhs_Step77' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step77', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step79' before"):
        assert actions.capture_for_preview('00054_vhs_Step79', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]')
    with step("[Action] Tap btn_ok_n at (79.6%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 79.6, 57.1)
    with step("[Verify] Capture '00054_vhs_Step79' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step79', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="editingImageView"]/XCUIElementTypeOther[1]', expected_result='different', threshold=0.999)
    with step("[Verify] Capture '00054_vhs_Step81' before"):
        assert actions.capture_for_preview('00054_vhs_Step81', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap btn_ok_n at (91.8%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 91.8, 53.1)
    with step("[Verify] Capture '00054_vhs_Step81' after — expect changed"):
        assert actions.capture_for_preview('00054_vhs_Step81', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Action] Tap homeButton at (53.8%, 92.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 53.8, 92.3)
    with step("[Action] Tap Discard at (73.9%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 73.9, 58.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.999)
    assert True
