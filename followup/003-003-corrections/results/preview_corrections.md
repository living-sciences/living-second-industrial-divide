# Preview correction — China BOF share (flows back to the H1 re-grade branch and the spec/PROVENANCE record)

**Status:** recorded only. The spec itself is the orchestrator's file and was **NOT**
edited (per the instruction). This note is the durable record of the correction and is
flagged for (a) the **H1 re-grade branch** and (b) the **spec / PROVENANCE record**.

## The correction (old → new)

| Item | Old (spec [PREVIEW-KNOWN]) | New (computed cold, this run) | Gate |
|---|---|---|---|
| China crude-steel share by basic-oxygen (BOF) process | **≈91.6% BOF** | **89.8% BOF** (10.2% EAF) | H1 re-grade |

The spec's `[PREVIEW-KNOWN: China ~91.6% BOF / US majority-EAF, worldsteel 2025, stated at
spec time]` carried **91.6%** for China. That figure is **not China's** — it is the
**Austria row** of the staged worldsteel table. China's true basic-oxygen share is
**89.8%**.

## Worldsteel row evidence

Source: *World Steel in Figures 2025* (staged: `followup_staging/shared-data/steel/world-steel-in-figures-2025.pdf`,
sha256 `a830f0b9…48d4`, A1 hash-verified in both studies' gates.json), table **"Crude steel
production by process, 2024"**. Columns: *Million tonnes | Oxygen % | Electric % | Other % |
Total %*. Extracted text `workspace/pdftext/worldsteel2025.txt`:

```
line 328:  Austria        7.1      91.6      8.4      -    100.0
line 377:  China e    1 005.1      89.8     10.2      -    100.0
```

- **Austria:** 7.1 Mt crude steel, **91.6% Oxygen (BOF)**, 8.4% Electric (EAF).  ← the spec's "91.6"
- **China (e):** 1,005.1 Mt crude steel, **89.8% Oxygen (BOF)**, 10.2% Electric (EAF).

So the spec read the Oxygen-% cell one row too high (Austria, 91.6) and attributed it to
China. The computed China BOF = **89.8%**; US majority-EAF (71.8% Electric) is confirmed
(worldsteel line 377/the US row). These are the values already carried honestly in study
002's `results/s1_steel_split.csv` and `results/_grid_keyresults.json` (`S1_steel`).

## Why the verdict/grid did not move

Per study 002's R-6 ("the magnitude gates nothing"), the S1 geography-split signature turns
on the qualitative fact *China ≈ integrated/basic-oxygen mills vs US ≈ electric-arc
mini-mills*, which holds at **89.8%** exactly as it would at 91.6%. No S1 cell, no evidence-
grid cell, and no verdict word changes. This correction is therefore a **label/provenance
fix**, carried forward so the spec's `[PREVIEW-KNOWN]` constant and any H1 re-grade use the
true China value (89.8%) and attribute 91.6% to Austria.

## Flagged for

1. **H1 re-grade branch** — when the book's own wording is available and verdicts are
   re-issued, use China BOF = 89.8% (not 91.6%) in the S1 steel-geography evidence.
2. **spec / PROVENANCE record** — the orchestrator should update the `[PREVIEW-KNOWN]`
   China-BOF constant from ≈91.6% to 89.8% and annotate that 91.6% is the Austria row.
   (Not done here: the spec is the orchestrator's file.)
