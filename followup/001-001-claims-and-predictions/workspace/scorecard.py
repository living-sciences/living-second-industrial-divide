import json, csv
RES="/workspace/eval/followup/001-001-claims-and-predictions/results"
K=json.load(open(f"{RES}/_blockB_keyresults.json"))

PV="[PREVIEW-CALIBRATED: 1973 OWID/HS-42 values in view at spec time — Automobile 82.0 (.943), Household refrigerator 99.0 (1.000), Washing machine 66.0 (.930), TV 96.4% HS-42 (.983 vs 98.1 in 1984)]"

rows=[]
def R(**kw): rows.append(kw)

R(id="B1",
  provisional_wording="Core consumer-durable markets in advanced countries were saturated by the early 1970s",
  verdict="supported",
  decision_statistic="per durable d in {Automobile,Household refrigerator,Washing machine,TV(HS-42)}: saturated if pen(1973)>=0.9*pen(1984) AND mean growth 1973->1984 <=1.0 pp/yr; supported if >=3/4 pass and none fails growth guard",
  one_line_basis="4/4 durables pass: Auto .943/0.46pp, Fridge 1.000/0.0pp, Washer .930/0.46pp, TV .983/0.15pp",
  attribution_sources="BHEN(p.184 car/TV 'one car for every'+'television sets by 1970'); BERG('saturation of mass consumer-good markets'); HAMP('markets for mass produced goods became saturated') [3 verified, A1b]",
  attribution_status="double-sourced",
  adjudication_sources="OWID us_household_technology_adoption (Automobile/Household refrigerator/Washing machine); Census Statistical Abstract HS-42 (TV, OWID TV starts 1992)",
  book_anchor_status="PROVISIONAL-PENDING-H1",
  data_story="all four durables already at >=93% of their 1984 penetration by 1973 with <=0.46 pp/yr residual growth",
  preview_labels=PV,
  data_files="claim_B1.csv",
  seams_notes="TV from HS-42 not OWID (OWID 'Television' starts 1992; 'Colour TV' mid-diffusion in 1973) - source split disclosed")

R(id="B2",
  provisional_wording="The international demand-stabilization regime broke 1971-79, removing mass production's macro prop",
  verdict="supported",
  decision_statistic="documentary timeline match only: Bretton Woods end 1971-73, oil shocks 1973/79, stagflation fall within the asserted 1971-79 window -> supported; causal weight out of scope [LIT]",
  one_line_basis="documented macro record (end of Bretton Woods Aug 1971 / Smithsonian 1971 / float 1973; OPEC shocks 1973 & 1979; 1970s stagflation) matches the 1971-79 timeline",
  attribution_sources="BHEN(p.176 'rigid wages and prices central to the system of macroeconomic regulation'); SCHW('overly rigid production structure'+'presented a multitude of shocks') [2 verified, A1b]",
  attribution_status="double-sourced",
  adjudication_sources="documentary record (no new data); Baldwin 2006 is adjudication-side history only (never cites the book)",
  book_anchor_status="PROVISIONAL-PENDING-H1",
  data_story="timeline-only grade; CAUSAL weight that this broke mass production is [LIT] and ungraded",
  preview_labels="",
  data_files="(none - documentary)",
  seams_notes="only the timeline is graded; the causal claim is out of grading scope (R3)")

b3=K["B3"]["detail"]
R(id="B3",
  provisional_wording="Mass-production productivity growth had internally exhausted by the 1970s",
  verdict="supported",
  decision_statistic="post-1973 vs 1950-73 mean annual growth of labor productivity (OPHMFG-or-SUCCESSOR) and TFP (MFPNFBS): slowdown in BOTH -> supported; direction+timing only, no magnitude bar",
  one_line_basis=f"labor prod OPHNFB {b3['labor_productivity_OPHNFB']['mean_growth_1950_1973']}%->{b3['labor_productivity_OPHNFB']['mean_growth_1974_1984']}% (74-84); TFP MFPNFBS {b3['TFP_MFPNFBS']['mean_growth_1950_1973']}%->{b3['TFP_MFPNFBS']['mean_growth_1974_1984']}%; slowdown in both",
  attribution_sources="SCHW('overly rigid production structure'); HAMP('the limits of the model of industrial development that is founded on mass production') [2 verified, A1b]",
  attribution_status="double-sourced (scoped: internal-exhaustion DIAGNOSIS; productivity operationalization is the briefing's, adjudicated by FRED)",
  adjudication_sources="FRED in-run fetch: OPHNFB (labor productivity, nonfarm business), MFPNFBS (TFP)",
  book_anchor_status="PROVISIONAL-PENDING-H1",
  data_story="US productivity growth slowed after 1973 on both measures (the classic post-1973 productivity slowdown)",
  preview_labels="",
  data_files="claim_B3.csv",
  seams_notes="OPHMFG (named) starts 1987 so cannot reach the pre-1973 window; successor OPHNFB (nonfarm business, 1947+) used per the 'or successor' clause - LOGGED DEVIATION (fetch_log). Series are economy/nonfarm-business, not manufacturing-only")

