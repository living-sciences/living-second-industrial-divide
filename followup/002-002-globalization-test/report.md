# Follow-up study 002 — globalization-test

**Book:** Piore & Sabel (1984), *The Second Industrial Divide* (Basic Books).
**Status:** BOOK under GO-WITH-SCOPE — there is NO Phase-1 replication and NO replication
score, by design. This study scores the book's closing **prediction P2 (Exit 1)**.
**Date:** 2026-10-27.

## Question

A reader asked, through the site: *is there any evidence of globalization as a new
mass-production system?* — the book's Exit 1 (prediction P2) asked 40 years on. This study
does not answer yes/no. It weighs three pre-declared, falsifiable hypotheses —
**H-A** (globalization as a *new mass-production system*), **H-B** (*flexible specialization
at global scale*), **H-C** (*neither — the second unbundling*: a task-trade regime organized
by lead-firm power) — across **seven pre-declared signatures** on 1984–2026 public data,
issues per-cell verdicts and one overall verdict in a fixed vocabulary, and treats "the
book's dichotomy itself fails" as a first-class pre-declared outcome. No pooled score is
computed.

## Approach — what I ran, reused, and added

**Reused from the completed work (read-only):** study 001's `claim_D1_manufacturing.csv`
(US BDS establishment-size series, for S1b), `claim_C1.csv` (Emilia-Romagna relative income,
for S7), and the 001 §I.1b P2 attribution locators and gate structure. The replication
scaffold confirms no Phase-1 code exists for this book; 001 is the verification layer.

**Gates re-run at run start:** sha256 integrity of all 13 staged data files (**13/13 match**);
**gate A1b** — the 6 inherited P2 anchor locators re-grepped against the staged Schwartz HTML,
Berger PDF and Bhengu PDF (**all hit at count = 1**) → P2 book-anchor **live** (≥2 independent
attribution sources), graded as worded, tagged `PROVISIONAL-PENDING-H1`.

**Declared in-run fetch (II.4):** the OECD TiVA retry (keyless) — **HTTP 500 across key
shapes** (endpoint degraded, confirmed at run time) → the binding fallback (WTO GVC Report
2025 chapters, page-cited, + staged WITS trend) was used for S3. Logged in `fetch_log.json`.
No other fetch; no FRED needed (001 outputs reused); no book text touched; INDSTAT (H3) and
USGS (blocked) not attempted.

