import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00086_main_05_07_18_1')
def test_00086_main_05_07_18_1(actions: DriverActions):
    """plumpness, have face"""
    mode = 1
    uuid = ['d76ea58f-c2e9-4d8f-a37e-5de0da6de867', '84bec159-c98a-4838-89a9-10930400825e', '76818139-4960-46d4-ba27-2a538b733d1d', 'c5a8b23d-e959-4413-9589-94d5b6642cef', 'a0016f07-b13d-401f-a6de-19b2df5ac043', '1b250e6b-9dfc-4ef4-b642-301a80bffcf0', '176c7916-71ac-471a-a7ad-0bfc4f0cf336', 'a82009c0-32a5-4d13-b2cd-be5e0523bca3', '3e652a89-6842-4885-bf7e-93c0d91c8283', 'ff4b5aeb-b746-46fc-8f0e-abc8193259ab', '8367a482-68a3-40e8-aa7a-df598df7d40d', '8a61c4cc-e949-4421-9064-145f5e649de5', 'e8976af3-a91b-499f-bbce-fd0f54bd2831', '6fe079d1-b9f6-41e6-981c-ce7998351968', 'dc148eef-f172-41d6-8225-4b034b2a16d0', '2a6943a1-68d0-4e96-b431-bdf71b04f5c6', 'a0ab7117-d6f1-4479-b1df-ebb55c41ad33', 'ca9dfadb-2003-41b9-a702-5ee29aa997c9', '48958959-2b1c-43ea-989b-edb037fef109', '0c061d53-ca60-44b9-81c7-1a250f304bc5', 'e52dd6a6-62fc-4e75-9f5a-ea0da0213692', '8a0d995f-e89c-485a-8d4e-9809ac144e2d', '49f96ac2-2587-4505-8b70-e7d104d8cf90', '0b82d0e7-341c-4dc8-b40b-9118b2f1f056', '24a0f9fa-2e1d-421d-a044-723a96b79187', '6227f8af-6983-4ad1-a75c-ac887b4f0abf', '7b1c12b4-a109-4dcc-a32d-a58e174cf8d5', '3b186105-45cc-4643-a014-4cb86a556859', '081649fd-809e-46f1-a72a-f6993321ee4e', '2fbf93db-2ebc-4f8c-ab1b-d38ce5cc7e9f', '0247a04e-2a92-49ec-99ad-ee894177e334', '154ddfe3-1cc2-4dbe-99cd-a9ec23c7c812', 'effb1bdd-742c-49f4-b8b6-53c6176a7b3c', '08411352-ae5a-4a2d-96a3-2e4cfe8455f3', 'f4c3ec72-0920-44c6-9cf6-5759f97aa8fe', 'f7815ccb-c88a-4da4-b991-7ccea10c52c3', '63e05e48-7084-4f7f-9cc3-7c17c03e680c', '05920ff4-bf1d-4058-aedf-fe81d7c9a38c', '3f865c3b-e2a4-4730-acb6-add8115cae07', '37a5225e-4b49-4384-a69c-e8164ebfc0d2', '353296ed-9898-44c1-b60b-ecfafed9793d', '388eb35b-5a39-4fea-aff8-a6214bafb209', '68bd792d-59de-451d-b66e-93143c0718c1', '28f369a2-22f5-4d36-8be7-cc2a7001b706', '31b062ea-8854-49ee-8106-0bdadb7055e1', '9624c26a-4940-40b3-8cc3-78d7176d708e', 'b1be30a3-bd82-4037-ac00-7520b88d3ed7', '908b0849-d20a-4132-a19b-44a96ddaa3f8', 'e19fbfcd-64e9-41ca-95e4-4fef3fdc76ba', 'a592d895-3fdb-4ed7-a1ab-741b7af1b090', 'ab862fba-cebf-4c09-bbf6-afde4db2c4d2', '7f0fad9f-b2eb-4299-b933-a5cae49f4fc0', '0f35e35c-2db1-4605-9887-8399a3e7a262', 'a7b3038b-43fd-4889-89da-4ec34d53fb4f', '8405f529-1c05-4f89-9753-cd6b2879620b', '20839b7d-bf1d-46aa-98a4-a5ee8871fdab', '7e3ce3b7-0e8b-4c1e-adf8-3cceb8e699e5', '64a17541-5b2b-47c5-80e0-8ae8a3cd2636']
    with step('[Action] close_continue_edit'):
        actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.wait_for_invisible(AppiumBy.NAME, 'Would you like to continue editing?')
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
    from_pos = (400, 780)
    destination = (10, 780)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 780, 10, 780)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Plumpness')
    with step('[Verify] snapshot: base05_07_18_default_auto_on.png'):
        actions.capture_for_gt('base05_07_18_default_auto_on.png')
    if actions.compare_with_gt('05_07_18_default_auto_on.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'default auto on fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step('[Verify] snapshot: 05_07_18_auto_off.png'):
        actions.capture_for_gt('05_07_18_auto_off.png')
    if actions.compare_with_gt('05_07_18_auto_off.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'auto off fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') == '50'):
        pass
    else:
        assert False, 'Default value verification failed'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_18_auto_off2.png'):
        actions.capture_for_gt('05_07_18_auto_off2.png')
    if actions.compare_with_gt('05_07_18_auto_off2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'auto off by slider fail'
    with step('[Verify] snapshot: base05_07_18_forehead_slider_min.png'):
        actions.capture_for_gt('base05_07_18_forehead_slider_min.png')
    if actions.compare_with_gt('05_07_18_forehead_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_18_forehead_slider_max.png'):
        actions.capture_for_gt('05_07_18_forehead_slider_max.png')
    if actions.compare_with_gt('05_07_18_forehead_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Tear Trough')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') == '80'):
        pass
    else:
        assert False, 'Default value verification failed'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_18_teartrough_slider_min.png'):
        actions.capture_for_gt('05_07_18_teartrough_slider_min.png')
    if actions.compare_with_gt('05_07_18_teartrough_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: base05_07_18_teartrough_slider_max.png'):
        actions.capture_for_gt('base05_07_18_teartrough_slider_max.png')
    if actions.compare_with_gt('05_07_18_teartrough_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cheek Apples')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') == '75'):
        pass
    else:
        assert False, 'Default value verification failed'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_18_cheek_apples_slider_min.png'):
        actions.capture_for_gt('05_07_18_cheek_apples_slider_min.png')
    if actions.compare_with_gt('05_07_18_cheek_apples_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_18_cheek_apples_slider_max.png'):
        actions.capture_for_gt('05_07_18_cheek_apples_slider_max.png')
    if actions.compare_with_gt('05_07_18_cheek_apples_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cheeks')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') == '45'):
        pass
    else:
        assert False, 'default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_18_cheeks_slider_min.png'):
        actions.capture_for_gt('05_07_18_cheeks_slider_min.png')
    if actions.compare_with_gt('05_07_18_cheeks_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_18_cheeks_slider_max.png'):
        actions.capture_for_gt('05_07_18_cheeks_slider_max.png')
    if actions.compare_with_gt('05_07_18_cheeks_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Nasal Base')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') == '75'):
        pass
    else:
        assert False, 'Default value verification failed'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_18_nasalbase_slider_min.png'):
        actions.capture_for_gt('05_07_18_nasalbase_slider_min.png')
    if actions.compare_with_gt('05_07_18_nasalbase_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_18_nasalbase_slider_max.png'):
        actions.capture_for_gt('05_07_18_nasalbase_slider_max.png')
    if actions.compare_with_gt('05_07_18_nasalbase_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Smile')
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
    with step('[Verify] snapshot: 05_07_18_eyesmile_slider_min.png'):
        actions.capture_for_gt('05_07_18_eyesmile_slider_min.png')
    if actions.compare_with_gt('05_07_18_eyesmile_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_18_eyesmile_slider_max.png'):
        actions.capture_for_gt('05_07_18_eyesmile_slider_max.png')
    if actions.compare_with_gt('05_07_18_eyesmile_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Sockets')
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
    with step('[Verify] snapshot: 05_07_18_eyesockets_slider_min.png'):
        actions.capture_for_gt('05_07_18_eyesockets_slider_min.png')
    if actions.compare_with_gt('05_07_18_eyesockets_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_18_eyesockets_slider_max.png'):
        actions.capture_for_gt('05_07_18_eyesockets_slider_max.png')
    if actions.compare_with_gt('05_07_18_eyesockets_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eyebrow Arch')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') == '30'):
        pass
    else:
        assert False, 'default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_18_eyebrow_arch_slider_min.png'):
        actions.capture_for_gt('05_07_18_eyebrow_arch_slider_min.png')
    if actions.compare_with_gt('05_07_18_eyebrow_arch_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_18_eyebrow_arch_slider_max.png'):
        actions.capture_for_gt('05_07_18_eyebrow_arch_slider_max.png')
    if actions.compare_with_gt('05_07_18_eyebrow_arch_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Chin')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') == '60'):
        pass
    else:
        assert False, 'default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_18_chin_slider_min.png'):
        actions.capture_for_gt('05_07_18_chin_slider_min.png')
    if actions.compare_with_gt('05_07_18_chin_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_18_chin_slider_max.png'):
        actions.capture_for_gt('05_07_18_chin_slider_max.png')
    if actions.compare_with_gt('05_07_18_chin_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mouth Corner')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') == '70'):
        pass
    else:
        assert False, 'default value fail'
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('0', '1', '2', '3', '4')):
        pass
    else:
        assert False, 'min value fail'
    with step('[Verify] snapshot: 05_07_18_mouth_corner_slider_min.png'):
        actions.capture_for_gt('05_07_18_mouth_corner_slider_min.png')
    if actions.compare_with_gt('05_07_18_mouth_corner_slider_min.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider left fail'
    with step('[Verify] snapshot: 05_07_18_undo_og.png'):
        actions.capture_for_gt('05_07_18_undo_og.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'max value fail'
    with step('[Verify] snapshot: 05_07_18_mouth_corner_slider_max.png'):
        actions.capture_for_gt('05_07_18_mouth_corner_slider_max.png')
    if actions.compare_with_gt('05_07_18_mouth_corner_slider_max.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'slider right fail'
    with step('[Verify] snapshot: 05_07_18_before_undo.png'):
        actions.capture_for_gt('05_07_18_before_undo.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_18_undo.png'):
        actions.capture_for_gt('05_07_18_undo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_18_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo comparison fail'
    with step('[Action] tap_redo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: 05_07_18_redo.png'):
        actions.capture_for_gt('05_07_18_redo.png', crop_rect=(0, 60, 276, 526))
    if actions.compare_with_gt('05_07_18_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo comparison fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'tap done button fail'
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, '[v] verification fail'
    with step("[Verify] test_00086 completion"):
        assert True