c1=K["C1"]
R(id="C1",
  provisional_wording="Emilia-Romagna rose sharply in relative income through the 1970s crisis on small-firm districts",
  verdict="supported",
  decision_statistic="direction AND approximate magnitude vs Rinaldi (7th in 1951 -> +29% vs national mean by 1980): reconstructed series rises through the 1970s with magnitude within a defensible reading of '+29% by 1980' -> supported",
  one_line_basis="Rinaldi (staged): E-R 7th among Italian regions by per-capita income in 1951; gap vs Italy mean rose to +29% by 1980; 2nd place (+25%) by 1995",
  attribution_sources="SCHW('ideal model for a better future'); RIN('Piore e Sabel 1984' in scholars-of-the-Emilian-model sentence); STUR('provided by Piore and Sabel (1984)') [3 verified, A1b]",
  attribution_status="double-sourced (scoped: E-R was the book's showcase/ideal model; income trajectory adjudicated by Rinaldi/ISTAT)",
  adjudication_sources="Rinaldi WP + ISTAT (historical); Eurostat nama_10r_2gdp PPS (modern endpoint, reported not graded)",
  book_anchor_status="PROVISIONAL-PENDING-H1",
  data_story=f"modern endpoint REPORTED: E-R per-capita (PPS) +{c1['modern']['2000']['ER_rel_IT_pct']}% vs Italy in 2000, +{c1['modern']['2024']['ER_rel_IT_pct']}% in 2024; {c1['modern']['2024']['ER_rel_EU_index']}% of EU27 in 2024",
  preview_labels="",
  data_files="claim_C1.csv",
  seams_notes="R2: the famous 'rose to second place' sentence circulates in incompatible tertiary versions; the row grades the TRAJECTORY and refuses the rank-in-1984 formulation pending H1. Modern Eurostat endpoint spliced visually, never graded into the historical claim")

R(id="C4",
  provisional_wording="US specialty steel/minimills thrived while integrated Big Steel collapsed",
  verdict="not-checkable (attribution)",
  decision_statistic="verdict cell not-checkable (attribution) unless a restoration event fires (none did: williams1987 not staged, no Google-Books verification). Data story graded supported-equivalent only if 1970s level AND direction to mid-80s agree across two named quotes",
  one_line_basis="zero verified attribution sources in corpus (the staged Schwartz essay has NO steel content; prior '~8%->~70%' Schwartz anchor was a false citation, withdrawn)",
  attribution_sources="NONE VERIFIED (A1b)",
  attribution_status="demoted: not-checkable (attribution) [pre-declared]",
  adjudication_sources="worldsteel World Steel in Figures 2025 (modern EAF shares); USGS DS140 BLOCKED (not staged); no OA Minerals-Yearbook quote staged",
  book_anchor_status="demoted (no anchor)",
  data_story="DATA TRAJECTORY (not a graded book claim): 2024 US EAF share 71.8% (worldsteel) vs China 10.2% EAF / 89.8% BOF, Italy 89.3% EAF, EU27 44.4% EAF. 1970s-84 US EAF LEVEL = not-checkable (data): USGS DS140 blocked and no staged literature quote -> historical branch has no supply route, trajectory not establishable from staged inputs (per fetch policy: input missing -> report, do not substitute from memory)",
  preview_labels="",
  data_files="claim_C4_worldsteel2024.csv",
  seams_notes="restoration events (H2 Williams 1987 / logged Google-Books snippet) did NOT fire -> anchor stays demoted; the modern EAF endpoint is the only computable datum")

