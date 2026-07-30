import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00165_image_to_video')
def test_00165_image_to_video(actions: DriverActions):
    """image to video"""
    uuid = ['b8694a39-12a7-4c1f-8b55-5041bb82e28e', 'f016bc0a-b88a-4b0b-ae23-77226a6fe796', 'ed370c93-466f-419b-b3b7-7360953c67d9', 'ee0941e6-ee5e-45dc-b3e9-0da74ae383ef', 'c111d398-6dc3-49f5-b46b-4e09b5fc0d99', '1721a1ab-a7a1-4941-b4d5-dc2e0d4a72f6', '6d5bea40-3c3b-4ee6-92ce-d192ecc7ca49', '61ff1bfb-4cb0-4306-a91d-ee1588d618f0', 'c8f525ef-119b-4762-8d1b-b5698351a0d3', 'dc8e014f-0db1-476b-9604-c26d4afa58aa', 'bf9be818-2f67-4e8c-8812-5930529dffca', '516cd1d8-b3fe-43a0-8872-eea2ddc85fba', 'bc6cc580-e929-4330-91d4-53eef06f6853', '13710cdf-5ff7-4669-9d9a-5ba20e967393', 'cdc9ce56-9072-4db9-b45a-506f38f3eb90', '7a269c46-62a1-469f-bd32-70d903357ba4', '37d6c70e-38d3-4687-91ac-deffc2e7c49f', 'fb3b9943-1851-476e-a702-42c10347b972', '5d40e0a9-9aa9-4982-b873-0e5a886f7901', '21fcb6e6-eba3-49be-a461-c44c7400d940', '6553bc41-8921-41e0-b2be-3c930bbc83d8', '8192b10f-5f6f-4e58-aacb-762131f5ebd2', 'fd3bfd60-54b6-4e71-949f-dd02917d4215', '48d2639f-786c-4761-ac4b-3c14ef885231', 'f29dd68b-7749-4e6e-8cbd-1d26b1345e16', '96a7b530-d40b-47a6-9b97-e058a598ce07', '92f9ca2b-9c6f-4539-a281-ce403381ce39', 'a126c51e-6f49-4196-b7e0-2a298fa830fe', '7fbdc866-1127-462e-9b76-d1b253d27d21', '849ab778-a310-4c2f-a2ac-d88ed0fdf4e2', 'eed52fff-daca-4c28-81b6-00ab7aac63fb', '8aea5352-71a0-4b36-bbca-93f01de5df26', '8b0ffc66-038d-4b31-8e18-19f34104e89d', 'b00c522f-879f-499d-9315-43a76e96fafd', '3e8689ac-9d56-4040-9e82-aca4f63b772f', '8b321c1b-5dd4-4560-8996-de56c4bffdeb', '55049396-53f4-428f-88d9-56bc1f52199a', '0db992ec-e676-4d29-bca9-bfb81e972922', 'cd7b1bec-e0c2-4137-8c0f-f5b9c8aa08dd', 'db8c9ca2-6c67-46ab-ab85-109646a33bf8', '38572d63-9758-4a6a-9605-92d14208e02c', '05297405-2b15-4176-bbc8-7dbcb908d555', 'c71b572a-2f41-4fae-b232-10f838d07dd4', '78bad5c2-feb2-4e92-8c65-d1ad06dd189d', 'ac00f3c0-073b-453d-9ea4-95fec1fb713c', '5d37f9f9-b4db-44b9-99f7-df941cb48a07', 'ca8b0411-350b-490f-864d-992cf648ce4f', 'eae3bf1f-bbd7-48f6-8ff1-57b566da26e5', 'd68a2115-f3b6-46f5-b31c-ea5dbd1e838d', 'e0a1b05d-3b37-4ae5-aa7d-d1f3d4228d85', '32990581-f3ea-46b5-ad62-abce2c0857a1', '57c5ae49-6327-4f20-a669-da084e1c294a', 'affdd43b-d5d9-4933-abb8-b90283cf68b0', '5bb3df1c-92bd-43db-863e-1ebd93f0642a', '5648b65c-c139-4f7b-b428-33697eccb766', '276f7202-dd89-4d24-bdda-7cde22e296ae']
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Image to Video')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblDesc'):
        pass
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navArtworkButton')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'):
        pass
    else:
        assert False, 'test_G02_02_07 - artwork fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Save')
    with step('[Action] tap_share_to_FB_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Post')
    assert False
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
        assert False, 'test_G02_02_07 - share more fail'
    assert False
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnPlay'):
        pass
    else:
        assert False, 'test_G02_02_07 - full view fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navBackButton')
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Image to Video')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'View All')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Life')
    with step('[Action] scroll_and_tap_vertical'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'High Five')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try with Example')
    with step('[Verify] snapshot: G02_02_07_2duo_ex.png'):
        actions.capture_for_gt('G02_02_07_2duo_ex.png')
    if actions.compare_with_gt('G02_02_07_2duo_ex.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare G02_02_07_2duo_ex.png failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btn refresh n')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step('[Verify] snapshot: G02_02_07_2duo_usr.png'):
        actions.capture_for_gt('G02_02_07_2duo_usr.png')
    if actions.compare_with_gt('G02_02_07_2duo_usr.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare G02_02_07_2duo_usr.png failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, '2 Solo Photos')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Try with Example"`][1]')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try with Example')
    with step('[Verify] snapshot: G02_02_07_2solo_ex.png'):
        actions.capture_for_gt('G02_02_07_2solo_ex.png')
    if actions.compare_with_gt('G02_02_07_2solo_ex.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare G02_02_07_2solo_ex.png failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "replaceImageButton"`][1]')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "replaceImageButton"`][2]')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step('[Verify] snapshot: G02_02_07_2solo_usr.png'):
        actions.capture_for_gt('G02_02_07_2solo_usr.png')
    if actions.compare_with_gt('G02_02_07_2solo_usr.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare G02_02_07_2solo_usr.png failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'imageSettingView')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, '5s')
    with step('[Verify] snapshot: G02_02_07_setting_5s.png'):
        actions.capture_for_gt('G02_02_07_setting_5s.png')
    with step('[Verify] compare: G02_02_07_setting_5s.png'):
        assert actions.compare_with_gt('G02_02_07_setting_5s.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, '10s')
    with step('[Verify] snapshot: G02_02_07_setting_10s.png'):
        actions.capture_for_gt('G02_02_07_setting_10s.png')
    with step('[Verify] compare: G02_02_07_setting_10s.png'):
        assert actions.compare_with_gt('G02_02_07_setting_10s.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pro')
    with step('[Verify] snapshot: G02_02_07_setting_pro.png'):
        actions.capture_for_gt('G02_02_07_setting_pro.png')
    with step('[Verify] compare: G02_02_07_setting_pro.png'):
        assert actions.compare_with_gt('G02_02_07_setting_pro.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Standard')
    with step('[Verify] snapshot: G02_02_07_setting_std.png'):
        actions.capture_for_gt('G02_02_07_setting_std.png')
    with step('[Verify] compare: G02_02_07_setting_std.png'):
        assert actions.compare_with_gt('G02_02_07_setting_std.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
    if actions.is_element_present(AppiumBy.NAME, 'Generate for $3.99'):
        pass
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'):
        pass
    else:
        assert False, 'test_G02_02_07 - artwork fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'View All')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Life')
    from_pos = (200, 700)
    destination = (200, 200)
    with step('[Action] brush_removal'):
        actions.drag_coordinates(200, 700, 200, 200)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Rich')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try with Example')
    with step('[Verify] snapshot: G02_02_07_1_ex.png'):
        actions.capture_for_gt('G02_02_07_1_ex.png')
    if actions.compare_with_gt('G02_02_07_1_ex.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare G02_02_07_1_ex.png failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'btn refresh n')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('[Verify] snapshot: G02_02_07_1_usr.png'):
        actions.capture_for_gt('G02_02_07_1_usr.png')
    if actions.compare_with_gt('G02_02_07_1_usr.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare G02_02_07_1_usr.png failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'imageSettingView')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, '5s')
    with step('[Verify] snapshot: G02_02_07_setting_5s_1.png'):
        actions.capture_for_gt('G02_02_07_setting_5s_1.png')
    if actions.compare_with_gt('G02_02_07_setting_5s_1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare G02_02_07_setting_5s_1.png failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, '10s')
    with step('[Verify] snapshot: G02_02_07_setting_10s_1.png'):
        actions.capture_for_gt('G02_02_07_setting_10s_1.png')
    if actions.compare_with_gt('G02_02_07_setting_10s_1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare G02_02_07_setting_10s_1.png failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pro')
    with step('[Verify] snapshot: G02_02_07_setting_pro_1.png'):
        actions.capture_for_gt('G02_02_07_setting_pro_1.png')
    if actions.compare_with_gt('G02_02_07_setting_pro_1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare G02_02_07_setting_pro_1.png failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Standard')
    with step('[Verify] snapshot: G02_02_07_setting_std_1.png'):
        actions.capture_for_gt('G02_02_07_setting_std_1.png')
    if actions.compare_with_gt('G02_02_07_setting_std_1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare G02_02_07_setting_std_1.png failed'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'):
        pass
    else:
        assert False, 'test_G02_02_07 - artwork fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'View All')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Female')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'All')
    with step("[Verify] test_00165 completion"):
        assert True
