import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_main_G02_02_06")
def test_test_main_G02_02_06(actions: DriverActions):
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap AI Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step("[Verify] lblTitle is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'), 'element lblTitle should be visible'
    with step("[Action] Tap notShowAgainCheckBox"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Action] Tap Clean"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Clean')
    with step("[Action] Tap Male"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Male')
    with step("[Action] Tap Figure"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Figure')
    with step("[Action] Tap importLabel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importLabel')
    with step("[Verify] descriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'), 'element descriptionLabel should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap importLabel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importLabel')
    with step("[Verify] descriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'), 'element descriptionLabel should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-6"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-6')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Action] Tap I Agree"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'I Agree')
    with step("[Verify] waitIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'waitIndicator'), 'element waitIndicator should be visible'
    with step("[Verify] waitIndicator is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'waitIndicator'), 'element waitIndicator should be visible'
    with step("[Verify] waitIndicator is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'waitIndicator'), 'element waitIndicator should not be visible'
    with step("[Verify] btnSave is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnSave'), 'element btnSave should be visible'
    with step("[Action] Tap btnSave"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSave')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Ok"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ok')
    with step("[Verify] Male is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Male'), 'element Male should be visible'
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap ArtisticAvatarResultCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-0')
    with step("[Action] Tap btnContinueEdit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnContinueEdit')
    with step("[Action] Tap photoPickerButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step("[Action] Tap ScrollableMenuViewCell-Portrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step("[Action] Tap AI Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step("[Action] Tap Clean"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Clean')
    with step("[Action] Tap importLabel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importLabel')
    with step("[Verify] descriptionLabel is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'descriptionLabel'), 'element descriptionLabel should be visible'
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Verify] btnSave is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnSave'), 'element btnSave should be visible'
    with step("[Action] Tap Generate More"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate More')
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap btnSave"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSave')
    with step("[Action] Tap btnBack"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap ArtisticAvatarResultCell-0"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ArtisticAvatarResultCell-0')
    with step("[Action] Tap btnContinueEdit"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnContinueEdit')
    with step("[Action] Tap photoPickerButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoPickerButton')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Action] Tap Discard"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discard')
    with step("[Action] Tap ScrollableMenuViewCell-Portrait"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'ScrollableMenuViewCell-Portrait')
    with step("[Action] Tap AI Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] btnNext is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btnNext'), 'element btnNext should not be visible'
    with step("[Verify] //*[@name=\"btnNext\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btnNext"]'), 'element //*[@name="btnNext"] should not be visible'
    with step("[Verify] //*[@label=\"btnNext\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="btnNext"]'), 'element //*[@label="btnNext"] should not be visible'
    with step("[Verify] //*[@value=\"btnNext\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="btnNext"]'), 'element //*[@value="btnNext"] should not be visible'
    with step("[Action] Tap Clean"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Clean')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Verify] Would you like to continue editing? is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Would you like to continue editing?'), 'element Would you like to continue editing? should be visible'
    with step("[Action] Tap Cancel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step("[Verify] Would you like to continue editing? is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'Would you like to continue editing?'), 'element Would you like to continue editing? should not be visible'
    with step("[Action] Tap AI Photos"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step("[Action] Tap AI Art"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    with step("[Action] Tap btnNext"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step("[Verify] btnNext is not visible"):
        assert actions.verify_not_visible(AppiumBy.NAME, 'btnNext'), 'element btnNext should not be visible'
    with step("[Verify] //*[@name=\"btnNext\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="btnNext"]'), 'element //*[@name="btnNext"] should not be visible'
    with step("[Verify] //*[@label=\"btnNext\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="btnNext"]'), 'element //*[@label="btnNext"] should not be visible'
    with step("[Verify] //*[@value=\"btnNext\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="btnNext"]'), 'element //*[@value="btnNext"] should not be visible'
    with step("[Action] Tap importLabel"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importLabel')
    with step("[Action] Tap Continue"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step("[Action] Tap btnAlbum"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step("[Action] Tap _AT"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step("[Action] Tap photoCell-1"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-1')
    with step("[Action] Tap Avatar"):
        actions.tap_by_locator(AppiumBy.NAME, 'Avatar')
    with step("[Verify] Avatar is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Avatar'), 'element Avatar should not be visible'
    with step("[Verify] //*[@name=\"Avatar\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@name="Avatar"]'), 'element //*[@name="Avatar"] should not be visible'
    with step("[Verify] //*[@label=\"Avatar\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@label="Avatar"]'), 'element //*[@label="Avatar"] should not be visible'
    with step("[Verify] //*[@value=\"Avatar\"] is not visible"):
        assert actions.verify_not_visible(AppiumBy.XPATH, '//*[@value="Avatar"]'), 'element //*[@value="Avatar"] should not be visible'
    with step("[Action] Tap Clean"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Clean')
    with step("[Action] Tap Generate"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step("[Verify] In progress is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should be visible'
    with step("[Verify] In progress is not visible"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'In progress'), 'element In progress should not be visible'
    with step("[Action] Tap homeButton"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'homeButton')
    with step("[Action] Tap btnHome"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
    with step("[Verify] Mine is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Mine'), 'element Mine should be visible'
    assert True