R(id="C5",
  provisional_wording="Programmable (NC/CNC) technology erodes scale economies, making small batches economic",
  verdict="supported",
  decision_statistic="graded on the OBSERVABLE IMPLICATION only (the D1 size shift in machinery-intensive BDS sectors); the scale-economics mechanism itself is [LIT] and ungraded",
  one_line_basis="the observable implication holds: in BDS manufacturing (NAICS 31-33, incl. machinery) mean establishment size fell 58.7->45.8 and the small-establishment (<100) employment share rose 27.7%->32.5%, 1978-2023",
  attribution_sources="BHEN(p.258 'application of computers to industry favours flexible systems' + p.261 'programmable equipment is used just as automatic machinery'); BERG('computer-aided manufacturing (programmable assembly)...adjust equipment') [2 verified, A1b]",
  attribution_status="double-sourced",
  adjudication_sources="BDS 2023 manufacturing size distribution (same series as D1)",
  book_anchor_status="PROVISIONAL-PENDING-H1",
  data_story="implication confirmed in manufacturing; the mechanism (programmable tech CAUSES the shift) stays [LIT]",
  preview_labels="",
  data_files="claim_D1_manufacturing.csv",
  seams_notes="only the observable implication is graded; the scale-economics causal mechanism is out of grading scope (R3)")

d1=K["D1"]
R(id="D1",
  provisional_wording="The long rise of plant size reversed: average establishment size falling, small-establishment employment share rising from the 1970s",
  verdict="not-checkable (attribution)",
  decision_statistic="verdict cell not-checkable (attribution) at launch (single attribution source). Data story: share up AND mean size down in BOTH economy and manufacturing (BDS 1978->2023) -> 'reversal confirmed'; mixed -> 'qualified'; both opposite -> 'reversal not found'",
  one_line_basis=f"MIXED -> data story 'qualified': economy small-estab emp share {d1['economy']['share_1978']}%->{d1['economy']['share_2023']}% (DOWN) & mean size {d1['economy']['meansize_1978']}->{d1['economy']['meansize_2023']} (UP); manufacturing share {d1['manufacturing']['share_1978']}%->{d1['manufacturing']['share_2023']}% (UP) & mean size {d1['manufacturing']['meansize_1978']}->{d1['manufacturing']['meansize_2023']} (DOWN)",
  attribution_sources="SCHW('shrink themselves via outsourcing and demerger'+'drove the vertical disintegration that') [1 verified]; CARL general-thesis locator verified but scoped insufficient for D1 wording",
  attribution_status="demoted: not-checkable (attribution) [pre-declared single-source]",
  adjudication_sources="BDS 2023 (economy + manufacturing, 1978-2023); 1963-77 segment from Carlsson 1988 (metalworking -12.3% 1972-82) + Davis-Haltiwanger-line BDS literature (figure only)",
  book_anchor_status="demoted (no anchor); Schwartz HIT-with-outsourcing-twist engaged as prior art in prose",
  data_story="reversal is a MANUFACTURING phenomenon, not economy-wide: manufacturing establishments shrank and small-plant employment share rose; economy-wide the opposite (large-establishment services). Matches Schwartz's outsourcing/vertical-disintegration twist",
  preview_labels="",
  data_files="claim_D1_economy.csv, claim_D1_manufacturing.csv",
  seams_notes="1963-77 Census-of-Manufactures segment is literature-quoted (Carlsson), feeds the figure only, not the verdict")

R(id="D2",
  provisional_wording="Mass-production work deskills while flexible specialization re-skills",
  verdict="not-checkable ([LIT])",
  decision_statistic="pre-declared not-checkable (labor-process debate; [LIT]) - one literature paragraph, no data grade",
  one_line_basis="pre-declared ungraded labor-process-debate row",
  attribution_sources="(attribution not required - row never graded)",
  attribution_status="n/a (not graded)",
  adjudication_sources="Hirst & Zeitlin 1991 (recorded, not read); Schwartz 2024",
  book_anchor_status="n/a",
  data_story="(not graded as data)",
  preview_labels="",
  data_files="(none)",
  seams_notes="deskilling/re-skilling is a labor-process debate, out of data-grading scope")

