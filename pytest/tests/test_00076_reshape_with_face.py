import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00076_reshape_with_face')
def test_00076_reshape_with_face(actions: DriverActions):
    """reshape, have face"""
    mode = 1
    uuid = ['d24db9da-aff4-4a20-b001-351b365b8444', '1d669574-1801-4e0f-90c5-b8bc49512a08', '29464bc4-16f9-4e44-9998-31e49b3b614e', 'd698340e-b06a-4283-a635-5249298b7630', 'cd4d4b67-0b6a-44f6-b6ec-fb0bdb8f3550', '6c8213ae-46bb-4d9d-b027-fe3cd2822d59', '35cfabcd-c15a-4ca1-a788-407ef7756cfa', '791d3eb4-bff5-4ec9-88de-1bae972dffc4', 'fd875a3f-feee-4f47-a3ef-3a7e732a0148', 'f4be48ef-d1d1-493c-a150-9f8fe9b79af1', '9ec4cc27-4d80-49eb-98fd-d6ddd5711ad0', '3f9fb067-1d47-4c67-8c6d-2ed7f3ecdcd0', '584eb78c-81e5-4a58-be8d-61c2e3a2d29f', '712d18a1-17c4-4690-b844-5de815363236', '08e7dfc4-5c51-4fc7-94d7-e55f97431683', '8d8aed96-2555-4c7f-bfa7-342e892bd2f5', '8f8098f7-7fd4-4872-86ee-cc5d964dcf69', '3ee55de9-6936-49a8-a259-fa1ee21cd39d', '00c455c4-f1ab-458b-b0bd-544868c49000', '9ba942cf-0366-4ac9-afd6-e983c3662072', 'b9b63a8f-4180-405f-a898-0647153a3816', '138d933b-09e2-48dd-889b-943e11d8eb2c', '385b4b1a-58c7-4967-ad5b-dc6d11c83df2', '9d2e8ed1-5607-43a6-9a28-c7cf7b3dc214', '4570be88-09ac-4e24-972f-291bde861ea3', 'd4b0b7df-aff5-4acf-852e-83be98a9b96c', '95733a12-4bbd-4b3f-b548-39b67374a03f', 'cecd200d-f906-4c4e-93c9-4ee9c0a87420', 'e6cbbb3f-326b-426e-839e-9fd56ecb10b5', 'a60c98ea-d8d0-4d22-a5e2-0a30267d7fd1', 'a87917ec-f644-44db-91df-abd3dbe8f4a4', 'b054f934-08d4-428e-bf0d-b89802032313', '2d76634f-a753-41e3-b62f-7e2458b30f6e', '9715f576-3d72-4368-a8b6-ad1e62fd3160', '9fbc5146-070a-43f3-afc3-906a592253b1', '41076f66-9e40-412d-a5af-3d37bf60bfa6', 'cdce1354-9dd3-41e3-8291-978205b3de54', '4f8550e2-2c94-487f-a713-5f12192a415f', 'c7efddc8-199f-4002-b748-2bc207941fb7', 'aa190f45-4061-4ac8-975f-50896aa722ab', 'dba052fa-63db-4296-8f42-9f94b58e45d1', 'deb1b943-9e28-4e40-a796-13be0cf114ae', '994f9866-32c4-475d-9f11-edf218f9a6cc', '089ff58c-70c8-41af-a00f-0545c566e78f', '35bad196-8598-4beb-9550-acdabeec3250', 'd5ef9e2b-e6a8-4fe5-b26e-ec6cd11d95f5', 'd1dbadf0-d76e-4a98-906f-3c4fd12670d7', 'a7a081ce-6e2d-407b-9dec-300e2b931ef1', '67a60666-d2f8-4a5c-abbe-fdf9e49b15d0', '09da6b01-1ca0-4fd1-9c18-99e4f943b618', '674e13cf-77ff-405e-a1e9-73017d584a78', 'ce8a52cc-500d-4435-82e1-3d0be46b53c4', 'd3213d2d-96fe-4e06-a364-3a735b741d48', 'fe10965d-565d-4b4d-aba9-4890e8d72295', '80ba89a9-6033-47cb-ba84-2e6c757ca623', '5cf43f14-11ee-4dbc-b159-dd4b4cf1c5a7', 'b4f67988-7d66-41cd-8e29-ece92ccfa3e0', 'c1e044f9-c016-4921-a46c-7e4dcebb571f', '4daaa072-3bef-411d-94fa-5dcd0a02cb9f', 'd9e94055-5bbf-4bdb-9153-c0a5888c491f', '3422f579-ccda-4586-8ba9-6f0c32121596', '5ceb6eb4-4317-45be-b804-95db5c74dbd5', 'be11559f-2029-4e8f-bcb4-3f806c41aa08', '7ad8b334-1b69-4f32-925f-0491e4fba64e', 'ead1aa5d-c6ba-405d-baba-eafad4d019cb', '79169247-050d-4da8-ad26-889e0e2b2cd7', 'ce933e5e-3ddf-4280-9989-271cdf294a9d', '8af70303-6040-42f8-ad4e-94167be32ff0', '8f71dcee-104e-4f5e-9a9d-c102ee231787', '16fd9acc-1ef3-4cc9-a93c-d57904364714', '029a73b1-5cb4-495a-80dd-fae4d520c0ed', 'b56e4a9b-212f-4ebb-a1cf-954d3b7cd614', 'bc05fa24-69f6-4323-ae6a-f63f00afedde', '082c094b-7e4d-47e9-a088-614670c5a505', '10965225-c090-432a-82c4-b0ba8c6c6323', '75fb04c3-b70c-48d6-ab5c-33db1426930c', 'fe152bb2-1468-4b84-85d1-9798cfcdfd04', 'ec10665e-3392-4495-b8e5-2b566f0ee602', 'f1f6ea77-d52b-4059-820b-8bf61cbaa0af', '253731b8-279b-472c-8213-228b2647ba4e', 'abee0623-dd06-4273-9bc2-62511288529c', '50d3e847-aa4b-426a-9d9b-f317cc7184ee', 'ba3da064-82f9-48a3-8e2f-90fb837b89d2', 'c4c0d142-5a71-431a-a7df-657b939274e8', 'b27a29e5-436e-4c88-ad3b-09f65296cab7', '7e6bbc85-472a-4bfc-a018-16ad355305dd', '62d73f6a-feda-4b30-8a5d-2648864c5321', '48793cdf-b2bc-4b83-b118-95aeb42eb644', '2ebc34be-bca4-4250-8a2e-67b820e2670a', '7c9d6f37-26fd-4a1f-8af2-a37264640912', '463183a8-0e22-45b2-aa0e-acb06a1ffef0', 'ffe9ca49-a5bc-472d-847a-db975ada4390', '431591fd-cfaf-46c6-b273-bb1e4d57f021', '2ddecc77-d0db-4c50-b7c7-80885ebe4fed', '96a96dd7-7881-4f61-9640-2084353e786f', '1bc50c6e-7086-46ca-ae4d-1a3d09d6fdb4', 'e47481cd-50be-4602-b769-ece9e3c35b07', '6f18ca58-cecc-44c6-bfa9-58f7a808bf41', 'd1a1c143-bf1d-4537-89db-3e59ce53bc7b', '44e0a79f-67a1-40f5-b8dc-e0ff6c706c8d', '16416111-d70f-4f55-8214-cf21f944f518', 'f6df4631-316b-4bea-a96a-ecc5da14f9ff', 'd38ca13b-e78d-40f9-8959-6f246249c615', '0885f000-21e0-4d91-aec9-6c427ee318f9', '301526a7-4f8d-48ee-8edb-3b95348fbc47', '27665f3a-4a2c-47ac-b861-3048a5200b7e', '6919c3a0-8c66-427f-82a9-e6408bad0d04', '66deb580-bbb4-4aa1-8942-c49b61bbb965', '05ad929f-16ad-44c7-a2cb-08ba42086825', '9159c5cf-0007-4f88-ae0b-2dc129153938', '9d831070-1985-4e98-95e1-e1a28ba6df48', 'aa78ce1b-6efc-496c-8bf8-1278b26b7fac', '8bf8b68e-cd43-4ccc-9dfb-570b5dc71a74', 'b7ae4360-d8a9-43b1-918f-642ed86c2a0d', 'fe52366d-25ce-4373-b83f-167bda3f19a9', 'bdafd117-9550-43b3-a14c-2656c353fd9f', 'cc3d48ac-ce10-4091-b144-f68d1ca64853', '0adf7dea-d294-4444-b223-08b4a097fe2e', 'e706388e-c3eb-4960-9be3-86d4fd695fa5', 'a3af1583-e961-489e-a97c-bcb0a513f71b', 'e7ebe7da-0669-4173-a331-fd0d3b98b504', '58096c50-bc76-452e-a1a4-056b1b0b8208', '1c904105-8a48-4500-b9ba-75ba847b9e6b', 'ad7093b1-462c-4c3d-9f5f-9ac14e9234e3', '27b22363-8040-46b6-914f-ba570aba6167', '559a1f03-78fa-4d6e-93e8-43f04ca00329', '238b8e52-0f3b-4aca-b4b2-7fe6d2f41014', '89e43000-47c1-4d73-981b-5da928cae5ed', '488ff990-0406-48cd-b6ab-4158cec713e4', '0aa24f93-b5b5-45a7-b86e-9c06ea9ba999', '4f8e3dcb-2d8d-4e27-a661-8401e8bc6ccd', '5d1c80a0-8f3b-4a72-8cbf-e35f4ecd406a', 'c5ac8b3d-8566-4c52-b1ca-2d9fb128f3ff', 'cee56151-0c16-4a80-89e6-f2e0b63ebd92', '9487b291-d9fb-4126-9b9f-b3df3cf1861f', 'd0efef0e-3dbd-4aa0-93d8-82c14570dae7', '37dc15c4-cab6-4f7b-9bf0-f058783d6baf', '1fd1b624-c481-4636-9a08-c2edacf0d592', '5986133c-98b4-4f1d-b77d-6d084f491253', '91caff3f-d44a-400e-aa2f-5218c2e7dda8', 'f3ffd93e-c105-4c6f-b472-68e8b8bf0a1b', 'cebdb35d-42ec-479e-9655-d39f5e7df1dd', '70616999-08cd-427a-9aac-bdc6ffee18a0', '7468e721-0b07-467f-87dc-4189c306a68a', '0d70aa09-bd50-4002-b5c2-2ed690bb768b', 'e6134152-4d9f-495c-b2e2-4177d0004d1b', 'c09fe29d-766b-4fe4-a2d6-8f9bb5722c8e', 'a80b6154-2108-4f61-8f01-022d3ffcbd8c', '32b6cd95-4b5c-4c8e-aa91-5cb08ea626c4', '259cccd0-6d3b-4357-8a1c-49b6f2c4a4d8', 'f3ac3574-2ee4-4fec-ac6c-ed95ca1b553b', '465e6a20-fb31-4b0e-85f8-990d937c224a', 'e5124ea4-2aec-476f-a5b0-d541a3befd0c', 'a94dfd12-1b73-467d-a404-5eb2247dd7d9', '2aaf042c-5571-4e30-b729-58510cf2c0ca', '3eb040d5-a642-4cd7-9870-6643a2a4d73e', '4cdac094-19c1-45e8-a3bf-d1a0e32852ed', '6c552a2e-7a92-4113-84c5-6699e5565bdf', 'cb5048bd-fd75-4862-9b99-df44d8b84db7', 'e769547f-a776-4236-9230-5222591b11fd', '8f90b322-2e9b-402f-b968-14de5c411182', 'edf8a7f6-7818-4335-a5bb-bb5b39a015a3', 'e477b036-7360-41ba-a503-cd8cc70f4d05', '543ebe18-36a4-41a0-b1ce-43d25e820a82', 'b8988d43-734f-4381-b80a-8bdf9a88b122', '6a991c6d-8c00-4b97-8e53-27644831b05a']
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
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Verify] snapshot: 05_07_10_before_reshape.png'):
        actions.capture_for_gt('05_07_10_before_reshape.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Reshape')
    with step('Preset - original (default)'):
        with step('[Verify] snapshot: 05_07_12_shape_og.png'):
            actions.capture_for_gt('05_07_12_shape_og.png')
        if actions.compare_with_gt('05_07_12_shape_og.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for shape og fail'
    with step('Preset - natural'):
        with step('[Action] select_reshape_preset'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Natural')
        with step('[Verify] snapshot: 05_07_12_shape_natural.png'):
            actions.capture_for_gt('05_07_12_shape_natural.png')
        if actions.compare_with_gt('05_07_12_shape_natural.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for shape natural fail'
    with step('Preset - oval'):
        with step('[Action] select_reshape_preset'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Oval')
        with step('[Verify] snapshot: 05_07_12_shape_oval.png'):
            actions.capture_for_gt('05_07_12_shape_oval.png')
        if actions.compare_with_gt('05_07_12_shape_oval.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for shape oval fail'
    with step('Preset - v-line'):
        with step('[Action] select_reshape_preset'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'V-line')
        with step('[Verify] snapshot: 05_07_12_shape_vline.png'):
            actions.capture_for_gt('05_07_12_shape_vline.png')
        if actions.compare_with_gt('05_07_12_shape_vline.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
    with step('Preset - baby'):
        with step('[Action] select_reshape_preset'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Baby')
        with step('[Verify] snapshot: 05_07_12_shape_baby.png'):
            actions.capture_for_gt('05_07_12_shape_baby.png')
        if actions.compare_with_gt('05_07_12_shape_baby.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for shape baby fail'
    with step('[Action] select_reshape_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Original')
    with step('[Action] tap_face'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Face')
    with step('Face - width'):
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Face width default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_face_width_min.png'):
            actions.capture_for_gt('05_07_12_face_width_min.png')
        if actions.compare_with_gt('05_07_12_face_width_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for face width min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_face_width_max.png'):
            actions.capture_for_gt('05_07_12_face_width_max.png')
        if actions.compare_with_gt('05_07_12_face_width_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for face width max fail'
    with step('Face - jaw (both)'):
        with step('[Action] tap_jaw_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Jaw')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Face jaw default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_face_jaw_min.png'):
            actions.capture_for_gt('05_07_12_face_jaw_min.png')
        if actions.compare_with_gt('05_07_12_face_jaw_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for face jaw min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_face_jaw_max.png'):
            actions.capture_for_gt('05_07_12_face_jaw_max.png')
        if actions.compare_with_gt('05_07_12_face_jaw_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for face jaw max fail'
    with step('Face - jaw (left)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Face jaw left default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_jaw_left_min.png'):
            actions.capture_for_gt('05_07_12_jaw_left_min.png', crop_rect=(0, 60, 276, 429))
        if actions.compare_with_gt('05_07_12_jaw_left_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for jaw left min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_jaw_left_max.png'):
            actions.capture_for_gt('05_07_12_jaw_left_max.png', crop_rect=(0, 60, 276, 429))
        if actions.compare_with_gt('05_07_12_jaw_left_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for jaw left max fail'
    with step('Face - jaw (right)'):
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        with step('[Action] tap_right_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Right')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Face jaw right default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_jaw_right_min.png'):
            actions.capture_for_gt('05_07_12_jaw_right_min.png', crop_rect=(0, 60, 276, 429))
        if actions.compare_with_gt('05_07_12_jaw_right_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for jaw right min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_jaw_right_max.png'):
            actions.capture_for_gt('05_07_12_jaw_right_max.png')
        if actions.compare_with_gt('05_07_12_jaw_right_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for jaw right max fail'
    with step('Face - forehead'):
        with step('[Action] tap_forehead_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Forehead')
        with step('[Verify] snapshot: 05_07_12_tap_forehead.png'):
            actions.capture_for_gt('05_07_12_tap_forehead.png')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Face forehead default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_face_forehead_min.png'):
            actions.capture_for_gt('05_07_12_face_forehead_min.png')
        if actions.compare_with_gt('05_07_12_face_forehead_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for face forehead min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_face_forehead_max.png'):
            actions.capture_for_gt('05_07_12_face_forehead_max.png')
        if actions.compare_with_gt('05_07_12_face_forehead_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for face forehead max fail'
    with step('Face - chin'):
        with step('[Action] tap_chin_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Chin')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Face chin default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_face_chin_min.png'):
            actions.capture_for_gt('05_07_12_face_chin_min.png')
        if actions.compare_with_gt('05_07_12_face_chin_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for face chin min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_face_chin_max.png'):
            actions.capture_for_gt('05_07_12_face_chin_max.png')
        if actions.compare_with_gt('05_07_12_face_chin_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for face chin max fail'
    with step('Eyes - size (both)'):
        with step('[Action] tap_size_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushSizeSliderView')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eyes size both default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_size_both_min.png'):
            actions.capture_for_gt('05_07_12_eye_size_both_min.png')
        if actions.compare_with_gt('05_07_12_eye_size_both_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye size both min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_size_both_max.png'):
            actions.capture_for_gt('05_07_12_eye_size_both_max.png')
        if actions.compare_with_gt('05_07_12_eye_size_both_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye size both max fail'
    with step('Eyes - size (left)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eyes size left default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 5_07_12_eye_size_left_min.png'):
            actions.capture_for_gt('5_07_12_eye_size_left_min.png')
        if actions.compare_with_gt('05_07_12_eye_size_left_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye size left min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_size_left_max.png'):
            actions.capture_for_gt('05_07_12_eye_size_left_max.png')
        if actions.compare_with_gt('05_07_12_eye_size_left_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye size left max fail'
    with step('Eyes - size (right)'):
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        with step('[Action] tap_right_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Right')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eyes size right default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_size_right_min.png'):
            actions.capture_for_gt('05_07_12_eye_size_right_min.png')
        if actions.compare_with_gt('05_07_12_eye_size_right_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye size right min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_size_right_max.png'):
            actions.capture_for_gt('05_07_12_eye_size_right_max.png')
        if actions.compare_with_gt('05_07_12_eye_size_right_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye size right max fail'
    with step('Eyes - height (both)'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Height')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye height both default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_height_both_min.png'):
            actions.capture_for_gt('05_07_12_eye_height_both_min.png')
        if actions.compare_with_gt('05_07_12_eye_height_both_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye height both min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_height_both_max.png'):
            actions.capture_for_gt('05_07_12_eye_height_both_max.png')
        if actions.compare_with_gt('05_07_12_eye_height_both_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye height both max fail'
    with step('Eyes - height (left)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye height left default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_height_left_min.png'):
            actions.capture_for_gt('05_07_12_eye_height_left_min.png')
        if actions.compare_with_gt('05_07_12_eye_height_left_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye height left min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_height_left_max.png'):
            actions.capture_for_gt('05_07_12_eye_height_left_max.png')
        if actions.compare_with_gt('05_07_12_eye_height_left_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye height left max fail'
    with step('Eyes - height (right)'):
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        with step('[Action] tap_right_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Right')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye height right default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_height_right_min.png'):
            actions.capture_for_gt('05_07_12_eye_height_right_min.png')
        if actions.compare_with_gt('05_07_12_eye_height_right_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye height right min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_height_right_max.png'):
            actions.capture_for_gt('05_07_12_eye_height_right_max.png')
        if actions.compare_with_gt('05_07_12_eye_height_right_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye height right max fail'
    with step('Eyes - lift (both)'):
        with step('[Action] tap_lift_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lift')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye lift both default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_lift_both_min.png'):
            actions.capture_for_gt('05_07_12_eye_lift_both_min.png')
        if actions.compare_with_gt('05_07_12_eye_lift_both_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye lift both min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_lift_both_max.png'):
            actions.capture_for_gt('05_07_12_eye_lift_both_max.png')
        if actions.compare_with_gt('05_07_12_eye_lift_both_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye lift both max fail'
    with step('Eyes - lift (left)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye lift left default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_lift_left_min.png'):
            actions.capture_for_gt('05_07_12_eye_lift_left_min.png')
        if actions.compare_with_gt('05_07_12_eye_lift_left_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye lift left min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_lift_left_max.png'):
            actions.capture_for_gt('05_07_12_eye_lift_left_max.png')
        if actions.compare_with_gt('05_07_12_eye_lift_left_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye lift left max fail'
    with step('Eyes - lift (right)'):
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        with step('[Action] tap_right_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Right')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye lift right default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_lift_right_min.png'):
            actions.capture_for_gt('05_07_12_eye_lift_right_min.png')
        if actions.compare_with_gt('05_07_12_eye_lift_right_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye lift right min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_lift_right_max.png'):
            actions.capture_for_gt('05_07_12_eye_lift_right_max.png')
        if actions.compare_with_gt('05_07_12_eye_lift_right_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye lift right max fail'
    with step('Eyes - angle (both)'):
        with step('[Action] tap_angle_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Angle')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye angle both default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_angle_both_min.png'):
            actions.capture_for_gt('05_07_12_eye_angle_both_min.png')
        if actions.compare_with_gt('05_07_12_eye_angle_both_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye angle both min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_angle_both_max.png'):
            actions.capture_for_gt('05_07_12_eye_angle_both_max.png')
        if actions.compare_with_gt('05_07_12_eye_angle_both_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye angle both max fail'
    with step('Eyes - angle (left)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_angle_left_min.png'):
            actions.capture_for_gt('05_07_12_eye_angle_left_min.png')
        if actions.compare_with_gt('05_07_12_eye_angle_left_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye angle left min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_angle_left_max.png'):
            actions.capture_for_gt('05_07_12_eye_angle_left_max.png')
        if actions.compare_with_gt('05_07_12_eye_angle_left_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye angle left max fail'
    with step('Eyes - angle (right)'):
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        with step('[Action] tap_right_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Right')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye angle right default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_angle_right_min.png'):
            actions.capture_for_gt('05_07_12_eye_angle_right_min.png')
        if actions.compare_with_gt('05_07_12_eye_angle_right_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye angle right min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_angle_right_max.png'):
            actions.capture_for_gt('05_07_12_eye_angle_right_max.png')
        if actions.compare_with_gt('05_07_12_eye_angle_right_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye angle right max fail'
    with step('Eyes - width (both)'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Width')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye width both default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_width_both_min.png'):
            actions.capture_for_gt('05_07_12_eye_width_both_min.png')
        if actions.compare_with_gt('05_07_12_eye_width_both_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye width both min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_width_both_max.png'):
            actions.capture_for_gt('05_07_12_eye_width_both_max.png')
        if actions.compare_with_gt('05_07_12_eye_width_both_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye width both max fail'
    with step('Eyes - width (left)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye width left default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_width_left_min.png'):
            actions.capture_for_gt('05_07_12_eye_width_left_min.png')
        if actions.compare_with_gt('05_07_12_eye_width_left_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye width left min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_width_left_max.png'):
            actions.capture_for_gt('05_07_12_eye_width_left_max.png')
        if actions.compare_with_gt('05_07_12_eye_width_left_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye width left max fail'
    with step('Eyes - width (right)'):
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        with step('[Action] tap_right_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Right')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye width right default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_width_right_min.png'):
            actions.capture_for_gt('05_07_12_eye_width_right_min.png')
        if actions.compare_with_gt('05_07_12_eye_width_right_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye width right min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_width_right_max.png'):
            actions.capture_for_gt('05_07_12_eye_width_right_max.png')
        if actions.compare_with_gt('05_07_12_eye_width_right_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye width right max fail'
    with step('Eyes - distance'):
        with step('[Action] tap_distance_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Distance')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye distance both default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_distance_both_min.png'):
            actions.capture_for_gt('05_07_12_eye_distance_both_min.png')
        if actions.compare_with_gt('05_07_12_eye_distance_both_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye distance both min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_distance_both_max.png'):
            actions.capture_for_gt('05_07_12_eye_distance_both_max.png')
        if actions.compare_with_gt('05_07_12_eye_distance_both_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye distance both max fail'
    with step('Eyes - distance (left)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye distance left default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_distance_left_min.png'):
            actions.capture_for_gt('05_07_12_eye_distance_left_min.png')
        if actions.compare_with_gt('05_07_12_eye_distance_left_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye distance left min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_distance_left_max.png'):
            actions.capture_for_gt('05_07_12_eye_distance_left_max.png')
        if actions.compare_with_gt('05_07_12_eye_distance_left_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye distance left max fail'
    with step('Eyes - distance (right)'):
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        with step('[Action] tap_right_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Right')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye distance right default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_distance_right_min.png'):
            actions.capture_for_gt('05_07_12_eye_distance_right_min.png')
        if actions.compare_with_gt('05_07_12_eye_distance_right_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye distance right min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_distance_right_max.png'):
            actions.capture_for_gt('05_07_12_eye_distance_right_max.png')
        if actions.compare_with_gt('05_07_12_eye_distance_right_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye distance right max fail'
    with step('Eyes - pupil (both)'):
        with step('[Action] tap_pupil_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pupil')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye pupil both default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_pupil_both_min.png'):
            actions.capture_for_gt('05_07_12_eye_pupil_both_min.png')
        if actions.compare_with_gt('05_07_12_eye_pupil_both_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye pupil both min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_pupil_both_max.png'):
            actions.capture_for_gt('05_07_12_eye_pupil_both_max.png')
        if actions.compare_with_gt('05_07_12_eye_pupil_both_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye pupil both max fail'
    with step('Eyes - pupil (left)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye pupil left default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_pupil_left_min.png'):
            actions.capture_for_gt('05_07_12_eye_pupil_left_min.png')
        if actions.compare_with_gt('05_07_12_eye_pupil_left_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye pupil left min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_pupil_left_max.png'):
            actions.capture_for_gt('05_07_12_eye_pupil_left_max.png')
        if actions.compare_with_gt('05_07_12_eye_pupil_left_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye pupil left max fail'
    with step('Eyes - pupil (right)'):
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        with step('[Action] tap_right_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Right')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eye pupil right default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eye_pupil_right_min.png'):
            actions.capture_for_gt('05_07_12_eye_pupil_right_min.png')
        if actions.compare_with_gt('05_07_12_eye_pupil_right_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye pupil right min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eye_pupil_right_max.png'):
            actions.capture_for_gt('05_07_12_eye_pupil_right_max.png')
        if actions.compare_with_gt('05_07_12_eye_pupil_right_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eye pupil right max fail'
    with step('Eyebrows - lift'):
        with step('[Action] tap_lift_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lift')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eyebrow lift both default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eyebrow_lift_both_min.png'):
            actions.capture_for_gt('05_07_12_eyebrow_lift_both_min.png')
        if actions.compare_with_gt('05_07_12_eyebrow_lift_both_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow lift both min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eyebrow_lift_both_max.png'):
            actions.capture_for_gt('05_07_12_eyebrow_lift_both_max.png')
        if actions.compare_with_gt('05_07_12_eyebrow_lift_both_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow lift both max fail'
    with step('Eyebrows - lift (left)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eyebrow lift left default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eyebrow_lift_left_min.png'):
            actions.capture_for_gt('05_07_12_eyebrow_lift_left_min.png')
        if actions.compare_with_gt('05_07_12_eyebrow_lift_left_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow lift left min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eyebrow_lift_left_max.png'):
            actions.capture_for_gt('05_07_12_eyebrow_lift_left_max.png')
        if actions.compare_with_gt('05_07_12_eyebrow_lift_left_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow lift left max fail'
    with step('Eyebrows - lift (right)'):
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        with step('[Action] tap_right_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Right')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eyebrow lift right default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eyebrow_lift_right_min.png'):
            actions.capture_for_gt('05_07_12_eyebrow_lift_right_min.png')
        if actions.compare_with_gt('05_07_12_eyebrow_lift_right_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow lift right min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eyebrow_lift_right_max.png'):
            actions.capture_for_gt('05_07_12_eyebrow_lift_right_max.png')
        if actions.compare_with_gt('05_07_12_eyebrow_lift_right_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow lift right max fail'
    with step('Eyebrows - distance'):
        with step('[Action] tap_eyebrows'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyebrows')
        with step('[Action] tap_distance2_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Distance')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eyebrow distance both default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eyebrow_distance_both_min.png'):
            actions.capture_for_gt('05_07_12_eyebrow_distance_both_min.png')
        if actions.compare_with_gt('05_07_12_eyebrow_distance_both_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow distance both min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eyebrow_distance_both_max.png'):
            actions.capture_for_gt('05_07_12_eyebrow_distance_both_max.png')
        if actions.compare_with_gt('05_07_12_eyebrow_distance_both_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow distance both max fail'
    with step('Eyebrows - distance (left)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eyebrow distance left default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eyebrow_distance_left_min.png'):
            actions.capture_for_gt('05_07_12_eyebrow_distance_left_min.png')
        if actions.compare_with_gt('05_07_12_eyebrow_distance_left_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow distance left min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eyebrow_distance_left_max.png'):
            actions.capture_for_gt('05_07_12_eyebrow_distance_left_max.png')
        if actions.compare_with_gt('05_07_12_eyebrow_distance_left_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow distance left max fail'
    with step('Eyebrows - distance (right)'):
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        with step('[Action] tap_right_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Right')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eyebrow distance right default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eyebrow_distance_right_min.png'):
            actions.capture_for_gt('05_07_12_eyebrow_distance_right_min.png')
        if actions.compare_with_gt('05_07_12_eyebrow_distance_right_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow distance right min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eyebrow_distance_right_max.png'):
            actions.capture_for_gt('05_07_12_eyebrow_distance_right_max.png')
        if actions.compare_with_gt('05_07_12_eyebrow_distance_right_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow distance right max fail'
    with step('Eyebrows - thickness'):
        with step('[Action] tap_thickness_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Thickness')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eyebrow_thickness_both_min.png'):
            actions.capture_for_gt('05_07_12_eyebrow_thickness_both_min.png')
        if actions.compare_with_gt('05_07_12_eyebrow_thickness_both_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow thickness both min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eyebrow_thickness_both_max.png'):
            actions.capture_for_gt('05_07_12_eyebrow_thickness_both_max.png')
        if actions.compare_with_gt('05_07_12_eyebrow_thickness_both_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow thickness both max fail'
    with step('Eyebrows - thickness (left)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eyebrow thickness left default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eyebrow_thickness_left_min.png'):
            actions.capture_for_gt('05_07_12_eyebrow_thickness_left_min.png')
        if actions.compare_with_gt('05_07_12_eyebrow_thickness_left_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow thickness left min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eyebrow_thickness_left_max.png'):
            actions.capture_for_gt('05_07_12_eyebrow_thickness_left_max.png')
        if actions.compare_with_gt('05_07_12_eyebrow_thickness_left_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow thickness left max fail'
    with step('Eyebrows - thickness (right)'):
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        with step('[Action] tap_right_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Right')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Eyebrow thickness right default value is not 0'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eyebrow_thickness_right_min.png'):
            actions.capture_for_gt('05_07_12_eyebrow_thickness_right_min.png')
        if actions.compare_with_gt('05_07_12_eyebrow_thickness_right_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow thickness right min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eyebrow_thickness_right_max.png'):
            actions.capture_for_gt('05_07_12_eyebrow_thickness_right_max.png')
        if actions.compare_with_gt('05_07_12_eyebrow_thickness_right_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow thickness right max fail'
    with step('Eyebrows - angle'):
        with step('[Action] tap_angle_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Angle')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eyebrow_angle_both_min.png'):
            actions.capture_for_gt('05_07_12_eyebrow_angle_both_min.png')
        if actions.compare_with_gt('05_07_12_eyebrow_angle_both_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow angle both min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eyebrow_angle_both_max.png'):
            actions.capture_for_gt('05_07_12_eyebrow_angle_both_max.png')
        if actions.compare_with_gt('05_07_12_eyebrow_angle_both_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow angle both max fail'
    with step('Eyebrows - angle (left)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eyebrow_angle_left_min.png'):
            actions.capture_for_gt('05_07_12_eyebrow_angle_left_min.png')
        if actions.compare_with_gt('05_07_12_eyebrow_angle_left_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow angle left min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eyebrow_angle_left_max.png'):
            actions.capture_for_gt('05_07_12_eyebrow_angle_left_max.png')
        if actions.compare_with_gt('05_07_12_eyebrow_angle_left_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow angle left max fail'
    with step('Eyebrows - angle (right)'):
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        with step('[Action] tap_right_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Right')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_eyebrow_angle_right_min.png'):
            actions.capture_for_gt('05_07_12_eyebrow_angle_right_min.png')
        if actions.compare_with_gt('05_07_12_eyebrow_angle_right_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow angle right min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_eyebrow_angle_right_max.png'):
            actions.capture_for_gt('05_07_12_eyebrow_angle_right_max.png')
        if actions.compare_with_gt('05_07_12_eyebrow_angle_right_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for eyebrow angle right max fail'
    with step('Nose - enlarge'):
        with step('[Action] tap_size_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushSizeSliderView')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_nose_enlarge_min.png'):
            actions.capture_for_gt('05_07_12_nose_enlarge_min.png')
        if actions.compare_with_gt('05_07_12_nose_enlarge_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose enlarge min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_nose_enlarge_max.png'):
            actions.capture_for_gt('05_07_12_nose_enlarge_max.png')
        if actions.compare_with_gt('05_07_12_nose_enlarge_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose enlarge max fail'
    with step('Nose - height'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Height')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_nose_height_min.png'):
            actions.capture_for_gt('05_07_12_nose_height_min.png')
        if actions.compare_with_gt('05_07_12_nose_height_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose height min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_nose_height_max.png'):
            actions.capture_for_gt('05_07_12_nose_height_max.png')
        if actions.compare_with_gt('05_07_12_nose_height_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose height max fail'
    with step('Nose - bridge'):
        with step('[Action] tap_bridge_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Bridge')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_nose_bridge_min.png'):
            actions.capture_for_gt('05_07_12_nose_bridge_min.png')
        if actions.compare_with_gt('05_07_12_nose_bridge_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose bridge min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_nose_bridge_max.png'):
            actions.capture_for_gt('05_07_12_nose_bridge_max.png')
        if actions.compare_with_gt('05_07_12_nose_bridge_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose bridge max fail'
    with step('Nose - ala (both)'):
        with step('[Action] tap_ala_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ala')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_nose_ala_both_min.png'):
            actions.capture_for_gt('05_07_12_nose_ala_both_min.png')
        if actions.compare_with_gt('05_07_12_nose_ala_both_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose ala both min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_nose_ala_both_max.png'):
            actions.capture_for_gt('05_07_12_nose_ala_both_max.png')
        if actions.compare_with_gt('05_07_12_nose_ala_both_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose ala both max fail'
    with step('Nose - ala (left)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_nose_ala_left_min.png'):
            actions.capture_for_gt('05_07_12_nose_ala_left_min.png')
        if actions.compare_with_gt('05_07_12_nose_ala_left_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose ala left min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_nose_ala_left_max.png'):
            actions.capture_for_gt('05_07_12_nose_ala_left_max.png')
        if actions.compare_with_gt('05_07_12_nose_ala_left_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose ala left max fail'
    with step('Nose - ala (right)'):
        with step('[Action] tap_left_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Left')
        with step('[Action] tap_right_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Right')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_nose_ala_right_min.png'):
            actions.capture_for_gt('05_07_12_nose_ala_right_min.png')
        if actions.compare_with_gt('05_07_12_nose_ala_right_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose ala right min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_nose_ala_right_max.png'):
            actions.capture_for_gt('05_07_12_nose_ala_right_max.png')
        if actions.compare_with_gt('05_07_12_nose_ala_right_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose ala right max fail'
    with step('Nose - tip'):
        with step('[Action] tap_tip_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tip')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_nose_tip_min.png'):
            actions.capture_for_gt('05_07_12_nose_tip_min.png')
        if actions.compare_with_gt('05_07_12_nose_tip_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose tip min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_nose_tip_max.png'):
            actions.capture_for_gt('05_07_12_nose_tip_max.png', crop_rect=(0, 60, 276, 429))
        if actions.compare_with_gt('05_07_12_nose_tip_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for nose tip max fail'
    with step('Lips - enlarge'):
        with step('[Action] tap_size_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushSizeSliderView')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Default value for lips size fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_lips_size_min.png'):
            actions.capture_for_gt('05_07_12_lips_size_min.png')
        with step('[Verify] compare: 05_07_12_lips_size_min.png'):
            assert actions.compare_with_gt('05_07_12_lips_size_min.png', gt_folder=TD.GT_FOLDER)[0]
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_lips_size_max.png'):
            actions.capture_for_gt('05_07_12_lips_size_max.png')
        with step('[Verify] compare: 05_07_12_lips_size_max.png'):
            assert actions.compare_with_gt('05_07_12_lips_size_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('Lips - smile'):
        with step('[Action] tap_smile2_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Smile')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Default value for lips smile fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_lips_smile_min.png'):
            actions.capture_for_gt('05_07_12_lips_smile_min.png')
        if actions.compare_with_gt('05_07_12_lips_smile_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for lips smile min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_lips_smile_max.png'):
            actions.capture_for_gt('05_07_12_lips_smile_max.png')
        if actions.compare_with_gt('05_07_12_lips_smile_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for lips smile max fail'
    with step('Lips - lift'):
        with step('[Action] tap_lift_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lift')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Default value for lips lift fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_lips_lift_min.png'):
            actions.capture_for_gt('05_07_12_lips_lift_min.png')
        if actions.compare_with_gt('05_07_12_lips_lift_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for lips lift min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_lips_lift_max.png'):
            actions.capture_for_gt('05_07_12_lips_lift_max.png')
        if actions.compare_with_gt('05_07_12_lips_lift_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for lips lift max fail'
    with step('Lips - thickness (both)'):
        with step('[Action] tap_thickness_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Thickness')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Default value for lips thickness both fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_lips_thickness_both_min.png'):
            actions.capture_for_gt('05_07_12_lips_thickness_both_min.png')
        if actions.compare_with_gt('05_07_12_lips_thickness_both_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for lips thickness both min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_lips_thickness_both_max.png'):
            actions.capture_for_gt('05_07_12_lips_thickness_both_max.png')
        if actions.compare_with_gt('05_07_12_lips_thickness_both_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for lips thickness both max fail'
    with step('Lips - thickness (upper)'):
        with step('[Action] tap_both_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Both')
        with step('[Action] tap_upper_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Upper')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Default value for lips thickness upper fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_lips_thickness_up_min.png'):
            actions.capture_for_gt('05_07_12_lips_thickness_up_min.png')
        if actions.compare_with_gt('05_07_12_lips_thickness_up_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for lips thickness upper min fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_lips_thickness_up_max.png'):
            actions.capture_for_gt('05_07_12_lips_thickness_up_max.png')
        if actions.compare_with_gt('05_07_12_lips_thickness_up_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for lips thickness upper max fail'
    with step('Lips - thickness (lower)'):
        with step('[Action] tap_upper_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Upper')
        with step('[Action] tap_lower_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Lower')
        if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel') == '0'):
            pass
        else:
            assert False, 'Default value for lips thickness lower fail'
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
        with step('[Verify] snapshot: 05_07_12_lips_thickness_low_min.png'):
            actions.capture_for_gt('05_07_12_lips_thickness_low_min.png')
        if actions.compare_with_gt('05_07_12_lips_thickness_low_min.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for lips thickness lower min fail'
        with step('[Verify] snapshot: 05_07_12_undo_og.png'):
            actions.capture_for_gt('05_07_12_undo_og.png', crop_rect=(0, 60, 276, 526))
        with step('[Action] adjust_harmonization_slider'):
            assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
        with step('[Verify] snapshot: 05_07_12_lips_thickness_low_max.png'):
            actions.capture_for_gt('05_07_12_lips_thickness_low_max.png')
        if actions.compare_with_gt('05_07_12_lips_thickness_low_max.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Comparison for lips thickness lower max fail'
        with step('[Verify] snapshot: 05_07_12_before_undo.png'):
            actions.capture_for_gt('05_07_12_before_undo.png', crop_rect=(0, 60, 276, 526))
    with step('Undo'):
        with step('[Action] tap_undo_btn_n'):
            for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
                if actions.is_element_present(__by, __val, timeout=2):
                    actions.tap_by_locator(__by, __val); break
        with step('[Verify] snapshot: 05_07_12_undo.png'):
            actions.capture_for_gt('05_07_12_undo.png', crop_rect=(0, 60, 276, 526))
        if actions.compare_with_gt('05_07_12_undo.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Undo comparison fail'
    with step('Redo'):
        with step('[Action] tap_redo_btn_n'):
            for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
                if actions.is_element_present(__by, __val, timeout=2):
                    actions.tap_by_locator(__by, __val); break
        with step('[Verify] snapshot: 05_07_12_redo.png'):
            actions.capture_for_gt('05_07_12_redo.png', crop_rect=(0, 60, 276, 526))
        if actions.compare_with_gt('05_07_12_redo.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False, 'Redo comparison fail'
    with step('Apply reshape'):
        if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
            assert False, 'Failed to tap done button'
        if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
            pass
        else:
            assert False, 'Verify IAP fail'
    with step("[Verify] test_00076 completion"):
        assert True
