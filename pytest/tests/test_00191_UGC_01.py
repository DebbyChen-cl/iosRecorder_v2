import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
from tests.SFT_renew import testdata as TD


@pytest.mark.name('00191_UGC_01')
def test_00191_UGC_01(actions: DriverActions):
    """UGC - create and share"""
    with step('Pre-step: sync UGC template contents with ETag cache'):
        ugc_cache_result = TD.fetch_ugc_template_contents_with_etag_cache(cache_file_path='SFT/material/ugc_cache/ugc_template_contents_en_US_2.0_1_201.json', etag_file_path='SFT/material/ugc_cache/ugc_template_contents_en_US_2.0_1_201.etag', lang='en_US', content_ver='2.0', sindex=1, eindex=201, timeout=20)
        if not ugc_cache_result.get('ok'):
            assert False, 'Failed to fetch and cache UGC template contents'
    with step('Precondition: Read and store test case guid'):
        case = {'ai_creative_studio': '', 'motion_swap': '', 'ai_try_on': ''}
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
            deeplink = str(item.get('Deeplink') or item.get('deeplink') or '').lower()
            tags = item.get('tags') if isinstance(item.get('tags'), list) else []
            tag_guids = {str(tag.get('guid') or '').strip().lower() for tag in tags if isinstance(tag, dict)}
            if not case['ai_creative_studio'] and 'ai_creative_studio' in tag_guids:
                case['ai_creative_studio'] = template_guid
            if not case['motion_swap'] and 'character_motion_swap' in tag_guids:
                case['motion_swap'] = template_guid
            if not case['ai_try_on'] and ('ai_try_on' in tag_guids or 'ai_try_on' in deeplink):
                case['ai_try_on'] = template_guid
            if all(case.values()):
                break
        ugc_template_case_guid = case
    with step('Trigger UGC deeplink via Appium'):
        style_guid = ugc_template_case_guid.get('ai_creative_studio')
        if not style_guid:
            assert False, 'Missing ai_creative_studio style_guid from UGC template cache'
        deeplink = f'clphd://navigate/page?name=ugc&style_guid={style_guid}'
        try:
            actions.execute_script('mobile: deepLink', {'url': deeplink, 'bundleId': 'com.cyberlink.photodirector'})
        except Exception:
            actions.open_url(deeplink)
    with step('Verify demo image is displayed'):
        with step('[Action] verify_demo_image'):
            assert actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage', timeout=5), 'Demo image is not displayed in AI Creative Studio showcase'
    with step('Verify prompt is displayed'):
        with step('[Action] verify_prompt'):
            assert actions.get_text(AppiumBy.XPATH, '//XCUIElementTypeTextView[@value]').strip() != '', 'Prompt text is not displayed in AI Creative Studio showcase'
    with step('Tap "v" to show full prompt'):
        with step('[Action] tap_expand_prompt'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptsCollapseIndicatorImageView')
    with step('Tap "^" to collapse prompt'):
        with step('[Action] tap_collapse_prompt'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'promptsCollapseIndicatorImageView')
    with step('Verify prompt area is collapsed'):
        with step('[Action] verify_prompt_collapsed'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'promptsCollapseIndicatorImageView', timeout=5), 'Prompt area is not collapsed after tapping "^"'
    with step('Tap "Use This Template"'):
        with step('[Action] tap_use_this_template'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use This Template')
    with step('Tap "Try Now" on intro page (optional)'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTitle', timeout=5):
            with step('[Action] tap_try_now'):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Verify entered AI Creative Studio feature'):
        with step('[Action] verify_entered_ai_creative_studio'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Custom', timeout=8), 'Did not enter AI Creative Studio feature after "Use This Template"'
    with step('Verify prompt is auto-filled in custom mode'):
        with step('[Action] verify_prompt_auto_filled'):
            assert actions.get_text(AppiumBy.ACCESSIBILITY_ID, 'textView').strip() != '', 'Prompt is not auto-filled in AI Creative Studio custom mode'
    with step('Tap back to return from AI Creative Studio'):
        with step('[Action] tap_back_from_template'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'aiCreativeStudioRouter_backButton')
    with step('Verify return to Discover'):
        with step('[Action] tap_phd_btn'):
            actions.try_tap(AppiumBy.ACCESSIBILITY_ID, 'navBackButton')
        with step('[Action] verify_ugc_page'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Discover', timeout=5), 'Failed to return to Discover page after exiting AI Creative Studio'
    with step('Trigger Character Motion Swap showcase via deeplink'):
        style_guid = ugc_template_case_guid.get('motion_swap')
        if not style_guid:
            assert False, 'Missing motion_swap style_guid from UGC template cache'
        deeplink = f'clphd://navigate/page?name=ugc&style_guid={style_guid}'
        try:
            actions.execute_script('mobile: deepLink', {'url': deeplink, 'bundleId': 'com.cyberlink.photodirector'})
        except Exception:
            actions.open_url(deeplink)
    with step('Verify demo video is displayed'):
        with step('[Action] verify_demo_video'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'videoPlayerView', timeout=5), 'Demo video is not displayed in Motion Swap showcase'
    with step('Verify duration info is displayed'):
        with step('[Action] verify_duration_info'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'lblTime', timeout=5), 'Duration info is not displayed in Motion Swap showcase'
    with step('Tap preview to pause video'):
        with step('[Action] tap_video_preview'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'videoPlayerView')
    with step('Verify video play is paused'):
        with step('[Action] verify_video_paused'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'playIconImageView', timeout=5), 'Video is not paused after tapping preview'
    with step('Tap preview again to resume video'):
        with step('[Action] tap_video_preview'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'videoPlayerView')
    with step('Verify video play is resumed'):
        with step('[Action] verify_video_playing'):
            assert (not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'playIconImageView', timeout=5))
    with step('Tap "Use This Template" for Motion Swap'):
        with step('[Action] tap_use_this_template'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use This Template')
    with step('Tap "Try Now" on intro page (optional)'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'AIFeatureDemoViewController', timeout=5):
            with step('[Action] tap_try_now'):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Verify entered Character Motion Swap feature'):
        with step('[Action] verify_entered_motion_swap'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnImportReference', timeout=8), 'Did not enter Character Motion Swap feature after "Use This Template"'
    with step('Verify the reference video is imported'):
        with step('[Action] verify_motion_swap_reference_video_imported'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnMuteToggle', timeout=5), 'Reference video is not imported in Character Motion Swap'
    with step('Tap back to return from Motion Swap'):
        with step('[Action] tap_home'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnHome')
        with step('[Action] tap_ugc_tab'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Discover')
        with step('[Action] verify_ugc_page'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Discover', timeout=5), 'Failed to return to Discover page after exiting Motion Swap'
    with step('Trigger AI Try-On showcase via deeplink'):
        style_guid = ugc_template_case_guid.get('ai_try_on')
        if not style_guid:
            assert False, 'Missing ai_try_on style_guid from UGC template cache'
        deeplink = f'clphd://navigate/page?name=ugc&style_guid={style_guid}'
        try:
            actions.execute_script('mobile: deepLink', {'url': deeplink, 'bundleId': 'com.cyberlink.photodirector'})
        except Exception:
            actions.open_url(deeplink)
    with step('Verify demo image is displayed'):
        with step('[Action] verify_tryon_demo_image'):
            assert actions.is_element_present(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="photodirector.DiscoverDetailTryOnRefImageViewController"]/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeImage[2]', timeout=5), 'Demo image is not displayed in AI Try-On showcase'
    with step('Verify outfit thumbnail is displayed'):
        with step('[Action] verify_outfit_thumbnail'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'DiscoverDetailTryOnRefImageCell-0', timeout=5), 'Outfit thumbnail is not displayed in AI Try-On showcase'
    with step('Tap "Use This Template" for AI Try-On'):
        with step('[Action] tap_use_this_template'):
            assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Use This Template')
    with step('Tap "Try Now" on intro page (optional)'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'notShowAgainCheckBox'):
            with step('[Action] tap_try_now'):
                actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnNext')
    with step('Verify entered AI Try-On feature'):
        with step('[Action] verify_entered_ai_tryon'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navDescriptionLabel', timeout=8), 'Did not enter AI Try-On feature after "Use This Template"'
    with step('Verify the outfit is imported'):
        with step('[Action] verify_tryon_outfit_imported'):
            assert actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Photo', timeout=8), 'Outfit is not imported in AI Try-On Custom style'
    with step("[Verify] test_00191 completion"):
        assert True
