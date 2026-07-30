import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00088_makeup_with_face')
def test_00088_makeup_with_face(actions: DriverActions):
    """makeup, have face"""
    mode = 1
    uuid = ['9ef85aa9-b473-48a7-a764-7d01aafa365e', '579c2c06-d0d2-49eb-9578-accb8c633c95', 'ba8c67cf-2e0e-43db-a510-82591a2d4188', '0113f4a1-520c-41ab-bb40-54fa16001b03', '97e5435d-6058-4aaf-90bc-105fb4b3cd13', '97072d03-0550-4d90-94e0-0057ab77bfc4', '81a89621-8e00-42e6-94e3-2c234b276466', '4b197492-f524-4619-a1c8-49ff94a168de', '49427266-d621-46ce-b623-cd18a437fef1', '1804952c-c961-4f6d-8100-8f6836d0bee7', '39424814-2f22-4390-ab21-734329576ed6', 'f0d65e85-c281-4c76-a0de-6d56f4150342', '988fc2af-9691-4c90-85ef-e306eceefb34', '024d0924-1a36-48e1-a4ad-c2e14d06cb41', 'a97e1246-0c14-4c55-bc82-a1b086e51b8c', '6db12f32-e44d-4246-a181-4b1345e7e390', '52226eef-e00a-48d9-8c5b-42e62b18f7f2', '7dd80947-fbce-4f6a-9890-7940b6ce1ba0', '8c6e727a-506e-4bc0-811d-33479d96cf9e', 'b01c4246-b896-42a4-b214-c991350aae3a', 'a074d05a-3465-40e5-a300-87a0c02a6878', 'ea649442-8c51-4c02-aa56-a644c807d796', '849e614a-fc91-4f85-9646-c689943bbfb4', '5145826c-7d00-4935-af8b-34cf2796179a', 'dcecd7f2-de69-4e2b-889d-de7af540b398', '5def12c2-3f8a-4265-83c8-c9ff638bfc3a', '3bc1d3e0-fe0e-4ada-9add-bccd482649d1', '25f7c855-56ea-4265-9c52-21b9f103805b', 'd516421b-ff32-42c2-b50e-c28af745c8b8', '4134db55-66ce-4033-8f65-3081b551cbdd', '75a388c4-8a59-4b72-bb58-51adc3bd768b', '89adc1af-d6b9-4ec6-b324-9e36e384cef1', 'a7bb87e8-1111-4868-b78a-67e301eca22f', '5b23b80d-b025-4e11-adf5-da943d7ff3ea', 'fdf372e3-57e9-4d28-b814-59853b069ea5', '1aa7c231-7275-4e4e-b065-eae01ae07752', '85cf0d01-7a16-4ea1-97a1-d0c61001d6a2', '4c75a3c3-7618-443b-9952-4e8c66f51faa', '7a10aeb9-099d-40f9-9a54-d6881029b623', '3110032e-30a0-4038-96d5-0a2b9daf9761', 'ab026cc1-4112-439e-a930-f7613f645339', '75d7d747-454c-4ea7-8eb9-0f40823e74c2', '76f97ad2-3fb7-4c31-97e5-4e7a706d3025', '3c416969-993c-4b25-991c-a84e312b2265', '914f78aa-1d61-486b-95ce-100db8f97912', '01895b31-6603-4078-967a-4bf7272815a6', '763031e0-4024-4211-9a49-49f1471156ae', 'b2637d53-f9af-4d82-b773-df92bbaae4ef', 'acee9950-4a47-4378-a137-5b82624666b5', '42ef14b6-8165-4da1-a438-5be5baeb30fd', '1959e740-2871-4f3d-b377-f5bd771c1fbd', '30f53a42-a02a-465f-ad8a-4b61bddbdd6b', 'f94c7f12-656b-4ffe-a5e4-502cec528307', 'a9370f3e-1e12-4596-b597-30352388a139', '11512a37-a345-4c9c-bc42-5e26bb4b72d7', 'd4e8dad4-d7d2-45c3-aa95-823db7d0cc56', 'badded11-3729-4bfb-ab52-dd88172be500', '924763d4-73e7-47c7-9556-1909d74b3fca']
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
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Makeup')
    with step('[Verify] snapshot: 05_07_19_enter_makeup.png'):
        actions.capture_for_gt('05_07_19_enter_makeup.png')
    with step('[Verify] snapshot: 05_07_19_enter_makeup2.png'):
        actions.capture_for_gt('05_07_19_enter_makeup2.png')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lipstick')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dried Rose 01')
    with step('[Verify] snapshot: 05_07_19_lipstick_debug.png'):
        actions.capture_for_gt('05_07_19_lipstick_debug.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]')
    with step('[Verify] snapshot: 05_07_19_lipsticker.png'):
        actions.capture_for_gt('05_07_19_lipsticker.png')
    if actions.compare_with_gt('05_07_19_lipsticker.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'lipsticker comparison fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') == '50'):
        pass
    else:
        assert False, 'default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_19_lipstick_slider_min.png'):
        actions.capture_for_gt('05_07_19_lipstick_slider_min.png')
    if actions.compare_with_gt('05_07_19_lipstick_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_19_lipstick_slider_max.png'):
        actions.capture_for_gt('05_07_19_lipstick_slider_max.png')
    if actions.compare_with_gt('05_07_19_lipstick_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Contour')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Highlight')
    with step('[Verify] snapshot: 05_07_19_contour.png'):
        actions.capture_for_gt('05_07_19_contour.png')
    if actions.compare_with_gt('05_07_19_contour.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'contour-1 comparison fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') == '75'):
        pass
    else:
        assert False, 'default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_19_contour_slider_min.png'):
        actions.capture_for_gt('05_07_19_contour_slider_min.png')
    if actions.compare_with_gt('05_07_19_contour_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_19_contour_slider_max.png'):
        actions.capture_for_gt('05_07_19_contour_slider_max.png')
    if actions.compare_with_gt('05_07_19_contour_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyelashes')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[6]')
    with step('[Verify] snapshot: 05_07_19_eyelashes.png'):
        actions.capture_for_gt('05_07_19_eyelashes.png')
    if actions.compare_with_gt('05_07_19_eyelashes.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'eyelashes comparison fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') == '50'):
        pass
    else:
        assert False, 'default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_19_eyelashes_slider_min.png'):
        actions.capture_for_gt('05_07_19_eyelashes_slider_min.png')
    if actions.compare_with_gt('05_07_19_eyelashes_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_19_eyelashes_slider_max.png'):
        actions.capture_for_gt('05_07_19_eyelashes_slider_max.png')
    if actions.compare_with_gt('05_07_19_eyelashes_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyebrows')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[6]')
    with step('[Verify] snapshot: 05_07_19_eyebrows.png'):
        actions.capture_for_gt('05_07_19_eyebrows.png')
    if actions.compare_with_gt('05_07_19_eyebrows.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'eyebrows comparison fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') == '50'):
        pass
    else:
        assert False, 'default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_19_eyebrows_slider_min.png'):
        actions.capture_for_gt('05_07_19_eyebrows_slider_min.png')
    if actions.compare_with_gt('05_07_19_eyebrows_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_19_eyebrows_slider_max.png'):
        actions.capture_for_gt('05_07_19_eyebrows_slider_max.png')
    if actions.compare_with_gt('05_07_19_eyebrows_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyeliner')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[6]')
    with step('[Verify] snapshot: 05_07_19_eyeliner.png'):
        actions.capture_for_gt('05_07_19_eyeliner.png')
    if actions.compare_with_gt('05_07_19_eyeliner.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'eyeliner comparison fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') == '50'):
        pass
    else:
        assert False, 'default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_19_eyeliner_slider_min.png'):
        actions.capture_for_gt('05_07_19_eyeliner_slider_min.png')
    if actions.compare_with_gt('05_07_19_eyeliner_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_19_eyeliner_slider_max.png'):
        actions.capture_for_gt('05_07_19_eyeliner_slider_max.png')
    if actions.compare_with_gt('05_07_19_eyeliner_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Shadow')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Daily')
    with step('[Verify] snapshot: 05_07_19_eyeshadow.png'):
        actions.capture_for_gt('05_07_19_eyeshadow.png')
    if actions.compare_with_gt('05_07_19_eyeshadow.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'eyeshadow comparison fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') == '50'):
        pass
    else:
        assert False, 'default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_19_eyeshadow_slider_min.png'):
        actions.capture_for_gt('05_07_19_eyeshadow_slider_min.png')
    if actions.compare_with_gt('05_07_19_eyeshadow_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_19_eyeshadow_slider_max.png'):
        actions.capture_for_gt('05_07_19_eyeshadow_slider_max.png')
    if actions.compare_with_gt('05_07_19_eyeshadow_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Blush')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Natural')
    with step('[Verify] snapshot: 05_07_19_blush.png'):
        actions.capture_for_gt('05_07_19_blush.png')
    if actions.compare_with_gt('05_07_19_blush.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'blush comparison fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') == '80'):
        pass
    else:
        assert False, 'default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_19_blush_slider_min.png'):
        actions.capture_for_gt('05_07_19_blush_slider_min.png')
    if actions.compare_with_gt('05_07_19_blush_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_19_blush_slider_max.png'):
        actions.capture_for_gt('05_07_19_blush_slider_max.png')
    if actions.compare_with_gt('05_07_19_blush_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Verify] snapshot: 05_07_19_before_undo.png'):
        actions.capture_for_gt('05_07_19_before_undo.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Foundation')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'White 01')
    with step('[Verify] snapshot: 05_07_19_foundation.png'):
        actions.capture_for_gt('05_07_19_foundation.png')
    if actions.compare_with_gt('05_07_19_foundation.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'foundation comparison fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') == '50'):
        pass
    else:
        assert False, 'default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_19_foundation_slider_min.png'):
        actions.capture_for_gt('05_07_19_foundation_slider_min.png')
    if actions.compare_with_gt('05_07_19_foundation_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Verify] snapshot: 05_07_19_undo_og.png'):
        actions.capture_for_gt('05_07_19_undo_og.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_19_foundation_slider_max.png'):
        actions.capture_for_gt('05_07_19_foundation_slider_max.png')
    if actions.compare_with_gt('05_07_19_foundation_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Verify] snapshot: 05_07_19_before_undo.png'):
        actions.capture_for_gt('05_07_19_before_undo.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_19_undo.png'):
        actions.capture_for_gt('05_07_19_undo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_19_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo comparison fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_19_redo.png'):
        actions.capture_for_gt('05_07_19_redo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_19_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo comparison fail'
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_19_[v].png'):
        actions.capture_for_gt('05_07_19_[v].png')
    if actions.compare_with_gt('05_07_19_[v].png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[v] comparison fail'
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00088 completion"):
        assert True
