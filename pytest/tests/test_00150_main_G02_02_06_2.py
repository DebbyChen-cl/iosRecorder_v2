import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00150_main_G02_02_06_2')
def test_00150_main_G02_02_06_2(actions: DriverActions):
    """artistic avatar - AI anime / sketch / cartoon"""
    uuid = ['de105cd8-4c13-4320-864a-4a22009ba184', '8646deb2-c785-48cb-a28d-50f52d5be68c', '313256fa-5bbd-431f-9985-629f233acd1a', 'c4eddfa6-5499-46a4-aea4-ec201f004a93', '16d0c83d-7b60-4dc3-8f3c-ac216d82bd48', 'fe900e36-aed7-47e6-8c07-d87f4109eb6b', '1115aac7-a2e4-4c4b-acad-a61c616313ef', '246dfc49-bb05-41a5-b33f-91583d3738a0', '21e7a7e9-7197-4589-a881-2f51cffd4f13', '2a06c9a0-b939-4a5f-9612-439a9b814e5d', 'a22fc0a3-ddb9-4503-8208-77ca55a543a4', 'a392309d-3ad9-4983-946f-69f818e50840', 'c0676895-e8cc-424d-a70d-f2e8ee807258', 'd7928f92-7b98-43b7-b6b4-15345a21acea', 'f991bb9e-8395-414f-bf28-b4f452f8335d']
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Art')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'importLabel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Realistic Art')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Sweet')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] wait_process'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'In progress')
        assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'In progress')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnSave'):
        pass
    else:
        assert False, 'Realistic art free style verification failed (uuid[0][2])'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.ArtisticAvatarResultViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeButton[1]')
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Ok')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Love')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    assert actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1), \
        'Realistic art paid style IAP verification failed (uuid[1])'
    with step('[Action] close_IAP'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Artistic Art')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Oil Painting')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] wait_process'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'In progress')
        assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'In progress')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnSave'):
        pass
    else:
        assert False, 'Artistic art free style verification failed (uuid[3][5])'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.ArtisticAvatarResultViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeButton[1]')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Intricate')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    assert actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1), \
        'Artistic art paid style IAP verification failed (uuid[4])'
    with step('[Action] close_IAP'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Character')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Swimsuit')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] wait_process'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'In progress')
        assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'In progress')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnSave'):
        pass
    else:
        assert False, 'Character free style verification failed (uuid[6][8])'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.ArtisticAvatarResultViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeButton[1]')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Maid')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    assert actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1), \
        'Character paid style IAP verification failed (uuid[7])'
    with step('[Action] close_IAP'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
        assert actions.wait_for_invisible(AppiumBy.NAME, 'Unlock premium features')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Male')
    with step('[Action] scroll_and_tap_feature_tab'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Fantasy 3D')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cowboy')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('[Action] wait_process'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'In progress')
        assert actions.wait_for_invisible(AppiumBy.ACCESSIBILITY_ID, 'In progress')
    with step('[Action] verify_phd_str'):
        assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnSave')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.ArtisticAvatarResultViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeButton[1]')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Prince')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    assert actions.is_element_present(AppiumBy.NAME, 'Start 7-Day Free Trial', timeout=1), \
        'Fantasy 3D paid style IAP verification failed (uuid[13])'
    with step("[Verify] test_00150 completion"):
        assert True
