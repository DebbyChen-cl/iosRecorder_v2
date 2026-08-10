import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00045_main_05_04a_05_20260804_105110")
def test_00045_main_05_04a_05_20260804_105110(actions: DriverActions):
    with step("[Action] Tap Edit at (54.3%, 32.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 54.3, 32.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (86.3%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 86.3, 71.4)
    with step("[Action] Tap _AT at (5.4%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 5.4, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (30.8%, 36.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 30.8, 36.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture '00045_main_05_04a_05_Step05' for GT comparison"):
        actions.capture_for_gt('00045_main_05_04a_05_Step05', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Effects at (54.9%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 54.9, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until icon_mirror_s"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'icon_mirror_s', direction='left', offset_start=(0.835, 0.495), offset_end=(0.307, 0.495), velocity=608)
    with step("[Action] Tap icon_mirror_s at (78.8%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_mirror_s', 78.8, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap mirror_template_05.jpg at (71.9%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'mirror_template_05.jpg', 71.9, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='mirrorLibrary', container_w=430, container_h=80)
    with step("[Verify] Capture '00045_main_05_04a_05_Step10' for GT comparison"):
        actions.capture_for_gt('00045_main_05_04a_05_Step10', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MirrorViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn mirrorfilter n at (52.8%, 72.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn mirrorfilter n', 52.8, 72.2)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"MirrorViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2] at (44.7%, 67.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MirrorViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]', 44.7, 67.4)
    with step("[Action] Tap HDR 07 at (55.9%, 35.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'HDR 07', 55.9, 35.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=93)
    with step("[Verify] Capture '00045_main_05_04a_05_Step14' for GT comparison"):
        actions.capture_for_gt('00045_main_05_04a_05_Step14', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MirrorViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (95.9%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 95.9, 34.7)
    with step("[Verify] Capture '00045_main_05_04a_05_Step16' for GT comparison"):
        actions.capture_for_gt('00045_main_05_04a_05_Step16', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MirrorViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn mirrorfilter n at (47.2%, 63.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn mirrorfilter n', 47.2, 63.9)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"MirrorViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[3] at (58.6%, 70.7%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MirrorViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[3]', 58.6, 70.7)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CMS-fa625752-7816-4075-add3-fbddcd00493b_trending\"]/XCUIElementTypeOther/XCUIElementTypeImage at (47.2%, 58.9%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-fa625752-7816-4075-add3-fbddcd00493b_trending"]/XCUIElementTypeOther/XCUIElementTypeImage', 47.2, 58.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=93)
    with step("[Verify] Capture '00045_main_05_04a_05_Step20' for GT comparison"):
        actions.capture_for_gt('00045_main_05_04a_05_Step20', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MirrorViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (36.7%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 36.7, 40.8)
    with step("[Verify] Capture '00045_main_05_04a_05_Step22' for GT comparison"):
        actions.capture_for_gt('00045_main_05_04a_05_Step22', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MirrorViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn mirrorfilter n at (50.0%, 52.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn mirrorfilter n', 50.0, 52.8)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"MirrorViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[4] at (46.5%, 62.8%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MirrorViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[4]', 46.5, 62.8)
    with step("[Action] Tap //XCUIElementTypeCell[@name=\"CMS-a0df0f61-ddc2-41ad-8810-4e3c3a1f40e6_trending\"]/XCUIElementTypeOther/XCUIElementTypeImage at (61.1%, 63.0%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-a0df0f61-ddc2-41ad-8810-4e3c3a1f40e6_trending"]/XCUIElementTypeOther/XCUIElementTypeImage', 61.1, 63.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=93)
    with step("[Verify] Capture '00045_main_05_04a_05_Step26' for GT comparison"):
        actions.capture_for_gt('00045_main_05_04a_05_Step26', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MirrorViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (75.5%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 75.5, 44.9)
    with step("[Action] Tap btn mirrorfilter n at (61.1%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn mirrorfilter n', 61.1, 75.0)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"MirrorViewController\"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[5] at (48.4%, 66.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MirrorViewController"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[5]', 48.4, 66.5)
    with step("[Action] Tap Lomo 06 at (60.3%, 58.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Lomo 06', 60.3, 58.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=421, container_h=93)
    with step("[Verify] Capture '00045_main_05_04a_05_Step31' for GT comparison"):
        actions.capture_for_gt('00045_main_05_04a_05_Step31', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MirrorViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (67.3%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 67.3, 42.9)
    with step("[Verify] Capture '00045_main_05_04a_05_Step33' for GT comparison"):
        actions.capture_for_gt('00045_main_05_04a_05_Step33', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="MirrorViewController"]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btn_cancel_n at (46.9%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 46.9, 26.5)
    with step("[Verify] Capture '00045_main_05_04a_05_Step35' for GT comparison"):
        actions.capture_for_gt('00045_main_05_04a_05_Step35', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap icon_mirror_s at (45.5%, 39.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'icon_mirror_s', 45.5, 39.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap mirror_template_05.jpg at (25.0%, 39.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'mirror_template_05.jpg', 25.0, 39.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='mirrorLibrary', container_w=430, container_h=80)
    with step("[Action] Tap btn_ok_n at (81.6%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 44.9)
    with step("[Verify] Capture '00045_main_05_04a_05_Step39' for GT comparison"):
        actions.capture_for_gt('00045_main_05_04a_05_Step39', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap homeButton at (61.5%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 73.1)
    with step("[Action] Tap Discard at (29.0%, 25.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 29.0, 25.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="EditViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=651)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
