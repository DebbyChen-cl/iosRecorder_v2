import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00132_main_05_15_02')
def test_00132_main_05_15_02(actions: DriverActions):
    """Live - animated sky"""
    mode = 1
    uuid = ['574fbc29-463f-4bac-aa0e-5d4ed022ecd6', '10f5ce55-48ba-4f8e-ad84-1d9ffd037807', '044ffbe5-8017-456e-b13b-a86926f59cc4', '08bd8612-403a-4c18-9e77-bb5070f4b84a', 'ab0afad8-c2bf-4a24-97ef-73d23d13a405', 'dee8ef32-df38-4ca6-bf47-dbc43ed7b7e3', 'ceeb044b-9449-4751-bc5e-bf92ee323530', '3bd2dbc5-d48f-46b1-883f-92876eedd0d3', '68900edc-9445-44d0-88cd-fd82f6164990', '0ba04024-ac59-4f68-bc85-198aef674ca6', 'c4557abd-93f2-4d93-8468-d489614b8b1d', '6e0c21f0-c3eb-4e76-8e12-76a38d44a8c9', '463c2e61-1bf7-4a42-bab7-184827b551d4', 'ee88b27f-e9aa-422c-bc60-5b9f9877eae0', 'dc617b7e-21ce-4009-9b01-05b323b0eb85', '2e5e0643-43a4-442b-863e-7b14003aa30b', '94daf791-7d3c-4b03-ad60-d6008b9ba046', 'a5b86862-cae8-422d-b2d7-6ede8aeb15c3', '826c57c9-811b-4cf1-8362-c3283be07699', 'd974c6ed-4503-4cbf-b0c1-1c01557049eb', '428dd0c5-42ef-418d-bdb2-5fdc1598f388', '8d562451-400d-4733-9a0c-9bc0bac5b61f']
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
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_sky_n')
    for x in range(5):
        from_pos = (371, 770)
        destination = (110, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(371, 770, 110, 770)
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Aurora')
    with step('[Verify] snapshot: 05_15_01_sky_ani_og.png'):
        actions.capture_for_gt('05_15_01_sky_ani_og.png')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')):
        assert False, 'tap template 1 failed in animated sky'
    with step('[Verify] snapshot: 05_15_01_ani_sky1.png'):
        actions.capture_for_gt('05_15_01_ani_sky1.png')
    if (not actions.compare_with_gt('05_15_01_ani_sky1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'compare animated sky-1 failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')):
        assert False, 'enter parameter adjustment failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feather')):
        assert False, 'tap sky_feather failed in animated sky'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    else:
        assert False, 'animated sky feather default value error'
    with step('[Action] adjust_bokeh_speed_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('-95', '-96', '-97', '-98', '-99', '-100'))):
        pass
    else:
        assert False, 'animated sky feather adjust min failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        pass
    else:
        assert False, 'animated sky feather adjust max failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Horizon')):
        assert False, 'tap sky_horizon failed in animated sky'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0')):
        pass
    else:
        assert False, 'animated sky horizon adjust min failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        pass
    else:
        assert False, 'animated sky horizon adjust max failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Land Ambient')):
        assert False, 'tap sky_land failed in animated sky'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '70'):
        pass
    with step('[Action] adjust_bokeh_speed_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('5', '4', '-3', '2', '1', '0'))):
        pass
    else:
        assert False, 'animated sky land ambient adjust min failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        pass
    else:
        assert False, 'animated sky land ambient adjust max failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sky Fade')):
        assert False, 'tap sky_fade failed in animated sky'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0')):
        pass
    else:
        assert False, 'animated sky fade adjust min failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        pass
    else:
        assert False, 'animated sky fade adjust max failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Speed')):
        assert False, 'tap sky_speed failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '30'):
        pass
    else:
        assert False, 'sky speed default value error'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('1', '2', '3', '4', '5'))):
        pass
    else:
        assert False, 'sky speed adjust min failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        pass
    else:
        assert False, 'sky speed adjust max failed'
    if actions.is_element_present(AppiumBy.IOS_PREDICATE, 'label == "photo animation btn pause n"'):
        pass
    else:
        assert False, 'playback verification failed'
    with step('[Action] tap_wraparound_pause'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'btnPlay')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, '01'):
        pass
    else:
        assert False, 'back to sky main page failed in animated sky'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_wraparound_n')):
        assert False, 'tap wraparound to back to Live Room failed'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'tap done button failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Still Image')):
        assert False, 'tap save_still_img failed'
    element = ['btn_save_to_file', 'btn_save_to_file4']
    if not any((actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, value) for value in ('btnSave', 'exportButton'))):
        assert False, 'save to still image verification failed'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_sky_n')
    for x in range(7):
        from_pos = (371, 770)
        destination = (50, 770)
        mode = 1
        with step('[Action] brush_surrealart'):
            actions.drag_coordinates(371, 770, 50, 770)
    with step('[Action] tap_phd_element'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Aurora')
    with step('[Action] tap_phd_element'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_done_btn'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Video')):
        assert False, 'tap save_video failed'
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'):
        pass
    else:
        assert False, 'save video verification failed'
    with step("[Verify] test_00132 completion"):
        assert True
