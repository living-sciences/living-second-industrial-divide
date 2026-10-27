import pandas as pd, numpy as np, json, os

SD = "/workspace/eval/followup_staging/shared-data"
R001 = "/workspace/eval/followup/001-001-claims-and-predictions/results"
RES = "/workspace/eval/followup/002-002-globalization-test/results"
os.makedirs(RES, exist_ok=True)
K = {}

PREVIEW_SOP = "[PREVIEW-KNOWN: WLD SoP2 export share 19.45-24.92%, flat 1988-2023, stated at spec time]"
PREVIEW_STEEL = "[PREVIEW-KNOWN: China ~91.6% BOF / US majority-EAF, worldsteel 2025, stated at spec time]"
SRC_2011 = "[SOURCE-DERIVED: WTO GVC Report 2025 plateau finding]"

# ================= S1: scale of the production unit =================
# (a) country shares of world manufacturing VA (WDI NV.IND.MANF.CD, current USD)
d = pd.read_csv(f"{SD}/worldbank-wdi/wdi_manufacturing_trade_1960_2025.csv")
va = d[d.indicator == "NV.IND.MANF.CD"].dropna(subset=["value"])
wld = va[va.iso3 == "WLD"].set_index("year")["value"]
s1a_rows = []
for iso, name in [("CHN", "China"), ("USA", "United States"), ("DEU", "Germany"),
                  ("JPN", "Japan"), ("KOR", "Korea")]:
    s = va[va.iso3 == iso].set_index("year")["value"]
    for y in sorted(set(s.index) & set(wld.index)):
        if 2004 <= y <= 2023:
            s1a_rows.append({"series": "share_world_manuf_VA_pct", "iso3": iso, "country": name,
                             "year": int(y), "value": round(100 * s[y] / wld[y], 2),
                             "source": "WDI NV.IND.MANF.CD (staged)"})
s1a = pd.DataFrame(s1a_rows)
s1a.to_csv(f"{RES}/s1_scale.csv", index=False)
# headline shares
def sh(iso, y):
    r = s1a[(s1a.iso3 == iso) & (s1a.year == y)]
    return float(r.value.iloc[0]) if len(r) else None
K["S1a_VA_share"] = {"CHN_2004": sh("CHN", 2004), "CHN_2011": sh("CHN", 2011), "CHN_2023": sh("CHN", 2023),
                     "USA_2004": sh("USA", 2004), "USA_2011": sh("USA", 2011), "USA_2021": sh("USA", 2021),
                     "note_pre2004_CHN": "pre-2004 China VA-share cells were specced from recency-research.md 5.4 literature values; that file is NOT in this run's staged inputs, so pre-2004 China cells are NOT substituted from memory (deviation). WDI staged series begins 2004."}

# (b) US manufacturing establishment size (reuse 001 D1 manufacturing, read-only)
bds = pd.read_csv(f"{R001}/claim_D1_manufacturing.csv")
bds.to_csv(f"{RES}/s1_us_estab_manuf.csv", index=False)  # local copy for the record
def bds_at(y, col):
    return float(bds[bds.year == y][col].iloc[0])
K["S1b_BDS_manuf"] = {"small_share_1978": bds_at(1978, "small_estab_emp_share"),
                      "small_share_2011": bds_at(2011, "small_estab_emp_share"),
                      "small_share_2023": bds_at(2023, "small_estab_emp_share"),
                      "mean_size_1978": bds_at(1978, "mean_estab_size"),
                      "mean_size_2011": bds_at(2011, "mean_estab_size"),
                      "mean_size_2023": bds_at(2023, "mean_estab_size"),
                      "source": "001 results/claim_D1_manufacturing.csv (BDS 2023, reused read-only)"}

