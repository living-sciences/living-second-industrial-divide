import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd, json, numpy as np

RES = "/workspace/eval/followup/002-002-globalization-test/results"
SD = "/workspace/eval/followup_staging/shared-data"
R001 = "/workspace/eval/followup/001-001-claims-and-predictions/results"
OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#56B4E9", "#F0E442", "#000000"]
plt.rcParams.update({
    "figure.dpi": 150, "savefig.dpi": 150, "savefig.bbox": "tight",
    "font.size": 11, "axes.titlesize": 12, "axes.labelsize": 11,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.25,
    "axes.prop_cycle": plt.cycler(color=OKABE_ITO),
})
ERAS = [(1984, 1995, "E1"), (1995, 2011, "E2"), (2011, 2026, "E3")]
def shade(ax, x0=1978):
    cols = ["#f2f2f2", "#e8eef5", "#fbf1e2"]
    for (a, b, lab), c in zip(ERAS, cols):
        ax.axvspan(max(a, x0), b, color=c, alpha=0.6, zorder=0)
        ax.text((max(a, x0)+b)/2, ax.get_ylim()[1], lab, ha="center", va="top", fontsize=8, color="#555")

# ---------- fig_scale.png (S1) ----------
fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.6))
s1a = pd.read_csv(f"{RES}/s1_scale.csv")
for i, (iso, name) in enumerate([("CHN", "China"), ("USA", "United States"), ("DEU", "Germany"),
                                 ("JPN", "Japan"), ("KOR", "Korea")]):
    s = s1a[s1a.iso3 == iso].sort_values("year")
    axL.plot(s.year, s.value, marker="o", ms=3, color=OKABE_ITO[i], label=name)
axL.set_ylim(0, axL.get_ylim()[1]); shade(axL, 2004)
axL.set_xlabel("year"); axL.set_ylabel("% of world manufacturing value added")
axL.set_title("S1a: hub concentration of manufacturing VA\n(WDI, current USD, staged)")
axL.legend(fontsize=8, loc="upper left")
# right: US establishment size (reuse 001 BDS)
bds = pd.read_csv(f"{R001}/claim_D1_manufacturing.csv")
axR.plot(bds.year, bds.small_estab_emp_share, color=OKABE_ITO[0], marker=".", ms=3, label="US small-estab (<100) emp share %")
axR.set_ylabel("US mfg small-estab emp share (%)", color=OKABE_ITO[0])
axR.set_ylim(20, 40)
ax2 = axR.twinx(); ax2.spines["top"].set_visible(False)
ax2.plot(bds.year, bds.mean_estab_size, color=OKABE_ITO[3], marker=".", ms=3, label="US mean estab size (emp)")
ax2.set_ylabel("US mfg mean establishment size (emp)", color=OKABE_ITO[3])
ax2.grid(False)
shade(axR, 1978)
axR.axvline(2011, color="#888", ls="--", lw=1)
axR.set_xlabel("year")
axR.set_title("S1b: US plant-size — smallization 1978-2011,\nE3 re-concentration 2011-2023 (BDS, via 001)")
l1, la1 = axR.get_legend_handles_labels(); l2, la2 = ax2.get_legend_handles_labels()
axR.legend(l1+l2, la1+la2, fontsize=8, loc="lower left")
fig.suptitle("S1 — Scale of the production unit: the unit SPLITS by geography and era (favors H-C)", fontsize=12)
fig.tight_layout(); fig.savefig(f"{RES}/fig_scale.png", facecolor="white"); plt.close(fig)
print("fig_scale.png written")

# ---------- fig_composition.png (S3) ----------
fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.6))
w = pd.read_csv(f"{SD}/wits-intermediates/wits_unctad_sop_product_shares.csv")
wx = w[(w.reporter == "WLD") & (w.indicator == "XPRT-PRDCT-SHR")].pivot(index="year", columns="product", values="value")
names = {"UNCTAD-SoP1": "raw", "UNCTAD-SoP2": "intermediate", "UNCTAD-SoP3": "consumer", "UNCTAD-SoP4": "capital"}
for i, c in enumerate(["UNCTAD-SoP1", "UNCTAD-SoP2", "UNCTAD-SoP3", "UNCTAD-SoP4"]):
    axL.plot(wx.index, wx[c], marker=".", ms=2, color=OKABE_ITO[i], label=names[c])
