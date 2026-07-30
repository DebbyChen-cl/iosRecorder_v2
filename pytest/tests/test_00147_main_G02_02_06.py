import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00147_main_G02_02_06')
def test_00147_main_G02_02_06(actions: DriverActions):
    """artistic avatar ( s ) ( AI art)"""
    mode = 1
    uuid = ['5f68594a-05e5-4c8f-a60b-0d5de341547e', '83414b31-2d39-4ea5-b3fe-ef6e59f5a615', '772c50dd-5f2f-407c-ae09-1e9478555c4d', '9a4d3bf2-9121-4721-b57c-637ae557cab9', 'd7fc0921-f44d-4360-a036-c059ae64f7df', 'e854f293-eb99-447d-b39b-94f7f03bf495', 'c00f253b-2f62-428d-8c64-ea066a003a31', 'ae2bbe33-0784-48e6-9e6c-fcb4ff4a6c28', 'babab00c-cd63-4329-92c0-72a128bade16', '47c6538e-16ca-4371-a863-08578980d2ba', '825d36be-b729-4120-8802-a602d6d40f28', 'b14030c1-2308-4b51-9b99-c9cc2b0de37f', '238ffc47-9c83-4b99-a534-97697c5f933a', '414f237d-28fc-4c25-89b5-bf5a1fea3819', '92050f51-bd2a-41a5-ac22-9fe789be4dc3', '25846a29-774c-4a39-b1b8-fe9ce0ee78a3', 'ebe42649-4e27-44ad-b0e2-188fca5d3144', 'ce0cb7ba-6830-41c1-9e58-0ca051beb944', 'c5f8186e-f599-4d23-a715-805bbc467223', '407984c0-3aaa-497a-afcb-a2c455b0be1d', '210016f3-3c81-4a1e-93cb-92edfb79168d', '8795809a-8f94-447b-824c-107e3b94a708', 'ff35d37e-5364-46f1-bec1-4c556e8b239a', '5e3d4e2d-8d5b-4248-88ba-c97afa97ec8c', '23482917-fe69-4fd1-92bd-24e48e90c96c', 'b6711a41-e8b7-4be2-966e-e5a30743cbcd', '27fb01ef-c97b-4b36-ba4f-a766409df61f', 'd2cdc78b-65c9-494d-ae8c-9fc535918a2a', '6b68946f-2d00-4c7a-bbc0-44522a58e810', '6f3dd8bb-68aa-487a-8fff-73413c3daa6f', 'b569f313-728c-41c9-b652-18f6dc91a3bf', 'd2622e64-7fc9-4a57-ba61-1139888a016e', 'fae8f3cb-be0d-41a7-a5a0-b53fe1e2936c', 'b3ab5978-9d17-4b65-934a-ad8d0aa4a1a7']
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')):
        pass
    else:
        with step('[Action] tap_dont_show_again'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('[Action] select_avatar_style'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Clean')
    with step('[Verify] snapshot: G02_02_06_female_style.png'):
        actions.capture_for_gt('G02_02_06_female_style.png')
    if actions.compare_with_gt('G02_02_06_female_style.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Female style comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Male')
    with step('[Action] select_avatar_style'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Figure')
    with step('[Verify] snapshot: G02_02_06_male_style.png'):
        actions.capture_for_gt('G02_02_06_male_style.png')
    if actions.compare_with_gt('G02_02_06_male_style.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Male style comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importLabel')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'):
        pass
    else:
        assert False, 'Outfit intro verification failed (uuid[3])'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Verify] snapshot: G02_02_06_import.png'):
        actions.capture_for_gt('G02_02_06_import.png')
    if actions.compare_with_gt('G02_02_06_import.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Import page comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importLabel')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'):
        pass
    else:
        assert False, 'Outfit intro verification failed (uuid[5])'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Verify] snapshot: G02_02_06_import2.png'):
        actions.capture_for_gt('G02_02_06_import2.png')
    if actions.compare_with_gt('G02_02_06_import2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Import2 page comparison failed'
    with step('[Verify] snapshot: G02_02_06_before_generating.png'):
        actions.capture_for_gt('G02_02_06_before_generating.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Verify] snapshot: G02_02_06_generating1.png'):
        actions.capture_for_gt('G02_02_06_generating1.png')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
    with step('[Action] wait_process'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'waitIndicator')
        assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'waitIndicator')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnSave'):
        pass
    else:
        assert False, 'Avatar result verification failed (uuid[7])'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSave')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.ArtisticAvatarResultViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeButton[1]')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ok')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Male'):
        pass
    else:
        assert False, 'Back to setting verification failed (uuid[17])'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Verify] snapshot: G02_02_06_generating2.png'):
        actions.capture_for_gt('G02_02_06_generating2.png')
    if actions.wait_for_invisible(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]', timeout=15):
        pass
    else:
        assert False, 'Wait process failed (second generation for uuid[17])'
    with step('[Verify] snapshot: G02_02_06_avatar2.png'):
        avatar2_path = actions.capture_for_gt('G02_02_06_avatar2.png')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Verify] snapshot: G02_02_06_avatar1.png'):
        avatar1_path = actions.capture_for_gt('G02_02_06_avatar1.png')
    with step('[Verify] compare: G02_02_06_avatar2.png vs G02_02_06_avatar1.png'):
        assert actions.compare_preview(
            'G02_02_06_avatar_selection',
            before_path=avatar2_path,
            after_path=avatar1_path,
            expected_result='different',
        )[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnContinueEdit')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] tap_portrait1_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step('[Verify] snapshot: G02_02_06_bring_source.png'):
        actions.capture_for_gt('G02_02_06_bring_source.png')
    if actions.compare_with_gt('G02_02_06_bring_source.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Bring source page comparison failed'
    with step('[Action] select_avatar_style'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Clean')
    with step('[Verify] snapshot: G02_02_06_female_stylen.png'):
        actions.capture_for_gt('G02_02_06_female_stylen.png')
    if actions.compare_with_gt('G02_02_06_female_stylen.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Female stylen comparison failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importLabel')
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Verify] snapshot: G02_02_06_import_e.png'):
        actions.capture_for_gt('G02_02_06_import_e.png')
    with step('[Verify] compare: G02_02_06_import_e.png'):
        assert actions.compare_with_gt('G02_02_06_import_e.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] wait_process'):
        assert actions.is_element_present(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]')
        assert actions.wait_for_invisible(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnSave'):
        pass
    else:
        assert False, 'Avatar result verification failed (uuid[27])'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate More')
    with step('[Action] wait_process'):
        assert actions.is_element_present(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]')
        assert actions.wait_for_invisible(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSave')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.ArtisticAvatarResultViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeButton[1]')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    if actions.wait_for_invisible(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]', timeout=15):
        pass
    else:
        assert False, 'Wait process failed (fourth generation after uuid[33])'
    with step('[Verify] snapshot: G02_02_06_avatare2.png'):
        avatare2_path = actions.capture_for_gt('G02_02_06_avatare2.png')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Verify] snapshot: G02_02_06_avatare1.png'):
        avatare1_path = actions.capture_for_gt('G02_02_06_avatare1.png')
    with step('[Verify] compare: G02_02_06_avatare2.png vs G02_02_06_avatare1.png'):
        assert actions.compare_preview(
            'G02_02_06_avatare_selection',
            before_path=avatare2_path,
            after_path=avatare1_path,
            expected_result='different',
        )[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnContinueEdit')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step('[Action] tap_portrait1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('[Action] select_avatar_style'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Clean')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    if actions.wait_for_invisible(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]', timeout=15):
        pass
    else:
        assert False, 'Wait process fail (home section)'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] close_continue_edit'):
        actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importLabel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.NAME, 'Avatar')
    with step('[Action] select_avatar_style'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Clean')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    if actions.wait_for_invisible(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][-1]', timeout=15):
        pass
    else:
        assert False, 'Wait process fail (final section)'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Mine'):
        pass
    else:
        assert False, 'Back to main verification failed (uuid[19])'
    with step("[Verify] test_00147 completion"):
        assert True
