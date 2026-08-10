import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00155_main_11_01_04_20260806_174453")
def test_00155_main_11_01_04_20260806_174453(actions: DriverActions):
    with step("[Action] Tap btnSettings at (63.6%, 23.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 63.6, 23.5)
    with step("[Action] Tap About at (86.3%, 73.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 86.3, 73.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (36.7%, 32.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 36.7, 32.0)
    with step("[Action] Tap Free at (35.3%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 35.3, 61.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (50.0%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 50.0, 69.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (40.0%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 40.0, 33.3)
    with step("[Action] Tap btnBack at (67.9%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 67.9, 48.9)
    with step("[Action] Tap btnBack at (67.9%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 67.9, 48.9)
    with step("[Action] Tap Edit at (65.7%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 65.7, 52.0)
    with step("[Action] Tap btnAlbum at (69.5%, 69.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 69.5, 69.0)
    with step("[Action] Tap _AT at (7.5%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.5, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-6 at (25.4%, 57.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6', 25.4, 57.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (54.1%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 54.1, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap btn_reshape_n at (54.5%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_reshape_n', 54.5, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_leg_width_n at (68.3%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_leg_width_n', 68.3, 55.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='bodyPartCollectionView', container_w=430, container_h=71)
    with step("[Action] Drag centerSlider (49.0%,52.0%) → intensitySlider (98.6%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 49.0, 52.0, AppiumBy.ACCESSIBILITY_ID, 'intensitySlider', 98.6, 49.0, duration=1.0)
    with step("[Action] Tap btn_ok_n at (85.7%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 85.7, 44.9)
    with step("[Verify] Capture '00155_main_11_01_04_Step18' for GT comparison"):
        actions.capture_for_gt('00155_main_11_01_04_Step18', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (28.2%, 35.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 28.2, 35.9)
    with step("[Action] Tap Enhance at (35.7%, 62.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 35.7, 62.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap btn_filter_n at (54.5%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_filter_n', 54.5, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Basic at (51.2%, 38.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Basic', 51.2, 38.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='cmsCategoryCollectionViewCollectionView', container_w=430, container_h=40)
    with step("[Action] Tap Vlogger 01 at (60.3%, 41.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Vlogger 01', 60.3, 41.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=94)
    with step("[Action] Tap btn_ok_n at (59.2%, 22.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 59.2, 22.4)
    with step("[Verify] Capture '00155_main_11_01_04_Step25' for GT comparison"):
        actions.capture_for_gt('00155_main_11_01_04_Step25', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (71.8%, 64.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 71.8, 64.1)
    with step("[Action] Tap Effects at (36.6%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 36.6, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until ic_lighthits"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_lighthits', direction='left', offset_start=(0.488, 0.423), offset_end=(0.177, 0.423), velocity=89)
    with step("[Action] Tap ic_lighthits at (57.6%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_lighthits', 57.6, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"LightHitCell-0\"]/XCUIElementTypeImage at (61.2%, 59.7%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="LightHitCell-0"]/XCUIElementTypeImage', 61.2, 59.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="light_hits"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=354, container_h=79)
    with step("[Action] Tap btn_ok_n at (87.8%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 87.8, 49.0)
    with step("[Verify] Capture '00155_main_11_01_04_Step32' for GT comparison"):
        actions.capture_for_gt('00155_main_11_01_04_Step32', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (59.0%, 71.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 59.0, 71.8)
    with step("[Action] Scroll until btn_live_n"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', direction='left', offset_start=(0.544, 0.454), offset_end=(0.098, 0.454), velocity=277)
    with step("[Action] Tap btn_live_n at (61.8%, 39.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n', 61.8, 39.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Action] Tap btn_live_lightray_n at (43.9%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_live_lightray_n', 43.9, 67.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='menuView', container_w=430, container_h=97)
    with step("[Action] Tap btn_singleSource at (32.8%, 61.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_singleSource', 32.8, 61.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='itemView', container_w=257, container_h=97)
    with step("[Action] Tap btn_ok_n at (83.7%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 83.7, 36.7)
    with step("[Action] Tap Still Image at (54.3%, 95.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Still Image', 54.3, 95.8)
    with step("[Verify] Capture '00155_main_11_01_04_Step40' for GT comparison"):
        actions.capture_for_gt('00155_main_11_01_04_Step40', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (64.1%, 59.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 64.1, 59.0)
    with step("[Action] Scroll until ic_blur"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_blur', direction='right', offset_start=(0.077, 0.464), offset_end=(0.723, 0.464), velocity=651)
    with step("[Action] Tap ic_blur at (42.4%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_blur', 42.4, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_ok_n at (73.5%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 49.0)
    with step("[Verify] Capture '00155_main_11_01_04_Step45' for GT comparison"):
        actions.capture_for_gt('00155_main_11_01_04_Step45', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (43.6%, 51.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 43.6, 51.3)
    with step("[Action] Tap Edit at (78.3%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 78.3, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap ic_background at (48.5%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_background', 48.5, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_bgart_n at (33.3%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_bgart_n', 33.3, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap Background at (49.1%, 54.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Background', 49.1, 54.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=216, container_h=46)
    with step("[Action] Tap CMS-phdm_BG_Greenery_18_free_trending at (47.2%, 45.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_BG_Greenery_18_free_trending', 47.2, 45.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="backgroundItemPanel"]/XCUIElementTypeCollectionView[3]', container_w=408, container_h=71)
    with step("[Action] Tap btn_ok_n at (75.5%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 49.0)
    with step("[Verify] Capture '00155_main_11_01_04_Step53' for GT comparison"):
        actions.capture_for_gt('00155_main_11_01_04_Step53', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (66.7%, 56.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 66.7, 56.4)
    with step("[Action] Tap ic_background at (18.2%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_background', 18.2, 36.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap btn_bgart_n at (63.6%, 75.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_bgart_n', 63.6, 75.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap CMS-phdm_BG_Sky_10_paid_trending at (37.5%, 53.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_BG_Sky_10_paid_trending', 37.5, 53.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="backgroundItemPanel"]/XCUIElementTypeCollectionView[3]', container_w=408, container_h=71)
    with step("[Action] Tap btn_ok_n at (85.7%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 85.7, 42.9)
    with step("[Verify] Capture '00155_main_11_01_04_Step59' for GT comparison"):
        actions.capture_for_gt('00155_main_11_01_04_Step59', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap ic edit undo n at (35.9%, 30.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n', 35.9, 30.8)
    with step("[Action] Tap ic_cutout at (42.4%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_cutout', 42.4, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_foreground at (50.0%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_foreground', 50.0, 40.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="funcPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=71)
    with step("[Action] Tap Cutout at (62.3%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cutout', 62.3, 47.6)
    with step("[Action] Tap Stroke at (67.4%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Stroke', 67.4, 66.7)
    with step("[Action] Tap stroke_thumb_2 at (71.2%, 36.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'stroke_thumb_2', 71.2, 36.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='strokeCollection', container_w=337, container_h=71)
    with step("[Action] Tap btn_ok_n at (51.0%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 51.0, 42.9)
    with step("[Verify] Capture '00155_main_11_01_04_Step67' for GT comparison"):
        actions.capture_for_gt('00155_main_11_01_04_Step67', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photoView"]/XCUIElementTypeImage', threshold=0.95)
    with step("[Action] Tap navHomeButton at (65.9%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton', 65.9, 51.1)
    with step("[Action] Tap Cancel at (74.0%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 74.0, 69.4)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