axL.set_ylim(0, 45); shade(axL, 1988)
axL.axhspan(19.45, 24.92, color=OKABE_ITO[1], alpha=0.12)
axL.set_xlabel("year"); axL.set_ylabel("% of world merchandise exports")
axL.set_title("WITS UNCTAD-SoP export mix\n(intermediate flat, [PREVIEW-KNOWN] band)", fontsize=11)
axL.legend(fontsize=8, loc="upper right")
# right: WTO participation phases schematic (bar) + GVC share peak
axR.axis("off")
axR.set_title("GVC participation — rose then plateaued\n(WTO GVC Report 2025; TiVA degraded)", fontsize=11)
txt = ("GVC participation (TiVA via WTO Fig 2.8):\n"
       "  1995-2011  broad-based gains (expansion/deepening)\n"
       "  2011-2022  backward modest, forward flat,\n"
       "             aggregate broadly unchanged (PLATEAU)\n\n"
       "GVC-related trade share of total trade:\n"
       "  peak 48.0% (2022)  ->  46.3% (2024)\n\n"
       "US-China bilateral trade grew ~30% slower than\n"
       "their trade with the rest of the world since 2018\n"
       "(tariff-timed decoupling); rerouting via Mexico/Viet Nam;\n"
       "services overtook goods in GVC participation.\n\n"
       "=> H-C's rise-then-plateau + regionalization signature.")
axR.text(0.02, 0.95, txt, va="top", ha="left", fontsize=9.5, family="monospace",
         bbox=dict(boxstyle="round", fc="#fbf1e2", ec="#E69F00", alpha=0.7))
fig.suptitle("S3 — Trade composition (favors H-C: task-trade rose 1995-2011, then plateaued)", fontsize=12, y=1.02)
fig.tight_layout(); fig.savefig(f"{RES}/fig_composition.png", facecolor="white"); plt.close(fig)
print("fig_composition.png written")

# ---------- fig_evidence_grid.png ----------
grid = pd.read_csv(f"{RES}/evidence_table.csv")
sigs = ["S1 scale of production unit", "S2 standardization vs variety", "S3 trade composition",
        "S4 chain governance (WEAK-CELL CAP)", "S5 skill content (DECLARED WEAK)",
        "S6 demand-side institutions", "S7 district persistence (partially measured)"]
siglab = ["S1 scale", "S2 standardization", "S3 trade comp.", "S4 governance\n(cap: weak)",
          "S5 skill\n(declared weak)", "S6 demand instit.\n(ex-ante doc.)", "S7 districts\n(partial)"]
hyps = ["H-A", "H-B", "H-C"]
cellcolor = {"favors": "#1b7837", "weakly favors": "#a6dba0", "not separable": "#f0f0f0",
             "weakly against": "#f4a582", "against": "#b2182b", "not measured": "#cccccc"}
celltxt = {"favors": "favors", "weakly favors": "weakly\nfavors", "not separable": "not\nseparable",
           "weakly against": "weakly\nagainst", "against": "against"}
fig, ax = plt.subplots(figsize=(8.2, 8.4))
for i, sig in enumerate(sigs):
    for j, hyp in enumerate(hyps):
        c = grid[(grid.signature == sig) & (grid.hypothesis == hyp)].cell.iloc[0]
        col = cellcolor.get(c, "#dddddd")
        ax.add_patch(plt.Rectangle((j, len(sigs)-1-i), 1, 1, facecolor=col, edgecolor="white", lw=2))
        fc = "white" if c in ("favors", "against") else "black"
        ax.text(j+0.5, len(sigs)-1-i+0.5, celltxt.get(c, c), ha="center", va="center", fontsize=8.5, color=fc)
ax.set_xlim(0, 3); ax.set_ylim(0, len(sigs))
ax.set_xticks([x+0.5 for x in range(3)])
ax.set_xticklabels(["H-A\nnew mass\nproduction", "H-B\nflexible spec.\nat global scale", "H-C\nneither:\nsecond unbundling"], fontsize=9)
ax.set_yticks([len(sigs)-1-i+0.5 for i in range(len(sigs))])
ax.set_yticklabels(siglab, fontsize=8.5)
ax.xaxis.tick_top(); ax.tick_params(length=0)
for s in ax.spines.values():
    s.set_visible(False)
ax.grid(False)
K = json.load(open(f"{RES}/_grid_keyresults.json"))
t = K["tallies"]
sub = (f"VERDICT: neither — the unbundling reading (threshold-sensitive)\n"
       f"full favors on live cells — H-A:{t['H-A']['full_favors_on_live_cells']}  "
       f"H-B:{t['H-B']['full_favors_on_live_cells']}  H-C:{t['H-C']['full_favors_on_live_cells']}  (>=4 bar not reached by any)")
ax.set_title("Evidence grid: 7 signatures × 3 hypotheses", fontsize=12, pad=38)
fig.text(0.5, 0.025, sub, ha="center", fontsize=9, color="#333")
# legend
handles = [mpatches.Patch(color=cellcolor[k], label=k) for k in ["favors", "weakly favors", "not separable", "weakly against", "against"]]
ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.02), ncol=5, fontsize=8, frameon=False)
fig.tight_layout(rect=[0, 0.06, 1, 1]); fig.savefig(f"{RES}/fig_evidence_grid.png", facecolor="white"); plt.close(fig)
print("fig_evidence_grid.png written")
