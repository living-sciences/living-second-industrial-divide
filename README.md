# Living paper: The Second Industrial Divide (Piore & Sabel 1984)

This repository holds the working files behind the living-paper page
**https://livingscience.ai/econ/living-second-industrial-divide**: a claims-verification
scorecard and a 40-years-later predictions scorecard for a 1984 book, plus a
three-hypothesis evidence-weighing study of a reader's question about globalization.

**Book.** Piore, Michael J., and Charles F. Sabel. 1984. *The Second Industrial Divide:
Possibilities for Prosperity*. New York: Basic Books. 355 pp.
ISBN 0-465-07562-2 (paperback; hardcover 0-465-07561-4). Still in print via
Basic Books / Hachette. Full bibliographic record: `package/book.metadata.md`.

## No replication score, by design

This is a book, not a paper with a replication package: there is no code, no dataset and
no regression table to re-run, so no replication score exists and none is reported
anywhere in these files. Instead the studies grade each of the book's checkable
empirical claims and closing predictions with one of four verdict words (supported,
partially supported, contradicted, not checkable), on public statistics, with no pooled
number.

## Headline outcomes

- **Study 001 (claims and predictions).** Of 9 checkable claims and 3 gradeable
  predictions: **6 supported, 1 partially supported, 0 contradicted, 5 not-checkable**.
  The book's diagnosis of the mass-production crisis (durables saturation, the 1971-79
  macro break, the productivity exhaustion) holds up on public series, as do
  Emilia-Romagna's relative-income rise and the prediction that national mass production
  would not recover. The most interesting data result is the plant-size reversal: real,
  but confined to manufacturing, consistent with an outsourcing reading rather than a
  craft revival.
- **Study 002 (the globalization test).** A reader asked, anonymously through the site,
  whether globalization became a new mass-production system, the book's own Exit 1.
  Three pre-declared hypotheses were weighed across seven signatures on 1984-2026 data.
  Verdict: **"neither, the unbundling reading"** (a task-trade regime organized by
  lead-firm power), with two conditions disclosed up front: the verdict is
  **threshold-sensitive** (the winning hypothesis clears via a split-plus-S3 route, not
  a clean margin, and several cells are weak), and the pre-declared **"the book's
  dichotomy itself fails"** condition is simultaneously satisfied.
- **Study 003 (corrections).** A provenance audit passed both studies and raised six
  bounded label, provenance and sourcing fixes; 003 applied exactly those. No verdict
  word or evidence-grid cell changed. Every old-to-new change is in its
  `results/card_corrections.csv`.

## The attribution state: PROVISIONAL-PENDING-H1

The book's text is in copyright and no lawful machine-readable copy was obtainable, so
the studies never read the book itself. Every claim wording is anchored through named
secondary sources that verifiably quote or attribute it (the register is in the specs
and in `followup/001-*/results/gates.json`; 37 quote locators were grep-verified against
7 sources at run start). Each verdict therefore carries the tag
`PROVISIONAL-PENDING-H1`: it grades the claim as worded from the quoting literature,
honestly, not as worded in the book. A pre-registered re-grade branch (H1) will re-issue
any verdict whose grade could change once a lawfully obtained copy of the book is read;
claims with too few independent quoting sources were demoted to "not-checkable
(attribution)" rather than graded on memory. No book text ships in this repository, and
quotations inside the study outputs are short, fair-use-length fragments, each
attributed to its named quoting source (quotes routed through the Bhengu 2001 UCT
thesis name the thesis, per its license).

## What is in the repository

| Path | What it is |
|---|---|
| `briefing.md` | The Phase 0 feasibility briefing: why a book gets scorecards instead of a replication, the claims inventory (families B, C, D, P) the studies graded, the copyright constraints, and the human gates. |
| `followup/001-001-claims-and-predictions/` | Study 001: the verification layer. Grades 9 claims and 3 predictions on public statistics (OWID, Census HS-42, FRED, Eurostat, Census BDS, WDI, worldsteel, Rinaldi). Verdict rows in `results/scorecard.csv`; gates and the locator register in `results/gates.json`. |
| `followup/002-002-globalization-test/` | Study 002: the reader question (Exit 1 / prediction P2) weighed as three hypotheses across seven signatures; the evidence grid, per-cell verdicts and the E3 discriminator. |
| `followup/003-003-corrections/` | Study 003: the audit-conformance corrections, with `results/card_corrections.csv` (18 old-to-new rows) and `results/preview_corrections.md` (the China-BOF preview correction, flagged for the H1 re-grade). |
| `specs/` | The studies' registered designs, written and judge-gated before the studies ran. Each study's `instruction.md` is the copy it executed under. |
| `recency-research.md` | The recency research that scoped the studies: the 2020s evidence landscape, every data endpoint live-verified with dates, and the prior art (Schwartz 2024, Kaplinsky 2023) engaged rather than rediscovered. |
| `package/` | The book's source-of-record metadata (`book.metadata.md`) and the literature provenance register (`PROVENANCE.md`), including the redistribution flags that decided what ships here. |
| `extension-assets/` | The staged input data the studies read, included where the license allows, with `PROVENANCE.md` recording every URL, byte count, sha256 and fetch date (all fetches keyless, 2026-10-27). |
| `LARGE_FILES_OMITTED.md` | Everything left out for copyright or license reasons, with exact provenance for re-fetching it. |

