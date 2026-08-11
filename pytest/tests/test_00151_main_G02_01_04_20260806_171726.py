import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00151_main_G02_01_04_20260806_171726")
def test_00151_main_G02_01_04_20260806_171726(actions: DriverActions):
    with step("[Action] Tap btnAIVideo at (55.3%, 34.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAIVideo', 55.3, 34.5)
    with step("[Action] Tap AI Anime Video at (69.4%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Anime Video', 69.4, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=264, container_h=44)
    with step("[Action] Tap Try Now at (55.4%, 76.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try Now', 55.4, 76.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animeVideoCollectionView', container_w=430, container_h=680)
    with step("[Action] Tap navArtworkButton at (61.4%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navArtworkButton', 61.4, 59.1)
    with step("[Action] Tap packThumbnailImageView at (83.0%, 55.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'packThumbnailImageView', 83.0, 55.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='packCollectionView', container_w=394, container_h=668)
    with step("[Action] Tap btnSave at (60.5%, 67.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSave', 60.5, 67.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=779)
    with step("[Action] Tap btnShareFB at (44.1%, 31.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB', 44.1, 31.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=779)
    with step("[Verify] New post is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'New post')
    with step("[Action] Tap composer-left-button at (52.3%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'composer-left-button', 52.3, 48.1)
    with step("[Action] Tap Discard at (48.9%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 48.9, 55.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Discard post?"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=270, container_h=45)
    with step("[Action] Tap btnShareIG at (53.0%, 42.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareIG', 53.0, 42.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=779)
    with step("[Verify] Share to Instagram is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram')
    with step("[Action] Tap //XCUIElementTypeApplication[@name=\"Instagram\"]/XCUIElementTypeWindow/XCUIElementTypeOther[2] at (9.8%, 4.3%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="Instagram"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]', 9.8, 4.3)
    with step("[Action] Tap btnShareMore at (41.0%, 34.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnShareMore', 41.0, 34.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=779)
    with step("[Verify] //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypePopover is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[6]/XCUIElementTypePopover')
    with step("[Action] Tap PopoverDismissRegion at (7.4%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PopoverDismissRegion', 7.4, 42.9)
    with step("[Action] Tap btnPlay at (62.1%, 67.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 62.1, 67.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=779)
    with step("[Verify] btnPlay is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step("[Action] Tap navBackButton at (45.5%, 61.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 45.5, 61.4)
    with step("[Action] Tap navHomeButton at (46.7%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton', 46.7, 33.3)
    with step("[Action] Tap btnAIVideo at (48.7%, 27.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAIVideo', 48.7, 27.3)
    with step("[Action] Tap AI Anime Video at (46.8%, 47.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Anime Video', 46.8, 47.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=264, container_h=44)
    with step("[Action] Tap Try Now at (92.9%, 76.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try Now', 92.9, 76.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='animeVideoCollectionView', container_w=430, container_h=680)
    with step("[Action] Tap continueButton at (9.8%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'continueButton', 9.8, 55.0)
    with step("[Verify] Why Must I Pay for ? is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Why Must I Pay for ?')
    with step("[Action] Tap leftButton at (66.3%, 55.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'leftButton', 66.3, 55.9)
    with step("[Verify] 1 - 10 sec is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, '1 - 10 sec')
    with step("[Action] Tap rightButton at (23.8%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'rightButton', 23.8, 50.0)
    with step("[Verify] lblPlan is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblPlan')
    with step("[Action] Tap Select Video and Trim at (45.4%, 40.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Select Video and Trim', 45.4, 40.5)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Action] Tap Continue at (58.1%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 58.1, 68.2)
    with step("[Action] Tap Collections at (57.9%, 60.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collections', 57.9, 60.4)
    with step("[Action] Tap _Video at (79.2%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_Video', 79.2, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albums-shelf-scrollView', container_w=430, container_h=120)
    with step("[Action] Tap photos_layout at (51.6%, 60.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photos_layout', 51.6, 60.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photosView_content_scroll_view', container_w=430, container_h=863)
    with step("[Action] Tap Choose at (61.9%, 73.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Choose', 61.9, 73.9)
    with step("[Action] Drag startBarImageView (50.0%,63.2%) → //XCUIElementTypeOther[@name=\"slidingWindow\"]/XCUIElementTypeOther[3] (42.4%,46.5%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'startBarImageView', 50.0, 63.2, AppiumBy.XPATH, '//XCUIElementTypeOther[@name="slidingWindow"]/XCUIElementTypeOther[3]', 42.4, 46.5, duration=1.0)
    with step("[Verify] Capture '00151_main_G02_01_04_Step40' for GT comparison"):
        actions.capture_for_gt('00151_main_G02_01_04_Step40', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="AIAnimeVideoTrimmerViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap btnNext at (7.4%, 68.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 7.4, 68.3)
    with step("[Verify] labelProcessing disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing', appear_timeout=5, disappear_timeout=1200), 'labelProcessing did not appear within 5s or is still shown after 1200s'
    with step("[Verify] labelTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'labelTitle')
    with step("[Action] Tap btnBack at (71.0%, 38.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 71.0, 38.7)
    with step("[Action] Tap btnHome at (52.6%, 49.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 52.6, 49.1)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
