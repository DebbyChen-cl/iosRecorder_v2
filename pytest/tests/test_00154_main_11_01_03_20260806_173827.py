import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00154_main_11_01_03_20260806_173827")
def test_00154_main_11_01_03_20260806_173827(actions: DriverActions):
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
    with step("[Action] Tap Edit at (57.1%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 57.1, 56.0)
    with step("[Action] Tap btnAlbum at (66.5%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 66.5, 52.4)
    with step("[Action] Tap _AT at (9.0%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.0, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (41.5%, 76.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 41.5, 76.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (60.8%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 60.8, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_beautify at (48.5%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 48.5, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_makeup_portrait at (30.3%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_makeup_portrait', 30.3, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Lipstick at (57.8%, 55.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Lipstick', 57.8, 55.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='makeupCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap Nude 01 at (57.7%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Nude 01', 57.7, 61.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuDescriptionViewCollectionView', container_w=430, container_h=88)
    with step("[Action] Tap btn_ok_n at (95.9%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 95.9, 34.7)
    with step("[Verify] Capture '00154_main_11_01_03_Step19' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step19', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (49.0%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 49.0, 38.8)
    with step("[Action] Tap ic_auto_retouch at (24.2%, 27.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_auto_retouch', 24.2, 27.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_ok_n at (79.6%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 79.6, 34.7)
    with step("[Verify] Capture '00154_main_11_01_03_Step23' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step23', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (55.1%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 55.1, 28.6)
    with step("[Action] Tap ic_face_reshape_portrait at (75.8%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_reshape_portrait', 75.8, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Face at (54.1%, 55.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Face', 54.1, 55.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='categoryCollectionView', container_w=430, container_h=40)
    with step("[Action] Drag centerSlider (49.7%,56.0%) → //XCUIElementTypeOther[@name=\"photodirector.FacialFeatureReshapeViewController\"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1] (79.5%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 49.7, 56.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.FacialFeatureReshapeViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]', 79.5, 53.1, duration=1.0)
    with step("[Action] Tap btn_ok_n at (65.3%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 65.3, 38.8)
    with step("[Verify] Capture '00154_main_11_01_03_Step29' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step29', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (77.6%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 77.6, 28.6)
    with step("[Action] Tap ic_conceal_portrait at (15.2%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 15.2, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_conceal_portrait at (55.9%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 55.9, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Verify] //XCUIElementTypeCell[@name=\"CircleMenuCell-0\"]/XCUIElementTypeImage is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CircleMenuCell-0"]/XCUIElementTypeImage')
    with step("[Action] Tap btn_ok_n at (65.3%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 65.3, 40.8)
    with step("[Verify] Capture '00154_main_11_01_03_Step34' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step34', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (51.0%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 51.0, 55.1)
    with step("[Action] Tap ic_conceal_portrait at (45.5%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 45.5, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_skintone_portrait at (11.8%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_skintone_portrait', 11.8, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Action] Tap cellColor-1 at (51.6%, 38.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'cellColor-1', 51.6, 38.7)
    with step("[Action] Tap btn_ok_n at (63.3%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 63.3, 34.7)
    with step("[Verify] Capture '00154_main_11_01_03_Step40' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step40', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (55.1%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 55.1, 59.2)
    with step("[Action] Tap ic_conceal_portrait at (75.8%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 75.8, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_jawline at (29.4%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_jawline', 29.4, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Action] Tap btn_ok_n at (83.7%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 83.7, 38.8)
    with step("[Verify] Capture '00154_main_11_01_03_Step45' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step45', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (81.6%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 81.6, 40.8)
    with step("[Action] Tap ic_conceal_portrait at (57.6%, 78.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 57.6, 78.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_double_chin at (67.6%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_double_chin', 67.6, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Action] Tap btn_ok_n at (85.7%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 85.7, 44.9)
    with step("[Verify] Capture '00154_main_11_01_03_Step50' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step50', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (71.4%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 71.4, 26.5)
    with step("[Action] Tap ic_conceal_portrait at (69.7%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 69.7, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_wrinkle at (70.6%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_wrinkle', 70.6, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Action] Tap btn_ok_n at (87.8%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 87.8, 46.9)
    with step("[Verify] Capture '00154_main_11_01_03_Step55' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step55', AppiumBy.ACCESSIBILITY_ID, '0%, 6%, 13%, 22%, 25%, 31%, 38%, 45%, 52%, 60%, 69%, 77%, 84%, 50', threshold=0.95)
    with step("[Action] Tap ic_undo at (75.5%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 75.5, 46.9)
    with step("[Action] Tap ic_conceal_portrait at (63.6%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 63.6, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_blemish at (29.4%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_blemish', 29.4, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Action] Tap btn_ok_n at (95.9%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 95.9, 28.6)
    with step("[Verify] Capture '00154_main_11_01_03_Step60' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step60', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (51.0%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 51.0, 49.0)
    with step("[Action] Scroll until ic_plumpness"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'photoEditFeatureCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_plumpness', direction='left', offset_start=(0.649, 0.381), offset_end=(0.112, 0.381), velocity=514)
    with step("[Action] Tap ic_plumpness at (39.4%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_plumpness', 39.4, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_ok_n at (75.5%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 46.9)
    with step("[Verify] Capture '00154_main_11_01_03_Step65' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step65', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (63.3%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 63.3, 49.0)
    with step("[Action] Tap ic_teeth_whiten_portrait at (75.8%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_teeth_whiten_portrait', 75.8, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_ok_n at (67.3%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 67.3, 53.1)
    with step("[Verify] Capture '00154_main_11_01_03_Step69' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step69', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (61.2%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 61.2, 53.1)
    with step("[Action] Tap ic_eye at (18.2%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_eye', 18.2, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_eye_brighten_portrait at (69.7%, 42.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_eye_brighten_portrait', 69.7, 42.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap btn_ok_n at (93.9%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 93.9, 44.9)
    with step("[Verify] Capture '00154_main_11_01_03_Step74' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step74', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (65.3%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 65.3, 69.4)
    with step("[Action] Tap ic_eye at (60.6%, 87.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_eye', 60.6, 87.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_eyebag_removal at (63.6%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_eyebag_removal', 63.6, 72.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap btn_ok_n at (83.7%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 83.7, 49.0)
    with step("[Verify] Capture '00154_main_11_01_03_Step79' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step79', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (53.1%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 53.1, 26.5)
    with step("[Action] Tap ic_conceal_portrait at (66.7%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 66.7, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_oilness at (82.4%, 84.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_oilness', 82.4, 84.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Action] Tap btn_ok_n at (79.6%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 79.6, 49.0)
    with step("[Verify] Capture '00154_main_11_01_03_Step84' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step84', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (77.6%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 77.6, 46.9)
    with step("[Action] Tap ic_conceal_portrait at (69.7%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 69.7, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_nose_enhance at (58.8%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_nose_enhance', 58.8, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionView', container_w=406, container_h=161)
    with step("[Action] Tap btn_ok_n at (87.8%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 87.8, 51.0)
    with step("[Verify] Capture '00154_main_11_01_03_Step89' for GT comparison"):
        actions.capture_for_gt('00154_main_11_01_03_Step89', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="imageScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (44.9%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 44.9, 51.0)
    with step("[Action] Tap btn_cancel_n at (40.8%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 40.8, 53.1)
    with step("[Action] Tap homeButton at (73.1%, 65.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 73.1, 65.4)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
