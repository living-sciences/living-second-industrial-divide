# Provenance — extension-assets (Phase 2a staging, 2026-10-27)

All files fetched keyless on 2026-10-27 from live endpoints by the Phase 2a
recency-research agent (census-statab/ added by the 2b revision agent, same
date). Total footprint 11,697,313 B ≈ 11.7 MB by `du -sb` (CORRECTED per
PS-C3c — the earlier "≈8.1 MB" understated the two WTO PDFs; box at 98%:
filtered extracts only; nothing near the 1 GB BATCH.md log threshold).
sha256 computed on staged files. Licenses permit internal analysis and public citation; the WTO and
worldsteel PDFs are redistributable-with-attribution documents but should be
LINKED, not re-hosted, in the public repo.

## worldbank-wdi/ — World Development Indicators (CC BY 4.0)

- `wdi_manufacturing_trade_1960_2025.csv` (332,627 B)
  sha256 6e33494746a95aa2ee9a7933ac6388915203e2c070e1489b73d7022b36342bdc
  API: `https://api.worldbank.org/v2/country/CHN;USA;JPN;DEU;KOR;ITA;FRA;GBR;MEX;VNM;IND;BRA;WLD/indicator/{NV.IND.MANF.CD,NV.IND.MANF.ZS,TX.VAL.MRCH.CD.WT,TX.VAL.MANF.ZS.UN,NE.TRD.GNFS.ZS}?format=json&date=1960:2025`
  Source last updated 2026-10-08 (API header). Sanity: CHN manuf VA 2023
  $4.57T; CHN share of WLD manuf VA 2023 = 27.9% (matches Schwartz 2024's
  "29% of value added" within revision noise).
- `wdi_durables_diffusion_demand_side.csv` (1,452 rows)
  sha256 4919c90924067d434057b0159cd634c1e6d6aa8a0025ad598e0404aa515e39eb
  Same API; indicators PRESENT IN THE FILE: IT.CEL.SETS.P2 (mobile
  subs/100) and NE.CON.PRVT.PP.KD only. CORRECTION (PS-A2a, 2026-10-27):
  IS.VEH.NVEH.P3 (motor vehicles/1000) was queried but the API RETURNED NO
  DATA ROWS — the indicator is archived at source (the v2 data endpoint
  answers "deleted or archived"; re-verified by the 2b revision agent) —
  so it is NOT staged and is NOT in this CSV; spec and recency references
  to a vehicles column have been removed. Countries
  CHN;IND;VNM;BRA;MEX;IDN;WLD;USA;DEU;JPN;KOR. Demand-side leg for
  P2's "global mass-consumption market" half (mobile subscriptions only).

## wits-intermediates/ — World Bank WITS / UN Comtrade (free re-use w/ attribution)

- `wits_unctad_sop_product_shares.csv`
  sha256 e3efc0453b8d115126062a11df82a47c3752c48c4f7e13a17e70341e1cb809ce
  API: `https://wits.worldbank.org/API/V1/SDMX/V21/datasource/tradestats-trade/reporter/{wld,chn,usa,deu}/year/all/partner/wld/product/UNCTAD-SoP{1..4}/indicator/{XPRT,MPRT}-PRDCT-SHR?format=JSON`
  Coverage verified: 1988-2023, world + CHN/USA/DEU, export+import shares by
  UNCTAD Stages-of-Processing class (1 raw, 2 intermediate, 3 consumer,
  4 capital). DATA SEAM (binding on use): UNCTAD-SoP "intermediate goods"
  (~20-24% of world exports, flat) is NARROWER than the BEC-based
  "intermediates ≈ half of world trade" definition used by WTO/Baldwin —
  parts & accessories sit partly under capital goods. Studies must use the
  within-series TREND, never compare the level to BEC-based claims.

## census-bds/ — US Census Business Dynamics Statistics 2023 release (public domain)

