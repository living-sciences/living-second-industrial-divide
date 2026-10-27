# Study 002 — globalization-test: scoring Piore & Sabel's Exit 1 (prediction P2)

**Launch line:** REPLICATION: NOT APPLICABLE — BOOK, GO-WITH-SCOPE (Phase 0);
THIS STUDY SCORES PREDICTION P2 (THE READER QUESTION).

**Reader question:** *is there any evidence of globalization as a new mass-production
system?* — the book's Exit 1 (prediction P2) asked 40 years on. The study does **not**
answer yes/no; it weighs three pre-declared hypotheses on seven pre-declared signatures
and issues a verdict in the §II.5 vocabulary. No pooled/replication score is computed
(R5; book under GO-WITH-SCOPE).

---

## Prior-art positioning (binding)

The closest prior claim is **Kaplinsky (2023)** — that GVCs *sustained and extended the
mass-production paradigm* from the 1980s, and that the recent decline in GVC participation
reflects the *fracture* of that paradigm (Kaplinsky, "El auge y caída de la globalización
profunda…", staged); our **H-A is his thesis made falsifiable**. **Schwartz (2024)** gives
a 40-year assessment naming five critical errors of omission in P&S and documenting a
three-layer lead-firm production chain — a *de facto* H-C. **Baldwin (2006/2016)** is H-C's
source: the "second unbundling" fragmented production into tasks (Baldwin, *Globalisation:
the great unbundling(s)*, 2006, staged). **Gereffi, Humphrey & Sturgeon (2005)** and
**Sturgeon (2008)** supply H-B's language — the modular/relational/captive governance
taxonomy (GHS 2005, *Review of International Political Economy* 12(1):78–104,
DOI 10.1080/09692290500049805 — INTERNAL-ONLY staged copy, cited by DOI; Sturgeon 2008,
"From Commodity Chains to Value Chains," published as ch. 6 in Bair (ed.), *Frontiers of
Commodity Chain Research*, Stanford University Press, 2009 — INTERNAL-ONLY staged working
paper, cited by published chapter). **Milberg & Winkler (2013)** and **Hirst & Zeitlin
(1991)** are **recorded but not read** in this tick — they are named for positioning only,
not coded. No text here claims to be the first to ask whether globalization is mass
production. What **is** new, in exactly these terms: *the first joint, pre-declared,
falsifiable scoring of Piore & Sabel's own Exit-1 prediction against the three competing
readings on public data in one place.*

---

## P2 anchor + the H-A ↔ Exit-1-as-written mapping (PS-B4, binding)

P2's provisional anchor inherits study 001's §I.1b locators verbatim and is tagged
`book-anchor: PROVISIONAL-PENDING-H1`. Gate A1b was re-run at run start (grep over the
staged files): **all 6 inherited P2 locators hit at count = 1** (Schwartz: "They saw only
two paths out of the problems animating the debate"; Schwartz global-demand-management
fork: "improbable expansion of mass production and thus Keynesian policy of demand
management to the global level"; Berger: "apportion the expansion of productive capacity
among the advanced industrial countries", "multinational Keynesian order"; Bhengu: "They
moved into mass-produced consumer durables" + "(Piore & Sabel, 1984: 188)"). The anchor is
**live** (≥2 independent attribution sources: Schwartz, Berger, Bhengu). `attribution_sources`
(the three above) and `adjudication_sources` (WDI, WITS, BDS, Eurostat, worldsteel, WTO GVC
Report, GHS, Sturgeon, Kaplinsky, Baldwin) are never conflated; adjudication sources never
count toward attribution.

| H-A component (as operationalized) | Status vs Exit 1 as provisionally anchored |
|---|---|
| Standardized, scale-intensive production spread to the developing world | RESTATES the anchored Exit 1 (Schwartz fork locator; Bhengu 1984:188 locator) |
| New demand-stabilizing institutions ("multinational Keynesianism" — the S6 half) | RESTATES the anchored Exit 1 (Berger locators) |
| Hub concentration of manufacturing output in one country | MODERNIZED OPERATIONALIZATION (Kaplinsky 2023 / Schwartz 2024) — NOT a book component |
| Lead-firm profit structure / output-vs-VA inversion | MODERNIZED OPERATIONALIZATION (Schwartz 2024: "firms in China generated 35 percent of global manufacturing output") — NOT a book component |

**Fixed sentence:** "Any 'H-A supported/against' verdict is a verdict on the OPERATIONALIZED
hypothesis; its hub-concentration and profit-structure components are modernizations by
Kaplinsky and Schwartz, so no verdict here reads as 'the book predicted / failed to predict
China'." (001's P2 hand-off row carries the same note.)

---

## The three hypotheses

- **H-A — globalization as a new mass-production system:** rising scale of the effective
  production unit, product standardization, captive/hierarchical coordination, hub
  concentration of manufacturing output, a new global mass-consumption market.
- **H-B — flexible specialization at global scale:** GVCs as networked, modular, rapidly
  switching production; modular/relational governance; variety growth and falling batch
  sizes; persistent district and Mittelstand exports; general-purpose digital production.
- **H-C — neither: the second unbundling:** ICT + wage gaps fragmented production into
  TASKS; the plant-level dichotomy is the wrong axis; both scale (China assembly) and
  flexibility (contract switching) are surface features of one task-trade regime with
  lead-firm power as the organizing fact (Baldwin 2006/2016; Schwartz 2024; Milberg & Winkler).

---

## The seven signatures, per-era directions (E1 1984–95, E2 1995–2011, E3 2011–26)

**S1 — Scale of the production unit → favors H-C (the unit splits).**
Hub concentration: China's share of world manufacturing value added rose 8.5% (2004) →
20.2% (2011) → 27.9% (2023) while the US fell 21.9% → 15.6% → 15.5% (2021) (WDI, staged).
Western plant size, however, *smallized* then *re-concentrated*: US manufacturing
small-establishment (<100 emp) employment share rose 27.7% (1978) → 37.2% (2011) then fell
to 32.5% (2023); mean establishment size fell 58.7 → 39.2 then rose to 45.8 (BDS, via 001).
EU27 is concordant with the recent re-concentration (small <50-emp share 34.8% (**2011**) →
29.2% (2023); large ≥250-emp share 40.1% (2011) → 48.3% (2020); Eurostat SBS, two panels,
2020/2021 break). **Coverage note (PS-PROV-2 correction):** the 34.8% small-plant share was
previously labeled "(2005)"; the EU27_2020 SBS aggregate is absent before 2011 in the staged
`sbs_sc_ind_r2` file, so the true first available year is 2011 (the "2005-2020" panel name is
the dataset's nominal span, not this value's vintage). The `s1_eu_sizeclass.csv` artifact
already carries `year=2011` and is unchanged; the **E3 window (2011–2026) is unaffected**,
because the re-concentration it reads runs 2011→2023, fully inside coverage. The geography split: **China ≈89.8% basic-oxygen (integrated mills) / US
71.8% electric-arc (mini-mills), worldsteel 2025** `[PREVIEW-KNOWN: China ~91.6% BOF / US
majority-EAF, worldsteel 2025, stated at spec time]` (the spec's "≈91.6%" is the Austria
row in the staged table; the computed China BOF share is 89.8%; US majority-EAF confirmed).
Across geography (China scale vs Western smallization), era (smallization 1978–2011, E3
re-concentration), and chain position (assembly giants vs small suppliers), the production
unit stops being well-defined on one axis.

**S2 — Product standardization vs variety → weakly measured (weak cells all round).**
Standardization leg: smartphone/mobile diffusion (the "smartphone-as-Model-T") — mobile
subscriptions per 100 rose from ~0 in 1995 to 128.2 (China), 80.6 (India), 131.0 (Viet Nam)
by 2023 (WDI). Variety leg: ultra-fast-fashion / mass-customization case literature (Shein,
`company-claimed`). SKU/batch-size data do not exist at scale; the signature grades
DIRECTION only and is **weakly measured** — it yields a weak cell to all three hypotheses.

**S3 — Trade composition → favors H-C (rose 1995–2011, then plateaued).**
GVC/task-trade participation rose broadly 1995–2011 then stagnated 2011–2022 (backward
linkages modest, forward flat, aggregate broadly unchanged — WTO GVC Report 2025 ch.2
Box 2.1 / Fig 2.8, TiVA-based); GVC-related trade's share of total trade peaked at 48%
(2022) and fell to 46.3% (2024) (WTO ch.1); US–China bilateral trade grew ~30% slower than
their trade with the rest of the world since the 2018 tariffs, with rerouting via Mexico /
Viet Nam (WTO ch.1). This is H-C's rise-then-plateau + regionalization signature.
Source: **fallback (TiVA endpoint degraded, verified 2026-10-27 and at run time)** — the
OECD TiVA data query returned HTTP 500 across key shapes; the binding fallback (WTO GVC
Report 2025 chapters, page-cited, + staged WITS trend) was used. The narrower WITS
UNCTAD-SoP intermediate-goods share is **flat** over the whole window
`[PREVIEW-KNOWN: WLD SoP2 export share 19.45–24.92%, flat 1988–2023, stated at spec time]`
(SoP≠BEC seam: parts & accessories sit partly under capital goods; within-series trend only).

**S4 — Chain governance → WEAK-CELL CAP (weakly against H-A; weakly favors H-B and H-C).**
Literature-coded from the staged corpus (every industry case the four staged texts discuss,
not only the modular ones — s4_governance.csv): GHS 2005 (bicycles hierarchy→market/modular;
apparel captive→relational; fresh vegetables→relational; US electronics hierarchy→modular),
Sturgeon 2008 (electronics/contract-manufacturing modular production networks; East-Asia
upgrading relational/modular), Schwartz 2024 (three-layer chain — IP owners / capital-intensive
high-barrier / labor-intensive low-barrier — captive **in power**; China 35% output vs 29% VA
output/VA inversion), Kaplinsky 2023 (GVCs sustaining the mass-production paradigm). The
documented FORM is modular/relational; Schwartz adds captive **power** → H-C's "captive in
power, modular in form." **Fixed sentence on every S4 cell:** "literature-coded from a staged
corpus whose composition cannot measure the population governance mix." Counts are reported
as documented instances in the staged corpus, never as population frequencies; S4 may take
only `weakly favors`/`weakly against`/`not separable` toward any hypothesis (PS-B1).

**S5 — Skill content → `not separable on staged data` (fixed by declaration).**
Declared weak (mirror of D2); one literature paragraph, verdict cell fixed. Included so its
absence from the scored verdict is pre-declared, not discovered. The published record shows
skill *polarization* (both tails) rather than clean deskilling or re-skilling, but the staged
data cannot separate the hypotheses, so no cell is scored.

**S6 — Demand-side institutions → `ex-ante-decided (documentary)` (favors H-C; against H-A
as the book wrote it; against H-B).**
Documentary absence test. **Result (study-written, PS-B2a; from s6_institutions.md):** "The
institutional half of Exit 1 is absent: none of the demand-management institutions P2-as-worded
required (0 of 2) was constructed; developing-world mass consumption did arrive on market terms
— mobile subscriptions per 100 people rose from near zero in 1995 (China 0.3, India 0.0, Viet
Nam 0.0) to at or above saturation by 2023 (China 128.2, India 80.6, Viet Nam 131.0), but it
was delivered by WTO-era market integration and private GVC participation, not by any
'multinational Keynesian' demand-coordinating institution — so the global mass-consumption
market exists while the institutions that P&S's Exit 1 said would stabilize it do not."

**S7 — District persistence → partially measured (weakly favors H-A and H-C; weakly against H-B).**
Emilia-Romagna persists and remains above the EU/Italy mean (116.8% of EU27, 2024) but its
*relative* advantage declined after 2000: +29% vs the Italian mean (1980) → +19.5% (2024),
against a stagnant Italy (no per-capita income rise after 2000). Districts became a "narrow
slice of industrial output" (Schwartz 2024, attributed); the Pearl River Delta became the
largest district. Persistence is real but relative, and tied to where design/IP power is held.

---

## What counts AGAINST each hypothesis (pre-declared, verbatim)

- **Against H-A:** Western establishment sizes keep falling (S1); variety growth where
  measurable (S2); modular/relational forms weakly dominant in the documented governance
  record (S4 — AT MOST a weak cell per the PS-B1 cap); no demand-management institutions
  (S6 — against H-A AS THE BOOK WROTE IT: market-led scale without the institutions is
  "half of Exit 1", a pre-declared partial cell, `ex-ante-decided (documentary)`).
- **Against H-B:** global manufacturing output concentrating into one hub (S1);
  captive/power-asymmetric governance weakly dominant in the documented record (S4 — AT MOST
  a weak cell per the PS-B1 cap); districts' relative decline post-2000 (S7).
- **Against H-C:** intermediates/task-trade share FLAT over the whole window (S3)
  `[PREVIEW-KNOWN: WLD SoP2 export share 19.45–24.92%, flat 1988–2023, stated at spec time]`
  — if TiVA also showed no rise in backward+forward participation, H-C's core mechanism
  would lose its signature and the verdict would have to say so. **It did not:** the WTO
  Fig 2.8 fallback shows backward/total participation *rose* 1995–2011 before the post-2011
  plateau, so H-C's rise-then-plateau signature survives (the WITS-SoP flatness is the
  narrower UNCTAD-SoP measure, reported as a caveat, not a refutation); production units
  remaining stable, well-defined plants (S1 — not observed; the unit splits).
