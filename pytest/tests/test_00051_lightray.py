import pytest
from appium.webdriver.common.appiumby import AppiumBy
from reportportal_client import step

from driver.driver_actions import DriverActions
import testdata as TD


@pytest.mark.name('00051_lightray')
def test_00051_lightray(actions: DriverActions):
    """Lightray"""
    mode = 1
    uuid = ['10eba25d-44c5-4dd4-96cb-031a5e246c44', '3ee72789-1313-4151-80c8-dbca443672a7', 'b98b19c9-b3e7-48fd-a803-3e26c25320bb', '94a496db-a74c-4fd6-87d5-8818bd029d2a', '2a590601-c82c-4298-bb95-c0972fb61405', 'dcc54f34-64fc-46ec-9474-0ce6d057ce28', '334fe2d0-0c48-4536-8d60-2e7797edc2ac', '33a2c9dd-0cf3-449c-8794-12437fe1e296', 'b8295918-56aa-4adb-9fd3-fd6f58acc2ae', 'd28d568d-cf28-416e-9bd8-e5feea20e6ba', 'd51710e1-132f-4f35-83d2-e66400189451', '3c7bd413-fa81-4c0c-a067-a298009e2817', '49c71033-182f-41d3-9308-6f66d7d9c96c', 'f8cc92d7-6e5c-434c-b445-1cdbe74928e2', '95bf82a6-8e9f-4847-b0bc-d99e8c7fe356', 'face12ac-5858-4174-9bc4-9678fe23d30a', 'b256064e-0c0d-46eb-b196-55e2b3040594', '28cffd51-6a1c-4797-ace8-92acd5b700b3', '22705744-24e0-43b0-8f85-b540ebd75a08', '55df32b4-e6cb-461b-984b-35377ddebbd6', 'af41c317-82f3-48f5-b8ec-4a6d8e1de7c3', '4c309447-cf89-49ff-8aff-6169a9cf09f6', '54d73900-f9d2-4172-8ea9-c6594ea7f4a1', '7d254808-f453-4312-8426-02563cbb3afa', 'f1eaf0cf-5413-41d6-86d4-a3decc8ede3d', '3f951809-21c6-4d23-9d8f-a3c33002f623', 'f838a93f-0db3-4aa4-ae10-7e6b09284b1e', 'ef477c6d-3387-4575-8ef9-d4eb8f93e19c', '0ae8b74e-78c2-47a6-8208-bbb07ce1ff9a', 'e4f1ed49-ba0e-42f7-9ea6-4b8cbf4e3629', '01b9d45c-176c-4f72-b0db-ae4daf54a9d9', 'd799b59d-5ba9-47d5-a434-db7a8b7b0281', 'bc16f46a-d337-4703-aad3-b0358364aedf', '2a322154-6b88-4d3b-aef2-a7c113ed4a2f', 'd50845b6-65f4-44f6-8eca-5fb7c5d6b227', 'e7ab0d56-2379-4c59-997d-0caebdf381e3', '9452df0c-33cc-413e-aa7e-fcb32c218e8f', '2b35ee32-6069-4173-9898-22af2fe03b91', 'cd007b10-15b9-49f7-9800-3157b60432d9', 'ce162701-45c2-46a1-b7d1-b7433477c2ff', '3a215b79-7deb-47e0-bc20-46dd4b5f5cc4', 'e7dfb6d3-a2e7-43c1-8a4f-e099b52ed897', '2db48b00-021b-4b75-b6b1-36e0310ba8b8', '2f7fbbec-8be5-4359-8cd8-c1b4573126a3', 'd37bd8de-3f72-424b-8ca1-ac1ed52b969f', '291f6934-aca5-4c99-8b3d-45ebaa346a4a', 'd911c6ff-0708-452f-8d76-726ec5c25922', '771b8b08-b805-4aee-8e5d-00275f0f779c', '984541e0-3431-410b-b587-24df000b31c2', 'f9d1bc82-a188-4779-a056-35626460d2ff', '4889e706-a04a-494c-8f7b-57dccf62470d', 'f5cc0f51-c665-465c-8733-602417c23a9d']
    with step('[Action] tap_editphoto'):
        actions.tap_by_locator(AppiumBy.NAME, 'Edit Photo')
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnAlbum')
    with step('[Action] select_category'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, '_AT')
    with step('[Action] select_photo'):
        actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'photoCell-0')
    with step('[Action] close_interstitial'):
        if actions.is_element_present(AppiumBy.ACCESSIBILITY_ID, 'btnIAP', timeout=2):
            actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnIAP')
    with step('[Action] tap_effects1_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Effects')
    from_pos = (380, 770)
    destination = (50, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(380, 770, 50, 770)
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_live_n')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light Ray')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Single source')):
        assert False, 'select single source fail'
    with step('[Verify] snapshot: base05_17_01_single_source.png'):
        actions.capture_for_gt('base05_17_01_single_source.png', crop_rect=(0, 507, 276, 573))
    if actions.compare_with_gt('05_17_01_single_source.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'select single source fail'
    with step('[Verify] snapshot: 05_17_01_before_move.png'):
        actions.capture_for_gt('05_17_01_before_move.png', crop_rect=(0, 60, 276, 597))
    destination = (351, 500)
    source_bounds = actions.get_element_bounds(AppiumBy.ACCESSIBILITY_ID, 'redDot')
    with step('[Action] drag_lightray'):
        actions.drag_coordinates(
            source_bounds[0] + source_bounds[2] // 2,
            source_bounds[1] + source_bounds[3] // 2,
            destination[0],
            destination[1],
        )
    with step('[Verify] snapshot: 05_17_01_after_move.png'):
        actions.capture_for_gt('05_17_01_after_move.png', crop_rect=(0, 60, 276, 597))
    if (not actions.compare_with_gt('05_17_01_after_move.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'move light source fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Single source')):
        assert False, 'enter adjust fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Intensity')):
        assert False, 'tap intensity fail'
    with step('[Verify] snapshot: 05_17_01_before_intensity1.png'):
        actions.capture_for_gt('05_17_01_before_intensity1.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Verify] snapshot: 05_17_01_after_intensity1.png'):
        actions.capture_for_gt('05_17_01_after_intensity1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_intensity1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust intensity fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False, 'tap reset fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False, 'tap reset fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '45'):
        pass
    else:
        assert False, 'undo fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Length')):
        assert False, 'tap length fail'
    with step('[Verify] snapshot: 05_17_01_before_length1.png'):
        actions.capture_for_gt('05_17_01_before_length1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')):
        assert False, 'adjust length fail'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')):
        assert False, 'adjust length fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Verify] snapshot: 05_17_01_after_length1.png'):
        actions.capture_for_gt('05_17_01_after_length1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_length1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust length fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False, 'tap reset fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '55'):
        pass
    else:
        assert False, 'undo fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light Color')):
        assert False, 'tap color fail'
    with step('[Verify] snapshot: 05_17_01_before_hue1.png'):
        actions.capture_for_gt('05_17_01_before_hue1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')):
        assert False, 'adjust hue fail'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')):
        assert False, 'adjust hue fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('175', '176', '177', '178', '179', '180')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Verify] snapshot: 05_17_01_after_hue1.png'):
        actions.capture_for_gt('05_17_01_after_hue1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_hue1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust hue fail'
    with step('[Verify] snapshot: 05_17_01_before_saturation1.png'):
        actions.capture_for_gt('05_17_01_before_saturation1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')):
        assert False, 'adjust saturation fail'
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')):
        assert False, 'adjust saturation fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('95', '96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Verify] snapshot: 05_17_01_after_saturation1.png'):
        actions.capture_for_gt('05_17_01_after_saturation1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_saturation1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust saturation fail'
    for _ in range(4):
        with step('[Action] tap_undo_btn_n'):
            for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
                if actions.is_element_present(__by, __val, timeout=2):
                    actions.tap_by_locator(__by, __val); break
    with step('[Action] get_lightray_hue_value'):
        assert actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '0'):
        pass
    else:
        assert False, 'reset fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Softness')):
        assert False, 'tap softness fail'
    with step('[Verify] snapshot: 05_17_01_before_softness1.png'):
        actions.capture_for_gt('05_17_01_before_softness1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')):
        assert False, 'adjust softness to 0 fail'
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('95', '96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Verify] snapshot: 05_17_01_after_softness1.png'):
        actions.capture_for_gt('05_17_01_after_softness1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_softness1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust softness fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False, 'tap reset fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    else:
        assert False, 'reset fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Expansion')):
        assert False, 'tap expansion fail'
    with step('[Verify] snapshot: 05_17_01_before_expansion1.png'):
        actions.capture_for_gt('05_17_01_before_expansion1.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('1', '2', '3', '4', '5')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Verify] snapshot: 05_17_01_after_expansion1.png'):
        actions.capture_for_gt('05_17_01_after_expansion1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_expansion1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust expansion fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False, 'tap reset fail'
    with step('[Action] tap_live_undo_btn_n'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '360'):
        pass
    else:
        assert False, 'reset fail'
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0.5')
    from_pos = (371, 760)
    destination = (158, 760)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(371, 760, 158, 760)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Range')):
        assert False, 'tap range fail'
    with step('[Verify] snapshot: 05_17_01_before_range1.png'):
        actions.capture_for_gt('05_17_01_before_range1.png')
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Verify] snapshot: 05_17_01_after_range1.png'):
        actions.capture_for_gt('05_17_01_after_range1.png')
    if (not actions.compare_with_gt('05_17_01_after_range1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust range fail'
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False, 'tap reset fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '80'):
        pass
    else:
        assert False, 'reset fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Direction')):
        assert False, 'tap direction fail'
    with step('[Verify] snapshot: 05_17_01_before_direction1.png'):
        actions.capture_for_gt('05_17_01_before_direction1.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('356', '357', '358', '359', '360')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0.5')
    with step('[Verify] snapshot: 05_17_01_after_direction1.png'):
        actions.capture_for_gt('05_17_01_after_direction1.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_direction1.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    if (not actions.try_tap_any([(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')])):
        assert False, 'tap reset fail'
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    with step('[Action] tap_undo_btn_n'):
        for __by, __val in [(AppiumBy.ACCESSIBILITY_ID, 'undoButton'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'ic_undo'), (AppiumBy.ACCESSIBILITY_ID, 'ic edit undo n'), (AppiumBy.ACCESSIBILITY_ID, 'btnUndo')]:
            if actions.is_element_present(__by, __val, timeout=2):
                actions.tap_by_locator(__by, __val); break
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '45'):
        pass
    else:
        assert False, 'reset fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_LightRayMode_n')):
        assert False, 'enter mode fail'
    with step('[Verify] snapshot: 05_17_01_before_hueshift.png'):
        actions.capture_for_gt('05_17_01_before_hueshift.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hue Shifting')):
        assert False, 'select hue shifting fail'
    with step('[Verify] snapshot: 05_17_01_after_hueshift.png'):
        actions.capture_for_gt('05_17_01_after_hueshift.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_hueshift.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'hue shifting fail'
    with step('[Verify] snapshot: 05_17_01_before_swaying.png'):
        actions.capture_for_gt('05_17_01_before_swaying.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Swaying')):
        assert False, 'select swaying fail'
    with step('[Verify] snapshot: 05_17_01_after_swaying.png'):
        actions.capture_for_gt('05_17_01_after_swaying.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_swaying.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'swaying fail'
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    with step('[Action] tap_phd_btn'):
        assert actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btnBack')
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Directional')):
        assert False, 'select directional fail'
    with step('[Verify] snapshot: base05_17_01_directional.png'):
        actions.capture_for_gt('base05_17_01_directional.png', crop_rect=(0, 507, 276, 573))
    if actions.compare_with_gt('05_17_01_directional.png', gt_folder=TD.GT_FOLDER)[0]:
        pass
    else:
        assert False, 'directional fail '
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Directional')):
        assert False, 'enter parameter adjustment fail'
    from_pos = (150, 770)
    destination = (350, 770)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(150, 770, 350, 770)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Intensity')):
        assert False, 'tap intensity fail'
    with step('[Verify] snapshot: 05_17_01_before_intensity2.png'):
        actions.capture_for_gt('05_17_01_before_intensity2.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Verify] snapshot: 05_17_01_after_intensity2.png'):
        actions.capture_for_gt('05_17_01_after_intensity2.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_intensity2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust intensity fail'
    if (not actions.tap_by_locator(AppiumBy.NAME, 'ic undo')):
        assert False, 'tap reset fail'
    with step('[Action] tap_live_undo_btn_n'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '45'):
        pass
    else:
        assert False, 'reset fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Length')):
        assert False, 'tap length fail'
    with step('[Verify] snapshot: 05_17_01_before_length2.png'):
        actions.capture_for_gt('05_17_01_before_length2.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Verify] snapshot: 05_17_01_after_length2.png'):
        actions.capture_for_gt('05_17_01_after_length2.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_length2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust length fail'
    if (not actions.tap_by_locator(AppiumBy.NAME, 'ic undo')):
        assert False, 'tap reset fail'
    with step('[Action] tap_live_undo_btn_n'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '55'):
        pass
    else:
        assert False, 'reset fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Direction')):
        assert False, 'tap direction fail'
    with step('[Verify] snapshot: 05_17_01_before_direction2.png'):
        actions.capture_for_gt('05_17_01_before_direction2.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('356', '357', '358', '359', '360')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Verify] snapshot: 05_17_01_after_direction2.png'):
        actions.capture_for_gt('05_17_01_after_direction2.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_direction2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust direction fail'
    if (not actions.tap_by_locator(AppiumBy.NAME, 'ic undo')):
        assert False, 'tap reset fail'
    with step('[Action] tap_live_undo_btn_n'):
        assert actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '45'):
        pass
    else:
        assert False, 'reset fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Light Color')):
        assert False, 'tap color fail'
    with step('[Verify] snapshot: 05_17_01_before_hue2.png'):
        actions.capture_for_gt('05_17_01_before_hue2.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_bokeh_hue_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '0')
    with step('[Action] adjust_bokeh_hue_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[1]', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') in ('176', '177', '178', '179', '180')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Verify] snapshot: 05_17_01_after_hue2.png'):
        actions.capture_for_gt('05_17_01_after_hue2.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_hue2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust hue fail'
    with step('[Verify] snapshot: 05_17_01_before_saturation2.png'):
        actions.capture_for_gt('05_17_01_before_saturation2.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_bokeh_saturation_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '0')
    with step('[Action] adjust_bokeh_saturation_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider[2]', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Verify] snapshot: 05_17_01_after_saturation2.png'):
        actions.capture_for_gt('05_17_01_after_saturation2.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_saturation2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust saturation fail'
    for _ in range(4):
        with step('[Action] tap_live_undo_btn_n'):
            assert actions.tap_by_locator(AppiumBy.NAME, 'ic undo')
    if ((actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]') == '0') and (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]') == '0')):
        pass
    else:
        assert False, 'reset fail'
    from_pos = (371, 760)
    destination = (158, 760)
    with step('[Action] brush_surrealart'):
        actions.drag_coordinates(371, 760, 158, 760)
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Softness')):
        assert False, 'tap softness fail'
    with step('[Verify] snapshot: 05_17_01_before_softness2.png'):
        actions.capture_for_gt('05_17_01_before_softness2.png', crop_rect=(0, 60, 276, 429))
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '0')
    with step('[Action] adjust_halftone_slider'):
        assert actions.set_slider(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSlider', '1')
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') in ('96', '97', '98', '99', '100')):
        pass
    else:
        assert False, 'change value fail'
    with step('[Verify] snapshot: 05_17_01_after_softness2.png'):
        actions.capture_for_gt('05_17_01_after_softness2.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_softness2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'adjust softness fail'
    if (not actions.tap_by_locator(AppiumBy.NAME, 'ic undo')):
        assert False, 'tap reset fail'
    if (actions.get_text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "light_ray"`]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText') == '0'):
        pass
    else:
        assert False, 'reset fail'
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'btn_LightRayMode_n')):
        assert False, 'enter mode fail'
    with step('[Verify] snapshot: 05_17_01_before_hueshift2.png'):
        actions.capture_for_gt('05_17_01_before_hueshift2.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Hue Shifting')):
        assert False, 'select hue shifting fail'
    with step('[Verify] snapshot: 05_17_01_after_hueshift2.png'):
        actions.capture_for_gt('05_17_01_after_hueshift2.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_hueshift2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'hue shifting fail'
    with step('[Verify] snapshot: 05_17_01_before_swaying2.png'):
        actions.capture_for_gt('05_17_01_before_swaying2.png', crop_rect=(0, 60, 276, 429))
    if (not actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Swaying')):
        assert False, 'select swaying fail'
    with step('[Verify] snapshot: 05_17_01_after_swaying2.png'):
        actions.capture_for_gt('05_17_01_after_swaying2.png', crop_rect=(0, 60, 276, 429))
    if (not actions.compare_with_gt('05_17_01_after_swaying2.png', gt_folder=TD.GT_FOLDER)[0]):
        pass
    else:
        assert False, 'swaying fail'
    with step("[Verify] test_00051 completion"):
        assert True