- `bds2023_ez.csv` (57,449 B) — economy-wide, by establishment size, 1978-2023.
  sha256 c3310039b69987ee5838826a626bbf00d0bfa3dba79a805ae03572fdd8b116ca
- `bds2023_sec_ez.csv` (942,352 B) — sector × establishment size, 1978-2023
  (manufacturing = NAICS sector 31-33).
  sha256 ccc20556eca518bd1c285212642fee74e1c622167b3bb660fe5f630f082219d8
  URL: `https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/`
  (verified live; the pre-2021 `esize`/`sec_esize` filenames are retired —
  current names are `_ez`/`_sec_ez`). Covers D1 (plant-size trend) 1978-2023;
  the 1963-1977 segment of D1 relies on Census of Manufactures values from the
  quoting literature (double-sourced), declared in the spec.

## eurostat/ — Eurostat dissemination API (CC BY 4.0)

- `nama_10r_2gdp_emilia_romagna.json` — regional GDP per head (EUR_HAB +
  PPS_EU27_2020_HAB), geo ITH5 (Emilia-Romagna), ITH, ITC4 (Lombardia), IT,
  EU27_2020; 2000-2024 (250 obs).
  sha256 54ac84e960db2da1c4581a854f64b5b1c9f9b2c667b5c77ed5ef1f92b591bc4a
- `sbs_sc_ind_r2_manufacturing_sizeclass.json` — SBS industry by employment
  size class, NACE C, 2005-2020 (820 obs; indic_sb V16110 persons employed,
  V11110 enterprises), EU27/IT/DE/FR/ES.
  sha256 074258f2d4af172daa4594053e548caa6936a204909de7f3063a9f5542f6991d
- `sbs_sc_ovw_manufacturing_sizeclass.json` — successor dataset, 2021+ (240
  obs; EMP_NR, ENT_NR). DATA SEAM: indicator codes and size-class breaks
  change at the 2020/2021 dataset boundary; series must be spliced with the
  overlap documented, or shown as two panels.
  sha256 f286f523317f80b792c87b1abd23631a20ef3c4b9cc270f82b8d25abf2afb25d
  API: `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/<dataset>?...&format=JSON&lang=EN`

## steel/ — claim C4 leg

