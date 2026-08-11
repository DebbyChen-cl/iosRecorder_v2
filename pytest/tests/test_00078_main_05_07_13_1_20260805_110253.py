import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00078_main_05_07_13_1_20260805_110253")
def test_00078_main_05_07_13_1_20260805_110253(actions: DriverActions):
    with step("[Action] Tap Edit at (85.7%, 36.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 85.7, 36.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (70.1%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 70.1, 61.9)
    with step("[Action] Tap _AT at (7.5%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.5, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (35.4%, 76.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 35.4, 76.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (63.5%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 63.5, 48.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (84.8%, 39.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 84.8, 39.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_conceal_portrait at (57.6%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 57.6, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_wrinkle at (73.5%, 27.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_wrinkle', 73.5, 27.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Verify] barImageView disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'barImageView', appear_timeout=5, disappear_timeout=1200), 'barImageView did not appear within 5s or is still shown after 1200s'
    with step("[Verify] 50 text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '50', '50')
    with step("[Verify] Capture '00078_main_05_07_13_1_Step10' for GT comparison"):
        actions.capture_for_gt('00078_main_05_07_13_1_Step10', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureWrinkleViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureWrinkleViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeSlider (51.4%,45.2%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureWrinkleViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4] (4.0%,59.2%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureWrinkleViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeSlider', 51.4, 45.2, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureWrinkleViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]', 4.0, 59.2, duration=1.0)
    with step("[Verify] 0 text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '0', '0')
    with step("[Verify] Capture '00078_main_05_07_13_1_Step13' for GT comparison"):
        actions.capture_for_gt('00078_main_05_07_13_1_Step13', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureWrinkleViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureWrinkleViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeSlider (5.0%,64.3%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureWrinkleViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4] (84.0%,59.2%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureWrinkleViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeSlider', 5.0, 64.3, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureWrinkleViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]', 84.0, 59.2, duration=1.0)
    with step("[Verify] 100 text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '100', '100')
    with step("[Verify] Capture '00078_main_05_07_13_1_Step16' for GT comparison"):
        actions.capture_for_gt('00078_main_05_07_13_1_Step16', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureWrinkleViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_undo at (57.1%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 57.1, 44.9)
    with step("[Verify] 0 text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '0', '0')
    with step("[Verify] Capture '00078_main_05_07_13_1_Step19' for GT comparison"):
        actions.capture_for_gt('00078_main_05_07_13_1_Step19', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureWrinkleViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_redo at (71.4%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 71.4, 53.1)
    with step("[Verify] 100 text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '100', '100')
    with step("[Verify] Capture '00078_main_05_07_13_1_Step22' for GT comparison"):
        actions.capture_for_gt('00078_main_05_07_13_1_Step22', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureWrinkleViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (87.8%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 87.8, 42.9)
    with step("[Action] Tap btnClose at (45.2%, 41.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 45.2, 41.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btn_cancel_n at (18.4%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 18.4, 30.6)
    with step("[Action] Tap btn_cancel_n at (34.7%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 34.7, 42.9)
    with step("[Action] Tap homeButton at (65.4%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 57.7)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
