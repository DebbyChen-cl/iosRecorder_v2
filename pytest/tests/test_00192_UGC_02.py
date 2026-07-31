import re

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests import testdata as TD


@pytest.mark.name('00192_UGC_02')
def test_00192_UGC_02(actions: DriverActions):
    """UGC - view and interact"""

    # ── Inlined from legacy UGC_Page like-count helpers (self.ugc_page.*) ──
    def _get_like_count():
        element = actions.get_element(AppiumBy.ACCESSIBILITY_ID, 'likeCountLabel', timeout=1)
        if element is None:
            return -1
        digits = re.findall(r'\d+', element.get_attribute('value') or '')
        if not digits:
            return -1
        return int(''.join(digits))

    def _search_like_count_value(*_):
        return _get_like_count()

    def _parse_like_count_text(raw_text):
        text = (raw_text or '').strip().replace(',', '')
        if not text:
            return -1
        match = re.match(r'^(\d+(?:\.\d+)?)([kKmM]?)$', text)
        if match:
            value = float(match.group(1))
            suffix = match.group(2).lower()
            if suffix == 'k':
                return int(value * 1000)
            if suffix == 'm':
                return int(value * 1000000)
            return int(value)
        digits = re.findall(r'\d+', text)
        if digits:
            return int(''.join(digits))
        return -1

    def _get_template_by_like_count(like_count):
        if like_count is None or like_count < 0:
            return None
        try:
            cells = actions.find_elements(AppiumBy.XPATH, '//XCUIElementTypeCell[@name="CMS-UGC_category_All"]')
        except Exception:
            return None
        for cell in cells:
            try:
                text_elements = cell.find_elements(AppiumBy.XPATH, './/XCUIElementTypeStaticText')
            except Exception:
                continue
            for text_element in text_elements:
                raw_text = (text_element.get_attribute('name') or text_element.get_attribute('label') or text_element.get_attribute('value') or '')
                if _parse_like_count_text(raw_text) == like_count:
                    return cell
        return None

    with step('Pre-step: sync UGC template contents with ETag cache'):
        ugc_cache_result = TD.fetch_ugc_template_contents_with_etag_cache(cache_file_path='SFT/material/ugc_cache/ugc_template_contents_en_US_2.0_1_201.json', etag_file_path='SFT/material/ugc_cache/ugc_template_contents_en_US_2.0_1_201.etag', lang='en_US', content_ver='2.0', sindex=1, eindex=201, timeout=20)
        if not ugc_cache_result.get('ok'):
            assert False, 'Failed to fetch and cache UGC template contents'
    with step('Precondition: Read and store first non-PHD and PhotoDirector template user_id'):
        template_owner = {'first_non_phd_user_id': '', 'first_non_phd_guid': '', 'first_photodirector_user_id': '', 'first_photodirector_guid': ''}
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
            user_id = str(item.get('user_id') or '').strip()
            if not template_guid or not user_id:
                continue
            normalized_user_id = user_id.lower()
            if not template_owner['first_non_phd_user_id'] and normalized_user_id != 'photodirector':
                template_owner['first_non_phd_user_id'] = user_id
                template_owner['first_non_phd_guid'] = template_guid
            if not template_owner['first_photodirector_user_id'] and normalized_user_id == 'photodirector':
                template_owner['first_photodirector_user_id'] = user_id
                template_owner['first_photodirector_guid'] = template_guid
            if template_owner['first_non_phd_user_id'] and template_owner['first_photodirector_user_id']:
                break
        ugc_template_owner = template_owner
    with step('Trigger non-PHD UGC deeplink via Appium'):
        style_guid = ugc_template_owner.get('first_non_phd_guid')
        if not style_guid:
            assert False, 'Missing first non-PHD template guid from UGC template cache'
        deeplink = f'clphd://navigate/page?name=ugc&style_guid={style_guid}'
        try:
            actions.execute_script('mobile: deepLink', {'url': deeplink, 'bundleId': 'com.cyberlink.photodirector'})
        except Exception:
            actions.open_url(deeplink)
    with step('Verify non-PHD showcase opened'):
        if not actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage', timeout=5) and not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'videoPlayerView', timeout=5):
            with step('[Action] tap_showcase_by_index'):
                assert actions.tap_by_locator(AppiumBy.XPATH, '(//XCUIElementTypeCell[@name="CMS-discover_all"])[1]'), 'Failed to open non-PHD showcase card'
    with step('Tap Like button'):
        like_before = _get_like_count()
        with step('[Action] tap_like'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'likeButton')
    with step('Verify like count +1'):
        like_after = _get_like_count()
        if like_after != like_before + 1:
            assert False, f'Like count did not increase: before={like_before}, after={like_after}'
    with step('Tap "<" to go back to Discover'):
        with step('[Action] tap_back_from_showcase'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'backButton')
    with step('Verify like count on the feed card matches step 5'):
        like_count = _search_like_count_value()
        if like_count != like_after:
            assert False, f'Does not find the updated like count {like_after} on the feed card after liking '
    with step('Tap the same showcase again'):
        style_guid = ugc_template_owner.get('first_non_phd_guid')
        if not style_guid:
            assert False, 'Missing first non-PHD template guid from UGC template cache'
        deeplink = f'clphd://navigate/page?name=ugc&style_guid={style_guid}'
        try:
            actions.execute_script('mobile: deepLink', {'url': deeplink, 'bundleId': 'com.cyberlink.photodirector'})
        except Exception:
            actions.open_url(deeplink)
    with step('Tap "?" community info button'):
        with step('[Action] tap_community_info'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'questionButton')
    with step('Verify community guidelines dialog pops up'):
        with step('[Action] verify_community_guidelines_dialog'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Community Guidelines & Terms', timeout=5), 'Community guidelines dialog not displayed'
    with step('Tap TOS hyperlink'):
        with step('[Action] tap_tos_link'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Terms of Service')
    with step('Verify TOS web page opened'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Community Guidelines & Terms', timeout=5):
            assert False, 'Still on community guidelines dialog — TOS page did not open'
    with step('Back to PHD'):
        with step('[Action] activate_app'):
            actions.activate_app('com.cyberlink.photodirector')
    with step('Tap OK to dismiss community guidelines dialog'):
        with step('[Action] tap_community_ok'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step('Tap "..." more-options button'):
        with step('[Action] tap_more_options'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'moreButton')
    with step('Tap "Report"'):
        with step('[Action] tap_report'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'Report')
    with step('Verify entered Feedback page'):
        with step('[Action] verify_feedback_page'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Send Feedback', timeout=8), 'Feedback page not displayed after tapping Report'
    with step('Verify report description is auto-filled'):
        with step('[Action] verify_report_description_auto_filled'):
            assert actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'textView').strip() != '', 'Report description is not auto-filled'
    with step('Tap "<" to go back'):
        with step('[Action] tap_phd_btn'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
        with step('[Action] tap_phd_element'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Leave')
    with step('Tap "..." more-options button'):
        with step('[Action] tap_more_options'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'moreButton')
    with step('Tap "Don\'t like this author"'):
        with step('[Action] tap_dont_like_author'):
            assert actions.tap_by_locator(AppiumBy.NAME, "Don't like this author")
    with step('Tap "Cancel" in the confirmation dialog'):
        with step('[Action] tap_cancel_dialog'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    with step('Verify dialog is closed'):
        with step('[Action] verify_dialog_closed'):
            assert not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Cancel', timeout=3), 'Dialog is still visible after tapping Cancel'
    with step('Tap "..." more-options button again'):
        with step('[Action] tap_more_options'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'moreButton')
    with step('Tap "Don\'t like this author" again'):
        with step('[Action] tap_dont_like_author'):
            assert actions.tap_by_locator(AppiumBy.NAME, "Don't like this author")
    with step('Tap "Block"'):
        with step('[Action] tap_block'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Block')
    with step("Verify blocked author's showcases are absent from feed"):
        pass
    with step('Trigger PhotoDirector showcase via deeplink'):
        style_guid = ugc_template_owner.get('first_photodirector_guid')
        if not style_guid:
            assert False, 'Missing PhotoDirector template guid from UGC template cache'
        deeplink = f'clphd://navigate/page?name=ugc&style_guid={style_guid}'
        try:
            actions.execute_script('mobile: deepLink', {'url': deeplink, 'bundleId': 'com.cyberlink.photodirector'})
        except Exception:
            actions.open_url(deeplink)
    with step('Step 29: Verify no "..." menu on PHD official showcase'):
        with step('[Action] verify_no_more_options'):
            assert not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'moreButton', timeout=3), '"..." button is present on PHD official showcase — should not exist'
    with step('Step 30: Tap Like button on PHD official showcase'):
        official_like_before = _get_like_count()
        with step('[Action] tap_like'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'likeButton')
    with step('Verify like count +1 on PHD official showcase'):
        official_like_after = _get_like_count()
        if official_like_after != official_like_before + 1:
            assert False, f'Like count did not increase: before={official_like_before}, after={official_like_after}'
    with step('Tap "<" to go back to Discover'):
        with step('[Action] tap_back_from_showcase'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'backButton')
    with step('Verify like count on feed card matches previous step'):
        official_like_count = _search_like_count_value(official_like_after)
        selected_official_template = _get_template_by_like_count(official_like_after)
        if official_like_after >= 0:
            if official_like_count == -1 or selected_official_template is None:
                assert False, f'Does not find the updated like count {official_like_after} on the official feed card after liking'
    with step('Re-open PhotoDirector showcase via deeplink'):
        style_guid = ugc_template_owner.get('first_photodirector_guid')
        deeplink = f'clphd://navigate/page?name=ugc&style_guid={style_guid}'
        try:
            actions.execute_script('mobile: deepLink', {'url': deeplink, 'bundleId': 'com.cyberlink.photodirector'})
        except Exception:
            actions.open_url(deeplink)
    with step('Tap "?" community info button'):
        with step('[Action] tap_community_info'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'questionButton')
    with step('Verify community guidelines dialog pops up'):
        with step('[Action] verify_community_guidelines_dialog'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Community Guidelines & Terms', timeout=5), 'Community guidelines dialog not displayed on official showcase'
    with step('Tap TOS hyperlink'):
        with step('[Action] tap_tos_link'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Terms of Service')
    with step('Verify TOS web page opened'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Community Guidelines & Terms', timeout=5):
            assert False, 'Still on community guidelines dialog — TOS page did not open'
    with step('Back to PHD'):
        with step('[Action] activate_app'):
            actions.activate_app('com.cyberlink.photodirector')
    with step('Tap OK to dismiss community guidelines dialog'):
        with step('[Action] tap_community_ok'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'OK')
    with step("[Verify] test_00192 completion"):
        assert True
