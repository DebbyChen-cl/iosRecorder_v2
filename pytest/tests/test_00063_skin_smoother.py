import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00063_skin_smoother')
def test_00063_skin_smoother(actions: DriverActions):
    """skin smoother"""
    mode = 1
    uuid = ['460d6f62-3435-4762-b996-d0fd9769ea8d', '22b74bf7-8d4a-4217-808b-0a4a80e5760d', 'f5853a19-4ec8-40c9-9700-b3f41e90e667', 'dc1173fc-4a3d-43e2-9752-6f9c4b0fb00f', '0429b9d5-02b6-4706-a053-7de10e2c0f91', 'e3861d51-10e0-4780-8686-c1e4971213e5', '5445e0db-4211-44b7-858e-6aa9a4e38d60', 'efcbde55-9b68-46d7-a286-f147e94ae3bb', 'd5f4c8af-6192-40d3-b3c4-c1357d1d5a09']
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
    with step('[Verify] snapshot: 05_07_01_before_skin_smoother.png'):
        actions.capture_for_gt('05_07_01_before_skin_smoother.png', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Beautify')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Smooth')
    with step('[Verify] snapshot: 05_07_01_before_brush+.png'):
        actions.capture_for_gt('05_07_01_before_brush+.png')
    from_pos = (220, 100)
    destination = (220, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(220, 100, 220, 600)
    with step('[Verify] snapshot: 05_07_01_brush+.png'):
        actions.capture_for_gt('05_07_01_brush+.png')
    with step('[Verify] snapshot: base05_07_01_brush+.png'):
        actions.capture_for_gt('base05_07_01_brush+.png')
    if actions.compare_with_gt('05_07_01_brush+1.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Brush+ fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False, 'Tap undo fail'
    with step('[Verify] snapshot: 05_07_01_undo_brush+.png'):
        actions.capture_for_gt('05_07_01_undo_brush+.png')
    if actions.compare_with_gt('05_07_01_undo_brush+.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Undo fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btnRedo'), (AppiumBy.ACCESSIBILITY_ID, 'redoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic_redo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit redo n'), (AppiumBy.NAME, 'Pop btn redo n')])):
        assert False, 'Tap redo fail'
    with step('[Verify] snapshot: 05_07_01_redo_brush+.png'):
        actions.capture_for_gt('05_07_01_redo_brush+.png')
    if actions.compare_with_gt('05_07_01_redo_brush+.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Redo fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn eraser n')):
        assert False, 'Tap brush- fail'
    from_pos = (220, 100)
    destination = (220, 400)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(220, 100, 220, 400)
    with step('[Verify] snapshot: 05_07_01_brush-.png'):
        actions.capture_for_gt('05_07_01_brush-.png', crop_rect=(0, 60, 276, 429))
    from_pos = (220, 100)
    destination = (220, 400)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(220, 100, 220, 400)
    if actions.compare_with_gt('05_07_01_brush-.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'Brush- fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n'), (AppiumBy.NAME, 'btnDone'), (AppiumBy.NAME, 'btn ok n'), (AppiumBy.ACCESSIBILITY_ID, 'doneButton')])):
        assert False, 'Tap v fail'
    with step('[Verify] snapshot: 05_07_01_[v].png'):
        actions.capture_for_gt('05_07_01_[v].png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_07_01_[v].png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, '[v] fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Verify] snapshot: before_05_07_01_[x].png'):
        actions.capture_for_gt('before_05_07_01_[x].png', crop_rect=(0, 60, 276, 429))
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Smooth')
    from_pos = (220, 100)
    destination = (220, 600)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(220, 100, 220, 600)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnCancel')):
        assert False, 'Tap x fail'
    with step('[Verify] snapshot: 05_07_01_[x].png'):
        actions.capture_for_gt('05_07_01_[x].png', crop_rect=(0, 60, 276, 429))
    if actions.compare_with_gt('05_07_01_[x].png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[x] fail'
    with step("[Verify] test_00063 completion"):
        assert True
