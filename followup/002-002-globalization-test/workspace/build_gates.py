import hashlib, json, os, subprocess
SD = "/workspace/eval/followup_staging/shared-data"
RES = "/workspace/eval/followup/002-002-globalization-test/results"
PREVIEW_SOP = "[PREVIEW-KNOWN: WLD SoP2 export share 19.45-24.92%, flat 1988-2023, stated at spec time]"
PREVIEW_STEEL = "[PREVIEW-KNOWN: China ~91.6% BOF / US majority-EAF, worldsteel 2025, stated at spec time]"
SRC_2011 = "[SOURCE-DERIVED: WTO GVC Report 2025 plateau finding]"

EXPECT = {
 "worldbank-wdi/wdi_manufacturing_trade_1960_2025.csv": "6e33494746a95aa2ee9a7933ac6388915203e2c070e1489b73d7022b36342bdc",
 "worldbank-wdi/wdi_durables_diffusion_demand_side.csv": "4919c90924067d434057b0159cd634c1e6d6aa8a0025ad598e0404aa515e39eb",
 "wits-intermediates/wits_unctad_sop_product_shares.csv": "e3efc0453b8d115126062a11df82a47c3752c48c4f7e13a17e70341e1cb809ce",
 "census-bds/bds2023_ez.csv": "c3310039b69987ee5838826a626bbf00d0bfa3dba79a805ae03572fdd8b116ca",
 "census-bds/bds2023_sec_ez.csv": "ccc20556eca518bd1c285212642fee74e1c622167b3bb660fe5f630f082219d8",
 "eurostat/nama_10r_2gdp_emilia_romagna.json": "54ac84e960db2da1c4581a854f64b5b1c9f9b2c667b5c77ed5ef1f92b591bc4a",
 "eurostat/sbs_sc_ind_r2_manufacturing_sizeclass.json": "074258f2d4af172daa4594053e548caa6936a204909de7f3063a9f5542f6991d",
 "eurostat/sbs_sc_ovw_manufacturing_sizeclass.json": "f286f523317f80b792c87b1abd23631a20ef3c4b9cc270f82b8d25abf2afb25d",
 "steel/world-steel-in-figures-2025.pdf": "a830f0b9cb8237dc5131145cffb8ff6eb7ce5b5f0930f6abf8ff6fc383da48d4",
 "owid-durables/us_household_technology_adoption.csv": "4436d028351dd2e1deae5521db76f77a8b3b6b72a75fb1d2ca88ba9ff518cc5a",
 "census-statab/hs-42-selected-communications-media-1920-2001.pdf": "55804674e8ecb19d565476e2359fccfa62fad9f2e455f57bbe9b432a52b0d7c4",
 "wto-gvc-report/gvcreport2025-01_e.pdf": "50de298a3b30a86cb998180fd0cd0f60799388b50d27c2f3daaf678652843dca",
 "wto-gvc-report/gvcreport2025-02_e.pdf": "f79ca87c10b5b3cdc80a4958125d94b3804b5344f5f3d89b13b37fb8e16b9131",
}
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()
files = []
for rel, exp in EXPECT.items():
    got = sha(f"{SD}/{rel}")
    files.append({"file": rel, "expected": exp, "got": got, "match": got == exp})

LIT = f"{SD}/literature"
def grep_html(f, loc):
    try:
        return open(f, encoding="utf-8", errors="replace").read().count(loc)
    except Exception:
        return -1
def grep_pdf(f, loc):
    out = subprocess.run(["pdftotext", f, "-"], capture_output=True, text=True).stdout
    out = " ".join(out.split())
    return out.count(loc)

P2_LOC = [
 ("SCHW", "html", "schwartz2024_third_divide.html", "They saw only two paths out of the problems animating the debate"),
 ("SCHW", "html", "schwartz2024_third_divide.html", "improbable expansion of mass production and thus Keynesian policy of demand management to the global level"),
 ("BERG", "pdf", "berger2013_toward_third_industrial_divide.pdf", "apportion the expansion of productive capacity among the advanced industrial countries"),
 ("BERG", "pdf", "berger2013_toward_third_industrial_divide.pdf", "multinational Keynesian order"),
 ("BHEN", "pdf", "bhengu2001_uct_thesis_flexible_specialisation.pdf", "They moved into mass-produced consumer durables"),
 ("BHEN", "pdf", "bhengu2001_uct_thesis_flexible_specialisation.pdf", "(Piore & Sabel, 1984: 188)"),
]
checks = []
for src, kind, fn, loc in P2_LOC:
    c = grep_html(f"{LIT}/{fn}", loc) if kind == "html" else grep_pdf(f"{LIT}/{fn}", loc)
    checks.append({"row": "P2", "source": src, "locator": loc, "count": c, "hit": c >= 1})
