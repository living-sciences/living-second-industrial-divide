<!-- LAUNCH FILE: study 002-globalization-test ONLY. Where this spec reuses 001 outputs, read them from this run's followup/ directory. -->

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


# PART II: Follow-up study 002, globalization-test

**LAUNCH LINE:** `REPLICATION: NOT APPLICABLE — BOOK, GO-WITH-SCOPE (Phase 0);
THIS STUDY SCORES PREDICTION P2 (THE READER QUESTION)` (fixed)

**Launcher settings:** the study launcher ran as `followup <run_dir> --instruction-file
<part-II.md> --name globalization-test --timeout 14400`. Crash protection
only; expect well under 1 core-hour (series assembly + figures). Runs after
001 completes (it reuses 001's D1 outputs read-only; if 001 has not run, the
D1-dependent cells compute their own BDS parse — declared, same code path).

## II.0 What this study is (binding framing)

The reader's question is the book's Exit 1 asked 40 years on. The study does
NOT answer yes/no; it weighs three pre-declared hypotheses on seven
pre-declared signatures and issues a verdict in the §II.5 vocabulary, where
"the dichotomy itself fails" (H-C or split verdicts) is as publishable as
either exit. The test must be able to come out any of the four ways.

**Hypotheses (fixed wording):**
- **H-A — globalization as a new mass-production system:** standardized,
  scale-intensive production reassembled at global level: rising scale of the
  effective production unit, product standardization, captive/hierarchical
  coordination, hub concentration of manufacturing output, and a new global
  mass-consumption market.
- **H-B — flexible specialization at global scale:** GVCs as networked,
  modular, rapidly switching production: modular/relational governance (GHS
  2005 taxonomy), variety growth and falling batch sizes, persistent district
  and Mittelstand exports, general-purpose digital production technology in
  the CNC role.
