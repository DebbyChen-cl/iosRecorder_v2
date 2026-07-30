import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions


@pytest.mark.name("reshape_shape_preset")
def test_reshape_shape_preset(actions: DriverActions):
    with step("[Action] Tap 'Edit'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Launcher_main_edit', 48.1, 28.0, container_by=AppiumBy.XPATH, container_value='//XCUIElementTypeOther[@name="LauncherProViewController"]/XCUIElementTypeScrollView', container_w=320, container_h=623)
    with step("[Action] Expand album list"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum', 50.0, 50.0)
    with step("[Action] Select 'Sample Photos' album"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Sample Photos', 28.4, 0.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='albumCollectionView', container_w=294, container_h=557)
    with step("[Action] Select the single-woman photo with large face"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'PhDM_example_3', 50.0, 50.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoCollectionView', container_w=320, container_h=557)
    with step("[Action] Tap 'Portrait' tab"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'Portrait', 49.1, 48.5, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='ScrollableMenuView', container_w=320, container_h=33)
    with step("[Action] Tap 'Beautify'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_beautify', 50.0, 52.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='EditViewControllerBottomBarCollectionView', container_w=320, container_h=72)
    with step("[Action] Tap 'Reshape'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_reshape_portrait', 48.0, 52.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='photoEditFeatureCollectionView', container_w=320, container_h=72)

    # --- Natural ---
    with step("[Action] Tap 'Natural'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_natural', 50.0, 52.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=320, container_h=72)
    with step("[Verify] Natural default value = 50"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50') is not False
    with step("[Verify] Natural effect is applied to preview"):
        assert actions.capture_for_preview('natural_default', 'before', AppiumBy.ACCESSIBILITY_ID, 'AppLogo')
    with step("[Action] Adjust slider to min"):
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 'left', velocity=246.0, from_pct_x=50.0, from_pct_y=48.6, distance_pts=123.0)
    with step("[Verify] Natural value = 0"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0') is not False
    with step("[Verify] Natural no effect at min"):
        assert actions.capture_for_preview('natural_min', 'before', AppiumBy.ACCESSIBILITY_ID, 'AppLogo')
    with step("[Action] Adjust slider to max"):
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 'right', velocity=492.0, from_pct_x=0.8, from_pct_y=48.6, distance_pts=246.0)
    with step("[Verify] Natural value = 100"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Natural effect is applied to preview"):
        assert actions.capture_for_preview('natural_max', 'before', AppiumBy.ACCESSIBILITY_ID, 'AppLogo')

    # --- Oval ---
    with step("[Action] Tap 'Oval'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_oval', 50.0, 52.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=320, container_h=72)
    with step("[Verify] Oval default value = 50"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50') is not False
    with step("[Verify] Oval effect is applied to preview"):
        assert actions.capture_for_preview('oval_default', 'before', AppiumBy.ACCESSIBILITY_ID, 'AppLogo')
    with step("[Action] Adjust slider to min"):
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 'left', velocity=246.0, from_pct_x=50.0, from_pct_y=48.6, distance_pts=123.0)
    with step("[Verify] Oval value = 0"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0') is not False
    with step("[Verify] Oval no effect at min"):
        assert actions.capture_for_preview('oval_min', 'before', AppiumBy.ACCESSIBILITY_ID, 'AppLogo')
    with step("[Action] Adjust slider to max"):
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 'right', velocity=492.0, from_pct_x=0.8, from_pct_y=48.6, distance_pts=246.0)
    with step("[Verify] Oval value = 100"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Oval effect is applied to preview"):
        assert actions.capture_for_preview('oval_max', 'before', AppiumBy.ACCESSIBILITY_ID, 'AppLogo')

    # --- V-line ---
    with step("[Action] Tap 'V-line'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_vline', 50.0, 52.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=320, container_h=72)
    with step("[Verify] V-line default value = 50"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50') is not False
    with step("[Verify] V-line effect is applied to preview"):
        assert actions.capture_for_preview('vline_default', 'before', AppiumBy.ACCESSIBILITY_ID, 'AppLogo')
    with step("[Action] Adjust slider to min"):
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 'left', velocity=246.0, from_pct_x=50.0, from_pct_y=48.6, distance_pts=123.0)
    with step("[Verify] V-line value = 0"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0') is not False
    with step("[Verify] V-line no effect at min"):
        assert actions.capture_for_preview('vline_min', 'before', AppiumBy.ACCESSIBILITY_ID, 'AppLogo')
    with step("[Action] Adjust slider to max"):
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 'right', velocity=492.0, from_pct_x=0.8, from_pct_y=48.6, distance_pts=246.0)
    with step("[Verify] V-line value = 100"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] V-line effect is applied to preview"):
        assert actions.capture_for_preview('vline_max', 'before', AppiumBy.ACCESSIBILITY_ID, 'AppLogo')

    # --- Baby ---
    with step("[Action] Tap 'Baby'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_baby', 50.0, 52.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=320, container_h=72)
    with step("[Verify] Baby default value = 50"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '50') is not False
    with step("[Verify] Baby effect is applied to preview"):
        assert actions.capture_for_preview('baby_default', 'before', AppiumBy.ACCESSIBILITY_ID, 'AppLogo')
    with step("[Action] Adjust slider to min"):
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 'left', velocity=246.0, from_pct_x=50.0, from_pct_y=48.6, distance_pts=123.0)
    with step("[Verify] Baby value = 0"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '0') is not False
    with step("[Verify] Baby no effect at min"):
        assert actions.capture_for_preview('baby_min', 'before', AppiumBy.ACCESSIBILITY_ID, 'AppLogo')
    with step("[Action] Adjust slider to max"):
        actions.swipe_on_element(AppiumBy.ACCESSIBILITY_ID, 'cpSlider', 'right', velocity=492.0, from_pct_x=0.8, from_pct_y=48.6, distance_pts=246.0)
    with step("[Verify] Baby value = 100"):
        assert actions.verify_text(AppiumBy.ACCESSIBILITY_ID, 'valueLabel', '100') is not False
    with step("[Verify] Baby effect is applied to preview"):
        assert actions.capture_for_preview('baby_max', 'before', AppiumBy.ACCESSIBILITY_ID, 'AppLogo')

    # --- Original ---
    with step("[Action] Tap 'Original'"):
        actions.tap_within_element(AppiumBy.ACCESSIBILITY_ID, 'ic_face_original', 50.0, 52.0, container_by=AppiumBy.ACCESSIBILITY_ID, container_value='adjustableOptionCollectionView', container_w=320, container_h=72)
    with step("[Verify] Original - no effect applied to preview"):
        assert actions.capture_for_preview('original_reset', 'before', AppiumBy.ACCESSIBILITY_ID, 'AppLogo')
    with step("[Verify] Screenshot comparisons"):
        assert actions.run_screenshot_comparisons(threshold=0.95) is not False
