import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00138_main_05_14_01')
def test_00138_main_05_14_01(actions: DriverActions):
    """Live - dispersion"""
    mode = 1
    uuid = ['c9670047-7b30-49ee-94a6-aa3244ce0e00', '54c50d77-f5af-4087-8681-fa64569f7051', '82b038e0-6313-458e-bdde-9bf681c665aa', 'c5f9fe5b-6032-481e-beaa-4b3cefe34067', 'e232b940-2fac-4e3d-80ca-bd1e64861c9e', '43374901-04ea-4781-bb4a-406adefa249f', '07f943d7-a85e-4ef5-9982-1ae998a1fa65', 'a084c85e-e6b6-4664-bf68-e3ed75018f73', '807a7c0e-6d9a-4172-bd34-d0aa39420b03', 'b6133ee0-70e6-4f13-89b3-1da7fd854ef9', 'db514658-72c2-43b5-ad29-40564e8773cd', '65f36e2f-0209-44eb-a882-8729ba0fe735', 'cc2cd90e-fe04-4201-a266-16c4966aa5a5', '0591ef73-322c-4a65-b582-8e230ea98d5b', '87588153-4a2d-4428-a429-9b98199156ca', '1118e4cd-d5a9-4cfe-8131-f9adece97243', 'ad7a4043-8841-4ab6-8bec-db756665cd6d', '17659d4c-8cb5-4eaa-b6b3-77327b7ecf8b', '4dd2ee4c-ded0-4b4a-955b-b0c9231dceda', 'e82e37fb-bb3f-440b-87ba-7aa54ec8ba46', '36dac41e-456b-465e-9b0d-df004605b73c', 'fe39e9a2-4606-4d8d-914c-6a48d2ac5631', '2b053746-0fd4-4236-8df8-f57b5dd39947', 'c4475870-e675-4cb5-ba97-ee5ff597df3a', '6fa6dbdf-42e0-43ed-9e20-11f43d8168a2', '18c0882a-513b-47e7-8b74-a295b1554667', '8bbf284d-f8ca-49b9-a111-a6bd449adbbb', '33db4e00-6255-4ba0-915e-969dc8978226', '25e7122a-f8ac-4ebe-b0d0-ae997c3796cf', 'e3526b7e-db43-4cb6-b5a9-364759d3cfdc', 'ee40bd0e-f672-4faa-8e38-65c083c6ce2c', 'a388dd7a-cb79-4787-95c9-a240bd12c4ba', 'ee2e92c2-a582-4eb7-969a-8ba272404a75', '9c6a3a31-bd0e-4939-a0ee-57a98a73b74a', '3379f812-3122-4748-9208-23ec4503971d', '5e5054c8-12a3-4c3d-90e0-83ddbefdd193', '48968c0e-bd42-4b86-bdfc-e6660b8f5841', '95dd451b-b11c-4c2b-9126-359c7660b6fd', 'c23b9acb-0798-4e81-9e4f-961d9f411f12', 'efacde80-19ad-42ca-82d9-d22e89d87a34', '024bec56-5f8e-41b1-a973-6cc9d58d5365', '89584fb4-940a-4037-90f8-f8ca26ef4e72']
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
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dispersion')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btn_live_wraparound_n'):
        pass
    else:
        assert False, 'leave dispersion page failed'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dispersion')
    with step('[Verify] snapshot: 05_14_01_default_brush.png'):
        actions.capture_for_gt('05_14_01_default_brush.png')
    if actions.compare_with_gt('05_14_01_default_brush.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'default brush size compare failed'
    from_pos = (222, 126)
    destination = (328, 571)
    mode = 1
    with step('[Verify] snapshot: 05_14_01_before_brush.png'):
        actions.capture_for_gt('05_14_01_before_brush.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(222, 126, 328, 571)
    with step('[Verify] snapshot: 05_14_01_after_brush.png'):
        actions.capture_for_gt('05_14_01_after_brush.png')
    if (not actions.compare_with_gt('05_14_01_after_brush.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'brush+ compare failed'
    if (not actions.tap_by_locator(AppiumBy.NAME, 'ic undo')):
        assert False, 'undo brush failed'
    with step('[Verify] snapshot: 05_14_01_after_undo_brush.png'):
        actions.capture_for_gt('05_14_01_after_undo_brush.png')
    if actions.compare_with_gt('05_14_01_after_undo_brush.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo brush compare failed'
    if (not actions.tap_by_locator(AppiumBy.NAME, 'ic redo')):
        assert False, 'redo brush tap failed'
    with step('[Verify] snapshot: 05_14_01_after_redo_brush.png'):
        actions.capture_for_gt('05_14_01_after_redo_brush.png')
    if (not actions.compare_with_gt('05_14_01_after_redo_brush.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'redo brush compare failed'
    with step('[Action] tap_live_undo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')):
        assert False, 'adjust brush size to min failed'
    from_pos = (222, 126)
    destination = (328, 571)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(222, 126, 328, 571)
    with step('[Verify] snapshot: 05_14_01_brush+size_min.png'):
        actions.capture_for_gt('05_14_01_brush+size_min.png')
    if (not actions.compare_with_gt('05_14_01_brush+size_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'min brush size compare failed'
    with step('[Action] tap_live_undo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')):
        assert False, 'adjust brush size to max failed'
    from_pos = (222, 126)
    destination = (328, 571)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(222, 126, 328, 571)
    with step('[Verify] snapshot: 05_14_01_brush+size_max.png'):
        actions.capture_for_gt('05_14_01_brush+size_max.png')
    if (not actions.compare_with_gt('05_14_01_brush+size_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'max brush size compare failed'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn live eraser n')
    from_pos = (40, 300)
    destination = (380, 300)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(40, 300, 380, 300)
    with step('[Verify] snapshot: 05_14_01_after_brush-.png'):
        actions.capture_for_gt('05_14_01_after_brush-.png')
    if (not actions.compare_with_gt('05_14_01_after_brush-.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'brush- compare failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch')):
        assert False, 'tap mask_edit to close eraser failed'
    if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btn live eraser n')):
        pass
    else:
        assert False, 'verify close eraser tab failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shape')):
        assert False, 'tap dispersion_shape failed'
    with step('[Verify] snapshot: 05_14_01_default_shape.png'):
        actions.capture_for_gt('05_14_01_default_shape.png')
    if actions.compare_with_gt('05_14_01_default_shape.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'default shape compare failed'
    with step('[Verify] snapshot: 05_14_01_default_shape_1.png'):
        actions.capture_for_gt('05_14_01_default_shape_1.png')
    if (not actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]')):
        assert False, 'tap dispersion_shape_2 failed'
    with step('[Verify] snapshot: 05_14_01_shape2.png'):
        actions.capture_for_gt('05_14_01_shape2.png')
    if (not actions.compare_with_gt('05_14_01_shape2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'free shape 2 compare failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_size_n')):
        assert False, 'tap dispersion_size failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '15'):
        pass
    else:
        assert False, 'size default value failed'
    with step('[Action] adjust_bokeh_speed_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('1', '2', '3')):
        pass
    else:
        assert False, 'size min value failed'
    if (not actions.tap_by_locator(AppiumBy.NAME, 'ic undo')):
        assert False, 'tap_live_undo_btn_n failed for size'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '15'):
        pass
    else:
        assert False, 'size undo to default value failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('98', '99', '100'))):
        pass
    else:
        assert False, 'size max value failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Direction')):
        assert False, 'tap dispersion_direction failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    else:
        assert False, 'direction default value failed'
    with step('[Verify] snapshot: 05_14_01_before_direction.png'):
        actions.capture_for_gt('05_14_01_before_direction.png')
    with step('[Action] adjust_bokeh_speed_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('356', '357', '358', '359')):
        pass
    else:
        assert False, 'direction max value failed'
    if (not actions.tap_by_locator(AppiumBy.NAME, 'ic undo')):
        assert False, 'tap_live_undo_btn_n failed for direction'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    else:
        assert False, 'direction undo to default value failed'
    with step('[Action] adjust_bokeh_speed_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0.5')
    with step('[Verify] snapshot: 05_14_01_after_adjust_direction.png'):
        actions.capture_for_gt('05_14_01_after_adjust_direction.png')
    if (not actions.compare_with_gt('05_14_01_after_adjust_direction.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust direction compare failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Mode')):
        assert False, 'tap dispersion_mode failed'
    with step('[Verify] snapshot: 05_14_01_default_mode.png'):
        actions.capture_for_gt('05_14_01_default_mode.png')
    if actions.compare_with_gt('05_14_01_default_mode.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'default mode compare failed'
    with step('[Verify] snapshot: 05_14_01_default_mode_1.png'):
        actions.capture_for_gt('05_14_01_default_mode_1.png')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Straight')):
        assert False, 'tap dispersion_mode_straight failed'
    with step('[Verify] snapshot: 05_14_01_straight_mode.png'):
        actions.capture_for_gt('05_14_01_straight_mode.png')
    if (not actions.compare_with_gt('05_14_01_straight_mode.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'straight mode compare failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shrink')):
        assert False, 'tap dispersion_mode_shrink failed'
    with step('[Verify] snapshot: 05_14_01_shrink_mode.png'):
        actions.capture_for_gt('05_14_01_shrink_mode.png')
    if (not actions.compare_with_gt('05_14_01_shrink_mode.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'shrink mode compare failed'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Stretch')):
        assert False, 'tap dispersion_stretch failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '25'):
        pass
    else:
        assert False, 'stretch default size value failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('1', '2'))):
        pass
    else:
        assert False, 'stretch min value failed'
    if (not actions.tap_by_locator(AppiumBy.NAME, 'ic undo')):
        assert False, 'tap_live_undo_btn_n failed for stretch'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '25'):
        pass
    else:
        assert False, 'stretch undo to default value failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('98', '99', '100'))):
        pass
    else:
        assert False, 'stretch max value failed'
    from_pos = (371, 780)
    destination = (158, 780)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(371, 780, 158, 780)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Fade')):
        assert False, 'tap dispersion_fade failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    else:
        assert False, 'fade default value failed'
    with step('[Verify] snapshot: 05_14_01_before_fade.png'):
        actions.capture_for_gt('05_14_01_before_fade.png')
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('98', '99', '100'))):
        pass
    else:
        assert False, 'fade max value failed'
    if (not actions.tap_by_locator(AppiumBy.NAME, 'ic undo')):
        assert False, 'tap_live_undo_btn_n failed for fade'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    else:
        assert False, 'fade undo to default value failed'
    with step('[Action] adjust_bokeh_speed_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0.5')
    with step('[Verify] snapshot: 05_14_01_after_adjust_fade.png'):
        actions.capture_for_gt('05_14_01_after_adjust_fade.png')
    if (not actions.compare_with_gt('05_14_01_after_adjust_fade.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust fade compare failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Speed')):
        assert False, 'tap animation_speed failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '50'):
        pass
    else:
        assert False, 'speed default value failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('1', '2'))):
        pass
    else:
        assert False, 'speed min value failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('98', '99', '100'))):
        pass
    else:
        assert False, 'speed max value failed'
    if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'label == "photo animation btn pause n"'):
        pass
    else:
        assert False, 'wraparound_play_verify failed'
    with step('[Action] tap_wraparound_pause'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Action] tap_live_done_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Still Image')):
        assert False, 'tap save_still_img failed'
    element = ['btn_save_to_file', 'btn_save_to_file4']
    if not any((actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, value) for value in ('btnSave', 'exportButton'))):
        assert False, 'verify btn_save_to_file failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] swipe_live_functionlist'):
        actions.drag_element(actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bokeh'), actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ellements_n'))
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Dispersion')
    from_pos = (222, 126)
    destination = (328, 571)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(222, 126, 328, 571)
    with step('[Action] tap_live_done_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Video')):
        assert False, 'tap save_video failed'
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'verify_save_page failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'GIF')):
        assert False, 'tap_save_to_gif_btn failed'
    with step('[Verify] snapshot: 05_14_01_tap_gif.png'):
        actions.capture_for_gt('05_14_01_tap_gif.png')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
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
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Video')):
        pass
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navSaveButton')
    with step('[Action] close_saved_IAP'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton', timeout=1):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step('[Action] close_rate_us'):
        if actions.is_element_present(AppiumBy.NAME, 'Your animation looks perfect!'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'verify_video_saved failed'
    with step("[Verify] test_00138 completion"):
        assert True
