# Corrective study: 003-corrections — audit conformance fixes for 001 and 002

The provenance audit passed both studies (13 load-bearing statistics recomputed cold, all
match; 16 locators re-grepped; gates, demotions, disclosures, copyright, privacy, reforms
all clean) with five bounded corrections. This study applies exactly those corrections
and nothing else. No verdict word changes; no grid cell moves. Record every old → new
change in this study's `results/card_corrections.csv` (file, item, old, new, reason).

Framing rules (binding): a mislabeled vintage is relabeled to the TRUE years with a seam
note, never left implying coverage that does not exist; an unsourced number is sourced
from a staged text or REMOVED, never kept on memory; nothing is upgraded.

## Corrections — study 001 (`followup/001-001-claims-and-predictions/`)

1. **PS-PROV-1 (material).** P1's value-added numbers labeled "1984→2023" are nearest-
   year substitutions (staged WDI coverage: USA 16.09 = 1997, 10.53 = 2021; DEU 24.62 =
   1991; JPN 23.39 = 1994). Relabel every surface that carries them (findings.md,
   report.md, followup_summary.json, results/claim_P1_va.csv) with the TRUE years and add
   the seam note: the WDI manufacturing-VA series starts too late for a 1984 baseline;
   the employment leg (FRED, genuine 1984→2025) is the vintage-clean series and already
   drives the verdict. State explicitly that the verdict direction is unaffected.
2. **PS-PROV-3 (minor).** Two stale log notes (gates.json note, fetch_log.json note)
   claim a "literature-quoted (Minerals Yearbook + Barnett&Crandall)" C4 branch that was
   never staged or used. Correct both notes to match the outputs' honest "not-checkable
   (data)" state.
3. **PS-PROV-4 (cosmetic).** Add the [PREVIEW-CALIBRATED] label block for the B1
   saturation rule to 001's gates.json (PS-C1 lists gates.json as a mandatory surface;
   mirror 002's gates label block format).

## Corrections — study 002 (`followup/002-002-globalization-test/`)

4. **PS-PROV-2 (material).** The EU SBS small-plant share labeled "34.8% (2005)" is the
   2011 value (EU27_2020 aggregates absent pre-2011 in the staged file; build_signatures.py
   hard-codes "_2005" key names). Relabel card M2, findings.md, and any other surface
   carrying the 2005 label with the true 2011 start + a one-line coverage note. The CSV
   artifact is already honest; the E3 window is unaffected — say so.
5. **PS-PROV-5 (minor).** The descriptive mega-plant row carries a from-memory Foxconn
   "~200k–350k" employment figure with no staged source. Check the staged texts
   (Kaplinsky 2023, WTO GVC chapters, Schwartz) for a citable figure: if one exists,
   cite it with a verified locator and move the value to results/s1_scale.csv where it
   belongs; if none exists, REMOVE the number (keep the row's qualitative sentence) and
   note the removal.

## Record-keeping (both studies' benefit; file under 003's results/)

6. **China-BOF preview correction flows back.** The run established the spec's
   [PREVIEW-KNOWN] "China ≈91.6% BOF" was the worldsteel Austria row; computed China BOF
   = 89.8%. Write results/preview_corrections.md recording old → new with the worldsteel
   row evidence, flagged for the H1 re-grade branch and the spec/PROVENANCE record. Do
   not edit the spec itself (orchestrator's file).

## Where things live

001 outputs: `followup/001-001-claims-and-predictions/`; 002 outputs:
`followup/002-002-globalization-test/`; staged data (read-only):
`followup_staging/shared-data/`. Edit files in place.

## Deliverables

report.md (one short section per item, including the item-5 outcome);
results/card_corrections.csv; results/preview_corrections.md; corrected files in place;
result_card.json for THIS study (status completed when all six are done; NO numeric
score — same score-free rule as the parent studies).

## Rules

Foreground only; no fetches; no new packages; `--timeout 7200`.