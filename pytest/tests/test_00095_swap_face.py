import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00095_swap_face')
def test_00095_swap_face(actions: DriverActions):
    """swap face"""
    mode = 1
    uuid = ['ee9268fe-ec61-4bbd-98a9-795c40108c6b', '98386bdf-064b-4ad1-bec2-9cf7fd268d7c', '7fa07c90-eb6d-486b-a579-53427aff8d64', 'f545ed7e-311d-478c-a796-696ebb99d3d9', '6fa9ab2f-ec1d-4c33-9319-f28e2d250325', 'bfb46bae-414c-4e88-8939-2d8b75ba2eb2', '7abddee5-d6a4-466b-b11d-6e26961051f7', '096733a3-d9be-46c3-aa81-4e7d3c416521', '7beb4186-cec5-437b-a2ec-29e7c93e2b45', '77e987d5-7171-428e-b7ec-fd3bebfe1669', 'e63e9f5e-f214-4189-b231-819ae48bba2b', '74dcb886-82c8-40ca-9c28-9f2c7a096b6e', '07422ec4-dc6d-4418-9219-7cb6fb5cadf9', '76881829-6d3a-46d0-8847-aecabcea1037', '173dd452-44a5-4f27-9a37-72708cafde9f', 'e1d37f72-3fa9-4282-aad5-ece3fb81f549', '43491cf7-3fe7-447c-a4aa-461e7ca66a80', '56bcee30-0bc6-4763-913c-5d81127072c9', 'fcb6e13d-fb39-4b83-9ddd-832717efcc49', '440c57bd-e8be-42da-8a26-e1e142bd2fb7', 'cc6433dd-8c70-4058-a058-d39c32e6e5ad', '03c502a7-a7d6-4c33-adfb-9feb8ee067e0', 'fcb6e13d-fb39-4b83-9ddd-832717efcc49', '440c57bd-e8be-42da-8a26-e1e142bd2fb7', 'cc6433dd-8c70-4058-a058-d39c32e6e5ad', '03c502a7-a7d6-4c33-adfb-9feb8ee067e0', '71c8f57f-655e-42eb-9a1d-2ab92aecec1e', '90571bc1-a599-4376-b51e-bc1518d9ba24', 'ff0f9a04-a555-4c30-8203-88ed7ccd81e4', '7ecd9620-2075-4b6f-8ab8-605c0fad01ac']
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Makeup')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Lipstick')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dried Rose 01')
    with step('[Verify] snapshot: 05_07_00_makeup_face1.png'):
        actions.capture_for_gt('05_07_00_makeup_face1.png')
    if actions.compare_with_gt('05_07_00_makeup_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'makeup face 1 fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[2]')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dried Rose 01')
    with step('[Verify] snapshot: 05_07_00_makeup_face2.png'):
        actions.capture_for_gt('05_07_00_makeup_face2.png')
    if actions.compare_with_gt('05_07_00_makeup_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'makeup face 2 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_auto_retouch_face1.png'):
        actions.capture_for_gt('05_07_00_auto_retouch_face1.png')
    if actions.compare_with_gt('05_07_00_auto_retouch_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'auto retouch face 1 fail'
    pos = (100, 90)
    with step('[Action] tap'):
        actions.tap_by_coordinates(100, 90)
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_auto_retouch_face2.png'):
        actions.capture_for_gt('05_07_00_auto_retouch_face2.png')
    if actions.compare_with_gt('05_07_00_auto_retouch_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'auto retouch face 2 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Jawline')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_jawline_face1.png'):
        actions.capture_for_gt('05_07_00_jawline_face1.png')
    if actions.compare_with_gt('05_07_00_jawline_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'jawline face 1 fail'
    with step('[Action] tap'):
        actions.tap_by_coordinates(tuple(pos)[0], tuple(pos)[1])
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_jawline_face2.png'):
        actions.capture_for_gt('05_07_00_jawline_face2.png')
    if actions.compare_with_gt('05_07_00_jawline_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'jawline face 2 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Reshape')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Action] tap_face'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Face')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_07_00_reshape_face1.png'):
        actions.capture_for_gt('05_07_00_reshape_face1.png')
    if actions.compare_with_gt('05_07_00_reshape_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'reshape face 1 fail'
    with step('[Action] tap'):
        actions.tap_by_coordinates(tuple(pos)[0], tuple(pos)[1])
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: 05_07_00_reshape_face2.png'):
        actions.capture_for_gt('05_07_00_reshape_face2.png')
    if actions.compare_with_gt('05_07_00_reshape_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'reshape face 2 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Conceal')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    with step('[Action] tap'):
        actions.tap_by_coordinates(40, 100)
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_conceal_face1.png'):
        actions.capture_for_gt('05_07_00_conceal_face1.png')
    if actions.compare_with_gt('05_07_00_conceal_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'conceal face 1 fail'
    with step('[Action] tap'):
        actions.tap_by_coordinates(tuple(pos)[0], tuple(pos)[1])
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_conceal_face2.png'):
        actions.capture_for_gt('05_07_00_conceal_face2.png')
    if actions.compare_with_gt('05_07_00_conceal_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'conceal face 2 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    from_pos = (400, 780)
    destination = (10, 780)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 780, 10, 780)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Plumpness')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_plumpness_face1.png'):
        actions.capture_for_gt('05_07_00_plumpness_face1.png')
    if actions.compare_with_gt('05_07_00_plumpness_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'plumpness face 1 fail'
    with step('[Action] tap'):
        actions.tap_by_coordinates(tuple(pos)[0], tuple(pos)[1])
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_plumpness_face2.png'):
        actions.capture_for_gt('05_07_00_plumpness_face2.png')
    if actions.compare_with_gt('05_07_00_plumpness_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'plumpness face 2 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    from_pos = (10, 780)
    destination = (300, 780)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(10, 780, 300, 780)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Smooth')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Auto')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_facesmoothener_face1.png'):
        actions.capture_for_gt('05_07_00_facesmoothener_face1.png')
    if actions.compare_with_gt('05_07_00_facesmoothener_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'facesmoothener face 1 fail'
    with step('[Action] tap'):
        actions.tap_by_coordinates(tuple(pos)[0], tuple(pos)[1])
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_facesmoothener_face2.png'):
        actions.capture_for_gt('05_07_00_facesmoothener_face2.png')
    if actions.compare_with_gt('05_07_00_facesmoothener_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'facesmoothener face 2 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Wrinkle')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_wrinkle_face1.png'):
        actions.capture_for_gt('05_07_00_wrinkle_face1.png')
    if actions.compare_with_gt('05_07_00_wrinkle_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'wrinkle face 1 fail'
    with step('[Action] tap'):
        actions.tap_by_coordinates(tuple(pos)[0], tuple(pos)[1])
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_wrinkle_face2.png'):
        actions.capture_for_gt('05_07_00_wrinkle_face2.png')
    if actions.compare_with_gt('05_07_00_wrinkle_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'wrinkle face 2 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blemish')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Verify] snapshot: 05_07_00_blemish_face1.png'):
        actions.capture_for_gt('05_07_00_blemish_face1.png')
    if actions.compare_with_gt('05_07_00_blemish_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'blemish face 1 fail'
    with step('[Action] tap'):
        actions.tap_by_coordinates(tuple(pos)[0], tuple(pos)[1])
    with step('[Verify] snapshot: 05_07_00_blemish_face2.png'):
        actions.capture_for_gt('05_07_00_blemish_face2.png')
    if actions.compare_with_gt('05_07_00_blemish_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'blemish face 2 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    from_pos = (400, 780)
    destination = (250, 780)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(400, 780, 250, 780)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Teeth Whiten')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_teethwhiten_face1.png'):
        actions.capture_for_gt('05_07_00_teethwhiten_face1.png')
    if actions.compare_with_gt('05_07_00_teethwhiten_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'teethwhiten face 1 fail'
    with step('[Action] tap'):
        actions.tap_by_coordinates(tuple(pos)[0], tuple(pos)[1])
    with step('[Verify] snapshot: 05_07_00_teethwhiten_face2.png'):
        actions.capture_for_gt('05_07_00_teethwhiten_face2.png')
    if actions.compare_with_gt('05_07_00_teethwhiten_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'teethwhiten face 2 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Brighten')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_eyebrighten_face1.png'):
        actions.capture_for_gt('05_07_00_eyebrighten_face1.png')
    if actions.compare_with_gt('05_07_00_eyebrighten_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'eyebrighten face 1 fail'
    with step('[Action] tap'):
        actions.tap_by_coordinates(tuple(pos)[0], tuple(pos)[1])
    with step('[Verify] snapshot: 05_07_00_eyebrighten_face2.png'):
        actions.capture_for_gt('05_07_00_eyebrighten_face2.png')
    if actions.compare_with_gt('05_07_00_eyebrighten_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'eyebrighten face 2 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Bags')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_eyebag_face1.png'):
        actions.capture_for_gt('05_07_00_eyebag_face1.png')
    if actions.compare_with_gt('05_07_00_eyebag_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'eyebag face 1 fail'
    with step('[Action] tap'):
        actions.tap_by_coordinates(tuple(pos)[0], tuple(pos)[1])
    with step('[Verify] snapshot: 05_07_00_eyebag_face2.png'):
        actions.capture_for_gt('05_07_00_eyebag_face2.png')
    if actions.compare_with_gt('05_07_00_eyebag_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'eyebag face 2 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    from_pos = (20, 780)
    destination = (300, 780)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(20, 780, 300, 780)
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Oiliness')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_oiliness_face1.png'):
        actions.capture_for_gt('05_07_00_oiliness_face1.png')
    if actions.compare_with_gt('05_07_00_oiliness_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'oiliness face 1 fail'
    with step('[Action] tap'):
        actions.tap_by_coordinates(tuple(pos)[0], tuple(pos)[1])
    with step('[Verify] snapshot: 05_07_00_oiliness_face2.png'):
        actions.capture_for_gt('05_07_00_oiliness_face2.png')
    if actions.compare_with_gt('05_07_00_oiliness_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'oiliness face 2 fail'
    with step('[Action] tap_feature_x_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Retouch')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Nose Enhance')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]')
    with step('[Action] adjust_harmonization_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_07_00_nose_face1.png'):
        actions.capture_for_gt('05_07_00_nose_face1.png')
    if actions.compare_with_gt('05_07_00_nose_face1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'nose face 1 fail'
    with step('[Action] tap'):
        actions.tap_by_coordinates(tuple(pos)[0], tuple(pos)[1])
    with step('[Verify] snapshot: 05_07_00_nose_face2.png'):
        actions.capture_for_gt('05_07_00_nose_face2.png')
    if actions.compare_with_gt('05_07_00_nose_face2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'nose face 2 fail'
    with step("[Verify] test_00095 completion"):
        assert True
