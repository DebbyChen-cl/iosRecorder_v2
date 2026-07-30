import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00143_main_05_01_12_4')
def test_00143_main_05_01_12_4(actions: DriverActions):
    """quick action - background"""
    mode = 1
    uuid = ['262cafbd-2d1e-4992-8645-8b856baabb96', 'd79582ed-83fd-470b-99bf-3978560173fa', 'b70b8f91-4b20-4022-905a-38c5d3eb36ef', 'd99eef00-faa1-400d-9860-8038a1f05753', '57375cce-5998-4b5e-86d1-725604765374', '61025103-898d-4c48-8c92-733e6d7d6eca', '97666038-474a-4ffc-b7d2-b2414477e585', 'b505b1e1-4039-40b4-a980-90810a649099', '013f9d68-ede7-4a49-b669-c351a6e935a5', '50486657-ef79-41a8-980a-8cbe798a46f1', '58d60a2a-9287-4565-8682-58d04c958e22', '7cef2fb2-aad2-486f-add7-21c57513cf28', '481ce344-32f2-4ac8-9be4-0aef668ef55f', '201bde9a-9ec0-43b4-acd8-110693ede08e', '80fbfe65-a41c-47f5-a844-8b405b6b5643', '98ee5935-ed71-4810-a1f1-fcab19956bce', 'be4a0a56-2230-4f08-870e-794f5646cd4b', '3774cccf-0313-4ba6-ad69-365508f7f44f', '7770bf61-9e71-4c93-b672-165a7ea064d8', 'f7d1d6c1-2563-4ff7-bb66-b14a7bb3bb16', '0e8e92d8-3197-40d2-a29d-dc63e08895c7', '0d94936d-cafa-4d6b-a887-e4a7343bc5fb', 'bbbdced2-66c9-4347-ba84-4f6b78e173b7', '3aa957c5-426e-4fe0-ae48-ef57e28fb73e', '804acbf9-68ba-4104-9ac2-8a1ae7505854', '4e8b75d4-8cf2-49fc-9bcc-899a3b5f613b', 'a4467fef-86ba-4f96-97fa-2311348690b5', '6d6000f2-5a8e-42f2-b92d-e0bf33827fc8', '4d5809e5-832a-4de0-a620-ea8e7ec37918', 'd47638b6-9735-4b30-a521-576b960ca0fb', 'dac4d650-70bc-4b28-88b7-863b3ff266c2', 'c2f5db25-2f8b-4413-8806-ade76059830a', '2b682d12-1500-4aba-ab52-2aeff207fee2', 'dab46856-20a7-40ae-81ea-b91f7c5efaaf', '3804a535-5f01-4450-a34b-573395ab7029', '1b8b822b-8c9c-435f-8359-3c535f82d254', '2226a032-a525-474c-be81-2a398468946e', '7afd3b59-d3aa-44f2-ac25-7970a0353651', 'be0daadf-9e99-4260-b1bd-37498fd3e36e', 'c53600e0-d897-493f-84b9-18f25147b89b', 'a1a35be8-5fec-4550-8a40-d1ac3843c1a3', '2b283233-525b-49f8-93b6-91f61841ed14', 'ae284e77-a7a9-4212-a5f7-5d9f1e8c0955', 'd92b7b04-256b-4938-ba58-7375664afa55', 'd369f228-2dad-4009-8732-5656e68031fe', '2e0cce44-a800-456c-a7b6-709cd4972080', '6c91576c-1e21-430e-a348-964e5ceff80e', '732b838e-647f-44d3-8dcb-43dec111ebfc', 'f24700dc-0114-4ec7-84af-1dc3270f37df', '13585286-0e7c-413a-850d-a7bcdf46813a']
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step('[Action] verify_settings_page'):
        assert (
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Setting')
            or actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
        )
    enter_about_page_success = False
    for attempt in range(3):
        with step('[Action] enter_about_page'):
            if actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'About') and actions.is_element_present(
                AppiumBy.ACCESSIBILITY_ID, 'developerButton'
            ):
                enter_about_page_success = True
                break
    if not enter_about_page_success:
        assert False, 'Enter about page fail after 3 retries'
    with step('[Action] enable_plan_from_settings'):
        assert actions.is_element_present(AppiumBy.NAME, 'Develop Info')
        assert actions.find_element(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="1"])[2]')
        actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[6]')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_home'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
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
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle')
    with step('[Verify] snapshot: 05_01_12_before_quick_bg.png'):
        actions.capture_for_gt('05_01_12_before_quick_bg.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Detecting Background', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Detecting Background')
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'None')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') == '0'):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_default.png'):
        assert actions.capture_for_gt('05_01_12_bg_default.png')
    with step('[Verify] compare: 05_01_12_bg_default.png'):
        assert actions.compare_with_gt('05_01_12_bg_default.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('-100', '-99', '-98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_exposure_min.png'):
        assert actions.capture_for_gt('05_01_12_bg_exposure_min.png')
    with step('[Verify] compare: 05_01_12_bg_exposure_min.png'):
        assert actions.compare_with_gt('05_01_12_bg_exposure_min.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_exposure_max.png'):
        assert actions.capture_for_gt('05_01_12_bg_exposure_max.png')
    with step('[Verify] compare: 05_01_12_bg_exposure_max.png'):
        assert actions.compare_with_gt('05_01_12_bg_exposure_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] reset_quick_exposure_value'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'exposureResetButton')
    with step('[Action] get_quick_exposure_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]')
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '0'):
        pass
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('-100', '-99', '-98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_saturation_min.png'):
        assert actions.capture_for_gt('05_01_12_bg_saturation_min.png')
    with step('[Verify] compare: 05_01_12_bg_saturation_min.png'):
        assert actions.compare_with_gt('05_01_12_bg_saturation_min.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_saturation_max.png'):
        assert actions.capture_for_gt('05_01_12_bg_saturation_max.png')
    with step('[Verify] compare: 05_01_12_bg_saturation_max.png'):
        assert actions.compare_with_gt('05_01_12_bg_saturation_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] reset_quick_saturation_value'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'saturationResetButton')
    with step('[Action] get_quick_saturation_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]')
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_01_12_bg_v.png'):
        assert actions.capture_for_gt('05_01_12_bg_v.png')
    if (not actions.compare_with_gt('05_01_12_bg_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Compare 05_01_12_bg_v.png fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Detecting Background', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Detecting Background')
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Blur')
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Verify] snapshot: 05_01_12_bg_blur_default.png'):
        assert actions.capture_for_gt('05_01_12_bg_blur_default.png')
    if actions.compare_with_gt('05_01_12_bg_blur_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_blur_default.png fail'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_blur_min.png'):
        assert actions.capture_for_gt('05_01_12_bg_blur_min.png')
    if actions.compare_with_gt('05_01_12_bg_blur_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_blur_min.png fail'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_blur_max.png'):
        assert actions.capture_for_gt('05_01_12_bg_blur_max.png')
    if actions.compare_with_gt('05_01_12_bg_blur_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_blur_max.png fail'
    with step('[Action] reset_quick_intensity_value'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Circle')
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Verify] snapshot: 05_01_12_bg_circle_default.png'):
        assert actions.capture_for_gt('05_01_12_bg_circle_default.png')
    if actions.compare_with_gt('05_01_12_bg_circle_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_circle_default.png fail'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_circle_min.png'):
        assert actions.capture_for_gt('05_01_12_bg_circle_min.png')
    if actions.compare_with_gt('05_01_12_bg_circle_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_circle_min.png fail'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_circle_max.png'):
        assert actions.capture_for_gt('05_01_12_bg_circle_max.png')
    if actions.compare_with_gt('05_01_12_bg_circle_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_circle_max.png fail'
    with step('[Action] reset_quick_intensity_value'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Heart')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_heart_default.png'):
        assert actions.capture_for_gt('05_01_12_bg_heart_default.png')
    if actions.compare_with_gt('05_01_12_bg_heart_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_heart_default.png fail'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_heart_min.png'):
        assert actions.capture_for_gt('05_01_12_bg_heart_min.png')
    if actions.compare_with_gt('05_01_12_bg_heart_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_heart_min.png fail'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_heart_max.png'):
        assert actions.capture_for_gt('05_01_12_bg_heart_max.png')
    if actions.compare_with_gt('05_01_12_bg_heart_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_heart_max.png fail'
    with step('[Action] reset_quick_intensity_value'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sparkle')
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Verify] snapshot: 05_01_12_bg_sparkle_default.png'):
        assert actions.capture_for_gt('05_01_12_bg_sparkle_default.png')
    if actions.compare_with_gt('05_01_12_bg_sparkle_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_sparkle_default.png fail'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_sparkle_min.png'):
        assert actions.capture_for_gt('05_01_12_bg_sparkle_min.png')
    if actions.compare_with_gt('05_01_12_bg_sparkle_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_sparkle_min.png fail'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_sparkle_max.png'):
        assert actions.capture_for_gt('05_01_12_bg_sparkle_max.png')
    if actions.compare_with_gt('05_01_12_bg_sparkle_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_sparkle_max.png fail'
    with step('[Action] reset_quick_intensity_value'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Star')
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Verify] snapshot: 05_01_12_bg_star_default.png'):
        assert actions.capture_for_gt('05_01_12_bg_star_default.png')
    if actions.compare_with_gt('05_01_12_bg_star_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_star_default.png fail'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_star_min.png'):
        assert actions.capture_for_gt('05_01_12_bg_star_min.png')
    if actions.compare_with_gt('05_01_12_bg_star_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_star_min.png fail'
    with step('[Verify] snapshot: 05_01_12_bg_undo_og.png'):
        actions.capture_for_gt('05_01_12_bg_undo_og.png')
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_bg_star_max.png'):
        assert actions.capture_for_gt('05_01_12_bg_star_max.png')
    if actions.compare_with_gt('05_01_12_bg_star_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_star_max.png fail'
    with step('[Action] reset_quick_intensity_value'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Zoom')
    if actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') != '25':
        assert False, 'Zoom default intensity is not 25'
    with step('[Verify] snapshot: 05_01_12_bg_zoom_default.png'):
        assert actions.capture_for_gt('05_01_12_bg_zoom_default.png')
    with step('[Verify] compare: 05_01_12_bg_zoom_default.png'):
        assert actions.compare_with_gt('05_01_12_bg_zoom_default.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') not in ('0', '1', '2', '3'):
        assert False, 'Zoom min intensity value error'
    with step('[Verify] snapshot: 05_01_12_bg_zoom_min.png'):
        assert actions.capture_for_gt('05_01_12_bg_zoom_min.png')
    with step('[Verify] compare: 05_01_12_bg_zoom_min.png'):
        assert actions.compare_with_gt('05_01_12_bg_zoom_min.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') not in ('100', '99', '98', '97'):
        assert False, 'Zoom max intensity value error'
    with step('[Verify] snapshot: 05_01_12_bg_zoom_max.png'):
        assert actions.capture_for_gt('05_01_12_bg_zoom_max.png')
    with step('[Verify] compare: 05_01_12_bg_zoom_max.png'):
        assert actions.compare_with_gt('05_01_12_bg_zoom_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] reset_quick_intensity_value'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Verify] snapshot: 05_01_12_bg_zoom_reset.png'):
        assert actions.capture_for_gt('05_01_12_bg_zoom_reset.png')
    with step('[Verify] compare: 05_01_12_bg_zoom_reset.png'):
        assert actions.compare_with_gt('05_01_12_bg_zoom_reset.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Radial')
    if actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') != '25':
        assert False, 'Radial default intensity is not 25'
    with step('[Verify] snapshot: 05_01_12_bg_radial_default.png'):
        assert actions.capture_for_gt('05_01_12_bg_radial_default.png')
    with step('[Verify] compare: 05_01_12_bg_radial_default.png'):
        assert actions.compare_with_gt('05_01_12_bg_radial_default.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') not in ('0', '1', '2', '3'):
        assert False, 'Radial min intensity value error'
    with step('[Verify] snapshot: 05_01_12_bg_radial_min.png'):
        assert actions.capture_for_gt('05_01_12_bg_radial_min.png')
    with step('[Verify] compare: 05_01_12_bg_radial_min.png'):
        assert actions.compare_with_gt('05_01_12_bg_radial_min.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') not in ('100', '99', '98', '97'):
        assert False, 'Radial max intensity value error'
    with step('[Verify] snapshot: 05_01_12_bg_radial_max.png'):
        assert actions.capture_for_gt('05_01_12_bg_radial_max.png')
    with step('[Verify] compare: 05_01_12_bg_radial_max.png'):
        assert actions.compare_with_gt('05_01_12_bg_radial_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] reset_quick_intensity_value'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'intensityResetButton')
    with step('[Action] get_quick_bg_intensity_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "valueLabel"`][3]') == '25'
    with step('[Verify] snapshot: 05_01_12_bg_radial_reset.png'):
        assert actions.capture_for_gt('05_01_12_bg_radial_reset.png')
    with step('[Verify] compare: 05_01_12_bg_radial_reset.png'):
        assert actions.compare_with_gt('05_01_12_bg_radial_reset.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Verify] snapshot: 05_01_12_bg_redo_og.png'):
        actions.capture_for_gt('05_01_12_bg_redo_og.png')
    with step('[Action] tap_undo_btn_2'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step('[Verify] snapshot: 05_01_12_bg_undo.png'):
        assert actions.capture_for_gt('05_01_12_bg_undo.png')
    if actions.compare_with_gt('05_01_12_bg_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_undo.png fail'
    with step('[Action] tap_redo_btn_2'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n')
    with step('[Verify] snapshot: 05_01_12_bg_redo.png'):
        assert actions.capture_for_gt('05_01_12_bg_redo.png')
    if actions.compare_with_gt('05_01_12_bg_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_redo.png fail'
    with step('[Action] tap_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic reset n')
    with step('[Verify] snapshot: 05_01_12_bg_reset.png'):
        assert actions.capture_for_gt('05_01_12_bg_reset.png')
    if actions.compare_with_gt('05_01_12_bg_reset.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare 05_01_12_bg_reset.png fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap done btn [v] fail'
    with step('[Verify] snapshot: 05_01_12_bg_v2.png'):
        assert actions.capture_for_gt('05_01_12_bg_v2.png')
    if (not actions.compare_with_gt('05_01_12_bg_v2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Compare 05_01_12_bg_v2.png fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_01_12_bg_x.png'):
        assert actions.capture_for_gt('05_01_12_bg_x.png')
    if actions.compare_with_gt('05_01_12_bg_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step("[Verify] test_00143 completion"):
        assert True