c23=K["C2C3"]
R(id="C2/C3",
  provisional_wording="District-sector growth (Prato, Carpi, Sassuolo, Bologna) & Baden-Wurttemberg/Japan parallels",
  verdict="not-checkable (data) + not-checkable (attribution)",
  decision_statistic="deferred; no statistic unless the Eurostat in-run branch delivers, and then data-story-only (attribution stays demoted this tick). The C3 'same phenomenon' framing is [INTERP] and never graded",
  one_line_basis="Eurostat in-run branch delivered BW (DE1) modern GDP 2000-2024 but NO 1980s backcast (nama_10r_2gdp starts 2000); Italian district SECTOR series not staged this tick",
  attribution_sources="BERG('the Italian and French industrial districts and the German and Japanese middle-firm sectors') [1 verified]",
  attribution_status="demoted: not-checkable (attribution) [pre-declared single-source]",
  adjudication_sources="Eurostat nama_10r_2gdp (BW DE1, in-run fetch); Brusco 1982 & Herrigel are adjudication-side context",
  book_anchor_status="demoted (no anchor)",
  data_story=f"BW modern data story REPORTED: Baden-Wurttemberg per-capita (PPS) = {c23['bw_modern']['2000']['BW_rel_EU_index']}% of EU27 in 2000, {c23['bw_modern']['2024']['BW_rel_EU_index']}% in 2024 (above EU, mildly converging). 1980s backcast absent -> historical 'same phenomenon' stays not-checkable (data)",
  preview_labels="",
  data_files="claim_C23_bw.csv",
  seams_notes="Italian district sector series (Prato/Carpi exports) = next-tick item, named in findings")

# ---- predictions ----
p1=K["P1"]["detail"]
R(id="P1",
  provisional_wording="Old-national-form mass production will not recover absent new institutions",
  verdict="supported",
  decision_statistic="direction of manufacturing employment and VA shares, 1984->2025, US/DE/JP: shares do not recover toward pre-1973 levels absent new institutions -> supported; mixed -> partial; sustained recovery -> contradicted (direction+timing only)",
  one_line_basis=f"manuf VA share fell in all three (US {p1['USA']['va_share_1984']}->{p1['USA']['va_share_2023']}, DE {p1['DEU']['va_share_1984']}->{p1['DEU']['va_share_2023']}, JP {p1['JPN']['va_share_1984']}->{p1['JPN']['va_share_2023']}); US manuf emp share {p1['US_emp_share']['1984']}%->{p1['US_emp_share']['2025']}% (pre-1973 ~{p1['US_emp_share']['1970']}%), no recovery",
  attribution_sources="SCHW('improbable expansion of mass production and thus Keynesian policy of demand management to the global level'); BERG('One family of solutions would be a global Keynesianism'+'multinational Keynesian order') [2 verified]",
  attribution_status="double-sourced",
  adjudication_sources="WDI NV.IND.MANF.ZS (manuf VA %GDP, US/DE/JP); FRED MANEMP/PAYEMS (US manuf emp share)",
  book_anchor_status="PROVISIONAL-PENDING-H1",
  data_story="no advanced economy recovered its mass-production manufacturing share; declines continued 1984-2025",
  preview_labels="",
  data_files="claim_P1_va.csv, claim_P1_us_empshare.csv",
  seams_notes="DE/JP employment-share not staged (only US via FRED); VA shares cover all three. Hindsight context: the book could not have anticipated China's post-2001 manufacturing surge (Schwartz omissions list)")

R(id="P3",
  provisional_wording="Flexible specialization could become the dominant regime, districts the growth model",
  verdict="partially supported",
  decision_statistic="MODAL (could/potential): graded ONLY on factual components (did districts persist/grow as a model? - E-R and D1 series); dominance non-realization REPORTED as 'the possibility was not realized', never contradicted on its own",
  one_line_basis="factual component holds: E-R still +19.5% above Italy / 130.8% of EU27 in 2024 (districts persisted, did not collapse); BDS manufacturing small-plant reversal present. Dominance possibility NOT realized (Schwartz 'narrow slice'; Italy post-2000 stagnation)",
  attribution_sources="SCHW('The other was a transformation of the industrial base in the direction of flexible specialization'+'narrow slice of industrial output'+'a potential second divide, for a return to flexible specialization'); BERG('nourish and strengthen flexible specialization and craft production') [2 verified]",
  attribution_status="double-sourced",
  adjudication_sources="Eurostat E-R (2000-2024) + Rinaldi/ISTAT historical + D1 BDS series",
  book_anchor_status="PROVISIONAL-PENDING-H1",
  data_story="districts persisted/grew as a model (supported factual component); flexible specialization did NOT become the dominant regime -> the possibility was not realized",
  preview_labels="",
  data_files="claim_C1.csv, claim_D1_manufacturing.csv",
  seams_notes="modal rule PS-A3: non-realization of dominance is not a failed prediction; fork-not-forecast sentence carried in findings")

