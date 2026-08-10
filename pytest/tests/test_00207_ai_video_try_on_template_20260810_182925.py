import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00207_ai_video_try_on_template_20260810_182925")
def test_00207_ai_video_try_on_template_20260810_182925(actions: DriverActions):
    with step("[Action] Scroll until AI Video Try-On"):
        actions.scroll_until(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', AppiumBy.ACCESSIBILITY_ID, 'AI Video Try-On', direction='left', offset_start=(0.956, 0.424), offset_end=(0.063, 0.424), velocity=460)
    with step("[Action] Tap AI Video Try-On at (55.2%, 70.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Video Try-On', 55.2, 70.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Action] Tap notShowAgainCheckBox at (48.1%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox', 48.1, 53.8)
    with step("[Action] Tap Try now at (74.3%, 73.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try now', 74.3, 73.9)
    with step("[Action] Tap //XCUIElementTypeOther[@name=\"aiVideoTryOn_importView\"]/XCUIElementTypeOther at (53.8%, 51.2%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="aiVideoTryOn_importView"]/XCUIElementTypeOther', 53.8, 51.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=719)
    with step("[Verify] recommendTitleLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'recommendTitleLabel')
    with step("[Action] Tap continueButton at (65.5%, 56.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'continueButton', 65.5, 56.7)
    with step("[Action] Tap Collections at (47.4%, 45.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Collections', 47.4, 45.8)
    with step("[Action] Tap _Video at (29.2%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_Video', 29.2, 61.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albums-shelf-scrollView', container_w=430, container_h=120)
    with step("[Action] Tap photos_layout at (21.4%, 51.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photos_layout', 21.4, 51.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photosView_content_scroll_view', container_w=430, container_h=863)
    with step("[Action] Drag startBarImageView (75.0%,44.4%) → contentAreaGradientBackground (89.5%,78.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'startBarImageView', 75.0, 44.4, AppiumBy.ACCESSIBILITY_ID, 'contentAreaGradientBackground', 89.5, 78.3, duration=1.0)
    with step("[Verify] lblDesc text equals 'Selected Length: 00:03'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblDesc', 'Selected Length: 00:03')
    with step("[Verify] lblCreditPrice text equals '21'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblCreditPrice', '21')
    with step("[Action] Drag startBarImageView (55.6%,61.1%) → contentAreaGradientBackground (14.4%,78.3%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'startBarImageView', 55.6, 61.1, AppiumBy.ACCESSIBILITY_ID, 'contentAreaGradientBackground', 14.4, 78.3, duration=1.0)
    with step("[Verify] lblDesc text equals 'Selected Length: 00:10'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblDesc', 'Selected Length: 00:10')
    with step("[Verify] lblCreditPrice text equals '70'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'lblCreditPrice', '70')
    with step("[Action] Tap btnPlay at (55.8%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 55.8, 59.1)
    with step("[Verify] Capture '00207_ai_video_try_on_template_Step19' for GT comparison"):
        actions.capture_for_gt('00207_ai_video_try_on_template_Step19', AppiumBy.ACCESSIBILITY_ID, 'btnPlay', threshold=0.95)
    with step("[Action] Tap btnPlay at (58.1%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay', 58.1, 59.1)
    with step("[Verify] Capture '00207_ai_video_try_on_template_Step21' for GT comparison"):
        actions.capture_for_gt('00207_ai_video_try_on_template_Step21', AppiumBy.ACCESSIBILITY_ID, 'btnPlay', threshold=0.95)
    with step("[Verify] Capture '00207_ai_video_try_on_template_Step22' for GT comparison"):
        actions.capture_for_gt('00207_ai_video_try_on_template_Step22', AppiumBy.ACCESSIBILITY_ID, 'btnMuteToggle', threshold=0.95)
    with step("[Action] Tap btnMuteToggle at (45.2%, 35.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnMuteToggle', 45.2, 35.5)
    with step("[Verify] Capture '00207_ai_video_try_on_template_Step24' for GT comparison"):
        actions.capture_for_gt('00207_ai_video_try_on_template_Step24', AppiumBy.ACCESSIBILITY_ID, 'btnMuteToggle', threshold=0.95)
    with step("[Action] Tap btnNext at (27.2%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 27.2, 65.0)
    with step("[Verify] 00:10 text equals '00:10'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, '00:10', '00:10')
    with step("[Verify] Capture '00207_ai_video_try_on_template_Step27' for GT comparison"):
        actions.capture_for_gt('00207_ai_video_try_on_template_Step27', AppiumBy.ACCESSIBILITY_ID, 'ic volume off', threshold=0.95)
    with step("[Action] Tap ic volume off at (65.4%, 70.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic volume off', 65.4, 70.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='scrollView', container_w=430, container_h=719)
    with step("[Verify] Capture '00207_ai_video_try_on_template_Step29' for GT comparison"):
        actions.capture_for_gt('00207_ai_video_try_on_template_Step29', AppiumBy.ACCESSIBILITY_ID, 'ic volume', threshold=0.95)
    with step("[Verify] Capture '00207_ai_video_try_on_template_Step30' for GT comparison"):
        actions.capture_for_gt('00207_ai_video_try_on_template_Step30', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="aiVideoTryOn_importView"]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap imageView at (65.1%, 56.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 65.1, 56.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='carouselCollectionView', container_w=394, container_h=123)
    with step("[Verify] Capture '00207_ai_video_try_on_template_Step32' for GT comparison"):
        actions.capture_for_gt('00207_ai_video_try_on_template_Step32', AppiumBy.ACCESSIBILITY_ID, 'photoImageView', threshold=0.95)
    with step("[Action] Tap titleLabel at (53.5%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'titleLabel', 53.5, 52.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='carouselCollectionView', container_w=394, container_h=123)
    with step("[Verify] Outfit Library is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Outfit Library')
    with step("[Action] Tap Male at (66.7%, 48.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Male', 66.7, 48.3)
    with step("[Action] Tap Female at (59.6%, 38.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Female', 59.6, 38.1)
    with step("[Action] Tap //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeImage at (62.2%, 66.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeImage', 62.2, 66.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=742)
    with step("[Verify] Capture '00207_ai_video_try_on_template_Step38' for GT comparison"):
        actions.capture_for_gt('00207_ai_video_try_on_template_Step38', AppiumBy.ACCESSIBILITY_ID, 'photoImageView', threshold=0.95)
    with step("[Action] Tap Generate at (53.1%, 43.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 53.1, 43.5)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Verify] processingLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'processingLabel', appear_timeout=5, disappear_timeout=1200), 'processingLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (64.5%, 74.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 64.5, 74.2)
    with step("[Action] Tap aiVideoTryOn_backButton at (53.8%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'aiVideoTryOn_backButton', 53.8, 55.6)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
