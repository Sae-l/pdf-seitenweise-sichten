# Search PDF course material page by page

[Deutsch](README.md) · **English**

**Find the right page. Check text and images. Reuse content with its source.**

A local Python tool and agent skill for lecture slides, exercise sheets and formula collections. For anyone who wants to work with large PDFs without loading the whole document into an AI context every time.

![From a compact page index to the relevant text and a check against the original page.](docs/assets/ablauf.svg)

<p align="center">
  <a href="https://github.com/Sae-l/pdf-seitenweise-sichten/releases/tag/v1.6.1"><strong>Download v1.6.1</strong></a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#use-it-with-your-agent">Agents</a> ·
  <a href="#verification">Verification</a>
</p>

<p align="center">
  <a href="https://github.com/Sae-l/pdf-seitenweise-sichten/actions/workflows/checks.yml"><img src="https://github.com/Sae-l/pdf-seitenweise-sichten/actions/workflows/checks.yml/badge.svg?branch=main" alt="Current status of the Windows and Linux CI" /></a>
</p>

> The tool's messages, index headings and the detailed documentation are in German. Commands, file names and JSON fields are the same in every language.

## Search less. Work more precisely.

| Your goal | What the tool provides |
| --- | --- |
| Find an explanation or an exercise | A few short hits with document and PDF page, also for queries like "Aufgabe 9" (exercise 9). |
| Understand text, formulas and diagrams | Single text pages and, if needed, the rendered original page as an image. |
| Reuse content | Separate working copies as Markdown, LaTeX, CSV or image files, linked to their source. |
| Work with the same material later | Detection of changed sources and reuse of unchanged results. |

**Two parts, one workflow:** the [Python tool](scripts/sichtung.py) handles search, extraction and integrity checks. The [skill](SKILL.md) guides an agent through selecting pages, checking the original and citing sources. The tool also works without AI.

## Quick start

You need **Python 3.12 or newer** and Git. On macOS/Linux use `python3` if `python` is not available.

```sh
git clone --branch v1.6.1 --depth 1 https://github.com/Sae-l/pdf-seitenweise-sichten.git
cd pdf-seitenweise-sichten
python -m pip install -r scripts/requirements.txt
```

Put your own PDFs in a folder, for example `../Material`. Then:

```sh
# Index once, locally; always use a new output folder.
python scripts/sichtung.py extract "../Material" "../Material_Sichtung"

# Search instead of loading the whole document.
python scripts/sichtung.py search "../Material_Sichtung" "force acceleration"
```

Each hit names the file and the PDF page. Read that page:

```sh
# Example: replace file name and page with an actual hit.
python scripts/sichtung.py read "../Material_Sichtung" "Mechanics.pdf" 7
```

The original PDFs are never modified. Only PDFs directly inside the given folder are processed; subfolders are not included automatically. On Windows, PDFs and output may be on different drives. Installation, ZIP use and updates: [docs/installation.md](docs/installation.md) (German).

## Use it with your agent

As a plugin from this repository (Python with `pypdfium2` and `Pillow` must be installed locally):

```text
/plugin install pdf-seitenweise-sichten --marketplace Sae-l/pdf-seitenweise-sichten
```

That is the Claude Code command. For Codex: `codex plugin marketplace add Sae-l/pdf-seitenweise-sichten`, then `codex plugin add pdf-seitenweise-sichten@sae-l-skills`. Cursor and VS Code/Copilot read the skill from a project copy (below). An agent can do the setup itself: [instructions for agents](AGENTS.md#installation-für-nutzer). The [`plugins/`](plugins/pdf-seitenweise-sichten) folder is a generated copy of `SKILL.md`, `scripts/` and `references/`; changes are made only in the source files.

Alternatively, install the skill from the cloned repository into an **existing project**:

```sh
python scripts/install_projekt.py "../My-Project"
```

This creates full copies under `.agents/skills/` and `.claude/skills/`. Existing copies are never overwritten.

Example request once the skill is active:

```text
Find the projectile motion exercise in my material.
Name the document, PDF page and exercise number.
Check formulas against the original page image and do not reveal the final answer.
```

## From source to working copy

**Search → read the page → look at the original → save what you need.**

`search` returns at most five short hits by default. `read` returns the selected page and shows when a long text continues. For formulas, tables and diagrams, look at the actual page image. `save` then stores a working copy you prepared, together with source and content hashes.

| Command | Purpose |
| --- | --- |
| `extract` | Index PDFs locally and create a page index |
| `search` / `read` | Find matching content and read single pages |
| `render` | Provide an original page as an image |
| `save` | Store a prepared file with its source and review status |
| `check` | Technically verify sources, page lists, links and image references |

Detected solution sections (headings such as `Solutions`, `Answers`, `Lösungen`) are hidden by default; `--mit-antworten` includes them explicitly. Worked examples: [references/gezielte-nutzung.md](references/gezielte-nutzung.md) (German).

## Verification

- **Automated checks:** self-test, portable installation, plugin package, vault, syntax and checksums run on Windows and Linux. [GitHub Actions](https://github.com/Sae-l/pdf-seitenweise-sichten/actions/workflows/checks.yml)
- **Real material:** 27 PDFs with 218 pages freshly extracted and checked; five fixed search tasks, two original pages actually inspected and one formula working copy reused. [Measurement and limits](docs/umsetzung-pdf-werkzeug-2026-10-24.md) (German)
- **Package integrity:** each release contains the skill ZIP and its SHA-256 file. The [repository checksums](SHA256SUMS) cover the listed source files.

In the five search tasks the output contained **92–95 % fewer characters** than the full index of the respective group. This measures the selection step only: it is not a general token saving and does not include images.

**Review states stay distinct:** indexed, read as text, inspected as original image and reviewed for content are separate states. A matching hash or a rendered image does not confirm that a formula is mathematically correct.

## What you should know

The Python tool runs locally. What an AI agent sends to its provider depends on that agent's environment. Scans and image-only content cannot be searched without a text layer; OCR is not included. Search matches words literally, not by meaning. Solution detection is heuristic: unmarked answers and answers inside images still need care. A full acceptance test of all agent interfaces and a complete content review are still open.

## More

| Link | Content |
| --- | --- |
| [Installation and updates](docs/installation.md) | Project, ZIP, global links and cloud (German) |
| [Usage examples](references/gezielte-nutzung.md) | Search, page reading, images and working copies (German) |
| [Skill instructions](SKILL.md) | Binding workflow for agents (German) |
| [Changes](CHANGELOG.md) · [Release notes](docs/releases/v1.6.1.md) | What changed and known limits (German) |
| [Contributing](CONTRIBUTING.md) | Reporting bugs and checking changes (German) |

[MIT License](LICENSE) for the code and documentation in this repository. Rights to third-party PDF material remain with their owners. Developed by [Sae-l](https://github.com/Sae-l), originally for a formula collection project.
