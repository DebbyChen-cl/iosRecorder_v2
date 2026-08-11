import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00181_2_ai_try_on_07_dontshowagain_20260807_143302")
def test_00181_2_ai_try_on_07_dontshowagain_20260807_143302(actions: DriverActions):
    with step("[Action] Tap AI Photos at (66.7%, 81.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Photos', 66.7, 81.8)
    with step("[Action] Tap AI Try-On at (95.5%, 44.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', 95.5, 44.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap notShowAgainCheckBox at (55.6%, 37.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox', 55.6, 37.0)
    with step("[Action] Tap thumbnailImageView at (64.4%, 87.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'thumbnailImageView', 64.4, 87.3)
    with step("[Action] Tap importLabel at (70.4%, 47.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importLabel', 70.4, 47.5)
    with step("[Action] Tap PhotoPickerRecommendDialog-notShowAgainCheckBox at (48.1%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox', 48.1, 55.6)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (75.9%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 75.9, 49.0)
    with step("[Action] Tap btnAlbum at (86.3%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 86.3, 33.3)
    with step("[Action] Tap _AT at (9.0%, 60.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.0, 60.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-2 at (32.3%, 51.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 32.3, 51.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap navBackButton at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 50.0, 50.0)
    with step("[Action] Tap btnHome at (51.3%, 47.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 51.3, 47.3)
    with step("[Action] Tap Edit at (68.6%, 64.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 68.6, 64.0)
    with step("[Action] Tap photoCell-2 at (27.7%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2', 27.7, 46.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (41.9%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 41.9, 48.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until AI Try-On"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', direction='left', offset_start=(0.791, 0.433), offset_end=(0.158, 0.433), velocity=483)
    with step("[Action] Tap AI Try-On at (73.6%, 26.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Try-On', 73.6, 26.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=431, container_h=97)
    with step("[Verify] Generate is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Action] Tap importButton at (47.5%, 54.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'importButton', 47.5, 54.3)
    with step("[Verify] btnAlbum is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap btnBack at (60.0%, 46.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 60.0, 46.3)
    with step("[Action] Tap navBackButton at (47.5%, 55.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 47.5, 55.0)
    with step("[Action] Tap homeButton at (53.8%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 53.8, 69.2)
    assert True
