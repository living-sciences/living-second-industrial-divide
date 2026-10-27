# Follow-up Study 003 — Corrective study: audit-conformance fixes for studies 001 and 002

## Question

A provenance audit passed both parent studies (001 claims-and-predictions; 002
globalization-test) — 13 load-bearing statistics recomputed cold all matched, 16 locators
re-grepped, and gates/demotions/disclosures/copyright/privacy/reforms all clean — but it
raised **five bounded corrections** plus one record-keeping item. This study applies
**exactly** those corrections and nothing else: no verdict word changes, no evidence-grid
cell moves, no numeric score. Every old → new change is logged in
`results/card_corrections.csv`. The binding framing rules were honored: a mislabeled vintage
is relabeled to its TRUE years with a seam note (never left implying coverage that does not
exist); an unsourced number is sourced from a staged text or REMOVED (never kept on memory);
nothing is upgraded.

## Approach

No parent pipeline was re-run. I read the parent studies' artifacts from disk and recomputed
each load-bearing number **cold** from the staged read-only data before touching any surface:
the WDI manufacturing-VA coverage (`wdi_manufacturing_trade_1960_2025.csv`), the EU SBS
small-plant series (`s1_eu_sizeclass.csv`), the worldsteel "Crude steel production by process"
table (`workspace/pdftext/worldsteel2025.txt`), and a full-corpus search of the staged texts
for a citable Foxconn/mega-plant employment figure. I then edited the parent files **in place**
and wrote this study's three deliverables (`card_corrections.csv`, `preview_corrections.md`,
and the card/summary/report). Three canvas figures were generated from the staged data. All
edited JSON was re-validated. 18 old → new rows are recorded in `card_corrections.csv`.

## Results — one section per item

### Item 1 — PS-PROV-1 (material): relabel P1's manufacturing value-added vintage (study 001)

Study 001's P1 carried manufacturing value-added shares labeled **"1984→2023"**. Recomputing
the staged WDI series `NV.IND.MANF.ZS` cold shows these are **nearest-year substitutions**: the
series has no 1984 value for any of the three economies. First non-missing years (and the
values the study used) are **USA 1997 = 16.09%, DEU 1991 = 24.62%, JPN 1994 = 23.39%**; the US
series also ends at **2021 = 10.53%** (2022–2025 missing), not 2023. Every surface carrying
these numbers was relabeled to the TRUE years with a seam note — `findings.md`, `report.md`,
`followup_summary.json`, and `results/claim_P1_va.csv` (whose `va_share_1984`/`va_share_2023`
columns were replaced by explicit per-country `baseline_year`/`endpoint_year` columns; values
unchanged). The seam note states, on each surface, that the WDI manufacturing-VA series starts
too late for a 1984 baseline, and that the **employment leg** (FRED MANEMP/PAYEMS, genuine
1984→2025: 19.0%→8.0%) is the vintage-clean series that **already drives the P1 verdict** — so
the verdict direction (no recovery) is **unaffected**. See `fig1_p1_va_vintage.png`.

| Economy | Mislabeled | True WDI coverage (relabeled) | Value |
|---|---|---|---|
| USA | 1984→2023 | **1997→2021** | 16.09% → 10.53% |
| DEU | 1984→2023 | **1991→2023** | 24.62% → 18.94% |
| JPN | 1984→2023 | **1994→2023** | 23.39% → 19.49% |

### Item 2 — PS-PROV-3 (minor): correct two stale C4 log notes (study 001)

Two notes claimed a *"literature-quoted (Minerals Yearbook + Barnett&Crandall)"* C4 historical-
EAF branch that was **never staged or used**. Both were corrected to the outputs' honest
**not-checkable (data)** state:
- `gates.json` `A3_staging_branch_flags.C4_historical_eaf_branch`: the old "literature-quoted …"
  string → a note that the 1970s–84 US EAF level has no staged supply route (USGS DS140 blocked;
  no OA Minerals-Yearbook/Barnett&Crandall quote ever staged), only the 2024 worldsteel endpoint
  computable.
- `fetch_log.json` `not_attempted[USGS DS140].reason`: "…→ C4 uses literature-quoted EAF branch"
  → "…→ C4 historical EAF is not-checkable (data), not filled from memory; no literature-quoted
  EAF branch exists."

### Item 3 — PS-PROV-4 (cosmetic): add the B1 [PREVIEW-CALIBRATED] label block to 001's gates.json

PS-C1 lists `gates.json` as a mandatory surface for the B1 saturation-rule preview label, which
was present in 001's `findings.md` prose but absent from its `gates.json`. I added a
`preview_calibration_labels_PS_C1` block mirroring study 002's gates label-block format, carrying
the `B1_saturation_rule` `[PREVIEW-CALIBRATED …]` label (1973 OWID/HS-42 values in view at spec
time: Automobile 82.0/.943, Household refrigerator 99.0/1.000, Washing machine 66.0/.930, TV
96.4%/.983) and the `banned_words_for_these_constants` (`pre-registered`, `validated`).

### Item 4 — PS-PROV-2 (material): relabel the EU SBS small-plant vintage (study 002)

