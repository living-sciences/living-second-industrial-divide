import pandas as pd, json, os
RES = "/workspace/eval/followup/002-002-globalization-test/results"
R001 = "/workspace/eval/followup/001-001-claims-and-predictions/results"
K = json.load(open(f"{RES}/_s1s3_keyresults.json"))

PREVIEW_SOP = "[PREVIEW-KNOWN: WLD SoP2 export share 19.45-24.92%, flat 1988-2023, stated at spec time]"
PREVIEW_STEEL = "[PREVIEW-KNOWN: China ~91.6% BOF / US majority-EAF, worldsteel 2025, stated at spec time]"
SRC_2011 = "[SOURCE-DERIVED: WTO GVC Report 2025 plateau finding]"
S4_FIXED = "literature-coded from a staged corpus whose composition cannot measure the population governance mix"

# ================= S4: governance tuples =================
# (source, year, industry, governance_type, direction) — code EVERY industry case the four staged texts discuss
s4 = [
 ("Gereffi-Humphrey-Sturgeon", 2005, "bicycles", "hierarchy -> market/modular", "toward market/modular (Shimano component standards)"),
 ("Gereffi-Humphrey-Sturgeon", 2005, "apparel", "captive -> relational", "toward relational (East Asia full-package supply)"),
 ("Gereffi-Humphrey-Sturgeon", 2005, "fresh vegetables (UK-Africa)", "relational/modular", "buyer-driven, became relational not captive (UK supermarkets)"),
 ("Gereffi-Humphrey-Sturgeon", 2005, "US electronics", "hierarchy -> modular", "toward modular (contract manufacturing, Solectron turn-key)"),
 ("Sturgeon", 2008, "electronics / contract manufacturing", "modular", "modular production networks, turn-key suppliers, generic machinery"),
 ("Sturgeon", 2008, "East Asia industrial upgrading", "relational/modular", "upgrading via modular + relational linkages"),
 ("Schwartz", 2024, "three-layer global production chain", "captive-in-power", "IP owners / capital-intensive high-barrier / labor-intensive low-barrier firms; lead-firm power over de-jure-independent suppliers"),
 ("Schwartz", 2024, "China vs US manufacturing (output/VA inversion)", "captive-in-power", "China 35% output / 29% VA vs US 12% output / 16% VA 2023; inversion = lingering US lead-firm dominance over Chinese subcontractors"),
 ("Kaplinsky", 2023, "GVC-era manufacturing (paradigm)", "scale/standardization sustained via GVCs", "GVCs maintained the mass-production paradigm from 1980s; decline of GVC participation = fracture of that paradigm"),
 ("Kaplinsky", 2023, "ICT techno-economic paradigm transition", "fragmentation/lead-firm", "transition away from mass-production paradigm toward ICT paradigm"),
]
s4df = pd.DataFrame(s4, columns=["source", "year", "industry", "governance_type", "direction"])
s4df["basis"] = "documented instance in the staged corpus (NOT a population frequency)"
s4df["cap_note"] = S4_FIXED
s4df.to_csv(f"{RES}/s4_governance.csv", index=False)
# documented-instance counts (NOT population frequencies)
import collections
form_counts = collections.Counter()
for _, _, _, gt, _ in s4:
    g = gt.lower()
    if "modular" in g: form_counts["modular"] += 1
    if "relational" in g: form_counts["relational"] += 1
    if "market" in g: form_counts["market"] += 1
    if "hierarchy" in g: form_counts["hierarchy(origin)"] += 1
    if "captive" in g: form_counts["captive"] += 1
    if "scale" in g or "fragmentation" in g: form_counts["scale/power(paradigm)"] += 1
K["S4"] = {"documented_instances_in_staged_corpus": dict(form_counts),
           "reading": "modular/relational dominant in FORM (GHS/Sturgeon); captive-in-POWER added by Schwartz; corpus cannot measure population mix",
           "fixed_sentence": S4_FIXED, "weak_cell_cap": "S4 cells take at most weakly favors / weakly against / not separable"}

# ================= S7: district persistence =================
# reuse 001 C1 (Emilia-Romagna), read-only
c1 = pd.read_csv(f"{R001}/claim_C1.csv")
s7 = []
for _, r in c1.iterrows():
    s7.append({"metric": r["metric"], "year": int(r["year"]), "value": r["value"], "source": r["source"] + " (via 001, read-only)"})
