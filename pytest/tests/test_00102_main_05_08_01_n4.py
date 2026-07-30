import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00102_main_05_08_01_n4')
def test_00102_main_05_08_01_n4(actions: DriverActions):
    """Text tools - text new - style"""
    mode = 1
    uuid = ['fc6358cb-6acb-4754-b432-2838708f6b6e', '43b9e0b1-78c4-497b-97fc-3f3c189bad70', '3da79dae-e39d-4d3b-91a9-05038e7eeb92', 'f3cc5dc9-0611-41f4-bec7-94a9d197b776', '48939ec9-9675-4b05-936a-f55e9ae99707', '71a97ab8-7830-46ec-bdaf-3f92937dcba1', '7ba5c059-43a2-4964-a953-6bccf7b43d87', '1bca473e-888b-49bf-b114-1e30a14753be', '77c7f6f5-3e2f-4833-ae2a-ea3a4dbe4348', '0fb9d5a3-131d-453b-b77d-26ae58cd2e01', '7e1c92b1-c1fa-4e14-9167-1a14f8f4d0df']
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
    with step('[Action] tap_edit1_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    from_pos = (380, 770)
    destination = (50, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 50, 770)
    if actions.is_element_present(AppiumBy.NAME, 'xpromo btn close n', timeout=2):
        with step('[Action] tap_close_xpromo_btn'):
            actions.tap_by_locator(AppiumBy.NAME, 'xpromo btn close n')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Text')
    with step('[Verify] snapshot: 05_08_01_no_style_panel.png'):
        actions.capture_for_gt('05_08_01_no_style_panel.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Colorful')
    with step('[Verify] snapshot: 05_08_01_style_default.png'):
        actions.capture_for_gt('05_08_01_style_default.png', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]')
    if actions.compare_with_gt('05_08_01_style_default.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare style default fail'
    with step('[Verify] snapshot: 05_08_01_style_default_size.png'):
        actions.capture_for_gt('05_08_01_style_default_size.png')
    from_pos = (215, 500)
    destination = (215, 100)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(215, 500, 215, 100)
    with step('[Verify] snapshot: 05_08_01_style_extend.png'):
        actions.capture_for_gt('05_08_01_style_extend.png')
    if not actions.compare_with_gt('05_08_01_style_extend.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Extended panel comparison fail'
    with step('[Verify] snapshot: 05_08_01_before_close_panel_x.png'):
        actions.capture_for_gt('05_08_01_before_close_panel_x.png')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'leaveButton')
    with step('[Verify] snapshot: 05_08_01_close_style_panel_x.png'):
        actions.capture_for_gt('05_08_01_close_style_panel_x.png')
    if not actions.compare_with_gt('05_08_01_close_style_panel_x.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Close style panel x comparison fail'
    with step('[Action] focus_text'):
        actions.tap_by_coordinates(205, 455)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Colorful')
    with step('[Action] tap_text_style_template'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_yellow_12_new')
    with step('[Verify] snapshot: 05_08_01_style_1.png'):
        actions.capture_for_gt('05_08_01_style_1.png', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]')
    if actions.compare_with_gt('05_08_01_style_1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_text_style_template'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_yellow_12_new')
    with step('[Verify] snapshot: 05_08_01_style_2.png'):
        actions.capture_for_gt('05_08_01_style_2.png', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]')
    if actions.compare_with_gt('05_08_01_style_2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_text_style_template'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_yellow_12_new')
    with step('[Verify] snapshot: 05_08_01_style_3.png'):
        actions.capture_for_gt('05_08_01_style_3.png', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]')
    if actions.compare_with_gt('05_08_01_style_3.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Background')
    with step('[Action] tap_text_bg_template'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_202212_004')
    with step('[Verify] snapshot: 05_08_01_bg_1.png'):
        actions.capture_for_gt('05_08_01_bg_1.png', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]')
    if actions.compare_with_gt('05_08_01_bg_1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_text_bg_template'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_202212_004')
    with step('[Verify] snapshot: 05_08_01_bg_2.png'):
        actions.capture_for_gt('05_08_01_bg_2.png', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]')
    if actions.compare_with_gt('05_08_01_bg_2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Compare bg shape 2 fail'
    with step('[Action] tap_text_bg_template'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_202212_004')
    with step('[Verify] snapshot: 05_08_01_bg_3.png'):
        actions.capture_for_gt('05_08_01_bg_3.png', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]')
    if actions.compare_with_gt('05_08_01_bg_3.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    with step('[Action] tap_text_bg_template'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-phdm_text_style_202212_004')
    with step('[Verify] snapshot: 05_08_01_bg_4.png'):
        actions.capture_for_gt('05_08_01_bg_4.png', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.AddImageViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]')
    with step('[Verify] compare: 05_08_01_bg_4.png'):
        assert actions.compare_with_gt('05_08_01_bg_4.png', gt_folder=TD.GT_FOLDER)[0]
    with step('[Verify] snapshot: 05_08_01_before_close_style_drag.png'):
        actions.capture_for_gt('05_08_01_before_close_style_drag.png')
    from_pos = (206, 476)
    destination = (206, 800)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(206, 476, 206, 800)
    with step('[Verify] snapshot: 05_08_01_after_close_style_drag.png'):
        actions.capture_for_gt('05_08_01_after_close_style_drag.png')
    if not actions.compare_with_gt('05_08_01_after_close_style_drag.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Drag down close panel comparison fail'
    with step("[Verify] test_00102 completion"):
        assert True
