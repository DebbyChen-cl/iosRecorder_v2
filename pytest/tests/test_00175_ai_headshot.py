# @sft-convert:generated  (自動生成；若手動編輯，請把檔名加進 .scratch/sft-convert/PROTECT.txt
#                          或把本行改成 '# @manual'，即不會被覆蓋)
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00175_ai_headshot')
def test_00175_ai_headshot(actions: DriverActions):
    """AI headshot"""
    uuid = ['2f35cbfd-042b-4fbd-8626-f6d4a5722e94', '2b4f4101-3c5d-40ff-b0b7-9049cc4759c6', '837a33e1-435e-43c3-9ac5-04541861f9ee', '6f3eeb34-b780-4ce1-a372-b24cc7ee5dac', '86041a9e-4451-4286-b5bd-e2784c437d32', '87c13cac-8708-4de9-bdf5-d54a23a74864', 'ff18bc17-f883-4529-9777-591e1eaf1031', 'a57a68fd-a853-4e29-9193-89c8e1ee2ebf', '6f454ed3-594c-43c2-a35e-ee8823176a05', 'a6732b69-936e-4ccf-b27d-108cb0f89d16', '5aa4cdd4-2944-43c7-936b-04fb884a1cb2', 'f3f81d12-c410-4971-a656-113b4a8aecc3', '830ea7da-8e00-490d-803d-a36a5258a7e4', '4815aef5-a656-42c3-b5a3-79b416b5679c', '207a7308-3a6d-4eba-a19b-837455617307', '5cc302da-8ce2-4f89-89d1-0c55c8b0f21b', '72ca4e15-f2ed-4308-bbc4-c4974bb27d5b', '0b08ef1b-f1c6-49b8-8a7d-51334ddbc39c', '565b945f-805a-4de2-84e2-18063e9a1d5b', 'f3d7a7ba-64bc-4171-bf1f-19b4aea20350', 'd6a92ff4-32fa-4963-90ca-a411c95aaba1', 'c27ebcb0-7617-4315-8feb-d1ca82a46e14']
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Photos')
    with step('[Action] scroll_and_tap_vertical'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'AI Headshot')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navArtworkButton'), '[08_03_01] Failed to enter artwork'
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle'):
        pass
    else:
        assert False, '[08_03_01] ai headshot list verification failed'
    assert actions.tap_by_locator(AppiumBy.NAME, 'Create More'), '[08_03_01] Failed to tap create_more'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Male'), '[08_03_01] Failed to tap male'
    if actions.is_element_present(AppiumBy.NAME, 'Office'):
        pass
    else:
        assert False, '[08_03_01] gender verification failed'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Shirt'), '[08_03_01] Failed to tap shirt'
    if actions.is_element_present(AppiumBy.NAME, 'Building'):
        pass
    else:
        assert False, '[08_03_01] category verification failed'
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'Building')
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'continueButton'), '[08_03_01] Failed to tap avatar_continue_1style'
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'recommendationLbl'):
        pass
    else:
        assert False, '[08_03_01] info page verification failed'
    assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue'), '[08_03_01] Failed to tap continue'
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'BG')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    if actions.is_element_present(AppiumBy.NAME, 'Please choose another photo.'):
        pass
    else:
        assert False, '[08_03_01] invalid photo verification failed'
    with step('[Action] tap_phd_btn'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('[Action] expand_album_list'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-2')
    with step('[Action] verify_pack_cash'):
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'iconImageView')
    with step('[Action] tap_phd_element'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'iconImageView')
    with step('[Action] verify_IAP'):
        assert actions.find_element(AppiumBy.NAME, 'Start 7-Day Free Trial')
        assert actions.find_element(AppiumBy.ACCESSIBILITY_ID, 'buyFlowLightButton')
    assert actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'btnClose'), '[08_03_01] Failed to close IAP'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Credits')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeButton')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Server Busy'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    else:
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'processingLabel'):
            pass
        else:
            assert False, '[08_03_01] generate verification failed'
    with step("[Verify] test_00175 completion"):
        assert True