## Reproducing

The studies are small data studies: CSV and JSON parsing plus small-series assembly,
well under one core-hour each, in Python 3 with pandas and matplotlib.

The study code is under `followup/*/workspace/` and reads a container staging mirror at
`/workspace/eval/followup_staging/shared-data/`, laid out exactly like
`extension-assets/` plus a `literature/` folder. To re-run: place the shipped
`extension-assets/` folders at that layout, re-fetch the non-shipped documents per the
URLs and sha256 hashes in `package/PROVENANCE.md` and `extension-assets/PROVENANCE.md`,
and convert the PDFs to text with `pdftotext` into each study's `workspace/pdftext/`
(the extracted texts are not shipped; see `LARGE_FILES_OMITTED.md`). Study 001 fetches
FRED series in-run (keyless, logged in `results/fetch_log.json`); study 002 re-runs
entirely from 001's shipped `results/` plus the staged data. Both studies re-verify the
staged files by sha256 at run start (`workspace/build_gates.py`).

## Data

Everything the studies read is inventoried, with URL, vintage, sha256 and fetch date, in
`extension-assets/PROVENANCE.md` and `package/PROVENANCE.md`, and audited row-by-row
against the code that used it. What ships follows each source's license:

- **US Census Bureau** Business Dynamics Statistics 2023-release CSVs and the
  Statistical Abstract HS-42 table (public domain): shipped.
- **World Bank WDI** extracts (CC BY 4.0) and **WITS / UNCTAD Stages-of-Processing**
  trade shares (free re-use with attribution): shipped. The WITS extract carries a
  binding seam note: UNCTAD-SoP "intermediates" is narrower than the BEC-based
  definition, so only the within-series trend is ever used.
- **Eurostat** regional GDP and SBS size-class extracts (CC BY 4.0): shipped, with the
  2020/2021 dataset break kept as two panels.
- **Our World in Data** US technology-adoption series (CC BY; underlying Comin & Hobijn
  CHAT): shipped.
- **FRED** series (OPHNFB, MFPNFBS, MANEMP, PAYEMS): fetched in-run, cached under
  `followup/001-*/workspace/data/`, cite FRED.
- **worldsteel** *World Steel in Figures 2025* and the **WTO** Global Value Chain
  Development Report 2025 chapters: free publications, linked rather than re-hosted;
  the hand-read values are disclosed row-by-row in the study outputs.
- **Emilia-Romagna historical income**: the graded historical values (7th in 1951, +29%
  versus the Italian mean in 1980, 2nd place in 1995) come from Alberto Rinaldi's DEMB
  working paper (University of Modena and Reggio Emilia, open repository), and Rinaldi
  is the source to credit for those numbers; an ISTAT regional factsheet was staged as
  context but no graded value traces to it.
- **Quoting and adjudication literature** (Schwartz 2024, Berger 2013, Bhengu 2001,
  Hampson 1991, Carlsson 1988, Gereffi-Humphrey-Sturgeon 2005, Sturgeon 2008, Kaplinsky
  2023, Baldwin 2006): not re-hosted; every item's canonical link, DOI or handle is in
  `package/PROVENANCE.md` and `LARGE_FILES_OMITTED.md`.

## Terms

The book's text remains the copyright of its authors and Basic Books; nothing from it
ships here beyond short, attributed, fair-use-length quotations inside the study
outputs. Shipped data files remain under their sources' terms: US Census files are
public domain; WDI, Eurostat and OWID extracts are CC BY 4.0; the WITS extract carries
World Bank/UNCTAD attribution terms. Study code and reports in this repository may be
reused with attribution to the living-paper page above.
