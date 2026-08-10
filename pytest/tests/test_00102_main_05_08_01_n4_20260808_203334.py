import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00102_main_05_08_01_n4_20260808_203334")
def test_00102_main_05_08_01_n4_20260808_203334(actions: DriverActions):
    with step("[Action] Tap Edit at (88.6%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 88.6, 56.0)
    with step("[Action] Tap btnAlbum at (72.6%, 40.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 72.6, 40.5)
    with step("[Action] Tap _AT at (11.8%, 40.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 11.8, 40.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (44.6%, 49.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 44.6, 49.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (53.3%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 53.3, 46.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Text"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Text', direction='left', offset_start=(0.263, 0.392), offset_end=(0.181, 0.392), velocity=50)
    with step("[Action] Tap Text at (58.3%, 21.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text', 58.3, 21.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Text at (55.8%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Text', 55.8, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Scroll until Colorful"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'titleCollectionViewCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Colorful', direction='left', offset_start=(0.707, 0.489), offset_end=(0.477, 0.489), velocity=128)
    with step("[Action] Tap Colorful at (45.7%, 59.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Colorful', 45.7, 59.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=431, container_h=45)
    with step("[Action] Drag imageView (74.5%,54.1%) → backgroundView (79.5%,37.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'imageView', 74.5, 54.1, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 79.5, 37.7, duration=1.0)
    with step("[Verify] Capture '00102_main_05_08_01_n4_Step12' for GT comparison"):
        actions.capture_for_gt('00102_main_05_08_01_n4_Step12', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap leaveButton at (47.5%, 51.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'leaveButton', 47.5, 51.2)
    with step("[Verify] mainPanel is not visible"):
        actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'mainPanel')
    with step("[Action] Tap imageView at (48.1%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 48.1, 50.0)
    with step("[Action] Tap Colorful at (28.6%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Colorful', 28.6, 53.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=45)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CMS-phdm_text_style_yellow_12_new\"]/XCUIElementTypeOther/XCUIElementTypeImage at (58.9%, 46.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-phdm_text_style_yellow_12_new"]/XCUIElementTypeOther/XCUIElementTypeImage', 58.9, 46.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='presetCollectionView', container_w=430, container_h=241)
    with step("[Verify] Capture '00102_main_05_08_01_n4_Step18' for GT comparison"):
        actions.capture_for_gt('00102_main_05_08_01_n4_Step18', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CMS-phdm_text_style_yellow_18_new\"]/XCUIElementTypeOther/XCUIElementTypeImage at (48.6%, 53.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-phdm_text_style_yellow_18_new"]/XCUIElementTypeOther/XCUIElementTypeImage', 48.6, 53.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='presetCollectionView', container_w=430, container_h=241)
    with step("[Verify] Capture '00102_main_05_08_01_n4_Step20' for GT comparison"):
        actions.capture_for_gt('00102_main_05_08_01_n4_Step20', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CMS-phdm_text_style_yellow_20_new\"]/XCUIElementTypeOther/XCUIElementTypeImage at (75.7%, 81.2%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-phdm_text_style_yellow_20_new"]/XCUIElementTypeOther/XCUIElementTypeImage', 75.7, 81.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='presetCollectionView', container_w=430, container_h=241)
    with step("[Verify] Capture '00102_main_05_08_01_n4_Step22' for GT comparison"):
        actions.capture_for_gt('00102_main_05_08_01_n4_Step22', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap Background at (37.8%, 71.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Background', 37.8, 71.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=45)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CMS-phdm_text_style_202212_004\"]/XCUIElementTypeOther/XCUIElementTypeImage at (17.0%, 77.9%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-phdm_text_style_202212_004"]/XCUIElementTypeOther/XCUIElementTypeImage', 17.0, 77.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='presetCollectionView', container_w=430, container_h=241)
    with step("[Verify] Capture '00102_main_05_08_01_n4_Step25' for GT comparison"):
        actions.capture_for_gt('00102_main_05_08_01_n4_Step25', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CMS-phdm_text_style_202508_008\"]/XCUIElementTypeOther/XCUIElementTypeImage[1] at (24.3%, 77.9%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-phdm_text_style_202508_008"]/XCUIElementTypeOther/XCUIElementTypeImage[1]', 24.3, 77.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='presetCollectionView', container_w=430, container_h=241)
    with step("[Verify] Capture '00102_main_05_08_01_n4_Step27' for GT comparison"):
        actions.capture_for_gt('00102_main_05_08_01_n4_Step27', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CMS-phdm_text_style_202508_011\"]/XCUIElementTypeOther/XCUIElementTypeImage at (26.1%, 60.0%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-phdm_text_style_202508_011"]/XCUIElementTypeOther/XCUIElementTypeImage', 26.1, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='presetCollectionView', container_w=430, container_h=241)
    with step("[Verify] Capture '00102_main_05_08_01_n4_Step29' for GT comparison"):
        actions.capture_for_gt('00102_main_05_08_01_n4_Step29', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CMS-phdm_text_style_202508_015\"]/XCUIElementTypeOther/XCUIElementTypeImage[1] at (50.9%, 48.2%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-phdm_text_style_202508_015"]/XCUIElementTypeOther/XCUIElementTypeImage[1]', 50.9, 48.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='presetCollectionView', container_w=430, container_h=241)
    with step("[Verify] Capture '00102_main_05_08_01_n4_Step31' for GT comparison"):
        actions.capture_for_gt('00102_main_05_08_01_n4_Step31', AppiumBy.ACCESSIBILITY_ID, 'imageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (87.8%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 87.8, 34.7)
    with step("[Action] Tap btnClose at (32.3%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 32.3, 48.4)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CMS-phdm_text_style_202508_011\"]/XCUIElementTypeOther/XCUIElementTypeImage at (47.7%, 49.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-phdm_text_style_202508_011"]/XCUIElementTypeOther/XCUIElementTypeImage', 47.7, 49.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='presetCollectionView', container_w=430, container_h=241)
    with step("[Action] Tap btn_ok_n at (73.5%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 34.7)
    with step("[Action] Tap OK at (63.3%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 63.3, 41.7)
    with step("[Action] Tap homeButton at (65.4%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 53.8)
    with step("[Action] Tap Discard at (66.7%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 66.7, 41.7)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
