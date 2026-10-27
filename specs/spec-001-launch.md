<!-- LAUNCH FILE: study 001-claims-and-predictions ONLY. Study 002 is out of scope for this session. -->

<!-- SPEC PAIR for the Phase 2b judge. At launch each part is copied to its own --instruction-file. This work is a BOOK under a GO-WITH-SCOPE verdict: there is NO Phase 1 replication and NO replication score, ever. -->

# Extension specs: Piore & Sabel (1984), *The Second Industrial Divide* (Basic Books)

**Status:** DRAFT for the Phase 2b judge, prepared 2026-10-27 by the Phase 2a
recency-research agent. Every data source verified live 2026-10-27
(`recency-research.md`; hashes in `extension-assets/PROVENANCE.md`).

**What this pair is, in one sentence.** Study 001 grades the book's checkable
empirical claims (families B, C, D) and three of its four closing predictions
(P1, P3, P4) against public statistics and the documented secondary record,
with per-claim verdicts and no pooled score; Study 002 answers the reader's
question — is there any evidence of globalization as a new mass-production
system? — by scoring the book's own Exit-1 prediction (P2) as a three-
hypothesis evidence-weighing contest (H-A new mass production / H-B flexible
specialization at global scale / H-C neither: the second unbundling) on
pre-declared, falsifiable signatures, where "the book's dichotomy itself
fails" is a first-class pre-declared outcome.

**Reader question (a reader, through the site, anonymous — no submitter
identity appears in any output):** *is there any evidence of globalization as
a new mass-production system?* This is the book's Exit 1 (prediction P2)
asked 40 years on.

**Shared binding constraints (both parts):**

- **No replication score.** Outputs are scorecards with per-row verdicts. Any
  text computing or implying a pooled numeric "replication score" is a
  violation (R5; page presentation is human gate H4). **Machine surfaces are
  bound too (PS-C2):** `result_card.json` and `followup_summary.json` contain
  no numeric score and no score-like aggregate — the headline's verdict
  counts are structured tallies and are allowed. If the followup template or
  card schema expects a score field, set it to `null` /
  `"not applicable (book; GO-WITH-SCOPE)"` and REPORT the schema mismatch in
  `followup_summary.json` for a pipeline-level fix per the uniform-evaluator
  rule — never hand-work around it inside the study. Phase 3 synthesis
  inherits this ban via H4; it is carried on the publication checklist
  (ORCH-4).
- **Preview-calibration labels (PS-C1).** Three constants in this pair rest
  on previewed staged values and one was written with the staged files in
  hand. The labels are mandatory on EVERY surface where the constant
  appears — the affected evidence-grid cells, `findings.md`, `gates.json`,
  and the result card:
  (a) the against-H-C flat-SoP condition carries
  `[PREVIEW-KNOWN: WLD SoP2 export share 19.45–24.92%, flat 1988–2023,
  stated at spec time]`;
  (b) the S1 geography-split condition carries
  `[PREVIEW-KNOWN: China ≈91.6% BOF / US majority-EAF, worldsteel 2025,
  stated at spec time]`;
  (c) the 2011 era boundary carries
  `[SOURCE-DERIVED: WTO GVC Report 2025 plateau finding]` — it was set BY a
  previewed source, and the words "pre-registered" and "validated" are
  BANNED for these three constants;
  (d) B1's saturation rule (§I.1b) is born
  `[PREVIEW-CALIBRATED]` with the relevant staged values stated beside it.
  Ruled not requiring labels (judge R-6): the ≥4 signature counts and
  reported magnitudes that gate nothing (CHN 27.9%, the steel shares).
