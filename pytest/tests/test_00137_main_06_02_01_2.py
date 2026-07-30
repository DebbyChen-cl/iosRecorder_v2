import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00137_main_06_02_01_2')
def test_00137_main_06_02_01_2(actions: DriverActions):
    """Live - animation - save to video"""
    mode = 1
    uuid = ['6fad0a62-00c1-4da6-b30f-7e0e39b6cbb9', '27b69705-4184-4a42-bcef-791f0b093d19', '0bcdb383-8103-429a-8519-7c33c1094b92', '4d2ada24-5d9f-48f8-a72a-8bc511bd3ddb', '187c4981-c6cd-489a-8893-c8edc6b96f87', '2c765203-4f75-4ff2-9c89-38ada5772916', 'bf9b28d6-36ab-4d84-a688-5590e169a8a0', '39da07aa-4e6c-4279-a803-6f0f711691a4', '099396f7-5290-4a78-ac45-e416acfdcb2d', '71eaa8a9-df67-448f-8f4f-d5bd260e90d6', 'fe24ac3c-c44e-4122-8be5-05f090ea824b', '2bb2ff8e-abdb-4cfd-bb28-8f7b583de84a', '32e7fec0-6be9-4996-aa75-76d2ab6bd23d', '39371ac7-d5be-4fdc-a834-681d7fe7dafa', '25d47ea0-0987-414c-80f0-cd59dcef7b94', '0350e503-868f-4aa6-ac1d-808de3f763d5', '01d34f51-66c1-4318-935f-4fb2bbd2426d', 'b18d39ea-c2f6-434c-b490-7dc5019efa11', '94bea896-f44e-460b-8310-11a24dc483e4', '91d52b44-e65c-4393-8e50-ea4a8cd35165', '8162cad0-0c6b-4a1b-b68c-8cebe3384bc7', '49e1ba9e-5781-495f-8a84-22ab4745f332', 'a12f950c-919d-4d16-91e9-29a2f6a155ca', '0808990f-278e-4953-83ff-c8641850e22e', '6841e2e6-374a-4198-b51e-e5945228b3cd', 'adb15093-c487-4746-8555-3a52adde0471', '23f0c64e-8d06-4bff-b91c-7ca1be5053ac', '4902d252-b1ff-4a1f-81de-c884862c24cd', '46535950-32d2-4fd9-a179-5500c621c7da', 'aaf412da-2ec7-4b59-bd25-6b3d05ebc5c7', 'af4ad6c7-3b1d-483a-a74a-207323b29cf2', 'dd685ab4-3f47-4f7e-832e-a3baf03fcdbf', '8a5b87b3-7b3b-49b5-ac0b-9446bfa44d2b', '096b34bd-833c-4304-9d8f-3ea0595969fd', '0a948216-d9e4-44fe-9a81-66944ac8e2ef', '49120ab4-0425-44e2-905f-0c5bab8229a9', '659f3d6e-19c7-4b95-bd65-ff97de4b6c01', 'c0d19d79-b7e2-4270-8a2a-0c1dba08bc63', '69c1a816-353b-4b18-a079-5579c998ebaa', 'f08ad882-e9cc-4798-be8c-a4e62a695ab9', '994d1180-9e4c-4ed7-81ba-1b1421501b9d', '15945559-0dfe-4221-b53e-bf0943a2e959', '4bb39a71-e926-4b1e-ba8e-a38fa3358305', 'bfb872d8-350e-412a-b064-1f14cd8657a4', '9099de37-6d37-4bb1-902f-4b74a5b9c8de', '25e44212-4de8-442d-b3c3-be1e76b32325', '3522618e-c317-4e97-93a8-6e42919c30bf', '95c63d4c-dc33-479a-8a88-4e97b15d2933', '37deb450-337f-4502-8c1e-680f474b4835', '4c682c38-8944-4bc7-93b1-ac74b9e1ae06', 'd5d8d279-1925-454e-8e19-eae6fbb608cd', 'a6944fa2-cc52-4967-9230-127515b4dfb9', '73703130-e93e-4314-b2e6-efedbfc82ca1', '54466fef-72ab-424e-aae0-d9d1f17cd1c1', 'd50f7636-4d28-410e-8899-37c26aac5115', '1bb4c158-0da1-4fa7-bc28-eae024115295', '2d5fe716-e16d-41a8-a268-271cc4c9f3bf', '6eb30c9c-176f-4234-9b64-9f70cd8b511c', 'a06911be-78c4-4bcb-9280-ea8d03686f90']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    element = ['verify_save_page', 'verify_save_page2']
    if not any((actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, value) for value in ('navDescriptionLabel',))):
        assert False, 'verify save video page failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'GIF')):
        assert False, 'tap save to GIF failed'
    element = ['btn_save_playback', 'btn_save_playback2']
    if not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'animationPlayIcon'):
        assert False, 'tap btn_save_playback failed'
    if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'animationPlayIcon')):
        pass
    else:
        assert False, 'verify playback preview failed'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther')
    if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'animationPlayIcon')):
        pass
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for original GIF failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    if actions.is_element_present(AppiumBy.NAME, 'Your GIF was exported'):
        pass
    else:
        assert False, 'save original GIF failed'
    with step('[Verify] snapshot: 06_02_01_save_original_GIF.png'):
        actions.capture_for_gt('06_02_01_save_original_GIF.png')
    with step('[Action] close_export_gif_msg'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Verify] snapshot: 06_02_01_close_export_gif_msg.png'):
        actions.capture_for_gt('06_02_01_close_export_gif_msg.png')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Verify] snapshot: 06_02_01_before_close_rate.png'):
        actions.capture_for_gt('06_02_01_before_close_rate.png')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')):
        assert False, 'tap save_16v9 failed'
    with step('[Verify] snapshot: 06_02_01_before_drag_preview_G.png'):
        actions.capture_for_gt('06_02_01_before_drag_preview_G.png')
    from_pos = (220, 200)
    destination = (220, 240)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(220, 200, 220, 240)
    with step('[Verify] snapshot: 06_02_01_after_drag_preview_G.png'):
        actions.capture_for_gt('06_02_01_after_drag_preview_G.png')
    if (not actions.compare_with_gt('06_02_01_after_drag_preview_G.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'drag preview G failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 16:9 GIF failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    if actions.is_element_present(AppiumBy.NAME, 'Your GIF was exported'):
        pass
    else:
        assert False, 'save 16:9 GIF failed'
    with step('[Action] close_export_gif_msg'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1:1')):
        assert False, 'tap save_1v1 for 1:1 GIF failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 1:1 GIF failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    if actions.is_element_present(AppiumBy.NAME, 'Your GIF was exported'):
        pass
    with step('[Action] close_export_gif_msg'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:4')):
        assert False, 'tap save_3v4 failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 3:4 GIF failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    if actions.is_element_present(AppiumBy.NAME, 'Your GIF was exported'):
        pass
    with step('[Action] close_export_gif_msg'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    with step('[Action] swipe_save_ratio_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, '3:4'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Original'))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')):
        assert False, 'tap save_4v3 failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 4:3 GIF failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    if actions.is_element_present(AppiumBy.NAME, 'Your GIF was exported'):
        pass
    else:
        assert False, 'save 4:3 GIF failed'
    with step('[Action] close_export_gif_msg'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '9:16')):
        assert False, 'tap save_9v16 failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 9:16 GIF failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    if actions.is_element_present(AppiumBy.NAME, 'Your GIF was exported'):
        pass
    else:
        assert False, 'save 9:16 GIF failed'
    with step('[Action] close_export_gif_msg'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    with step('[Action] tap_save_to_video_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Video')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther')
    if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'animationPlayIcon')):
        pass
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'animationPlayIcon'):
        pass
    else:
        assert False, 'verify pause preview failed'
    with step('[Action] swipe_save_ratio_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, '3:4'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Original'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '16:9')
    with step('[Verify] snapshot: 06_02_01_before_drag_preview_v.png'):
        actions.capture_for_gt('06_02_01_before_drag_preview_v.png')
    from_pos = (260, 215)
    destination = (260, 300)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(260, 215, 260, 300)
    with step('[Verify] snapshot: 06_02_01_after_drag_preview_v.png'):
        actions.capture_for_gt('06_02_01_after_drag_preview_v.png')
    if (not actions.compare_with_gt('06_02_01_after_drag_preview_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'drag preview V failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1:1')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 1:1 720p failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save 1:1 720p failed'
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1:1')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1080P')):
        assert False, 'tap save_1080p failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 1:1 1080p failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save 1:1 1080p failed'
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1:1')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '2K')):
        assert False, 'tap save_2k failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 1:1 2k failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save 1:1 2k failed'
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1:1')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4K')):
        assert False, 'tap save_4k failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 1:1 4k failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save 1:1 4k failed'
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Action] swipe_save_ratio_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, '3:4'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Original'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 4:3 720p failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save 4:3 720p failed'
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Action] swipe_save_ratio_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, '3:4'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Original'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1080P')):
        assert False, 'tap save_1080p failed for 4:3 1080p'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 4:3 1080p failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save 4:3 1080p failed'
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Action] swipe_save_ratio_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, '3:4'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Original'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '2K')):
        assert False, 'tap save_2k failed for 4:3 2k'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 4:3 2k failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save 4:3 2k failed'
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Action] swipe_save_ratio_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, '3:4'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Original'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4:3')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4K')):
        assert False, 'tap save_4k failed for 4:3 4k'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 4:3 4k failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save 4:3 4k failed'
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Action] swipe_save_ratio_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, '3:4'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Original'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '9:16')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 9:16 720p failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save 9:16 720p failed'
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Action] swipe_save_ratio_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, '3:4'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Original'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '9:16')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '1080P')):
        assert False, 'tap save_1080p failed for 9:16 1080p'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 9:16 1080p failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save 9:16 1080p failed'
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Action] swipe_save_ratio_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, '3:4'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Original'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '9:16')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '2K')):
        assert False, 'tap save_2k failed for 9:16 2k'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 9:16 2k failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save 9:16 2k failed'
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for ORIGINAL failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save original failed'
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '3:4')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 3:4 failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save 3:4 failed'
    with step('[Action] tap_back_to_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        assert actions.is_element_present(AppiumBy.NAME, 'Feature Tryout')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    for x in range(2):
        from_pos = (380, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Motion')
    from_pos = (60, 100)
    destination = (60, 500)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(60, 100, 60, 500)
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('[Action] swipe_save_ratio_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, '3:4'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Original'))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '9:16')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '4K')):
        assert False, 'tap save_4k failed for 9:16 4k'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')):
        assert False, 'tap save6 for 9:16 4k failed'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Saving...', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Saving...')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your animation looks perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your animation looks perfect!')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save 9:16 4k failed'
    with step('[Action] tap_share_to_IG_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Instagram')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram')
    with step('[Action] back_to_phd_from_sns'):
        actions.activate_app('com.cyberlink.photodirector')
    with step('[Action] tap_share_to_more_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'More')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="shareCell" and @label="U"]')
    with step('[Verify] snapshot: 06_02_01_share_U.png'):
        actions.capture_for_gt('06_02_01_share_U.png')
    if actions.compare_with_gt('06_02_01_share_U.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare share to U failed'
    with step('[Action] Tap'):
        actions.tap_by_coordinates(48, 89)
    with step("[Verify] test_00137 completion"):
        assert True
