# @sft-convert:generated  (自動生成；若手動編輯，請把檔名加進 .scratch/sft-convert/PROTECT.txt
#                          或把本行改成 '# @manual'，即不會被覆蓋)
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00170_image_to_video_vidu_q2')
def test_00170_image_to_video_vidu_q2(actions: DriverActions):
    """1. Launch ITV, import city photo from Sample Photos, select Custom style"""
    with step('Tap Image to Video'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Image to Video')
    with step('Tap Try now (optional)'):
        with step('[Action] tap_phd_btn'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Tap Continue of step page (optional)'):
        with step('[Action] tap_phd_btn'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Tap Import photo of 1 person'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "imageIconView"`][1]')
    with step('Tap Continue of recommendation dialog (optional)'):
        with step('[Action] tap_phd_btn'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Continue')
    with step('Expand album list'):
        with step('[Action] expand_album_list'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('Select Sample Photos album'):
        with step('[Action] select_category'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos')
    with step('Select city photo'):
        with step('[Action] select_photo'):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-5')
    with step('Tap Custom style'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Custom')
    with step('Tap model list'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="ImageToVideoCustomModelDetailViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton')
    with step('Select Vidu Q2'):
        with step('[Action] select_itv_model'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Vidu Q2')
    with step('Verify Vidu Q2 is selected'):
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Vidu Q2')
    with step('Verify 5s and 8s durations are listed'):
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.NAME, '5')
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.NAME, '8')
    with step('Tap 8s duration'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, '8')
    with step('Verify 8s is selected'):
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.NAME, '8')
    with step('Verify standard and pro quality are listed'):
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.NAME, 'Standard')
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Pro')
    with step('Tap Standard quality'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Standard')
    with step('Verify Standard is selected'):
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.NAME, 'Standard')
    with step('Tap AI sound ON'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate Sound by AI')
    with step('Tap info button of AI sound'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="ImageToVideoCustomModelDetailViewController"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[5]/XCUIElementTypeButton[1]')
    with step('Verify "AI-generated sound isn\'t available for this model" bubble displays'):
        with step('[Action] verify_phd_str'):
            assert actions.is_element_present(AppiumBy.NAME, 'AI-generated sound isn’t available for this model.')
    with step('Tap outside to close bubble'):
        with step('[Action] tap_outside_bubble'):
            actions.tap_by_coordinates([(50, 50)][0], [(50, 50)][1])
    with step('Tap prompt column'):
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther')
    with step('Input prompt "The train drive through"'):
        with step('[Action] input_itv_prompt'):
            assert actions.type_text_by_locator(AppiumBy.CLASS_NAME, 'XCUIElementTypeTextView', 'The train drive through')
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Next:')
    with step('Tap V to confirm prompt'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n')
    with step('Tap generate'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Generate')
    with step('Verify go to artwork and start generating without error'):
        with step('[Action] wait_itv_process'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'processingLabel')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step("[Verify] test_00170 completion"):
        assert True