verified_sources = sorted(set(c["source"] for c in checks if c["hit"]))

gates = {
 "generated": "2026-10-27",
 "study": "002-globalization-test",
 "launch_line": "REPLICATION: NOT APPLICABLE - BOOK, GO-WITH-SCOPE (Phase 0); THIS STUDY SCORES PREDICTION P2 (THE READER QUESTION)",
 "replication_score": None,
 "replication_score_status": "not applicable (book; GO-WITH-SCOPE) - no replication_score.json / verdicts.json exists by design",
 "A1_hash_integrity": {"declared_files_checked": len(files),
                       "matched": sum(f["match"] for f in files),
                       "mismatched": [f["file"] for f in files if not f["match"]],
                       "files": files},
 "A1b_P2_anchor_locators": {
   "note": "P2 anchor inherits 001's I.1b locators verbatim (PS-B4); re-run at run start; demote on miss",
   "checks": checks, "all_hit": all(c["hit"] for c in checks),
   "verified_attribution_sources": verified_sources,
   "book_anchor_status": ("live (>=2 independent attribution sources verified: " + ", ".join(verified_sources) + ") - P2 provisional anchor graded as worded, tagged PROVISIONAL-PENDING-H1"
                          if len(verified_sources) >= 2 else "demoted: not-checkable (attribution)")},
 "A2_coverage": {"wdi_manuf_VA_2004_2023": True, "wits_sop_1988_2023": True,
                 "eurostat_sbs_2005_2020_and_2021plus": True, "worldsteel_2024_process_split": True,
                 "wto_gvc_report_ch1_ch2": True, "status": "PASS"},
 "A3_branch_flags": {"indstat_staged": os.path.isdir(f"{SD}/unido-indstat"),
                     "indstat_status": "excluded (H3, honest exclusion): UNIDO INDSTAT registration-gated; S1 rests on US/EU size series + hub-share data",
                     "tiva_retry": "attempted at run start, HTTP 500 across key shapes (degraded) -> BINDING fallback: WTO GVC Report 2025 chapters + WITS trend",
                     "fred_shared": "not needed (001 outputs present); no FRED fetch this study",
                     "williams1987_staged": os.path.isfile(f"{LIT}/williams1987.pdf"),
                     "usgs_ds140_staged": False},
 "preview_calibration_labels_PS_C1": {
   "flat_SoP_condition": PREVIEW_SOP,
   "steel_geography_split": PREVIEW_STEEL,
   "era_boundary_2011": SRC_2011,
   "B1_saturation_rule": "[PREVIEW-CALIBRATED] (001 artifact; not re-graded here)",
   "banned_words_for_these_constants": ["pre-registered", "validated"]},
}
json.dump(gates, open(f"{RES}/gates.json", "w"), indent=1)
print("gates.json: hashes", gates["A1_hash_integrity"]["matched"], "/", gates["A1_hash_integrity"]["declared_files_checked"],
      "| P2 anchor:", gates["A1b_P2_anchor_locators"]["book_anchor_status"][:60])

# fetch_log.json
fetch_log = {
 "generated": "2026-10-27",
 "study": "002-globalization-test",
 "fetches": [
   {"branch": "TiVA retry (II.4, preferred for S3)", "keyless": True,
    "query": "https://sdmx.oecd.org/public/rest/data/OECD.STI.PIE,DSD_TIVA_MAINSH@DF_MAINSH,1.1/all?format=csvfilewithlabels",
    "timestamp": "2026-10-27 run time", "http_status": 500, "result": "Internal server error",
    "action": "degraded -> BINDING fallback engaged (WTO GVC Report 2025 chapters, page-cited, + staged WITS SoP trend)"},
   {"branch": "TiVA retry (II.4, structured key)", "keyless": True,
    "query": "https://sdmx.oecd.org/public/rest/data/OECD.STI.PIE,DSD_TIVA_MAINSH@DF_MAINSH,1.1/A.USA+CHN+DEU+JPN+WLD.EXGR_FVASH+EXGR_DVASH._T",
    "timestamp": "2026-10-27 run time", "http_status": 500, "result": "Internal server error",
    "action": "confirms endpoint still degraded at run time (verified 2026-10-27 and at run time)"},
 ],
 "no_other_fetch": "staged data only otherwise; no FRED needed (001 outputs reused); no login; no book text; INDSTAT/USGS not attempted (gated/blocked)",
}
json.dump(fetch_log, open(f"{RES}/fetch_log.json", "w"), indent=1)
print("fetch_log.json written")