s7.append({"metric": "ER_rel_EU27_index_2024", "year": 2024, "value": 116.8, "source": "Eurostat PPS (001 key_results)"})
s7.append({"metric": "Schwartz judgment", "year": 2024, "value": "districts = 'narrow slice of industrial output'; Italy no per-capita income rise after 2000; E-R relies on cheap immigrant labor", "source": "Schwartz 2024 (staged, attributed)"})
pd.DataFrame(s7).to_csv(f"{RES}/s7_districts.csv", index=False)
K["S7"] = {"ER_rel_IT_1980": 29.0, "ER_rel_IT_2024": 19.5, "ER_rel_EU27_2024": 116.8,
           "reading": "E-R persists and remains above EU/Italy mean but its RELATIVE advantage declined post-2000 (+29% -> +19.5% vs Italy; Italy stagnant); 'narrow slice' (Schwartz). partially measured."}

# ================= S6: demand-side institutions (ex-ante-decided documentary) =================
# developing-world demand diffusion from WDI mobile subs ONLY (vehicles indicator returned no data)
md = pd.read_csv("/workspace/eval/followup_staging/shared-data/worldbank-wdi/wdi_durables_diffusion_demand_side.csv")
mob = md[md.indicator == "IT.CEL.SETS.P2"].dropna(subset=["value"])
dev = {}
for iso in ["CHN", "IND", "VNM", "BRA", "MEX", "IDN"]:
    s = mob[mob.iso3 == iso].set_index("year")["value"]
    dev[iso] = {"1995": round(float(s[1995]), 1) if 1995 in s.index else None,
                "2023": round(float(s[2023]), 1) if 2023 in s.index else None}
institutions_required = [
    "international demand management / 'multinational Keynesianism' (constructed global demand-stabilizing institution)",
    "labor-share / capacity-apportionment mechanisms in the South (apportioning expansion of productive capacity among countries; global Keynesian demand coordination)",
]
exists_instead = [
    "WTO accession and rules-based market integration (market-led, not demand-coordinating)",
    "GVC participation without any demand-coordination institution",
    "post-2018 geopolitics: tariffs, friend-shoring, national industrial policy (decay handled by geopolitics, not by demand institutions)",
]
n_required = len(institutions_required)
n_exist = 0  # documentary: none of the demand-management institutions exist
# STUDY-WRITTEN result sentence (PS-B2a fill slot) -- NOT pre-written by the spec:
s6_result_sentence = ("The institutional half of Exit 1 is absent: none of the demand-management institutions P2-as-worded "
    "required (0 of 2) was constructed; developing-world mass consumption did arrive on market terms - mobile subscriptions "
    f"per 100 people rose from near zero in 1995 (China {dev['CHN']['1995']}, India {dev['IND']['1995']}, Viet Nam {dev['VNM']['1995']}) "
    f"to at or above saturation by 2023 (China {dev['CHN']['2023']}, India {dev['IND']['2023']}, Viet Nam {dev['VNM']['2023']}), "
    "but it was delivered by WTO-era market integration and private GVC "
    "participation, not by any 'multinational Keynesian' demand-coordinating institution - so the global mass-consumption "
    "market exists while the institutions that P&S's Exit 1 said would stabilize it do not.")
s6_md = f"""# S6 - Demand-side institutions (documentary absence test)

**Signature label: `ex-ante-decided (documentary)`** - the outcome is documentary and known at
spec time; this result sentence is written by the study (PS-B2a fill slot), not by the spec.

## Institutions P2-as-written (provisional anchor) requires
(from the inherited P2 anchor: Berger "apportion the expansion of productive capacity among the
advanced industrial countries" / "multinational Keynesian order"; Schwartz "improbable expansion of
mass production and thus Keynesian policy of demand management to the global level")

1. {institutions_required[0]}
2. {institutions_required[1]}

## What exists instead (each line sourced)
- {exists_instead[0]} (WTO GVC Report 2025, staged)
- {exists_instead[1]} (WTO GVC Report 2025 ch.2, staged)
- {exists_instead[2]} (WTO GVC Report 2025 ch.1, staged; Schwartz 2024: industrial policies "undoing the globalization trends of the ICT era")

## Developing-world demand diffusion (WDI mobile subscriptions per 100; vehicles indicator returned no data, PS-A2a)
{json.dumps(dev, indent=1)}

## Result (institutions required: {n_exist} of {n_required} exist)
{s6_result_sentence}
"""
open(f"{RES}/s6_institutions.md", "w").write(s6_md)
K["S6"] = {"n_required": n_required, "n_exist": n_exist, "institutions_required": institutions_required,
           "exists_instead": exists_instead, "dev_mobile": dev, "result_sentence": s6_result_sentence,
           "label": "ex-ante-decided (documentary)"}

