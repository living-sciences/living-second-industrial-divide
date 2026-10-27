import pandas as pd, numpy as np, json, os
SD="/workspace/eval/followup_staging/shared-data"
DATA="/workspace/eval/followup/001-001-claims-and-predictions/workspace/data"
RES="/workspace/eval/followup/001-001-claims-and-predictions/results"
os.makedirs(RES,exist_ok=True)
K={}  # key results

# ---------- B1 durables saturation ----------
o=pd.read_csv(f"{SD}/owid-durables/us_household_technology_adoption.csv")
col=o.columns[-1]
def owid(e,y):
    s=o[o.entity==e].set_index('year')[col]; return float(s.loc[y])
durs={"Automobile":("OWID",owid("Automobile",1973),owid("Automobile",1984)),
      "Household refrigerator":("OWID",owid("Household refrigerator",1973),owid("Household refrigerator",1984)),
      "Washing machine":("OWID",owid("Washing machine",1973),owid("Washing machine",1984)),
      "TV":("Census HS-42",96.4,98.1)}
b1rows=[]; npass=0; any_growth_fail=False
for d,(src,p73,p84) in durs.items():
    ratio=p73/p84; growth=(p84-p73)/(1984-1973)
    pass_ratio=ratio>=0.9; pass_growth=growth<=1.0; passed=pass_ratio and pass_growth
    if not pass_growth: any_growth_fail=True
    if passed: npass+=1
    b1rows.append({"durable":d,"source":src,"pen_1973":round(p73,1),"pen_1984":round(p84,1),
                   "ratio_73_84":round(ratio,3),"mean_growth_pp_yr":round(growth,3),
                   "pass_ratio":pass_ratio,"pass_growth":pass_growth,"saturated_by_early70s":passed})
if npass>=3 and not any_growth_fail: b1v="supported"
elif npass==2: b1v="partially supported"
else: b1v="contradicted"
pd.DataFrame(b1rows).to_csv(f"{RES}/claim_B1.csv",index=False)
K["B1"]={"verdict":b1v,"n_pass":npass,"table":b1rows}

# ---------- B3 productivity slowdown ----------
def fred_annual(fn,coln):
    df=pd.read_csv(f"{DATA}/{fn}"); df['year']=pd.to_datetime(df['observation_date']).dt.year
    return df.groupby('year')[coln].mean()
lp=fred_annual("fred_OPHNFB.csv","OPHNFB")   # labor productivity (nonfarm business) - successor to OPHMFG
tfp=fred_annual("fred_MFPNFBS.csv","MFPNFBS")# TFP
def mean_growth(series,y0,y1):
    s=series[(series.index>=y0)&(series.index<=y1)].sort_index()
    g=np.log(s).diff().dropna()*100  # approx % per year
    return float(g.mean())
b3={}
for name,s in [("labor_productivity_OPHNFB",lp),("TFP_MFPNFBS",tfp)]:
    pre=mean_growth(s,1950,1973); post7384=mean_growth(s,1974,1984); postall=mean_growth(s,1974,int(s.index.max()))
    b3[name]={"mean_growth_1950_1973":round(pre,3),"mean_growth_1974_1984":round(post7384,3),
              "mean_growth_1974_latest":round(postall,3),"latest_year":int(s.index.max()),
              "slowdown_73":pre>post7384}
slow_both = b3["labor_productivity_OPHNFB"]["slowdown_73"] and b3["TFP_MFPNFBS"]["slowdown_73"]
b3v="supported" if slow_both else ("partially supported" if (b3["labor_productivity_OPHNFB"]["slowdown_73"] or b3["TFP_MFPNFBS"]["slowdown_73"]) else "contradicted")
# claim CSV: annual series both
lpf=lp.rename("labor_prod_OPHNFB"); tfpf=tfp.rename("TFP_MFPNFBS")
pd.concat([lpf,tfpf],axis=1).reset_index().to_csv(f"{RES}/claim_B3.csv",index=False)
K["B3"]={"verdict":b3v,"detail":b3}

