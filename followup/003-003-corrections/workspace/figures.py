import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv, os

OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#D55E00",
             "#CC79A7", "#56B4E9", "#F0E442", "#000000"]
plt.rcParams.update({
    "figure.figsize": (7.5, 4.5), "figure.dpi": 150,
    "savefig.dpi": 150, "savefig.bbox": "tight",
    "font.size": 12, "axes.titlesize": 13, "axes.labelsize": 12,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.25,
    "axes.prop_cycle": plt.cycler(color=OKABE_ITO),
})

RES = "/workspace/eval/followup/003-003-corrections/results"
WDI = "/workspace/eval/followup_staging/shared-data/worldbank-wdi/wdi_manufacturing_trade_1960_2025.csv"
EU  = "/workspace/eval/followup/002-002-globalization-test/results/s1_eu_sizeclass.csv"
os.makedirs(RES, exist_ok=True)

# ---------- Figure 1: PS-PROV-1 WDI manufacturing VA-share vintage ----------
series = {"USA": {}, "DEU": {}, "JPN": {}}
with open(WDI) as f:
    for r in csv.DictReader(f):
        if r["indicator"] == "NV.IND.MANF.ZS" and r["iso3"] in series:
            v = r["value"]
            if v not in ("", None):
                fv = float(v)
                if fv > 0:  # 0.00 = missing in this staged file
                    series[r["iso3"]][int(r["year"])] = fv

labels = {"USA": "United States", "DEU": "Germany", "JPN": "Japan"}
true_start = {"USA": 1997, "DEU": 1991, "JPN": 1994}
end_pt = {"USA": 2021, "DEU": 2023, "JPN": 2023}
colors = {"USA": "#0072B2", "DEU": "#009E73", "JPN": "#CC79A7"}

fig, ax = plt.subplots()
for iso in ["USA", "DEU", "JPN"]:
    yrs = sorted(series[iso])
    vals = [series[iso][y] for y in yrs]
    ax.plot(yrs, vals, "-o", ms=3, color=colors[iso], label=labels[iso])
    s = true_start[iso]
    ax.plot([s], [series[iso][s]], "o", ms=10, mfc="none", mec="#D55E00", mew=2, zorder=5)
    ax.annotate(f"{iso} series starts {s}\n({series[iso][s]:.1f}%)",
                (s, series[iso][s]), textcoords="offset points",
                xytext=(6, 10), fontsize=8.5, color="#D55E00")
ax.axvline(1984, color="#555555", ls="--", lw=1.2)
ax.text(1984.4, ax.get_ylim()[1]*0.60,
        'claimed "1984" baseline:\nNO WDI VA-share data',
        fontsize=8.5, color="#555555")
ax.set_xlabel("Year")
ax.set_ylabel("Manufacturing value added (% of GDP)")
ax.set_xlim(1982, 2026)
ax.legend(title="WDI NV.IND.MANF.ZS", loc="upper right", fontsize=9)
fig.savefig(f"{RES}/fig1_p1_va_vintage.png", facecolor="white")
plt.close(fig)
print("fig1 written; true starts", {k: (true_start[k], round(series[k][true_start[k]],2)) for k in series})

# ---------- Figure 2: PS-PROV-2 EU SBS small-plant share starts 2011 ----------
rows = list(csv.DictReader(open(EU)))
yrs = [int(r["year"]) for r in rows]
small = [float(r["small_lt50_emp_share"]) for r in rows]
# split by panel for the 2020/2021 break
p1 = [(int(r["year"]), float(r["small_lt50_emp_share"])) for r in rows if r["panel"].startswith("2005")]
p2 = [(int(r["year"]), float(r["small_lt50_emp_share"])) for r in rows if r["panel"].startswith("2021")]
fig, ax = plt.subplots()
ax.plot([x[0] for x in p1], [x[1] for x in p1], "-o", ms=4, color="#0072B2",
        label="panel 2005–2020 (V16110)")
ax.plot([x[0] for x in p2], [x[1] for x in p2], "-s", ms=4, color="#009E73",
        label="panel 2021+ (EMP_NR) [break]")
# emphasize the first available point (2011)
ax.plot([p1[0][0]], [p1[0][1]], "o", ms=12, mfc="none", mec="#D55E00", mew=2, zorder=5)
ax.annotate(f'label said "(2005)"\n→ true first year {p1[0][0]} ({p1[0][1]:.1f}%)',
            (p1[0][0], p1[0][1]), textcoords="offset points", xytext=(10, -2),
            fontsize=9, color="#D55E00")
ax.axvspan(2011, 2026, color="#E69F00", alpha=0.08)
ax.text(2017.5, ax.get_ylim()[0]+0.4, "E3 window (2011–2026) — unaffected",
        fontsize=8.5, color="#8a6d00")
ax.set_xlabel("Year")
ax.set_ylabel("EU27 small-plant (<50 emp) share of mfg employment (%)")
ax.set_xlim(2009, 2025.5)
ax.legend(loc="upper right", fontsize=9)
fig.savefig(f"{RES}/fig2_eu_sbs_vintage.png", facecolor="white")
plt.close(fig)
print("fig2 written; EU first year", p1[0])

# ---------- Figure 3: item 6 China-BOF preview correction ----------
# worldsteel 2025 "Crude steel production by process 2024" (staged), BOF (Oxygen) %
names = ["Austria\n(the 91.6 source)", "China\nspec PREVIEW", "China\ncomputed (true)", "United States"]
vals  = [91.6, 91.6, 89.8, 28.2]
cols  = ["#56B4E9", "#D55E00", "#0072B2", "#999999"]
hatch = [None, "//", None, None]
fig, ax = plt.subplots()
bars = ax.bar(names, vals, color=cols, edgecolor="white")
for b, h in zip(bars, hatch):
    if h: b.set_hatch(h)
for b, v in zip(bars, vals):
    ax.text(b.get_x()+b.get_width()/2, v+0.8, f"{v:.1f}%", ha="center", fontsize=10)
ax.annotate("", xy=(2, 89.8), xytext=(1, 91.6),
            arrowprops=dict(arrowstyle="->", color="#D55E00", lw=1.6))
ax.text(1.5, 93.5, "−1.8 pp\n(Austria→China)", ha="center", fontsize=8.5, color="#D55E00")
ax.set_ylabel("Basic-oxygen (BOF) share of crude steel, 2024 (%)")
ax.set_ylim(0, 102)
ax.set_title("")
fig.text(0.5, -0.02, "worldsteel 2025, 'Crude steel production by process' table (staged)",
         ha="center", fontsize=8, color="#555555")
fig.savefig(f"{RES}/fig3_china_bof_preview.png", facecolor="white")
plt.close(fig)
print("fig3 written")
