import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00014_main_04_01_04')
def test_00014_main_04_01_04(actions: DriverActions):
    """camera - retouch - reshape"""
    uuid = ['7f001c37-a250-44fd-9e15-ae5ee2919068', 'd1458b6b-eaf4-4a28-b7f9-e6b001dae437', '20cb14b9-dee0-4851-b44c-b0c5d9dbb45f', 'b42032cd-08c7-46dc-9cf8-46592329852e', 'fdef75ff-9a60-442d-97ea-1896813f551e', 'dc06f989-a79e-4383-a82d-2d1eed224268', '33c2ad3c-b1a2-4085-a92b-09005e067022', 'a238238e-6ba7-4a9c-95ff-c3a7ec2eba76', 'c3781602-b1ad-44a4-825f-5c045f1ab91b', '5a806a90-cbc7-42eb-a382-d43c64aa5568', '13e9737d-d2a6-4573-ab75-af7be2abb133', '7053bc15-a53c-4cb4-9f25-570b0ba9e072', '7995ab9d-ca0f-4b80-ab44-a906db7ea063', '6217e11c-32bb-431d-b291-766eb3a0a311', '79e4de41-6985-442a-ad58-e06ba5b273bd', '27f6cb89-85a6-4c2d-917a-ee32fda7e6f1', '2ed2c02d-9d95-452a-ad66-bdab8ae5a955', '5eaaaa1a-fda7-4609-85b0-3874c490e7d4', '3f19b7ee-7260-4643-989d-beeeb06e2715', '40771fa4-b7e5-4a70-a5fe-7d15b558e1b1', 'd6ffb233-13c7-4d21-a04d-09f4f26612dc', 'dcf683cc-eedf-4d09-958d-609e831302f7', '6f9f4afc-735c-464d-81c5-3a6a9fe6c8ae', '8eb96b1e-3176-4592-90c2-266cf2944104', '03c944b1-4290-4343-8d29-2a1ff78181b7', '546f1f9e-4885-4b61-9952-dd68ffd14946', '67b7044a-7bdb-4941-99fe-54100c81be66', 'eb4fad34-0294-4d5a-81fe-4c9da7d3fc14', '269c693f-32e8-45aa-b228-474b22c7ce27', '5524e967-fdea-4547-af82-fe0b90d6b9cd', '5d7aa9b1-5b96-4f88-bc5e-7f35bdfae48b']
    with step("[Action] Tap Camera at (53.6%, 44.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Camera', 53.6, 44.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnPortrait at (46.8%, 41.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPortrait', 46.8, 41.3)
    with step("[Action] Tap ic_face_reshape_portrait at (80.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_reshape_portrait', 80.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)

    elements = ['ic_face_width', 'ic_jaw', 'ic_forhead', 'ic_chin', 'ic_eye_size', 'ic_eye_span', 'ic_eye_height', 'ic_brow_span', 'ic_brow_height', 'ic_brow_thickness', 'ic_nose_size', 'ic_nose_ala', 'ic_mouth_size', 'ic_mouth_height', 'ic_mouth_thickness']

    for ele in elements:
        with step(f"[Action] Tap {ele} at (60.0%, 63.4%)"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, ele, 60.0, 63.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=93)
        with step("[Verify] Capture 'screenshot' before screenshot"):
            assert actions.capture_for_preview('screenshot', f'before_min_{ele}', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.CameraProViewController"]/XCUIElementTypeOther[5]')
        with step("[Action] Drag centerSlider (51.3%,59.5%) → slider (1.0%,63.4%)"):
            actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 51.3, 59.5, AppiumBy.ACCESSIBILITY_ID, 'slider', 1.0, 63.4, duration=1.0)
        with step("[Verify] Capture 'screenshot' after screenshot"):
            assert actions.capture_for_preview('screenshot', f'after_min_{ele}', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.CameraProViewController"]/XCUIElementTypeOther[5]', expected_result='different', threshold=0.99)
        with step("[Verify] Capture 'screenshot' before screenshot"):
            assert actions.capture_for_preview('screenshot', f'before_max_{ele}', AppiumBy.XPATH,'//XCUIElementTypeOther[@name="photodirector.CameraProViewController"]/XCUIElementTypeOther[5]')
        with step("[Action] Drag centerSlider (6.8%,59.5%) → slider (99.7%,51.2%)"):
            actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.8, 59.5, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.7, 51.2, duration=1.0)
        with step("[Verify] Capture 'screenshot' after screenshot"):
            assert actions.capture_for_preview('screenshot', f'after_max_{ele}', AppiumBy.XPATH,'//XCUIElementTypeOther[@name="photodirector.CameraProViewController"]/XCUIElementTypeOther[5]', expected_result='different', threshold=0.99)

    with step("[Action] Tap btnTakePhoto at (59.3%, 52.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 59.3, 52.8)
    with step("[Action] Tap btnClose at (64.5%, 41.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 64.5, 41.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btnHome at (55.0%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 55.0, 65.0)

    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.995)
    with step("[Verify] test_00014 completion"):
        assert True