- **H1 two-branch rule (BLOCKING for attribution; revised per PS-A1).** No
  lawful machine-readable copy of the book exists in the corpus by design.
  Every claim or prediction row is graded in its PROVISIONAL branch: worded
  per the Phase 0 briefing and tagged `book-anchor: PROVISIONAL-PENDING-H1`.
  Each row's sources are split into TWO columns that are never conflated:
  - `attribution_sources` — sources that verifiably ATTRIBUTE the claim to
    the book. A row's book-anchor is live only if ≥2 independent attribution
    sources are verified, each with a LOCATOR: an exact quoted phrase that
    occurs in the staged text (register in §I.1b; every locator there was
    verified by grep against the staged file before being written in).
  - `adjudication_sources` — data/literature that ADJUDICATE the claim
    (Minerals Yearbook values, the Davis-Haltiwanger-line BDS literature,
    Rinaldi's income series, Carlsson 1988's establishment-size tables,
    FRED/Census/Eurostat/worldsteel data). These NEVER count toward the
    attribution requirement.
  Locator verification is mechanical (gate A1b, §I.4): for the staged HTML,
  `grep -F '<locator>' <file>`; for staged PDFs,
  `pdftotext <file> - | tr -s '[:space:]' ' ' | grep -F '<locator>'`. (Note:
  the staged Schwartz HTML encodes "P&S" as "P&amp;S", so locators are
  chosen ampersand-free.) At run start the agent re-runs every locator check
  and, on any miss, drops that source; any row left with <2 verified
  attribution sources is demoted to `not-checkable (attribution)` — its data
  story is still computed and reported, but no book citation from an
  unverified anchor may reach findings or the card. No output may assert
  "the book says X at p.Y". A pre-registered H1 branch (not run in these
  studies) later replaces anchors with the book's own wording + page cites
  and re-issues any verdict whose grade could change; rows that can neither
  be double-sourced nor H1-verified are published as "not-checkable
  (attribution)", never graded from a single tertiary quote and never
  silently dropped. Rows pre-declared single-sourced at spec time (§I.1b:
  C4, D1, C2/C3) launch with book-anchor already demoted; the named
  restoration events (H2 Williams 1987 staged pre-launch, or a logged
  fair-use Google-Books-snippet verification executed by the orchestrator
  pre-launch) are the only ways back.
- **Copyright.** Never fetch, OCR, or re-host any part of the book's text.
  Quotes already present in staged OA literature may be cited at fair-use
  length with attribution to the quoting source. The two INTERNAL ONLY PDFs
  (GHS 2005 FAO mirror; Sturgeon 2008 ISA WP) are read internally and cited
  by DOI/published chapter only; no copy, no excerpt beyond fair use, never
  into `results/` assets destined for the public repo.
- **Interpretive boundary (R3).** Family F (technology-choice indeterminacy,
  the first-divide counterfactual as a general claim, the normative frame,
  the two-divides periodization) and family A (historiographical [LIT]
  claims) receive NO verdicts. They are engaged in prose, labelled
  "out of grading scope", in at most one paragraph each.
- **Uniform-evaluator rule.** Any grading-artifact problem found while
  running is reported for a pipeline-level fix; nothing is special-cased for
  this book inside the studies.
- **Fetch policy.** Staged data only, except the declared in-run fetch
  branches listed per study (§I.3 / §II.4), each keyless, each logged with
  query string + timestamp in `results/fetch_log.json`. No logins, no
  registration walls (UNIDO INDSTAT stays excluded unless the orchestrator
  marks H3 cleared and stages the extract), no shadow libraries, no
  circumvention of bot blocks (USGS stays blocked unless a staged copy
  appears). If an input is missing, stop that block and report; never
  substitute from memory.
- **FOREGROUND RULE.** Every command runs in the foreground; a single shell
  call stays under ~8 minutes (hard cap 10). Never background a job (`&`,
  `nohup`, background-task tools) and never end the turn "to wait".
- **Continuation rule.** Every block writes its outputs to `results/` and a
  `workspace/checkpoints/<block>.done` marker as soon as it finishes, and
  updates `followup_summary.json` (with a `remaining` list). If the session
  ends before `result_card.json` completes, the orchestrator relaunches the
  same instruction as `NNN-<name>-cont`; the continuation reuses
  `workspace/` and `results/`, skips `.done` blocks, and finishes `remaining`.
  Every pre-declared block runs; nothing is dropped for time or budget.

---


# PART I: Follow-up study 001, claims-and-predictions

**LAUNCH LINE:** `REPLICATION: NOT APPLICABLE — BOOK, GO-WITH-SCOPE (Phase 0);
THIS STUDY IS THE VERIFICATION LAYER` (fixed; see ORCH-1)

**Launcher settings:** the study launcher ran as `followup <run_dir> --instruction-file
<part-I.md> --name claims-and-predictions --timeout 14400`. The timeout is
crash protection only; measured Phase 2a probes put every block in
seconds-to-minutes on one core (CSV/JSON parsing + small-series assembly;
expect well under 1 core-hour). `<run_dir>` is the bespoke book scaffold
(ORCH-1), since no Phase 1 replication run exists.

## I.0 What this study is (binding framing)

