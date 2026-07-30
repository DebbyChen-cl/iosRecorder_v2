import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00014_main_04_01_04')
def test_00014_main_04_01_04(actions: DriverActions):
    """camera - retouch - reshape"""
    uuid = ['7f001c37-a250-44fd-9e15-ae5ee2919068', 'd1458b6b-eaf4-4a28-b7f9-e6b001dae437', '20cb14b9-dee0-4851-b44c-b0c5d9dbb45f', 'b42032cd-08c7-46dc-9cf8-46592329852e', 'fdef75ff-9a60-442d-97ea-1896813f551e', 'dc06f989-a79e-4383-a82d-2d1eed224268', '33c2ad3c-b1a2-4085-a92b-09005e067022', 'a238238e-6ba7-4a9c-95ff-c3a7ec2eba76', 'c3781602-b1ad-44a4-825f-5c045f1ab91b', '5a806a90-cbc7-42eb-a382-d43c64aa5568', '13e9737d-d2a6-4573-ab75-af7be2abb133', '7053bc15-a53c-4cb4-9f25-570b0ba9e072', '7995ab9d-ca0f-4b80-ab44-a906db7ea063', '6217e11c-32bb-431d-b291-766eb3a0a311', '79e4de41-6985-442a-ad58-e06ba5b273bd', '27f6cb89-85a6-4c2d-917a-ee32fda7e6f1', '2ed2c02d-9d95-452a-ad66-bdab8ae5a955', '5eaaaa1a-fda7-4609-85b0-3874c490e7d4', '3f19b7ee-7260-4643-989d-beeeb06e2715', '40771fa4-b7e5-4a70-a5fe-7d15b558e1b1', 'd6ffb233-13c7-4d21-a04d-09f4f26612dc', 'dcf683cc-eedf-4d09-958d-609e831302f7', '6f9f4afc-735c-464d-81c5-3a6a9fe6c8ae', '8eb96b1e-3176-4592-90c2-266cf2944104', '03c944b1-4290-4343-8d29-2a1ff78181b7', '546f1f9e-4885-4b61-9952-dd68ffd14946', '67b7044a-7bdb-4941-99fe-54100c81be66', 'eb4fad34-0294-4d5a-81fe-4c9da7d3fc14', '269c693f-32e8-45aa-b228-474b22c7ce27', '5524e967-fdea-4547-af82-fe0b90d6b9cd', '5d7aa9b1-5b96-4f88-bc5e-7f35bdfae48b']
    if (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnMore')):
        assert False
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnPortrait')):
        assert False
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'faceRetouchAutoSwitch')):
        assert False
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Reshape')):
        assert False
    with step('[Verify] snapshot: 04_01_04_face_width_default.png'):
        actions.capture_for_gt('04_01_04_face_width_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_face_width_min.png'):
        actions.capture_for_gt('04_01_04_face_width_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_face_width_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_face_width_max.png'):
        actions.capture_for_gt('04_01_04_face_width_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_face_width_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Jaw')):
        assert False
    with step('[Verify] snapshot: 04_01_04_face_jaw_default.png'):
        actions.capture_for_gt('04_01_04_face_jaw_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_face_jaw_min.png'):
        actions.capture_for_gt('04_01_04_face_jaw_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_face_jaw_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_face_jaw_max.png'):
        actions.capture_for_gt('04_01_04_face_jaw_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_face_jaw_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Forehead')):
        assert False
    with step('[Verify] snapshot: 04_01_04_face_forehead_default.png'):
        actions.capture_for_gt('04_01_04_face_forehead_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_face_forehead_min.png'):
        actions.capture_for_gt('04_01_04_face_forehead_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_face_forehead_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_face_forehead_max.png'):
        actions.capture_for_gt('04_01_04_face_forehead_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_face_forehead_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Chin')):
        assert False
    with step('[Verify] snapshot: 04_01_04_face_chin_default.png'):
        actions.capture_for_gt('04_01_04_face_chin_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_face_chin_min.png'):
        actions.capture_for_gt('04_01_04_face_chin_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_face_chin_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_face_chin_max.png'):
        actions.capture_for_gt('04_01_04_face_chin_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_face_chin_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushSizeSliderView')):
        assert False
    with step('[Verify] snapshot: 04_01_04_eye_size_default.png'):
        actions.capture_for_gt('04_01_04_eye_size_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_eye_size_min.png'):
        actions.capture_for_gt('04_01_04_eye_size_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_eye_size_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_eye_size_max.png'):
        actions.capture_for_gt('04_01_04_eye_size_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_eye_size_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Distance')):
        assert False
    with step('[Verify] snapshot: 04_01_04_eye_distance_default.png'):
        actions.capture_for_gt('04_01_04_eye_distance_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_eye_distance_min.png'):
        actions.capture_for_gt('04_01_04_eye_distance_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_eye_distance_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_eye_distance_max.png'):
        actions.capture_for_gt('04_01_04_eye_distance_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_eye_distance_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Height')):
        assert False
    with step('[Verify] snapshot: 04_01_04_eye_height_default.png'):
        actions.capture_for_gt('04_01_04_eye_height_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_eye_height_min.png'):
        actions.capture_for_gt('04_01_04_eye_height_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_eye_height_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_eye_height_max.png'):
        actions.capture_for_gt('04_01_04_eye_height_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_eye_height_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Distance')):
        assert False
    with step('[Verify] snapshot: 04_01_04_eyebrow_distance_default.png'):
        actions.capture_for_gt('04_01_04_eyebrow_distance_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_eyebrow_distance_min.png'):
        actions.capture_for_gt('04_01_04_eyebrow_distance_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_eyebrow_distance_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_eyebrow_distance_max.png'):
        actions.capture_for_gt('04_01_04_eyebrow_distance_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_eyebrow_distance_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Height')):
        assert False
    with step('[Verify] snapshot: 04_01_04_eyebrow_height_default.png'):
        actions.capture_for_gt('04_01_04_eyebrow_height_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_eyebrow_height_min.png'):
        actions.capture_for_gt('04_01_04_eyebrow_height_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_eyebrow_height_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_eyebrow_height_max.png'):
        actions.capture_for_gt('04_01_04_eyebrow_height_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_eyebrow_height_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Thickness')):
        assert False
    with step('[Verify] snapshot: 04_01_04_eyebrow_thickness_default.png'):
        actions.capture_for_gt('04_01_04_eyebrow_thickness_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_eyebrow_thickness_min.png'):
        actions.capture_for_gt('04_01_04_eyebrow_thickness_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_eyebrow_thickness_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_eyebrow_thickness_max.png'):
        actions.capture_for_gt('04_01_04_eyebrow_thickness_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_eyebrow_thickness_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushSizeSliderView')):
        assert False
    with step('[Verify] snapshot: 04_01_04_nose_size_default.png'):
        actions.capture_for_gt('04_01_04_nose_size_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_nose_size_min.png'):
        actions.capture_for_gt('04_01_04_nose_size_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_nose_size_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_nose_size_max.png'):
        actions.capture_for_gt('04_01_04_nose_size_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_nose_size_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ala')):
        assert False
    with step('[Verify] snapshot: 04_01_04_nose_ala_default.png'):
        actions.capture_for_gt('04_01_04_nose_ala_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_nose_ala_min.png'):
        actions.capture_for_gt('04_01_04_nose_ala_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_nose_ala_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_nose_ala_max.png'):
        actions.capture_for_gt('04_01_04_nose_ala_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_nose_ala_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'brushSizeSliderView')):
        assert False
    with step('[Verify] snapshot: 04_01_04_lips_size_default.png'):
        actions.capture_for_gt('04_01_04_lips_size_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_lips_size_min.png'):
        actions.capture_for_gt('04_01_04_lips_size_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_lips_size_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_lips_size_max.png'):
        actions.capture_for_gt('04_01_04_lips_size_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_lips_size_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Height')):
        assert False
    with step('[Verify] snapshot: 04_01_04_lips_height_default.png'):
        actions.capture_for_gt('04_01_04_lips_height_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_lips_height_min.png'):
        actions.capture_for_gt('04_01_04_lips_height_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_lips_height_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_lips_height_max.png'):
        actions.capture_for_gt('04_01_04_lips_height_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_lips_height_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Thickness')):
        assert False
    with step('[Verify] snapshot: 04_01_04_lips_thickness_default.png'):
        actions.capture_for_gt('04_01_04_lips_thickness_default.png', crop_rect=(9, 636, 315, 677))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '0')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_lips_thickness_min.png'):
        actions.capture_for_gt('04_01_04_lips_thickness_min.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_lips_thickness_min.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False  # legacy raise
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[-1]', '1')):
        assert False  # legacy raise
    with step('[Verify] snapshot: 04_01_04_lips_thickness_max.png'):
        actions.capture_for_gt('04_01_04_lips_thickness_max.png', crop_rect=(9, 636, 315, 677))
    if (not actions.compare_with_gt('04_01_04_lips_thickness_max.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'lips_thickness max fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto')):
        assert False  # legacy raise
    if actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1):
        pass
    else:
        assert False  # legacy raise
    if (not actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose')):
        assert False  # legacy raise
    with step("[Verify] test_00014 completion"):
        assert True
