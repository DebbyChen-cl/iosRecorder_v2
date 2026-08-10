import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00015_main_04_01_05')
def test_00015_main_04_01_05(actions: DriverActions):
    """camera - retouch - others"""
    uuid = ['cc8538b1-944f-4adc-836a-11f788ffe453', '006fc6bd-9dfd-4b9f-ab7c-63a75af7804b', '796eaa9a-776e-448a-ac29-e51536fab29a', '3d16da87-a4d4-4fd6-8ca7-877b18b68e9f', 'c674aa22-095c-49de-9fa6-84fd4944f770', '782afe58-9afb-42e1-b887-51cd863b7e0e', 'e4a3974d-71af-4006-81f5-a5620b1d6d9e', '6ca7983d-5058-4f8c-b103-d7a7cf47430c', 'ba37bd19-0a54-43c3-8b13-5fe6115ca89c', '64881f1b-3335-484c-ae23-1b1e1e30d264', '3df7f06d-3bff-4dcf-98e8-55fe1115b766', '767917bc-740a-4981-af87-7a61490fefa2', '5c3cbb5b-2a79-4b93-a1b1-3c0ba4576df1', 'df5565c2-f401-4ed4-9e66-9d3cadd373ac', '5de7d8e4-ffc4-410d-bb50-c83566d22a2b', '65273e03-e77a-459e-b087-cc090f885128', 'e8cfb976-a5c4-410a-aa74-2cbde764f016', '5724974c-fbe6-4490-a4c7-382b78bf9740', 'ff4942e5-f608-4257-bf2f-d373194f2263', '70778ba6-cb62-4ecd-a601-3f4a5d922833', '3448aeab-de7d-4a87-881c-2dbf374e3f59', '245a3616-5115-4b73-9a30-54b0f5e42cf3', 'b789e0d8-22f7-43f0-b3b2-a3ed16ca2b60']
    with step("[Action] Tap Camera at (34.8%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Camera', 34.8, 64.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=430, container_h=843)
    with step("[Action] Tap btnPortrait at (44.3%, 23.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnPortrait', 44.3, 23.8)
    with step("[Action] Tap ic_auto_retouch at (70.0%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_auto_retouch', 70.0, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Tap faceRetouchAutoSwitch at (56.0%, 46.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'faceRetouchAutoSwitch', 56.0, 46.0)
    with step("[Action] Tap faceRetouchAutoSwitch at (63.8%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'faceRetouchAutoSwitch', 63.8, 46.9)
    with step("[Action] Tap ic_conceal_portrait at (60.0%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_conceal_portrait', 60.0, 67.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Drag cpSlider (28.4%,52.4%) → slider (41.0%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 28.4, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 41.5, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (45.0%,45.2%) → slider (82.8%,53.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 45.0, 45.2, AppiumBy.ACCESSIBILITY_ID, 'slider', 82.8, 53.1, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap btnTakePhoto at (72.2%, 39.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 72.2, 39.6)
    with step("[Verify] Continue is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnClose at (35.5%, 41.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 35.5, 41.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap ic_skin_smooth at (70.0%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_skin_smooth', 70.0, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Drag cpSlider (77.1%,57.1%) → slider (42.0%,51.2%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 77.1, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 42.0, 51.2, duration=1.0)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (45.0%,54.8%) → slider (98.4%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 45.0, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 98.4, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap ic_skintone_portrait at (55.0%, 45.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_skintone_portrait', 55.0, 45.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Drag centerSlider (50.0%,45.2%) → slider (2.9%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 50.0, 45.2, AppiumBy.ACCESSIBILITY_ID, 'slider', 2.9, 53.7, duration=1.0)
    with step("[Verify] valueLabel text equals '-100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '-100')
    with step("[Action] Drag centerSlider (6.8%,52.4%) → slider (97.4%,53.7%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'centerSlider', 6.8, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 97.4, 53.7, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap btnTakePhoto at (63.0%, 73.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 63.0, 73.6)
    with step("[Verify] Continue is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnClose at (54.8%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 54.8, 51.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap ic_teeth_whiten_portrait at (52.5%, 67.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_teeth_whiten_portrait', 52.5, 67.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Drag cpSlider (7.4%,64.3%) → slider (41.5%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.4, 64.3, AppiumBy.ACCESSIBILITY_ID, 'slider', 41.5, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (45.0%,52.4%) → valueLabel (10.3%,43.9%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 45.0, 52.4, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 10.3, 43.9, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap btnTakePhoto at (59.3%, 77.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 59.3, 77.4)
    with step("[Verify] Continue is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnClose at (45.2%, 29.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 45.2, 29.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap ic_eyebag_removal at (62.5%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_eyebag_removal', 62.5, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Drag cpSlider (6.8%,47.6%) → slider (41.0%,48.8%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 6.8, 47.6, AppiumBy.ACCESSIBILITY_ID, 'slider', 41.0, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (45.0%,54.8%) → slider (83.6%,49.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 45.0, 54.8, AppiumBy.ACCESSIBILITY_ID, 'slider', 83.6, 49.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap btnTakePhoto at (68.5%, 67.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 68.5, 67.9)
    with step("[Verify] Continue is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnClose at (58.1%, 67.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 58.1, 67.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap ic_eye_brighten_portrait at (57.5%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_eye_brighten_portrait', 57.5, 65.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Drag cpSlider (29.7%,52.4%) → slider (41.5%,48.8%)"):
            actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 29.7, 52.4, AppiumBy.ACCESSIBILITY_ID, 'slider', 41.5, 48.8, duration=1.0)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (45.0%,61.9%) → slider (84.2%,46.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 45.0, 61.9, AppiumBy.ACCESSIBILITY_ID, 'slider', 84.2, 46.0, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap btnTakePhoto at (53.7%, 75.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 53.7, 75.5)
    with step("[Verify] buyFlowLightButton is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    with step("[Action] Tap btnClose at (61.3%, 77.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 61.3, 77.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap ic_oilness at (72.5%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_oilness', 72.5, 75.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='lookEffectCollectionViewCollectionView', container_w=430, container_h=94)
    with step("[Action] Drag cpSlider (7.7%,57.1%) → slider (42.0%,56.1%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 7.7, 57.1, AppiumBy.ACCESSIBILITY_ID, 'slider', 42.0, 56.1, duration=1.0)
    with step("[Verify] valueLabel text equals '50'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50')
    with step("[Action] Drag cpSlider (45.0%,59.5%) → valueLabel (15.5%,63.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 45.0, 59.5, AppiumBy.ACCESSIBILITY_ID, 'valueLabel', 15.5, 63.4, duration=1.0)
    with step("[Verify] valueLabel text equals '100'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100')
    with step("[Action] Tap btnTakePhoto at (77.8%, 22.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnTakePhoto', 77.8, 22.6)
    with step("[Verify] Continue is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnClose at (64.5%, 41.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 64.5, 41.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='featureCarouselItemCollectionView', container_w=430, container_h=514)
    with step("[Action] Tap btnHome at (65.0%, 52.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 65.0, 52.5)
    with step("[Verify] test_00015 completion"):
        assert True
