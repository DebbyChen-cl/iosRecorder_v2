import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00015_main_04_01_05')
def test_00015_main_04_01_05(actions: DriverActions):
    """camera - retouch - others"""
    uuid = ['cc8538b1-944f-4adc-836a-11f788ffe453', '006fc6bd-9dfd-4b9f-ab7c-63a75af7804b', '796eaa9a-776e-448a-ac29-e51536fab29a', '3d16da87-a4d4-4fd6-8ca7-877b18b68e9f', 'c674aa22-095c-49de-9fa6-84fd4944f770', '782afe58-9afb-42e1-b887-51cd863b7e0e', 'e4a3974d-71af-4006-81f5-a5620b1d6d9e', '6ca7983d-5058-4f8c-b103-d7a7cf47430c', 'ba37bd19-0a54-43c3-8b13-5fe6115ca89c', '64881f1b-3335-484c-ae23-1b1e1e30d264', '3df7f06d-3bff-4dcf-98e8-55fe1115b766', '767917bc-740a-4981-af87-7a61490fefa2', '5c3cbb5b-2a79-4b93-a1b1-3c0ba4576df1', 'df5565c2-f401-4ed4-9e66-9d3cadd373ac', '5de7d8e4-ffc4-410d-bb50-c83566d22a2b', '65273e03-e77a-459e-b087-cc090f885128', 'e8cfb976-a5c4-410a-aa74-2cbde764f016', '5724974c-fbe6-4490-a4c7-382b78bf9740', 'ff4942e5-f608-4257-bf2f-d373194f2263', '70778ba6-cb62-4ecd-a601-3f4a5d922833', '3448aeab-de7d-4a87-881c-2dbf374e3f59', '245a3616-5115-4b73-9a30-54b0f5e42cf3', 'b789e0d8-22f7-43f0-b3b2-a3ed16ca2b60']
    if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnMore')):
        assert False
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPortrait')):
        assert False
    with step('[Verify] snapshot: 04_01_05_auto_retouch_on.png'):
        actions.capture_for_gt('04_01_05_auto_retouch_on.png', crop_rect=(9, 636, 315, 677))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'faceRetouchAutoSwitch')):
        assert False
    with step('[Verify] snapshot: 04_01_05_auto_retouch_off1.png'):
        actions.capture_for_gt('04_01_05_auto_retouch_off1.png', crop_rect=(9, 636, 315, 677))
    with step('[Verify] snapshot: 04_01_05_auto_retouch_off.png'):
        actions.capture_for_gt('04_01_05_auto_retouch_off.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_auto_retouch_off.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    with step('[Action] tap_shot_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Conceal')):
        assert False
    with step('[Verify] snapshot: 04_01_05_conceal_default.png'):
        actions.capture_for_gt('04_01_05_conceal_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0.5')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_conceal_mid.png'):
        actions.capture_for_gt('04_01_05_conceal_mid.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_conceal_mid.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_conceal_max.png'):
        actions.capture_for_gt('04_01_05_conceal_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_conceal_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Smooth')):
        assert False
    with step('[Verify] snapshot: 04_01_05_skinsmoothen_default.png'):
        actions.capture_for_gt('04_01_05_skinsmoothen_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_skinsmoothen_min.png'):
        actions.capture_for_gt('04_01_05_skinsmoothen_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_skinsmoothen_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_skinsmoothen_max.png'):
        actions.capture_for_gt('04_01_05_skinsmoothen_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_skinsmoothen_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Skin Tone')):
        assert False
    with step('[Verify] snapshot: 04_01_05_skintone_default.png'):
        actions.capture_for_gt('04_01_05_skintone_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_skintone_min.png'):
        actions.capture_for_gt('04_01_05_skintone_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_skintone_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_skintone_max.png'):
        actions.capture_for_gt('04_01_05_skintone_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_skintone_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Teeth Whiten')):
        assert False
    with step('[Verify] snapshot: 04_01_05_teethwhiten_default.png'):
        actions.capture_for_gt('04_01_05_teethwhiten_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0.5')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_teethwhiten_mid.png'):
        actions.capture_for_gt('04_01_05_teethwhiten_mid.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_teethwhiten_mid.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_teethwhiten_max.png'):
        actions.capture_for_gt('04_01_05_teethwhiten_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_teethwhiten_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Brighten')):
        assert False
    with step('[Verify] snapshot: 04_01_05_eyebrighten_default.png'):
        actions.capture_for_gt('04_01_05_eyebrighten_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0.5')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_eyebrighten_mid.png'):
        actions.capture_for_gt('04_01_05_eyebrighten_mid.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_eyebrighten_mid.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_eyebrighten_max.png'):
        actions.capture_for_gt('04_01_05_eyebrighten_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_eyebrighten_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Eye Bags')):
        assert False
    with step('[Verify] snapshot: 04_01_05_eyebag_default.png'):
        actions.capture_for_gt('04_01_05_eyebag_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0.5')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_eyebag_mid.png'):
        actions.capture_for_gt('04_01_05_eyebag_mid.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_eyebag_mid.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_eyebag_max.png'):
        actions.capture_for_gt('04_01_05_eyebag_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_eyebag_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')):
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Oiliness')):
        assert False
    with step('[Verify] snapshot: 04_01_05_oiliness_default.png'):
        actions.capture_for_gt('04_01_05_oiliness_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0.5')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_oiliness_mid.png'):
        actions.capture_for_gt('04_01_05_oiliness_mid.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_oiliness_mid.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_05_oiliness_max.png'):
        actions.capture_for_gt('04_01_05_oiliness_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_05_oiliness_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')):
        assert False  # legacy raise
    with step("[Verify] test_00015 completion"):
        assert True
