import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00221_AIArt_MyStyle_20260812_115934")
def test_00221_AIArt_MyStyle_20260812_115934(actions: DriverActions):
    with step("[Action] Tap AI Photos at (66.7%, 77.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 66.7, 77.3)
    with step("[Action] Scroll until AI Art"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Art', direction='down', offset_start=(0.247, 0.192), offset_end=(0.247, 0.105), velocity=115)
    with step("[Action] Tap AI Art at (71.8%, 52.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Art', 71.8, 52.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap importLabel at (96.3%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importLabel', 96.3, 47.5)
    with step("[Action] Tap btnAlbum at (76.6%, 64.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 76.6, 64.3)
    with step("[Action] Tap _AT at (7.9%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (24.6%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 24.6, 46.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap My Style at (65.6%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Style', 65.6, 55.0)
    with step("[Verify] //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell is visible"):
        actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell')
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell at (59.3%, 68.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell', 59.3, 68.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=361)
    with step("[Action] Tap Generate at (37.0%, 83.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 37.0, 83.3)
    with step("[Verify] waitLabel disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'waitLabel', appear_timeout=5, disappear_timeout=1200), 'waitLabel did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (73.1%, 73.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 73.1, 73.1)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeButton at (63.4%, 63.4%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeButton', 63.4, 63.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=361)
    with step("[Verify] photodirector.ArtisticAvatarMyStyleDetailViewController is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'photodirector.ArtisticAvatarMyStyleDetailViewController')
    with step("[Action] Tap btn_cancel_n at (51.0%, 63.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 51.0, 63.3)
    with step("[Verify] photodirector.ArtisticAvatarMyStyleDetailViewController is not visible"):
        actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'photodirector.ArtisticAvatarMyStyleDetailViewController')
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeButton at (61.0%, 48.8%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeButton', 61.0, 48.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=361)
    with step("[Action] Tap btnReuse at (9.0%, 88.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnReuse', 9.0, 88.6)
    with step("[Verify] contentAreaGradientBackground is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'contentAreaGradientBackground')
    with step("[Action] Tap submitButton at (79.4%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'submitButton', 79.4, 45.5)
    with step("[Verify] Prompt is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Prompt')
    with step("[Action] Tap btnGenerate at (11.1%, 37.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnGenerate', 11.1, 37.1)
    with step("[Verify] In progress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'In progress', appear_timeout=5, disappear_timeout=1200), 'In progress did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btnBack at (61.5%, 84.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 61.5, 84.6)
    with step("[Action] Tap My Style at (65.6%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'My Style', 65.6, 40.0)
    with step("[Action] Long press //XCUIElementTypeCollectionView[@name=\"styleCollectionView\"]/XCUIElementTypeCell/XCUIElementTypeOther[2] at (61.6%, 63.3%)"):
        actions.long_press_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="styleCollectionView"]/XCUIElementTypeCell/XCUIElementTypeOther[2]', 61.6, 63.3, duration=1.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=361)
    with step("[Action] Tap ic delete at (50.0%, 38.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic delete', 50.0, 38.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=361)
    with step("[Verify] Delete My Style? is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Delete My Style?')
    with step("[Action] Tap Cancel at (66.1%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 66.1, 50.0)
    with step("[Action] Tap navBackButton at (65.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 65.0, 50.0)
    with step("[Action] Tap Home at (20.8%, 13.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Home', 20.8, 13.6)
    assert True
