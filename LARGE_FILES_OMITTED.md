# Files not included, and where they came from

Nothing was cut for size; everything omitted is either in copyright, someone else's to
distribute, or regenerable from what is here. Exact URLs, byte counts, sha256 hashes and
fetch dates for every omitted input are in the shipped provenance registers,
`package/PROVENANCE.md` and `extension-assets/PROVENANCE.md`.

## The book itself

No text of *The Second Industrial Divide* ships in this repository, in any form. The
book is in copyright (Basic Books, 1984; paperback 1986; still in print) and no lawful
machine-readable full text is freely obtainable. Lawful access routes (purchase,
Internet Archive controlled digital lending item `secondindustrial00pior`, Google Books
snippet view) are documented in `package/book.metadata.md`. The studies never read the
book; see the PROVISIONAL-PENDING-H1 section of the README.

## Literature staged for internal verification (never redistributable here)

These four files were used to verify claim attributions and governance codings and are
flagged INTERNAL ONLY in `package/PROVENANCE.md`; cite the canonical records instead:

| Omitted | Why | Canonical record |
|---|---|---|
| Gereffi, Humphrey & Sturgeon (2005), "The governance of global value chains" (PDF from an FAO courtesy mirror) | Taylor & Francis paywalled journal article; the mirror copy is not redistributable | *Review of International Political Economy* 12(1):78-104, doi:10.1080/09692290500049805 |
| Sturgeon (2008), "From Commodity Chains to Value Chains", ISA WP 2008-02 | Carries an explicit Stanford UP "no further reproduction" notice | Published as ch. in J. Bair (ed.), *Frontiers of Commodity Chain Research*, Stanford UP 2009; WP at https://isapapers.pitt.edu/84/ |
| Berger (2013), "Toward a Third Industrial Divide?" (author manuscript, DSpace@MIT) | MIT Press book chapter; the OA manuscript is the author's to host, not ours | Ch. 3 of P. Osterman (ed.), *Economy in Society*, MIT Press 2013, ISBN 9780262018241; hdl:1721.1/96124 |
| Bhengu (2001), UCT Master's thesis on flexible specialisation | UCT non-exclusive license (private study or non-commercial research only); quotes routed through it are fair-use length and name the thesis | hdl:11427/10097 (OpenUCT) |

## Free publications, linked rather than re-hosted

| Omitted | Why | Provenance / how to get it |
|---|---|---|
| worldsteel, *World Steel in Figures 2025* (2.8 MB PDF) | Free publication; the staging decision is to link, not re-host | https://worldsteel.org/wp-content/uploads/World-Steel-in-Figures-2025.pdf (sha256 in `extension-assets/PROVENANCE.md`) |
| WTO, *Global Value Chain Development Report 2025*, chapters 1 and 2 (PDFs) | Free publication; link, not re-host | https://www.wto.org/english/res_e/booksp_e/gvcreport2025-01_e.pdf and ...-02_e.pdf (sha256 in `extension-assets/PROVENANCE.md`) |
| Schwartz (2024), "Brave New World: A third industrial divide?" (HTML) | Web essay, copyright Phenomenal World / author; cite and quote with attribution, do not re-host | https://phenomenalworld.org/analysis/a-third-industrial-divide/ |
| Hampson (1991), "Post-Fordism, the 'French Regulation School', and the Work of John Mathews" (PDF) | Journal's own open archive; link, not re-host | *Journal of Australian Political Economy* 28; https://www.ppesydney.net/content/uploads/2020/05/Post-Fordism-the-French-regulation-school-and-the-work-of-John-Mathews.pdf |
| Carlsson (1988), IUI Working Paper No. 203 (PDF) | Institute-posted working paper; canonical link kept | https://www.ifn.se/media/baeprbee/wp203.pdf |
| Rinaldi, DEMB working paper on Emilia-Romagna's long-run income (PDF) | Open institutional repository; canonical link kept. The graded C1 historical values come from this paper | https://iris.unimore.it/retrieve/handle/11380/1299317/565434/Rinaldi_Materiali%20Discussione_0684.pdf |
| ISTAT, "Storie di dati regionali: Emilia-Romagna" factsheet (PDF) | CC BY, but staged as context only; no graded value traces to it | https://www.istat.it/wp-content/uploads/2026/10/08-Storiedidatiregionali-EMILIA-ROMAGNA.pdf |
| Kaplinsky (2023), "Global Value Chains: the Rise (and Fall?) of Deep Globalisation" (PDF) | Open access at the journal and repository; link kept canonical | *Papeles de Europa* 36, doi:10.5209/pade.87812 |
| Baldwin (2006), "Globalisation: the great unbundling(s)" (PDF) | Freely distributed government-commissioned report; repository link kept canonical | https://repository.graduateinstitute.ch/record/295612 |
| Wayback snapshot of Charles Sabel's Columbia paper archive (HTML) | Provenance evidence only, untouched by the studies | web.archive.org snapshot 2012-06-08 of www2.law.columbia.edu/sabel/papers.htm |

## Regenerable or internal run machinery

| Omitted | Why | How to reconstruct |
|---|---|---|
| `workspace/pdftext/` text extractions inside studies 001 and 002 | pdftotext conversions of the omitted literature above; shipping them would re-host the texts | Re-fetch each document per the provenance registers and run `pdftotext -layout` into `workspace/pdftext/` with the filenames the scripts expect |
| The run-time staging mirror the scripts read (`followup_staging/shared-data/`) | Byte-identical to `extension-assets/` (the shipped subset) plus the omitted literature above; both studies sha256-verified all 13 staged data files against the shipped registers at run start | Lay the shipped `extension-assets/` folders plus re-fetched literature out as `shared-data/` per the paths in `workspace/build_gates.py` |
| Run transcripts, lane logs and the internal book-record scaffold | Internal run machinery, never published | Not applicable; every number they support is traceable through the shipped results, gates and fetch logs |