An inventory-with-verdicts: the book's checkable empirical claims (families
B, C, D) reconstructed from public statistics for the period the book
describes (roughly 1950-1984), each graded with one of four verdict words
(§I.2); plus the 40-years-later predictions scorecard for P1, P3, P4
(extending the same series 1984-2025). P2 is OUT OF SCOPE here — it is study
002 entire. Prior art is engaged by name: Williams et al. 1987 is the
contemporary audit of exactly these claims (paywalled; if the orchestrator
stages it under H2 before launch, Block D engages its chapter-level verdicts
row by row; otherwise findings.md states, verbatim: "Williams, Cutler,
Williams & Haslam (1987, Economy & Society 16(3)) audited these claims at
publication; it is paywalled and was not read; our verdicts are independent
of it and must be compared against it before external publication" — and the
card carries the same disclosure). Schwartz 2024 (staged) is engaged in
every family where it issued a judgment (B3, D1, P1, P3), named as prior art,
with our data-grounded rows positioned as the check on his narrative ones.

## I.1 The claim rows (grading targets, with provisional anchors)

Legend: every row carries `book-anchor: PROVISIONAL-PENDING-H1`. Wording is
the Phase 0 briefing's (§4), which is the binding claim text for the
provisional branch. Per PS-A1 the old single anchor column is SPLIT:
`Attribution` names only sources that verifiably attribute the claim to the
book (locators + status in §I.1b, the binding register); `Adjudication`
names the data/literature that decide the claim and NEVER counts toward
attribution. `scorecard.csv` carries both columns
(`attribution_sources`, `adjudication_sources`) plus
`attribution_status` (`double-sourced` / `demoted: not-checkable
(attribution)`).

