import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00026_removal_manual')
def test_00026_removal_manual(actions: DriverActions):
    """removal - manual"""
    mode = 1
    uuid = ['d4f06494-5d67-4d1c-b1b8-71cadbcf72e1', '4bb879a8-1039-4ba9-82d2-1f347c0e9817', '1064c782-d448-4044-8d68-ed0a799a4492', '45871133-6a98-4e0a-ac1d-a3602d42b92d', '5b2c27cd-6b54-47a6-856d-e133c76f8a10', '91c8fba9-6f1c-448f-8848-d22a963ccc45', '14625380-842b-43db-949b-6313d32f491d', 'edbc569a-2d50-4948-a175-ebcadc8607cc', 'a7e6f0e3-386a-4c62-8c50-2d41adf106ab', 'c6d321b3-e4d0-49b9-a37c-8a800bde0210', '76774317-1f08-4488-bfc2-6fef0b44bfad', '4410d745-9496-40c7-afc1-65ecc7283dde', '6499b7bd-3ec6-45a9-8fdc-10e7cf113b84', '80f4e7d6-4ff6-4757-b768-5083e4d86105', '21d6d66b-0240-4050-b4c2-a244efad0d34', '8ab17e86-21ed-4db6-97d1-622d2c708f21', '602cf00d-f0bf-40b3-93b8-e46d11b617ae', '3ee8746f-fdd0-43ed-a7ec-2e610c044f24', '7744e8c0-2fac-4c85-a7f5-2152d846de21']

    with step("[Action] Tap Edit at (57.1%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 57.1, 40.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (80.7%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 80.7, 54.8)
    with step("[Action] Tap _AT at (8.2%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 8.2, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (45.4%, 50.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 45.4, 50.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap icon_removal at (36.4%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_removal', 36.4, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Try First at (2.9%, 37.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try First', 2.9, 37.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='RemovalEditingImageView', container_w=430, container_h=630)
    with step("[Action] Tap Manual at (58.8%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Manual', 58.8, 33.3)
    with step("[Action] Drag cpSlider (24.4%,48.0%) → backgroundView (27.0%,80.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 24.4, 48.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 27.0, 80.7, duration=1.0)
    with step("[Verify] valueLabel text equals '8'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '8')
    with step("[Action] Drag cpSlider (7.4%,46.0%) → backgroundView (86.3%,81.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.4, 46.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 86.3, 81.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag EditingImageView_ImageView (54.0%,17.5%) → backgroundView (55.6%,49.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 54.0, 17.5, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 55.6, 49.1, duration=1.0)
    with step("[Verify] Capture 'Removal_Step13' for GT comparison"):
        actions.capture_for_gt('Removal_Step13', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag EditingImageView_ImageView (15.6%,52.5%) → backgroundView (58.4%,41.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 15.6, 52.5, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 58.4, 41.2, duration=1.0)
    with step("[Verify] Capture 'Removal_Step15' for GT comparison"):
        actions.capture_for_gt('Removal_Step15', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap undoButton at (35.0%, 32.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 35.0, 32.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='RemovalEditingImageView', container_w=430, container_h=630)
    with step("[Verify] Capture 'Removal_Step17' for GT comparison"):
        actions.capture_for_gt('Removal_Step17', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap redoButton at (82.5%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'redoButton', 82.5, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='RemovalEditingImageView', container_w=430, container_h=630)
    with step("[Verify] Capture 'Removal_Step19' for GT comparison"):
        actions.capture_for_gt('Removal_Step19', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btt_eraser_n at (47.5%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n', 47.5, 57.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushEraserView"]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag EditingImageView_ImageView (10.9%,51.4%) → backgroundView (69.8%,40.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 10.9, 51.4, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 69.8, 40.5, duration=1.0)
    with step("[Verify] Capture 'Removal_Step22' for GT comparison"):
        actions.capture_for_gt('Removal_Step22', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap applyButton at (88.5%, 74.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'applyButton', 88.5, 74.1)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.95)
    with step("[Action] Tap undoButton at (52.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 52.5, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='RemovalEditingImageView', container_w=430, container_h=630)
    with step("[Verify] Capture 'Removal_Step27' for GT comparison"):
        actions.capture_for_gt('Removal_Step27', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap redoButton at (40.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'redoButton', 40.0, 52.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='RemovalEditingImageView', container_w=430, container_h=630)
    with step("[Verify] Capture 'Removal_Step29' for GT comparison"):
        actions.capture_for_gt('Removal_Step29', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (28.6%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 28.6, 28.6)
    with step("[Action] Tap icon_removal at (75.8%, 78.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_removal', 75.8, 78.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Manual at (68.6%, 88.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Manual', 68.6, 88.9)
    with step("[Action] Drag cpSlider (24.7%,52.0%) → backgroundView (84.4%,80.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 24.7, 52.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 84.4, 80.7, duration=1.0)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Drag EditingImageView_ImageView (54.7%,15.0%) → backgroundView (55.8%,53.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 54.7, 15.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 55.8, 53.9, duration=1.0)
    with step("[Action] Tap Remove at (81.8%, 87.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Remove', 81.8, 87.0)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (93.9%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 93.9, 34.7)
    with step("[Verify] Continue is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnClose at (61.3%, 71.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 61.3, 71.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (38.8%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 38.8, 28.6)
    with step("[Action] Tap homeButton at (76.9%, 88.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 76.9, 88.5)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True

    with step("[Verify] test_00026 completion"):
        assert True
