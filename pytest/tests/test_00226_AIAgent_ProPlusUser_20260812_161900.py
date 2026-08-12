import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00226_AIAgent_ProPlusUser_20260812_161900")
def test_00226_AIAgent_ProPlusUser_20260812_161900(actions: DriverActions):
    with step("[Action] Tap btnSettings at (66.7%, 44.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 66.7, 44.1)
    with step("[Action] Tap About at (64.7%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 64.7, 52.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (51.0%, 34.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 51.0, 34.0)
    with step("[Action] Tap Free at (73.5%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 73.5, 47.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (74.3%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 74.3, 42.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (20.0%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 20.0, 44.4)
    with step("[Action] Tap btnBack at (60.7%, 53.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 60.7, 53.2)
    with step("[Action] Tap btnBack at (53.6%, 55.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 53.6, 55.3)
    with step("[Action] Tap AI Edit Agent at (25.0%, 32.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', 25.0, 32.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Verify] chatWelcomeBannerDialog-messageLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'chatWelcomeBannerDialog-messageLabel')
    with step("[Action] Tap chatWelcomeBannerDialog-closeButton at (55.6%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatWelcomeBannerDialog-closeButton', 55.6, 44.4)
    with step("[Action] Tap chatMenuButton at (77.4%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatMenuButton', 77.4, 51.6)
    with step("[Verify] //XCUIElementTypeOther[@name=\"photodirector.ChatUIViewController\"]/XCUIElementTypeOther[2]/XCUIElementTypeOther is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.ChatUIViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    with step("[Action] Long press New Chat at (65.3%, 52.4%)"):
        actions.long_press_within_element(AppiumBy.ACCESSIBILITY_ID, 'New Chat', 65.3, 52.4, duration=1.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.ChatUIViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=353, container_h=753)
    with step("[Action] Tap Rename at (46.4%, 51.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Rename', 46.4, 51.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=250, container_h=933)
    with step("[Action] Type 'Old Chat' into Rename"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rename', 'Old Chat')
    with step("[Action] Tap Confirm at (19.3%, 61.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Confirm', 19.3, 61.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Rename The Chat"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=81)
    with step("[Verify] Old Chat is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Old Chat')
    with step("[Action] Tap Old Chat at (82.4%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Old Chat', 82.4, 66.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.ChatUIViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=353, container_h=753)
    with step("[Action] Tap chatSuggestionButton-0 at (4.6%, 63.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSuggestionButton-0', 4.6, 63.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatCollectionView', container_w=422, container_h=775)
    with step("[Action] Tap chatSendButton at (30.0%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 30.0, 60.0)
    with step("[Verify] Thinking disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Thinking', appear_timeout=5, disappear_timeout=1200), 'Thinking did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Processing... disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Processing...', appear_timeout=5, disappear_timeout=1200), 'Processing... did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap downloadButton at (68.6%, 63.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'downloadButton', 68.6, 63.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatCollectionView', container_w=422, container_h=775)
    with step("[Action] Tap quoteButton at (57.1%, 63.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'quoteButton', 57.1, 63.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatCollectionView', container_w=422, container_h=775)
    with step("[Verify] imageView is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'imageView')
    with step("[Action] Tap chatInputImageRemoveButton at (52.5%, 51.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatInputImageRemoveButton', 52.5, 51.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatInputImagePreview', container_w=408, container_h=88)
    with step("[Verify] Capture '00226_AIAgent_ProPlusUser_Step28' for GT comparison"):
        actions.capture_for_gt('00226_AIAgent_ProPlusUser_Step28', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.ChatUIViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap editButton at (48.6%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'editButton', 48.6, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatCollectionView', container_w=422, container_h=775)
    with step("[Verify] EditingImageView_ImageView is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap Edit at (75.6%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 75.6, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap AI Edit Agent at (52.1%, 21.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', 52.1, 21.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] imageView is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'imageView')
    with step("[Action] Tap chatBackButton at (38.7%, 58.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatBackButton', 38.7, 58.1)
    with step("[Action] Tap Enhance at (46.4%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Enhance', 46.4, 44.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap AI Edit Agent at (57.7%, 26.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', 57.7, 26.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] photodirector.ChatUIViewController is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'photodirector.ChatUIViewController')
    with step("[Action] Tap chatBackButton at (80.6%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatBackButton', 80.6, 51.6)
    with step("[Action] Tap Portrait at (47.3%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 47.3, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap AI Edit Agent at (77.5%, 23.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', 77.5, 23.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] photodirector.ChatUIViewController is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'photodirector.ChatUIViewController')
    with step("[Action] Tap chatBackButton at (48.4%, 61.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatBackButton', 48.4, 61.3)
    with step("[Action] Tap Effects at (69.0%, 57.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Effects', 69.0, 57.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Tap AI Edit Agent at (43.7%, 28.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', 43.7, 28.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] photodirector.ChatUIViewController is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'photodirector.ChatUIViewController')
    with step("[Action] Tap chatBackButton at (54.8%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatBackButton', 54.8, 64.5)
    with step("[Action] Tap AI Edit Agent at (77.5%, 13.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', 77.5, 13.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap chatMenuButton at (64.5%, 71.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatMenuButton', 64.5, 71.0)
    with step("[Action] Tap Old Chat at (94.1%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Old Chat', 94.1, 52.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.ChatUIViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=353, container_h=753)
    with step("[Action] Tap imageView at (60.1%, 43.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 60.1, 43.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatCollectionView', container_w=422, container_h=774)
    with step("[Verify] titleLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'titleLabel')
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="previewScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage')
    with step("[Action] Tap imageView at (57.6%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 57.6, 81.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='historyThumbnailCollectionView', container_w=430, container_h=88)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="previewScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', expected_result='different', threshold=0.95)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="previewScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage')
    with step("[Action] Tap imageView at (47.0%, 60.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'imageView', 47.0, 60.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='historyThumbnailCollectionView', container_w=430, container_h=88)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.XPATH, '//XCUIElementTypeScrollView[@name="previewScrollView"]/XCUIElementTypeScrollView/XCUIElementTypeImage', expected_result='different', threshold=0.95)
    with step("[Action] Tap historyAddToInputButton at (47.2%, 47.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'historyAddToInputButton', 47.2, 47.0)
    with step("[Action] Tap chatInputImageRemoveButton at (52.5%, 43.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatInputImageRemoveButton', 52.5, 43.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatInputImagePreview', container_w=408, container_h=88)
    with step("[Verify] Capture '00226_AIAgent_ProPlusUser_Step60' for GT comparison"):
        actions.capture_for_gt('00226_AIAgent_ProPlusUser_Step60', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.ChatUIViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap downloadButton at (74.3%, 36.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'downloadButton', 74.3, 36.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatCollectionView', container_w=422, container_h=774)
    with step("[Action] Tap editButton at (60.0%, 47.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'editButton', 60.0, 47.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatCollectionView', container_w=422, container_h=774)
    with step("[Verify] EditingImageView_ImageView is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step("[Action] Tap AI Edit Agent at (81.7%, 21.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', 81.7, 21.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap chatMenuButton at (25.8%, 22.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatMenuButton', 25.8, 22.6)
    with step("[Action] Long press Old Chat at (33.8%, 38.1%)"):
        actions.long_press_within_element(AppiumBy.ACCESSIBILITY_ID, 'Old Chat', 33.8, 38.1, duration=1.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.ChatUIViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=353, container_h=753)
    with step("[Action] Tap Delete at (32.0%, 46.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Delete', 32.0, 46.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[6]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=250, container_h=933)
    with step("[Action] Tap Delete at (14.3%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Delete', 14.3, 53.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Delete The Chat?"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=81)
    with step("[Verify] Old Chat is not visible"):
        actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Old Chat')
    with step("[Action] Tap photodirector.ChatUIViewController at (6.5%, 9.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photodirector.ChatUIViewController', 6.5, 9.2)
    with step("[Action] Tap chatBackButton at (45.2%, 58.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatBackButton', 45.2, 58.1)
    with step("[Action] Tap homeButton at (65.4%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 65.4, 53.8)
    with step("[Action] Tap Discard at (15.8%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 15.8, 60.0)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
