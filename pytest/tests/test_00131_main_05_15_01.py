import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00131_main_05_15_01')
def test_00131_main_05_15_01(actions: DriverActions):
    """Live - static sky"""
    mode = 1
    uuid = ['be90f2ac-1abd-4dea-b9d0-4dfd9d6deeda', 'e74f2d99-0d8d-47f6-b212-4b21474a065f', '97c8e058-ab1a-4d70-895d-a3e13eb56ac6', '700457ba-1dea-4d69-9d21-b144a817022f', 'dc10ce23-327a-483c-afd1-3484b1070725', 'ca74f479-9fa4-4681-8057-d524f8230013', 'ab440441-a12a-402f-9c5a-ffd06166cf46', 'febb6f94-b983-428d-9fe1-e73a8613c94b', 'fccd442f-82df-456f-97e2-abb6b73f9fe1', '7f71eb36-879a-401e-88c2-a4fd4a9ede3e', 'ad13c63f-8237-4101-a1af-1de69cd94c65', '7e431e17-afa7-4cd5-aa59-acb63de71e06', 'd1e47e2d-4935-4971-87cb-4cc570317f27', '3bf54cd6-b7ea-473a-865c-aefc31d2da14', '2f562258-4317-4860-8dfc-5961dd24c0bf', '6b7a7598-c5c4-4853-90fc-bba547de802c', 'c30f548a-ab85-44f2-a149-c52a49c511ee', '26b8b400-fc9e-4553-b6b3-3db5a9a75e28', '33aeffe8-b59b-4b1e-afbd-1c971e008913', '7be8d66f-2028-4638-846c-0e0ed9b3af95', '93fedec7-22ac-4db4-b224-c8b06ed071b2', '656e8772-d63c-41ad-98fd-c9118bf975f6', '794e14a1-b971-4d45-b048-bd3d9a52e58a', '2ab291d1-c575-4ac7-9e5d-c91b7bbb8672', '7f163724-adea-45cb-aef7-fa8fde56fd09', '9a22a251-4873-44ba-be9d-981e2e50bc6f', 'fdf0ef1e-92cc-4acd-930d-e4d72dbacb0b', '159aeb2d-2569-4212-aecb-df442669d826', '09d60d84-9e50-4d07-accd-f28442f8ebeb', 'e70818d0-1ed1-4ae4-8236-0b71e4efd5a4', '185320da-eb8d-4f57-84d2-427a4ac634e6', '6c5b6c51-e689-4503-bbdd-ac06c8927b03', '09a290e5-a987-4e24-9da7-84e6788efa65', 'fff824d5-68a0-40bb-bbc0-7f69d2d902c0']
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
    with step('[Verify] snapshot: 05_15_01_no_sky.png'):
        actions.capture_for_gt('05_15_01_no_sky.png')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cloudy 1')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')):
        assert False, 'tap template 1 failed'
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Verify] snapshot: 05_15_01_sky1.png'):
        actions.capture_for_gt('05_15_01_sky1.png')
    if actions.compare_with_gt('05_15_01_sky1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'compare sky-1 failed'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch')
    with step('[Verify] snapshot: 05_15_01_brushsize_before.png'):
        actions.capture_for_gt('05_15_01_brushsize_before.png')
    with step('[Action] adjust_harmonization_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: 05_15_01_brushsize_after.png'):
        actions.capture_for_gt('05_15_01_brushsize_after.png')
    if (not actions.compare_with_gt('05_15_01_brushsize_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust brush size comparison failed'
    from_pos = (338, 232)
    destination = (300, 400)
    mode = 1
    with step('[Verify] snapshot: 05_15_01_before+.png'):
        actions.capture_for_gt('05_15_01_before+.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(338, 232, 300, 400)
    with step('[Verify] snapshot: 05_15_01_after+.png'):
        actions.capture_for_gt('05_15_01_after+.png')
    if (not actions.compare_with_gt('05_15_01_after+.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'eraser+ comparison failed'
    with step('[Action] tap_live_undo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step('[Verify] snapshot: 05_15_01_after_undo.png'):
        actions.capture_for_gt('05_15_01_after_undo.png')
    if actions.compare_with_gt('05_15_01_after_undo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'undo brush comparison failed'
    with step('[Action] tap_live_redo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic redo')
    with step('[Verify] snapshot: 05_15_01_after_redo.png'):
        actions.capture_for_gt('05_15_01_after_redo.png')
    if actions.compare_with_gt('05_15_01_after_redo.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'redo brush comparison failed'
    with step('[Action] tap_live_undo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    from_pos = (338, 232)
    destination = (300, 400)
    mode = 1
    with step('[Verify] snapshot: 05_15_01_before-.png'):
        actions.capture_for_gt('05_15_01_before-.png')
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(338, 232, 300, 400)
    with step('[Verify] snapshot: 05_15_01_after-.png'):
        actions.capture_for_gt('05_15_01_after-.png')
    if (not actions.compare_with_gt('05_15_01_after-.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'eraser- comparison failed'
    with step('[Action] tap_live_undo_btn_n'):
        actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnMaskSwitch')
    with step('[Verify] snapshot: 05_15_01_close_mask_edit.png'):
        actions.capture_for_gt('05_15_01_close_mask_edit.png')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-sky_static_cloudy1_01')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feather')):
        assert False, 'tap sky_feather failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    with step('[Action] adjust_bokeh_speed_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('-95', '-96', '-97', '-98', '-99', '-100'))):
        pass
    else:
        assert False, 'feather adjust min failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        pass
    else:
        assert False, 'feather adjust max failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Horizon')):
        assert False, 'tap sky_horizon failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0')):
        pass
    else:
        assert False, 'horizon adjust min failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        pass
    else:
        assert False, 'horizon adjust max failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Land Ambient')):
        assert False, 'tap sky_land failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '35'):
        pass
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('5', '4', '-3', '2', '1', '0'))):
        pass
    else:
        assert False, 'land ambient adjust min failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        pass
    else:
        assert False, 'land ambient adjust max failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HDR Glow')):
        assert False, 'tap sky_HDRglow failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0')):
        pass
    else:
        assert False, 'HDR Glow adjust min failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        pass
    else:
        assert False, 'HDR Glow adjust max failed'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'HDR Edge')):
        assert False, 'tap sky_HDRedge failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('-15', '-16', '-17', '-18', '-19', '-20'))):
        pass
    else:
        assert False, 'HDR edge adjust min failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('78', '79', '80'))):
        pass
    else:
        assert False, 'HDR edge adjust max failed'
    from_pos = (371, 783)
    destination = (158, 783)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(371, 783, 158, 783)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sky Fade')):
        assert False, 'tap sky_fade failed'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0')):
        pass
    else:
        assert False, 'sky fade adjust min failed'
    if (actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "sky_replacement"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100'))):
        pass
    else:
        assert False, 'sky fade adjust max failed'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Verify] snapshot: 05_15_01_back_2_sky.png'):
        actions.capture_for_gt('05_15_01_back_2_sky.png')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, '01'):
        pass
    else:
        assert False, 'back to sky main page failed'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Verify] snapshot: 05_15_01_back_2_live.png'):
        actions.capture_for_gt('05_15_01_back_2_live.png')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btn_live_wraparound_n'):
        pass
    else:
        assert False, 'leave sky page failed'
    from_pos = (371, 770)
    destination = (158, 770)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(371, 770, 158, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Animation')
    with step('[Action] close_animation_tutorial'):
        actions.is_element_present(AppiumBy.NAME, 'Tap to draw motion arrows on areas that you want to animate.')
        actions.tap_by_coordinates(250, 250)
        actions.tap_by_coordinates(250, 250)
        actions.wait_for_invisible(AppiumBy.NAME, 'Tap to draw motion arrows on areas that you want to animate.')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    from_pos = (158, 777)
    destination = (371, 777)
    mode = 1
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(158, 777, 371, 777)
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_sky_n')
    with step('[Action] tap_phd_element'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-static_sky_category_cloudy1')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cloudy 2')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '01')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'UNLOCK TO'):
        pass
    else:
        assert False, 'verify CTA bar failed'
    if (not actions.tap_by_locator(AppiumBy.NAME, 'Premium')):
        assert False, 'tap CTA bar free trial failed'
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False, 'verify IAP popup failed'
    with step("[Verify] test_00131 completion"):
        assert True
