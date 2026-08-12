import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00222_AITryOn_MyStlye_TextPrompt_20260812_141850")
def test_00222_AITryOn_MyStlye_TextPrompt_20260812_141850(actions: DriverActions):
    with step("[Action] Tap AI Photos at (63.9%, 72.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 63.9, 72.7)
    with step("[Action] Scroll until AI Try-On"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', direction='down', offset_start=(0.407, 0.171), offset_end=(0.407, 0.133), velocity=50)
    with step("[Action] Tap AI Try-On at (72.7%, 77.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', 72.7, 77.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap importLabel at (68.5%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importLabel', 68.5, 47.5)
    with step("[Action] Tap btnAlbum at (81.7%, 71.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 81.7, 71.4)
    with step("[Action] Tap _AT at (15.1%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 15.1, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (27.7%, 68.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 27.7, 68.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap My Style at (38.5%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Style', 38.5, 40.0)
    with step("[Action] Tap Prompts at (33.7%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Prompts', 33.7, 44.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=33)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell at (62.9%, 75.9%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell', 62.9, 75.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeButton at (48.8%, 56.1%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeButton', 48.8, 56.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Verify] //XCUIElementTypeApplication[@name=\"PhotoDirector\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther')
    with step("[Action] Tap btnReuse at (9.0%, 75.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnReuse', 9.0, 75.0)
    with step("[Verify] promptField is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'promptField')
    with step("[Action] Tap promptApplyButton at (60.9%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptApplyButton', 60.9, 53.1)
    with step("[Action] Tap btnGenerate at (14.8%, 43.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 14.8, 43.5)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (25.8%, 71.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 25.8, 71.0)
    with step("[Action] Tap My Style at (75.4%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Style', 75.4, 50.0)
    with step("[Action] Tap Prompts at (66.3%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Prompts', 66.3, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=33)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeButton at (36.6%, 56.1%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeButton', 36.6, 56.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Action] Tap btnDelete at (40.8%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDelete', 40.8, 42.9)
    with step("[Verify] Delete My Style? is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete My Style?')
    with step("[Action] Tap Cancel at (24.1%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 24.1, 50.0)
    with step("[Action] Tap btn_cancel_n at (30.6%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 30.6, 55.1)
    with step("[Action] Long press //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell at (78.5%, 26.6%)"):
        actions.long_press_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell', 78.5, 26.6, duration=1.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Action] Tap ic delete at (59.4%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic delete', 59.4, 51.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=323)
    with step("[Verify] Delete My Style? is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete My Style?')
    with step("[Action] Tap Cancel at (15.2%, 62.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 15.2, 62.0)
    with step("[Action] Tap navBackButton at (45.0%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 45.0, 55.0)
    with step("[Action] Tap btnHome at (21.1%, 36.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 21.1, 36.4)
    assert True
