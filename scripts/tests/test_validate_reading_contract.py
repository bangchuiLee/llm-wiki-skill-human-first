import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).parents[1] / "validate-reading-contract.py"
SPEC = importlib.util.spec_from_file_location("validate_reading_contract", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ValidateReadingContractTests(unittest.TestCase):
    def create_valid_vault(self, root: Path) -> None:
        (root / "raw").mkdir()
        (root / "sources").mkdir()
        (root / "wiki" / "sources").mkdir(parents=True)
        (root / "templates").mkdir()
        (root / ".wiki-rules.md").write_text(
            "# Wiki 页面格式规范\n\n## 阅读卡\n\n## 原文定位\n\n## 我的批注与学习反馈\n",
            encoding="utf-8",
        )
        (root / "raw" / "README.md").write_text("完整输入文本层\n", encoding="utf-8")
        (root / "sources" / "README.md").write_text("历史兼容区\n", encoding="utf-8")
        (root / "wiki" / "sources" / "README.md").write_text("阅读卡层\n", encoding="utf-8")
        (root / "templates" / "source-card.md").write_text(
            "---\nsource_type: file\nsource_path: raw/articles/example.md\noriginal_ref: D:/sources/example.pdf\nsource_format: pdf\nextraction_method: markitdown\nlocator_scheme: page\nsource_hash: sha256:example\n---\n\n"
            "## 原文定位\n\n## 我的批注与学习反馈\n",
            encoding="utf-8",
        )

    def test_accepts_vault_with_a_single_authoritative_rule_and_reading_card_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.create_valid_vault(root)

            self.assertEqual(MODULE.validate_contract(root), [])

    def test_rejects_legacy_rule_location_and_missing_reading_card_sections(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.create_valid_vault(root)
            (root / ".wiki-rules.md").unlink()
            (root / "wiki" / ".wiki-rules.md").write_text("legacy", encoding="utf-8")
            (root / "templates" / "source-card.md").write_text("---\nsource_type: file\n---\n", encoding="utf-8")

            errors = MODULE.validate_contract(root)

            self.assertIn("缺少根目录权威规则：.wiki-rules.md", errors)
            self.assertIn("不允许保留第二份规则文件：wiki/.wiki-rules.md", errors)
            self.assertIn("阅读卡模板缺少字段：original_ref", errors)
            self.assertIn("阅读卡模板缺少章节：我的批注与学习反馈", errors)


if __name__ == "__main__":
    unittest.main()