# ---------- C1 Emilia-Romagna relative income ----------
# historical (Rinaldi, verbatim from staged PDF): rank 7th (1951); +29% vs Italy mean (1980); 2nd place, +25% (1995)
er=json.load(open(f"{SD}/eurostat/nama_10r_2gdp_emilia_romagna.json"))
val=er['value']; dim=er['dimension']; size=er['size']; ids=er['id']
idx={k:list(dim[k]['category']['index'].keys()) for k in ids}
def eu_val(geo,unit,time):
    pos=[idx['freq'].index('A'),idx['unit'].index(unit),idx['geo'].index(geo),idx['time'].index(time)]
    flat=0
    for i,p in enumerate(pos):
        stride=1
        for s in size[i+1:]: stride*=s
        flat+=p*stride
    return val.get(str(flat))
c1_modern={}
for t in ['2000','2024']:
    it=eu_val('IT','PPS_EU27_2020_HAB',t); erv=eu_val('ITH5','PPS_EU27_2020_HAB',t); eu=eu_val('EU27_2020','PPS_EU27_2020_HAB',t)
    c1_modern[t]={"ER_pps":erv,"IT_pps":it,"EU_pps":eu,
                  "ER_rel_IT_pct": round(100*(erv/it-1),1) if erv and it else None,
                  "ER_rel_EU_index": round(100*erv/eu,1) if erv and eu else None}
c1_hist={"1951":"7th place among Italian regions (Rinaldi, staged)","1980":"+29% vs Italian per-capita mean (Rinaldi)","1995":"2nd place; +25% vs Italian mean (Rinaldi)"}
# verdict: rises through 1970s, magnitude +29% by 1980 matches spec reading
c1v="supported"
pd.DataFrame([{"year":1951,"metric":"rank_italy","value":7,"source":"Rinaldi"},
              {"year":1980,"metric":"pct_above_italy_mean","value":29,"source":"Rinaldi"},
              {"year":1995,"metric":"pct_above_italy_mean","value":25,"source":"Rinaldi(rank 2nd)"},
              {"year":2000,"metric":"ER_rel_IT_pct","value":c1_modern['2000']['ER_rel_IT_pct'],"source":"Eurostat PPS"},
              {"year":2024,"metric":"ER_rel_IT_pct","value":c1_modern['2024']['ER_rel_IT_pct'],"source":"Eurostat PPS"},
             ]).to_csv(f"{RES}/claim_C1.csv",index=False)
K["C1"]={"verdict":c1v,"historical":c1_hist,"modern":c1_modern}

# ---------- D1 plant-size reversal (BDS) ----------
def bds_metrics(df):
    df=df.copy()
    df['emp']=pd.to_numeric(df['emp'],errors='coerce')
    df['estabs']=pd.to_numeric(df['estabs'],errors='coerce')
    small={"a) 1 to 4","b) 5 to 9","c) 10 to 19","d) 20 to 99"}
    rows=[]
    for y,g in df.groupby('year'):
        tot_emp=g['emp'].sum(); tot_est=g['estabs'].sum()
        small_emp=g[g['esize'].isin(small)]['emp'].sum()
        rows.append({"year":int(y),"small_estab_emp_share":round(100*small_emp/tot_emp,2),
                     "mean_estab_size":round(tot_emp/tot_est,2),"total_emp":int(tot_emp),"total_estabs":int(tot_est)})
    return pd.DataFrame(rows).sort_values('year')
ez=pd.read_csv(f"{SD}/census-bds/bds2023_ez.csv")
econ=bds_metrics(ez)
sec=pd.read_csv(f"{SD}/census-bds/bds2023_sec_ez.csv")
man=bds_metrics(sec[sec['sector'].astype(str)=="31-33"])
econ.to_csv(f"{RES}/claim_D1_economy.csv",index=False)
man.to_csv(f"{RES}/claim_D1_manufacturing.csv",index=False)
def chg(df):
    a=df[df.year==1978].iloc[0]; b=df[df.year==2023].iloc[0]
    return {"share_1978":a.small_estab_emp_share,"share_2023":b.small_estab_emp_share,
            "share_up":b.small_estab_emp_share>a.small_estab_emp_share,
            "meansize_1978":a.mean_estab_size,"meansize_2023":b.mean_estab_size,
            "meansize_down":b.mean_estab_size<a.mean_estab_size}
d1e=chg(econ); d1m=chg(man)
reversal = (d1e["share_up"] and d1e["meansize_down"] and d1m["share_up"] and d1m["meansize_down"])
d1_story = "reversal confirmed" if reversal else ("qualified" if (d1e["share_up"] or d1m["share_up"]) else "reversal not found")
K["D1"]={"verdict_cell":"not-checkable (attribution)","data_story":d1_story,"economy":d1e,"manufacturing":d1m}

