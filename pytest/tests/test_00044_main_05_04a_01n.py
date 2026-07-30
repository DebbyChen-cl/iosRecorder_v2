import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00044_main_05_04a_01n')
def test_00044_main_05_04a_01n(actions: DriverActions):
    """blur tool new"""
    mode = 1
    uuid = ['4ee0994e-26ed-4056-be90-e424bfff7087', 'd403cabf-86bd-46ff-a938-be2d5f026a14', 'd5625edb-4eca-4d67-a951-7c8a22c805ec', '03fe06f4-c568-4141-85c1-52d681b57376', '433c9135-218b-450d-bbb8-12f94f6a2cec', '677815b1-a6a1-45a2-a36d-465213d6872c', 'b72ff536-c881-4c70-b1ed-4c1f2d755655', 'bb9b9857-28bf-4da4-b806-10eed54470fb', '9adc9610-91ce-4f18-809d-f0bc8813a991', 'eb8db3cd-ea7b-4b31-b182-566c0d8c99d1', '2d1f2f6d-6929-47a2-8787-991978de0f7b', '22539baf-d423-41e3-94b9-74cd8f648e2f', 'ea28516c-359d-4404-a294-34df94290e02', 'be86e674-62ed-425e-a515-175074bc10e3', '4b976aff-2410-4160-970b-4abe3edece5e', '5eea6dfb-8231-4245-a8aa-d63a3eb8e9d4', '746763d6-99b5-490f-8946-acb2f5ce9fd6', '5400d8b8-8225-4d72-bc5e-b3497129c485', 'd49ff600-d0a1-45ab-af8e-df4a4323ba5a', 'b4bae83d-670c-4710-8400-3b1b26d7fdd9', '568c10b1-4f2e-4090-8144-bffca7536d8b', '689370b3-61f7-4208-a6d6-f3adcf50b99c', '8a5b4020-f4bb-4494-a732-3517e4c836dd', '5cc1ac9d-8929-49c3-b898-c8ec66a5f3a2', 'f0639c77-f62c-41a9-ae99-480a6d3bccec', '08a48393-7445-4878-857e-49e108f13d32', 'ff67d0b9-b6c8-48cf-960c-a1778b3d83d9', 'bb5be129-1c97-4b9a-aa44-748873d730cd', '91596c95-15f9-46b8-99aa-2d085859492c', '00895f02-f841-4f0d-b7af-7f33cf72109d', '0c1e394a-2757-41f9-acd6-e1e5ba0ff380', '9c4d80d3-8d85-44b2-a43a-11749216020d', 'c10f082c-c5c2-47ef-9877-e055cc26c26f', '0ad56d77-0e2d-4db7-ac1a-e641c85a881d', '71e34201-e632-457a-ae85-c968734f754c', '0cccc10c-33d3-4053-b4c1-154cbf264828', 'e2ac4bbc-bac1-4a5a-a14e-1dd9c36a5f24', '7cf4d1a1-448c-4d72-a579-f5d348153e9a', '0a11920c-9f89-40ba-a13c-60950b0f7235']
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
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 05_04a_01_before_blur.png'):
        actions.capture_for_gt('05_04a_01_before_blur.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blur Tool')):
        assert False  # legacy raise
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    with step('[Verify] snapshot: base05_04a_01_default.png'):
        actions.capture_for_gt('base05_04a_01_default.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Manual')):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '50') == '75'):
        pass
    with step('[Action] adjust_hsl_hue_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 1)
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', 0)):
        assert False  # legacy raise
    if (actions.get_text(AppiumBy.ACCESSIBILITY_ID, '50') == '75'):
        pass
    from_pos = (20, 450)
    destination = (375, 450)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(20, 450, 375, 450)
    from_pos = (208, 255)
    destination = (208, 225)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    if (not actions.try_tap(AppiumBy.CLASS_NAME, 'XCUIElementTypeScrollView')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_01_circle_outside.png'):
        actions.capture_for_gt('base05_04a_01_circle_outside.png', crop_rect=(0, 60, 276, 526))
    from_pos = (291, 378)
    destination = (270, 378)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    if (not actions.try_tap(AppiumBy.CLASS_NAME, 'XCUIElementTypeScrollView')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_01_circle_inner.png'):
        actions.capture_for_gt('base05_04a_01_circle_inner.png', crop_rect=(0, 60, 276, 526))
    from_pos = (208, 378)
    destination = (208, 430)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    if (not actions.try_tap(AppiumBy.CLASS_NAME, 'XCUIElementTypeScrollView')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_01_circle_position.png'):
        actions.capture_for_gt('base05_04a_01_circle_position.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] adjust_blurtool_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: base05_04a_01_circle_min.png'):
        actions.capture_for_gt('base05_04a_01_circle_min.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] adjust_blurtool_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: base05_04a_01_circle_max.png'):
        actions.capture_for_gt('base05_04a_01_circle_max.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False  # legacy raise
    else:
        with step('[Verify] snapshot: 05_04a_01_exit_blur.png'):
            actions.capture_for_gt('05_04a_01_exit_blur.png', crop_rect=(0, 60, 276, 429))
        if actions.compare_with_gt('05_04a_01_exit_blur.png', gt_folder=TD.GT_FOLDER)[0]:
            pass
        else:
            assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blur Tool')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Linear')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_01_linear_default.png'):
        actions.capture_for_gt('base05_04a_01_linear_default.png', crop_rect=(0, 60, 276, 526))
    from_pos = (207, 255)
    destination = (207, 225)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(207, 255, 207, 225)
    with step('[Verify] snapshot: base05_04a_01_linear_outside.png'):
        actions.capture_for_gt('base05_04a_01_linear_outside.png', crop_rect=(0, 60, 276, 526))
    from_pos = (207, 296)
    destination = (207, 316)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(207, 296, 207, 316)
    with step('[Verify] snapshot: base05_04a_01_linear_inside.png'):
        actions.capture_for_gt('base05_04a_01_linear_inside.png', crop_rect=(0, 60, 276, 526))
    from_pos = (350, 378)
    destination = (350, 320)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(350, 378, 350, 320)
    with step('[Verify] snapshot: base05_04a_01_linear_rotate.png'):
        actions.capture_for_gt('base05_04a_01_linear_rotate.png', crop_rect=(0, 60, 276, 526))
    from_pos = (208, 378)
    destination = (208, 410)
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Verify] snapshot: base05_04a_01_linear_position.png'):
        actions.capture_for_gt('base05_04a_01_linear_position.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] adjust_blurtool_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '0')
    with step('[Verify] snapshot: base05_04a_01_linear_min.png'):
        actions.capture_for_gt('base05_04a_01_linear_min.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] adjust_blurtool_slider'):
        actions.set_slider(AppiumBy.CLASS_NAME, 'XCUIElementTypeSlider', '1')
    with step('[Verify] snapshot: base05_04a_01_linear_max.png'):
        actions.capture_for_gt('base05_04a_01_linear_max.png', crop_rect=(0, 60, 276, 526))
    with step('[Action] tap_feature_x_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Blur Tool')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Manual')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Brush')):
        assert False  # legacy raise
    with step('[Verify] snapshot: base05_04a_01_brush_default.png'):
        actions.capture_for_gt('base05_04a_01_brush_default.png', crop_rect=(0, 60, 276, 526))
    from_pos = (50, 120)
    destination = (350, 550)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 120, 350, 550)
    with step('[Verify] snapshot: base05_04a_01_brush-.png'):
        actions.capture_for_gt('base05_04a_01_brush-.png', crop_rect=(0, 60, 276, 526))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btt_eraser_n')):
        assert False  # legacy raise
    from_pos = (50, 120)
    destination = (350, 550)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(50, 120, 350, 550)
    with step('[Verify] snapshot: base05_04a_01_brush+.png'):
        actions.capture_for_gt('base05_04a_01_brush+.png', crop_rect=(0, 60, 276, 526))
    with step('[Verify] snapshot: 05_04a_01_brushsize_before.png'):
        actions.capture_for_gt('05_04a_01_brushsize_before.png', crop_rect=(0, 725, 367, 783))
    with step('[Action] adjust_bokeh_saturation_slider'):
        actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    with step('[Action] tap'):
        actions.tap_by_coordinates(220, 220)
    with step('[Verify] snapshot: 05_04a_01_brushsize_after.png'):
        actions.capture_for_gt('05_04a_01_brushsize_after.png', crop_rect=(0, 725, 367, 783))
    if (not actions.compare_with_gt('05_04a_01_brushsize_after.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn regional effect brushsize ')
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False  # legacy raise
    else:
        with step('[Verify] snapshot: 05_04a_01_exit_blur_v.png'):
            actions.capture_for_gt('05_04a_01_exit_blur_v.png', crop_rect=(0, 60, 276, 429))
        if (not actions.compare_with_gt('05_04a_01_exit_blur_v.png', gt_folder=TD.GT_FOLDER)[0]):
            pass
        else:
            assert False  # legacy raise
    with step('[Action] tap_edit_home'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'homeButton'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.ACCESSIBILITY_ID, 'btnHome'), (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Verify] test_00044 completion"):
        assert True
