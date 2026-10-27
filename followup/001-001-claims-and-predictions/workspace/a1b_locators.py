import json, os

SD = "/workspace/eval/followup_staging/shared-data/literature"
TXT = "/workspace/eval/followup/001-001-claims-and-predictions/workspace/pdftext"

# Load sources: SCHW = raw html; others = normalized pdftext
def load(name, kind):
    if kind == "html":
        with open(os.path.join(SD, "schwartz2024_third_divide.html"), encoding="utf-8", errors="replace") as fh:
            return fh.read()
    with open(os.path.join(TXT, name + ".txt"), encoding="utf-8", errors="replace") as fh:
        return fh.read()

SRC = {
    "SCHW": load("schwartz2024_third_divide", "html"),
    "BERG": load("berger2013_toward_third_industrial_divide", "pdf"),
    "BHEN": load("bhengu2001_uct_thesis_flexible_specialisation", "pdf"),
    "HAMP": load("hampson1991_postfordism_regulation_school_jape28", "pdf"),
    "CARL": load("carlsson1988_iui_wp203_manufacturing_technology_plant_size", "pdf"),
    "RIN":  load("rinaldi-emilia-romagna-income-history", "pdf"),
    "STUR": load("sturgeon2008-commodity-to-value-chains-isa-wp", "pdf"),
}

# (row, source, locator, expected_count)
LOCATORS = [
    ("B1","BHEN","by 1979 there was one car for every",1),
    ("B1","BHEN","households had television sets by 1970",1),
    ("B1","BHEN","(Piore & Sabel, 1984: 184)",1),
    ("B1","BERG","saturation of mass consumer-good markets",1),
    ("B1","HAMP","According to Piore and Sabel, domestic markets for mass produced goods became saturated",1),
    ("B2","BHEN","Given the rigid wages and prices central to the system of macroeconomic regulation",1),
    ("B2","BHEN","(Piore & Sabel, 1984: 176)",1),
    ("B2","SCHW","overly rigid production structure",1),
    ("B2","SCHW","presented a multitude of shocks",1),
    ("B3","SCHW","overly rigid production structure",1),
    ("B3","HAMP","the limits of the model of industrial development that is founded on mass production",1),
    ("C1","SCHW","ideal model for a better future",1),
    ("C1","RIN","Piore e Sabel 1984",1),
    ("C1","STUR","provided by Piore and Sabel (1984)",1),
    ("C5","BHEN","the application of computers to industry favours flexible systems",1),
    ("C5","BHEN","(Piore & Sabel, 1984: 258)",1),
    ("C5","BHEN","programmable equipment is used just as automatic machinery was used in the past",1),
    ("C5","BHEN","(Piore & Sabel, 1984: 261)",2),
    ("C5","BERG","computer-aided manufacturing (programmable assembly) might make it efficient and profitable to adjust equipment",1),
    ("D1","SCHW","shrink themselves via outsourcing and demerger",1),
    ("D1","SCHW","drove the vertical disintegration that",1),
    ("D1","CARL","have argued that the United States is currently in a period of transition from mass production to",1),
    ("D1","CARL","average establishment size declined by 12.3",1),
    ("C2C3","BERG","the Italian and French industrial districts and the German and Japanese middle-firm sectors",1),
    ("P1","SCHW","improbable expansion of mass production and thus Keynesian policy of demand management to the global level",1),
    ("P1","BERG","One family of solutions would be a global Keynesianism",1),
    ("P1","BERG","multinational Keynesian order",1),
    ("P2","SCHW","They saw only two paths out of the problems animating the debate",1),
    ("P2","BERG","apportion the expansion of productive capacity among the advanced industrial countries",1),
    ("P2","BHEN","They moved into mass-produced consumer durables",1),
    ("P2","BHEN","(Piore & Sabel, 1984: 188)",1),
    ("P3","SCHW","The other was a transformation of the industrial base in the direction of flexible specialization",1),
    ("P3","SCHW","narrow slice of industrial output",1),
    ("P3","SCHW","a potential second divide, for a return to flexible specialization",1),
    ("P3","BERG","nourish and strengthen flexible specialization and craft production",1),
    ("P4","HAMP","a political choice between the technology of",1),
    ("P4","SCHW","utter indeterminacy of any given divide",1),
]

results = []
for row, src, loc, exp in LOCATORS:
    text = SRC[src]
    cnt = text.count(loc)
    results.append({"row":row,"source":src,"locator":loc,"expected":exp,"count":cnt,
                    "hit": cnt>=1, "meets_expected": cnt==exp})

for r in results:
    flag = "OK" if r["meets_expected"] else ("HIT-NONEXPECTED" if r["hit"] else "MISS")
    print(f'{flag:17s} {r["row"]:5s} {r["source"]:5s} cnt={r["count"]} exp={r["expected"]}  {r["locator"][:60]}')

with open("/workspace/eval/followup/001-001-claims-and-predictions/workspace/a1b_results.json","w") as fh:
    json.dump(results, fh, indent=2)
