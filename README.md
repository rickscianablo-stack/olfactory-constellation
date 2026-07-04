# Olfactory Constellation — a tool for cross-referencing structure, vibration, and odor

**Olfactory Constellation is software.** It takes public olfaction datasets that *you* obtain
from their original sources and turns them into two interactive maps of chemical space — one
laid out by molecular structure, one by odor similarity — and it flags "activity cliffs" where
near-identical molecules smell completely different.

This repository contains the **pipeline and the interactive viewers**. It does **not** contain,
redistribute, or claim ownership of any underlying chemical, odor, or naming data. You point the
tool at data you have the right to use, and it builds the maps on your machine.

**Author & copyright holder:** Rick Scianablo Jr (2026) — author of the software, the cross-linking method, the two-lens (structural + perceptual) layout, and the activity-cliff detection.
**ORCID:** _[0009-0005-8713-9041]_

---

## What this tool does (and what it is not)

**It is:** a reproducible method + code — SMILES canonicalization and deduplication, a structural
embedding (Morgan/Tanimoto k-NN + force layout), a perceptual embedding (TF-IDF-weighted
odor-vector cosine k-NN + force layout), structure-derived enrichment, activity-cliff detection,
and two self-contained HTML viewers.

**It is not:** a dataset. No odor labels, vibrational data, molecule names, or identifiers are
included or redistributed here. Those remain the property of their respective sources under their
own terms.

---

## What is claimed here

Only the **software and the analytical method** — the pipeline, the two-lens layout approach, the
activity-cliff detection, and the viewers. Released under the **MIT License** (see `LICENSE`).

No claim is made over any input data, and nothing in this repository grants you rights to any
third-party dataset. Whether you may download, use, or share a given input dataset is governed
solely by that dataset's own license and terms — check them yourself before running the tool.

---

## Inputs you provide (from their original sources, under their own terms)

The tool expects, as local files you have obtained and are permitted to use:

1. **Vibrational + odor data** — e.g. the supplementary tables from Ameta et al. (2024),
   *Scientific Reports* 14:20321 (published open access, CC-BY). Download from the publisher.
2. **Molecule identity (names / IUPAC / CAS)** — obtain from **PubChem** (freely usable public
   data) via the included `resolve_identity.py`, keyed by structure. Do **not** substitute
   sources whose terms forbid redistribution if you intend to share your build outputs.

The tool reads these, builds the maps locally, and writes outputs to your machine. Redistribution
of the *outputs* is your responsibility and depends entirely on the input licenses.

---

## Usage

```bash
pip install rdkit pandas numpy networkx openpyxl requests
# 1. place your input file(s) alongside the scripts
# 2. resolve identities from PubChem (public data):
python resolve_identity.py
# 3. build the compilation + both maps:
python build.py
```

Outputs (written locally, not distributed with this tool): master.csv, master.xlsx,
olfactory_constellation.html, perceptual_constellation.html.

---

## Please cite the tool, and cite your data sources separately

**Tool:**
> Rick Scianablo Jr (2026). *Olfactory Constellation: a tool for cross-referencing molecular
> structure, vibrational data, and odor* (Version 1.0) [Software]. Zenodo.
> https://doi.org/10.5281/zenodo.21184930 - ORCID: 0009-0005-8713-9041

**Whichever data you feed it — cite the original source, e.g.:**
- Ameta, D., Behera, L., Chakraborty, A., & Sandhan, T. (2024). Predicting odor from vibrational
  spectra: a data-driven approach. *Scientific Reports, 14*, 20321.
  https://doi.org/10.1038/s41598-024-70696-w
- PubChem — Kim, S. et al. *Nucleic Acids Research* (identity data).
- Sanchez-Lengeling, B. et al. (2019). Machine Learning for Scent. *arXiv:1910.10685.*
  (activity-cliff concept)
- RDKit: Open-source cheminformatics. https://www.rdkit.org

---

## Publishing this tool to get credit

1. **ORCID** (orcid.org) — free permanent researcher ID; add it to the author line.
2. **GitHub** — host the code and viewers as the living project.
3. **Zenodo** (zenodo.org) — connect the GitHub repo; each release is archived with a citable
   **DOI**. That DOI credits *you* for the tool.

Framing it as a **tool/method** is both the safest position and the stronger claim: the novelty
here is the cross-linking approach and the two-lens visualization, not the data it runs on.

---

## Disclaimer

Provided "as is," without warranty. This tool does not grant rights to any third-party data.
Users are solely responsible for ensuring their use of any input dataset complies with that
dataset's license and terms. This document is practical guidance, not legal advice.
