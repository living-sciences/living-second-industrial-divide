import pandas as pd, json
SD = "/workspace/eval/followup_staging/shared-data"
out = {}

# OWID
owid = pd.read_csv(f"{SD}/owid-durables/us_household_technology_adoption.csv")
col = owid.columns[-1]
ents = {}
for e in ["Automobile","Household refrigerator","Washing machine","Refrigerator","Washer","Television","Colour TV"]:
    sub = owid[owid.entity==e]
    if len(sub):
        ents[e] = {"n":len(sub),"ymin":int(sub.year.min()),"ymax":int(sub.year.max()),
                   "has_1973": bool((sub.year==1973).any())}
out["owid_entities"] = ents
out["owid_all_entities"] = sorted(owid.entity.unique().tolist())

# BDS ez
bds = pd.read_csv(f"{SD}/census-bds/bds2023_ez.csv")
out["bds_ez"] = {"ymin":int(bds.year.min()),"ymax":int(bds.year.max()),
                 "esize_values": sorted(bds.esize.unique().tolist())}
# BDS sec
bdss = pd.read_csv(f"{SD}/census-bds/bds2023_sec_ez.csv")
out["bds_sec"] = {"ymin":int(bdss.year.min()),"ymax":int(bdss.year.max()),
                  "sectors": sorted(bdss.sector.unique().tolist()) if 'sector' in bdss.columns else bdss.columns.tolist()[:6]}

# WITS
wits = pd.read_csv(f"{SD}/wits-intermediates/wits_unctad_sop_product_shares.csv")
out["wits"] = {"ymin":int(wits.year.min()),"ymax":int(wits.year.max()),
               "reporters":sorted(wits.reporter.unique().tolist()),
               "indicators":sorted(wits.indicator.unique().tolist()),
               "products":sorted(wits['product'].unique().tolist())}

# Eurostat E-R
er = json.load(open(f"{SD}/eurostat/nama_10r_2gdp_emilia_romagna.json"))
dims = er.get("dimension",{})
out["eurostat_er_dims"] = {k:list(v.get("category",{}).get("index",{}).keys()) for k,v in dims.items() if 'category' in v}

# WDI
wdi = pd.read_csv(f"{SD}/worldbank-wdi/wdi_manufacturing_trade_1960_2025.csv")
out["wdi_manuf_cols"] = wdi.columns.tolist()
out["wdi_manuf_head"] = wdi.head(3).to_dict('records')

print(json.dumps(out, indent=2, default=str))
