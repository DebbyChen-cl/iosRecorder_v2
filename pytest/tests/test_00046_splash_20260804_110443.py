import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00046_splash_20260804_110443")
def test_00046_splash_20260804_110443(actions: DriverActions):
    with step("[Action] Dismiss continue editing dialog if present"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Cancel', timeout=3):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step("[Action] Tap Edit at (62.9%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 62.9, 44.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (93.9%, 88.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 93.9, 88.1)
    with step("[Action] Tap _AT at (11.8%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 11.8, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (34.6%, 74.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 34.6, 74.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Effects at (38.0%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 38.0, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until icon_splash_s"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'icon_splash_s', direction='left', offset_start=(0.749, 0.423), offset_end=(0.237, 0.423), velocity=345)
    with step("[Action] Tap icon_splash_s at (50.0%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_splash_s', 50.0, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Action] Tap EditingImageView_ImageView at (58.8%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 58.8, 61.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeScrollView', container_w=430, container_h=702)
    with step("[Verify] Capture '00046_splash_Step09' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step09', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"SplashViewMainController\"]/XCUIElementTypeOther[1]/XCUIElementTypeImage/XCUIElementTypeSlider (23.8%,60.0%) → //XCUIElementTypeOther[@name=\"SplashViewMainController\"]/XCUIElementTypeOther[1]/XCUIElementTypeImage (6.7%,60.2%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeOther[1]/XCUIElementTypeImage/XCUIElementTypeSlider', 23.8, 60.0, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeOther[1]/XCUIElementTypeImage', 6.7, 60.2, duration=1.0)
    with step("[Verify] Capture '00046_splash_Step11' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step11', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Verify] 0 text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '0', '0')
    with step("[Action] Drag //XCUIElementTypeOther[@name=\"SplashViewMainController\"]/XCUIElementTypeOther[1]/XCUIElementTypeImage/XCUIElementTypeSlider (7.1%,55.6%) → //XCUIElementTypeOther[@name=\"SplashViewMainController\"]/XCUIElementTypeOther[1]/XCUIElementTypeImage (77.7%,56.8%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeOther[1]/XCUIElementTypeImage/XCUIElementTypeSlider', 7.1, 55.6, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeOther[1]/XCUIElementTypeImage', 77.7, 56.8, duration=1.0)
    with step("[Verify] 100 text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '100', '100')
    with step("[Verify] Capture '00046_splash_Step15' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step15', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn shape mask n at (62.5%, 70.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn shape mask n', 62.5, 70.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeScrollView', container_w=430, container_h=702)
    with step("[Action] Tap original_thumb at (61.4%, 63.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'original_thumb', 61.4, 63.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='splashMaskCollectionView', container_w=373, container_h=88)
    with step("[Verify] Capture '00046_splash_Step18' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step18', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn invert n at (62.5%, 61.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn invert n', 62.5, 61.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=702)
    with step("[Verify] Capture '00046_splash_Step20' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step20', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn invert n at (55.0%, 43.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn invert n', 55.0, 43.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=702)
    with step("[Action] Tap circle_thumb at (60.2%, 40.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'circle_thumb', 60.2, 40.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='splashMaskCollectionView', container_w=373, container_h=88)
    with step("[Verify] Capture '00046_splash_Step23' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step23', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Rotate circle 61.2°"):
        actions.rotate(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'circle'), rotation=61.2)
    with step("[Verify] Capture '00046_splash_Step25' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step25', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (22.4%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 22.4, 44.9)
    with step("[Verify] Capture '00046_splash_Step27' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step27', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn shape mask n at (50.0%, 53.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn shape mask n', 50.0, 53.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeScrollView', container_w=430, container_h=702)
    with step("[Action] Tap circle_thumb at (36.4%, 45.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'circle_thumb', 36.4, 45.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='splashMaskCollectionView', container_w=373, container_h=88)
    with step("[Action] Tap btn_ok_n at (79.6%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 79.6, 38.8)
    with step("[Verify] Capture '00046_splash_Step31' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step31', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (77.6%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 42.9)
    with step("[Verify] Capture '00046_splash_Step33' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step33', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (56.4%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 56.4, 69.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Capture '00046_splash_Step35' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step35', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap icon_splash_s at (26.5%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_splash_s', 26.5, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Action] Tap EditingImageView_ImageView at (62.1%, 88.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 62.1, 88.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeScrollView', container_w=430, container_h=702)
    with step("[Verify] Capture '00046_splash_Step38' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step38', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn mask switch n at (67.5%, 41.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn mask switch n', 67.5, 41.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeScrollView', container_w=430, container_h=702)
    with step("[Verify] Capture '00046_splash_Step40' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step40', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag cpSlider (31.8%,57.1%) → slider (63.7%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 31.8, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 63.7, 48.8, duration=1.0)
    with step("[Verify] Capture '00046_splash_Step42' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step42', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1] (12.1%,47.9%) → EditingImageView_ImageView (83.5%,46.8%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', 12.1, 47.9, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 83.5, 46.8, duration=1.0)
    with step("[Verify] Capture '00046_splash_Step44' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step44', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btt_brush_n at (60.0%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 60.0, 65.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag cpSlider (64.8%,54.8%) → slider (2.2%,58.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 64.8, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.2, 58.5, duration=1.0)
    with step("[Action] Drag //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1] (15.3%,50.7%) → EditingImageView_ImageView (49.5%,48.2%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', 15.3, 50.7, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 49.5, 48.2, duration=1.0)
    with step("[Verify] Capture '00046_splash_Step48' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step48', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Drag cpSlider (7.5%,59.5%) → valueLabel (0.0%,63.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.5, 59.5, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 0.0, 63.4, duration=1.0)
    with step("[Action] Drag //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1] (10.0%,48.6%) → EditingImageView_ImageView (54.4%,44.3%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', 10.0, 48.6, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 54.4, 44.3, duration=1.0)
    with step("[Verify] Capture '00046_splash_Step51' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step51', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn invert n at (65.0%, 61.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn invert n', 65.0, 61.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=670)
    with step("[Verify] Capture '00046_splash_Step53' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step53', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (28.6%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 28.6, 49.0)
    with step("[Verify] Capture '00046_splash_Step55' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step55', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn mask switch n at (35.0%, 70.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn mask switch n', 35.0, 70.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeScrollView', container_w=430, container_h=702)
    with step("[Action] Drag cpSlider (31.8%,52.4%) → //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[2] (3.0%,20.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 31.8, 52.4, AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[2]', 3.0, 20.8, duration=1.0)
    with step("[Action] Tap btn filterEdge n at (35.0%, 43.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn filterEdge n', 35.0, 43.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=670)
    with step("[Action] Drag //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1] (6.0%,56.8%) → EditingImageView_ImageView (81.9%,58.2%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', 6.0, 56.8, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 81.9, 58.2, duration=1.0)
    with step("[Verify] Capture '00046_splash_Step60' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step60', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (38.8%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 38.8, 51.0)
    with step("[Action] Tap btn mask switch n at (55.0%, 51.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn mask switch n', 55.0, 51.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeScrollView', container_w=430, container_h=702)
    with step("[Action] Drag cpSlider (32.4%,66.7%) → slider (2.8%,68.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 32.4, 66.7, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.8, 68.3, duration=1.0)
    with step("[Action] Drag //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1] (15.8%,54.6%) → EditingImageView_ImageView (81.4%,52.5%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', 15.8, 54.6, AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 81.4, 52.5, duration=1.0)
    with step("[Verify] Capture '00046_splash_Step65' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step65', AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (69.4%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 69.4, 53.1)
    with step("[Action] Tap btn_cancel_n at (28.6%, 24.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 28.6, 24.5)
    with step("[Verify] Capture '00046_splash_Step68' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step68', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap icon_splash_s at (55.9%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_splash_s', 55.9, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Action] Tap EditingImageView_ImageView at (60.5%, 89.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 60.5, 89.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeScrollView', container_w=430, container_h=702)
    with step("[Verify] Capture '00046_splash_Step71' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step71', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic color tint n at (65.0%, 63.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic color tint n', 65.0, 63.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeScrollView', container_w=430, container_h=702)
    with step("[Verify] 0 text equals '0'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '0', '0')
    with step("[Action] Drag //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeSlider (6.1%,56.1%) → //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage (49.1%,47.7%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeSlider', 6.1, 56.1, AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage', 49.1, 47.7, duration=1.0)
    with step("[Verify] Capture '00046_splash_Step75' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step75', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.70)
    with step("[Action] Drag //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeSlider (55.0%,53.7%) → //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage (83.3%,55.7%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeSlider', 55.0, 53.7, AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage', 83.3, 55.7, duration=1.0)
    with step("[Verify] 100 text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '100', '100')
    with step("[Verify] Capture '00046_splash_Step78' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step78', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.70)
    with step("[Action] Tap ic reset n at (55.0%, 53.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic reset n', 55.0, 53.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=702)
    with step("[Verify] Capture '00046_splash_Step80' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step80', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.70)
    with step("[Action] Drag //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeSlider (5.6%,56.1%) → //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage (50.9%,52.3%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeSlider', 5.6, 56.1, AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage', 50.9, 52.3, duration=1.0)
    with step("[Action] Tap btn_cancel_n at (24.5%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 24.5, 53.1)
    with step("[Verify] Capture '00046_splash_Step83' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step83', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic color tint n at (75.0%, 65.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic color tint n', 75.0, 65.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="SplashViewMainController"]/XCUIElementTypeScrollView', container_w=430, container_h=702)
    with step("[Action] Drag //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeSlider (5.0%,43.9%) → //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage (47.2%,48.9%)"):
        actions.drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeSlider', 5.0, 43.9, AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeImage', 47.2, 48.9, duration=1.0)
    with step("[Action] Tap btn_ok_n at (77.6%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 77.6, 44.9)
    with step("[Verify] Capture '00046_splash_Step87' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step87', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (71.4%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 71.4, 32.7)
    with step("[Verify] Capture '00046_splash_Step89' for GT comparison"):
        actions.capture_for_gt('00046_splash_Step89', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (34.6%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 34.6, 42.3)
    with step("[Action] Tap Discard at (55.7%, 76.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 55.7, 76.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
