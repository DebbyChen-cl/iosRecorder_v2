# @sft-convert:generated  (自動生成；若手動編輯，請把檔名加進 .scratch/sft-convert/PROTECT.txt
#                          或把本行改成 '# @manual'，即不會被覆蓋)
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00171_ai_face_swap_multi')
def test_00171_ai_face_swap_multi(actions: DriverActions):
    """AI face swap - multi face"""
    uuid = ['9b572af2-570c-4e87-aeb0-a2653083f549', '5fcdfc82-cc7a-4e2f-af76-694f1c53f95d', 'e4310517-f6d6-4955-a5f9-332c7001b2aa', '657007fa-1a2f-47d3-b587-3d9415a2bd7f', '6d255f88-8282-4d10-8a5a-e55d793140ba', 'e8d0bfd9-edb2-4374-b99d-df8d60bcca18', 'dfc4c173-0c0f-405a-883e-ddc9482f0c81', '17649292-d5ab-4ef7-aed7-d78a3383ec94']
    enter_settings_page_success = False
    for attempt in range(3):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
        enter_settings_page_success = True
        break
        if attempt < 2:
            pass
    if not enter_settings_page_success:
        assert False, 'Failed to tap settings3 after 3 retries'
    with step('[Action] verify_settings_page'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Setting') or actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    enter_about_page_success = False
    for attempt in range(3):
        with step('[Action] enter_about_page'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'About')
            assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton')
        enter_about_page_success = True
        break
        if attempt < 2:
            pass
    if not enter_about_page_success:
        assert False, 'Enter about page fail after 3 retries'
    with step('[Action] enable_plan_from_settings'):
        assert actions.is_element_present(AppiumBy.NAME, 'Develop Info')
        assert actions.find_element(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="1"])[2]')
        actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[6]')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'chevron.left')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome'), '[G02_01_03_2] Failed to tap_home'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos'), '[G02_01_03_2] Failed to tap ai_photos'
    with step('[Action] scroll_and_tap_vertical'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext'), '[G02_01_03_2] Failed to tap try_now'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue'), '[G02_01_03_2] Failed to tap continue'
    assert actions.tap_by_coordinates(210, 340)
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'hintLabel'):
        pass
    else:
        assert False, '[G02_01_03_2] verify face swap select target failed'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'faceSelectionCell-0'), '[G02_01_03_2] Failed to tap select_target_face 1'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'faceSelectionCell-1'), '[G02_01_03_2] Failed to tap select_target_face 2'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext'), '[G02_01_03_2] Failed to tap next_btn'
    if actions.is_element_present(AppiumBy.NAME, 'titleLabel'):
        pass
    else:
        assert False, '[G02_01_03_2] select target face or import page failed'
    assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "addSourceImageView"`][1]'), '[G02_01_03_2] Failed to tap_import_source_btn 1'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue'), '[G02_01_03_2] Failed to tap continue for import 1'
    with step('[Action] expand_album_list'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Import Photos...', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Import Photos...')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'hintLabel'):
        pass
    else:
        assert False, '[G02_01_03_2] verify source face menu failed'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'faceSelectionCell-0'), '[G02_01_03_2] Failed to select source face 1'
    with step('[Action] tap_next_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "addSourceImageView"`][2]'), '[G02_01_03_2] Failed to tap_import_source_btn 2'
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.NAME, 'Import Photos...', timeout=5):
            actions.wait_for_invisible(AppiumBy.NAME, 'Import Photos...')
    if actions.is_element_present(AppiumBy.NAME, 'titleLabel'):
        pass
    else:
        assert False, '[G02_01_03_2] verify one-face import failed'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate'), '[G02_01_03_2] Failed to tap generate_ai'
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnSave'):
        pass
    else:
        assert False, '[G02_01_03_2] generate face swap result failed'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSave'), '[G02_01_03_2] Failed to tap save_to_file2'
    with step('[Action] tap_next_edit_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Next Edit')
        assert actions.is_element_present(AppiumBy.NAME, 'Stock')
    with step("[Verify] test_00171 completion"):
        assert True