- The S1 geography-split condition carries `[PREVIEW-KNOWN: China ~91.6% BOF / US majority-EAF,
  worldsteel 2025, stated at spec time]`.

**E3 discriminator (PS-B3) → `not separable this tick`.** *Scale-economics decay* (Kaplinsky /
mass-production-paradigm fracture) requires BOTH (i) plant re-concentration in BDS/SBS over
2011→2023 — **fired** (US mean size up 39.2→45.8, small-estab share down 37.2→32.5; EU
concordant) — AND (ii) standardization reversal in the WITS SoP E3 mix (consumer share rising
*at the expense of intermediates*) — **not fired** (consumer rose 30.6→32.7 but intermediates
were flat 20.7→20.8; the consumer rise came at the expense of raw goods, not intermediates).
*Geopolitics/ICT decay* (H-C) requires ≥2 of {US–China ~30% below trend since 2018; rerouting/
friend-shoring via Mexico/Viet Nam; services/digital resilience while goods-GVC plateaus} —
**all 3 fired**. One side partial + the other firing → the E3 cell is **fixed to "not separable
this tick."** The 2011 era boundary itself carries `[SOURCE-DERIVED: WTO GVC Report 2025 plateau
finding]`.

---

## Effective denominator and tallies (PS-B2b / II.3.7)

With **S5 fixed by declaration** and **S6 ex-ante-decided (documentary)**, there are **5 live
cells** (S1, S2, S3, S4-capped-weak, S7). Because S4 is capped to at most a weak cell, each
hypothesis can reach at most **k = 4 full favors** on live cells (from S1, S2, S3, S7), read
against the ≥4 bars. **Full favors on live cells: H-A = 0, H-B = 0, H-C = 2 (S1, S3).**
No hypothesis reaches the ≥4 bar.

| Hypothesis | favors | weakly favors | against | weakly against | not separable | full favors (live) |
|---|---|---|---|---|---|---|
| H-A | 0 | 3 | 2 | 1 | 1 | 0 |
| H-B | 0 | 2 | 2 | 1 | 2 | 0 |
| H-C | 3 | 3 | 0 | 0 | 1 | 2 |

(H-C's three full `favors` are S1, S3 and S6; S6 is not a live cell — ex-ante-decided.)

**Conjunct justification (PS-B2c, decided before any cell was visible):** H-A keeps the
S1-AND-S2 conjunct because standardization is CONSTITUTIVE of mass production — scale without
standardized products is not the book's Exit 1, so "H-A without S2" is not H-A; H-B's or-form
(S2 or S7) stands because flexible specialization can express through either variety (S2) or
districts (S7).

---

## Verdict

**neither — the unbundling reading** (the second unbundling), *threshold-sensitive*.

No hypothesis reaches its ≥4-signature bar (H-A 0, H-B 0, H-C 2 full favors on live cells).
The **split condition is met** — S1 splits by geography/chain position AND S4 shows mixed
governance within chains (captive in power, modular in form) AND no hypothesis reaches ≥4 —
**and S3 favors H-C**, which routes the split into the *unbundling* verdict (§II.5): the
40-year evidence reads as one task-trade regime in which scale (China assembly) and
flexibility (contract switching) are surface features and lead-firm power is the organizing
fact. The "the dichotomy fails" condition is *simultaneously* satisfied; the unbundling
reading is **why** the book's plant-level axis fails — "the 40-year evidence cannot be scored
on the book's own axis; the axis, not the evidence, is what failed." The verdict is tagged
**threshold-sensitive** because H-C clears the bar only via the split+S3 route, with several
weak contributing cells (S2 weakly measured, S4 capped, S7 partial). The test could have come
out any of the four ways; it came out H-C.

**Fork-not-forecast (inherited verbatim, §I.2 modal rule):** "The book posed Exit 1 and
Exit 2 as politically contingent possibilities, not forecasts; neither exit's non-realization
is, by itself, a failed prediction."

---

## Headline (§II.6 template, filled)

Asked whether globalization became the new mass-production system the book's Exit 1 foresaw:
across seven pre-declared signatures on 1984–2026 data, the production unit splits by
geography and era (China's share of world manufacturing value added rose 8.5%→27.9% with
integrated basic-oxygen mills while Western plants smallized then re-concentrated and run on
electric-arc mini-mills; S1→H-C), task-trade rose 1995–2011 then plateaued (GVC-trade share
48%→46.3%; S3→H-C), governance is captive in power but modular in form (S4, capped weak),
standardization-vs-variety is only weakly measurable (S2), skill content is not separable
(S5), and districts persist as a narrow slice in relative decline (S7); the evidence points
to **neither exit — the second-unbundling reading (threshold-sensitive)**, no hypothesis
reaching the ≥4-signature bar; the institutional half of Exit 1 is absent — none of the
demand-management institutions P2-as-worded required (0 of 2) was built, yet developing-world
mass consumption arrived on market terms (mobile subscriptions per 100 rising from ~0 in 1995
to 128 in China, 131 in Viet Nam by 2023); this makes Kaplinsky's (2023) claim that GVCs
sustained the mass-production paradigm falsifiable and finds it unsupported as a whole-system
reading, converging instead with Schwartz's (2024) de facto H-C.

---

## Out-of-grading-scope engagement (R3, ≤1 paragraph each)

*Family F (interpretive):* The two-divides periodization, the first-divide counterfactual as
a general claim, the normative "possibilities for prosperity" frame, and technology-choice
indeterminacy are **out of grading scope**; engaged only to note that the unbundling reading
is itself a *re-specification* of P&S's "divide" idea onto the task rather than the plant —
a substantive but non-gradeable reframing. *Family A (historiographical [LIT]):* P&S's reading
of the first industrial divide and craft-vs-mass history is **out of grading scope**; it is
neither confirmed nor scored here.

---

## Branch disclosures, deviations & limitations

- **TiVA retry (II.4):** attempted at run start (keyless), HTTP 500 across key shapes
  (endpoint degraded, verified 2026-10-27 and at run time); binding fallback engaged (WTO GVC
  Report 2025 chapters, page-cited, + staged WITS SoP trend). S3 rows labelled accordingly.
- **INDSTAT (H3):** `shared-data/unido-indstat/` does not exist → honest exclusion:
  "cross-country plant-size distributions excluded: UNIDO INDSTAT is registration-gated (H3);
  the S1 verdict rests on US/EU size series plus hub-share data." No workaround.
- **Pre-2004 China VA-share seam:** the spec's pre-2004 China manufacturing-VA-share cells
  were to come from recency-research.md §5.4 literature values; that file is **not** among this
  run's staged inputs, so pre-2004 China cells are **not** substituted from memory. The staged
  WDI series begins 2004; the China hub-concentration finding rests on 2004–2023 (deviation).
- **steel PREVIEW label:** the spec stated "China ≈91.6% BOF"; the staged worldsteel-2025 table
  gives China 89.8% BOF (the 91.6 is the Austria row). Reported as computed; label travels (R-6:
  the magnitude gates nothing).
- **S5 (skill content):** not scored by design — no staged data separates deskilling /
  re-skilling / polarization; its absence from the verdict is pre-declared.
- **S4 corpus composition:** governance cells are literature-coded from a staged corpus whose
  composition cannot measure the population governance mix (capped weak).
- **mega-plant row (S1e):** Foxconn/EMS scale is descriptive only, carries no verdict weight.
- **Fetch policy:** staged data only otherwise; no FRED needed (001 outputs reused read-only);
  no login; no book text fetched/OCR'd/re-hosted; the two INTERNAL-ONLY PDFs (GHS 2005, Sturgeon
  2008) were read internally and cited by DOI/published chapter, no excerpt beyond fair use.
- **Schema (PS-C2 / uniform-evaluator):** `result_card.json` and `followup_summary.json` carry
  no numeric/pooled score; `gates.json` sets `replication_score: null` with
  "not applicable (book; GO-WITH-SCOPE)". The followup/card schemas do not force a score field,
  so none had to be hand-worked-around; verdict-count tallies (structured) are used. Reported
  here per the uniform-evaluator rule for any downstream pipeline fix.
