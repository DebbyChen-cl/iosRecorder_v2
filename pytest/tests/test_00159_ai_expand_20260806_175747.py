import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00159_ai_expand_20260806_175747")
def test_00159_ai_expand_20260806_175747(actions: DriverActions):
    with step("[Action] Tap btnSettings at (72.7%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnSettings', 72.7, 50.0)
    with step("[Action] Tap About at (86.3%, 60.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'About', 86.3, 60.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="photodirector.SettingPageViewController"]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView', container_w=430, container_h=592)
    with step("[Action] Five tap developerButton at (44.9%, 30.0%)"):
        actions.five_tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'developerButton', 44.9, 30.0)
    with step("[Action] Tap Free at (61.8%, 47.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Free', 61.8, 47.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeApplication[@name="PhotoDirector"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView', container_w=430, container_h=932)
    with step("[Action] Tap Pro+ at (50.0%, 44.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Pro+', 50.0, 44.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeAlert[@name="Select an Option"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]', container_w=320, container_h=305)
    with step("[Action] Tap chevron.left at (45.0%, 52.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'chevron.left', 45.0, 52.8)
    with step("[Action] Tap btnBack at (57.1%, 55.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 57.1, 55.3)
    with step("[Action] Tap btnBack at (57.1%, 55.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnBack', 57.1, 55.3)
    with step("[Action] Tap Edit at (48.6%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 48.6, 52.0)
    with step("[Action] Tap btnAlbum at (65.0%, 40.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 65.0, 40.5)
    with step("[Action] Tap _AT at (5.0%, 0.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 5.0, 0.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-4 at (25.4%, 33.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-4', 25.4, 33.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Edit at (64.4%, 51.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 64.4, 51.1, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until ic_AI_expand"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_AI_expand', direction='left', offset_start=(0.612, 0.371), offset_end=(0.172, 0.371), velocity=465)
    with step("[Action] Tap ic_AI_expand at (21.2%, 69.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_AI_expand', 21.2, 69.7, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap ic_original_size at (75.6%, 65.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_original_size', 75.6, 65.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step17' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step17', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_custom_size at (22.0%, 46.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_custom_size', 22.0, 46.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step19' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step19', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_square at (68.3%, 68.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_square', 68.3, 68.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step21' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step21', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_2v3 at (61.0%, 65.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_2v3', 61.0, 65.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step23' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step23', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_3v2 at (67.5%, 65.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_3v2', 67.5, 65.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step25' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step25', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_3v4 at (70.0%, 73.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_3v4', 70.0, 73.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step27' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step27', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_4v3 at (65.0%, 68.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_4v3', 65.0, 68.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step29' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step29', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_9v16 at (36.6%, 82.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_9v16', 36.6, 82.9, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=431, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step31' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step31', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_16v9 at (80.5%, 46.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_16v9', 80.5, 46.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step33' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step33', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_4v5 at (61.0%, 75.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_4v5', 61.0, 75.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=431, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step35' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step35', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_5v4 at (95.1%, 73.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_5v4', 95.1, 73.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step37' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step37', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_IG4v5 at (51.2%, 80.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_IG4v5', 51.2, 80.5, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step39' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step39', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_IG9v16 at (78.0%, 87.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_IG9v16', 78.0, 87.8, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=431, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step41' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step41', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_tictok9v16 at (78.0%, 75.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_tictok9v16', 78.0, 75.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=431, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step43' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step43', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_tictok16v9 at (65.9%, 75.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_tictok16v9', 65.9, 75.6, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=431, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step45' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step45', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_snapchat9v16 at (48.8%, 29.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_snapchat9v16', 48.8, 29.3, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=431, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step47' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step47', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_Youtube16v9 at (68.3%, 90.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_Youtube16v9', 68.3, 90.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step49' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step49', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_FB1.91v1 at (68.3%, 73.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_FB1.91v1', 68.3, 73.2, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=72)
    with step("[Verify] Capture '00159_ai_expand_Step51' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step51', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_undo at (74.0%, 49.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 74.0, 49.0)
    with step("[Verify] Capture '00159_ai_expand_Step53' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step53', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_redo at (48.0%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 48.0, 36.7)
    with step("[Verify] Capture '00159_ai_expand_Step55' for GT comparison"):
        actions.capture_for_gt('00159_ai_expand_Step55', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage', threshold=0.95)
    with step("[Action] Tap ic_snapchat9v16 at (34.1%, 34.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_snapchat9v16', 34.1, 34.1, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="canvasPanel"]/XCUIElementTypeOther/XCUIElementTypeCollectionView', container_w=430, container_h=72)
    with step("[Action] Tap Generate at (73.8%, 73.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 73.8, 73.9)
    with step("[Verify] Expand More is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Expand More')
    with step("[Action] Tap ic_undo at (65.3%, 36.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 65.3, 36.7)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.ACCESSIBILITY_ID, 'CutoutTileImage')
    with step("[Action] Tap ic_redo at (44.0%, 22.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 44.0, 22.4)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.ACCESSIBILITY_ID, 'zoomView', expected_result='different', threshold=0.95)
    with step("[Action] Tap Expand More at (41.5%, 55.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Expand More', 41.5, 55.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='aiExpandResultPanelCollectionView', container_w=430, container_h=120)
    with step("[Action] Tap btn_cancel_n at (26.5%, 42.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 26.5, 42.9)
    with step("[Action] Tap ic_AI_expand at (72.7%, 57.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_AI_expand', 72.7, 57.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Generate at (61.3%, 17.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 61.3, 17.4)
    with step("[Action] Tap btn_ok_n at (81.6%, 51.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 81.6, 51.0)
    with step("[Verify] barImageView disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'barImageView', appear_timeout=5, disappear_timeout=1200), 'barImageView did not appear within 5s or is still shown after 1200s'
    with step("[Action] Tap btn_ok_n at (79.6%, 55.1%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 79.6, 55.1)
    with step("[Action] Tap homeButton at (61.5%, 46.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 61.5, 46.2)
    with step("[Action] Tap Discard at (68.1%, 0.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 68.1, 0.0)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.95)
    assert True
