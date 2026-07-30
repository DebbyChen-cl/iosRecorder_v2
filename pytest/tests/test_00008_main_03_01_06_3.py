import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00008_main_03_01_06_3')
def test_00008_main_03_01_06_3(actions: DriverActions):
    """1. Enter setting page"""
    quality_config = {'efficient': {'expected_text': 'Efficient (Long Side = 800 Pixels)', 'premium_uuid': 'e7fc4b74-9361-432d-a394-89eff7946cc6', 'normal_uuid': '3b9c1fad-64eb-459e-9ae7-488af5e9e409'}, 'good': {'expected_text': 'Good (Long Side = 1600 Pixels)', 'premium_uuid': '77ec7682-4848-4964-9761-a6788ad2e1ec', 'normal_uuid': 'b42c960f-569c-49e3-8bfa-58647bd8e1de'}, 'hd': {'expected_text': 'HD (Long Side = 2560 Pixels)', 'premium_uuid': 'b31df12b-666d-44b6-9aed-902a533976e1', 'normal_uuid': 'e8af5aa4-8c16-4f4f-a4be-5840b29f5455'}, 'ultra': {'expected_text': 'Ultra HD (Long Side = 3264 Pixels)', 'premium_uuid': 'a549a6a4-36b9-48bf-a156-b7a966371b85', 'normal_uuid': '764df295-881d-4ab9-b374-8c3cb32b2ae0', 'iap_uuid': '871204cf-4206-4702-9b94-1091cbf49a6c'}, 'max': {'expected_text': 'Maximum (Long Side = 4000 Pixels)', 'premium_uuid': '70381944-8b10-4a94-8d97-84f1c45cd98c', 'normal_uuid': 'e60506c9-00b0-4e83-b86f-f51e17a0586c', 'iap_uuid': '261be726-2522-478a-97ff-939ec2fa6ddc'}}
    premium_only = ['ultra', 'max']
    build_type = 'normal'
    with step('[Action] close_continue_edit'):
        if actions.is_element_present(AppiumBy.NAME, 'Would you like to continue editing?', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'closeButton', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'closeButton')
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'navCloseButton')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnSettings')
    with step('[Action] tap_imagequalitysetting_tab'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Image Quality Setting')
        assert (
            actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Image Quality Setting')
            or actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
        )
    quality_locators = {
        'efficient': (AppiumBy.ACCESSIBILITY_ID, 'Efficient (Long Side = 800 Pixels)'),
        'good': (AppiumBy.ACCESSIBILITY_ID, 'Good (Long Side = 1600 Pixels)'),
        'hd': (AppiumBy.ACCESSIBILITY_ID, 'HD (Long Side = 2560 Pixels)'),
        'ultra': (AppiumBy.ACCESSIBILITY_ID, 'Ultra HD (Long Side = 3264 Pixels)'),
        'max': (AppiumBy.ACCESSIBILITY_ID, 'Maximum (Long Side = 4000 Pixels)'),
    }
    for quality in quality_config:
        config = quality_config[quality]
        quality_by, quality_value = quality_locators[quality]
        if actions.is_element_present(quality_by, quality_value):
            assert actions.tap_by_locator(quality_by, quality_value)
            result = quality_value
        else:
            result = 'No Option'
        if build_type == 'normal' and quality in premium_only:
            if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'creditTipsLabel') or actions.is_element_present(
                AppiumBy.ACCESSIBILITY_ID, 'btnNext'
            ):
                with step('[Action] tap_IAP_back_btn_quality'):
                    actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnClose')
                    assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Image Quality Setting')
                continue
            else:
                assert False
        if result != config['expected_text']:
            assert False
    with step('[Action] tap_back_btn'):
        actions.tap_by_locator(AppiumBy.NAME, 'img tryout back n')
        assert actions.is_element_present(AppiumBy.NAME, 'Setting')
    with step("[Verify] test_00008 completion"):
        assert True
