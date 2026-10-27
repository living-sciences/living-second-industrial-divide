# Findings — Study 001, claims-and-predictions
### Piore & Sabel (1984), *The Second Industrial Divide* (Basic Books)

`REPLICATION: NOT APPLICABLE — BOOK, GO-WITH-SCOPE (Phase 0); THIS STUDY IS THE VERIFICATION LAYER`

## METHOD

**This is a claims-verification scorecard for a book, not a replication.** The
work has no Phase 1 replication and no replication score, ever (GO-WITH-SCOPE).
It reconstructs the book's checkable empirical claims (families B, C, D) from
public statistics for the period the book describes (~1950–1984), grades each
with one of four verdict words, and extends three of its four closing
predictions (P1, P3, P4) to 1984–2025. P2 (Exit 1 / globalization) is out of
scope here and is study 002 entire. **No pooled numeric score is computed on
any surface** (R5/H4/PS-C2); the only aggregates are structured verdict
tallies.

Every claim/prediction row is graded in its **PROVISIONAL branch**, worded per
the Phase 0 briefing and tagged `book-anchor: PROVISIONAL-PENDING-H1`. No
lawful machine-readable copy of the book is in the corpus by design; no output
asserts "the book says X at p.Y". Sources are split into two never-conflated
columns: **attribution** (sources that verifiably attribute the claim to the
book, each with a greppable locator — gate A1b) and **adjudication** (the
data/literature that decide the claim). A row's book-anchor is live only with
≥2 verified attribution sources; rows that cannot be double-sourced are
published as `not-checkable (attribution)` with the data story still computed.

**Gate A1b (run-start, this session):** all 37 pre-registered §I.1b locators
re-verified at their expected counts against the staged files (raw `grep -F` on
the Schwartz HTML; `pdftotext … | tr -s | grep -F` on the PDFs) — zero misses,
so no source was dropped. All 13 staged data files matched their PROVENANCE
sha256. See `gates.json` for the full A1/A1b/A2/A3 log.

## Prior-art disclosures

**Williams et al. 1987 (not read).** Williams, Cutler, Williams & Haslam (1987,
Economy & Society 16(3)) audited these claims at publication; it is paywalled
and was not read; our verdicts are independent of it and must be compared
against it before external publication. (Gate A3 confirmed no `williams1987`
staged, so the H2 restoration events for C4 and D1 did **not** fire.)

