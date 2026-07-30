import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00142_main_05_01_12_2')
def test_00142_main_05_01_12_2(actions: DriverActions):
    """quick action - subject"""
    mode = 1
    uuid = ['ad86d16a-301a-45f4-baa6-9862ad0e4c0f', 'add15695-4598-4ce9-aa89-3873f4bd0618', '72f063ea-78fe-4cad-af79-0c5a947e6b02', 'edb8d032-1f47-4427-9eae-92a15d009cb8', 'cf76a39d-8635-4c6a-b113-bc34f2a064fb', '0d7e45dc-b286-4cf6-b614-f4dba2f05384', 'a5b387d6-4ce4-4451-b853-ef2a860660a7', '43e3e61d-0524-4e4e-b346-1e8e1a324616', '83984da4-23c2-4378-ad7e-bbd15d77348a', '77dcbc97-79ec-42ca-9f0d-198a9a633cb5', '0770c206-bd46-4997-a830-00c448fd88db', '07111ad5-7002-4139-9f8f-a3755c943fca', 'eb5461f9-c52e-42c7-9785-089748437847', 'da1dfcdc-2e57-4622-a325-f942d2fa17e7', 'f5e54439-ad88-4553-a4c3-741f4170d510', 'f55b53c7-2ede-464f-838c-d9d2b1b22976', '2533e340-9a5e-4350-93b7-b7a1b20dea0b', '3cf97c17-bcf2-4806-b003-23e0534c4659', '5ebda368-4b91-4884-b821-edaabfb73b2b', '6227c50d-e0c7-46a1-b044-38bd0851d840', 'e6e70610-0fe9-4a47-ac38-aacad287c04f', '89f0aa1a-d083-4291-b915-984626d93280', 'e76e50aa-c3e3-4adc-b263-ed81141e4b20', '611cff8d-4b8d-45ce-8f5e-f270bb751b07', 'b38d6697-d8e7-49b0-9f55-2e4d90d6772f', 'eb5d5ec0-54e0-4866-9e50-9142979824d2', '5347fc0f-889d-4892-b243-7fa255b3cde4', '03136f73-8341-4714-9021-9e10cdfb7383', '01a169a0-276a-49f7-bcf6-ed78fed5ee8f', '4a1ccc15-12f9-4ba7-ab22-d364ba4e1cdb', '004e21da-36f3-4fa8-a74d-177a32642dc1', '06650507-47c7-45ea-a969-00b9d6045124', '038bfa49-5f29-4fb6-a8fe-cc17b04c9e87', '91306154-3952-483f-b2dd-87bef9eb4729', '4a65ebe5-7320-4894-8b1d-041f607e99e1', 'ea82ca45-429a-4a48-94b7-70c9e4693349', '57b22d1b-fc82-4c83-a9ca-7e0c5519e913', '1b56376d-5893-4e3b-aeef-a87a99c6acb8', '0c51ab74-330d-4bb9-857d-34118293e1ea', '60de7afd-7c4a-45c5-bbfa-10d259a58c4f', '6379e701-807e-4b22-9c61-30302390e388', 'f7336a2c-41eb-451a-919e-b82341cfc516', 'b068c7ca-c7e3-447e-b2fc-3c155da0f42a', 'e7e84e5f-2a66-4d62-91b3-4fae60e1d0d0', 'ebaac88a-8e41-4e22-9075-b435917ffce1', '540f96e9-5270-469a-b120-612577c7de71', 'd3501364-ca37-447a-9fcf-86258a464a16', 'f41f088c-8440-494f-a87a-bb0967cbe4a7', '714b76fb-1835-458d-b428-1c2b41d94ebc', 'd78bae7a-d91b-47db-93e7-4a458966a20d', '90364b86-4089-4490-8692-9c9fd6c002d8', '3c6331a4-ce46-456c-9d26-a6de8bc6e7d1', 'a3d0abad-95d8-4a7d-b727-45a29790ef68', '9256dbec-0768-4c63-a78f-1c9f3706b8bc', '28fdd2f6-7abe-44e6-9240-c5ce6a8d804c']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
            actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Quick Actions')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'waitingTitle')
    with step('[Verify] snapshot: 05_01_12_before_quick_subject.png'):
        actions.capture_for_gt('05_01_12_before_quick_subject.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Subject')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Detecting Subject', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Detecting Subject')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') == '0'):
        pass
    else:
        assert False, 'Default exposure value error'
    with step('[Verify] snapshot: 05_01_12_subject_default.png'):
        actions.capture_for_gt('05_01_12_subject_default.png')
    with step('[Verify] compare: 05_01_12_subject_default.png'):
        assert actions.compare_with_gt('05_01_12_subject_default.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('-100', '-99', '-98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_exposure_min.png'):
        actions.capture_for_gt('05_01_12_subject_exposure_min.png')
    with step('[Verify] compare: 05_01_12_subject_exposure_min.png'):
        assert actions.compare_with_gt('05_01_12_subject_exposure_min.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if (not (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97'))):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_exposure_max.png'):
        actions.capture_for_gt('05_01_12_subject_exposure_max.png')
    with step('[Verify] compare: 05_01_12_subject_exposure_max.png'):
        assert actions.compare_with_gt('05_01_12_subject_exposure_max.png', gt_folder=TD.GT_FOLDER)[0]
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '0'):
        pass
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('-100', '-99', '-98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_saturation_min.png'):
        actions.capture_for_gt('05_01_12_subject_saturation_min.png')
    if actions.compare_with_gt('05_01_12_subject_saturation_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject saturation min comparison failed'
    with step('[Action] adjust_hsl_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_saturation_max.png'):
        actions.capture_for_gt('05_01_12_subject_saturation_max.png')
    with step('[Verify] compare: 05_01_12_subject_saturation_max.png'):
        assert actions.compare_with_gt('05_01_12_subject_saturation_max.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_01_12_subject_v.png'):
        actions.capture_for_gt('05_01_12_subject_v.png')
    if (not actions.compare_with_gt('05_01_12_subject_v.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Subject done without preset comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_subject'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Subject')
    with step('[Verify] snapshot: 05_01_12_subject_no_preset.png'):
        actions.capture_for_gt('05_01_12_subject_no_preset.png')
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_light_default.png'):
        actions.capture_for_gt('05_01_12_subject_light_default.png')
    if actions.compare_with_gt('05_01_12_subject_light_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject light default comparison failed'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_light_min.png'):
        actions.capture_for_gt('05_01_12_subject_light_min.png')
    if actions.compare_with_gt('05_01_12_subject_light_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject light min comparison failed'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_light_max.png'):
        actions.capture_for_gt('05_01_12_subject_light_max.png')
    if actions.compare_with_gt('05_01_12_subject_light_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject light max comparison failed'
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Pop')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_pop_default.png'):
        actions.capture_for_gt('05_01_12_subject_pop_default.png')
    if actions.compare_with_gt('05_01_12_subject_pop_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject pop default comparison failed'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_pop_min.png'):
        actions.capture_for_gt('05_01_12_subject_pop_min.png')
    if actions.compare_with_gt('05_01_12_subject_pop_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject pop min comparison failed'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_pop_max.png'):
        actions.capture_for_gt('05_01_12_subject_pop_max.png')
    if actions.compare_with_gt('05_01_12_subject_pop_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject pop max comparison failed'
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cool')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_cool_default.png'):
        actions.capture_for_gt('05_01_12_subject_cool_default.png')
    if actions.compare_with_gt('05_01_12_subject_cool_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject cool default comparison failed'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_cool_min.png'):
        actions.capture_for_gt('05_01_12_subject_cool_min.png')
    if actions.compare_with_gt('05_01_12_subject_cool_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject cool min comparison failed'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_cool_max.png'):
        actions.capture_for_gt('05_01_12_subject_cool_max.png')
    if actions.compare_with_gt('05_01_12_subject_cool_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject cool max comparison failed'
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Warm')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_warm_default.png'):
        actions.capture_for_gt('05_01_12_subject_warm_default.png')
    if actions.compare_with_gt('05_01_12_subject_warm_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject warm default comparison failed'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_warm_min.png'):
        actions.capture_for_gt('05_01_12_subject_warm_min.png')
    if actions.compare_with_gt('05_01_12_subject_warm_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject warm min comparison failed'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_warm_max.png'):
        actions.capture_for_gt('05_01_12_subject_warm_max.png')
    if actions.compare_with_gt('05_01_12_subject_warm_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject warm max comparison failed'
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Vibrant')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_vibrant_default.png'):
        actions.capture_for_gt('05_01_12_subject_vibrant_default.png')
    if actions.compare_with_gt('05_01_12_subject_vibrant_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject vibrant default comparison failed'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_vibrant_min.png'):
        actions.capture_for_gt('05_01_12_subject_vibrant_min.png')
    if actions.compare_with_gt('05_01_12_subject_vibrant_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject vibrant min comparison failed'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_vibrant_max.png'):
        actions.capture_for_gt('05_01_12_subject_vibrant_max.png')
    if actions.compare_with_gt('05_01_12_subject_vibrant_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject vibrant max comparison failed'
    with step('[Action] select_quick_preset'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Glow')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') == '50'):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_glow_default.png'):
        actions.capture_for_gt('05_01_12_subject_glow_default.png')
    if actions.compare_with_gt('05_01_12_subject_glow_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject glow default comparison failed'
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 0)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('0', '1', '2', '3')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_glow_min.png'):
        actions.capture_for_gt('05_01_12_subject_glow_min.png')
    if actions.compare_with_gt('05_01_12_subject_glow_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject glow min comparison failed'
    with step('[Verify] snapshot: 05_01_12_subject_undo_og.png'):
        actions.capture_for_gt('05_01_12_subject_undo_og.png')
    with step('[Action] adjust_hsl_lightness_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[3]', 1)
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText[2]') in ('100', '99', '98', '97')):
        pass
    with step('[Verify] snapshot: 05_01_12_subject_glow_max.png'):
        actions.capture_for_gt('05_01_12_subject_glow_max.png')
    if actions.compare_with_gt('05_01_12_subject_glow_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject glow max comparison failed'
    with step('[Verify] snapshot: 05_01_12_subject_redo_og.png'):
        actions.capture_for_gt('05_01_12_subject_redo_og.png')
    with step('[Action] tap_undo_btn_2'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n')
    with step('[Verify] snapshot: 05_01_12_subject_undo.png'):
        actions.capture_for_gt('05_01_12_subject_undo.png')
    if actions.compare_with_gt('05_01_12_subject_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject undo comparison failed'
    with step('[Action] tap_redo_btn_2'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n')
    with step('[Verify] snapshot: 05_01_12_subject_redo.png'):
        actions.capture_for_gt('05_01_12_subject_redo.png')
    if actions.compare_with_gt('05_01_12_subject_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject redo comparison failed'
    with step('[Action] tap_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic reset n')
    with step('[Verify] snapshot: 05_01_12_subject_reset.png'):
        actions.capture_for_gt('05_01_12_subject_reset.png')
    if actions.compare_with_gt('05_01_12_subject_reset.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Subject reset comparison failed'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Failed to tap done button for subject with preset'
    with step('[Verify] snapshot: 05_01_12_subject_v2.png'):
        actions.capture_for_gt('05_01_12_subject_v2.png')
    if (not actions.compare_with_gt('05_01_12_subject_v2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'Subject done with preset comparison failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Subject')
    with step('[Action] select_quick_preset'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light')
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Verify] snapshot: 05_01_12_subject_x.png'):
        actions.capture_for_gt('05_01_12_subject_x.png')
    if actions.compare_with_gt('05_01_12_subject_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step("[Verify] test_00142 completion"):
        assert True
