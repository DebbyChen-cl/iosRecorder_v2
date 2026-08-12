import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00223_AITryOn_MyStyle_ReferencePhoto_20260812_142439")
def test_00223_AITryOn_MyStyle_ReferencePhoto_20260812_142439(actions: DriverActions):
    with step("[Action] Tap btnStudio at (14.5%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnStudio', 14.5, 54.5)
    with step("[Action] Scroll until AI Try-On"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', direction='down', offset_start=(0.783, 0.131), offset_end=(0.783, 0.088), velocity=50)
    with step("[Action] Tap AI Try-On at (68.2%, 63.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', 68.2, 63.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap importButton at (11.9%, 79.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importButton', 11.9, 79.3)
    with step("[Action] Tap btnAlbum at (78.7%, 54.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 78.7, 54.8)
    with step("[Action] Tap _AT at (25.4%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 25.4, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (56.9%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 56.9, 40.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap My Style at (30.8%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Style', 30.8, 80.0)
    with step("[Action] Tap Photos at (44.6%, 59.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Photos', 44.6, 59.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=33)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage at (48.9%, 58.7%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage', 48.9, 58.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=305)
    with step("[Action] Tap btnGenerate at (20.6%, 56.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 20.6, 56.5)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (41.9%, 16.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 41.9, 16.1)
    with step("[Action] Tap NonScrollableSegment-myStyle at (26.2%, 76.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'NonScrollableSegment-myStyle', 26.2, 76.1)
    with step("[Action] Tap Photos at (9.5%, 59.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Photos', 9.5, 59.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='titleCollectionViewCollectionView', container_w=430, container_h=33)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell[2]/XCUIElementTypeOther[1]/XCUIElementTypeImage at (40.9%, 50.0%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell[2]/XCUIElementTypeOther[1]/XCUIElementTypeImage', 40.9, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=305)
    with step("[Verify] Select up to 3 apparel photos. (2/3) is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Select up to 3 apparel photos. (2/3)')
    with step("[Action] Tap btnGenerate at (13.2%, 66.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 13.2, 66.1)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (74.2%, 83.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 74.2, 83.9)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell[3]/XCUIElementTypeOther[1]/XCUIElementTypeImage at (36.4%, 59.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell[3]/XCUIElementTypeOther[1]/XCUIElementTypeImage', 36.4, 59.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=305)
    with step("[Verify] Select up to 3 apparel photos. (3/3) is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Select up to 3 apparel photos. (3/3)')
    with step("[Action] Tap btnGenerate at (20.6%, 64.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 20.6, 64.5)
    with step("[Verify] statusLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'statusLabel', appear_timeout=5, disappear_timeout=1200), 'statusLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (54.8%, 93.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 54.8, 93.5)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell[4]/XCUIElementTypeOther[1]/XCUIElementTypeImage at (30.7%, 42.1%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell[4]/XCUIElementTypeOther[1]/XCUIElementTypeImage', 30.7, 42.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=305)
    with step("[Verify] Select up to 3 apparel photos. (3/3) is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Select up to 3 apparel photos. (3/3)')
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell[3]/XCUIElementTypeOther[1]/XCUIElementTypeImage at (55.7%, 46.8%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell[3]/XCUIElementTypeOther[1]/XCUIElementTypeImage', 55.7, 46.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=305)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell[2]/XCUIElementTypeOther[1]/XCUIElementTypeImage at (47.7%, 51.6%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell[2]/XCUIElementTypeOther[1]/XCUIElementTypeImage', 47.7, 51.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=305)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage at (40.9%, 52.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage', 40.9, 52.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=305)
    with step("[Verify] Select up to 3 apparel photos. (0/3) is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Select up to 3 apparel photos. (0/3)')
    with step("[Action] Long press //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage at (52.3%, 53.2%)"):
        actions.long_press_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage', 52.3, 53.2, duration=1.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=305)
    with step("[Action] Tap ic delete at (54.8%, 51.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic delete', 54.8, 51.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=305)
    with step("[Verify] Delete My Style? is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete My Style?')
    with step("[Action] Tap Cancel at (13.3%, 56.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 13.3, 56.0)
    with step("[Action] Tap navBackButton at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 50.0, 50.0)
    with step("[Action] Tap btnHome at (30.3%, 50.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 30.3, 50.9)
    assert True
