# @sft-convert:generated  (自動生成；若手動編輯，請把檔名加進 .scratch/sft-convert/PROTECT.txt
#                          或把本行改成 '# @manual'，即不會被覆蓋)
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00172_ai_face_swap')
def test_00172_ai_face_swap(actions: DriverActions):
    """AI face swap"""
    uuid = ['3fc55fe8-e9d8-4fdd-992b-23b639491ce5', 'd9c57909-2e1a-406c-b222-bf4477cc39ae', '4ba3ed1f-beb5-4c0a-851e-b07da754b8ff', '138927d7-322c-4fd9-8723-102b8c11a976', '182c281e-f7fd-4b51-8c69-e8716910744b', '6d212731-ee32-4433-a7d9-4719d5dd0e5b', '23ed0bf5-f9d9-4515-a597-727dc84c4c6a', '6e4b1575-f295-4687-89e0-83a492d63f26', '619601f0-2fb8-47b8-8e89-d096b6423b21', 'a0592531-e322-41f8-8a30-4018e9b36c24', '8ac0bfea-b463-47d0-8630-05e09008cf64', '567b6e2c-67d9-4f56-8ceb-bbc7c8a18117', '4fe5c4f7-bc6d-438c-bb6f-8b749aaa8e3d', '6e82cfc9-d79c-410a-9052-a3df3af213ea', 'ac5884ba-dba7-43a7-a453-7b0fe3929fb8', '55380dc2-013d-4198-b981-d890c38a68bf', '8f8ba6d0-1ad8-4f58-8465-58101a766019', '13c8e0fd-d612-449d-86a9-17165dda4dec', 'e0f2ce92-31bb-4a5e-b89a-e2c8d61793bc', '3432d59d-1ba7-4164-b23a-3bb4d6254178', '5e9c8d21-1dc0-48e1-a2da-929cadb393e7', 'f21043eb-41f2-4250-8f9f-5fa2a0e22a43', '5083fee1-a37b-42a9-a9a5-fe63e2e3511a', '90e3bb70-1d1f-45a0-a009-60ab6e2d81b1', 'a8de5475-c275-4baf-bf13-4a6f2a19fdac', 'b3baf309-1bc1-4010-b037-fde94bd25af8', '447033eb-9cb8-49e4-8c02-9365eb5f5c64', 'ff88a588-bfdc-4d93-8745-911abd10ccce', '03dd12fe-b756-490f-b568-609a0ba48779']
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos'), '[G02_01_03] Failed to tap ai_photos'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap'), '[G02_01_03] Failed to tap aifaceswap'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext'), '[G02_01_03] Failed to tap try_now'
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, '[G02_01_03] Failed to verify steps page'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue'), '[G02_01_03] Failed to tap continue for steps'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Masculine')
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.NAME, 'Muscular')
    assert actions.tap_by_coordinates(210, 340)
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.NAME, 'titleLabel')
    assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "addSourceImageView"`][1]'), '[G02_01_03] Failed to tap_import_source_btn 1'
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel')
    with step('[Verify] snapshot: G02_01_03_picker.png'):
        actions.capture_for_gt('G02_01_03_picker.png')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue'), '[G02_01_03] Failed to tap continue for picker'
    with step('[Verify] snapshot: G02_01_03_picker2.png'):
        actions.capture_for_gt('G02_01_03_picker2.png')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Import Photos...', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Import Photos...')
    assert actions.is_element_present(AppiumBy.NAME, 'The face in the chosen photo is either too small or blurry. This may result in a poor face swap or unexpected defects in the photo. We recommended using a larger photo where the face is clearer.'), '[G02_01_03] Failed to verify small face dialog'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT'), '[G02_01_03] Failed to select category in picker for no-face'
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Import Photos...', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Import Photos...')
    if actions.is_element_present(AppiumBy.NAME, 'No face detected. A face is required for this feature.'):
        pass
    else:
        assert False, '[G02_01_03] Failed to verify no-face dialog'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK'), '[G02_01_03] Failed to tap OK for no-face'
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Import Photos...', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Import Photos...')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'cancelButton', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'cancelButton')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate'), '[G02_01_03] Failed to tap generate_ai'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnSave'):
        pass
    else:
        assert False, '[G02_01_03] Failed to verify face swap result'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSave')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=2):
            actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] close_rate_us_photo'):
        actions.is_element_present(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your Photo Looks Perfect!')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=2):
            actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] close_rate_us_photo'):
        actions.is_element_present(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your Photo Looks Perfect!')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collage'), '[G02_01_03] Failed to tap tab_collage'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'saveBtn')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=2):
            actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] close_rate_us_photo'):
        actions.is_element_present(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your Photo Looks Perfect!')
    with step('[Action] tap_share_to_FB_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Post')
    assert actions.tap_by_coordinates(42, 41)
    with step('[Action] tap_share_to_IG_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Instagram')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram')
    with step('[Action] back_to_phd_from_sns'):
        actions.activate_app('com.cyberlink.photodirector')
    assert actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'More'), '[G02_01_03] Failed to tap_share_to_more_btn'
    if actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="shareCell" and @label="AirDrop"]'):
        pass
    else:
        assert False, '[G02_01_03] Failed to verify share more'
    assert actions.tap_by_coordinates(63, 277)
    assert actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnHome'), '[G02_01_03] Failed to tap_back_to_home'
    with step('[Verify] snapshot: G02_01_03_after_backing_to_home.png'):
        actions.capture_for_gt('G02_01_03_after_backing_to_home.png')
    with step('[Action] close_IAP'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] close_IAP'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue'), '[G02_01_03] Failed to tap continue for edit room'
    if actions.is_element_present(AppiumBy.NAME, 'Crop to Continue'):
        pass
    else:
        assert False, '[G02_01_03] Failed to verify crop_to_continue'
    assert actions.tap_by_locator(AppiumBy.NAME, 'Crop'), '[G02_01_03] Failed to tap basicedit_crop'
    assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]), '[G02_01_03] Failed to tap_done_btn for crop'
    actions.capture_for_gt('G02_01_03_crop.png')
    if actions.compare_with_gt('G02_01_03_crop.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[G02_01_03] Compare fail for crop'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'ic indi home')
    with step('[Verify] snapshot: G02_01_03_home1.png'):
        actions.capture_for_gt('G02_01_03_home1.png')
    assert actions.try_tap(AppiumBy.NAME, 'Edit Photo'), '[G02_01_03] Failed to tap_editphoto'
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] scroll_and_tap_feature_tab'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap'), '[G02_01_03] Failed to tap aifaceswap second time'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue'), '[G02_01_03] Failed to tap continue second time'
    assert actions.tap_by_locator(AppiumBy.NAME, 'Crop'), '[G02_01_03] Failed to tap basicedit_crop second time'
    assert actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]), '[G02_01_03] Failed to tap_done_btn second time'
    assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "addSourceImageView"`][1]'), '[G02_01_03] Failed to tap import_source_face_swap_1'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Import Photos...', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Import Photos...')
    with step('[Verify] snapshot: G02_01_03_before_generate_again.png'):
        actions.capture_for_gt('G02_01_03_before_generate_again.png')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate'), '[G02_01_03] Failed to tap generate_ai second time'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    with step('[Verify] snapshot: G02_01_03_after_generate_again.png'):
        actions.capture_for_gt('G02_01_03_after_generate_again.png')
    with step('[Action] verify_face_swap_result_page'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnSave')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navBackButton'), '[G02_01_03] Failed to tap back_from_face_swap'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ok')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRemove'), '[G02_01_03] Failed to tap del_src'
    assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "addSourceImageView"`][1]'), '[G02_01_03] Failed to tap import_source_face_swap_1 second time'
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Xsilva')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Import Photos...', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Import Photos...')
    if actions.is_element_present(AppiumBy.NAME, 'Celebrity face detected in the uploaded image and it may violate our terms. Please choose another one.'):
        pass
    else:
        assert False, '[G02_01_03] Failed to verify celebrity face'
    with step("[Verify] test_00172 completion"):
        assert True