**Added (this study):** the seven signature constructions from the staged data (WDI
manufacturing VA shares; BDS + Eurostat SBS establishment sizes; worldsteel process split;
WITS UNCTAD-SoP export mix; WDI mobile-subscription diffusion; WTO GVC Report participation
and decoupling figures; literature-coded governance tuples from GHS 2005, Sturgeon 2008,
Schwartz 2024, Kaplinsky 2023; Baldwin 2006 as H-C's source), the E3 discriminator, the
evidence grid with the §II.5 cell vocabulary, and the verdict logic.

## Results

**Verdict: "neither — the unbundling reading" (the second unbundling), threshold-sensitive.**
No hypothesis reached its ≥4-signature bar (full favors on live cells: H-A 0, H-B 0, H-C 2).
The split condition was met (S1 splits by geography/chain position; S4 mixed governance; no
hypothesis ≥4) **and** S3 favors H-C, which routes the split into the unbundling verdict. The
"dichotomy fails" condition is simultaneously satisfied — the unbundling reading is *why* the
book's plant-level axis fails.

| Signature | Reading | H-A | H-B | H-C |
|---|---|---|---|---|
| S1 scale of production unit | unit splits by geography & era | weakly favors | against | **favors** |
| S2 standardization vs variety | weakly measured | weakly favors | weakly favors | weakly favors |
| S3 trade composition | rose 1995–2011, then plateaued | against | not separable | **favors** |
| S4 chain governance (cap: weak) | captive in power, modular in form | weakly against | weakly favors | weakly favors |
| S5 skill content (declared weak) | not separable on staged data | not separable | not separable | not separable |
| S6 demand-side institutions (ex-ante doc.) | no demand-management institutions exist | against | against | **favors** |
| S7 district persistence (partial) | persist as a narrow slice, relative decline | weakly favors | weakly against | weakly favors |

### Key quantities (all computed this study unless noted)

| Quantity | Value | Source |
|---|---|---|
| China share of world manuf VA | 8.5% (2004) → 20.2% (2011) → 27.9% (2023) | WDI NV.IND.MANF.CD (staged) |
| US share of world manuf VA | 21.9% (2004) → 15.6% (2011) → 15.5% (2021) | WDI (staged) |
| US mfg small-estab (<100) emp share | 27.7% (1978) → 37.2% (2011) → 32.5% (2023) | BDS, via 001 (read-only) |
| US mfg mean establishment size | 58.7 → 39.2 (2011) → 45.8 (2023) | BDS, via 001 |
| EU27 mfg small (<50) emp share | 34.8% (2011) → 29.2% (2023) | Eurostat SBS (staged, 2 panels; PS-PROV-2: relabeled from "(2005)" — EU27_2020 absent pre-2011; CSV already honest, E3 unaffected) |
| Steel process split (2024) | China 89.8% BOF / US 71.8% EAF | worldsteel 2025 (staged) |
| WITS intermediate (SoP2) export share | flat, 19.45–24.92%, 1988–2023 | WITS UNCTAD-SoP (staged) |
| GVC-related trade share of total trade | peak 48.0% (2022) → 46.3% (2024) | WTO GVC Report 2025 ch.1 (staged) |
| US–China bilateral trade vs rest-of-world | ~30% slower since 2018 tariffs | WTO GVC Report 2025 ch.1 (staged) |
| Developing-world mobile subs/100 (1995→2023) | China 0.3→128.2; India 0.0→80.6; Viet Nam 0.0→131.0 | WDI IT.CEL.SETS.P2 (staged) |
| Demand-management institutions required vs exist | 0 of 2 exist | documentary (S6) |

**E3 discriminator (2011–2026): "not separable this tick."** US/EU plant re-concentration
fired, but S2 standardization-reversal did not (consumer-goods export share rose at the
expense of raw, not intermediates); the geopolitics/ICT side fired on all three observables.
One side partial + the other firing → the pre-declared "not separable" outcome.

### Figures
- `results/fig_scale.png` — S1: China hub concentration of manufacturing VA (left) and US
  plant-size smallization-then-re-concentration (right), era-shaded.
- `results/fig_composition.png` — S3: WITS SoP export mix (flat intermediates, PREVIEW-KNOWN
  band) and the WTO rise-then-plateau participation summary.
- `results/fig_evidence_grid.png` — the 7×3 signature × hypothesis grid, color-coded.

## Comparison to the original work

The baseline for a GO-WITH-SCOPE book is **not** a replication number — none exists (confirmed
in `/workspace/eval/replication/codebase/README.md`). The relevant comparison is to study 001's
hand-off: 001 graded P3 (flexible specialization) "partially supported (modal)" and handed P2
to this study. Where 001 built series this study reuses them unchanged:

| Quantity | 001 value | 002 use | Source file |
|---|---|---|---|
| US mfg small-estab emp share (1978→2023) | 27.69% → 32.53% | reused for S1b (adds E3 reversal reading: up to 37.2% in 2011 then down) | 001 `claim_D1_manufacturing.csv` |
| Emilia-Romagna rel. income | +29% vs Italy (1980) → +19.5% (2024) | reused for S7 | 001 `claim_C1.csv` |
| P2 anchor locators | 37/37 verified (incl. P2) | re-grepped 6 P2 locators, all hit | 001 `gates.json` |

## Deviations & limitations

1. **TiVA degraded** → binding WTO+WITS fallback for S3 (logged); preferred backward/forward
   participation series unavailable this tick.
2. **Pre-2004 China VA share** not substituted — the specced literature source (recency-research.md
   §5.4) is not among this run's staged inputs; China hub finding rests on WDI 2004–2023.
3. **S5 (skill)** not scored by design; **S4** capped weak (corpus cannot measure population
   governance mix); **S2** weakly measured (no SKU/batch data); **S7** partially measured.
4. **INDSTAT** excluded (H3, registration-gated); **steel PREVIEW label** travels with the
   computed value (China 89.8% BOF, not the spec's 91.6% = Austria row).
5. **No pooled/replication score** anywhere (R5); `gates.json` sets `replication_score: null`
   = "not applicable (book; GO-WITH-SCOPE)".
6. **PS-PROV-2 correction (study 003):** the EU27 small-plant share was relabeled from
   "34.8% (2005)" to **"34.8% (2011)"** — the EU27_2020 SBS aggregate is absent before 2011
   in the staged `sbs_sc_ind_r2` file ("2005-2020" is the dataset's nominal span, not the
   value's vintage; `build_signatures.py` had hard-coded `_2005` key names). The
   `s1_eu_sizeclass.csv` artifact was already honest (`year=2011`) and is unchanged; the E3
   window (2011–2026) is **unaffected**. No verdict word or grid cell changed.
7. **PS-PROV-5 correction (study 003):** the descriptive mega-plant row's from-memory Foxconn
   "~200k–350k" peak-employment figure had no staged source and was **removed** (the
   qualitative sentence is kept). The staged texts (Kaplinsky 2023, WTO GVC ch.1 & ch.2,
   Schwartz 2024) carry no citable single-plant employment figure — Kaplinsky names Foxconn
   only as a triangular-governance intermediary — so nothing was moved to `s1_scale.csv`. The
   row was descriptive only and carried no verdict weight; no verdict changed.

The verdict is **threshold-sensitive**: H-C clears via the split+S3 route, not by a clean
≥4-favor margin, and several contributing cells are weak. A future tick with a recovered TiVA
endpoint, a staged INDSTAT extract, and Rauch product-differentiation series (the named
next-tick items) would tighten S1, S2 and S3.
