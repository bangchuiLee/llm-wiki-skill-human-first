# Optional Adapters

The public core intentionally does not bundle external URL or YouTube extractor code. Optional adapters are not required for local Markdown files, pasted text, reading cards, or wiki maintenance. Install only the adapter required by the source at hand.

## Agent Installation Protocol

When `scripts/adapter-state.sh check <source_id>` reports `not_installed` or `env_unavailable`, an agent should:

1. Read the relevant section below and verify the upstream repository and license before installing anything.
2. Install the stated prerequisite and adapter using the user's approved package manager or Skill installation flow.
3. Ensure the declared command is on `PATH`.
4. Re-run `bash scripts/adapter-state.sh check <source_id>` before attempting extraction.
5. If installation is unavailable or extraction fails, use the documented manual fallback. Do not copy browser profiles, cookies, captures, or source originals into this repository or an Obsidian vault.

The expected commands are `baoyu-url-to-markdown`, `wechat-article-to-markdown`, and `youtube-transcript`. An adapter is available only when its expected command passes `command -v`.

## URL Pages, X/Twitter, and Zhihu

Recommended upstream: [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) (`MIT`, copyright Jim Liu). Install its `baoyu-url-to-markdown` Skill through the current agent platform's Skill installer, following the upstream instructions. The resulting `baoyu-url-to-markdown` command must be on `PATH`.

For pages that need login, the adapter may use a separately started Chrome debugging session. Treat browser profiles and cookies as local secrets; do not commit or distribute them. If the adapter cannot extract the page, copy the authorized article text into the ingest flow instead.

## WeChat

Recommended upstream: [jackwener/wechat-article-to-markdown](https://github.com/jackwener/wechat-article-to-markdown). Install `uv` from its [official installation instructions](https://docs.astral.sh/uv/getting-started/installation/), then install the tool:

```bash
uv tool install git+https://github.com/jackwener/wechat-article-to-markdown.git
```

Verify with `command -v wechat-article-to-markdown`. The site and any source content remain subject to their respective terms and rights. If extraction fails, open the authorized article and paste the text manually.

## YouTube

This repository deliberately does **not** recommend a particular wrapper implementation yet. The historical local `youtube-transcript` wrapper had no verifiable upstream or license, so it is excluded.

An agent may enable this source only after selecting a separately installed `youtube-transcript` command or Skill with a verifiable upstream, SPDX-compatible license, and compliance with YouTube terms and the content owner's rights. Record the selected implementation, version, and license in the consuming project's provenance record, put its command on `PATH`, then re-run the adapter-state check. Until then, ingest a user-provided subtitle file or pasted transcript.

## Graph Tooling

Interactive graph generation requires `jq` and Node.js. Install them with the host's package manager, confirm `jq --version` and `node --version`, then run the graph scripts. They are optional; Markdown reading cards and the rest of the wiki work without them.

## MarkItDown

MarkItDown integration is intentionally not included in this release preparation. When added, it must use an isolated Python environment, preserve the original binary outside the vault, write only derived Markdown into `raw/`, and record converter version, hash, extraction method, and page/slide/sheet locators.
