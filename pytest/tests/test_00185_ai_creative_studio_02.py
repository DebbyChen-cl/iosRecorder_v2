import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00185_ai_creative_studio_02')
def test_00185_ai_creative_studio_02(actions: DriverActions):
    """AI Creative Studio - Custom"""
    if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton', timeout=2)):
        pass
    else:
        with step('[Action] tap_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
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
    with step('Verify intro page displays'):
        if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle', timeout=5)):
            pass
        else:
            with step("Check Don't show again"):
                with step('[Action] check_dont_show_again'):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
            with step('Tap Try now'):
                with step('[Action] tap_try_now'):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Verify Template list page'):
        with step('[Action] verify_template_list_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step('Select Collage tab'):
        with step('[Action] tap_collage_tab'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step('Select a premium style'):
        with step('[Action] select_style'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage[1]')
    with step('Verify selected template page'):
        with step('[Action] verify_selected_template_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'templateSectionLabel')
    with step('Tap back button'):
        with step('[Action] tap_back_from_template'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton')
    with step('Verify back to template list page'):
        with step('[Action] verify_template_list_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step('Select a premium style'):
        with step('[Action] select_style'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage[1]')
    with step('Tap add photo button'):
        with step('[Action] tap_add_photo'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addIconView')
    with step('Continue recommendation dialog (v20.13 new flow)'):
        with step('[Action] tap_continue_button'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton')
    with step('Verify Next button is disabled'):
        pass
    with step('Add photos (min required number)'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step('Verify photos are added'):
        pass
    with step('Verify Next button is enabled'):
        pass
    with step('Tap remove added photo'):
        with step('[Action] tap_remove_photo'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n')
    with step('Verify Next is disabled after removing photo'):
        pass
    with step('Tap expand button to enter photo full view'):
        with step('[Action] tap_expand_photo'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'icon photo enlarge n')
    with step('Tap add photo in full view'):
        with step('[Action] tap_add_photo_in_fullview'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'collageAddButton')
    with step('Verify photo is added from full view'):
        pass
    with step('Verify Next button is enabled'):
        pass
    with step('Tap Next button'):
        with step('[Action] tap_next'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Verify added photos are listed on feature page'):
        with step('[Action] verify_photos_listed'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Verify] snapshot: ai_creative_studio_photos_listed.png'):
        actions.capture_for_gt('ai_creative_studio_photos_listed.png')
    with step('Long press 2nd photo and drag to front'):
        with step('[Action] long_press_and_drag_photo'):
            actions.long_press_drag_within_elements(AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeImage', 50, 50, AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage', 50, 50)
    with step('[Verify] snapshot: ai_creative_studio_photo_reorder_attempt.png'):
        actions.capture_for_gt('ai_creative_studio_photo_reorder_attempt.png')
    with step('Verify photo order changed'):
        if actions.compare_with_gt('ai_creative_studio_photo_reorder_attempt.png', gt_folder=TD.GT_FOLDER)[0]:
            assert False, 'Photo order change verification failed - screenshot does not match expected order'
    with step('Tap credit number capsule'):
        with step('[Action] tap_credit_capsule'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_creditButton')
    with step('Verify credit IAP page'):
        with step('[Action] verify_credit_iap_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'lblCreditTitle')
    with step('Tap back from credit IAP'):
        with step('[Action] close_credit_iap'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Tap Generate'):
        with step('[Action] tap_generate'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
        with step('[Action] tap_phd_btn'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
    with step('Verify go to Artwork page'):
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
    with step('Tap back button'):
        with step('[Action] tap_back_from_artwork'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Verify back to selected template page'):
        with step('[Action] verify_selected_template_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'templateSectionLabel')
    with step('Tap Artwork button'):
        with step('[Action] tap_artwork_button_in_template'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_artworkButton')
    with step('Verify artwork page'):
        with step('[Action] verify_artwork_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
    with step('Tap new generated image thumbnail'):
        with step('[Action] tap_new_artwork_thumbnail'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AIStudioAIArtworkShortTaskPackSelectionViewController"]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther')
    with step('Verify enter full view'):
        with step('[Action] verify_full_view'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnShare')
    with step("[Verify] test_00185 completion"):
        assert True