# (c) Eurostat SBS size-class, two panels
def eurostat_series(path, indic_dim, indic_val, size_val, geo="EU27_2020"):
    o = json.load(open(path)); dim = o["dimension"]; size = o["size"]; ids = o["id"]; val = o["value"]
    idx = {k: dim[k]["category"]["index"] for k in ids}
    out = {}
    for t in idx["time"]:
        pos = []
        for dcode in ids:
            if dcode == "time":
                key = t
            elif dcode == indic_dim:
                key = indic_val
            elif dcode == "size_emp":
                key = size_val
            elif dcode == "geo":
                key = geo
            else:
                key = list(idx[dcode].keys())[0]
            pos.append(idx[dcode][key])
        flat = 0
        for i, p in enumerate(pos):
            stride = 1
            for s in size[i+1:]:
                stride *= s
            flat += p * stride
        v = val.get(str(flat))
        if v is not None:
            out[int(t)] = v
    return out
# Panel 1 (2005-2020): V16110 persons employed, small = 0-9+10-19+20-49, large = GE250, total = TOTAL
p1 = f"{SD}/eurostat/sbs_sc_ind_r2_manufacturing_sizeclass.json"
emp_tot = eurostat_series(p1, "indic_sb", "V16110", "TOTAL")
small_bands = ["0-9", "10-19", "20-49"]
s1c_rows = []
for y in sorted(emp_tot):
    tot = emp_tot[y]
    small = sum(eurostat_series(p1, "indic_sb", "V16110", b).get(y, 0) for b in small_bands)
    large = eurostat_series(p1, "indic_sb", "V16110", "GE250").get(y, 0)
    s1c_rows.append({"panel": "2005-2020 (NACE C, V16110 persons employed)", "geo": "EU27_2020", "year": y,
                     "small_lt50_emp_share": round(100*small/tot, 2), "large_ge250_emp_share": round(100*large/tot, 2),
                     "source": "Eurostat sbs_sc_ind_r2 (staged)"})
# Panel 2 (2021+): EMP_NR
p2 = f"{SD}/eurostat/sbs_sc_ovw_manufacturing_sizeclass.json"
emp_tot2 = eurostat_series(p2, "indic_sbs", "EMP_NR", "TOTAL")
for y in sorted(emp_tot2):
    tot = emp_tot2[y]
    small = sum(eurostat_series(p2, "indic_sbs", "EMP_NR", b).get(y, 0) for b in small_bands)
    large = eurostat_series(p2, "indic_sbs", "EMP_NR", "GE250").get(y, 0)
    s1c_rows.append({"panel": "2021+ (NACE C, EMP_NR) [BREAK: successor dataset]", "geo": "EU27_2020", "year": y,
                     "small_lt50_emp_share": round(100*small/tot, 2), "large_ge250_emp_share": round(100*large/tot, 2),
                     "source": "Eurostat sbs_sc_ovw (staged)"})
pd.DataFrame(s1c_rows).to_csv(f"{RES}/s1_eu_sizeclass.csv", index=False)
p1rows = [r for r in s1c_rows if r["panel"].startswith("2005")]
p2rows = [r for r in s1c_rows if r["panel"].startswith("2021")]
# PS-PROV-2 correction (study 003): the EU27_2020 SBS aggregate is absent pre-2011 in the
# staged sbs_sc_ind_r2 file, so p1rows[0] is year 2011 (NOT 2005). The first-value keys are
# therefore labeled _2011; "2005-2020" (the panel name) is the dataset's nominal span only.
K["S1c_EU_SBS"] = {"small_lt50_share_2011": p1rows[0]["small_lt50_emp_share"],   # p1rows[0].year == 2011
                   "small_lt50_share_2020": p1rows[-1]["small_lt50_emp_share"],
                   "small_lt50_share_2021": p2rows[0]["small_lt50_emp_share"],
                   "small_lt50_share_2023": [r for r in p2rows if r["year"] == 2023][0]["small_lt50_emp_share"],
                   "large_ge250_share_2011": p1rows[0]["large_ge250_emp_share"],  # p1rows[0].year == 2011
                   "large_ge250_share_2020": p1rows[-1]["large_ge250_emp_share"],
                   "note": "two panels, dataset break 2020/2021 (indicator + size-class codes change). First-value keys labeled _2011 (EU27_2020 SBS absent pre-2011; PS-PROV-2)."}

# (d) INDSTAT -> honest exclusion
indstat_exists = os.path.isdir(f"{SD}/unido-indstat")
K["S1d_INDSTAT"] = {"staged": indstat_exists,
                    "status": "excluded (H3): UNIDO INDSTAT is registration-gated; S1 verdict rests on US/EU size series plus hub-share data. No workaround." if not indstat_exists else "staged"}

