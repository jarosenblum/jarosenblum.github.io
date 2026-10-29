# jarosenblum.github.io

Portfolio site, built with Jekyll on GitHub Pages (served from `main`, repo root).

## Structure

| Path | What it holds |
|---|---|
| `_case_studies/` | One file per case study. Copy `_TEMPLATE.md`; front matter carries the facts, the body carries the narrative. |
| `_data/strands.yml` | Research strands on the Approach page; cases link to them by id. |
| `_data/early_builds.yml` | Cards on the Work page's early-builds strip, oldest first. |
| `_layouts/`, `_includes/` | Shared page shell, case template, access line, gallery. Edit here, not per page. |
| `assets/snapshots/<case>/` | Screenshots only (sanitized). Every app gets 3 to 5. |
| `exhibits/<case>/` | Curated excerpts copied from source repos after the sanitization audit. |
| `scripts/check_cases.rb` | Publish gate. Runs in GitHub Actions on every push. |

## Rules the gate enforces

- Every case has 3 to 5 screenshots, each with alt text.
- A case marked beta or early alpha, or running on a paid key, has a caveat.
- A repo link renders only when `repo_public_audited: true`.
- No `[P3` placeholder copy and no `placeholder: true` at publish time.

Run locally: `ruby scripts/check_cases.rb`. Before launch (`launched: false` in
`_config.yml`) it skips the placeholder-copy checks; `--strict` forces the full
publish gate. Setting `launched: true` also removes the pre-launch `noindex` tag.

## Downloads

Binaries (e.g. the SpeedGrader Rubric Review macOS build) go up as GitHub
Release assets on this repo, never committed to the tree.
