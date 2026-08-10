import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_00153_main_11_01_02_20260806_173039")
def test_00153_main_11_01_02_20260806_173039(actions: DriverActions):
    with step("[Action] Tap btnSettings at (57.6%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 57.6, 50.0)
    with step("[Action] Tap About at (15.7%, 87.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 15.7, 87.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (46.9%, 38.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 46.9, 38.0)
    with step("[Action] Tap Free at (50.0%, 57.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 50.0, 57.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (52.8%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 52.8, 53.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (75.0%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 75.0, 55.6)
    with step("[Action] Tap btnBack at (53.6%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 53.6, 48.9)
    with step("[Action] Tap btnBack at (39.3%, 40.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 39.3, 40.4)
    with step("[Action] Tap Edit at (45.7%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 45.7, 64.0)
    with step("[Action] Tap photoCell-0 at (40.8%, 75.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 40.8, 75.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Enhance at (54.8%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 54.8, 62.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap icon_AIenhance_110 at (60.6%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_AIenhance_110', 60.6, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn close outline n at (59.3%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n', 59.3, 44.4)
    with step("[Action] Tap Enhance at (50.7%, 79.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 50.7, 79.2)
    with step("[Verify] advancedWaitLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'advancedWaitLabel', appear_timeout=5, disappear_timeout=1200), 'advancedWaitLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btn_ok_n at (85.7%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 85.7, 44.9)
    with step("[Verify] Capture '00152_main_11_01_01_Step16' for GT comparison"):
        actions.capture_for_gt('00152_main_11_01_01_Step16', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.8)
    with step("[Action] Tap ic edit undo n at (71.8%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 71.8, 53.8)
    with step("[Action] Tap Edit at (69.6%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 69.6, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap icon_removal at (60.6%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_removal', 60.6, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Try First at (66.2%, 45.8%)"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Try First'):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try First', 66.2, 45.8)
    with step("[Action] Tap Manual at (49.0%, 38.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Manual', 49.0, 38.9)
    with step("[Action] Drag cpSlider (22.1%,52.0%) → backgroundView (87.4%,81.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 22.1, 52.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 87.4, 81.3, duration=1.0)
    with step("[Action] Drag EditingImageView_ImageView (54.7%,15.7%) → backgroundView (56.5%,52.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 54.7, 15.7, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 56.5, 52.4, duration=1.0)
    with step("[Action] Tap Remove at (48.5%, 26.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Remove', 48.5, 26.1)
    with step("[Verify] magicText disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'magicText', appear_timeout=5, disappear_timeout=1200), 'magicText did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btn_ok_n at (71.4%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 71.4, 36.7)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap ic edit undo n at (59.0%, 48.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 59.0, 48.7)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', expected_result='different', threshold=0.95)
    with step("[Action] Tap Enhance at (67.9%, 68.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 67.9, 68.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until icon_deblur"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'icon_deblur', direction='left', offset_start=(0.598, 0.474), offset_end=(0.335, 0.474), velocity=195)
    with step("[Action] Tap icon_deblur at (58.8%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_deblur', 58.8, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn close outline n at (51.9%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n', 51.9, 44.4)
    with step("[Action] Drag cpSlider (7.7%,48.0%) → backgroundView (85.6%,88.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.7, 48.0, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 85.6, 88.5, duration=1.0)
    with step("[Action] Tap btn_ok_n at (73.5%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 26.5)
    with step("[Verify] Capture '00152_main_11_01_01_Step35' for GT comparison"):
        actions.capture_for_gt('00152_main_11_01_01_Step35', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (43.6%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 43.6, 53.8)
    with step("[Action] Tap Enhance at (57.1%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 57.1, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until icon_denoise"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'icon_denoise', direction='left', offset_start=(0.551, 0.402), offset_end=(0.242, 0.402), velocity=235)
    with step("[Action] Tap icon_denoise at (39.4%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_denoise', 39.4, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Denoise at (34.2%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Denoise', 34.2, 58.3)
    with step("[Verify] downloadingAssetText disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'downloadingAssetText', appear_timeout=5, disappear_timeout=1200), 'downloadingAssetText did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btn_ok_n at (89.8%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 89.8, 32.7)
    with step("[Verify] Capture '00152_main_11_01_01_Step42' for GT comparison"):
        actions.capture_for_gt('00152_main_11_01_01_Step42', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (73.1%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 73.1, 73.1)
    with step("[Action] Tap Discard at (72.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 72.5, 50.0)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