R(id="P4",
  provisional_wording="The exits are a political choice, not technologically determined",
  verdict="not-checkable ([INTERP] as stated)",
  decision_statistic="pre-declared ungraded ([INTERP]); one paragraph notes the weaker VoC-adjacent reading (Hall & Soskice), grades nothing",
  one_line_basis="interpretive/normative claim, not a data-decidable proposition as worded",
  attribution_sources="HAMP('a political choice between the technology of'); SCHW('utter indeterminacy of any given divide') [recorded; row never graded]",
  attribution_status="n/a (not graded)",
  adjudication_sources="(none - interpretive)",
  book_anchor_status="n/a",
  data_story="(not graded)",
  preview_labels="",
  data_files="(none)",
  seams_notes="political-choice thesis is [INTERP]; a weaker Varieties-of-Capitalism reading exists (Hall & Soskice) but is not graded")

R(id="P2",
  provisional_wording="Exit 1: mass production rebuilt at global scale with multinational-Keynesian institutions",
  verdict="see study 002",
  decision_statistic="HANDED TO 002 (H-A/H-B/H-C evidence-weighing on pre-declared signatures)",
  one_line_basis="out of scope for study 001",
  attribution_sources="SCHW/BERG/BHEN P2 locators verified (A1b) and inherited by 002 §II.0b",
  attribution_status="handed to study 002",
  adjudication_sources="(study 002)",
  book_anchor_status="PROVISIONAL-PENDING-H1 (002)",
  data_story="PS-B4 mapping note: 002's H-A is the OPERATIONALIZED hypothesis; its hub-concentration and profit-structure components are Kaplinsky's/Schwartz's modernizations, not Exit 1 as provisionally anchored - no 002 verdict reads as 'the book predicted/failed to predict China'",
  preview_labels="",
  data_files="(study 002)",
  seams_notes="P2 is study 002 entire; appears here only as the hand-off row")

cols=["id","provisional_wording","verdict","decision_statistic","one_line_basis",
 "attribution_sources","attribution_status","adjudication_sources","book_anchor_status",
 "data_story","preview_labels","data_files","seams_notes"]
with open(f"{RES}/scorecard.csv","w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=cols); w.writeheader()
    for r in rows: w.writerow(r)

# also write the C4 worldsteel + C23 bw small CSVs
import pandas as pd
pd.DataFrame([{"geo":"United States","EAF_pct":71.8,"BOF_oxygen_pct":28.2,"year":2024},
 {"geo":"China","EAF_pct":10.2,"BOF_oxygen_pct":89.8,"year":2024},
 {"geo":"Italy","EAF_pct":89.3,"BOF_oxygen_pct":10.7,"year":2024},
 {"geo":"EU27","EAF_pct":44.4,"BOF_oxygen_pct":55.6,"year":2024},
 {"geo":"Japan","EAF_pct":26.2,"BOF_oxygen_pct":73.8,"year":2024}]).to_csv(f"{RES}/claim_C4_worldsteel2024.csv",index=False)
pd.DataFrame([{"year":2000,**{k:v for k,v in c23['bw_modern']['2000'].items()}},
              {"year":2024,**{k:v for k,v in c23['bw_modern']['2024'].items()}}]).to_csv(f"{RES}/claim_C23_bw.csv",index=False)

# verdict counts
from collections import Counter
graded=[r for r in rows if r["id"]!="P2"]
def bucket(v):
    if v=="supported": return "supported"
    if v=="partially supported": return "partially supported"
    if v=="contradicted": return "contradicted"
    return "not-checkable"
c=Counter(bucket(r["verdict"]) for r in graded)
print("rows:",len(rows))
print("counts (excl P2):",dict(c))
for r in rows: print(f'  {r["id"]:7s} {r["verdict"]}')
json.dump(dict(c),open(f"{RES}/_verdict_counts.json","w"))