- **H-C — neither: the second unbundling:** ICT + wage gaps fragmented
  production into TASKS; the plant-level dichotomy of the book is the wrong
  axis; the production unit dissolves; both scale (China assembly) and
  flexibility (contract switching) appear as surface features of one
  task-trade regime with lead-firm power as the organizing fact (Baldwin
  2006/2016; Schwartz 2024's omissions; Milberg & Winkler).

**Prior-art positioning (binding; first results paragraph of
`results/findings.md` verbatim in structure):** must name Kaplinsky 2023 (the
closest prior claim — GVCs sustained the mass-production paradigm; our H-A is
his thesis made falsifiable), Schwartz 2024 (40-year assessment; five
omissions; a de facto H-C), Baldwin 2006/2016 (H-C's source), GHS 2005 and
Sturgeon 2008 (H-B's language; cite DOIs — INTERNAL ONLY files), Milberg &
Winkler 2013 and Hirst & Zeitlin 1991 (recorded, not read — say so). No text
may claim to be the first to ask whether globalization is mass production.
What IS new, in exactly these terms: "the first joint, pre-declared,
falsifiable scoring of Piore & Sabel's own Exit-1 prediction against the
three competing readings on public data in one place."

**II.0b P2 anchor inheritance + the H-A ↔ Exit-1-as-written mapping
(PS-B4, binding).** P2's provisional anchor inherits study 001's §I.1b
locators verbatim (Schwartz: `They saw only two paths out of the problems
animating the debate` and the global-demand-management fork locator;
Berger: `apportion the expansion of productive capacity among the advanced
industrial countries`, `multinational Keynesian order`; Bhengu:
`They moved into mass-produced consumer durables` + `(Piore & Sabel, 1984:
188)` for the developing-world component). Gate A1b applies here identically
(run-start grep; demote on miss). The per-component mapping below ships as a
table in `results/findings.md` and as one line on the card, and BINDS every
H-A verdict sentence:

| H-A component (as operationalized) | Status vs Exit 1 as provisionally anchored |
|---|---|
| Standardized, scale-intensive production spread to the developing world | RESTATES the anchored Exit 1 (Schwartz fork locator; Bhengu 1984:188 locator) |
| New demand-stabilizing institutions ("multinational Keynesianism" — the S6 half) | RESTATES the anchored Exit 1 (Berger locators) |
| Hub concentration of manufacturing output in one country | MODERNIZED OPERATIONALIZATION (Kaplinsky 2023 / Schwartz 2024) — NOT a book component |
| Lead-firm profit structure / output-vs-VA inversion | MODERNIZED OPERATIONALIZATION (Schwartz 2024: `firms in China generated 35 percent of global manufacturing output`) — NOT a book component |

Fixed sentence (findings + card): "Any 'H-A supported/against' verdict is a
verdict on the OPERATIONALIZED hypothesis; its hub-concentration and
profit-structure components are modernizations by Kaplinsky and Schwartz,
so no verdict here reads as 'the book predicted / failed to predict
China'." 001's P2 hand-off row carries the same note.

## II.1 The seven signatures (pre-declared; per-signature data, predictions, and what counts AGAINST each)

For each signature: prediction under H-A / H-B / H-C, the series, and the
pre-declared reading. "↑/↓/—" are directions over the era windows of §II.2.

| S | Signature | H-A predicts | H-B predicts | H-C predicts | Data (staged unless marked) |
|---|---|---|---|---|---|
| S1 | Scale of the production unit | ↑ (global concentration of manufacturing into mega-hubs and mega-plants) | ↓/— (smallization continues everywhere) | SPLITS by position in the chain (assembly giant, rest small) — the unit stops being well-defined | WDI (China/hub shares of world manuf VA); BDS + Eurostat SBS (US/EU establishment size); INDSTAT branch (gated, H3): cross-country size distributions; mega-plant row: Foxconn/EMS scale from public filings/press, DESCRIPTIVE ONLY, no verdict weight |
| S2 | Product standardization vs variety | standardization ↑ (smartphone-as-Model-T) | variety ↑, batch size ↓ | variety in CONSUMPTION, standardization in TASKS/components — both, at different layers | export similarity/composition from WITS SoP (consumer vs intermediate mix); smartphone diffusion (WDI mobile subs); declared-limits row: SKU/batch-size data do not exist at scale — the signature grades DIRECTION from named case literature (Shein LATR = company-claimed, labelled; mass-customization lit) and says "weakly measured" |
| S3 | Trade composition | final goods dominate (export of standardized products) | specialized/differentiated intermediates between network equals | intermediates/task trade ↑ then plateau; regionalization after 2011 | WITS SoP 1988-2023 (staged; TREND only — SoP≠BEC seam binding); TiVA retry branch (II.4): backward/forward participation 1995-2020; WTO GVC Report 2025 (staged) for the 2011+ plateau and decoupling |
| S4 | Chain governance | captive/hierarchy (central control of standardized work) | modular/relational (district logic stretched) | lead-firm IP power over de-jure-independent suppliers — captive in POWER, modular in FORM | GHS 2005 taxonomy applied to the documented record (literature-coded rows, each with named source); Schwartz 2024 profit-concentration figures; NO new firm-level data this tick. **WEAK-CELL CAP (PS-B1, binding):** S4's cell may take ONLY `weakly favors` / `weakly against` / `not separable` — never full `favors`/`against` — toward ANY hypothesis (H-A "captive dominant", H-B "modular/relational", H-C "captive in power, modular in form" alike), and every S4 cell carries the fixed sentence: "literature-coded from a staged corpus whose composition cannot measure the population governance mix" |
| S5 | Skill content | ↓ (deskilling at the global line) | ↑ (re-skilling) | polarization (both tails) | DECLARED WEAK (mirror of D2): one literature paragraph, verdict cell fixed to "not separable on staged data" — included so its absence from the verdict is pre-declared, not discovered |
| S6 | Demand-side institutions | P2-as-written REQUIRES constructed global demand management ("multinational Keynesianism") | regional institutions balancing competition/cooperation | market-led integration; no demand institutions; decay handled by geopolitics (tariffs, industrial policy) | Documentary absence test: does any global demand-management institution exist? (WTO-era market integration instead; WTO report staged); developing-world demand diffusion from WDI mobile subscriptions ONLY (PS-A2a: the vehicles indicator returned no data and is not staged) — the cleanest single test of the institutional half of Exit 1. EX-ANTE-DECIDED LABEL (PS-B2): the outcome is documentary and known at spec time; the cell is labelled `ex-ante-decided (documentary)` on the grid, in findings, and on the card, and its RESULT SENTENCE is written by the study into `s6_institutions.md`, never pre-written by this spec |
| S7 | District persistence | districts absorbed/marginalized | districts persist as exporters inside GVCs | districts persist only where they hold IP/design power | Eurostat E-R series (staged) + 001's C1/P3 outputs; Third-Italy post-2000 record (Schwartz; Italian stagnation); labelled partially-measured |

**What counts AGAINST each hypothesis (pre-declared, verbatim in findings):**
- *Against H-A:* Western establishment sizes keep falling (S1); variety
  growth where measurable (S2); modular/relational forms weakly dominant in
  the documented governance record (S4 — AT MOST a weak cell per the PS-B1
  cap); no demand-management institutions (S6 — against H-A AS THE BOOK
  WROTE IT, noted as such: market-led scale without the institutions is
  "half of Exit 1", a pre-declared partial cell, `ex-ante-decided
  (documentary)`).
- *Against H-B:* global manufacturing output concentrating into one hub
  (S1); captive/power-asymmetric governance weakly dominant in the
  documented record (S4 — AT MOST a weak cell per the PS-B1 cap);
  districts' relative decline post-2000 (S7).
- *Against H-C:* intermediates/task-trade share FLAT over the whole window
  (S3) `[PREVIEW-KNOWN: WLD SoP2 export share 19.45–24.92%, flat 1988–2023,
  stated at spec time]` — if TiVA also shows no rise in backward+forward
  participation, H-C's core mechanism loses its signature and the verdict
  must say so; production units remaining stable, well-defined plants (S1).
- The S1 geography-split condition (used by "the dichotomy fails") carries
  `[PREVIEW-KNOWN: China ≈91.6% BOF / US majority-EAF, worldsteel 2025,
  stated at spec time]`. Both PREVIEW-KNOWN labels travel to the affected
  S1/S3 cells, findings.md, gates.json, and the card (PS-C1).
- **E3 discriminator rule (PS-B3, fixed).** The era structure (II.2)
  separates Kaplinsky's H-A-decay reading from H-C on NAMED observables
  over E3 (2011-2026), decided as follows:
  - *scale-economics decay* (reads as "mass-production paradigm fracture",
    Kaplinsky) = BOTH of: (i) plant re-concentration in the BDS/SBS E3
    window (US mean establishment size rising AND small-establishment
    employment share falling, 2011→2023; EU panel direction concordant);
    (ii) standardization reversal in S2's export mix (consumer-goods share
    rising at the expense of intermediates in the WITS SoP E3 window).
  - *geopolitics/ICT decay* (reads as H-C) = at least TWO of: (i) the
    staged WTO ch.1 tariff-timed bilateral collapse (US-China ~30% below
    trend since 2018); (ii) rerouting/friend-shoring per the staged WTO
    chapters (e.g., Mexico overtaking China as top US import source, late
    2023); (iii) services/digital trade resilience per WTO ch.2 while
    goods-GVC participation plateaus.
  - Mixed evidence (one side partial, or both sides firing) → the E3 cell
    is FIXED to "not separable this tick", stated with the per-side tally.
  The 2011 era boundary itself carries `[SOURCE-DERIVED: WTO GVC Report
  2025 plateau finding]` everywhere it appears (PS-C1).

## II.2 Era windows (fixed)

E0 1950-1984 (the book's own record — read-only from 001), E1 1984-1995
(pre-GVC), E2 1995-2011 (deep globalization; the contest's home era), E3
2011-2026 (slowbalisation/decoupling). Every signature row reports per-era
direction where its series reaches; no era is dropped.

## II.3 Pre-declared constructions

1. `results/s1_scale.csv`: (a) China/US/DE/JP/KR shares of world
   manufacturing VA, 2004-2023 (WDI; pre-2004 China cells from labelled
   literature values, seam §5.4 of recency-research.md); (b) US manufacturing
   small-establishment (<100 emp) employment share and mean establishment
   size, 1978-2023 (BDS sector 31-33); (c) EU size-class shares 2005-2020 /
   2021+ (two panels, break labelled); (d) INDSTAT branch if staged;
   (e) mega-plant descriptive row (labelled, no weight).
2. `results/s2_standardization.csv`: WITS consumer-vs-capital-vs-intermediate
   export mix by era; WDI smartphone diffusion curves (CHN, IND, VNM, BRA,
   MEX, IDN vs USA/DEU); the case-literature rows labelled
   `company-claimed`/`literature`.
3. `results/s3_composition.csv`: SoP shares by era + TiVA branch output
   (II.4) + the WTO-report 2011+ plateau figures (page-cited to the staged
   PDF).
4. `results/s4_governance.csv`: literature-coded rows — each a (source,
   year, industry, governance type, direction) tuple. CODING PROTOCOL
   (PS-B1c, binding): code EVERY industry case the four staged texts
   discuss — the GHS 2005 and Sturgeon 2008 examples AND Schwartz 2024's
   captive/power and profit-concentration passages AND Kaplinsky 2023's
   paradigm cases — never only the modular examples; the full tuple table
   ships as the csv. Counts reported as "documented instances in the staged
   corpus", never as population frequencies; the resulting cell obeys the
   S4 weak-cell cap and carries the fixed corpus-composition sentence
   (II.1).
5. `results/s6_institutions.md`: the absence test — enumerate the
   institutions P2-as-written requires (from the provisional anchor:
   international demand management, labor-share mechanisms in the South),
   state what exists instead (WTO accession, GVC participation without
   demand coordination), each line sourced.
6. `results/s7_districts.csv`: E-R relative income by era; the Schwartz
   "narrow slice" judgment quoted with attribution.
7. `results/evidence_table.csv`: signature × hypothesis grid with cells from
   the §II.5 cell vocabulary + one-line basis + data file per cell, PLUS
   (PS-B2b, PS-C1) per-cell label columns: `ex_ante_label` (S5 = `fixed by
   declaration`; S6 = `ex-ante-decided (documentary)`; S3's staged primary =
   `[PREVIEW-KNOWN: flat SoP, stated at spec time]`; S1's steel split =
   `[PREVIEW-KNOWN]`; blank otherwise) and the EFFECTIVE-DENOMINATOR
   statement, computed and printed with the grid, in findings, and on the
   card: "with S5 fixed and S6 known ex ante, each hypothesis can reach at
   most k favors on live cells" (k stated per hypothesis; 5 live cells —
   S1, S2, S3, S4-capped-weak, S7 — against the ≥4 bars, so the bars are
   read honestly).

## II.4 Declared branches

- **TiVA retry (preferred for S3 and the participation headline):** at run
  start, retry the recorded query
  (`https://sdmx.oecd.org/public/rest/data/OECD.STI.PIE,DSD_TIVA_MAINSH@DF_MAINSH,1.1/...`,
  keyless) with the exact patterns in `extension-assets/PROVENANCE.md`. If it
  answers: stage to `results/`, log in fetch_log, use backward+forward
  participation 1995-2020+ as S3's primary. If it still 500s: the fallback is
  BINDING — WTO GVC Report 2025 chapter figures (page-cited) + the staged
  WITS trend, and the S3 rows say `source: fallback (TiVA endpoint degraded,
  verified 2026-10-27 and at run time)`.
- **INDSTAT (H3):** if `shared-data/unido-indstat/` exists, S1(d) runs; else
  the honest-exclusion sentence ships in findings and on the card: "cross-
  country plant-size distributions excluded: UNIDO INDSTAT is registration-
  gated (H3); the S1 verdict rests on US/EU size series plus hub-share
  data." No workaround.
- **FRED (shared with 001):** same declared endpoints if 001's outputs are
  absent.
- No other fetch. No login. No book text.

## II.5 Pre-declared verdict vocabulary

Cell vocabulary (evidence_table.csv): `favors` / `weakly favors` /
`against` / `weakly against` / `not separable` / `not measured (gate: …)`.

Verdict vocabulary (exactly one, the §II.6 template filled; wherever a
condition counts cells, an S4 cell can contribute AT MOST a weak cell per
the PS-B1 cap, for every hypothesis):
- "**globalization as new mass production — supported with the institutional
  half absent**": ≥4 signatures favor H-A, including S1 AND S2, and the S6
  caveat sentence attaches (the book's Exit 1 required institutions that do
  not exist — so even full H-A support is "Exit 1's market half").
  CONJUNCT JUSTIFICATION (PS-B2c, decided now, before any cell is visible):
  H-A keeps the S1-AND-S2 conjunct because standardization is CONSTITUTIVE
  of mass production — scale without standardized products is not the
  book's Exit 1, so "H-A without S2" is not H-A; H-B's or-form stands
  because flexible specialization can express through either variety (S2)
  or districts (S7). This sentence ships in findings beside the conditions.
- "**flexible specialization at global scale — supported**": ≥4 favor H-B
  including (S2 or S7), with S4 contributing at most a weak cell (PS-B1b:
  H-B's condition no longer REQUIRES the corpus-biased S4 cell).
- "**neither — the unbundling reading**": ≥4 favor H-C including S3, or the
  split condition below plus S3 favoring H-C.
- "**the dichotomy fails**": S1 splits by geography/chain position AND S4
  shows mixed governance within chains AND no hypothesis reaches its ≥4
  condition — stated as a finding about the book's frame, with the sentence:
  "the 40-year evidence cannot be scored on the book's own axis; the axis,
  not the evidence, is what failed." This outcome is as reportable as any
  other.
- If none of the four conditions is met: "**uninformative at this tick**",
  with the per-signature power statement (which cells were `not separable`/
  `not measured` and what would separate them — the next-tick list).

Banned words anywhere: "proves", "debunks", "the book predicted China"
(it did not — the provisional anchor is graded as worded), any pooled score;
and (PS-C1) "pre-registered" / "validated" applied to the three previewed
constants (the flat-SoP condition, the steel geography split, the 2011 era
boundary) — those take their [PREVIEW-KNOWN]/[SOURCE-DERIVED] labels
instead. Threshold rule: a verdict resting on exactly 4 signatures where any
cell is `weakly favors` is reported with ", threshold-sensitive" attached.
P2 verdict block: `results/findings.md` inherits 001's fork-not-forecast
sentence VERBATIM (§I.2 modal rule): "The book posed Exit 1 and Exit 2 as
politically contingent possibilities, not forecasts; neither exit's
non-realization is, by itself, a failed prediction."

## II.6 Headline template (fixed)

"Asked whether globalization became the new mass-production system the book's
Exit 1 foresaw: across seven pre-declared signatures on 1984-2026 data,
[filled per-signature summary]; the evidence [verdict phrase from §II.5];
[S6 result sentence, from s6_institutions.md — a FILL SLOT per PS-B2a: even
a certain result is written by the study, never pre-written by this spec];
[one sentence positioning vs Kaplinsky 2023 and Schwartz 2024]."

## II.7 Deliverables

`report.md`, `followup_summary.json`, `result_card.json`,
`results/findings.md` (with the binding prior-art paragraph, the against-
lists verbatim incl. their PREVIEW-KNOWN labels, the PS-B4 mapping table +
fixed sentence, the fork-not-forecast sentence in the P2 block, the S4
corpus-composition sentence, the conjunct-justification sentence, the
ex-ante-decided labels + effective denominators, the branch disclosures,
limitations incl. S5), the seven §II.3 files, `results/fetch_log.json`, `gates.json`, figures (at most 3 on
the card): `fig_scale.png` (S1: hub shares + establishment-size panels,
era-shaded), `fig_composition.png` (S3: SoP trend + TiVA-or-fallback
participation, era-shaded), `fig_evidence_grid.png` (the signature ×
hypothesis grid rendered).

Result card (at most 5 metrics; `result_card.json` and
`followup_summary.json` are score-free per the shared PS-C2 constraint —
schema-expects-a-score → null / "not applicable (book; GO-WITH-SCOPE)" +
reported mismatch; the card also carries the PS-B4 mapping line, the
ex-ante-decided labels, the effective-denominator statement, and the
[PREVIEW-KNOWN]/[SOURCE-DERIVED] labels wherever the three previewed
constants appear):
- `headline`: §II.6 filled.
- M1: China share of world manufacturing VA by era (2004→2023) beside the US
  share, with the Schwartz output/VA inversion sentence (attributed to
  Schwartz 2024 — a modernized-operationalization component per the PS-B4
  mapping, never phrased as a book prediction).
- M2: US small-establishment employment share 1978→2023 + EU panel endpoint.
- M3: S3's participation/intermediates trend per era, source-labelled
  (TiVA or fallback).
- M4: the evidence grid's column tallies (favors/against per hypothesis).
- M5: the S6 absence finding as a structured row (institutions required: 0
  of [k] exist; what exists instead, named).

## II.8 Out of scope

- Firm-level governance datasets, Orbis/compustat anything (paywalled);
  SKU/batch-size measurement beyond the declared weak-signature row.
- Rauch-classification product-differentiation series and export-
  concentration indices this tick (endpoint not verified at 2a — NAMED
  next-tick item, not improvised in-run).
- Hendon-Mob-style scraping of plant lists; Foxconn beyond the descriptive
  row; any China NBS fetch (registration + language gates — next-tick with
  INDSTAT).
- Re-grading 001's rows; any family-F judgment; any "book says p.Y".
- Any outward message; any login; any model/API spend beyond the session.

---

