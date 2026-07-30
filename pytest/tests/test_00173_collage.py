# @sft-convert:generated  (自動生成；若手動編輯，請把檔名加進 .scratch/sft-convert/PROTECT.txt
#                          或把本行改成 '# @manual'，即不會被覆蓋)
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00173_collage')
def test_00173_collage(actions: DriverActions):
    """collage"""
    uuid = ['ac5e29c9-5254-4c3e-b03d-191bda504d63', 'ff20597c-9ac8-47db-ad28-f8a9f848387d', 'c5157fa9-6edd-4ffe-b3a3-8a7d55071ef2', '334141d6-0316-47f7-a38b-b4bdac74d5de', '3b589521-e4f6-4d43-9b06-e897b32ccc8f', '30a24cd9-6a71-4fbc-a134-e57ee4860881', '7826433c-1bb6-40db-8682-37a1e77aaf05', '5946b9d7-a8bb-4168-a003-b103d4ab9b12', '26b7a36a-6168-4c3f-bc6f-a206902d0aa9', 'e5f75d7b-8795-423f-821b-435b7cb2d673', 'aaeea69f-0a83-4828-8e3c-cf4f0f4bab51', '94d4a700-8190-445d-9dbc-5b0442a8b878', 'd79809f1-4930-4e3b-8a97-e720fcbacc48', 'd59b5ed1-6c30-4015-9266-45980eabf9cd', 'd66f0b6b-ca8c-4341-a4b7-534fac77c4f7', '2aaa46de-5fce-4f0b-9dda-f48da1e5e7b7', '4f3a75c9-07c0-4766-ac8e-eccdfffa148f', 'f98538f5-e697-4f67-960b-cf59d7ebb122', '547a1dea-a2a6-41af-b6ad-127386be2d5e', '34b19160-afc8-4c1a-938c-666e60717668', '03683888-1d59-4bff-b9b4-c6db7261c310', '2a74fa94-6890-4cd9-9d09-264ed6a5169e', 'bb9bdc45-3f79-416f-83b6-e0cf99aeec3b', 'a0cf7b68-58a9-4587-9c54-628bc873e7b2', 'c569b4ef-7f59-4ff5-a9f5-ae53ef20e0cd', 'ab7ebff1-4267-4dfc-b2a9-9f9a5d7a942b', 'b8a27c5e-b317-41ed-8387-827135449da0', 'b06c1243-7505-4f27-a3ed-174467ee5fc1', 'da76c4b4-dac3-4922-a70b-4c366bf3ffa2', '665d0738-be4f-426d-81d1-36565cfb1089', '91730cb6-9e7e-414e-a1ee-8dad5b913aab', '8f3a2163-0c5a-4e0c-8ec6-2e634532ea4b', '230f3e70-d106-4dc9-9b00-30fde3e56f6c', '5b3b95be-7faf-4e85-af66-528afb743f29', '1a647c30-cc9c-4c98-957d-ba140c836e90', '25bbc82f-54c0-4b67-811b-c9a2c374b2d7', '2c11a377-f1fb-4256-8b55-41bf166c420b', 'a49461e8-8159-4b19-bbb0-029ed10fdf21', '6d20e487-cc0f-47e1-8765-1c214bb45af2', 'd943f76c-be50-4c54-82bf-81122933bdcd', '55421357-d45b-43d9-9c0b-8aada86f28f6']
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'More')):
        pass
    else:
        if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Less')):
            pass
        else:
            assert False, 'Failed to tap more or less button'
    assert actions.try_tap(AppiumBy.NAME, 'Collage'), '[06_03_01] Failed to tap collage'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    assert actions.tap_by_locator(AppiumBy.NAME, 'Collage'), '[06_03_01] Failed to tap collage again'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn2'), '[06_03_01] Failed to tap_2photo_cateogry'
    assert actions.tap_by_coordinates(70, 280)
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.NAME, '_AT')
    with step('[Verify] snapshot: 06_03_01_no_photo_selected.png'):
        actions.capture_for_gt('06_03_01_no_photo_selected.png')
    assert actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0'), '[06_03_01] Failed to select photo1'
    with step('[Verify] snapshot: 06_03_01_add_1_photo.png'):
        actions.capture_for_gt('06_03_01_add_1_photo.png')
    if actions.compare_with_gt('06_03_01_add_1_photo.png', gt_folder=TD.GT_FOLDER)[0]:
        assert False, 'Failed to add photo'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn FontDelete n'), '[06_03_01] Failed to tap remove photo'
    with step('[Verify] snapshot: 06_03_01_photo_removed.png'):
        actions.capture_for_gt('06_03_01_photo_removed.png')
    with step('[Verify] compare: 06_03_01_photo_removed.png'):
        assert actions.compare_with_gt('06_03_01_photo_removed.png', gt_folder=TD.GT_FOLDER)[0]
    assert actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0'), '[06_03_01] Failed to add photo1'
    assert actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1'), '[06_03_01] Failed to add photo'
    with step('[Verify] snapshot: 06_03_01_before_apply.png'):
        actions.capture_for_gt('06_03_01_before_apply.png')
    with step('[Action] click_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('[Verify] snapshot: 06_03_01_after_apply.png'):
        actions.capture_for_gt('06_03_01_after_apply.png')
    if (not actions.compare_with_gt('06_03_01_after_apply.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Verify] snapshot: 06_03_01_apply1_1.png'):
        actions.capture_for_gt('06_03_01_apply1_1.png')
    assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[2]'), '[06_03_01] Failed to select template 02'
    with step('[Verify] snapshot: 06_03_01_apply_another.png'):
        actions.capture_for_gt('06_03_01_apply_another.png')
    if (not actions.compare_with_gt('06_03_01_apply1_1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_store_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnWebstore')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnAll')
    with step('[Action] select_templatestore_collage_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn2')
    with step('[Action] verify_templatestore_collage_tab'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btn2')
    assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther')
    actions.capture_for_gt('06_03_01_change.png')
    if (not actions.compare_with_gt('06_03_01_change.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Verify] snapshot: 06_03_01_before_store.png'):
        actions.capture_for_gt('06_03_01_before_store.png')
    with step('[Action] tap_store_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnWebstore')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnAll')
    with step('[Action] tap_store_all'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAll')
    with step('[Action] verify_store_all'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnAll')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack'), '[06_03_01] Failed to tap artwork_back'
    with step('[Verify] snapshot: 06_03_01_after_store.png'):
        actions.capture_for_gt('06_03_01_after_store.png')
    if actions.compare_with_gt('06_03_01_before_store.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] click_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    for x in range(20):
        from_pos = (400, 780)
        destination = (40, 780)
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(400, 780, 40, 780)
    assert actions.tap_by_coordinates(395, 810)
    with step('[Verify] snapshot: 06_03_01_before_save.png'):
        actions.capture_for_gt('06_03_01_before_save.png')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), '[06_03_01] Failed to tap quick_done2'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK'), '[06_03_01] Failed to tap OK'
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=2):
            actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] close_rate_us_photo'):
        actions.is_element_present(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your Photo Looks Perfect!')
    assert actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'More'), '[06_03_01] Failed to tap share more'
    assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="shareCell" and @label="U"]'), '[06_03_01] Failed to tap share_to_U'
    actions.capture_for_gt('06_03_01_share_to_U.png')
    if actions.compare_with_gt('06_03_01_share_to_U.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False  # legacy raise
    with step('[Verify] snapshot: 06_03_01_share_U.png'):
        actions.capture_for_gt('06_03_01_share_U.png')
    assert actions.tap_by_coordinates(48, 89)
    assert actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'More'), '[06_03_01] Failed to tap share more for message'
    with step('[Action] tap_share_to_message_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_PREDICATE, 'name == "shareCell" AND label == "Messages"')
        assert actions.find_element(AppiumBy.IOS_PREDICATE, 'label == "New Message"')
    with step('[Verify] snapshot: 06_03_01_share_msg.png'):
        actions.capture_for_gt('06_03_01_share_msg.png')
    with step('[Action] Tap'):
        assert actions.tap_by_coordinates(406, 105)
    assert actions.tap_by_coordinates(63, 277)
    with step('[Action] tap_share_to_IG_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Instagram')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram')
    with step('[Verify] snapshot: 06_03_01_share_IG.png'):
        actions.capture_for_gt('06_03_01_share_IG.png')
    with step('[Action] back_to_phd_from_sns'):
        actions.activate_app('com.cyberlink.photodirector')
    with step('[Action] tap_share_to_FB_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Post')
    with step('[Verify] snapshot: 06_03_01_share_FB.png'):
        actions.capture_for_gt('06_03_01_share_FB.png')
    assert actions.tap_by_coordinates(42, 41)
    with step('[Verify] snapshot: 06_03_01_back_from_FB.png'):
        actions.capture_for_gt('06_03_01_back_from_FB.png')
    assert actions.tap_by_locator(AppiumBy.NAME, 'Next Edit'), '[06_03_01] Failed to tap next edit'
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnCamera'):
        pass
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.NAME, 'Collage')
    with step('[Action] tap_2photo_cateogry'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn2')
    assert actions.tap_by_coordinates(70, 280)
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.NAME, '_AT')
    assert actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0'), '[06_03_01] Failed to select photo1 for save'
    assert actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1'), '[06_03_01] Failed to select photo2 for save'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    for x in range(20):
        from_pos = (400, 780)
        destination = (40, 780)
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(400, 780, 40, 780)
    assert actions.tap_by_coordinates(395, 810)
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=2):
            actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] close_rate_us_photo'):
        actions.is_element_present(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your Photo Looks Perfect!')
    with step('[Action] tap_back_to_home'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Verify] test_00173 completion"):
        assert True
