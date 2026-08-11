import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00171_ai_face_swap_multi_20260807_111120")
def test_00171_ai_face_swap_multi_20260807_111120(actions: DriverActions):
    with step("[Action] Tap btnStudio at (64.5%, 32.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnStudio', 64.5, 32.7)
    with step("[Action] Scroll until AI Face Swap"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap', direction='down', offset_start=(0.278, 0.438), offset_end=(0.278, 0.354), velocity=50)
    with step("[Action] Tap AI Face Swap at (78.3%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap', 78.3, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap btnNext at (83.2%, 22.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 83.2, 22.4)
    with step("[Action] Tap btnNext at (87.1%, 80.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 87.1, 80.0)
    with step("[Action] Tap CMS-Style_204_Count&Countess at (52.4%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_204_Count&Countess', 52.4, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='templateSelection_styleCollectionView', container_w=394, container_h=643)
    with step("[Verify] hintLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'hintLabel')
    with step("[Action] Tap faceSelectionCell-0 at (63.4%, 33.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'faceSelectionCell-0', 63.4, 33.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='faceChooseCollectionView', container_w=430, container_h=88)
    with step("[Action] Tap faceSelectionCell-1 at (62.0%, 55.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'faceSelectionCell-1', 62.0, 55.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='faceChooseCollectionView', container_w=430, container_h=88)
    with step("[Action] Tap btnNext at (28.4%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 28.4, 50.0)
    with step("[Action] Tap addSourceFaceButton at (81.7%, 33.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'addSourceFaceButton', 81.7, 33.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='addFaceCollectionView', container_w=394, container_h=162)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (16.7%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 16.7, 28.6)
    with step("[Action] Tap btnAlbum at (90.4%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 90.4, 28.6)
    with step("[Action] Tap _AT at (7.9%, 39.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 7.9, 39.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-4 at (26.2%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4', 26.2, 46.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] faceValidationProgress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'faceValidationProgress', appear_timeout=5, disappear_timeout=1200), 'faceValidationProgress did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap faceSelectionCell-0 at (53.5%, 45.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'faceSelectionCell-0', 53.5, 45.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='faceChooseCollectionView', container_w=430, container_h=88)
    with step("[Action] Tap btnNext at (30.9%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 30.9, 36.7)
    with step("[Action] Tap addSourceFaceButton at (25.4%, 36.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'addSourceFaceButton', 25.4, 36.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='addFaceCollectionView', container_w=394, container_h=162)
    with step("[Action] Tap photoCell-5 at (56.9%, 75.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5', 56.9, 75.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] The face in this photo is too small or blurry, which may result in poorly generated results. is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'The face in this photo is too small or blurry, which may result in poorly generated results.')
    with step("[Action] Tap Continue Anyway at (11.1%, 54.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway', 11.1, 54.0)
    with step("[Verify] faceValidationProgress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'faceValidationProgress', appear_timeout=5, disappear_timeout=1200), 'faceValidationProgress did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap multipleAddFace_generateButton at (14.9%, 31.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'multipleAddFace_generateButton', 14.9, 31.7)
    with step("[Action] Tap btnClose at (71.0%, 54.8%)"):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnClose'):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 71.0, 54.8)
    with step("[Verify] Turn it into video is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Turn it into video')
    with step("[Action] Tap btnHome at (65.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 65.0, 50.0)
    with step("[Action] Tap btnSettings at (69.7%, 38.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 69.7, 38.2)
    with step("[Action] Tap //XCUIElementTypeImage[@name=\"SettingPageHelpCenterCell-1\"]/XCUIElementTypeOther[2] at (39.8%, 47.2%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="SettingPageHelpCenterCell-1"]/XCUIElementTypeOther[2]', 39.8, 47.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (24.5%, 12.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 24.5, 12.0)
    with step("[Action] Tap Free at (70.6%, 76.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 70.6, 76.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (62.8%, 53.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 62.8, 53.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (45.0%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 45.0, 58.3)
    with step("[Action] Tap btnBack at (50.0%, 53.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 50.0, 53.2)
    with step("[Action] Tap btnBack at (60.7%, 53.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 60.7, 53.2)
    with step("[Action] Tap btnStudio at (51.3%, 41.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnStudio', 51.3, 41.8)
    with step("[Action] Tap CMS-PhDM_AIMagic_AIFaceSwap_20255E at (70.0%, 30.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-PhDM_AIMagic_AIFaceSwap_20255E', 70.0, 30.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Action] Tap btnNext at (88.9%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 88.9, 55.1)
    with step("[Action] Tap btnNext at (88.1%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 88.1, 65.0)
    with step("[Action] Tap CMS-Style_204_Count&Countess at (48.4%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_204_Count&Countess', 48.4, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='templateSelection_styleCollectionView', container_w=394, container_h=643)
    with step("[Action] Tap faceSelectionCell-0 at (49.3%, 68.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'faceSelectionCell-0', 49.3, 68.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='faceChooseCollectionView', container_w=430, container_h=88)
    with step("[Action] Tap faceSelectionCell-1 at (66.2%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'faceSelectionCell-1', 66.2, 62.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='faceChooseCollectionView', container_w=430, container_h=88)
    with step("[Action] Tap btnNext at (68.0%, 28.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 68.0, 28.3)
    with step("[Action] Tap addSourceImageView at (48.4%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'addSourceImageView', 48.4, 48.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='addFaceCollectionView', container_w=394, container_h=162)
    with step("[Action] Tap PhotoPickerRecommendDialog-continueButton at (75.7%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-continueButton', 75.7, 44.9)
    with step("[Action] Tap photoCell-4 at (26.2%, 70.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4', 26.2, 70.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Verify] faceValidationProgress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'faceValidationProgress', appear_timeout=5, disappear_timeout=1200), 'faceValidationProgress did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap faceSelectionCell-0 at (60.6%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'faceSelectionCell-0', 60.6, 66.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='faceChooseCollectionView', container_w=430, container_h=88)
    with step("[Action] Tap btnNext at (71.4%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnNext', 71.4, 58.3)
    with step("[Action] Tap addSourceFaceButton at (7.0%, 47.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'addSourceFaceButton', 7.0, 47.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='addFaceCollectionView', container_w=394, container_h=162)
    with step("[Action] Tap photoCell-5 at (44.6%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5', 44.6, 53.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Continue Anyway at (80.7%, 76.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway', 80.7, 76.0)
    with step("[Verify] faceValidationProgress disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'faceValidationProgress', appear_timeout=5, disappear_timeout=1200), 'faceValidationProgress did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap multipleAddFace_generateButton at (58.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'multipleAddFace_generateButton', 58.0, 50.0)
    with step("[Verify] Turn it into video is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Turn it into video')
    with step("[Action] Tap btnSave at (55.0%, 65.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSave', 55.0, 65.0)
    with step("[Verify] navDescriptionLabel is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel')
    with step("[Action] Tap navHomeButton at (63.6%, 68.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton', 63.6, 68.9)
    assert True
