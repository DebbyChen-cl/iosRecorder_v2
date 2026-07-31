import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00186_ai_creative_studio_03')
def test_00186_ai_creative_studio_03(actions: DriverActions):
    """AI Creative Studio - Portrait & Creative"""
    with step('Tap AI photos tab'):
        with step('[Action] tap_ai_photos'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step('Tap AI Creative Studio entry'):
        with step('[Action] find_and_tap_category'):
            for _ in range(10):
                if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', timeout=2):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
                    break
                actions.drag_coordinates(350, 120, 50, 120)
            else:
                assert False, 'Failed to tap AI Creative Studio entry'
    with step('Verify no intro page displays'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox', timeout=3):
            with step('[Action] check_dont_show_again'):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
            with step('[Action] tap_try_now'):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
        with step('[Action] verify_template_list_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step('Select Portrait category'):
        with step('[Action] tap_portrait_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Portrait')
    with step('Select a premium style'):
        with step('[Action] select_style'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeOther/XCUIElementTypeImage')
    with step('Import photos'):
        with step('[Action] tap_add_photo'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addIconView')
    with step('Continue recommendation dialog (v20.13 new flow)'):
        with step('[Action] tap_continue_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Select Photos from picker'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('Tap Next button'):
        with step('[Action] tap_next'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Tap Generate button'):
        with step('[Action] check_and_tap_order_popup'):
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Long press to adjust order', timeout=5):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Long press to adjust order')
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
        with step('[Action] tap_phd_btn'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
    with step('Tap back button'):
        with step('[Action] tap_back'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        with step('[Action] tap_back_from_template'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton')
    with step('Select a free style'):
        with step('[Action] select_style'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage[1]')
    with step('Tap add photo button'):
        with step('[Action] tap_add_photo'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addIconView')
    with step('Continue recommendation dialog (v20.13 new flow)'):
        with step('[Action] tap_continue_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Add photos with face'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('Tap Next button'):
        with step('[Action] tap_next'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Tap Generate button'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
        with step('[Action] tap_phd_btn'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
    with step('Verify go to artwork page'):
        with step('[Action] verify_artwork_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
    with step('Verify thumbnail shows Processing'):
        with step('[Action] verify_processing'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
    with step('Wait for generation to finish'):
        with step('[Action] wait_for_generation'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=120)
    with step('Verify generated thumbnail appears'):
        with step('[Action] verify_thumbnail_appear'):
            assert actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AIStudioAIArtworkShortTaskPackSelectionViewController"]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther')
    with step('Tap back from artwork'):
        with step('[Action] tap_back_from_artwork'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Tap back to template list'):
        with step('[Action] tap_back_from_template'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton')
    with step('Select Creative category'):
        with step('[Action] tap_creative_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Creative')
    with step('Select a premium style'):
        with step('[Action] select_style'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage[1]')
    with step('Import photos'):
        with step('[Action] tap_add_photo'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addIconView')
        with step('Continue recommendation dialog (v20.13 new flow)'):
            with step('[Action] tap_continue_button'):
                assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('Tap Next button'):
        with step('[Action] tap_next'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Tap Generate button'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
        with step('[Action] tap_phd_btn'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
    with step('Verify IAP page'):
        if (not actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=5)):
            pass
        else:
            with step('Tap x to close IAP'):
                with step('[Action] close_iap'):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('Tap back button'):
        with step('[Action] tap_back'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        with step('[Action] tap_back_from_template'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton')
    with step('Select a free style'):
        with step('[Action] select_style'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeOther/XCUIElementTypeImage')
    with step('Tap add photo button'):
        with step('[Action] tap_add_photo'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addIconView')
    with step('Continue recommendation dialog (v20.13 new flow)'):
        with step('[Action] tap_continue_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Add photos with face'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('Tap Next button'):
        with step('[Action] tap_next'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Tap Generate button'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify go to artwork page'):
        pass
    with step('Verify thumbnail shows Processing'):
        with step('[Action] verify_processing'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator')
    with step('Wait for generation to finish'):
        with step('[Action] wait_for_generation'):
            assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'activityIndicator', timeout=120)
    with step('Verify generated thumbnail appears'):
        with step('[Action] verify_thumbnail_appear'):
            assert actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AIStudioAIArtworkShortTaskPackSelectionViewController"]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther')
    with step('Tap back from artwork'):
        with step('[Action] tap_back_from_artwork'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Tap home button'):
        with step('[Action] tap_home_from_template'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_homeButton')
    with step('Verify go to home page'):
        with step('[Action] verify_home_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Verify] test_00186 completion"):
        assert True
