import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00100_main_05_08_01_n2')
def test_00100_main_05_08_01_n2(actions: DriverActions):
    """Text tools - text new - font"""
    mode = 1
    uuid = ['5bf07726-2a4f-4296-ae89-6dfa3076fa0d', 'bf6e4a28-673b-42d7-b28c-2e2d3b17042d', '5b7e02a8-f355-4856-b408-7d61d00fa773', '569711df-917c-4ef6-88e5-841945495e50', '88a25268-fd69-48d4-bc95-ece73d953ea4', '611c8812-7e08-4bf6-9a14-ebde305bb202', '64847436-f1d8-420d-872b-73a1d86cbee8', '74b71b2f-69e1-4a6f-817a-8356b1d5175a', 'b617c7aa-0688-4b73-b8d5-9cbe4f822714', '08a79887-caa1-4f2a-ac74-4bcf9bfecab2', 'a9689bad-1f1f-46d7-b168-24ec3245b1ff', '50e4e828-5ce6-4965-beda-3f6a02c1d776', '1518982e-2609-4949-a127-cdde928aafaa', '01899cf7-e070-4647-a08c-e23920d53552', '9488501e-0c36-4dca-8e9e-d7a9ef165575', '8a3002c7-a253-4a74-9fab-43987fb00513', '9b4fe4af-7458-4073-9857-de2788cbefe5', '2edf9907-e33f-4d08-8b3d-2ea83307239a', 'cea5b480-015b-46f7-994f-01173ae828a3']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_edit1_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    from_pos = (380, 770)
    destination = (50, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Verify] snapshot: 05_08_01_no_font_panel.png'):
        actions.capture_for_gt('05_08_01_no_font_panel.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Font')
    with step('[Verify] snapshot: 05_08_01_font_default.png'):
        actions.capture_for_gt('05_08_01_font_default.png')
    if actions.compare_with_gt('05_08_01_font_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare font default fail'
    with step('[Verify] snapshot: 05_08_01_font_default_size.png'):
        actions.capture_for_gt('05_08_01_font_default_size.png')
    from_pos = (215, 500)
    destination = (215, 100)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(215, 500, 215, 100)
    with step('[Verify] snapshot: 05_08_01_font_extend.png'):
        actions.capture_for_gt('05_08_01_font_extend.png')
    if not actions.compare_with_gt('05_08_01_font_extend.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Extended panel comparison fail'
    with step('[Verify] snapshot: 05_08_01_before_close_panel_x.png'):
        actions.capture_for_gt('05_08_01_before_close_panel_x.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 05_08_01_close_panel_x.png'):
        actions.capture_for_gt('05_08_01_close_panel_x.png')
    if not actions.compare_with_gt('05_08_01_close_panel_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Close panel x comparison fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Font')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[2]')
    with step('[Verify] snapshot: 05_08_01_change_font.png'):
        actions.capture_for_gt('05_08_01_change_font.png')
    if actions.compare_with_gt('05_08_01_change_font.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare change font fail'
    with step('[Verify] snapshot: 05_08_01_before_close_panel_drag.png'):
        actions.capture_for_gt('05_08_01_before_close_panel_drag.png')
    destination = (206, 800)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(215, 500, 206, 800)
    with step('[Verify] snapshot: 05_08_01_after_close_panel_drag.png'):
        actions.capture_for_gt('05_08_01_after_close_panel_drag.png')
    if not actions.compare_with_gt('05_08_01_after_close_panel_drag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Drag down close panel comparison fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Font')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'English')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'All Languages')
    with step('[Verify] snapshot: 05_08_01_filter_all.png'):
        actions.capture_for_gt('05_08_01_filter_all.png')
    if actions.compare_with_gt('05_08_01_filter_all.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare filter all fail'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'All Languages')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Traditional Chinese')
    with step('[Verify] snapshot: 05_08_01_filter_cht.png'):
        actions.capture_for_gt('05_08_01_filter_cht.png')
    if actions.compare_with_gt('05_08_01_filter_cht.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare filter CHT fail'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Traditional Chinese')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Simplified Chinese')
    with step('[Verify] snapshot: 05_08_01_filter_chs.png'):
        actions.capture_for_gt('05_08_01_filter_chs.png')
    if actions.compare_with_gt('05_08_01_filter_chs.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare filter CHS fail'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Simplified Chinese')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Japanese')
    with step('[Verify] snapshot: 05_08_01_filter_jpn.png'):
        actions.capture_for_gt('05_08_01_filter_jpn.png')
    if actions.compare_with_gt('05_08_01_filter_jpn.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare filter JPN fail'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Japanese')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Korean')
    with step('[Verify] snapshot: 05_08_01_filter_KOR.png'):
        actions.capture_for_gt('05_08_01_filter_KOR.png')
    if actions.compare_with_gt('05_08_01_filter_KOR.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare filter KOR fail'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Korean')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'English')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'All Styles')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Handwriting')
    with step('[Verify] snapshot: 05_08_01_filter_ENU_hand.png'):
        actions.capture_for_gt('05_08_01_filter_ENU_hand.png')
    if actions.compare_with_gt('05_08_01_filter_ENU_hand.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare filter ENU handwriting fail'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Handwriting')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Calligraphy')
    with step('[Verify] snapshot: 05_08_01_filter_calligraphy.png'):
        actions.capture_for_gt('05_08_01_filter_calligraphy.png')
    if actions.compare_with_gt('05_08_01_filter_calligraphy.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare filter calligraphy fail'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Calligraphy')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Monospace')
    with step('[Verify] snapshot: 05_08_01_filter_monospace.png'):
        actions.capture_for_gt('05_08_01_filter_monospace.png')
    if actions.compare_with_gt('05_08_01_filter_monospace.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare filter monospace fail'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Monospace')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'All Styles')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'favoriteButton')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'selectedButton')
    with step('[Verify] snapshot: 05_08_01_font_favorite.png'):
        actions.capture_for_gt('05_08_01_font_favorite.png')
    if actions.compare_with_gt('05_08_01_font_favorite.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare add favorite fail'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'favoriteButton')
    with step('[Verify] snapshot: 05_08_01_font_favorite_remove.png'):
        actions.capture_for_gt('05_08_01_font_favorite_remove.png')
    if actions.compare_with_gt('05_08_01_font_favorite_remove.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare remove favorite fail'
    with step("[Verify] test_00100 completion"):
        assert True
