import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00218_AIHairstyle_MyStyle_TextPrompt_20260812_112030")
def test_00218_AIHairstyle_MyStyle_TextPrompt_20260812_112030(actions: DriverActions):
    with step("[Action] Tap AI Photos at (45.8%, 40.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 45.8, 40.9)
    with step("[Action] Scroll until AI Hairstyle"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle', direction='down', offset_start=(0.356, 0.442), offset_end=(0.356, 0.365), velocity=113)
    with step("[Action] Tap AI Hairstyle at (71.8%, 15.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Hairstyle', 71.8, 15.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap importLabel at (1.9%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importLabel', 1.9, 55.0)
    with step("[Action] Tap btnAlbum at (91.9%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 91.9, 66.7)
    with step("[Action] Tap _AT at (7.9%, 69.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 69.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (46.2%, 42.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 46.2, 42.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap My Style at (48.4%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Style', 48.4, 55.0)
    with step("[Action] Tap Prompts at (65.1%, 48.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Prompts', 65.1, 48.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=33)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeButton at (65.9%, 48.8%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeButton', 65.9, 48.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=319)
    with step("[Verify] //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther')
    with step("[Action] Tap Reuse & Edit at (39.3%, 22.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Reuse & Edit', 39.3, 22.2)
    with step("[Verify] promptField is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'promptField')
    with step("[Action] Tap Apply at (80.4%, 65.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Apply', 80.4, 65.2)
    with step("[Action] Tap Generate at (58.0%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 58.0, 66.7)
    with step("[Verify] selectCheckBoxOverlay disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'selectCheckBoxOverlay', appear_timeout=5, disappear_timeout=1200), 'selectCheckBoxOverlay did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (58.1%, 80.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 58.1, 80.6)
    with step("[Action] Tap My Style at (40.6%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Style', 40.6, 30.0)
    with step("[Action] Tap Prompts at (59.0%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Prompts', 59.0, 44.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=33)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeButton at (56.1%, 36.6%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeButton', 56.1, 36.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=319)
    with step("[Action] Tap btnDelete at (59.2%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDelete', 59.2, 53.1)
    with step("[Action] Tap Cancel at (87.1%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 87.1, 83.3)
    with step("[Action] Tap btn_cancel_n at (51.0%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 51.0, 51.0)
    with step("[Verify] //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeButton is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeButton')
    with step("[Action] Long press //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell at (72.2%, 63.3%)"):
        actions.long_press_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell', 72.2, 63.3, duration=1.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=319)
    with step("[Action] Tap ic delete at (56.2%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic delete', 56.2, 51.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=319)
    with step("[Verify] Delete My Style? is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete My Style?')
    with step("[Action] Tap Cancel at (67.7%, 45.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 67.7, 45.8)
    with step("[Action] Tap navBackButton at (47.5%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 47.5, 60.0)
    with step("[Action] Tap btnHome at (57.9%, 38.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 57.9, 38.2)
    assert True
