import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


def _drag_slider(actions: DriverActions, start_pct: float, end_pct: float) -> None:
    actions.drag_within_elements(
        AppiumBy.ACCESSIBILITY_ID,
        "cpSlider",
        start_pct,
        50.0,
        AppiumBy.ACCESSIBILITY_ID,
        "cpSlider",
        end_pct,
        50.0,
        duration=0.5,
    )


@pytest.mark.name("makeup_look")
def test_makeup_look(actions: DriverActions, reset_app):
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"edit\"]/XCUIElementTypeOther at (49.2%, 48.0%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="edit"]/XCUIElementTypeOther', 49.2, 48.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=320, container_h=623)
    with step("[Action] Expand album list"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 50.0, 50.0)
    with step("[Action] Tap Sample Photos at (34.1%, 52.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 34.1, 52.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=294, container_h=557)
    with step("[Action] Tap PhDM_example_3 at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_3', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=320, container_h=557)
    with step("[Action] Tap Portrait at (49.1%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 49.1, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=320, container_h=33)
    with step("[Action] Tap icon_makeup at (50.0%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_makeup', 50.0, 80.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=320, container_h=72)
    with step("[Verify] btn_no is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btn_no')
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='same', threshold=0.99)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Daily at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Daily', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '71'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '71') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 71.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Chestnut at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Chestnut', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '76'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '76') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 71.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Neutral at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Neutral', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '62'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '62') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 62.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Lavish at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Lavish', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '76'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '76') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 76.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Peach at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Peach', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '83'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '83') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 83.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Charming at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Charming', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '83'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '83') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 83.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Tender at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Tender', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '83'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '83') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 83.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Aesthetic at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Aesthetic', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '83'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '83') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 83.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Bright at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Bright', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '76'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '76') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 76.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Smoky at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Smoky', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '83'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '83') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 83.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Orange at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Orange', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '76'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '76') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 76.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Glowy at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Glowy', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '62'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '62') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 62.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Elegant at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Elegant', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '90'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '90') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 90.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Spring at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Spring', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '90'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '90') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 90.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Vitality at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Vitality', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '90'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '90') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 90.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Energetic at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Energetic', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '90'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '90') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 90.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Alluring at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Alluring', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '89'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '89') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 89.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Chic at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Chic', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '83'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '83') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 83.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Party at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Party', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '88'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '88') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 88.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Adorable at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Adorable', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=320, container_h=66)
    with step("[Verify] valueLabel text equals '90'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '90') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to minimum"):
        _drag_slider(actions, 90.0, 1.0)
    with step("[Verify] valueLabel text equals '1'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '1') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        assert actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag cpSlider to maximum"):
        _drag_slider(actions, 1.0, 100.0)
    with step("[Verify] valueLabel text equals '100'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Capture 'screenshot' after screenshot"):
        assert actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.999)
    with step("[Verify] Screenshot comparisons"):
        assert actions.run_screenshot_comparisons(threshold=0.99) is not False
    assert True
