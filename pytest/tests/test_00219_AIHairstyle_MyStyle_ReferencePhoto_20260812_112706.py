import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00219_AIHairstyle_MyStyle_ReferencePhoto_20260812_112706")
def test_00219_AIHairstyle_MyStyle_ReferencePhoto_20260812_112706(actions: DriverActions):
    with step("[Action] Tap AI Photos at (58.3%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 58.3, 72.7)
    with step("[Action] Scroll until AI Hairstyle"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle', direction='down', offset_start=(0.28, 0.141), offset_end=(0.28, 0.064), velocity=84)
    with step("[Action] Tap AI Hairstyle at (23.1%, 63.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle', 23.1, 63.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap importLabel at (72.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importLabel', 72.2, 50.0)
    with step("[Action] Tap btnAlbum at (79.7%, 52.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 79.7, 52.4)
    with step("[Action] Tap _AT at (11.5%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 11.5, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (45.4%, 63.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 45.4, 63.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap My Style at (82.8%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Style', 82.8, 70.0)
    with step("[Action] Tap Photos at (60.8%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Photos', 60.8, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=33)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeImage at (50.0%, 45.2%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeImage', 50.0, 45.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=319)
    with step("[Action] Tap Generate at (91.4%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 91.4, 33.3)
    with step("[Verify] selectCheckBoxOverlay disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'selectCheckBoxOverlay', appear_timeout=5, disappear_timeout=1200), 'selectCheckBoxOverlay did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (51.6%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 51.6, 64.5)
    with step("[Action] Long press //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeImage at (48.9%, 47.6%)"):
        actions.long_press_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeImage', 48.9, 47.6, duration=1.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=319)
    with step("[Action] Tap ic delete at (61.3%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic delete', 61.3, 54.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=319)
    with step("[Verify] Delete My Style? is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete My Style?')
    with step("[Action] Tap Cancel at (87.1%, 41.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 87.1, 41.7)
    with step("[Action] Tap navBackButton at (57.5%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 57.5, 55.0)
    with step("[Action] Tap Home at (54.2%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Home', 54.2, 54.5)
    assert True
