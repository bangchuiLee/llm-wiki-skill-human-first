# Agent Guide

`llm-wiki` is a shared human-agent knowledge base, not a disposable retrieval index.

## Required Reading Order

1. Read `SKILL.md`.
2. Resolve the active vault and read its root `.wiki-rules.md`.
3. Read the target `raw/` text and corresponding `wiki/sources/` reading card before modifying knowledge pages.

## Write Boundaries

- Treat `raw/` as complete input text. Do not rewrite it to record a user's new opinion.
- Store interpretations, objections, practice notes, and questions on the matching reading card.
- Keep the external original outside the vault and retain `original_ref`, `source_hash`, `extraction_method`, and locator metadata.
- Do not promote a user's personal interpretation into a source fact.
- Update an entity, topic, or synthesis page only when the user asks to propagate the feedback.

## Source Quality

Use page, slide, worksheet range, heading, or quotation anchors whenever available. Mark unsupported or ambiguous extraction clearly rather than inventing a precise locator.

## Optional Capability Recovery

For an optional source, run `bash scripts/adapter-state.sh check <source_id>` before extraction. When it reports a missing command or environment, follow [docs/OPTIONAL_ADAPTERS.md](docs/OPTIONAL_ADAPTERS.md): verify the upstream and license, install the recommended prerequisite and adapter through an approved mechanism, ensure its command is on `PATH`, and re-run the check. Do not claim an optional capability is available until that check reports `available`.

If a listed implementation is intentionally unspecified, such as YouTube extraction, do not install a same-named package by guesswork. Select only a separately verified implementation and retain its provenance in the consuming project. Use the manual fallback when verification or installation is not possible.
