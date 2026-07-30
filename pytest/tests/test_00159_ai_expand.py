import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name('00159_ai_expand')
def test_00159_ai_expand(actions: DriverActions):
    """AI Expand crop, generation, history, and apply flow."""
    with step('[Action] open_settings_and_enable_plan'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'About')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton')
        assert actions.is_element_present(AppiumBy.NAME, 'Develop Info')
        assert actions.find_element(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="1"])[2]')
        actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[6]')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')

    with step('[Action] open_ai_expand'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
        assert actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
        actions.capture_for_gt('G01_01_07_before_aiexpand.png')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Expand')

    ratios = [
        ('Original', 'original'), ('Square', 'square'), ('2:3', '2v3'),
        ('3:2', '3v2'), ('3:4', '3v4'), ('4:3', '4v3'),
        ('9:16', '9v16'), ('16:9', '16v9'), ('4:5', '4v5'),
        ('5:4', '5v4'), ('IG post', 'ig_p'), ('IG story', 'ig_s'),
        ('ic_tictok9v16', 'tictok_p'), ('ic_tictok16v9', 'tictok_l'),
        ('Snapchat', 'snapchat'), ('YouTube', 'youtube'), ('Facebook', 'fb'),
    ]
    for locator, suffix in ratios:
        with step(f'[Action] tap_crop_{suffix}'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID if ':' in locator or locator in {'Original', 'Square'} else AppiumBy.NAME, locator)
        actions.capture_for_gt(f'G01_01_07_{suffix}.png')

    with step('[Action] undo_ratio'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnUndo')
    actions.capture_for_gt('G01_01_07_undo.png')

    with step('[Action] generate_expand'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Snapchat')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Expand More')
        actions.capture_for_gt('G01_01_07_redo_generate_og.png')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnUndo')
        actions.capture_for_gt('G01_01_07_undo_generate.png')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnRedo')
        actions.capture_for_gt('G01_01_07_redo_generate.png')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Expand More')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
        actions.capture_for_gt('G01_01_07_genera_more.png')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n')
        actions.capture_for_gt('G01_01_07_x.png')

    with step('[Action] apply_expand_and_leave'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Expand')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
        assert actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
        actions.capture_for_gt('G01_01_07_v.png')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Verify] test_00159 completion"):
        assert True