**Schwartz 2024 (staged), engaged as prior art** in every family where he
issued a judgment: B3 (rigidity / endogenous-decay diagnosis), D1
(HIT-with-outsourcing-twist), P1 (the global-Keynesianism fork), P3 ("narrow
slice of industrial output"). Our data-grounded rows are positioned as the
check on his narrative ones.

## Verdict tally (no pooled score)

Of **9 checkable claims and 3 gradeable predictions**: **6 supported, 1
partially supported, 0 contradicted, 5 not-checkable**; every book-value anchor
is provisional pending a lawful copy (H1); the globalization prediction (P2) is
scored separately in study 002.

| Row | Verdict | Attribution |
|---|---|---|
| B1 durable saturation | supported | double-sourced |
| B2 demand-regime break 1971–79 | supported (timeline only) | double-sourced |
| B3 productivity internally exhausted | supported | double-sourced (scoped) |
| C1 Emilia-Romagna relative income | supported | double-sourced (scoped) |
| C4 specialty steel / minimills | not-checkable (attribution) | demoted (pre-declared) |
| C5 programmable tech → small batches | supported (implication) | double-sourced |
| C2/C3 district-sector / BW–Japan | not-checkable (data)+(attribution) | demoted (single-source) |
| D1 plant-size reversal | not-checkable (attribution) | demoted (single-source) |
| D2 deskilling / re-skilling | not-checkable ([LIT]) | not graded |
| P1 mass production won't recover | supported | double-sourced |
| P3 flexible spec. could dominate | partially supported (modal) | double-sourced |
| P4 exits are a political choice | not-checkable ([INTERP]) | not graded |
| P2 Exit 1 / globalization | see study 002 | handed to 002 |

## Per-family results

### Family B — the crisis of mass production

- **B1 (supported).** Decision rule (per durable: pen(1973) ≥ 0.9·pen(1984)
  AND mean growth 1973→1984 ≤ 1.0 pp/yr; supported if ≥3/4 pass). All four
  pass: Automobile 82.0→87.0 (ratio .943, 0.46 pp/yr), Household refrigerator
  99.0→99.0 (1.000, 0.0), Washing machine 66.0→71.0 (.930, 0.46), TV 96.4→98.1
  (.983, 0.15, Census HS-42). `[PREVIEW-CALIBRATED: 1973 OWID/HS-42 values in
  view at spec time — Automobile 82.0 (.943), Household refrigerator 99.0
  (1.000), Washing machine 66.0 (.930), TV 96.4% HS-42 (.983 vs 98.1 in
  1984)]`. TV comes from Census HS-42 (OWID `Television` starts 1992; `Colour
  TV` was mid-diffusion in 1973) — source split disclosed.
- **B2 (supported, timeline only).** The documentary macro record — end of
  Bretton Woods (Aug 1971 / Smithsonian 1971 / float 1973), the 1973 and 1979
  oil shocks, 1970s stagflation — falls inside the asserted 1971–79 window. The
  **causal** weight (that this removed mass production's prop) is [LIT] and
  ungraded (R3).
- **B3 (supported).** US productivity growth slowed after 1973 on both FRED
  measures: labor productivity (OPHNFB) mean annual growth **2.58% (1950–73) →
  1.58% (1974–84)**; TFP (MFPNFBS) **1.71% → 0.58%** — the classic post-1973
  slowdown, in both series. Scope: the attribution sources support the
  internal-exhaustion *diagnosis*; the productivity operationalization is the
  briefing's, adjudicated by FRED. **Deviation:** the named series OPHMFG
  begins in 1987 and cannot reach the pre-1973 window; the canonical long
  successor OPHNFB (nonfarm business, 1947+) was used per the "or successor"
  clause, logged in `fetch_log.json`. These series are economy/nonfarm-business,
  not manufacturing-only.

### Family C — flexible specialization and the districts

- **C1 (supported).** Rinaldi (staged): Emilia-Romagna sat **7th** among
  Italian regions by per-capita income in 1951; the gap to the Italian mean
  rose to **+29% by 1980**, and the region reached **2nd place (+25%) by 1995**
  — a sharp rise through the 1970s crisis, magnitude within a defensible reading
  of "+29% by 1980." Modern Eurostat endpoint **reported, not graded**: E-R
  per-capita income (PPS) was +23.0% above Italy in 2000 and +19.5% in 2024
  (116.8% of EU27). Per R2 the row grades the *trajectory* and refuses the
  contested rank-in-1984 formulation pending H1.
- **C4 (not-checkable (attribution)).** Zero verified attribution sources in
  the corpus (the staged Schwartz essay has no steel content; the previously
  cited "~8%→~70%" Schwartz anchor was a false citation and is withdrawn), and
  no restoration event fired. **Data trajectory (not a graded book claim):**
  2024 worldsteel US EAF share **71.8%** (US is majority electric-arc /
  minimill) vs China 10.2% EAF (89.8% BOF), Italy 89.3% EAF, EU27 44.4%. The
  **1970s–84 US EAF level is not-checkable (data)**: USGS DS140 is blocked (bot
  filter), no staged OA source quotes the Minerals-Yearbook value, so the
  historical branch has no supply route and the full trajectory cannot be
  established from staged inputs (per the fetch policy — missing input is
  reported, never filled from memory).
- **C5 (supported, implication only).** Graded on the observable implication —
  the D1 size shift in machinery-intensive sectors. In BDS manufacturing (NAICS
  31-33, which includes machinery) mean establishment size fell 58.7→45.8 and
  the small-establishment (<100) employment share rose 27.7%→32.5%, 1978–2023.
  The scale-economics *mechanism* (programmable tech *causes* the shift) stays
  [LIT] (R3).
- **C2/C3 (not-checkable (data) + (attribution)).** Single attribution source
  (Berger). The declared Eurostat in-run branch delivered Baden-Württemberg
  (DE1) modern GDP: BW per-capita (PPS) was 144.0% of EU27 in 2000 and 130.8%
  in 2024 (above EU, mildly converging) — reported as a data story. But
  `nama_10r_2gdp` starts in 2000 (no 1980s backcast), and the Italian district
  **sector** series (Prato/Carpi/Sassuolo/Bologna exports) was not staged this
  tick, so the historical "same phenomenon" test stays not-checkable; it is a
  named next-tick item. The C3 "same phenomenon" framing is [INTERP] and never
  graded.

### Family D — plant size and the labor process

- **D1 (verdict cell not-checkable (attribution); data story "qualified").**
  Single attribution source (Schwartz, outsourcing/vertical-disintegration;
  Carlsson's verified locator attributes only the general transition thesis,
  scoped insufficient for the D1-specific wording). **Data story is the heart of
  D1 and is fully reported:** the plant-size reversal is a **manufacturing
  phenomenon, not economy-wide**. In manufacturing, small-establishment
  employment share rose **27.69%→32.53%** and mean establishment size fell
  **58.74→45.82** (1978→2023) — the reversal the claim predicts. Economy-wide
  the opposite holds (small share 55.62%→52.66% down, mean size 16.23→18.34 up),
  driven by large service establishments. Because the two levels disagree, the
  pre-declared rule returns "qualified." This matches **Schwartz's
  HIT-with-outsourcing-twist** judgment (manufacturers shed scale via
  outsourcing/demerger rather than via a craft revival). The 1963–77 segment
  (Carlsson 1988: metalworking average establishment size −12.3% 1972–82) is
  literature-quoted and feeds the figure, not the verdict.
- **D2 (not-checkable ([LIT])).** The deskilling/re-skilling claim is a
  labor-process debate, pre-declared out of data-grading scope. One paragraph:
  the Braverman-vs-flexible-specialization literature (Hirst & Zeitlin 1991,
  recorded not read; Schwartz 2024) remains contested and is not adjudicable on
  public aggregate series.

### Predictions (P-row block)

**The book posed Exit 1 and Exit 2 as politically contingent possibilities,
not forecasts; neither exit's non-realization is, by itself, a failed
prediction.**

- **P1 (supported).** Old-national-form mass production did not recover absent
  new institutions. Manufacturing value-added share fell in all three
  economies over each series' true WDI coverage: US 16.1%→10.5%
  (**1997→2021**), Germany 24.6%→18.9% (**1991→2023**), Japan 23.4%→19.5%
  (**1994→2023**) (WDI NV.IND.MANF.ZS). US manufacturing employment share fell
  19.0%→8.0% (1984→2025, FRED MANEMP/PAYEMS), far below the pre-1973 ~25%. No
  recovery. **Vintage seam (PS-PROV-1 correction):** these VA-share figures were
  previously labeled "1984→2023"; they are nearest-year substitutions. The WDI
  manufacturing-VA series (NV.IND.MANF.ZS) starts too late for a 1984 baseline
  — its first non-missing year is USA 1997, DEU 1991, JPN 1994 — so no "1984"
  value exists and the labels are corrected to the TRUE years (USA also ends
  2021, the last non-missing year, not 2023). The employment leg (FRED, genuine
  1984→2025) is the vintage-clean series and already drives the verdict; the
  verdict direction (no recovery) is **unaffected**.
  *Hindsight context (not part of the verdict):* the book could not have
  anticipated China's post-2001 manufacturing surge (Schwartz omissions list).
  *Seam:* DE/JP employment-share series were not staged (US only via FRED); VA
  shares cover all three.
- **P3 (partially supported — modal).** Worded with "could"/"potential," so
  graded only on its factual components per PS-A3. Factual component holds:
  Emilia-Romagna persisted as a strong regional model (+19.5% above Italy,
  130.8% of EU27 in 2024 — it did not collapse) and the BDS manufacturing
  small-plant reversal is present. But flexible specialization did **not**
  become the dominant regime — **the possibility was not realized** (Schwartz's
  "narrow slice of industrial output"; Italy's post-2000 stagnation). Per the
  modal rule this is reported, never scored `contradicted`.
- **P4 (not-checkable ([INTERP])).** The "exits are a political, not
  technological, choice" thesis is interpretive/normative and not
  data-decidable as worded. A weaker Varieties-of-Capitalism-adjacent reading
  exists (Hall & Soskice 2001); it is noted, not graded.
- **P2 (handed to study 002).** Appears here only as the hand-off row, carrying
  the PS-B4 mapping note verbatim: *"002's H-A is the OPERATIONALIZED
  hypothesis; its hub-concentration and profit-structure components are
  Kaplinsky's/Schwartz's modernizations, not Exit 1 as provisionally anchored —
  no 002 verdict reads as 'the book predicted/failed to predict China'."*

## Attribution register as published (A1b)

- **Double-sourced (book-anchor live, provisional):** B1 (BHEN+BERG+HAMP),
  B2 (BHEN+SCHW), B3 (SCHW+HAMP, scoped), C1 (SCHW+RIN+STUR, scoped),
  C5 (BHEN+BERG), P1 (SCHW+BERG), P3 (SCHW+BERG).
- **Demoted to not-checkable (attribution):** C4 (zero sources), D1 (SCHW only;
  Carlsson general-thesis insufficient), C2/C3 (Berger only).
- **Not graded (attribution not required):** D2 ([LIT]), P4 ([INTERP]).
- All 37 locator checks passed at expected count (full log in `gates.json`
  → `A1b_attribution_locators`). A pre-registered H1 branch (not run here) will
  later replace anchors with the book's own wording + page cites and re-issue
  any verdict whose grade could change.

## Out of grading scope (families A and F — one paragraph each)

**Family F (engaged, not graded).** The book's technology-choice indeterminacy,
its first-divide counterfactual as a general claim, its normative frame, and
its two-divides periodization are interpretive/theoretical (R3). They are the
intellectual core of the book but are not propositions decidable against public
series; we take no verdict on whether the nineteenth-century "divide" could
have gone the craft way, or on whether the exits are ultimately political.

**Family A (engaged, not graded).** The book's historiographical [LIT] claims —
its reading of nineteenth-century craft production, the Lyon silk and Sheffield
cutlery cases, the account of how mass production won — are historical
scholarship we do not adjudicate here; the contemporary audit of that record is
exactly Williams et al. 1987 (not read; see disclosure above).

## Limitations

- **Provisional anchors (H1).** Every book-value anchor is provisional pending
  a lawful machine-readable copy; no "the book says p.Y" claim is made. Rows
  that could be neither double-sourced nor H1-verified (C4, D1, C2/C3) are
  published as not-checkable (attribution), never graded from a single tertiary
  quote and never silently dropped.
- **OWID TV gap.** OWID's `Television` entity begins in 1992 and `Colour TV`
  was mid-diffusion in 1973, so B1's TV series comes from Census HS-42 — a
  deliberate, disclosed source split.
- **C4 historical EAF** has no staged supply route (USGS DS140 blocked; no OA
  Minerals-Yearbook quote), so only the 2024 endpoint is computable.
- **B3** uses nonfarm-business (not manufacturing-only) productivity series
  because the manufacturing-specific FRED series does not reach the pre-1973
  window.
- **P1** lacks staged DE/JP employment-share series; VA shares substitute for
  the employment leg in those two economies.
