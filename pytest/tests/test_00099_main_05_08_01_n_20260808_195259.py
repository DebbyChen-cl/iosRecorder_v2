import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00099_main_05_08_01_n_20260808_195259")
def test_00099_main_05_08_01_n_20260808_195259(actions: DriverActions):
    with step("[Action] Tap Edit at (34.3%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 34.3, 48.0)
    with step("[Action] Tap btnAlbum at (72.1%, 40.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 72.1, 40.5)
    with step("[Action] Tap _AT at (11.8%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 11.8, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (52.3%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 52.3, 57.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (53.3%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 53.3, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Text"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Text', direction='right', offset_start=(0.132, 0.443), offset_end=(0.817, 0.443), velocity=704)
    with step("[Action] Tap Text at (56.3%, 7.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text', 56.3, 7.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Text at (53.2%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text', 53.2, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap btnTextEdit at (63.0%, 22.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTextEdit', 63.0, 22.2)
    with step("[Action] Tap A at (51.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'A', 51.2, 50.0)
    with step("[Action] Tap a at (51.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'a', 51.2, 50.0)
    with step("[Action] Tap a at (51.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'a', 51.2, 50.0)
    with step("[Action] Tap Return at (54.2%, 35.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Return', 54.2, 35.7)
    with step("[Action] Tap A at (53.5%, 44.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'A', 53.5, 44.6)
    with step("[Action] Tap leftAlignmentButton at (75.7%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'leftAlignmentButton', 75.7, 50.0)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step17' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step17', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap centerAlignmentButton at (70.3%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'centerAlignmentButton', 70.3, 69.4)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step19' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step19', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap rightAlignmentButton at (43.2%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'rightAlignmentButton', 43.2, 41.7)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step21' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step21', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap applyButton at (29.5%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'applyButton', 29.5, 54.5)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step23' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step23', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Drag imageView (51.4%,49.2%) → backgroundView (50.9%,36.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'imageView', 51.4, 49.2, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 50.9, 36.3, duration=1.0)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step25' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step25', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (80.0%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 80.0, 34.7)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step27' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step27', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_redo at (44.0%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 44.0, 38.8)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step29' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step29', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (32.0%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 32.0, 53.1)
    with step("[Action] Drag imageView (61.0%,54.8%) → backgroundView (66.5%,36.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'imageView', 61.0, 54.8, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 66.5, 36.7, duration=1.0)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step32' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step32', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Drag rotateImageView (48.1%,55.6%) → backgroundView (33.5%,31.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'rotateImageView', 48.1, 55.6, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 33.5, 31.7, duration=1.0)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step34' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step34', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Rotate imageView 45.0°"):
        actions.rotate(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'imageView'), rotation=45.0)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step36' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step36', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap btnDuplicate at (66.7%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDuplicate', 66.7, 44.4)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step38' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step38', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap ic_undo at (52.0%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 52.0, 32.7)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step40' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step40', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap imageView at (50.0%, 49.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 50.0, 49.1)
    with step("[Action] Tap btnTextEdit at (74.1%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTextEdit', 74.1, 55.6)
    with step("[Action] Tap delete at (55.4%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'delete', 55.4, 42.9)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step44' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step44', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap applyButton at (52.3%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'applyButton', 52.3, 50.0)
    with step("[Action] Tap ic_undo at (64.0%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 64.0, 40.8)
    with step("[Action] Tap maskButton at (52.5%, 46.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'maskButton', 52.5, 46.3)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther (3.0%,50.0%) → //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage (88.2%,48.3%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther', 3.0, 50.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage', 88.2, 48.3, duration=1.0)
    with step("[Action] Tap btn_ok_n at (75.5%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 55.1)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step50' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step50', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap maskButton at (60.0%, 63.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'maskButton', 60.0, 63.4)
    with step("[Action] Tap Brush at (62.9%, 27.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Brush', 62.9, 27.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="menuView"]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther (4.7%,50.0%) → //XCUIElementTypeOther[@name=\"MaskingViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage (89.2%,50.0%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther', 4.7, 50.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MaskingViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage', 89.2, 50.0, duration=1.0)
    with step("[Action] Tap btn_ok_n at (59.2%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 59.2, 26.5)
    with step("[Verify] Capture '00099_main_05_08_01_n_Step55' for GT comparison"):
        actions.capture_for_gt('00099_main_05_08_01_n_Step55', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap maskButton at (52.5%, 46.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'maskButton', 52.5, 46.3)
    with step("[Action] Drag cpSlider (45.6%,47.6%) → sliderArea (2.3%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 45.6, 47.6, AppiumBy.ACCESSIBILITY_ID, 'sliderArea', 2.3, 57.1, duration=1.0)
    with step("[Verify] valueLabel text equals '8'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '8')
    with step("[Action] Drag cpSlider (5.0%,42.9%) → valueLabel (3.1%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 5.0, 42.9, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 3.1, 56.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap btn_cancel_n at (44.9%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 44.9, 38.8)
    with step("[Action] Tap btn_cancel_n at (24.5%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 24.5, 46.9)
    with step("[Action] Tap homeButton at (50.0%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 50.0, 76.9)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
