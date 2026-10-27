import json, hashlib, os

RES = "/workspace/eval/followup/001-001-claims-and-predictions/results"
WS = "/workspace/eval/followup/001-001-claims-and-predictions/workspace"
SD = "/workspace/eval/followup_staging/shared-data"
os.makedirs(RES, exist_ok=True)
os.makedirs(f"{WS}/checkpoints", exist_ok=True)

# PROVENANCE-declared hashes (data files)
PROV = {
 "worldbank-wdi/wdi_manufacturing_trade_1960_2025.csv":"6e33494746a95aa2ee9a7933ac6388915203e2c070e1489b73d7022b36342bdc",
 "worldbank-wdi/wdi_durables_diffusion_demand_side.csv":"4919c90924067d434057b0159cd634c1e6d6aa8a0025ad598e0404aa515e39eb",
 "wits-intermediates/wits_unctad_sop_product_shares.csv":"e3efc0453b8d115126062a11df82a47c3752c48c4f7e13a17e70341e1cb809ce",
 "census-bds/bds2023_ez.csv":"c3310039b69987ee5838826a626bbf00d0bfa3dba79a805ae03572fdd8b116ca",
 "census-bds/bds2023_sec_ez.csv":"ccc20556eca518bd1c285212642fee74e1c622167b3bb660fe5f630f082219d8",
 "eurostat/nama_10r_2gdp_emilia_romagna.json":"54ac84e960db2da1c4581a854f64b5b1c9f9b2c667b5c77ed5ef1f92b591bc4a",
 "eurostat/sbs_sc_ind_r2_manufacturing_sizeclass.json":"074258f2d4af172daa4594053e548caa6936a204909de7f3063a9f5542f6991d",
 "eurostat/sbs_sc_ovw_manufacturing_sizeclass.json":"f286f523317f80b792c87b1abd23631a20ef3c4b9cc270f82b8d25abf2afb25d",
 "steel/world-steel-in-figures-2025.pdf":"a830f0b9cb8237dc5131145cffb8ff6eb7ce5b5f0930f6abf8ff6fc383da48d4",
 "owid-durables/us_household_technology_adoption.csv":"4436d028351dd2e1deae5521db76f77a8b3b6b72a75fb1d2ca88ba9ff518cc5a",
 "census-statab/hs-42-selected-communications-media-1920-2001.pdf":"55804674e8ecb19d565476e2359fccfa62fad9f2e455f57bbe9b432a52b0d7c4",
 "wto-gvc-report/gvcreport2025-01_e.pdf":"50de298a3b30a86cb998180fd0cd0f60799388b50d27c2f3daaf678652843dca",
 "wto-gvc-report/gvcreport2025-02_e.pdf":"f79ca87c10b5b3cdc80a4958125d94b3804b5344f5f3d89b13b37fb8e16b9131",
}
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(65536),b''): h.update(c)
    return h.hexdigest()

a1 = {"declared_files_checked":0,"matched":0,"mismatched":[],"files":[]}
for rel,exp in PROV.items():
    got = sha(f"{SD}/{rel}")
    ok = got==exp
    a1["declared_files_checked"]+=1
    a1["matched"]+= 1 if ok else 0
    if not ok: a1["mismatched"].append(rel)
    a1["files"].append({"file":rel,"expected":exp,"got":got,"match":ok})
# literature files: present, no hash on record in staged PROVENANCE
lit = sorted([f for f in os.listdir(f"{SD}/literature")])
a1["literature_present_no_staged_hash"] = lit

# A1b
a1b_raw = json.load(open(f"{WS}/a1b_results.json"))
a1b = {"checks":a1b_raw,
       "total_checks":len(a1b_raw),
       "all_meet_expected": all(r["meets_expected"] for r in a1b_raw)}

# attribution status per row (per I.1 / PS-A1 pre-declarations)
attribution = {
 "B1":{"verified":["BHEN","BERG","HAMP"],"status":"double-sourced"},
 "B2":{"verified":["BHEN","SCHW"],"status":"double-sourced"},
 "B3":{"verified":["SCHW","HAMP"],"status":"double-sourced (scoped: internal-exhaustion diagnosis)"},
 "C1":{"verified":["SCHW","RIN","STUR"],"status":"double-sourced (scoped: E-R ideal-model)"},
 "C4":{"verified":[],"status":"demoted: not-checkable (attribution) [pre-declared; no steel anchor in corpus]"},
 "C5":{"verified":["BHEN","BERG"],"status":"double-sourced"},
 "D1":{"verified":["SCHW"],"carl_general_thesis_only":True,
       "status":"demoted: not-checkable (attribution) [pre-declared; CARL general-thesis insufficient for D1 wording]"},
 "C2C3":{"verified":["BERG"],"status":"demoted: not-checkable (attribution) [pre-declared single-source]"},
 "P1":{"verified":["SCHW","BERG"],"status":"double-sourced"},
 "P3":{"verified":["SCHW","BERG"],"status":"double-sourced"},
 "P2":{"verified":["SCHW","BERG","BHEN"],"status":"handed to study 002"},
 "P4":{"verified":["HAMP","SCHW"],"status":"not graded ([INTERP]); attribution recorded, not required"},
 "D2":{"verified":[],"status":"not graded ([LIT]); attribution not required"},
}
a1b["attribution_status_by_row"] = attribution

# A2 coverage
a2 = {
 "bds_max_year_2023": True,
 "wits_1988_2023": True,
 "eurostat_er_2000_2024": True,
 "owid_entities_nonempty_through_1973": {"Automobile":True,"Household refrigerator":True,"Washing machine":True},
 "hs42_1973_TV_present": True, "hs42_TV_1973":96.4, "hs42_TV_1984":98.1,
 "bds_esize_breaks":["a) 1 to 4","b) 5 to 9","c) 10 to 19","d) 20 to 99","e) 100 to 499","f) 500 to 999","g) 1000+"],
 "note":"'<100 emp' small-establishment band = esize a+b+c+d",
 "status":"PASS",
}

# A3 staging/branch flags
a3 = {
 "williams1987_staged": False,  # H2 not cleared
 "indstat_staged": False,       # H3 not cleared
 "usgs_ds140_staged": False,    # USGS blocked
 "C4_D1_restoration_events_fired": False,
 "C4_historical_eaf_branch":"literature-quoted (Minerals Yearbook via OA + Barnett&Crandall); USGS DS140 unavailable",
 "williams1987_disclosure_required_verbatim": True,
}

gates = {"generated":"2026-10-27","study":"001-claims-and-predictions",
         "launch_line":"REPLICATION: NOT APPLICABLE — BOOK, GO-WITH-SCOPE (Phase 0); THIS STUDY IS THE VERIFICATION LAYER",
         "A1_hash_integrity":a1,"A1b_attribution_locators":a1b,
         "A2_coverage":a2,"A3_staging_branch_flags":a3}
json.dump(gates, open(f"{RES}/gates.json","w"), indent=2)

print("A1: %d/%d declared hashes matched; mismatches=%s"%(a1["matched"],a1["declared_files_checked"],a1["mismatched"]))
print("A1b: %d checks, all_meet_expected=%s"%(a1b["total_checks"],a1b["all_meet_expected"]))
print("Double-sourced rows:", [k for k,v in attribution.items() if v["status"].startswith("double")])
print("Demoted rows:", [k for k,v in attribution.items() if "demoted" in v["status"]])
open(f"{WS}/checkpoints/A.done","w").write("gates A1/A1b/A2/A3 complete\n")
print("checkpoint A.done written")