# ================= E3 discriminator (PS-B3) =================
bds = K["S1b_BDS_manuf"]
# scale-economics decay (Kaplinsky/H-A paradigm fracture) = BOTH:
#  (i) plant re-concentration E3: US mean estab size rising AND small-estab emp share falling 2011->2023; EU concordant
us_reconc = (bds["mean_size_2023"] > bds["mean_size_2011"]) and (bds["small_share_2023"] < bds["small_share_2011"])
eu_reconc = (K["S1c_EU_SBS"]["small_lt50_share_2023"] < K["S1c_EU_SBS"]["small_lt50_share_2005"])
cond_i = us_reconc and eu_reconc
#  (ii) standardization reversal: consumer-goods share rising AT THE EXPENSE OF intermediates in WITS SoP E3 (2011->2023)
# consumer rose (30.59->32.73) but intermediates FLAT (20.72->20.81) -> consumer rose at expense of RAW, not intermediates
cons_2011, cons_2023 = 30.59, 32.73
int_2011, int_2023 = 20.72, 20.81
cond_ii = (cons_2023 > cons_2011) and (int_2023 < int_2011 - 0.5)  # intermediates must actually fall
scale_decay = cond_i and cond_ii
# geopolitics/ICT decay (H-C) = at least TWO of:
geo = {
 "i_us_china_30pct_below_trend_since_2018": True,   # WTO ch.1: grew ~30% slower than trade with rest of world
 "ii_rerouting_friendshoring_mexico_vietnam": True, # WTO ch.1: US import shares from Mexico & Viet Nam rose; connector economies
 "iii_services_digital_resilient_goods_plateau": True,  # WTO ch.1: 'Services have overtaken goods in GVC participation'; services more resilient 2021-24
}
geo_count = sum(geo.values())
geopol_decay = geo_count >= 2
# decision
if scale_decay and not geopol_decay:
    e3 = "scale-economics decay (reads as mass-production paradigm fracture, Kaplinsky)"
elif geopol_decay and not scale_decay:
    # one side partial (scale-decay (i) fired but (ii) did not) -> mixed per rule
    if cond_i and not cond_ii:
        e3 = "not separable this tick"
    else:
        e3 = "geopolitics/ICT decay (reads as H-C)"
else:
    e3 = "not separable this tick"
K["E3_discriminator"] = {
 "scale_decay_cond_i_plant_reconcentration": {"US": us_reconc, "EU_concordant": eu_reconc, "fired": cond_i},
 "scale_decay_cond_ii_standardization_reversal": {"consumer_2011_2023": [cons_2011, cons_2023],
     "intermediate_2011_2023": [int_2011, int_2023], "fired": cond_ii,
     "note": "consumer share rose but intermediates FLAT (rose at expense of raw, not intermediates) -> (ii) NOT met"},
 "scale_decay_fires_both": scale_decay,
 "geopolitics_ICT_decay": geo, "geo_count": geo_count, "geopol_fires": geopol_decay,
 "result": e3, "label_2011_boundary": SRC_2011,
 "per_side_tally": f"scale-decay: (i) plant re-concentration FIRED (US+EU), (ii) standardization reversal NOT fired -> scale side PARTIAL; geopolitics/ICT: {geo_count}/3 fired -> FIRES. One side partial + other firing -> 'not separable this tick'."}

# ================= EVIDENCE GRID =================
# cells per (signature, hypothesis): favors / weakly favors / against / weakly against / not separable / not measured
grid = []
def cell(S, hA, bA, hB, bB, hC, bC, ex_label="", preview=""):
    for hyp, c, b in [("H-A", hA, bA), ("H-B", hB, bB), ("H-C", hC, bC)]:
        grid.append({"signature": S, "hypothesis": hyp, "cell": c, "basis": b,
                     "ex_ante_label": ex_label, "preview_label": preview})

