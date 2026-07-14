# Contributing

Thank you for helping make knowledge bases easier for humans to understand and agents to maintain.

## Before Opening a Pull Request

1. Do not include a personal vault, raw source document, browser capture, credential, private URL, or user configuration.
2. Add or update tests for scripts that change behavior.
3. Preserve the root `.wiki-rules.md` contract and the separation between `raw/`, reading cards, and durable knowledge pages.
4. For third-party code or assets, add the exact upstream URL, SPDX license, copyright notice, and required license text before requesting inclusion.
5. Run the checks in [docs/PUBLISHING_CHECKLIST.md](docs/PUBLISHING_CHECKLIST.md).

## Good Contributions

- Better source location and evidence tracking
- Safer import and conversion fallbacks
- Obsidian-first navigation and reading-card ergonomics
- Tests that protect human-readable output contracts

## Changes That Need Discussion First

- New cloud services or paid APIs
- New binary or model dependencies
- Changes that move original documents into a vault
- Changes that alter existing reading-card semantics
