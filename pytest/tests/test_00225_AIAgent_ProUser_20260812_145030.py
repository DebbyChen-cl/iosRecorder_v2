import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00225_AIAgent_ProUser_20260812_145030")
def test_00225_AIAgent_ProUser_20260812_145030(actions: DriverActions):
    with step("[Action] Tap btnSettings at (51.5%, 52.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 51.5, 52.9)
    with step("[Action] Tap About at (35.3%, 39.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 35.3, 39.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (40.8%, 38.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 40.8, 38.0)
    with step("[Action] Tap Free at (70.6%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 70.6, 71.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro at (18.8%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro', 18.8, 69.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (50.0%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 50.0, 55.6)
    with step("[Action] Tap btnBack at (50.0%, 59.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 50.0, 59.6)
    with step("[Action] Tap btnBack at (57.1%, 61.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 57.1, 61.7)
    with step("[Action] Tap AI Edit Agent at (57.3%, 16.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent', 57.3, 16.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView', container_w=430, container_h=203)
    with step("[Verify] chatWelcomeBannerDialog-messageLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'chatWelcomeBannerDialog-messageLabel')
    with step("[Verify] chatWelcomeBannerDialog-titleLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'chatWelcomeBannerDialog-titleLabel')
    with step("[Action] Tap chatWelcomeBannerDialog-closeButton at (33.3%, 30.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatWelcomeBannerDialog-closeButton', 33.3, 30.8)
    with step("[Action] Tap navArtworkButton at (29.0%, 61.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navArtworkButton', 29.0, 61.3)
    with step("[Verify] AI Edit Agent is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AI Edit Agent')
    with step("[Action] Tap btnBack at (64.5%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 64.5, 51.6)
    with step("[Action] Tap chatSuggestionSuggestMeButton at (4.5%, 22.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSuggestionSuggestMeButton', 4.5, 22.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='chatCollectionView', container_w=422, container_h=774)
    with step("[Action] Tap chatPhotoButton at (25.0%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatPhotoButton', 25.0, 67.5)
    with step("[Action] Tap btnAlbum at (89.8%, 73.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 89.8, 73.8)
    with step("[Action] Tap Sample Photos at (16.1%, 52.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 16.1, 52.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=632)
    with step("[Action] Tap PhDM_example_8 at (34.6%, 62.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_8', 34.6, 62.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=632)
    with step("[Action] Tap btnNext at (15.7%, 61.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 15.7, 61.1)
    with step("[Action] Tap chatSendButton at (37.5%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 37.5, 80.0)
    with step("[Verify] Thinking disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Thinking', appear_timeout=5, disappear_timeout=1200), 'Thinking did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap Tell AI Edit Agent your requirements at (6.3%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 6.3, 50.0)
    with step("[Action] Type 'more suggestion?' into Tell AI Edit Agent your requirements"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 'more suggestion?')
    with step("[Action] Tap chatSendButton at (20.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 20.0, 50.0)
    with step("[Verify] Thinking disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Thinking', appear_timeout=5, disappear_timeout=1200), 'Thinking did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap Tell AI Edit Agent your requirements at (20.3%, 86.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 20.3, 86.4)
    with step("[Action] Type 'more suggestion?' into Tell AI Edit Agent your requirements"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 'more suggestion?')
    with step("[Action] Tap chatSendButton at (30.0%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 30.0, 70.0)
    with step("[Action] Tap chatInputTextView at (55.5%, 27.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatInputTextView', 55.5, 27.3)
    with step("[Action] Type 'more suggestion?' into chatInputTextView"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chatInputTextView', 'more suggestion?')
    with step("[Action] Tap chatSendButton at (45.0%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 45.0, 75.0)
    with step("[Verify] Thinking disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Thinking', appear_timeout=5, disappear_timeout=1200), 'Thinking did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap chatInputTextView at (63.7%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatInputTextView', 63.7, 63.6)
    with step("[Action] Type 'more suggestion?' into chatInputTextView"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chatInputTextView', 'more suggestion?')
    with step("[Action] Tap chatSendButton at (32.5%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 32.5, 75.0)
    with step("[Verify] Thinking disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Thinking', appear_timeout=5, disappear_timeout=1200), 'Thinking did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap Tell AI Edit Agent your requirements at (31.1%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 31.1, 54.5)
    with step("[Action] Type 'more suggestion?' into Tell AI Edit Agent your requirements"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 'more suggestion?')
    with step("[Action] Tap chatSendButton at (17.5%, 85.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 17.5, 85.0)
    with step("[Verify] Thinking disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Thinking', appear_timeout=5, disappear_timeout=1200), 'Thinking did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap Tell AI Edit Agent your requirements at (18.5%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 18.5, 45.5)
    with step("[Action] Type 'more suggestion?' into Tell AI Edit Agent your requirements"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 'more suggestion?')
    with step("[Action] Tap chatSendButton at (27.5%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 27.5, 57.5)
    with step("[Verify] Thinking disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Thinking', appear_timeout=5, disappear_timeout=1200), 'Thinking did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap Tell AI Edit Agent your requirements at (18.2%, 22.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 18.2, 22.7)
    with step("[Action] Type 'more suggestion?' into Tell AI Edit Agent your requirements"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 'more suggestion?')
    with step("[Action] Tap chatSendButton at (20.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 20.0, 52.5)
    with step("[Verify] Thinking disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Thinking', appear_timeout=5, disappear_timeout=1200), 'Thinking did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap Tell AI Edit Agent your requirements at (80.1%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 80.1, 54.5)
    with step("[Action] Type 'more suggestion?' into Tell AI Edit Agent your requirements"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 'more suggestion?')
    with step("[Action] Tap chatSendButton at (17.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 17.5, 50.0)
    with step("[Verify] Thinking disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Thinking', appear_timeout=5, disappear_timeout=1200), 'Thinking did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap Tell AI Edit Agent your requirements at (62.9%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 62.9, 68.2)
    with step("[Action] Type 'more suggestion?' into Tell AI Edit Agent your requirements"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 'more suggestion?')
    with step("[Action] Tap chatSendButton at (35.0%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 35.0, 57.5)
    with step("[Verify] Thinking disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'Thinking', appear_timeout=5, disappear_timeout=1200), 'Thinking did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap Tell AI Edit Agent your requirements at (63.3%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 63.3, 68.2)
    with step("[Action] Type 'more suggestion?' into Tell AI Edit Agent your requirements"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tell AI Edit Agent your requirements', 'more suggestion?')
    with step("[Action] Tap chatSendButton at (30.0%, 57.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendButton', 30.0, 57.5)
    with step("[Verify] chatSendLimitBannerDialog-messageLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'chatSendLimitBannerDialog-messageLabel')
    with step("[Action] Tap chatSendLimitBannerDialog-closeButton at (33.3%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatSendLimitBannerDialog-closeButton', 33.3, 46.2)
    with step("[Action] Tap chatBackButton at (64.5%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chatBackButton', 64.5, 64.5)
    assert True
