# Provenance and License Audit

This file records the evidence used to decide what may be redistributed in the public core. A dependency is not included merely because it has a familiar name; the project requires a direct file-to-upstream or file-to-license connection.

## Upstream Skill

This repository is a customized derivative of [sdyckjq-lab/llm-wiki-skill](https://github.com/sdyckjq-lab/llm-wiki-skill). The upstream author is `sdyckjq-lab`; its published project credits [Andrej Karpathy's llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) as the methodology source.

| Component | Evidence reviewed on 2026-07-15 | License conclusion | Public-core decision |
|---|---|---|---|
| Upstream Skill core | Upstream `README.md` has an MIT badge and an `## License` section stating `MIT`; upstream root `package.json` declares `"license": "MIT"`; reviewed revision `37aba6cbb07e058313f410cbedb23a13d661028b` | Upstream-declared MIT | Included as a customized derivative with explicit upstream attribution in `NOTICE`, both READMEs, and citation metadata |

GitHub does not currently detect a root-level upstream `LICENSE` file. This public distribution therefore records the concrete upstream MIT declarations and revision rather than inventing a separate provenance claim.

| Component | Evidence | License conclusion | Public-core decision |
|---|---|---|---|
| `deps/d3.min.js` | Local `LICENSE-d3.txt` names Mike Bostock and grants ISC-style permission | ISC | Included with license text |
| `deps/marked.min.js` | Local `LICENSE-marked.txt` names MarkedJS and includes MIT text | MIT | Included with license text |
| `deps/purify.min.js` | Local `LICENSE-purify.txt` names DOMPurify / Cure53 and includes Apache-2.0 and MPL-2.0 | Apache-2.0 option selected | Included with license text |
| `deps/rough.min.js` | Local `LICENSE-roughjs.txt` names Preet Shihn and includes MIT text | MIT | Included with license text |
| `baoyu-url-to-markdown` | Local Skill metadata names `https://github.com/JimLiu/baoyu-skills`; upstream GitHub `LICENSE` identifies MIT, copyright Jim Liu | MIT upstream confirmed | Not bundled; documented as external adapter |
| `youtube-transcript` local wrapper | Local wrapper identifies only the dependency `youtube-transcript-api`; no author, copyright header, repository URL, or exact upstream match was confirmed | Wrapper license unverified. `youtube-transcript-api` itself is MIT, but that does not license this wrapper. | Excluded |

## Maintainer Rule

For every future bundled dependency, record: the exact local file or package, its exact upstream URL, its SPDX identifier, the retained license text, and any required notices. If any link in that chain is missing, keep the component external until it is resolved.