# ---------- P1 manufacturing employment & VA shares ----------
man_emp=pd.read_csv(f"{DATA}/fred_MANEMP.csv"); pay=pd.read_csv(f"{DATA}/fred_PAYEMS.csv")
for d in (man_emp,pay): d['year']=pd.to_datetime(d['observation_date']).dt.year
me=man_emp.groupby('year')['MANEMP'].mean(); pe=pay.groupby('year')['PAYEMS'].mean()
usshare=(100*me/pe).rename("US_manuf_emp_share_pct")
wdi=pd.read_csv(f"{SD}/worldbank-wdi/wdi_manufacturing_trade_1960_2025.csv")
va=wdi[wdi.indicator=="NV.IND.MANF.ZS"]
def va_series(iso):
    s=va[va.iso3==iso].set_index('year')['value']; return s
p1={}
for iso in ["USA","DEU","JPN"]:
    s=va_series(iso)
    def near(s,y):
        s2=s.dropna();
        if y in s2.index: return float(s2.loc[y])
        c=s2.index[(s2.index-y).to_series().abs().values.argmin()] if len(s2) else None
        return float(s2.loc[c]) if c is not None else None
    p1[iso]={"va_share_1984":round(near(s,1984),2) if near(s,1984) else None,
             "va_share_2023":round(near(s,2023),2) if near(s,2023) else None}
p1["US_emp_share"]={"1984":round(float(usshare.loc[1984]),2),"2025":round(float(usshare.loc[2025]),2),
                    "1970":round(float(usshare.loc[1970]),2) if 1970 in usshare.index else None}
# recovery? shares should NOT recover toward pre-1973. Check 1984->2023/25 all down
va_down=all((p1[i]["va_share_2023"]<p1[i]["va_share_1984"]) for i in ["USA","DEU","JPN"])
emp_down=p1["US_emp_share"]["2025"]<p1["US_emp_share"]["1984"]
p1v="supported" if (va_down and emp_down) else "partially supported"
pd.DataFrame([{"iso":i,**p1[i]} for i in ["USA","DEU","JPN"]]).to_csv(f"{RES}/claim_P1_va.csv",index=False)
usshare.reset_index().to_csv(f"{RES}/claim_P1_us_empshare.csv",index=False)
K["P1"]={"verdict":p1v,"va_down_all3":va_down,"us_emp_down":emp_down,"detail":p1}

# ---------- C2/C3 BW modern (data story only) ----------
bw=json.load(open(f"{DATA}/eurostat_bw.json"))
bwval=bw['value']; bwdim=bw['dimension']; bwsize=bw['size']; bwids=bw['id']
bwidx={k:list(bwdim[k]['category']['index'].keys()) for k in bwids}
def bwv(geo,unit,time):
    pos=[bwidx['freq'].index('A') if 'freq' in bwidx else 0, bwidx['unit'].index(unit),bwidx['geo'].index(geo),bwidx['time'].index(time)]
    # recompute flat index
    pos=[]
    for k in bwids:
        if k=='freq': pos.append(bwidx['freq'].index('A'))
        elif k=='unit': pos.append(bwidx['unit'].index(unit))
        elif k=='geo': pos.append(bwidx['geo'].index(geo))
        elif k=='time': pos.append(bwidx['time'].index(time))
    flat=0
    for i,p in enumerate(pos):
        stride=1
        for s in bwsize[i+1:]: stride*=s
        flat+=p*stride
    return bwval.get(str(flat))
c23={}
for t in ['2000','2024']:
    de1=bwv('DE1','PPS_EU27_2020_HAB',t); de=bwv('DE','PPS_EU27_2020_HAB',t); eu=bwv('EU27_2020','PPS_EU27_2020_HAB',t)
    c23[t]={"BW_pps":de1,"DE_pps":de,"EU_pps":eu,"BW_rel_EU_index":round(100*de1/eu,1) if de1 and eu else None}
K["C2C3"]={"verdict_cell":"not-checkable (attribution) + not-checkable (data: 1980s backcast & sector series absent)","bw_modern":c23}

json.dump(K,open(f"{RES}/_blockB_keyresults.json","w"),indent=2,default=str)
print(json.dumps(K,indent=2,default=str))
