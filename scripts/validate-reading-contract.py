#!/usr/bin/env python3
"""Validate the human-readable source and reading-card contract of an llm-wiki vault."""

from __future__ import annotations

import sys
from pathlib import Path


RULE_FILE = ".wiki-rules.md"
LEGACY_RULE_FILE = "wiki/.wiki-rules.md"
LAYER_READMES = {
    "raw/README.md": "完整输入文本层",
    "sources/README.md": "历史兼容区",
    "wiki/sources/README.md": "阅读卡层",
}
SOURCE_CARD_FIELDS = (
    "source_type",
    "source_path",
    "original_ref",
    "source_format",
    "extraction_method",
    "locator_scheme",
    "source_hash",
)
SOURCE_CARD_SECTIONS = ("原文定位", "我的批注与学习反馈")


def validate_contract(root: Path) -> list[str]:
    """Return all contract violations without modifying the vault."""
    errors: list[str] = []
    root = root.resolve()

    if not (root / RULE_FILE).is_file():
        errors.append("缺少根目录权威规则：.wiki-rules.md")
    if (root / LEGACY_RULE_FILE).is_file():
        errors.append("不允许保留第二份规则文件：wiki/.wiki-rules.md")

    for relative_path, expected_text in LAYER_READMES.items():
        file_path = root / relative_path
        if not file_path.is_file():
            errors.append(f"缺少层级说明：{relative_path}")
        elif expected_text not in file_path.read_text(encoding="utf-8"):
            errors.append(f"层级说明缺少约定文字：{relative_path} -> {expected_text}")

    template_path = root / "templates/source-card.md"
    if not template_path.is_file():
        errors.append("缺少阅读卡模板：templates/source-card.md")
        return errors

    template = template_path.read_text(encoding="utf-8")
    for field in SOURCE_CARD_FIELDS:
        if f"{field}:" not in template:
            errors.append(f"阅读卡模板缺少字段：{field}")
    for section in SOURCE_CARD_SECTIONS:
        if f"## {section}" not in template:
            errors.append(f"阅读卡模板缺少章节：{section}")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate-reading-contract.py <wiki_root>", file=sys.stderr)
        return 2

    errors = validate_contract(Path(argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("OK: reading-card contract validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