- `world-steel-in-figures-2025.pdf` (2.8 MB) — worldsteel, World Steel in
  Figures 2025. Crude steel production by process (BOF/EAF) by country,
  2022-2024 (e.g. China ≈91.6% oxygen / 8.4% electric — the H-A signature;
  US majority-EAF — the book's C4 win at its 2026 endpoint).
  sha256 a830f0b9cb8237dc5131145cffb8ff6eb7ce5b5f0930f6abf8ff6fc383da48d4
  URL: `https://worldsteel.org/wp-content/uploads/World-Steel-in-Figures-2025.pdf`
  (free publication; link, don't re-host).
- **BLOCKED FETCH (recorded, not staged): USGS DS140 iron & steel historical
  statistics** `https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/ds140-iron-steel-2021.xlsx`
  (link verified via the USGS page through Wayback) — USGS CloudFront returns
  403 to this box (bot filter); no circumvention attempted (anti-bot-bypass
  rule). Public domain; a HUMAN BROWSER FETCH staged under
  `shared-data/steel/` before launch is the ONLY supply route — spec I.3 is
  binding and forbids any in-run attempt against the blocked CDN (aligned
  per PS-C3b; this file previously said "or in-run retry", which was wrong).
  The series: annual US raw-steel-by-furnace-type, 1900-2021. Fallback for the
  1970-1984 EAF share: USBM Minerals Yearbook "Iron and Steel" chapters
  (public domain, scanned at UW-Madison digital library + HathiTrust),
  double-sourced with Barnett & Crandall (1986) as quoted in the OA
  literature.

## owid-durables/ — Our World in Data (CC BY; underlying: Comin & Hobijn CHAT)

- `us_household_technology_adoption.csv` — US household/technology adoption
  shares, long series; leg for claim B1 (saturation by early 1970s). B1
  uses the entities `Automobile` (1915-2005), `Household refrigerator`
  (1931-2017), `Washing machine` (1930-2008) — NOT the shorter duplicates
  `Refrigerator`/`Washer`. CAVEAT (PS-A2b): `Television` covers 1992-2018
  only and `Colour TV` (1966-2005) was mid-diffusion in 1973, so the TV
  series for B1 comes from `census-statab/` (above), with the source split
  disclosed in the row and on the card.
  sha256 4436d028351dd2e1deae5521db76f77a8b3b6b72a75fb1d2ca88ba9ff518cc5a
  URL: `https://ourworldindata.org/grapher/technology-adoption-by-households-in-the-united-states.csv`

## census-statab/ — US Census Statistical Abstract historical table (public domain; added at the 2b revision, PS-A2b)

- `hs-42-selected-communications-media-1920-2001.pdf` (82,120 B) — "No.
  HS-42. Selected Communications Media: 1920 to 2001", mini historical
  statistics appendix, Statistical Abstract of the United States 2003
  (123rd ed.). Column "Percent of households with Television" 1950-2001
  (1973 = 96.4; 1984 = 98.1) — B1's TV-penetration series, staged because
  the OWID file's `Television` entity starts 1992 and `Colour TV`
  (1966-2005) was still mid-diffusion in 1973.
  sha256 55804674e8ecb19d565476e2359fccfa62fad9f2e455f57bbe9b432a52b0d7c4
  URL: `https://www2.census.gov/library/publications/2004/compendia/statab/123ed/hist/hs-42.pdf`
  Fetched keyless 2026-10-27. US government work, public domain.

## wto-gvc-report/ — WTO Global Value Chain Development Report 2025 (free publication)

- `gvcreport2025-01_e.pdf` (1.6 MB) — ch.1 "Recent Developments in GVCs".
  sha256 50de298a3b30a86cb998180fd0cd0f60799388b50d27c2f3daaf678652843dca
- `gvcreport2025-02_e.pdf` (5.6 MB) — ch.2 "Resilience and Reglobalization:
  GVC Trends" (GVC participation slowed/plateaued since 2011; US-China
  decoupling ~30%; Mexico overtook China as top US import source late 2023).
  sha256 f79ca87c10b5b3cdc80a4958125d94b3804b5344f5f3d89b13b37fb8e16b9131
  URLs: `https://www.wto.org/english/res_e/booksp_e/gvcreport2025-0{1,2}_e.pdf`
  Role: authoritative 2025-vintage GVC-trend numbers + staged fallback for the
  OECD TiVA endpoint (below). Link, don't re-host.

## DEGRADED ENDPOINT (recorded): OECD TiVA 2025 edition

Dataflow `OECD.STI.PIE:DSD_TIVA_MAINSH@DF_MAINSH(1.1)` ("TiVA 2025 edition:
Principal Indicators, shares") CONFIRMED to exist 2026-10-27 via the structure
API (`https://sdmx.oecd.org/public/rest/dataflow/OECD.STI.PIE`), but every data
query (`/public/rest/data/...`) returned HTTP 500 "Internal server error" or
403 "Invalid structure" across formats and key shapes, while other OECD flows
(e.g. DSD_STES@DF_CLI) answered normally — the TiVA flow itself was broken
server-side on the verification date. Study 002 carries a retry-with-recorded-
query branch (preferred if the endpoint recovers: measures EXGR_FVASH-family
backward/forward participation, 1995-2020+) and a staged fallback (WTO GVC
Report 2025 chapter data + WITS intermediates trend). No key or login is
involved either way.

## GATED (honest exclusion, H3): UNIDO INDSTAT

INDSTAT 2/4 (establishment counts/employment by country, incl. China) requires
free registration — a human gate per batch rules. NOT staged; NOT worked
around. The cross-country plant-size leg of H-A runs on its honest-exclusion
branch (BDS + Eurostat SBS + literature values for China plant scale) unless
H3 clears before launch.