# (e) steel geography split + mega-plant descriptive row
s1_steel = [
    {"series": "crude_steel_pct_BOF", "geo": "China", "year": 2024, "value": 89.8, "source": "worldsteel World Steel in Figures 2025 (staged)", "label": PREVIEW_STEEL},
    {"series": "crude_steel_pct_EAF", "geo": "China", "year": 2024, "value": 10.2, "source": "worldsteel 2025 (staged)", "label": PREVIEW_STEEL},
    {"series": "crude_steel_pct_BOF", "geo": "United States", "year": 2024, "value": 28.2, "source": "worldsteel 2025 (staged)", "label": PREVIEW_STEEL},
    {"series": "crude_steel_pct_EAF", "geo": "United States", "year": 2024, "value": 71.8, "source": "worldsteel 2025 (staged)", "label": PREVIEW_STEEL},
]
pd.DataFrame(s1_steel).to_csv(f"{RES}/s1_steel_split.csv", index=False)
K["S1_steel"] = {"CHN_BOF_pct": 89.8, "USA_EAF_pct": 71.8, "label": PREVIEW_STEEL,
                 "note": "spec PREVIEW label stated China ~91.6% BOF (the 91.6 is the Austria row in the staged table); computed China BOF = 89.8%. US majority-EAF confirmed (71.8%)."}
s1_megaplant = {"row": "mega-plant descriptive (DESCRIPTIVE ONLY, NO verdict weight)",
                "note": "Foxconn/EMS scale (Zhengzhou 'iPhone City' employing ~200k-350k at peak) illustrates assembly-giant concentration; public-press figures, descriptive only per spec."}
K["S1e_megaplant"] = s1_megaplant

# ================= S2: standardization vs variety =================
w = pd.read_csv(f"{SD}/wits-intermediates/wits_unctad_sop_product_shares.csv")
wx = w[(w.reporter == "WLD") & (w.indicator == "XPRT-PRDCT-SHR")].pivot(index="year", columns="product", values="value")
sop_names = {"UNCTAD-SoP1": "raw", "UNCTAD-SoP2": "intermediate", "UNCTAD-SoP3": "consumer", "UNCTAD-SoP4": "capital"}
s2_rows = []
for y in [1988, 1995, 2000, 2011, 2023]:
    for c in ["UNCTAD-SoP1", "UNCTAD-SoP2", "UNCTAD-SoP3", "UNCTAD-SoP4"]:
        s2_rows.append({"measure": "WLD export share by SoP class (%)", "sop_class": sop_names[c],
                        "year": y, "value": round(float(wx.loc[y, c]), 2),
                        "source": "WITS UNCTAD-SoP (staged); SoP!=BEC seam: trend only",
                        "label": PREVIEW_SOP if c == "UNCTAD-SoP2" else ""})
# mobile subscriptions diffusion (standardized global consumer product -> smartphone-as-Model-T)
md = pd.read_csv(f"{SD}/worldbank-wdi/wdi_durables_diffusion_demand_side.csv")
mob = md[md.indicator == "IT.CEL.SETS.P2"].dropna(subset=["value"])
for iso, name in [("CHN", "China"), ("IND", "India"), ("VNM", "Viet Nam"), ("BRA", "Brazil"),
                  ("MEX", "Mexico"), ("IDN", "Indonesia"), ("USA", "United States"), ("DEU", "Germany")]:
    s = mob[mob.iso3 == iso].set_index("year")["value"]
    for y in [1995, 2000, 2011, 2023]:
        if y in s.index:
            s2_rows.append({"measure": "mobile_subscriptions_per_100", "sop_class": name, "year": y,
                            "value": round(float(s[y]), 1), "source": "WDI IT.CEL.SETS.P2 (staged)", "label": ""})
# case-literature row (labelled)
s2_rows.append({"measure": "case-literature (direction only, weakly measured)", "sop_class": "Shein ultra-fast fashion",
                "year": 2023, "value": None, "source": "company-claimed / literature (SKU/batch data do not exist at scale)",
                "label": "company-claimed"})
