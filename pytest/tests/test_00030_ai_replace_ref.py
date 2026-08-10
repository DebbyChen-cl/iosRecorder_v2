import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00030_ai_replace_ref')
def test_00030_ai_replace_ref(actions: DriverActions):
    """AI replace reference"""
    with step("[Action] Tap btnSettings at (57.6%, 61.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 57.6, 61.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap About at (64.7%, 82.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 64.7, 82.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (63.3%, 44.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 63.3, 44.0)
    with step("[Action] Tap Free at (61.8%, 76.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 61.8, 76.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (62.5%, 77.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 62.5, 77.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (65.0%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 65.0, 55.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap btnBack at (60.7%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 60.7, 51.1)
    with step("[Action] Tap btnBack at (60.7%, 57.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 60.7, 57.4)
    with step("[Action] Tap Edit at (45.7%, 76.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 45.7, 76.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnAlbum at (80.7%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 80.7, 54.8)
    with step("[Action] Tap Sample Photos at (14.3%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 14.3, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap PhDM_example_2 at (31.5%, 40.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_2', 31.5, 40.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (55.6%, 42.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 55.6, 42.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until ic_ai_replace"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_ai_replace', direction='left', offset_start=(0.784, 0.454), offset_end=(0.172, 0.454), velocity=346)
    with step("[Action] Tap ic_ai_replace at (39.4%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_ai_replace', 39.4, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Drag instanceSegmentationGestureReceiverView (33.4%,46.1%) → instanceSegmentationGestureReceiverView (89.5%,83.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 33.4, 46.1, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 89.5, 83.8, duration=1.0)
    with step("[Action] Tap Replace at (98.6%, 17.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Replace', 98.6, 17.4)
    with step("[Action] Tap Upload a reference image at (62.1%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Upload a reference image', 62.1, 45.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=640)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (88.4%, 20.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 88.4, 20.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap ic info n at (67.5%, 53.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic info n', 67.5, 53.7)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (90.2%, 38.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 90.2, 38.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap btnAlbum at (95.4%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 95.4, 47.6)
    with step("[Action] Scroll until Replace"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'albumCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Replace', direction='down', offset_start=(0.449, 0.894), offset_end=(0.449, 0.141), velocity=900)
    with step("[Action] Tap Replace at (6.5%, 43.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Replace', 6.5, 43.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-1 at (60.0%, 45.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1', 60.0, 45.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture 'AI_Replace_Pro_ref_Step26' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_ref_Step26', AppiumBy.ACCESSIBILITY_ID, 'refImageView', threshold=0.95)
    with step("[Action] Tap promptDisplayLabel at (36.9%, 22.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptDisplayLabel', 36.9, 22.2)
    with step("[Action] Type 'Replace to the guitar' into promptDisplayLabel"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptDisplayLabel', 'Replace to the guitar')
    with step("[Action] Tap Next: at (53.3%, 51.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 53.3, 51.8)
    with step("[Verify] Capture 'AI_Replace_Pro_ref_Step30' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_ref_Step30', AppiumBy.ACCESSIBILITY_ID, 'refImageView', threshold=0.95)
    with step("[Action] Tap btnGenerate at (17.8%, 46.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 17.8, 46.8)
    with step("[Action] Tap btnBack at (58.1%, 38.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 58.1, 38.7)
    with step("[Action] Tap reSelectButton at (65.4%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'reSelectButton', 65.4, 50.0)
    with step("[Action] Tap PhotoPickerRecommendDialog-notShowAgainCheckBox at (51.9%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox', 51.9, 48.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Continue at (83.8%, 65.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 83.8, 65.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap btnBack at (65.0%, 36.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 65.0, 36.6)
    with step("[Action] Tap reSelectButton at (65.4%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'reSelectButton', 65.4, 73.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=640)
    with step("[Action] Tap photoCell-0 at (32.3%, 83.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 32.3, 83.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] Capture 'AI_Replace_Pro_ref_Step39' for GT comparison"):
        actions.capture_for_gt('AI_Replace_Pro_ref_Step39', AppiumBy.ACCESSIBILITY_ID, 'refImageView', threshold=0.95)
    with step("[Action] Tap promptDisplayLabel at (84.3%, 77.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptDisplayLabel', 84.3, 77.8)
    with step("[Action] Tap btnClear at (50.0%, 90.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClear', 50.0, 90.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textView', container_w=394, container_h=71)
    with step("[Action] Tap Next: at (53.3%, 51.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 53.3, 51.8)
    with step("[Action] Tap promptTextTapCoverView at (0.7%, 45.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptTextTapCoverView', 0.7, 45.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=430, container_h=552)
    with step("[Verify] promptDisplayLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'promptDisplayLabel')
    with step("[Action] Tap Replace at (54.3%, 29.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Replace', 54.3, 29.2)
    with step("[Verify] selectCheckBoxOverlay is not visible"):
        actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress', timeout=90)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    with step("[Verify] test_00030 completion"):
        assert True
