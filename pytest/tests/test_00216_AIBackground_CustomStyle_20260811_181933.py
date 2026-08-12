import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00216_AIBackground_CustomStyle_20260811_181933")
def test_00216_AIBackground_CustomStyle_20260811_181933(actions: DriverActions):
    with step("[Action] Tap Edit at (62.9%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 62.9, 52.0)
    with step("[Action] Tap btnAlbum at (86.8%, 61.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 86.8, 61.9)
    with step("[Action] Tap Sample Photos at (34.1%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 34.1, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap PhDM_example_3 at (40.8%, 60.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_3', 40.8, 60.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (68.9%, 46.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 68.9, 46.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until Background"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'Background', direction='left', offset_start=(0.449, 0.371), offset_end=(0.277, 0.371), velocity=155)
    with step("[Action] Tap Background at (23.6%, 28.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Background', 23.6, 28.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap AI Background at (51.9%, 100.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Background', 51.9, 100.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='effectMenuCollectionViewPresenterCollectionView', container_w=168, container_h=89)
    with step("[Action] Tap Custom at (64.5%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Custom', 64.5, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='styleCollectionView', container_w=430, container_h=84)
    with step("[Verify] promptTextView text equals 'Please provide a description of the background's appearance or characteristics.'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 'Please provide a description of the background\'s appearance or characteristics.')
    with step("[Action] Tap styleNameTextField at (21.6%, 52.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'styleNameTextField', 21.6, 52.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='contentView', container_w=430, container_h=701)
    with step("[Action] Five tap delete at (44.6%, 28.6%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'delete', 44.6, 28.6)
    with step("[Action] Type 'Custom name 1' into delete"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'delete', 'Custom name 1')
    with step("[Action] Tap promptTextView at (28.2%, 29.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 28.2, 29.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='contentView', container_w=430, container_h=701)
    with step("[Action] Type 'Taipei street' into promptTextView"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 'Taipei street')
    with step("[Verify] promptTextView text equals 'Taipei street'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 'Taipei street')
    with step("[Verify] styleNameTextField text equals 'Custom name 1'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'styleNameTextField', 'Custom name 1')
    with step("[Action] Tap clearButton at (54.5%, 59.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'clearButton', 54.5, 59.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='contentView', container_w=430, container_h=701)
    with step("[Verify] promptTextView text equals 'Please provide a description of the background's appearance or characteristics.'"):
        actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 'Please provide a description of the background\'s appearance or characteristics.')
    with step("[Action] Tap promptTextView at (36.3%, 34.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 36.3, 34.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='contentView', container_w=430, container_h=701)
    with step("[Action] Type 'Taipei street' into promptTextView"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptTextView', 'Taipei street')
    with step("[Action] Tap Next: at (57.0%, 48.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 57.0, 48.2)
    with step("[Action] Tap Generate at (58.8%, 29.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 58.8, 29.2)
    with step("[Verify] Retry is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Retry')
    with step("[Action] Tap btn_ok_n at (79.6%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 79.6, 69.4)
    with step("[Action] Tap homeButton at (80.8%, 38.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 80.8, 38.5)
    with step("[Action] Tap Discard at (50.7%, 29.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 50.7, 29.2)
    assert True