pd.DataFrame(s2_rows).to_csv(f"{RES}/s2_standardization.csv", index=False)
K["S2"] = {"SoP2_interm_1988": round(float(wx.loc[1988, "UNCTAD-SoP2"]), 2),
           "SoP2_interm_2023": round(float(wx.loc[2023, "UNCTAD-SoP2"]), 2),
           "SoP2_min": round(float(wx["UNCTAD-SoP2"].min()), 2), "SoP2_max": round(float(wx["UNCTAD-SoP2"].max()), 2),
           "SoP3_consumer_1988": round(float(wx.loc[1988, "UNCTAD-SoP3"]), 2),
           "SoP3_consumer_2023": round(float(wx.loc[2023, "UNCTAD-SoP3"]), 2),
           "mob_CHN_1995_2023": [round(float(mob[mob.iso3=='CHN'].set_index('year')['value'][1995]),1),
                                 round(float(mob[mob.iso3=='CHN'].set_index('year')['value'][2023]),1)],
           "label": "weakly measured; smartphone/mobile diffusion is the measurable leg"}

# ================= S3: trade composition =================
# WITS SoP trend by era + WTO fallback participation (TiVA degraded)
s3_rows = []
for y in [1988, 1995, 2000, 2011, 2023]:
    s3_rows.append({"measure": "WLD intermediate (SoP2) export share %", "year": y,
                    "value": round(float(wx.loc[y, "UNCTAD-SoP2"]), 2),
                    "source": "fallback (TiVA endpoint degraded, verified 2026-10-27 and at run time); WITS UNCTAD-SoP staged trend",
                    "label": PREVIEW_SOP})
# WTO GVC participation phases (Figure 2.8 / Box 2.1, ch.2) + GVC-trade share peak (ch.1)
wto = [
    {"measure": "GVC-related trade share of total trade (%)", "year": 2022, "value": 48.0,
     "source": "WTO GVC Report 2025 ch.1 (staged, p.~7): 'peak of 48% in 2022'", "label": SRC_2011},
    {"measure": "GVC-related trade share of total trade (%)", "year": 2024, "value": 46.3,
     "source": "WTO GVC Report 2025 ch.1 (staged): 'declined ... to 46.3% in 2024'", "label": SRC_2011},
    {"measure": "GVC participation phase (TiVA via WTO Fig 2.8)", "year": "1995-2011", "value": "broad-based gains (expansion/deepening)",
     "source": "WTO GVC Report 2025 ch.2 Box 2.1 / Fig 2.8 (staged): rapid global production expansion", "label": SRC_2011},
    {"measure": "GVC participation phase (TiVA via WTO Fig 2.8)", "year": "2011-2022", "value": "backward modest, forward flat, aggregate broadly unchanged (plateau)",
     "source": "WTO GVC Report 2025 ch.2 (staged): 'post-2011 decade ... stagnation and divergence'", "label": SRC_2011},
]
s3_rows += wto
pd.DataFrame(s3_rows).to_csv(f"{RES}/s3_composition.csv", index=False)
K["S3"] = {"SoP2_flat": [K["S2"]["SoP2_1988" if False else "SoP2_interm_1988"], K["S2"]["SoP2_interm_2023"]],
           "SoP2_min_max": [K["S2"]["SoP2_min"], K["S2"]["SoP2_max"]],
           "wto_gvc_share_peak_2022": 48.0, "wto_gvc_share_2024": 46.3,
           "participation": "rose 1995-2011 then plateaued post-2011 (WTO Fig 2.8); US-China bilateral ~30% below trend since 2018 tariffs (WTO ch.1)",
           "source_label": "fallback (TiVA endpoint degraded 2026-10-27 and at run time)"}

print("S1-S3 built. key dump:")
print(json.dumps({k: K[k] for k in ["S1a_VA_share","S1b_BDS_manuf","S1c_EU_SBS","S1_steel","S2","S3"]}, indent=1, default=str)[:2500])
json.dump(K, open(f"{RES}/_s1s3_keyresults.json", "w"), indent=1, default=str)
