import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00224_AIAgent_FreeUser_20260812_143909")
def test_00224_AIAgent_FreeUser_20260812_143909(actions: DriverActions):
    with step("[Action] Tap AI Edit Agent at (19.8%, 24.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', 19.8, 24.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Verify] chatWelcomeBannerDialog-titleLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'chatWelcomeBannerDialog-titleLabel')
    with step("[Action] Tap chatWelcomeBannerDialog-closeButton at (70.4%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatWelcomeBannerDialog-closeButton', 70.4, 48.1)
    with step("[Action] Tap chatInfoButton at (71.0%, 71.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatInfoButton', 71.0, 71.0)
    with step("[Verify] //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther')
    with step("[Action] Tap Confirm at (12.3%, 73.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Confirm', 12.3, 73.5)
    with step("[Action] Tap chatPhotoButton at (30.0%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatPhotoButton', 30.0, 40.0)
    with step("[Action] Tap btnAlbum at (93.4%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 93.4, 54.8)
    with step("[Action] Tap Sample Photos at (65.2%, 60.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 65.2, 60.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=632)
    with step("[Action] Tap PhDM_example_1 at (40.0%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_1', 40.0, 42.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap PhDM_example_2 at (50.0%, 35.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_2', 50.0, 35.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap PhDM_example_3 at (43.8%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_3', 43.8, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap PhDM_example_6 at (46.2%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_6', 46.2, 53.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap PhDM_example_7 at (47.7%, 56.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_7', 47.7, 56.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Verify] Capture '00224_AIAgent_FreeUser_Step15' for GT comparison"):
        actions.capture_for_gt('00224_AIAgent_FreeUser_Step15', AppiumBy.ACCESSIBILITY_ID, 'selectionContainerView', threshold=0.95)
    with step("[Action] Tap btn FontDelete n at (68.2%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n', 68.2, 54.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=430, container_h=74)
    with step("[Action] Tap btn FontDelete n at (54.5%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n', 54.5, 45.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=430, container_h=74)
    with step("[Action] Tap btn FontDelete n at (59.1%, 40.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n', 59.1, 40.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=430, container_h=74)
    with step("[Action] Tap btn FontDelete n at (45.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n', 45.5, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="selectionContainerView"]/XCUIElementTypeOther/XCUIElementTypeTable', container_w=430, container_h=74)
    with step("[Verify] Capture '00224_AIAgent_FreeUser_Step20' for GT comparison"):
        actions.capture_for_gt('00224_AIAgent_FreeUser_Step20', AppiumBy.ACCESSIBILITY_ID, 'selectionContainerView', threshold=0.95)
    with step("[Action] Tap PhDM_example_8 at (41.5%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_8', 41.5, 67.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap btnNext at (14.3%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 14.3, 55.6)
    with step("[Verify] Capture '00224_AIAgent_FreeUser_Step23' for GT comparison"):
        actions.capture_for_gt('00224_AIAgent_FreeUser_Step23', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.ChatUIViewController"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther', threshold=0.95)
    with step("[Action] Tap chatSuggestionSuggestMeButton at (3.1%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSuggestionSuggestMeButton', 3.1, 57.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatCollectionView', container_w=422, container_h=774)
    with step("[Verify] messageLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'messageLabel')
    with step("[Verify] Here are a few edit ideas is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Here are a few edit ideas')
    with step("[Action] Tap chatSuggestionButton-0 at (2.1%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSuggestionButton-0', 2.1, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatCollectionView', container_w=422, container_h=774)
    with step("[Action] Tap chatSendButton at (20.0%, 72.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 20.0, 72.5)
    with step("[Verify] //XCUIElementTypeCell[@name=\"ChatMessageCell-8\"]/XCUIElementTypeOther/XCUIElementTypeOther disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="ChatMessageCell-8"]/XCUIElementTypeOther/XCUIElementTypeOther', appear_timeout=5, disappear_timeout=1200), '//XCUIElementTypeCell[@name="ChatMessageCell-8"]/XCUIElementTypeOther/XCUIElementTypeOther did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Thinking disappears within 1200s"):
            assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Thinking', appear_timeout=5, disappear_timeout=1200), 'Thinking did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Processing... disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Processing...', appear_timeout=5, disappear_timeout=1200), 'Processing... did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Result 1 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Result 1')
    with step("[Verify] What you can try next is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'What you can try next')
    with step("[Action] Tap chatSuggestionButton-0 at (99.4%, 25.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSuggestionButton-0', 99.4, 25.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatCollectionView', container_w=422, container_h=774)
    with step("[Action] Tap chatSendButton at (32.5%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 32.5, 57.5)
    with step("[Verify] Thinking disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Thinking', appear_timeout=5, disappear_timeout=1200), 'Thinking did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Processing... disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Processing...', appear_timeout=5, disappear_timeout=1200), 'Processing... did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Result 2 is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Result 2')
    with step("[Action] Tap chatSuggestionButton-0 at (4.8%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSuggestionButton-0', 4.8, 30.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatCollectionView', container_w=422, container_h=774)
    with step("[Action] Tap chatSendButton at (72.5%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 72.5, 52.5)
    with step("[Verify] chatSendLimitBannerDialog-titleLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'chatSendLimitBannerDialog-titleLabel')
    with step("[Action] Tap chatSendLimitBannerDialog-closeButton at (77.8%, 23.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendLimitBannerDialog-closeButton', 77.8, 23.1)
    with step("[Action] Tap chatBackButton at (61.3%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatBackButton', 61.3, 54.8)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