cell("S1 scale of production unit",
     "weakly favors", "hub concentration of manuf VA in China (8.5%->27.9% 2004-23) fits H-A; but Western plant-sizes fell long-run (mega-plant leg not met)",
     "against", "China hub concentration contradicts 'smallization everywhere'",
     "favors", "SPLITS by geography/chain position: China scale+integrated BOF mills vs Western smallization+EAF mini-mills; US smallization 1978-2011 then E3 re-concentration - the unit is not well-defined on one axis",
     preview=PREVIEW_STEEL)
cell("S2 standardization vs variety",
     "weakly favors", "smartphone/mobile diffusion = standardized global consumer product spreading (China 0.3->128.2/100); smartphone-as-Model-T",
     "weakly favors", "variety / mass-customization in named case lit (Shein, company-claimed)",
     "weakly favors", "standardization in components/tasks + variety in consumption = both layers",
     ex_label="weakly measured", preview="")
cell("S3 trade composition",
     "against", "final goods do not dominate; intermediates substantial; task/GVC trade present",
     "not separable", "differentiated intermediates between equals partly consistent but not decisive",
     "favors", "GVC/task-trade participation rose 1995-2011 then plateaued post-2011 (WTO Fig 2.8); regionalization+US-China ~30% decoupling since 2018 - H-C's rise-then-plateau + regionalization. WITS SoP intermediate share FLAT 19.45-24.92% whole window (narrower UNCTAD-SoP measure; SoP!=BEC seam)",
     preview=PREVIEW_SOP)
cell("S4 chain governance (WEAK-CELL CAP)",
     "weakly against", f"GHS cases moved AWAY from captive/hierarchy toward modular/relational. {S4_FIXED}",
     "weakly favors", f"GHS/Sturgeon document modular/relational forms. {S4_FIXED}",
     "weakly favors", f"Schwartz three-layer lead-firm-power chain (captive in power) + modular form = H-C synthesis. {S4_FIXED}")
cell("S5 skill content (DECLARED WEAK)",
     "not separable", "fixed by declaration (mirror of D2); one literature paragraph only",
     "not separable", "fixed by declaration",
     "not separable", "fixed by declaration",
     ex_label="fixed by declaration")
cell("S6 demand-side institutions",
     "against", "P2-as-written required constructed global demand management; it does not exist. Market-led scale without institutions = 'half of Exit 1' (partial cell)",
     "against", "no regional demand institutions balancing competition/cooperation; WTO is market-led",
     "favors", "market-led integration, no demand institutions, decay via geopolitics/tariffs/industrial policy - exactly H-C",
     ex_label="ex-ante-decided (documentary)")
cell("S7 district persistence (partially measured)",
     "weakly favors", "districts a 'narrow slice' (Schwartz); E-R relative advantage declined post-2000 (+29%->+19.5% vs Italy) = partial marginalization",
     "weakly against", "relative decline post-2000 undercuts 'thriving exporters inside GVCs' (pre-declared against-H-B)",
     "weakly favors", "E-R persists where it holds design/IP-intensive niches; Pearl River Delta the biggest district - persistence tied to position")
gridf = pd.DataFrame(grid)
# effective denominator: live cells = S1,S2,S3,S4(capped weak),S7 (5); S5 fixed, S6 ex-ante
live_sigs = ["S1 scale of production unit", "S2 standardization vs variety", "S3 trade composition",
             "S4 chain governance (WEAK-CELL CAP)", "S7 district persistence (partially measured)"]
def count_full_favors(hyp):
    sub = gridf[(gridf.hypothesis == hyp) & (gridf.signature.isin(live_sigs))]
    # S4 capped: never counts as full favor
    n = 0
    for _, r in sub.iterrows():
        if r["cell"] == "favors" and not r["signature"].startswith("S4"):
            n += 1
    return n
