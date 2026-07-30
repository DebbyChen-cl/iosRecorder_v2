import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("test_ai_replace_text_prompt_mode")
def test_ai_replace_text_prompt_mode(actions: DriverActions):
    with step("[Action] Launch PhotoDirector"):
        actions.launch_app('com.cyberlink.photodirector')
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'Would you like to continue editing?', timeout=3):
        with step("[Action] Discard an unfinished edit from an earlier interrupted run"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel', 50.0, 50.0)
    with step("[Action] Tap btnSettings at (48.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 48.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=320, container_h=623)
    with step("[Action] Tap About"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 50.0, 50.0)
    with step("[Action] Five tap developerButton at (50.0%, 48.6%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 50.0, 48.6)
    with step("[Action] Open Debug Subscription Plan"):
        actions.tap_within_element(
            AppiumBy.XPATH,
            "(//XCUIElementTypeStaticText[@name='Debug Subscription Plan']/following::XCUIElementTypeButton)[1]",
            50.0,
            50.0,
        )
    with step("[Action] Tap Pro+ at (50.0%, 48.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 50.0, 48.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=270, container_h=222)
    with step("[Action] Tap chevron.left at (50.0%, 48.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 50.0, 48.4, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=320, container_h=693)
    with step("[Action] Tap btnBack at (47.6%, 48.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 47.6, 48.6)
    with step("[Action] Tap btnBack at (47.6%, 48.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 47.6, 48.6)
    with step("[Action] Tap btnStudio at (49.1%, 48.8%)"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnStudio')
    with step("[Verify] AI Photos entry list displays"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView')
    with step("[Action] Scroll until CMS-PhDM_AIMagic_AIReplace_20255E"):
        ai_replace_cell = actions.scroll_until(
            AppiumBy.ACCESSIBILITY_ID,
            'entryCollectionView',
            AppiumBy.ACCESSIBILITY_ID,
            'CMS-PhDM_AIMagic_AIReplace_20255E',
            direction='down',
            offset_start=(0.23, 0.865),
            offset_end=(0.23, 0.144),
            velocity=487,
        )
    with step("[Action] Tap AI Replace"):
        actions.tap(ai_replace_cell)
    with step("[Verify] AI Replace photo picker displays"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnCamera')
    intro_copy = (
        'Experience the evolved technology of AI Replace! '
        'Brush and describe to simply recreate any part of your image.'
    )
    if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, intro_copy, timeout=3):
        with step("[Verify] Intro page displays"):
            assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, intro_copy)
        with step("[Action] Tap Don't show again on Intro"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'checkbox_uncheck', 50.0, 50.0)
        with step("[Action] Tap Try now"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try now', 50.0, 50.0)
        with step("[Verify] Recommendation dialog displays"):
            assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Recommendation')
        with step("[Action] Tap Don't show again on Recommendation"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhotoPickerRecommendDialog-notShowAgainCheckBox', 50.0, 50.0)
        with step("[Action] Tap Continue"):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 50.0, 50.0)
    with step("[Action] Tap ic info n at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic info n', 50.0, 50.0)
    with step("[Verify] Recommendation is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Recommendation')
    with step("[Action] Tap Continue at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=320, container_h=557)
    with step("[Action] Expand album list"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 50.0, 50.0)
    with step("[Action] Tap Sample Photos at (34.1%, 47.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 34.1, 47.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=294, container_h=557)
    with step("[Action] Tap PhDM_example_10 at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_10', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=320, container_h=557)
    with step("[Action] Tap btt_brush_n at (50.0%, 76.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btt_brush_n', 50.0, 76.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushEraserView"]/XCUIElementTypeCollectionView', container_w=320, container_h=53)
    with step("[Action] Paint on instanceSegmentationGestureReceiverView (8 points)"):
        actions.paint_in_element(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', [(73.4, 35.6, 0), (78.1, 33.9, 120), (84.4, 34.4, 240), (88.1, 38.0, 360), (85.9, 42.1, 480), (79.7, 44.0, 600), (74.4, 41.1, 720), (73.4, 35.6, 840)], duration_ms=840)
    with step("[Verify] Capture 'ai_replace_brush_mask' for GT comparison"):
        assert actions.capture_for_gt('ai_replace_brush_mask', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap undoButton at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 50.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=320, container_h=442)
    with step("[Verify] Capture 'ai_replace_no_mask' for GT comparison"):
        assert actions.capture_for_gt('ai_replace_no_mask', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap redoButton at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'redoButton', 50.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=320, container_h=442)
    with step("[Verify] The mask reappears after Redo"):
        assert actions.capture_for_gt('ai_replace_brush_mask', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap undoButton at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 50.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=320, container_h=442)
    with step("[Action] Drag cpSlider (25.1%,48.6%) → slider (99.5%,50.0%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 25.1, 48.6, AppiumBy.ACCESSIBILITY_ID, 'slider', 99.5, 50.0, duration=0.7)
    with step("[Action] Paint on instanceSegmentationGestureReceiverView (8 points)"):
        actions.paint_in_element(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', [(73.4, 35.6, 0), (78.1, 33.9, 120), (84.4, 34.4, 240), (88.1, 38.0, 360), (85.9, 42.1, 480), (79.7, 44.0, 600), (74.4, 41.1, 720), (73.4, 35.6, 840)], duration_ms=840)
    with step("[Verify] Capture 'ai_replace_large_brush_mask' for GT comparison"):
        assert actions.capture_for_gt('ai_replace_large_brush_mask', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap undoButton at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 50.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="zoomView"]/XCUIElementTypeScrollView', container_w=320, container_h=442)
    with step("[Action] Tap ic_circle at (50.0%, 76.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_circle', 50.0, 76.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushEraserView"]/XCUIElementTypeCollectionView', container_w=320, container_h=53)
    with step("[Action] Paint on instanceSegmentationGestureReceiverView (8 points)"):
        actions.paint_in_element(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', [(31.2, 7.2, 0), (42.2, 2.4, 150), (54.7, 6.0, 300), (57.8, 16.8, 450), (51.6, 25.2, 600), (37.5, 26.4, 750), (29.7, 18.0, 900), (31.2, 7.2, 1050)], duration_ms=1050)
    with step("[Verify] Capture 'ai_replace_circle_bread_mask' for GT comparison"):
        assert actions.capture_for_gt('ai_replace_circle_bread_mask', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap Undo"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'undoButton', 50.0, 50.0)
    with step("[Action] Tap ic_box at (50.0%, 76.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_box', 50.0, 76.7, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushEraserView"]/XCUIElementTypeCollectionView', container_w=320, container_h=53)
    with step("[Action] Box-mask the coffee"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 68.1, 24.0, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 93.8, 49.0, duration=1.0)
    with step("[Verify] Capture 'ai_replace_box_coffee_mask' for GT comparison"):
        assert actions.capture_for_gt('ai_replace_box_coffee_mask', AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', threshold=0.95)
    with step("[Action] Tap Replace at (50.0%, 47.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Replace', 50.0, 47.1)
    with step("[Action] Tap btnDescribeOption at (50.0%, 69.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnDescribeOption', 50.0, 69.4)
    with step("[Action] Tap lblPlaceHolder at (29.6%, 47.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 29.6, 47.4, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textView', container_w=294, container_h=53)
    with step("[Action] Type 'aaa' into lblPlaceHolder"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 'aaa')
    with step("[Verify] promptTextField text equals 'aaa'"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'promptTextField', 'aaa') is not False
    with step("[Action] Tap btnClear at (93.8%, 93.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClear', 93.8, 93.8, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='textView', container_w=294, container_h=53)
    with step("[Verify] lblPlaceHolder is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder')
    with step("[Action] Type 'bubble tea' into prompt"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 'bubble tea')
    with step("[Action] Tap Next: at (37.5%, 51.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 37.5, 51.2)
    with step("[Verify] AIReplaceResultCell-0 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AIReplaceResultCell-0')
    with step("[Verify] AIReplaceResultCell-1 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AIReplaceResultCell-1')
    with step("[Action] Tap Generate More at (50.0%, 47.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate More', 50.0, 47.1)
    with step("[Verify] AIReplaceResultCell-2 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AIReplaceResultCell-2')
    with step("[Verify] AIReplaceResultCell-3 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AIReplaceResultCell-3')
    with step("[Verify] Capture result preview before selection"):
        assert actions.capture_for_preview('ai_replace_result_selection', 'before', AppiumBy.ACCESSIBILITY_ID, 'mainImageView')
    with step("[Action] Tap AIReplaceResultCell-1 at (52.5%, 49.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AIReplaceResultCell-1', 52.5, 49.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushEraserView"]/XCUIElementTypeCollectionView', container_w=320, container_h=53)
    with step("[Verify] Selected result changes the preview"):
        assert actions.capture_for_preview('ai_replace_result_selection', 'after', AppiumBy.ACCESSIBILITY_ID, 'mainImageView', expected_result='different', threshold=0.99)
    with step("[Action/Verify] Long press Compare shows the original photo"):
        assert actions.capture_for_preview('ai_replace_compare', 'before', AppiumBy.ACCESSIBILITY_ID, 'mainImageView')
        assert actions.long_press_capture_for_preview_within_element(
            AppiumBy.ACCESSIBILITY_ID,
            'btnCompare',
            50.0,
            50.0,
            duration=1.0,
            capture_name='ai_replace_compare',
            capture_by=AppiumBy.ACCESSIBILITY_ID,
            capture_value='mainImageView',
            expected_result='different',
            threshold=0.99,
        )
    with step("[Action] Tap topView_editButton at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'topView_editButton', 50.0, 50.0)
    with step("[Action] Reveal AI Replace in the Edit feature list"):
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', 'left', velocity=480.0, from_pct_x=87.5, from_pct_y=50.0, distance_pts=240.0)
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', 'right', velocity=300.0, from_pct_x=18.8, from_pct_y=50.0, distance_pts=120.0)
    with step("[Action] Tap ic_ai_replace at (50.0%, 48.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_ai_replace', 50.0, 48.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=320, container_h=72)
    with step("[Verify] Replace is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Replace')
    with step("[Action] Tap Box at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Box', 50.0, 50.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushEraserView"]/XCUIElementTypeCollectionView', container_w=320, container_h=53)
    with step("[Action] Drag instanceSegmentationGestureReceiverView (17.5%,51.7%) → instanceSegmentationGestureReceiverView (75.9%,83.4%)"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 17.5, 51.7, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 75.9, 83.4, duration=1.0)
    with step("[Action] Tap Replace at (5.6%, 47.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Replace', 5.6, 47.1)
    with step("[Action] Tap Describe with Text at (73.9%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Describe with Text', 73.9, 50.0)
    with step("[Action] Type 'steak' into prompt"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 'steak')
    with step("[Action] Tap Next: at (37.5%, 51.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 37.5, 51.2)
    with step("[Action] Wait for steak generation to finish"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AIReplaceResultCell-0')
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AIReplaceResultCell-1')
    with step("[Action] Tap topView_saveButton at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'topView_saveButton', 50.0, 50.0)
        if not actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', timeout=5):
            actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'topView_saveButton', 50.0, 50.0)
    with step("[Verify] Save & Share is visible"):
        assert actions.verify_visible(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@label="Save & Share"]')
    with step("[Action] Tap navBackButton at (45.5%, 45.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 45.5, 45.5)
    with step("[Action] Tap Replace More at (50.0%, 53.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Replace More', 50.0, 53.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="brushEraserView"]/XCUIElementTypeCollectionView', container_w=320, container_h=53)
    with step("[Verify] Box is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Box')
    with step("[Action] Box-mask the coffee"):
        actions.drag_within_elements(AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 63.4, 19.7, AppiumBy.ACCESSIBILITY_ID, 'instanceSegmentationGestureReceiverView', 93.8, 49.0, duration=1.0)
    with step("[Action] Tap Replace at (50.0%, 47.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Replace', 50.0, 47.1)
    with step("[Action] Tap Describe with Text at (73.9%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Describe with Text', 73.9, 50.0)
    with step("[Action] Type 'coke cola' into prompt"):
        actions.type_text_by_locator(AppiumBy.ACCESSIBILITY_ID, 'lblPlaceHolder', 'coke cola')
    with step("[Action] Tap Next: at (37.5%, 51.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Next:', 37.5, 51.2)
    with step("[Verify] AIReplaceResultCell-0 is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'AIReplaceResultCell-0')
    with step("[Action] Tap topView_homeButton at (50.0%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'topView_homeButton', 50.0, 50.0)
    with step("[Verify] Home is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Home')
    with step("[Action] Tap btnStudio at (63.2%, 41.5%)"):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnStudio')
    with step("[Action] Tap CMS-PhDM_AIMagic_AIReplace_20255E at (47.9%, 41.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'CMS-PhDM_AIMagic_AIReplace_20255E', 47.9, 41.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=296, container_h=541)
    with step("[Verify] btnCamera is visible"):
        assert actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'btnCamera')
    with step("[Verify] Intro page does not display again"):
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, intro_copy, timeout=3)
        assert actions.verify_not_visible(AppiumBy.ACCESSIBILITY_ID, 'Try now', timeout=3)
    with step("[Verify] Screenshot comparisons"):
        assert actions.run_screenshot_comparisons(threshold=0.95) is not False
    assert True
