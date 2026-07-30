import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00193_UGC_03')
def test_00193_UGC_03(actions: DriverActions):
    """UGC - KOL"""
    with step('Pre-step: sync UGC template contents with ETag cache'):
        ugc_cache_result = TD.fetch_ugc_template_contents_with_etag_cache(cache_file_path='SFT/material/ugc_cache/ugc_template_contents_en_US_2.0_1_201.json', etag_file_path='SFT/material/ugc_cache/ugc_template_contents_en_US_2.0_1_201.etag', lang='en_US', content_ver='2.0', sindex=1, eindex=201)
        if not ugc_cache_result.get('ok'):
            assert False, 'Failed to fetch and cache UGC template contents'
    with step('Pre-step: find KOL template guid from cache (tag name: kol_tag)'):
        kol_guid = ''
        ugc_template_content = ugc_cache_result.get('content')
        if isinstance(ugc_template_content, dict):
            content_list = ugc_template_content.get('contentList') or []
        else:
            if isinstance(ugc_template_content, list):
                content_list = ugc_template_content
            else:
                content_list = []
        for item in content_list:
            if not isinstance(item, dict):
                continue
            template_guid = str(item.get('guid') or '').strip()
            if not template_guid:
                continue
            tags = item.get('tags') if isinstance(item.get('tags'), list) else []
            tag_names = {str(tag.get('name') or '').strip().lower() for tag in tags if isinstance(tag, dict)}
            if 'kol_tag' in tag_names:
                kol_guid = template_guid
                break
        if not kol_guid:
            assert False, 'No KOL template found with tag name "kol_tag" in UGC template cache'
    with step('Step 2: Tap Discover tab'):
        with step('[Action] tap_ugc_tab'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discover')
        with step('[Action] verify_ugc_page'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Discover', timeout=5), 'Discover page is not displayed'
    with step('Navigate to KOL template via deeplink'):
        deeplink = f'clphd://navigate/page?name=ugc&style_guid={kol_guid}'
        try:
            actions.execute_script('mobile: deepLink', {'url': deeplink, 'bundleId': 'com.cyberlink.photodirector'})
        except Exception:
            actions.open_url(deeplink)
    with step('Step 3: Verify KOL template is listed (blue tick sign visible)'):
        with step('[Action] verify_kol_badge'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'verifiedBadgeImageView', timeout=5), 'KOL blue tick badge is not visible on the template'
    with step('Step 5: Verify blue tick sign on KOL detail page'):
        with step('[Action] verify_kol_badge'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'verifiedBadgeImageView', timeout=5), 'KOL blue tick badge is not visible on the detail page'
    with step('Step 6: Verify KOL hyperlink is displayed'):
        with step('[Action] verify_kol_hyperlink'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'socialLinkImageView', timeout=5), 'KOL hyperlink is not visible on the detail page'
    with step('Step 7: Tap KOL hyperlink'):
        with step('[Action] tap_kol_hyperlink'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'socialLinkImageView')
    with step('Step 8: Verify KOL Instagram page is opened'):
        with step('[Action] verify_ig_page'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Instagram', timeout=8), 'KOL Instagram page did not open after tapping hyperlink'
    with step('Cleanup: return to PHD'):
        with step('[Action] activate_app'):
            actions.activate_app('com.cyberlink.photodirector')
    with step("[Verify] test_00193 completion"):
        assert True
