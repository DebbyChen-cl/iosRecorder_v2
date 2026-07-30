import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00151_main_G02_01_04')
def test_00151_main_G02_01_04(actions: DriverActions):
    """AI anime video"""
    mode = 1
    uuid = ['00db6d6d-d71b-47aa-9797-91a6c462bf14', '0fb561f2-b225-4914-b06f-3ca19487031b', 'a8c4fd6d-1f7f-42ad-9956-d9c1e3180271', 'd7d1ab13-b62f-4c3a-9b6b-c75772ea9b7f', 'eb570194-992d-4cee-afe8-ee074057bcb6', 'c62a3f7f-ce92-41cd-9084-7d8924d40552', '7570f944-3e8c-42e1-ae31-eece9949d67c', '9e6fc789-4334-4a76-8154-dcc9cb87f85d', 'ed942de2-58ea-4c22-a318-56cbc9d15cac', '70c6fc32-0d28-4337-934e-997ad1c06a6d', 'dc6422d1-7e01-4798-99bc-c028f8668dba', '083de870-3524-45eb-b3eb-c5e217b08388', '45b11cb8-1b1f-464d-8493-0e7857be6b86', '7a607c1e-b158-43c2-9430-f2c53c51f524', 'b8b89075-2d9e-4d57-ba45-0a5ff59fdf6c', 'e1d00f67-93ba-4325-b483-107747d6281b', 'e6eca8e9-89cb-436f-a5ae-530abdc3d6dd', '9cc33ffc-7e72-470b-b8af-26e3bf7b6b57', 'db8bbf72-a089-45d7-a86f-1b84278cacb0', 'ae87fca3-b969-4b9f-bfc3-3bfad215acee']
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Videos')
    with step('[Verify] snapshot: G02_01_04_before_tap_ai_anime_video.png'):
        actions.capture_for_gt('G02_01_04_before_tap_ai_anime_video.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Anime Video')
    with step('[Verify] snapshot: G02_01_04_after_tap_ai_anime_video.png'):
        actions.capture_for_gt('G02_01_04_after_tap_ai_anime_video.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Try Now')
    with step('[Verify] snapshot: G02_01_04_after_tap_ai_try_now.png'):
        actions.capture_for_gt('G02_01_04_after_tap_ai_try_now.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navArtworkButton')
    with step('[Verify] snapshot: G02_01_04_go_to_artwork.png'):
        actions.capture_for_gt('G02_01_04_go_to_artwork.png')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AIAnimeVideoHistoryCellView-0')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]', timeout=5):
            actions.wait_for_invisible(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Save')
    with step('[Action] tap_share_to_FB_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Post')
    with step('[Action] close_share_to_FB_panel'):
        assert actions.tap_by_coordinates(42, 41)
    with step('[Action] tap_share_to_IG_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Instagram')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram')
    with step('[Action] back_to_phd_from_sns'):
        actions.activate_app('com.cyberlink.photodirector')
    with step('[Action] tap_share_to_more_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'More')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    if actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="shareCell" and @label="AirDrop"]'):
        pass
    else:
        assert False, 'Share more fail (uuid[8])'
    with step('[Action] close_share_more_panel'):
        assert actions.tap_by_coordinates(63, 277)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic play whiteCircleBg black')):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'):
        pass
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')):
        pass
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')):
        pass
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    if actions.is_element_present(AppiumBy.NAME, 'Save & Share'):
        pass
    else:
        assert False, 'Back to save page fail (uuid[16])'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Videos')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Anime Video')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Try Now')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Continue with the Vivid Style')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'iconImageView'):
        pass
    else:
        assert False, 'Cash mode fail (uuid[17])'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'iconImageView')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'):
        pass
    else:
        assert False, 'IAP fail (uuid[19])'
    with step('[Action] close_IAP'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Credits')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblPlan'):
        pass
    else:
        assert False, 'Price page fail (uuid[1])'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Select Video and Trim')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'):
        pass
    else:
        assert False, 'Intro page fail (uuid[2])'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] select_video'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collections')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_Video')
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "PXGGridLayout-Info"`][2]')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Choose')
    with step('[Verify] snapshot: G02_01_04_before_trim.png'):
        actions.capture_for_gt('G02_01_04_before_trim.png')
    from_pos = (60, 718)
    destination = (140, 718)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 718, 140, 718)
    with step('[Verify] snapshot: G02_01_04_after_trim.png'):
        actions.capture_for_gt('G02_01_04_after_trim.png')
    if (not actions.compare_with_gt('G02_01_04_after_trim.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Trim fail (uuid[3])'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeButton')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'labelProcessing')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Please keep the app open.', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Please keep the app open.')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'):
        pass
    else:
        assert False, 'Generate fail (uuid[4])'
    with step("[Verify] test_00151 completion"):
        assert True
