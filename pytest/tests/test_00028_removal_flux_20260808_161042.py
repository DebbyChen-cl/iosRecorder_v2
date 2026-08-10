import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00028_removal_flux_20260808_161042")
def test_00028_removal_flux_20260808_161042(actions: DriverActions):
    with step("[Action] Tap Edit at (80.0%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 80.0, 56.0)
    with step("[Action] Tap btnAlbum at (78.7%, 64.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 78.7, 64.3)
    with step("[Action] Tap _AT at (9.3%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.3, 77.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (27.7%, 76.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 27.7, 76.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (66.7%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 66.7, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap AI Removal at (54.9%, 21.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Removal', 54.9, 21.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap proPlusToggle at (33.3%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'proPlusToggle', 33.3, 62.5)
    with step("[Verify] Upgrade to Pro+ Premium is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Upgrade to Pro+ Premium')
    with step("[Action] Tap btn close outline n at (51.9%, 59.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n', 51.9, 59.3)
    with step("[Action] Tap btn_cancel_n at (24.5%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 24.5, 32.7)
    with step("[Action] Tap settingButton at (57.7%, 38.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'settingButton', 57.7, 38.5)
    with step("[Action] Tap About at (80.4%, 73.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 80.4, 73.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (38.8%, 52.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 38.8, 52.0)
    with step("[Action] Tap Free at (47.1%, 76.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 47.1, 76.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro at (52.1%, 34.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro', 52.1, 34.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 50.0, 50.0)
    with step("[Action] Tap btnBack at (50.0%, 46.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 50.0, 46.8)
    with step("[Action] Tap btnBack at (57.1%, 57.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 57.1, 57.4)
    with step("[Action] Tap AI Removal at (50.7%, 36.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Removal', 50.7, 36.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap proPlusToggle at (62.3%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'proPlusToggle', 62.3, 50.0)
    with step("[Verify] Upgrade to Pro+ Premium is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Upgrade to Pro+ Premium')
    with step("[Action] Tap btn close outline n at (29.6%, 25.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn close outline n', 29.6, 25.9)
    with step("[Action] Tap btn_cancel_n at (24.5%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 24.5, 38.8)
    with step("[Action] Tap settingButton at (57.7%, 23.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'settingButton', 57.7, 23.1)
    with step("[Action] Tap About at (62.7%, 34.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 62.7, 34.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (32.7%, 32.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 32.7, 32.0)
    with step("[Action] Tap Pro at (57.7%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro', 57.7, 61.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (55.6%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 55.6, 59.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 50.0, 50.0)
    with step("[Action] Tap btnBack at (50.0%, 46.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 50.0, 46.8)
    with step("[Action] Tap btnBack at (57.1%, 57.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 57.1, 57.4)
    with step("[Action] Tap AI Removal at (74.6%, 15.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Removal', 74.6, 15.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Capture '00028_removal_flux_Step33' for GT comparison"):
        actions.capture_for_gt('00028_removal_flux_Step33', AppiumBy.ACCESSIBILITY_ID, 'proPlusToggle', threshold=0.95)
    with step("[Action] Tap Manual at (52.9%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Manual', 52.9, 83.3)
    with step("[Action] Drag EditingImageView_ImageView (54.9%,20.4%) → backgroundView (56.5%,54.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', 54.9, 20.4, AppiumBy.ACCESSIBILITY_ID, 'backgroundView', 56.5, 54.9, duration=1.0)
    with step("[Verify] Capture '00028_removal_flux_Step36' for GT comparison"):
        actions.capture_for_gt('00028_removal_flux_Step36', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap Remove at (90.9%, 87.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Remove', 90.9, 87.0)
    with step("[Verify] magicText disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'magicText', appear_timeout=5, disappear_timeout=1200), 'magicText did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Capture '00028_removal_flux_Step39' for GT comparison"):
        actions.capture_for_gt('00028_removal_flux_Step39', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.95)
    with step("[Action] Tap btn_ok_n at (85.7%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 85.7, 32.7)
    with step("[Action] Tap homeButton at (38.5%, 61.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 38.5, 61.5)
    with step("[Action] Tap Discard at (43.5%, 54.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 43.5, 54.2)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
