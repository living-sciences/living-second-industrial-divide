import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd, json
RES="/workspace/eval/followup/001-001-claims-and-predictions/results"
OKABE=["#0072B2","#E69F00","#009E73","#D55E00","#CC79A7","#56B4E9","#F0E442","#000000"]
plt.rcParams.update({"figure.figsize":(7.5,4.5),"figure.dpi":150,"savefig.dpi":150,
 "savefig.bbox":"tight","font.size":12,"axes.titlesize":13,"axes.labelsize":12,
 "axes.spines.top":False,"axes.spines.right":False,"axes.grid":True,"grid.alpha":0.25,
 "axes.prop_cycle":plt.cycler(color=OKABE)})

# ---- fig_b1_saturation ----
b1=pd.read_csv(f"{RES}/claim_B1.csv")
fig,ax=plt.subplots()
x=range(len(b1));
ax.bar([i-0.2 for i in x],b1.pen_1973,0.4,label="1973 penetration",color=OKABE[0])
ax.bar([i+0.2 for i in x],b1.pen_1984,0.4,label="1984 penetration",color=OKABE[1])
for i,r in b1.iterrows():
    ax.text(i,max(r.pen_1973,r.pen_1984)+1.5,f"{r.ratio_73_84:.3f}",ha="center",fontsize=9)
ax.set_xticks(list(x)); ax.set_xticklabels(["Automobile","Household\nrefrigerator","Washing\nmachine","TV\n(HS-42)"])
ax.set_ylabel("% of US households with durable"); ax.set_ylim(0,110)
ax.axhline(0,color="k",lw=0.5)
ax.set_title("B1: US durable penetration, 1973 vs 1984 (ratio = 1973/1984)")
ax.legend(loc="center right")
ax.text(0.0,1.06,"All four already >=93% of 1984 level by 1973 -> supported  [PREVIEW-CALIBRATED]",
        transform=ax.transAxes,fontsize=8,color="#444")
fig.savefig(f"{RES}/fig_b1_saturation.png",facecolor="white"); plt.close(fig)

# ---- fig_c1_emilia ----
fig,ax=plt.subplots()
# historical Rinaldi: % above Italian per-capita mean
hist_y=[1951,1980,1995]; hist_v=[None,29,25]
# compute 1951: 7th place, gap not given as % -> plot only 1980/1995; mark 1951 rank as annotation
ax.plot([1980,1995],[29,25],"o-",color=OKABE[1],label="Rinaldi/ISTAT: E-R income vs Italy mean (historical, %)")
c1=pd.read_csv(f"{RES}/claim_C1.csv")
mod=c1[c1.metric=="ER_rel_IT_pct"].dropna(subset=["value"])
ax.plot(mod.year,mod.value,"s--",color=OKABE[0],label="Eurostat PPS: E-R vs Italy (modern, %)")
ax.axvline(1999,color="#999",ls=":",lw=1); ax.text(1999.5,32,"splice\n(diff. sources)",fontsize=8,color="#666")
ax.annotate("1951: 7th among\nItalian regions\n(rank, not %)",xy=(1951,10),fontsize=8,color="#444")
ax.set_xlabel("Year"); ax.set_ylabel("E-R per-capita income, % above Italian mean")
ax.set_title("C1: Emilia-Romagna relative income (historical + modern)")
ax.legend(loc="upper right",fontsize=8); ax.set_xlim(1948,2026); ax.set_ylim(0,35)
fig.savefig(f"{RES}/fig_c1_emilia.png",facecolor="white"); plt.close(fig)

# ---- fig_d1_plantsize ----
econ=pd.read_csv(f"{RES}/claim_D1_economy.csv"); man=pd.read_csv(f"{RES}/claim_D1_manufacturing.csv")
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10.5,4.5))
ax1.plot(econ.year,econ.small_estab_emp_share,color=OKABE[0],label="Economy-wide")
ax1.plot(man.year,man.small_estab_emp_share,color=OKABE[1],label="Manufacturing (NAICS 31-33)")
ax1.axvspan(1963,1978,color="#ccc",alpha=0.4)
ax1.text(1964,ax1.get_ylim()[0]+2 if False else 30,"literature-quoted\n(Carlsson 1988):\nmetalworking avg\nestab size -12.3%\n1972-82",fontsize=7,color="#555")
ax1.set_xlim(1963,2024); ax1.set_xlabel("Year"); ax1.set_ylabel("Small-estab (<100 emp) share of employment, %")
ax1.set_title("Small-establishment employment share"); ax1.legend(fontsize=9)
ax2.plot(econ.year,econ.mean_estab_size,color=OKABE[0],label="Economy-wide")
ax2.plot(man.year,man.mean_estab_size,color=OKABE[1],label="Manufacturing (NAICS 31-33)")
ax2.axvspan(1963,1978,color="#ccc",alpha=0.4)
ax2.set_xlim(1963,2024); ax2.set_xlabel("Year"); ax2.set_ylabel("Mean establishment size (employees)")
ax2.set_title("Mean establishment size"); ax2.legend(fontsize=9)
fig.suptitle("D1: plant-size reversal is a MANUFACTURING phenomenon (BDS 1978-2023; shaded = pre-1978 literature segment)",fontsize=11)
fig.savefig(f"{RES}/fig_d1_plantsize.png",facecolor="white"); plt.close(fig)
print("figures written:")
import os
for f in ["fig_b1_saturation.png","fig_c1_emilia.png","fig_d1_plantsize.png"]:
    print("  ",f,os.path.getsize(f"{RES}/{f}"),"bytes")
