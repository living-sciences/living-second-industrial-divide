# Follow-up Study 001 — Claims and Predictions
## Piore & Sabel (1984), *The Second Industrial Divide* (Basic Books)

`REPLICATION: NOT APPLICABLE — BOOK, GO-WITH-SCOPE (Phase 0); THIS STUDY IS THE VERIFICATION LAYER`

## Question

This is a BOOK under a GO-WITH-SCOPE verdict: there is **no Phase 1
replication and no replication score**. The task is to build the verification
layer — an inventory-with-verdicts that reconstructs the book's checkable
empirical claims (families B, C, D) from public statistics for the period the
book describes (~1950–1984), grades each with one of four verdict words, and
extends three of its four closing predictions (P1, P3, P4) to 1984–2025. Each
claim is graded in a **provisional branch** (worded from the Phase 0 briefing,
tagged `PROVISIONAL-PENDING-H1`) with attribution and adjudication sources kept
strictly separate; no pooled numeric score is produced on any surface. P2
(Exit 1 / globalization) is out of scope and is study 002 entire.

## Approach

There was no replicated codebase to reuse (the scaffold README confirms "no
replicated codebase because there is no code: study 001 IS the verification
layer"), so the study was built from the staged data under
`followup_staging/shared-data/` and the instruction's pre-registered decision
statistics. Blocks, all checkpointed under `workspace/checkpoints/`:

- **Block A (gates).** A1 re-verified all 13 staged data files against their
  PROVENANCE sha256 (**13/13 match**). A1b re-ran all **37** §I.1b
  attribution-locators with the canonical commands (`grep -F` on the Schwartz
  HTML; `pdftotext … | tr -s | grep -F` on the PDFs) — **all 37 hit at their
  expected counts, zero misses**, so no source was dropped. A2 confirmed series
  coverage (BDS 1978–2023, WITS 1988–2023, Eurostat E-R 2000–2024, OWID
  durables through ≥1973, HS-42 1973 TV row). A3 confirmed no `williams1987`,
  `indstat`, or `ds140` staged → the C4/D1 restoration events did **not** fire;
  USGS stays blocked; UNIDO stays excluded. Full log: `results/gates.json`.
- **Declared in-run fetches** (keyless, foreground, logged in
  `results/fetch_log.json`): FRED CSVs for B3/P1 (OPHNFB, MFPNFBS, MANEMP,
  PAYEMS) and the Eurostat `nama_10r_2gdp` branch for Baden-Württemberg (DE1).
  USGS DS140 was **not** attempted (blocked CDN; policy-forbidden in-run).
- **Block B (claims)** and **Block C (predictions + figures):** per-claim
  series to `results/claim_*.csv`, verdict rows to `results/scorecard.csv`,
  three figures.
- **Block D:** `results/findings.md`, this report, the result card.

**Deviation (logged):** B3's named series OPHMFG begins in 1987 and cannot
reach the pre-1973 window required by the decision statistic; the canonical long
successor OPHNFB (nonfarm-business output per hour, 1947+) was used under the
"or successor" clause. These are economy/nonfarm-business, not
manufacturing-only, series.

## Results

**Verdict tally (no pooled score): of 9 checkable claims and 3 gradeable
predictions — 6 supported, 1 partially supported, 0 contradicted, 5
not-checkable.**

| Row | Claim / prediction (provisional wording) | Verdict | Key evidence |
|---|---|---|---|
| B1 | Durable markets saturated by early 1970s | **supported** | 4/4 durables ≥0.93× their 1984 penetration by 1973 (Auto .943, Fridge 1.000, Washer .930, TV .983) |
| B2 | Demand-stabilization regime broke 1971–79 | **supported** (timeline) | Bretton Woods end / oil shocks / stagflation fall in window; causal weight [LIT] |
| B3 | Mass-production productivity internally exhausted | **supported** | Labor prod. growth 2.58%→1.58%; TFP 1.71%→0.58% (1950–73 vs 1974–84) |
| C1 | Emilia-Romagna rose in relative income | **supported** | 7th (1951) → +29% vs Italy (1980) → 2nd place (1995); +19.5% in 2024 |
| C4 | US specialty steel/minimills thrived | **not-checkable (attribution)** | zero verified anchors; data: US EAF 71.8% (2024), 1970s level not-checkable |
| C5 | Programmable tech → economic small batches | **supported** (implication) | manuf. small-plant share 27.7%→32.5%, mean size 58.7→45.8; mechanism [LIT] |
| C2/C3 | District-sector growth; BW/Japan parallels | **not-checkable (data+attribution)** | BW 144.0%→130.8% of EU27 (data story); no 1980s backcast, no sector series |
| D1 | Plant-size reversal | **not-checkable (attribution)** | data story *qualified*: reversal in manufacturing, not economy-wide |
| D2 | Deskilling vs re-skilling | **not-checkable ([LIT])** | labor-process debate, out of data scope |
| P1 | Mass production won't recover | **supported** | VA share US 16.1%→10.5% (1997→2021), DE 24.6%→18.9% (1991→2023), JP 23.4%→19.5% (1994→2023), WDI true coverage; US emp 19.0%→8.0% (1984→2025) |
| P3 | Flexible specialization could dominate | **partially supported** (modal) | districts persisted (factual component); dominance *possibility not realized* |
| P4 | Exits are a political choice | **not-checkable ([INTERP])** | interpretive, not data-decidable |
| P2 | Exit 1 / globalization | **see study 002** | handed off with PS-B4 mapping note |

### Headline findings

- **The book's diagnosis of the mass-production crisis holds up well.**
  Consumer-durable saturation (B1), the 1971–79 macro-regime break (B2), and the
  internal productivity exhaustion (B3) are all supported on public series.
- **The flexible-specialization showcase is confirmed where it can be
  attributed and measured.** Emilia-Romagna's relative-income rise (C1) is
  supported; the programmable-technology implication (C5) holds in manufacturing.
- **The single most interesting data result is D1.** The plant-size reversal
  the book predicted is real **but confined to manufacturing**: manufacturing
  establishments shrank (mean size 58.7→45.8) and small-plant employment share
  rose (27.7%→32.5%), 1978–2023, while economy-wide the opposite held
  (large service establishments). This is exactly Schwartz's "outsourcing twist"
  — firms shed scale via outsourcing/demerger, not via a craft revival. (D1's
  *verdict cell* is nonetheless not-checkable (attribution): only one source
  verifiably attributes the specific wording to the book.)
- **Predictions:** P1 (no recovery of national mass production) is clearly
  supported; P3 is a modal possibility whose dominance half "was not realized"
  while its factual component (districts persisting) holds.

### Comparison baseline

There is no replication run to compare against (book, GO-WITH-SCOPE; no
`replication_score.json` or `verdicts.json` exists — confirmed absent). Where a
"baseline" is shown on the card it is the historical/earlier-period value
(e.g. BDS 1978, Rinaldi 1951) against which the reconstructed trajectory is
read. All numbers in this report were produced by this session's execution;
none was copied from the book or tuned toward an expected value.

## Deviations & limitations

1. **B3 series substitution (logged):** OPHMFG → OPHNFB, because the named
   series starts in 1987; nonfarm-business rather than manufacturing-only.
2. **C4 historical EAF unavailable:** USGS DS140 blocked, no OA
   Minerals-Yearbook quote staged — only the 2024 worldsteel endpoint is
   computable; the 1970s–84 level is reported as not-checkable (data) rather
   than filled from memory.
3. **C2/C3:** the Eurostat branch gave modern BW GDP but no 1980s backcast
   (`nama_10r_2gdp` starts 2000); the Italian district sector series is a named
   next-tick item.
4. **P1 (vintage seam, PS-PROV-1 correction):** the WDI manufacturing-VA
   shares were previously labeled "1984→2023" but are nearest-year
   substitutions — the WDI series (NV.IND.MANF.ZS) first non-missing year is
   USA 1997 / DEU 1991 / JPN 1994 (and USA last 2021), so no 1984 value exists;
   the labels are corrected to the TRUE years (US 1997→2021, DE 1991→2023,
   JP 1994→2023). DE/JP manufacturing-employment-share series were not staged;
   VA shares substitute for those two economies' employment leg. The employment
   leg (FRED, genuine 1984→2025) is the vintage-clean series that drives the
   verdict; direction (no recovery) is unaffected.
5. **All book-value anchors are provisional (H1).** No "the book says p.Y"
   claim is made; C4, D1 and C2/C3 are demoted to not-checkable (attribution)
   with their data stories still reported. A pre-registered H1 branch (not run
   here) will later re-issue any verdict whose grade could change against the
   book's own wording.
6. **Williams et al. 1987 was not read** (paywalled; not staged); our verdicts
   are independent of it and must be compared against it before external
   publication.
7. **No pooled score anywhere** (R5/H4/PS-C2). The result card and
   `followup_summary.json` contain only structured verdict tallies; neither
   schema has a score field, so none was nulled or hand-worked-around.

### Artifacts

`results/scorecard.csv`, `results/claim_*.csv` (B1, B3, C1, D1 economy +
manufacturing, P1 VA + US emp share, C4 worldsteel, C23 BW), `results/gates.json`,
`results/fetch_log.json`, `results/findings.md`, and three figures
(`fig_b1_saturation.png`, `fig_c1_emilia.png`, `fig_d1_plantsize.png`).
