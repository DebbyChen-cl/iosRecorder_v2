import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("00160_ai_glow_up_20260806_182753")
def test_00160_ai_glow_up_20260806_182753(actions: DriverActions):
    with step("[Action] Tap Edit at (40.0%, 52.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Edit', 40.0, 52.0)
    with step("[Action] Tap btnAlbum at (66.5%, 40.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 66.5, 40.5)
    with step("[Action] Tap _AT at (9.7%, 68.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, '_AT', 9.7, 68.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=394, container_h=746)
    with step("[Action] Tap photoCell-0 at (16.9%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0', 16.9, 46.9, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=430, container_h=746)
    with step("[Action] Tap Portrait at (44.6%, 53.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 44.6, 53.3, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=430, container_h=45)
    with step("[Action] Scroll until ic_ai_glowup"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'EditViewControllerBottomBarCollectionView', AppiumBy.ACCESSIBILITY_ID, 'ic_ai_glowup', direction='left', offset_start=(0.621, 0.402), offset_end=(0.16, 0.402), velocity=526)
    with step("[Action] Tap ic_ai_glowup at (61.8%, 48.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_ai_glowup', 61.8, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Verify] Glow up your portraits in one tap! is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Glow up your portraits in one tap!')
    with step("[Action] Tap Try First at (77.1%, 62.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try First', 77.1, 62.5)
    with step("[Verify] Please choose another photo is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'Please choose another photo')
    with step("[Action] Tap AlertDialog-btnPositive at (48.7%, 76.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AlertDialog-btnPositive', 48.7, 76.0)
    with step("[Action] Tap ic_ai_glowup at (76.5%, 54.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_ai_glowup', 76.5, 54.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Try First at (30.0%, 16.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try First', 30.0, 16.7)
    with step("[Action] Tap Continue Anyway at (74.3%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway', 74.3, 66.7)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"aiGlowupPanelCollectionView\"]/XCUIElementTypeCell[1]/XCUIElementTypeOther[2] at (61.4%, 92.0%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="aiGlowupPanelCollectionView"]/XCUIElementTypeCell[1]/XCUIElementTypeOther[2]', 61.4, 92.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='aiGlowupPanelCollectionView', container_w=430, container_h=121)
    with step("[Action] Tap Generate at (31.2%, 50.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 31.2, 50.0)
    with step("[Verify] barImageView disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'barImageView', appear_timeout=5, disappear_timeout=1200), 'barImageView did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Capture '00160_ai_glow_up_Step18' for GT comparison"):
        actions.capture_for_gt('00160_ai_glow_up_Step18', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="editAreaView"]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.9)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"aiGlowupPanelCollectionView\"]/XCUIElementTypeCell[2]/XCUIElementTypeOther[2] at (61.4%, 48.2%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="aiGlowupPanelCollectionView"]/XCUIElementTypeCell[2]/XCUIElementTypeOther[2]', 61.4, 48.2, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='aiGlowupPanelCollectionView', container_w=430, container_h=121)
    with step("[Action] Tap Generate at (50.0%, 37.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 50.0, 37.5)
    with step("[Verify] Capture '00160_ai_glow_up_Step21' for GT comparison"):
        actions.capture_for_gt('00160_ai_glow_up_Step21', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="editAreaView"]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.9)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="editAreaView"]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage')
    with step("[Action] Tap ic_undo at (63.3%, 59.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_undo', 63.3, 59.2)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="editAreaView"]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage', expected_result='different', threshold=0.95)
    with step("[Verify] Capture 'screenshot' before screenshot"):
        actions.capture_for_preview('screenshot', 'before', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="editAreaView"]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage')
    with step("[Action] Tap ic_redo at (57.1%, 26.5%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_redo', 57.1, 26.5)
    with step("[Verify] Capture 'screenshot' after screenshot"):
        actions.capture_for_preview('screenshot', 'after', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="editAreaView"]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage', expected_result='different', threshold=0.95)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"aiGlowupPanelCollectionView\"]/XCUIElementTypeCell[3]/XCUIElementTypeOther[2] at (39.8%, 42.0%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="aiGlowupPanelCollectionView"]/XCUIElementTypeCell[3]/XCUIElementTypeOther[2]', 39.8, 42.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='aiGlowupPanelCollectionView', container_w=430, container_h=121)
    with step("[Action] Tap Generate at (45.0%, 20.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 45.0, 20.8)
    with step("[Action] Tap btnClose at (41.9%, 61.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnClose', 41.9, 61.3)
    with step("[Action] Tap btn_cancel_n at (32.7%, 28.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_cancel_n', 32.7, 28.6)
    with step("[Action] Tap ic_ai_glowup at (41.2%, 63.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_ai_glowup', 41.2, 63.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=430, container_h=97)
    with step("[Action] Tap Try First at (77.1%, 20.8%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Try First', 77.1, 20.8)
    with step("[Action] Tap Continue Anyway at (60.1%, 66.7%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Continue Anyway', 60.1, 66.7)
    with step("[Action] Tap //XCUIElementTypeCollectionView[@name=\"aiGlowupPanelCollectionView\"]/XCUIElementTypeCell[2]/XCUIElementTypeOther[2] at (40.9%, 45.5%)"):
        actions.tap_within_element(AppiumBy.XPATH, '//XCUIElementTypeCollectionView[@name="aiGlowupPanelCollectionView"]/XCUIElementTypeCell[2]/XCUIElementTypeOther[2]', 40.9, 45.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='aiGlowupPanelCollectionView', container_w=430, container_h=121)
    with step("[Action] Tap Generate at (45.0%, 58.3%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Generate', 45.0, 58.3)
    with step("[Verify] barImageView disappears within 1200s"):
        assert actions.wait_until_not_show(AppiumBy.ACCESSIBILITY_ID, 'barImageView', appear_timeout=5, disappear_timeout=1200), 'barImageView did not appear within 5s or is still shown after 1200s'
    with step("[Verify] Capture '00160_ai_glow_up_Step38' for GT comparison"):
        actions.capture_for_gt('00160_ai_glow_up_Step38', AppiumBy.XPATH, '//XCUIElementTypeOther[@name="editAreaView"]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeImage', threshold=0.9)
    with step("[Action] Tap btn_ok_n at (93.9%, 46.9%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btn_ok_n', 93.9, 46.9)
    with step("[Verify] Capture '00160_ai_glow_up_Step40' for GT comparison"):
        actions.capture_for_gt('00160_ai_glow_up_Step40', AppiumBy.ACCESSIBILITY_ID, 'EditingImageView_ImageView', threshold=0.9)
    with step("[Action] Tap homeButton at (57.7%, 69.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'homeButton', 57.7, 69.2)
    with step("[Action] Tap Discard at (56.5%, 29.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Discard', 56.5, 29.2)
    with step("[Action] Tap btnStudio at (63.2%, 38.2%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnStudio', 63.2, 38.2)
    with step("[Action] Scroll until AI Glow Up"):
        actions.scroll_until(AppiumBy.ACCESSIBILITY_ID, 'entryCollectionView', AppiumBy.ACCESSIBILITY_ID, 'AI Glow Up', direction='down', offset_start=(0.253, 0.497), offset_end=(0.253, 0.349), velocity=255)
    with step("[Action] Tap AI Glow Up at (63.2%, 31.6%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'AI Glow Up', 63.2, 31.6, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='entryCollectionView', container_w=396, container_h=724)
    with step("[Verify] lblTitle is visible"):
        actions.verify_visible(AppiumBy.ACCESSIBILITY_ID, 'lblTitle')
    with step("[Action] Tap navBackButton at (47.7%, 61.4%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'navBackButton', 47.7, 61.4)
    with step("[Action] Tap btnHome at (40.8%, 40.0%)"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnHome', 40.8, 40.0)
    with step("[Verify] Screenshot comparisons"):
        actions.run_screenshot_comparisons(threshold=0.9)
    assert True
