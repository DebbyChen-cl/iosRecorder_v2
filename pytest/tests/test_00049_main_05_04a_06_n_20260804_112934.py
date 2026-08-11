import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00049_main_05_04a_06_n_20260804_112934")
def test_00049_main_05_04a_06_n_20260804_112934(actions: DriverActions):
    with step("[Action] Tap Edit at (45.7%, 72.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 45.7, 72.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (77.2%, 38.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 77.2, 38.1)
    with step("[Action] Tap _AT at (6.5%, 100.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 6.5, 100.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (69.2%, 66.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 69.2, 66.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (55.6%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 55.6, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step06' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step06', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Scroll until ic_instafill"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_instafill', direction='left', offset_start=(0.788, 0.464), offset_end=(0.277, 0.464), velocity=274)
    with step("[Action] Tap ic_instafill at (50.0%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_instafill', 50.0, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step09' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step09', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_4v3 at (73.2%, 68.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_4v3', 73.2, 68.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='instaFillAspectRatioSelectionPanelCollectionView', container_w=430, container_h=76)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step11' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step11', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_3v2 at (56.1%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_3v2', 56.1, 58.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='instaFillAspectRatioSelectionPanelCollectionView', container_w=430, container_h=76)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step13' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step13', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]', threshold=0.95)
    with step("[Action] Tap ic_16v9 at (55.0%, 65.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_16v9', 55.0, 65.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='instaFillAspectRatioSelectionPanelCollectionView', container_w=430, container_h=76)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step15' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step15', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag control_dot (75.0%,83.3%) → //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3] (40.9%,1.6%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'control_dot', 75.0, 83.3, AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]', 40.9, 1.6, duration=1.0)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step17' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step17', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_IG1v1 at (47.5%, 85.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_IG1v1', 47.5, 85.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='instaFillAspectRatioSelectionPanelCollectionView', container_w=430, container_h=76)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step19' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step19', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_IG9v16 at (24.4%, 68.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_IG9v16', 24.4, 68.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='instaFillAspectRatioSelectionPanelCollectionView', container_w=431, container_h=76)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step21' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step21', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_FB1v1 at (29.3%, 51.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_FB1v1', 29.3, 51.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='instaFillAspectRatioSelectionPanelCollectionView', container_w=430, container_h=76)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step23' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step23', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap ic_FBCover at (17.1%, 63.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_FBCover', 17.1, 63.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='instaFillAspectRatioSelectionPanelCollectionView', container_w=430, container_h=76)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step25' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step25', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Drag cpSlider (50.6%,56.0%) → slider (98.1%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 50.6, 56.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.1, 53.1, duration=1.0)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step27' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step27', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag cpSlider (92.3%,60.0%) → slider (2.3%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 92.3, 60.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.3, 57.1, duration=1.0)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step29' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step29', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag cpSlider (9.6%,48.0%) → slider (99.2%,57.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 9.6, 48.0, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.2, 57.1, duration=1.0)
    with step("[Action] Tap NonScrollableMenuView-1 at (52.7%, 73.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'NonScrollableMenuView-1', 52.7, 73.9)
    with step("[Action] Tap pickedColorView at (66.1%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'pickedColorView', 66.1, 42.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]', container_w=408, container_h=71)
    with step("[Action] Tap gradientColorPanel at (67.6%, 77.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'gradientColorPanel', 67.6, 77.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]', container_w=408, container_h=71)
    with step("[Action] Tap Done at (36.4%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'doneButton', 36.4, 52.2)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step35' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step35', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btn_addimg_n at (45.0%, 51.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_addimg_n', 45.0, 51.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]', container_w=408, container_h=71)
    with step("[Action] Tap btnAlbum at (80.7%, 31.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 80.7, 31.0)
    with step("[Action] Tap BG at (8.2%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'BG', 8.2, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (43.8%, 64.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 43.8, 64.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step40' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step40', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap CMS- at (50.0%, 74.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-', 50.0, 74.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]', container_w=408, container_h=71)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step42' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step42', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther', threshold=0.95)
    # with step("[Action] Tap CMS- at (50.0%, 61.9%)"):
    #     actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-', 50.0, 61.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]', container_w=408, container_h=71)
    # with step("[Verify] Capture '00049_main_05_04a_06_n_Step44' for GT comparison"):
    #     actions.capture_for_gt('00049_main_05_04a_06_n_Step44', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap pickedColorView at (66.1%, 42.9%)"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'pickedColorView', 66.1, 42.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]', container_w=408, container_h=71)
    with step("[Action] Close color picker"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    with step("[Action] Tap btn_cancel_n at (30.6%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 30.6, 40.8)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step47' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step47', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic_instafill at (64.7%, 78.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_instafill', 64.7, 78.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_ok_n at (85.7%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 85.7, 40.8)
    with step("[Verify] Capture '00049_main_05_04a_06_n_Step50' for GT comparison"):
        actions.capture_for_gt('00049_main_05_04a_06_n_Step50', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (69.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 69.2, 50.0)
    with step("[Action] Tap Discard at (75.4%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 75.4, 75.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
