from __future__ import annotations

import json
from pathlib import Path

import pytest

from app import static_converter
from app.cli import run_cli


def write_fixture_project(root: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    source = root / "suite.py"
    (root / "pages.py").write_text(
        """
from appium.webdriver.common.appiumby import AppiumBy as By

class SettingsPage:
    feedback = (By.ACCESSIBILITY_ID, "Feedback")
    email = (By.NAME, "emailField")

    def open_feedback(self):
        self.driver.find_element(*self.feedback).click()

    def submit(self, email):
        self.driver.find_element(*self.email).send_keys(email)

""",
        encoding="utf-8",
    )
    source.write_text(
        """
from pages import SettingsPage

class Tests:
    def helper(self, page, email):
        page.open_feedback()
        if email:
            page.submit(email)
        assert page.driver.find_element(*page.feedback).is_displayed()

    def test_case_one(self):
        page = SettingsPage(driver)
        self.helper(page, "qa@example.com")
        self.driver.legacy_upload("fixture.png")

    # def test_disabled_case(self):
    #     pass
""",
        encoding="utf-8",
    )
    return source


def test_inventory_resolves_helpers_page_methods_and_disabled_cases(tmp_path: Path):
    source = write_fixture_project(tmp_path)

    inventory = static_converter.build_inventory(source)

    assert inventory["active_case_count"] == 1
    assert inventory["disabled_case_count"] == 1
    case = inventory["cases"][0]
    assert case["source_case"] == "test_case_one"
    assert [step["kind"] for step in case["steps"]] == ["tap", "branch", "assertion", "external"]
    assert case["steps"][1]["body"][0]["kind"] == "type_text"
    assert case["steps"][0]["locator"] == {"by": "AppiumBy.ACCESSIBILITY_ID", "value": "Feedback"}
    assert case["steps"][1]["body"][0]["locator"] == {"by": "AppiumBy.NAME", "value": "emailField"}
    assert case["coverage"]["unknown"] == 0
    assert case["coverage"]["branches"] == 1


def test_generator_preserves_branch_and_allocates_collision_safe_five_digit_names(tmp_path: Path):
    source = write_fixture_project(tmp_path / "project")
    inventory = static_converter.build_inventory(source)
    inventory_path = tmp_path / "inventory.json"
    inventory_path.write_text(json.dumps(inventory), encoding="utf-8")
    tests_dir = tmp_path / "generated"
    tests_dir.mkdir()
    (tests_dir / "test_00001_case_one.py").write_text("existing", encoding="utf-8")

    result = static_converter.generate_tests(inventory_path, tests_dir)

    generated = Path(result["files"][0])
    assert generated.name == "test_00001_case_one_1.py"
    text = generated.read_text(encoding="utf-8")
    assert "def test_00001_case_one_1(actions: DriverActions):" in text
    assert "if actions.legacy_condition('email'):" in text
    assert "from pages" not in text
    assert "actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feedback')" in text
    assert "actions.type_text_by_locator(AppiumBy.NAME, 'emailField', 'qa@example.com')" in text
    assert "assert actions.external_action(" in text


def test_validation_checks_generated_ast_and_inventory_coverage(tmp_path: Path):
    source = write_fixture_project(tmp_path / "project")
    inventory = static_converter.build_inventory(source)
    inventory_path = tmp_path / "inventory.json"
    inventory_path.write_text(json.dumps(inventory), encoding="utf-8")
    result = static_converter.generate_tests(inventory_path, tmp_path / "generated")

    report = static_converter.validate_artifacts(inventory_path, tmp_path / "generated")

    assert report["ok"] is True
    assert report["files_checked"] == len(result["files"])
    assert report["collection"]["ok"] is True
    assert report["runtime_readiness"]["ready"] is False
    assert report["runtime_readiness"]["hook_counts"]["external_action"] == 1
    assert report["errors"] == []


def test_inventory_rejects_missing_expected_case_count(tmp_path: Path):
    source = write_fixture_project(tmp_path)

    with pytest.raises(static_converter.StaticConversionError, match="expected 2 active cases"):
        static_converter.build_inventory(source, expected_active=2)


def test_generator_unwraps_step_context_and_normalizes_page_action_conditions(tmp_path: Path):
    root = tmp_path / "project"
    root.mkdir()
    (root / "pages.py").write_text(
        """
from appium.webdriver.common.appiumby import AppiumBy as By

class SettingsPage:
    feedback = (By.ACCESSIBILITY_ID, "Feedback")

    def open_feedback(self):
        self.driver.find_element(*self.feedback).click()
""",
        encoding="utf-8",
    )
    source = root / "suite.py"
    source.write_text(
        """
from pages import SettingsPage

class Tests:
    def setup_pages(self):
        self.settings_page = SettingsPage(driver)

    def test_case_one(self):
        with self.rp_step("Open feedback"):
            if not self.settings_page.open_feedback():
                assert False, "could not open feedback"
""",
        encoding="utf-8",
    )
    inventory = static_converter.build_inventory(source, project_root=root)
    inventory_path = tmp_path / "inventory.json"
    inventory_path.write_text(json.dumps(inventory), encoding="utf-8")

    result = static_converter.generate_tests(inventory_path, tmp_path / "generated")
    generated = Path(result["files"][0]).read_text(encoding="utf-8")

    assert "actions.tap_by_locator(AppiumBy.ACCESSIBILITY_ID, 'Feedback')" in generated
    assert "legacy_condition" not in generated
    assert "external_action" not in generated


def test_static_conversion_cli_runs_the_inventory_generation_and_validation_gates(tmp_path: Path):
    source = write_fixture_project(tmp_path / "project")
    inventory = tmp_path / "inventory.json"
    output_dir = tmp_path / "generated"

    code, payload = run_cli([
        "static-inventory", "--source", str(source), "--output", str(inventory), "--expected-active", "1",
    ])
    assert code == 0
    assert payload["active_case_count"] == 1

    code, payload = run_cli(["static-generate", "--inventory", str(inventory), "--tests-dir", str(output_dir)])
    assert code == 0
    assert payload["count"] == 1

    code, payload = run_cli(["static-validate", "--inventory", str(inventory), "--tests-dir", str(output_dir)])
    assert code == 0
    assert payload["files_checked"] == 1