| ID | Claim (provisional wording) | Adjudication (data leg(s)) | Attribution (verified; §I.1b) |
|---|---|---|---|
| B1 | Core consumer-durable markets in advanced countries were saturated by the early 1970s | OWID US tech-adoption CSV, entities named exactly: `Automobile`, `Household refrigerator`, `Washing machine` (the duplicate entities `Refrigerator`/`Washer` are shorter series and are NOT used); TV from Census Statistical Abstract HS-42 (staged, `extension-assets/census-statab/`), since OWID `Television` starts 1992 and `Colour TV` (1966-2005) was still mid-diffusion in 1973 — the entity-and-source choice is disclosed in the row and on the card | DOUBLE-SOURCED: Bhengu 2001 (quotes the book's p.184 saturation passage); Berger 2013; Hampson 1991 |
| B2 | The international demand-stabilization regime broke 1971-79, removing mass production's macro prop | Documentary record (no new data needed): Bretton Woods end, oil shocks, stagflation — graded only as "the record matches the asserted timeline"; the CAUSAL weight is out of scope ([LIT]) | DOUBLE-SOURCED: Bhengu 2001 (quotes the book's p.176 macro-breakdown passage); Schwartz 2024. (Baldwin 2006 is ADJUDICATION-side history only — it never mentions the book) |
| B3 | Mass-production productivity growth had internally exhausted by the 1970s | FRED/BLS declared in-run fetch (I.3): US labor productivity + TFP growth, 1950-1984 | DOUBLE-SOURCED (scoped): Schwartz 2024 (rigidity/endogenous-decay attribution); Hampson 1991 (quotes the book's internal-limits diagnosis, 1984:3-4). Scope note: both attribute the internal-exhaustion DIAGNOSIS; the productivity-growth operationalization is the briefing's and is adjudicated by FRED. (Kaplinsky 2023 is removed: it never mentions the book) |
| C1 | Emilia-Romagna rose sharply in relative income through the 1970s crisis on small-firm districts | Staged Rinaldi WP + ISTAT Storie di dati (historical series: 7th in 1951, +29% vs national mean by 1980, 2nd by 1995); Eurostat regional GDP (modern endpoint) — ALL adjudication-side | DOUBLE-SOURCED (scoped): Schwartz 2024 ("ideal model" passage); Rinaldi WP (names P&S 1984 among the scholars of the E-R small-firm model); Sturgeon 2008 (districts-example attribution). Scope note: these attribute "E-R's small-firm districts were the book's showcase/ideal model"; the income TRAJECTORY is adjudicated by Rinaldi/ISTAT. NOTE (binding, R2, unchanged): the famous "rose to second place" book sentence circulates in incompatible tertiary versions — the row grades the TRAJECTORY and explicitly refuses the rank-in-1984 formulation pending H1 |
| C4 | US specialty steel/minimills thrived while integrated Big Steel collapsed | worldsteel 2025 (staged; modern EAF shares); historical US EAF share via the provenance-split rule (I.3); Minerals-Yearbook-quoted values are ADJUDICATION, not attribution | PRE-DECLARED DOWNGRADE: zero verified attribution sources in the staged corpus (the staged Schwartz essay contains NO steel/minimill content — the previously cited "~8%→~70%" Schwartz anchor was a false citation and is withdrawn). Book-anchor = `not-checkable (attribution)` at launch; the DATA STORY is still computed and reported (the EAF-share trajectory, branch-labelled), phrased with no book attribution. Restoration events: H2 (Williams et al. 1987, whose audit covers the steel showcase) staged pre-launch, or a logged fair-use Google-Books-snippet verification pre-launch |
| C5 | Programmable (NC/CNC) technology erodes scale economies, making small batches economic | Graded on its OBSERVABLE implication only: the D1 size shift in machinery-intensive sectors (BDS sector rows); the scale-economics mechanism itself is [LIT] | DOUBLE-SOURCED: Bhengu 2001 (quotes the book's pp.258/261 computer-technology passages); Berger 2013 (programmable-assembly attribution). (Kaplinsky 2023 removed: no book mention, no flexibilization content) |
| D1 | The long rise of plant size reversed: average establishment size falling, small-establishment employment share rising from the 1970s | BDS 2023 (staged, 1978-2023, economy + manufacturing); Eurostat SBS (staged, 2005-2020 + 2021+); 1963-1977 segment from literature-quoted Census of Manufactures values, now NAMED and double-sourced: Carlsson 1988 (staged, IUI WP 203 size tables incl. metalworking −12.3% 1972-82) + the Davis & Haltiwanger-line BDS literature (named in findings) | PRE-DECLARED DOWNGRADE: one verified attribution source (Schwartz 2024, outsourcing/vertical-disintegration passages). Carlsson 1988 attributes only the general transition thesis (locator in §I.1b) — recorded, but scoped as insufficient for the D1-specific wording. Book-anchor = `not-checkable (attribution)` at launch; the data story (the heart of D1) is fully graded as the reconstructed record, phrased with no book attribution; Schwartz's HIT-with-outsourcing-twist judgment is engaged as prior art in prose. Restoration events: as C4 (Williams 1987 audits the plant-size chapter) |
| D2 | Mass-production work deskills while flexible specialization re-skills | NOT GRADED as data: pre-declared `not-checkable (labor-process debate; [LIT])` row with one literature paragraph | ATTRIBUTION NOT REQUIRED (row never graded); sources recorded: Hirst & Zeitlin 1991 (recorded, not read); Schwartz 2024 |
| C2, C3 | District-sector growth (Prato, Carpi, Sassuolo, Bologna) & Baden-Württemberg/Japan parallels | DEFERRED: graded `not-checkable (data: sector series not staged this tick)` unless the declared Eurostat in-run branch (I.3) yields the BW regional series; the C3 "same phenomenon" framing is [INTERP] and never graded | PRE-DECLARED: one verified attribution source (Berger 2013: "the German and Japanese middle-firm sectors" passage). Even if the Eurostat branch delivers data, the book-anchor stays `not-checkable (attribution)` this tick (single-sourced); the data story is reported. Brusco 1982 (recorded) and Herrigel (named) are adjudication-side context |

### I.1b Verified attribution-locator register (binding; gate A1b greps exactly these)

Every locator below was verified against the staged file before being
written here, with the canonical commands of the H1 rule (raw `grep -F` for
the HTML; `pdftotext <file> - | tr -s '[:space:]' ' ' | grep -F` for PDFs).
Each occurs exactly once in its file, except where an expected count is stated in the row. Staged files:
SCHW = `literature/retrospectives/schwartz2024_third_divide.html`;
BERG = `literature/quoting-sources/berger2013_toward_third_industrial_divide.pdf`;
BHEN = `literature/quoting-sources/bhengu2001_uct_thesis_flexible_specialisation.pdf`;
HAMP = `literature/quoting-sources/hampson1991_postfordism_regulation_school_jape28.pdf`;
CARL = `literature/quoting-sources/carlsson1988_iui_wp203_manufacturing_technology_plant_size.pdf`;
RIN = `literature/districts/rinaldi-emilia-romagna-income-history.pdf`;
STUR = `literature/globalization-gvc/sturgeon2008-commodity-to-value-chains-isa-wp.pdf`.

| Row | Source | Locator (exact quoted phrase, greppable) | Decision statistic for the supported/partial boundary (PS-A4) |
|---|---|---|---|
| B1 | BHEN | `by 1979 there was one car for every` AND `households had television sets by 1970` AND `(Piore & Sabel, 1984: 184)` | Saturation rule, per durable d in {Automobile, Household refrigerator, Washing machine, TV(HS-42)}: d counts "saturated by the early 1970s" if penetration(1973) ≥ 0.9 × penetration(1984) AND mean annual growth 1973→1984 ≤ 1.0 pp/yr. Verdict: `supported` if ≥3 of 4 durables pass and none fails the growth guard; `partially supported` if exactly 2 pass; `contradicted` if ≤1 passes. `[PREVIEW-CALIBRATED: staged 1973 values in view when written — Automobile 82.0 (ratio .943), Household refrigerator 99.0 (1.000), Washing machine 66.0 (.930), TV 96.4% of households per HS-42 (ratio .983 vs 98.1 in 1984)]`. The per-durable table and the TV-source note ship in the row and on the card |
| B1 | BERG | `saturation of mass consumer-good markets` | (same rule) |
| B1 | HAMP | `According to Piore and Sabel, domestic markets for mass produced goods became saturated` | (same rule) |
| B2 | BHEN | `Given the rigid wages and prices central to the system of macroeconomic regulation` AND `(Piore & Sabel, 1984: 176)` | Timeline match only: the documentary record (Bretton Woods end 1971-73, oil shocks 1973/79, stagflation) matches the claim's 1971-79 window → `supported`; partial overlap → `partially supported`. No magnitude; causal weight [LIT] |
| B2 | SCHW | `overly rigid production structure` AND `presented a multitude of shocks` | (same) |
| B3 | SCHW | `overly rigid production structure` | Post-1973 vs 1950-73 mean growth of the two named FRED series (labor productivity OPHMFG-or-successor; TFP MFPNFBS-or-successor): slowdown present in BOTH → `supported`; in one → `partially supported`; in neither → `contradicted`. No magnitude bar — direction + timing only |
| B3 | HAMP | `the limits of the model of industrial development that is founded on mass production` | (same) |
| C1 | SCHW | `ideal model for a better future` | Direction AND approximate magnitude vs the Rinaldi values (7th in 1951 → +29% vs national mean by 1980): reconstructed series rises through the 1970s with magnitude within a defensible reading of "+29% by 1980" → `supported`; rises but magnitude/timing qualified → `partially supported`; flat/falling → `contradicted`. The modern Eurostat endpoint is REPORTED, never graded into the historical claim |
| C1 | RIN | `Piore e Sabel 1984` (in the scholars-of-the-Emilian-model sentence) | (same) |
| C1 | STUR | `provided by Piore and Sabel (1984)` | (same) |
| C4 | — | NONE VERIFIED (pre-declared downgrade, see I.1 row) | The existing two-branch provenance-split rule (I.3) governs the DATA STORY: branch named in the row; `supported`-equivalent language for the data story available only if the 1970s level AND the direction to the mid-80s agree across the two named quotes. The verdict cell itself is `not-checkable (attribution)` unless a restoration event fires |
| C5 | BHEN | `the application of computers to industry favours flexible systems` AND `(Piore & Sabel, 1984: 258)`; also `programmable equipment is used just as automatic machinery was used in the past` AND `(Piore & Sabel, 1984: 261)` [expected hits: 2 — the thesis quotes the book's p.261 twice; both occurrences are verbatim book quotes] | Graded on the observable implication only: the D1 size shift present in machinery-intensive BDS sectors → `supported`-side wording for the implication; mechanism stays [LIT] per the row |
| C5 | BERG | `computer-aided manufacturing (programmable assembly) might make it efficient and profitable to adjust equipment` | (same) |
| D1 | SCHW | `shrink themselves via outsourcing and demerger` AND `drove the vertical disintegration that` | Sign of the small-establishment (<100 emp) employment-share change AND of mean establishment size, 1978→2023, economy AND manufacturing (BDS): share up AND mean size down in both → data story "reversal confirmed"; mixed → qualified; both opposite → "reversal not found". The 1963-1977 literature segment (Carlsson 1988 + Davis-Haltiwanger line) feeds the FIGURE, not the verdict, unless double-sourced per the data rule. Verdict cell: `not-checkable (attribution)` at launch (see I.1 row) |
| D1 | CARL | `have argued that the United States is currently in a period of transition from mass production to` (general-thesis attribution — recorded, insufficient alone for the D1 wording); adjudication locator: `average establishment size declined by 12.3` | (same) |
| C2/C3 | BERG | `the Italian and French industrial districts and the German and Japanese middle-firm sectors` | Deferred rows; no statistic unless the Eurostat branch delivers, and then data-story-only (attribution stays demoted this tick) |
| P1 | SCHW | `improbable expansion of mass production and thus Keynesian policy of demand management to the global level` | Direction of manufacturing employment and VA shares, 1984→2025, US/DE/JP (WDI + FRED): shares do not recover toward pre-1973 levels absent new institutions → `supported`; mixed across the three economies → `partially supported`; sustained recovery → `contradicted`. Direction + timing only, no magnitude |
| P1 | BERG | `One family of solutions would be a global Keynesianism` AND `multinational Keynesian order` | (same) |
| P2 | SCHW | `They saw only two paths out of the problems animating the debate` AND the P1 fork locator above | HANDED TO 002 (whose §II.0b inherits this register's P2 locators) |
| P2 | BERG | `apportion the expansion of productive capacity among the advanced industrial countries` | (handed to 002) |
| P2 | BHEN | `They moved into mass-produced consumer durables` AND `(Piore & Sabel, 1984: 188)` (the developing-world component) | (handed to 002) |
| P3 | SCHW | `The other was a transformation of the industrial base in the direction of flexible specialization` AND `narrow slice of industrial output`; also `a potential second divide, for a return to flexible specialization` | Modal claim — graded per the I.2 modal rule on its factual components: districts persisted/grew as a model (E-R series, D1 series) vs collapsed outright; dominance non-realization is REPORTED with the fixed phrase, never graded `contradicted` on its own |
| P3 | BERG | `nourish and strengthen flexible specialization and craft production` | (same) |
| P4 | HAMP | `a political choice between the technology of` (recorded; row never graded) | `not-checkable ([INTERP] as stated)` — unchanged |
| P4 | SCHW | `utter indeterminacy of any given divide` (recorded; row never graded) | (same) |

Standing rule: if 2b re-review scopes any attribution above as insufficient
for its row's specific wording, that row follows the single-source downgrade
path (book-anchor `not-checkable (attribution)`, data story still graded) —
no re-negotiation inside the run.

Predictions scorecard rows (same split-anchor discipline — attribution
locators and per-row statistics live in §I.1b; graded AS WRITTEN per the
provisional wording, hindsight-bias + modal rules §I.2):

| ID | Prediction | Data leg(s) |
|---|---|---|
| P1 | Old-national-form mass production will not recover absent new institutions | WDI manufacturing VA shares + declared FRED fetch (US/DE/JP manufacturing employment share 1984-2025). Attribution: DOUBLE-SOURCED (§I.1b: Schwartz fork + Berger global-Keynesianism locators) |
| P3 | Flexible specialization could become the dominant regime, districts the growth model | Eurostat E-R vs IT vs EU (staged, 2000-2024) + Rinaldi/ISTAT historical + D1 series; verdict engages Schwartz's "narrow slice" judgment and Italy's post-2000 stagnation. MODAL wording — graded per the §I.2 modal rule. Attribution: DOUBLE-SOURCED (§I.1b) |
| P4 | The exits are a political choice, not technologically determined | `not-checkable ([INTERP] as stated)` — one paragraph notes the weaker VoC-adjacent reading exists, cites Hall & Soskice, grades nothing |
| P2 | Exit 1: mass production rebuilt at global scale with multinational-Keynesian institutions | **HANDED TO 002** — this row appears in the scorecard with verdict cell "see study 002" and carries the PS-B4 mapping note verbatim: "002's H-A is the OPERATIONALIZED hypothesis; its hub-concentration and profit-structure components are Kaplinsky's/Schwartz's modernizations, not Exit 1 as provisionally anchored — no 002 verdict reads as 'the book predicted/failed to predict China'" |

## I.2 Pre-declared verdict vocabulary (per row; banned anywhere outside a
verdict row: "proves", "vindicated", "debunked", "replication score",
"the book is right/wrong" unqualified)

| Verdict | Condition |
|---|---|
| `supported` | the reconstructed public series matches the provisional claim's direction AND approximate magnitude where the claim states one. Where the claim wording carries NO magnitude, `supported` = direction + timing match, and the word "magnitude" is dropped from that row's test (PS-A4); every row's concrete decision statistic is pre-declared in §I.1b and is the only test applied |
| `partially supported` | direction matches; magnitude, timing, or mechanism qualified — the qualification named in the row |
| `contradicted` | the reconstructed series runs against the claim's direction, or a stated magnitude is off beyond any defensible reading — with the series shown |
| `not-checkable (attribution)` | the claim cannot be double-sourced and H1 has not cleared |
| `not-checkable (data)` | the required series is gated/blocked/not staged — the gate named |
| `not-checkable ([LIT]/[INTERP])` | pre-declared out-of-grading rows (B2-causal, C3-framing, C5-mechanism, D2, P4) |

Hindsight-bias rule (R6, binding): predictions are graded against the
provisional WORDING, not against later reconstructions of "what they really
meant"; each P row carries one sentence on what the book could not have known
(from the Schwartz omissions list), labelled as context, outside the verdict.

**Modal-prediction rule (PS-A3, binding).** Pre-declared modal vocabulary:
a prediction worded with "could", "might", "may", "opens the possibility",
or "potential" is a POSSIBILITY claim, not a forecast. Such claims (P3 is
the instance; the book's own P4 asserts the outcome is a political choice)
are graded ONLY on their factual components (for P3: did districts persist/
grow as a model? — decidable on the E-R and D1 series), and the modality is
reported with the fixed phrase **"the possibility was not realized"** —
never `contradicted` for non-realization alone. `contradicted` is reserved
for factual components that ran against the data (e.g., if districts had
collapsed outright even as a narrow slice). The fork-not-forecast sentence
ships verbatim in the P-row block of `results/findings.md`:
**"The book posed Exit 1 and Exit 2 as politically contingent
possibilities, not forecasts; neither exit's non-realization is, by
itself, a failed prediction."** Study 002's findings inherit this sentence
verbatim in their P2 verdict block (§II.5).

Threshold-sensitivity rule: any `supported`/`contradicted` verdict resting on
a single series point within obvious revision noise is downgraded to
`partially supported` with the sensitivity stated.

## I.3 Sources and the declared in-run fetch branches

Staged (verify `extension-assets/PROVENANCE.md` sha256 per file before use):
all eight legs of recency-research.md §3, PLUS (added at the 2b revision,
hashed in the PROVENANCE files): `extension-assets/census-statab/hs-42-
selected-communications-media-1920-2001.pdf` (US Census Statistical
Abstract historical table HS-42, public domain — B1's TV-penetration
series, covering 1950-2001 incl. 1973 = 96.4% of households) and the four
attribution/quoting sources under `literature/quoting-sources/` (Berger
2013, Hampson 1991, Bhengu 2001, Carlsson 1988 — provenance, licenses, and
INTERNAL ONLY flags in `package/PROVENANCE.md`), mirrored per ORCH-2.
Correction (PS-A2a): the WDI vehicles indicator `IS.VEH.NVEH.P3` is NOT in
the staged durables CSV — the API query returns no data rows (indicator
archived at source; re-verified 2026-10-27). No spec text may instruct an
agent to use a vehicles column; PROVENANCE has been corrected to match.

Declared in-run fetches (keyless, logged, each ≤ a few MB):
1. **FRED CSV endpoints** (`https://fred.stlouisfed.org/graph/fredgraph.csv?id=...`)
   for B3/P1: US manufacturing labor productivity (OPHMFG or successor),
   TFP (MFPNFBS/successor), manufacturing employment share (MANEMP/PAYEMS).
   If FRED is unreachable, B3/P1 rows degrade to `not-checkable (data)` —
   never hand-copied numbers.
2. **Eurostat API** (same dissemination endpoint as the staged pulls) for the
   C2/C3 upgrade branch: BW NUTS-1 (DE1) GDP series and, if available in
   `nama_10r_2gdp`, the 1980s backcast — if absent, C3 stays not-checkable.
3. **USGS DS140 xlsx ONLY IF a staged copy appears** under
   `shared-data/steel/` (human fetch; see ORCH-3). No in-run attempt against
   the blocked CDN.

Historical-EAF provenance-split rule (binding for C4): the verdict row states
which branch supplied the 1970-84 values — `primary (USGS DS140)` or
`literature-quoted (Minerals Yearbook via [named OA source] + Schwartz 2024)`
— and `supported` is available on either branch only if both the 1970s level
AND the direction to the mid-80s agree across the two named quotes.

## I.4 Blocks (checkpointed; any order after A)

- **A gates:** A1 sha256 integrity of every staged file vs PROVENANCE;
  **A1b attribution-locator verification (PS-A1d, run-start, BLOCKING for
  anchors):** re-run every §I.1b locator check with the canonical commands
  (raw `grep -F` on the Schwartz HTML; `pdftotext <file> - | tr -s
  '[:space:]' ' ' | grep -F` on PDFs); log every check (locator, file, hit
  count) in `gates.json`; on zero hits, or a hit count differing from the register's expected count (default 1), drop that source, and demote any row
  left with <2 verified attribution sources to `not-checkable
  (attribution)` — an unverifiable anchor must never reach findings or the
  card as a citation; A2 coverage sanity (BDS max year 2023; WITS
  1988-2023; Eurostat E-R 2000-2024; OWID entities `Automobile`,
  `Household refrigerator`, `Washing machine` non-empty through ≥1973; HS-42
  parseable with the 1973 TV row present); A3 the H2/H3/USGS staging check
  (does `shared-data/` carry williams1987, indstat, or ds140? — set branch
  flags accordingly, log them in `gates.json`; a williams1987 hit fires the
  C4/D1 attribution-restoration events of §I.1).
- **B claims:** B-family (B1, B2, B3), C-family (C1, C4, C5, C2/C3 branch),
  D-family (D1, D2) — each writes `results/claim_<id>.csv` (the reconstructed
  series) + a verdict row in `results/scorecard.csv` with columns: id,
  provisional_wording, verdict, decision_statistic (from §I.1b),
  one_line_basis, attribution_sources (verified locators only),
  attribution_status, adjudication_sources, book_anchor_status, data_story
  (for attribution-demoted rows), preview_labels, data_files, seams_notes.
- **C predictions:** P1, P3, P4 rows + the P2 hand-off row; over-time figures
  `fig_d1_plantsize.png` (1963-2023, the literature-quoted segment visually
  distinguished), `fig_c1_emilia.png` (relative income, Rinaldi/ISTAT
  historical + Eurostat modern, the splice labelled), `fig_b1_saturation.png`.
- **D findings + card:** `results/findings.md` with: METHOD paragraph (the
  GO-WITH-SCOPE framing verbatim: "this is a claims-verification scorecard
  for a book, not a replication"); the Williams-1987 disclosure (I.0); the
  Schwartz engagements; per-family results; the fork-not-forecast sentence
  verbatim in the P-row block (§I.2 modal rule); the attribution register
  as published (which rows graded double-sourced, which demoted, with the
  A1b log referenced); the F/A out-of-scope paragraph; limitations (anchor
  table + the OWID TV gap note). Card per §I.5.

## I.5 Deliverables

`report.md`, `followup_summary.json`, `result_card.json` (per the
followup-studies handoff §5), `results/scorecard.csv`,
`results/claim_*.csv`, `results/findings.md`, `results/fetch_log.json`,
`gates.json`, 3 figures.

Result card (NO pooled score; at most 5 metrics, each a scorecard fact):
- `headline` (fixed template): "Of [n] checkable claims and 3 gradeable
  predictions, [a] supported, [b] partially supported, [c] contradicted,
  [d] not-checkable; every book-value anchor provisional pending a lawful
  copy (H1); the globalization prediction (P2) is scored separately in 002."
- M1: D1 small-establishment employment share, 1978 vs 2023 (BDS), with the
  Schwartz "outsourcing twist" sentence.
- M2: C1 Emilia-Romagna relative income, 1951/1980/1995 (Rinaldi) + 2024
  endpoint (Eurostat).
- M3: B1 saturation: penetration levels of the four durables at 1973 (OWID
  for Automobile / Household refrigerator / Washing machine; Census HS-42
  for TV — the OWID TV gap disclosed in the metric note), with the
  [PREVIEW-CALIBRATED] label on the saturation rule.
- M4: C4 EAF share trajectory (branch-labelled 1970s value → 2024
  worldsteel) — presented as a DATA TRAJECTORY, not a graded book claim,
  while C4's book-anchor stands demoted (§I.1); relabelled a claim grade
  only if a restoration event fired.
- M5: the verdict-count row of the headline as structured fields.

Machine-surface assertion (PS-C2, binding): `result_card.json` and
`followup_summary.json` are score-free (no numeric score, no score-like
aggregate; verdict-count tallies allowed); a schema field expecting a score
is set to null / "not applicable (book; GO-WITH-SCOPE)" and the mismatch is
reported for a pipeline-level fix — never hand-worked-around here.

## I.6 Out of scope

- P2 and everything H-A/H-B/H-C (study 002's entire job).
- Families A and F (prose only); the causal/mechanism halves of B2, B3, C5;
  C3's framing; D2 as data.
- Any pooled score; any "book says p.Y" attribution; any book-text fetch.
- UNIDO INDSTAT (unless A3 finds it staged), Williams et al. 1987 content
  (unless staged), paywalled literature beyond recorded metadata.
- Italian district SECTOR series (Prato/Carpi exports) this tick: next-tick
  item, named in findings as such.

---

