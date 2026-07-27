import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_face_swap")
def test_test_ai_face_swap(actions: DriverActions):
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] navDescriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel'), 'element navDescriptionLabel should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap Masculine"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Masculine')
    with step("[Verify] Muscular is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Muscular'), 'element Muscular should be visible'
    with step("[Action] Tap at (210, 340)"):
        actions.tap_by_coordinates(210, 340)
    with step("[Verify] titleLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'titleLabel'), 'element titleLabel should be visible'
    with step("[Action] Tap addSourceImageView"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'addSourceImageView')
    with step("[Verify] descriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'), 'element descriptionLabel should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step("[Verify] Import Photos... is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Import Photos...'), 'element Import Photos... should not be visible'
    with step("[Verify] The face in the chosen photo is either too small or blurry. This may result in a poor face swap or unexpected defects in the photo. We recommended using a larger photo where the face is clearer. is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'The face in the chosen photo is either too small or blurry. This may result in a poor face swap or unexpected defects in the photo. We recommended using a larger photo where the face is clearer.'), 'element The face in the chosen photo is either too small or blurry. This may result in a poor face swap or unexpected defects in the photo. We recommended using a larger photo where the face is clearer. should not be visible'
    with step("[Verify] The face in this photo is too small or blurry, which may result in poorly generated results. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'The face in this photo is too small or blurry, which may result in poorly generated results.'), 'element The face in this photo is too small or blurry, which may result in poorly generated results. should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Verify] Import Photos... is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Import Photos...'), 'element Import Photos... should not be visible'
    with step("[Verify] No face detected. A face is required for this feature. is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'No face detected. A face is required for this feature.'), 'element No face detected. A face is required for this feature. should be visible'
    with step("[Action] Tap OK"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-5"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step("[Verify] Import Photos... is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Import Photos...'), 'element Import Photos... should not be visible'
    with step("[Action] Tap Continue Anyway"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway')
    with step("[Verify] cancelButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'cancelButton'), 'element cancelButton should not be visible'
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] barImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'barImageView'), 'element barImageView should be visible'
    with step("[Verify] barImageView is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'barImageView'), 'element barImageView should be visible'
    with step("[Verify] barImageView is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'barImageView'), 'element barImageView should not be visible'
    with step("[Verify] btnSave is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnSave'), 'element btnSave should be visible'
    with step("[Action] Tap btnSave"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSave')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your Photo Looks Perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your Photo Looks Perfect!'), 'element Your Photo Looks Perfect! should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your Photo Looks Perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your Photo Looks Perfect!'), 'element Your Photo Looks Perfect! should not be visible'
    with step("[Action] Tap Collage"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Collage')
    with step("[Action] Tap saveBtn"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'saveBtn')
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] buyFlowLightButton is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton'), 'element buyFlowLightButton should not be visible'
    with step("[Verify] Your Photo Looks Perfect! is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Your Photo Looks Perfect!'), 'element Your Photo Looks Perfect! should not be visible'
    with step("[Action] Tap btnShareFB"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnShareFB')
    with step("[Action] Tap Allow Paste"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
    with step("[Verify] Post is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Post'), 'element Post should be visible'
    with step("[Action] Tap at (42, 41)"):
        actions.tap_by_coordinates(42, 41)
    with step("[Action] Tap Instagram"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Instagram')
    with step("[Action] Tap Allow Paste"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Allow Paste')
    with step("[Verify] Share to Instagram is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Share to Instagram'), 'element Share to Instagram should be visible'
    with step("[Action] Tap More"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'More')
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Verify] shareCell is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'shareCell'), 'element shareCell should be visible'
    with step("[Action] Tap at (63, 277)"):
        actions.tap_by_coordinates(63, 277)
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Action] Tap **/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"):
        actions.tap_by_locator(AppiumBy.XPATH, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    with step("[Action] Tap navHomeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navHomeButton')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Action] Tap Edit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Edit')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step("[Verify] btnIAP is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'btnIAP'), 'element btnIAP should not be visible'
    with step("[Action] Tap btnClose"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
    with step("[Action] Tap ScrollableMenuViewCell-Portrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap AI Face Swap"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Face Swap')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Verify] Crop to Continue is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Crop to Continue'), 'element Crop to Continue should be visible'
    with step("[Action] Tap Crop"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Crop')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnDone"):
        actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    with step("[Action] Tap btn ok n"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn ok n')
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnDone"):
        actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    with step("[Action] Tap btn ok n"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn ok n')
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnDone"):
        actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    with step("[Action] Tap btn ok n"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn ok n')
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnDone"):
        actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    with step("[Action] Tap btn ok n"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn ok n')
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    with step("[Action] Tap btn_ok_n"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step("[Action] Tap btnDone"):
        actions.tap_by_locator(AppiumBy.NAME, 'btnDone')
    with step("[Action] Tap btn ok n"):
        actions.tap_by_locator(AppiumBy.NAME, 'btn ok n')
    with step("[Action] Tap doneButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'doneButton')
    assert False, "original pytest run failed — this recording reproduces a failing run"
