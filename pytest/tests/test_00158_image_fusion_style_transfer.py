import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00158_image_fusion_style_transfer')
def test_00158_image_fusion_style_transfer(actions: DriverActions):
    """image fusion style transfer"""
    uuid = ['e4cb6292-7d01-4837-81e9-981dded761a8', '37d63713-b6b0-4d13-a03e-f05bd7b672ca', '8febe979-63c9-4b1b-8a75-e89a20b9fcf4', '87e97656-7169-4906-a51e-b9d7ed6da216', 'ea5a1434-b99f-4859-8f43-774f7114acfe', '81217d76-4b83-4761-a009-c4c34a4f65fe', '0494f6b1-71e6-4f36-bf27-b8f25e633e0e', '249cff61-d196-4a0e-9750-6b2ccc46c164', '80f97972-d2b6-44ed-b11d-4df8509a3028', '3e48ce3d-e63a-495e-857a-59e3b53b9a1a', '7b0cdeb0-8f59-423f-b52b-04b389b207b9', 'a069c361-004a-43db-a13a-09b6d5131645', 'c072657b-853b-45ce-abcc-6af1087b7fef', '9dda788e-33c9-4ec6-9c71-3ba31a851f09', 'a5b9150e-fa89-4f2d-a970-b8b44fd63185', '0e5c3cc3-5ccf-4682-8558-3a87238ab36f', '2b70e28b-311d-464e-8b86-6a0904c56a6f', '5cbb239d-0741-4971-9f43-0d75be3f0457', 'c8b6f74a-88b5-48fc-90ab-996d28b42200', '3f47f9ff-d7ae-489f-bee1-bde79b5f41e7', 'bed5ba02-4d49-4b4f-9fd3-985c7be26ce0', '7691eccc-bc0e-43bb-a368-c858d2eef24b']
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    actions.scroll(direction='up')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style Transfer')
    assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblDesc')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_076_076')
    actions.capture_for_gt('G02_02_04_style.png')
    if actions.compare_with_gt('G02_02_04_style.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[G02_02_04] Compare fail for style'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnImportFace')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnSave'):
        pass
    else:
        assert False, '[G02_02_04] Failed to generate first image'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navBackButton')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ok')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    actions.capture_for_gt('G02_02_04_style2.png')
    if actions.compare_with_gt('G02_02_04_style2.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[G02_02_04] Compare fail for style2'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate More')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnSave'):
        pass
    else:
        assert False, '[G02_02_04] Failed to generate second image'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSave')
    with step('[Action] close_saved_IAP'):
        actions.is_element_present(AppiumBy.NAME, 'Unlock premium features')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        actions.is_element_present(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] close_rate_us_photo'):
        actions.is_element_present(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your Photo Looks Perfect!')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Btn Save N')
    with step('[Action] close_saved_IAP'):
        actions.is_element_present(AppiumBy.NAME, 'Unlock premium features')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        actions.is_element_present(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] close_rate_us_photo'):
        actions.is_element_present(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your Photo Looks Perfect!')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'saveBtn')
    with step('[Action] close_saved_IAP'):
        actions.is_element_present(AppiumBy.NAME, 'Unlock premium features')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        actions.is_element_present(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] close_rate_us_photo'):
        actions.is_element_present(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Later')
        actions.find_element(AppiumBy.NAME, 'Your Photo Looks Perfect!')
        actions.wait_for_invisible(AppiumBy.NAME, 'Your Photo Looks Perfect!')
    with step('[Action] tap_share_to_FB_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Post')
    assert actions.tap_by_coordinates(42, 41)
    with step('[Action] tap_share_to_IG_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Instagram')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram')
    with step('[Action] back_to_phd_from_sns'):
        actions.activate_app('com.cyberlink.photodirector')
    assert actions.tap_by_coordinates(63, 277)
    if actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="shareCell" and @label="AirDrop"]'):
        pass
    else:
        assert False, '[G02_02_04] Failed to verify share more'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Mine'):
        pass
    else:
        assert False, '[G02_02_04] Failed to verify home'
    with step('[Verify] snapshot: G02_02_02_after_backing_to_home.png'):
        actions.capture_for_gt('G02_02_02_after_backing_to_home.png')
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step('[Action] close_interstitial'):
        actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
        actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Style Transfer')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    if actions.is_element_present(AppiumBy.NAME, 'The face in the chosen photo is either too small or blurry. This may result in a poor face swap or unexpected defects in the photo. We recommended using a larger photo where the face is clearer.'):
        pass
    else:
        assert False, '[G02_02_04] Failed to verify small face dialog'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway')
    actions.capture_for_gt('G02_02_04_my_face.png')
    if actions.compare_with_gt('G02_02_04_my_face.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, '[G02_02_04] Compare fail for my_face'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'CMS-Style_076_076')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate More')
    with step('[Action] wait_process'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'barImageView', timeout=5):
            actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'barImageView')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnSave'):
        pass
    else:
        assert False, '[G02_02_04] Failed to generate image from edit room'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ic edit')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Edit'):
        pass
    else:
        assert False, '[G02_02_04] Failed to bring result to edit room'
    with step("[Verify] test_00158 completion"):
        assert True
