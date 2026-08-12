import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00173_collage_20260811_164156")
def test_00173_collage_20260811_164156(actions: DriverActions):
    with step("[Action] Scroll until Collage"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'Collage', direction='left', offset_start=(0.94, 0.498), offset_end=(0.109, 0.498), velocity=582)
    with step("[Action] Tap Collage at (63.5%, 29.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collage', 63.5, 29.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Action] Tap btnBack at (60.4%, 62.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 60.4, 62.3)
    with step("[Action] Tap Collage at (72.9%, 37.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collage', 72.9, 37.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Action] Tap 2 at (9.1%, 42.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '2', 9.1, 42.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.CollageWebViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=396, container_h=44)
    with step("[Action] Tap CMS-phdm_20230610_IndependenceDay_G_1_02 at (59.8%, 49.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_20230610_IndependenceDay_G_1_02', 59.8, 49.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='CollageContentViewCell-contentCollectionView', container_w=413, container_h=138)
    with step("[Action] Tap btnAlbum at (76.6%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 76.6, 52.4)
    with step("[Action] Tap _AT at (10.4%, 90.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 10.4, 90.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=632)
    with step("[Verify] Capture '00173_collage_Step09' for GT comparison"):
        actions.capture_for_gt('00173_collage_Step09', AppiumBy.ACCESSIBILITY_ID, 'selectionContainerView', threshold=0.95)
    with step("[Action] Tap photoCell-1 at (43.1%, 56.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 43.1, 56.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Verify] //XCUIElementTypeOther[@name=\"selectionContainerView\"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage')
    with step("[Action] Tap btn FontDelete n at (68.2%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n', 68.2, 54.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=430, container_h=74)
    with step("[Verify] Capture '00173_collage_Step13' for GT comparison"):
        actions.capture_for_gt('00173_collage_Step13', AppiumBy.ACCESSIBILITY_ID, 'selectionContainerView', threshold=0.95)
    with step("[Action] Tap photoCell-1 at (44.6%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 44.6, 58.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap photoCell-2 at (56.9%, 56.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 56.9, 56.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap Next at (67.6%, 52.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next', 67.6, 52.6)
    with step("[Verify] Capture '00173_collage_Step17' for GT comparison"):
        actions.capture_for_gt('00173_collage_Step17', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap CMS-Optional(\"phdm_20230710_Father\\\\\\'sDay_T_02_02\") at (47.8%, 73.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("phdm_20230710_Father\\\'sDay_T_02_02")', 47.8, 73.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=357, container_h=80)
    with step("[Verify] Capture '00173_collage_Step19' for GT comparison"):
        actions.capture_for_gt('00173_collage_Step19', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btnWebstore at (69.7%, 47.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnWebstore', 69.7, 47.1)
    with step("[Action] Tap 2 at (63.6%, 68.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '2', 63.6, 68.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.CollageWebViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=396, container_h=44)
    with step("[Action] Tap CMS-phdm_20230610_MarineDay_J_1_02 at (60.8%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_20230610_MarineDay_J_1_02', 60.8, 55.1)
    with step("[Verify] Capture '00173_collage_Step23' for GT comparison"):
        actions.capture_for_gt('00173_collage_Step23', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]', threshold=0.95)
    with step("[Action] Tap btnWebstore at (33.3%, 55.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnWebstore', 33.3, 55.9)
    with step("[Action] Tap All at (94.4%, 84.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'All', 94.4, 84.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.CollageWebViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=396, container_h=44)
    with step("[Action] Tap btnBack at (50.9%, 52.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 50.9, 52.8)
    with step("[Action] Tap btn_cancel_n at (46.9%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 46.9, 51.0)
    with step("[Action] Tap Next at (38.2%, 78.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next', 38.2, 78.9)
    with step("[Action] Scroll until CMS-Optional(\"25ad0d20-c68a-454e-baeb-7c05e728982f\")"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("25ad0d20-c68a-454e-baeb-7c05e728982f")', direction='left', offset_start=(0.504, 0.25), offset_end=(0.196, 0.25), velocity=236, max_attempts=150)
    with step("[Action] Tap CMS-Optional(\"25ad0d20-c68a-454e-baeb-7c05e728982f\") at (62.1%, 46.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("25ad0d20-c68a-454e-baeb-7c05e728982f")', 62.1, 46.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=357, container_h=80)
    with step("[Action] Tap btn_ok_n at (91.8%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 91.8, 38.8)
    with step("[Action] Tap OK at (56.7%, 54.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 56.7, 54.2)
    with step("[Action] Tap btnShareMore at (51.3%, 39.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareMore', 51.3, 39.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=786)
    with step("[Verify] //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypePopover is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypePopover')
    with step("[Action] Tap PopoverDismissRegion at (11.4%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PopoverDismissRegion', 11.4, 40.0)
    with step("[Action] Tap btnShareIG at (52.1%, 47.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareIG', 52.1, 47.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=786)
    with step("[Verify] Share to Instagram is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram')
    with step("[Action] Tap //XCUIElementTypeApplication[@name=\"Instagram\"]/XCUIElementTypeWindow/XCUIElementTypeOther[2] at (12.8%, 4.8%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="Instagram"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]', 12.8, 4.8)
    with step("[Action] Tap btnShareFB at (56.8%, 47.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB', 56.8, 47.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=786)
    with step("[Verify] New post is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'New post')
    with step("[Action] Tap //XCUIElementTypeApplication[@name=\"Facebook\"]/XCUIElementTypeWindow/XCUIElementTypeOther[2] at (13.0%, 4.3%)"):
            actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="Facebook"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]', 13.0, 4.3)
    with step("[Action] Tap Next Edit at (76.2%, 78.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next Edit', 76.2, 78.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=786)
    with step("[Action] Tap btnCamera at (65.0%, 58.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnCamera', 65.0, 58.5)
    with step("[Action] Tap DismissImagePickerButton at (35.4%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'DismissImagePickerButton', 35.4, 33.3)
    with step("[Action] Tap btnBack at (50.0%, 51.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 50.0, 51.2)
    with step("[Action] Scroll until Collage"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'Collage', direction='left', offset_start=(0.935, 0.488), offset_end=(0.13, 0.488), velocity=533)
    with step("[Action] Tap Collage at (74.0%, 32.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collage', 74.0, 32.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Action] Tap 2 at (54.5%, 52.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '2', 54.5, 52.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.CollageWebViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=396, container_h=44)
    with step("[Action] Tap CMS-phdm_20230610_IndependenceDay_G_1_02 at (32.4%, 58.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_20230610_IndependenceDay_G_1_02', 32.4, 58.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='CollageContentViewCell-contentCollectionView', container_w=413, container_h=138)
    with step("[Action] Tap photoCell-1 at (60.0%, 43.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 60.0, 43.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap photoCell-2 at (63.1%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 63.1, 30.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap Next at (29.4%, 52.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next', 29.4, 52.6)
    with step("[Action] Scroll until CMS-Optional(\"2edd9f2c-d570-4007-a4c2-5b467f49c167\")"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("2edd9f2c-d570-4007-a4c2-5b467f49c167")', direction='left', offset_start=(0.669, 0.325), offset_end=(0.258, 0.325), velocity=325, max_attempts=150)
    with step("[Action] Tap CMS-Optional(\"2edd9f2c-d570-4007-a4c2-5b467f49c167\") at (24.2%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Optional("2edd9f2c-d570-4007-a4c2-5b467f49c167")', 24.2, 54.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=357, container_h=80)
    with step("[Action] Tap btn_ok_n at (73.5%, 30.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 73.5, 30.6)
    with step("[Action] Tap OK at (83.3%, 87.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'OK', 83.3, 87.5)
    with step("[Action] Tap navHomeButton at (59.1%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton', 59.1, 51.1)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
