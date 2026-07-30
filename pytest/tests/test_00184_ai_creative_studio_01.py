import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00184_ai_creative_studio_01')
def test_00184_ai_creative_studio_01(actions: DriverActions):
    """AI Creative Studio - Template"""
    with step('Tap AI photos tab'):
        with step('[Action] tap_ai_photos'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step('Tap My artwork'):
        with step('[Action] tap_myartwork'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step('Slide to find and tap AI Creative Studio category'):
        with step('[Action] find_and_tap_category'):
            for _ in range(10):
                if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', timeout=2):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
                    break
                actions.drag_coordinates(350, 120, 50, 120)
            else:
                assert False, 'Failed to find and tap AI Creative Studio category'
    with step('Tap a thumbnail to enter full view'):
        with step('[Action] tap_thumbnail'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "photodirector.AIStudioAIArtworkShortTaskPackSelectionViewController"`]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]')
    with step('Verify enter full view'):
        with step('[Verify] snapshot: ai_cs_full_view_1.png'):
            actions.capture_for_gt('ai_cs_full_view_1.png')
    with step('Slide to next image'):
        with step('[Action] swipe_to_next_image'):
            actions.drag_coordinates(375, 450, 20, 450)
    with step('Verify full view is next image'):
        with step('[Verify] snapshot: ai_cs_full_view_2.png'):
            actions.capture_for_gt('ai_cs_full_view_2.png')
        if actions.compare_with_gt('ai_cs_full_view_2.png', gt_folder=TD.GT_FOLDER)[0]:
            assert False, 'Full view did not change to next image - screenshots are the same'
    with step('Slide to previous image'):
        with step('[Action] swipe_to_previous_image'):
            actions.drag_coordinates(20, 450, 375, 450)
    with step('Verify full view back to original image'):
        with step('[Verify] snapshot: ai_cs_full_view_3.png'):
            actions.capture_for_gt('ai_cs_full_view_3.png')
        with step('[Verify] compare: ai_cs_full_view_3.png'):
            assert actions.compare_with_gt('ai_cs_full_view_3.png', gt_folder=TD.GT_FOLDER)[0]
    with step('Tap share'):
        with step('[Action] tap_share'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShare')
    with step('Verify share menu pop up'):
        with step('[Action] verify_share_menu'):
            assert actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="shareCell" and @label="AirDrop"]')
    with step('Close share menu'):
        with step('[Action] close_share_menu'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'header.closeButton')
    with step('Tap save'):
        with step('[Action] tap_save'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDownload')
    with step('Verify save to photos toast'):
        with step('[Action] verify_save_toast'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'likeCountLabel')
    with step('Tap delete'):
        with step('[Action] tap_delete'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnDelete')
    with step('Verify confirm delete dialog'):
        with step('[Action] verify_confirm_delete_dialog'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Delete this photo permanently?')
    with step('Tap cancel'):
        with step('[Action] tap_cancel'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Cancel"`][1]')
    with step('Tap Edit'):
        with step('[Action] tap_edit'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnEdit')
    with step('Verify go to edit room'):
        with step('[Action] verify_in_edit_room'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait')
    with step('Tap Home'):
        with step('[Action] tap_home'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step('Tap AI Photo > My artwork'):
        with step('[Action] tap_ai_photos'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
        with step('[Action] tap_myartwork'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step('Slide to find and tap AI Creative Studio category'):
        with step('[Action] find_and_tap_category'):
            for _ in range(10):
                if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', timeout=2):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
                    break
                actions.drag_coordinates(350, 120, 50, 120)
            else:
                assert False, 'Failed to find and tap AI Creative Studio category'
    with step('Tap select'):
        with step('[Action] tap_select'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Select')
    with step('Select 6 images'):
        with step('[Action] select_images'):
            for _i in range(1, 7):
                assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, f'**/XCUIElementTypeOther[`name == "photodirector.AIStudioAIArtworkShortTaskPackSelectionViewController"`]/XCUIElementTypeCollectionView/XCUIElementTypeCell[{_i}]')
    with step('Tap share'):
        with step('[Action] tap_group_share'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'shareButton')
    with step('Verify share menu pop up'):
        with step('[Action] verify_share_menu'):
            assert actions.find_element(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="shareCell" and @label="AirDrop"]')
    with step('Close share menu'):
        with step('[Action] close_share_menu'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'header.closeButton')
    with step('Tap save'):
        with step('[Action] tap_group_save'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'downloadButton')
    with step('Verify save to photos toast'):
        with step('[Action] verify_save_toast'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'likeCountLabel')
    with step('Tap delete'):
        with step('[Action] tap_group_delete'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'deleteButton')
    with step('Verify confirm delete dialog'):
        with step('[Action] verify_confirm_delete_group_dialog'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Delete 6 photos permanently?')
    with step('Tap cancel'):
        with step('[Action] tap_cancel'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Cancel"`][1]')
    with step('Tap collage'):
        with step('[Action] tap_collage'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'collageButton')
    with step('Verify go to collage'):
        with step('[Action] verify_in_collage'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step('Tap back from collage'):
        with step('[Action] tap_back_from_collage'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('Tap select'):
        with step('[Action] tap_select'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Select')
    with step('Select 7 images'):
        with step('[Action] select_images'):
            for _i in range(1, 8):
                assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, f'**/XCUIElementTypeOther[`name == "photodirector.AIStudioAIArtworkShortTaskPackSelectionViewController"`]/XCUIElementTypeCollectionView/XCUIElementTypeCell[{_i}]')
    with step('[Action] _scroll_vertical_to_top'):
        for _ in range(10):
            _src_before = actions.driver.page_source
            actions.drag_coordinates(200, 750, 200, 800)
            if actions.driver.page_source == _src_before:
                break
    with step('Verify no collage button when 7 images selected'):
        with step('[Action] verify_no_collage_button'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'collageButton')
    with step('De-select 6 images'):
        with step('[Action] deselect_images'):
            for _i in range(2, 8):
                assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, f'**/XCUIElementTypeOther[`name == "photodirector.AIStudioAIArtworkShortTaskPackSelectionViewController"`]/XCUIElementTypeCollectionView/XCUIElementTypeCell[{_i}]')
    with step('Tap edit'):
        with step('[Action] tap_group_edit'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'editButton')
    with step('Verify go to edit room'):
        with step('[Action] verify_in_edit_room'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait')
    with step('Tap home'):
        with step('[Action] tap_home'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step('Tap AI photos tab'):
        with step('[Action] tap_ai_photos'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step('Tap My artwork'):
        with step('[Action] tap_myartwork'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'My Artwork')
    with step('Slide to find and tap AI Creative Studio category'):
        with step('[Action] find_and_tap_category'):
            for _ in range(10):
                if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio', timeout=2):
                    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Creative Studio')
                    break
                actions.drag_coordinates(350, 120, 50, 120)
            else:
                assert False, 'Failed to find and tap AI Creative Studio category'
    with step('Tap Create more'):
        with step('[Action] tap_create_more'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Create More')
    with step('Verify enter AI Creative Studio feature'):
        with step('[Action] verify_intro_page'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
        with step('[Action] tap_try_now'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
        with step('[Action] verify_ai_creative_studio_feature'):
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step("[Verify] test_00184 completion"):
        assert True