tallies = {}
for hyp in ["H-A", "H-B", "H-C"]:
    sub = gridf[gridf.hypothesis == hyp]
    tallies[hyp] = {"favors": int((sub.cell == "favors").sum()),
                    "weakly favors": int((sub.cell == "weakly favors").sum()),
                    "against": int((sub.cell == "against").sum()),
                    "weakly against": int((sub.cell == "weakly against").sum()),
                    "not separable": int((sub.cell == "not separable").sum()),
                    "full_favors_on_live_cells": count_full_favors(hyp)}
# effective-denominator statement
eff_denom = ("Effective denominator: with S5 fixed by declaration and S6 ex-ante-decided (documentary), there are 5 live "
    "cells (S1, S2, S3, S4-capped-weak, S7). Because S4 is capped to at most a weak cell, each hypothesis can reach at most "
    "k=4 FULL favors on live cells (from S1, S2, S3, S7). Read against the >=4 bars: H-A full-favors="
    f"{tallies['H-A']['full_favors_on_live_cells']}, H-B={tallies['H-B']['full_favors_on_live_cells']}, "
    f"H-C={tallies['H-C']['full_favors_on_live_cells']}.")
gridf.to_csv(f"{RES}/evidence_table.csv", index=False)
K["tallies"] = tallies
K["effective_denominator"] = eff_denom

# ================= VERDICT =================
# conditions
hA_cond = (tallies["H-A"]["full_favors_on_live_cells"] >= 4 and
           gridf[(gridf.signature.str.startswith("S1")) & (gridf.hypothesis == "H-A")].cell.iloc[0] == "favors" and
           gridf[(gridf.signature.str.startswith("S2")) & (gridf.hypothesis == "H-A")].cell.iloc[0] == "favors")
hB_cond = (tallies["H-B"]["full_favors_on_live_cells"] >= 4)  # incl (S2 or S7)
hC_full = (tallies["H-C"]["full_favors_on_live_cells"] >= 4 and
           gridf[(gridf.signature.str.startswith("S3")) & (gridf.hypothesis == "H-C")].cell.iloc[0] == "favors")
# split condition (dichotomy fails): S1 splits AND S4 mixed AND no hypothesis reaches >=4
s1_splits = gridf[(gridf.signature.str.startswith("S1")) & (gridf.hypothesis == "H-C")].cell.iloc[0] == "favors"
s4_mixed = True  # S4 shows mixed governance within chains (captive in power, modular in form)
no_hyp_4 = not (hA_cond or hB_cond or hC_full)
split_cond = s1_splits and s4_mixed and no_hyp_4
s3_favors_hC = gridf[(gridf.signature.str.startswith("S3")) & (gridf.hypothesis == "H-C")].cell.iloc[0] == "favors"
# resolution
if hA_cond:
    verdict = "globalization as new mass production - supported with the institutional half absent"
elif hB_cond:
    verdict = "flexible specialization at global scale - supported"
elif hC_full or (split_cond and s3_favors_hC):
    verdict = "neither - the unbundling reading"
elif split_cond:
    verdict = "the dichotomy fails"
else:
    verdict = "uninformative at this tick"
K["verdict"] = {"verdict": verdict,
    "conditions": {"hA_S1andS2_and_4favors": hA_cond, "hB_4favors": hB_cond, "hC_4favors_inclS3": hC_full,
                   "split_condition_dichotomy_fails": split_cond, "s3_favors_hC": s3_favors_hC,
                   "s1_splits": s1_splits, "s4_mixed": s4_mixed, "no_hypothesis_reaches_4": no_hyp_4},
    "route": "H-C via the split condition (S1 splits + S4 mixed + no hypothesis reaches >=4) PLUS S3 favoring H-C",
    "dichotomy_fails_also_satisfied": split_cond,
    "threshold_sensitive": True,
    "threshold_note": "H-C reaches only 2 full favors on live cells (S1, S3), below the >=4 bar; the verdict rests on the split+S3 route with several weak contributing cells (S2, S4-capped, S7) -> threshold-sensitive."}

json.dump(K, open(f"{RES}/_grid_keyresults.json", "w"), indent=1, default=str)
print("VERDICT:", verdict)
print("tallies:", json.dumps(tallies, indent=1))
print("E3:", e3)
print("eff_denom:", eff_denom)
print("split_cond:", split_cond, "| s3_favors_hC:", s3_favors_hC, "| hC_full:", hC_full)
