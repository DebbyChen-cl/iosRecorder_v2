import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00145_main_05_01_12_6')
def test_00145_main_05_01_12_6(actions: DriverActions):
    """quick action - preset"""
    uuid = ['6601ce13-3fe0-4e2e-a611-23b7b871bef8', '1b40e817-8273-48ca-979d-9258e1151dc2', 'bbd6d4c6-ad8a-45c1-9983-503ae4277e52', '26ae1ce7-b3dc-40c6-b366-423aae487f0f', 'ffd61a65-112b-41ab-a348-3492aab47011', 'ad049f6a-afd4-47e4-b397-4750a77dbcec', '656d6bbf-927e-45f8-af98-670cc5d6701f', 'a01db1ea-6ba6-4be7-90a8-751dc53f17cd', '3480cab2-3a90-40fa-b771-afd7eb7fa45f', '5eb772b5-0c30-4794-843b-7a9ef03a81a3', '24c8e490-08b2-43ba-9c10-50f5437f00cc', '0e8a6fea-c549-4064-bbb6-8ad70fde37c0', 'c28c17f6-62b5-422c-87d1-730b33796400', '7b88688f-0914-465c-83d5-62bc87e0d640', '63dd72fd-09e7-4a46-8488-bc0bbd6a5da7', '12b30ee3-3655-4e7e-afe8-158a25516c5a', '6f38912c-cf98-4eec-a6b6-5cf0f477458e', '56c6a1cd-f814-486f-8da3-df9202ecb8da', '5e04e53f-11f8-4a6d-92d7-35b7d786d361', 'cd4e3536-64f4-4e3c-bfab-a0d9cb362c0e', 'bb757938-22f5-44bc-8f28-96940ba20623', 'faaacba2-55c9-4171-906c-e6eab573601f', 'd3ee0acf-9e51-4078-a58e-6b9ee7fe1bc7', 'a07416ae-0030-4a0d-96a0-72582732359e', 'fa34815a-056a-4355-be2a-0943f20f5607', '7367766f-e6b6-4512-91d5-915624ceceb6', '7fd6ece6-a5da-4357-aae9-a13d655c27c4', 'f37d2cfa-c594-44d4-b9cc-f03bd4eb0795', 'e35eba48-71e6-4c7f-be78-cf0f2f83c19b', '9275d55e-cd36-42dd-8cf0-7ac280c7894c', '5ab744d4-da03-4c8e-aef2-13f299dd4c6a', 'a13ea329-007c-4d1b-ab6c-96631c2e45cf', 'a6030cbe-0148-44a4-b8f9-8f862d468498', 'fb39ee07-f68e-4d77-ab07-a4393f8807f6', '3a21d1c7-e8dd-4e67-af27-38ef105961fe', 'e70f6923-99aa-48f6-9d91-a62d0c1ebfaa', '9d0b92b3-873d-482c-a180-5bc396746e89', '8c6c3fd1-f879-4df1-942c-308d9dfc7db5', 'eb8d6ad3-1d22-48a4-86f6-2644a8e656f7', '0023ce6e-5b3b-4496-94cc-4cd4aa9cdf5a', '5b3c8d31-d577-4487-8ef8-087221325f34', '1442c701-9ced-4095-9c2b-db346b754277', '83d6f230-fec9-4df4-bb87-11daddac26b2', '46ab9305-0ef8-4014-bbd1-0af09be321c1', '8ea7c02e-5568-49fa-9fba-85645a719f31', '2ab10435-8d79-4a6b-ba6b-bf0e5c9dcae8', '1d4c1678-3501-422e-b208-2f1f28b233eb', '40023e35-8adf-4113-8100-4153ff445568', 'f315631b-a7aa-45e0-84ae-cd0ce5e5a49a', 'bc2f1eb6-eca9-44b2-afe2-78269dfc3e2b']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
            actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'BG')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
    with step('[Action] close_airemoval_iap_dialog2'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Try First', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle')
    with step('[Verify] snapshot: 05_01_12_before_quick_preset.png'):
        actions.capture_for_gt('05_01_12_before_quick_preset.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Presets')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Food')
    with step('[Verify] snapshot: 05_01_12_preset_food_d.png'):
        actions.capture_for_gt('05_01_12_preset_food_d.png')
    if actions.compare_with_gt('05_01_12_preset_food_d.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare food default fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') == '70'):
        pass
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_preset_food_min.png'):
        actions.capture_for_gt('05_01_12_preset_food_min.png')
    if actions.compare_with_gt('05_01_12_preset_food_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare food min fail'
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_preset_food_max.png'):
        actions.capture_for_gt('05_01_12_preset_food_max.png')
    if actions.compare_with_gt('05_01_12_preset_food_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare food max fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Food 02')
    with step('[Verify] snapshot: 05_01_12_preset_food_2.png'):
        actions.capture_for_gt('05_01_12_preset_food_2.png')
    if actions.compare_with_gt('05_01_12_preset_food_2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare food 2 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Food 01')
    with step('[Verify] snapshot: 05_01_12_preset_food_1.png'):
        actions.capture_for_gt('05_01_12_preset_food_1.png')
    if actions.compare_with_gt('05_01_12_preset_food_1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare food 1 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Food 03')
    with step('[Verify] snapshot: 05_01_12_preset_food_3.png'):
        actions.capture_for_gt('05_01_12_preset_food_3.png')
    if actions.compare_with_gt('05_01_12_preset_food_3.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare food 3 fail'
    from_pos = (360, 780)
    to_pos = (60, 780)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(360, 780, 60, 780)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Food 04')
    with step('[Verify] snapshot: 05_01_12_preset_food_4.png'):
        actions.capture_for_gt('05_01_12_preset_food_4.png')
    if actions.compare_with_gt('05_01_12_preset_food_4.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare food 4 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('[Action] close_airemoval_iap_dialog2'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Try First', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Presets')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Indoor')
    with step('[Verify] snapshot: 05_01_12_preset_indoor_d.png'):
        actions.capture_for_gt('05_01_12_preset_indoor_d.png')
    if actions.compare_with_gt('05_01_12_preset_indoor_d.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare indoor default fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') == '70'):
        pass
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_preset_indoor_min.png'):
        actions.capture_for_gt('05_01_12_preset_indoor_min.png')
    if actions.compare_with_gt('05_01_12_preset_indoor_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare indoor min fail'
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_preset_indoor_max.png'):
        actions.capture_for_gt('05_01_12_preset_indoor_max.png')
    if actions.compare_with_gt('05_01_12_preset_indoor_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare indoor max fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Indoor 02')
    with step('[Verify] snapshot: 05_01_12_preset_indoor_2.png'):
        actions.capture_for_gt('05_01_12_preset_indoor_2.png')
    if actions.compare_with_gt('05_01_12_preset_indoor_2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare indoor 2 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Indoor 01')
    with step('[Verify] snapshot: 05_01_12_preset_indoor_1.png'):
        actions.capture_for_gt('05_01_12_preset_indoor_1.png')
    if actions.compare_with_gt('05_01_12_preset_indoor_1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare indoor 1 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Indoor 03')
    with step('[Verify] snapshot: 05_01_12_preset_indoor_3.png'):
        actions.capture_for_gt('05_01_12_preset_indoor_3.png')
    if actions.compare_with_gt('05_01_12_preset_indoor_3.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare indoor 3 fail'
    with step('[Verify] snapshot: 05_01_12_preset_indoor_4.png'):
        actions.capture_for_gt('05_01_12_preset_indoor_4.png')
    if actions.compare_with_gt('05_01_12_preset_indoor_4.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare indoor 4 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Indoor 05')
    with step('[Verify] snapshot: 05_01_12_preset_indoor_5.png'):
        actions.capture_for_gt('05_01_12_preset_indoor_5.png')
    if actions.compare_with_gt('05_01_12_preset_indoor_5.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare indoor 5 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Indoor 06')
    with step('[Verify] snapshot: 05_01_12_preset_indoor_6.png'):
        actions.capture_for_gt('05_01_12_preset_indoor_6.png')
    if actions.compare_with_gt('05_01_12_preset_indoor_6.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare indoor 6 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-3')
    with step('[Action] close_airemoval_iap_dialog2'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Try First', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Presets')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor')
    with step('[Verify] snapshot: 05_01_12_preset_outdoor_d.png'):
        actions.capture_for_gt('05_01_12_preset_outdoor_d.png')
    if actions.compare_with_gt('05_01_12_preset_outdoor_d.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare outdoor default fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') == '70'):
        pass
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_preset_outdoor_min.png'):
        actions.capture_for_gt('05_01_12_preset_outdoor_min.png')
    if actions.compare_with_gt('05_01_12_preset_outdoor_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare outdoor min fail'
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_preset_outdoor_max.png'):
        actions.capture_for_gt('05_01_12_preset_outdoor_max.png')
    if actions.compare_with_gt('05_01_12_preset_outdoor_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare outdoor max fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 02')
    with step('[Verify] snapshot: 05_01_12_preset_outdoor_2.png'):
        actions.capture_for_gt('05_01_12_preset_outdoor_2.png')
    if actions.compare_with_gt('05_01_12_preset_outdoor_2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare outdoor 2 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 01')
    with step('[Verify] snapshot: 05_01_12_preset_outdoor_1.png'):
        actions.capture_for_gt('05_01_12_preset_outdoor_1.png')
    if actions.compare_with_gt('05_01_12_preset_outdoor_1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare outdoor 1 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 03')
    with step('[Verify] snapshot: 05_01_12_preset_outdoor_3.png'):
        actions.capture_for_gt('05_01_12_preset_outdoor_3.png')
    if actions.compare_with_gt('05_01_12_preset_outdoor_3.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare outdoor 3 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 04')
    with step('[Verify] snapshot: 05_01_12_preset_outdoor_4.png'):
        actions.capture_for_gt('05_01_12_preset_outdoor_4.png')
    if actions.compare_with_gt('05_01_12_preset_outdoor_4.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare outdoor 4 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 05')
    with step('[Verify] snapshot: 05_01_12_preset_outdoor_5.png'):
        actions.capture_for_gt('05_01_12_preset_outdoor_5.png')
    if actions.compare_with_gt('05_01_12_preset_outdoor_5.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare outdoor 5 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 06')
    with step('[Verify] snapshot: 05_01_12_preset_outdoor_6.png'):
        actions.capture_for_gt('05_01_12_preset_outdoor_6.png')
    if actions.compare_with_gt('05_01_12_preset_outdoor_6.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare outdoor 6 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 07')
    with step('[Verify] snapshot: 05_01_12_preset_outdoor_7.png'):
        actions.capture_for_gt('05_01_12_preset_outdoor_7.png')
    if actions.compare_with_gt('05_01_12_preset_outdoor_7.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare outdoor 7 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 08')
    with step('[Verify] snapshot: 05_01_12_preset_outdoor_8.png'):
        actions.capture_for_gt('05_01_12_preset_outdoor_8.png')
    if actions.compare_with_gt('05_01_12_preset_outdoor_8.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare outdoor 8 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Outdoor 09')
    with step('[Verify] snapshot: 05_01_12_preset_outdoor_9.png'):
        actions.capture_for_gt('05_01_12_preset_outdoor_9.png')
    if actions.compare_with_gt('05_01_12_preset_outdoor_9.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare outdoor 9 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step('[Action] close_airemoval_iap_dialog2'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Try First', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Try First')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'Try First')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Presets')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery')
    with step('[Verify] snapshot: 05_01_12_preset_scenery_d.png'):
        actions.capture_for_gt('05_01_12_preset_scenery_d.png')
    if actions.compare_with_gt('05_01_12_preset_scenery_d.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare scenery default fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') == '70'):
        pass
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_preset_scenery_min.png'):
        actions.capture_for_gt('05_01_12_preset_scenery_min.png')
    if actions.compare_with_gt('05_01_12_preset_scenery_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare scenery min fail'
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_preset_scenery_max.png'):
        actions.capture_for_gt('05_01_12_preset_scenery_max.png')
    if actions.compare_with_gt('05_01_12_preset_scenery_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare scenery max fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 02')
    with step('[Verify] snapshot: 05_01_12_preset_scenery_2.png'):
        actions.capture_for_gt('05_01_12_preset_scenery_2.png')
    if actions.compare_with_gt('05_01_12_preset_scenery_2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare scenery 2 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 01')
    with step('[Verify] snapshot: 05_01_12_preset_scenery_1.png'):
        actions.capture_for_gt('05_01_12_preset_scenery_1.png')
    if actions.compare_with_gt('05_01_12_preset_scenery_1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare scenery 1 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 03')
    with step('[Verify] snapshot: 05_01_12_preset_scenery_3.png'):
        actions.capture_for_gt('05_01_12_preset_scenery_3.png')
    if actions.compare_with_gt('05_01_12_preset_scenery_3.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare scenery 3 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 04')
    with step('[Verify] snapshot: 05_01_12_preset_scenery_4.png'):
        actions.capture_for_gt('05_01_12_preset_scenery_4.png')
    if actions.compare_with_gt('05_01_12_preset_scenery_4.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare scenery 4 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 05')
    with step('[Verify] snapshot: 05_01_12_preset_scenery_5.png'):
        actions.capture_for_gt('05_01_12_preset_scenery_5.png')
    if actions.compare_with_gt('05_01_12_preset_scenery_5.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare scenery 5 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 06')
    with step('[Verify] snapshot: 05_01_12_preset_scenery_6.png'):
        actions.capture_for_gt('05_01_12_preset_scenery_6.png')
    if actions.compare_with_gt('05_01_12_preset_scenery_6.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare scenery 6 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 07')
    with step('[Verify] snapshot: 05_01_12_preset_scenery_7.png'):
        actions.capture_for_gt('05_01_12_preset_scenery_7.png')
    if actions.compare_with_gt('05_01_12_preset_scenery_7.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare scenery 7 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 08')
    with step('[Verify] snapshot: 05_01_12_preset_scenery_8.png'):
        actions.capture_for_gt('05_01_12_preset_scenery_8.png')
    if actions.compare_with_gt('05_01_12_preset_scenery_8.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare scenery 8 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Scenery 09')
    with step('[Verify] snapshot: 05_01_12_preset_scenery_9.png'):
        actions.capture_for_gt('05_01_12_preset_scenery_9.png')
    if actions.compare_with_gt('05_01_12_preset_scenery_9.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare scenery 9 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Presets')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'General')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'General 01')
    with step('[Verify] snapshot: 05_01_12_preset_general_1.png'):
        actions.capture_for_gt('05_01_12_preset_general_1.png')
    if actions.compare_with_gt('05_01_12_preset_general_1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare general 1 fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') == '70'):
        pass
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_preset_general_min.png'):
        actions.capture_for_gt('05_01_12_preset_general_min.png')
    if actions.compare_with_gt('05_01_12_preset_general_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare general min fail'
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_preset_general_max.png'):
        actions.capture_for_gt('05_01_12_preset_general_max.png')
    if actions.compare_with_gt('05_01_12_preset_general_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare general max fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'General 02')
    with step('[Verify] snapshot: 05_01_12_preset_general_2.png'):
        actions.capture_for_gt('05_01_12_preset_general_2.png')
    if actions.compare_with_gt('05_01_12_preset_general_2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare general 2 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'General 03')
    with step('[Verify] snapshot: 05_01_12_preset_general_3.png'):
        actions.capture_for_gt('05_01_12_preset_general_3.png')
    if actions.compare_with_gt('05_01_12_preset_general_3.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare general 3 fail'
    with step("[Verify] test_00145 completion"):
        assert True