Study 002 labeled the EU27 small-plant (<50 emp) share **"34.8% (2005)"**. The staged
`sbs_sc_ind_r2` file has **no EU27_2020 aggregate before 2011**; the 34.8% value is the **2011**
value (confirmed cold: `s1_eu_sizeclass.csv` first data row is `year=2011, 34.84`, and
`build_signatures.py`'s `p1rows[0]` is year 2011). The "2005-2020" string is the dataset's
nominal span, not this value's vintage; `build_signatures.py` had hard-coded `_2005` key names.
Relabeled to **"34.8% (2011)"** with a one-line coverage note on every carrying surface:
`findings.md`, `report.md`, `result_card.json` (card **M2**), both `_grid_keyresults.json` and
`_s1s3_keyresults.json` (keys `small_lt50_share_2005`→`_2011`, `large_ge250_share_2005`→`_2011`),
and `build_signatures.py` (key strings + corrective comment; the `"2005-2020"` panel filter left
intact as the dataset-span label). The `s1_eu_sizeclass.csv` artifact was already honest
(`year=2011`) and is unchanged; the **E3 window (2011–2026) is unaffected** because the
re-concentration it reads runs 2011→2023, fully inside coverage. See `fig2_eu_sbs_vintage.png`.

### Item 5 — PS-PROV-5 (minor): the mega-plant Foxconn figure — REMOVED (no staged source)

The descriptive mega-plant row (S1e) carried a from-memory Foxconn **"~200k–350k"** peak-
employment figure with no staged source. I searched the staged texts named by the instruction —
**Kaplinsky 2023, WTO GVC Report ch.1 & ch.2, Schwartz 2024** — for a citable single-plant
employment figure. **None exists:** Kaplinsky mentions Foxconn only as a *triangular-governance
intermediary* (no headcount); the one large worker-count in Kaplinsky is a **district** figure
(Jinjiang footwear cluster, >5,000 firms / >5,000,000 workers — not a single plant); WTO ch.1/ch.2
and Schwartz carry no Foxconn plant headcount. Per the framing rule, the number was **REMOVED**
from both `_grid_keyresults.json` and `_s1s3_keyresults.json` (the row's qualitative sentence —
Foxconn/EMS assembly-giant scale, descriptive only, no verdict weight — is kept), the removal is
noted, and **nothing was moved to `s1_scale.csv`** (no citable figure to move). The row carried
no verdict weight, so no cell moved.

### Item 6 — China-BOF preview correction flows back (record-keeping, filed under 003)

The parent run established that the spec's `[PREVIEW-KNOWN] "China ≈91.6% BOF"` is the worldsteel
**Austria** row; the computed **China BOF = 89.8%**. I confirmed this cold against the staged
worldsteel 2025 "Crude steel production by process, 2024" table: **Austria** 7.1 Mt, Oxygen
**91.6%**; **China** 1,005.1 Mt, Oxygen **89.8%**, Electric 10.2%. Recorded in
`results/preview_corrections.md` (old → new, with the worldsteel row evidence), **flagged for the
H1 re-grade branch and the spec/PROVENANCE record**. The spec itself was **not** edited (it is the
orchestrator's file). The correction gates nothing (R-6: the qualitative China≈BOF / US≈EAF split
holds at 89.8% as at 91.6%); no verdict or grid cell moves. See `fig3_china_bof_preview.png`.

## Deviations & limitations

- **No verdict word or grid cell changed**, by design — every item is a label/provenance/sourcing
  fix. No numeric/pooled score is produced (the parent studies' score-free GO-WITH-SCOPE rule is
  inherited).
- **Item 6 is recorded, not applied to the spec.** The instruction forbids editing the
  orchestrator's spec, so the China-BOF correction lives in `preview_corrections.md` and is flagged
  forward; study 002's own outputs (`s1_steel_split.csv`, `_grid_keyresults.json`) already carried
  the honest 89.8%.
- **Item 4 touched two surfaces beyond the three named** (`report.md`, both keyresults JSONs, and
  `build_signatures.py`) because they also carried the 2005 label; the instruction's "any other
  surface carrying the 2005 label" directs this. `build_signatures.py` is the generator — its
  `_2005` keys were fixed so a future re-run matches the corrected outputs; it was **not** re-run.
- **Item 5 outcome is a removal, not a citation**, because the staged texts yielded no citable
  figure — the instruction's explicit fallback. The removed value is quoted inside the removal note
  for provenance (documented as removed, not presented as a datum).
- **Item 1 extended to two more reader-facing surfaces** (`results/scorecard.csv` and
  `results/_blockB_keyresults.json`) that also carried the mislabeled VA vintage, under "relabel
  every surface that carries them". Study 001's **generator scripts** (`workspace/analyze.py`,
  `workspace/scorecard.py`) retain the internal `va_share_1984` key name: they are the mechanism,
  not a result surface, were not named in item 1, and were not re-run — I left them untouched to
  avoid scope creep (contrast item 4, where the instruction explicitly named `build_signatures.py`
  as the cause, so its `_2005` keys were fixed).
- All numbers here were recomputed cold from the staged read-only data; none was copied from the
  parent artifacts or tuned. Original (pre-correction) values are cited from the parent files in
  `card_corrections.csv` and `followup_summary.json`.
