# Release Announcement — Olfactory Constellation

**A new open tool for exploring how molecular structure, vibration, and smell connect —
and for finding where they surprisingly don't.**

*Released 2026 · Author: Rick Scianablo Jr · MIT License (software)*

---

## Summary

**Olfactory Constellation** is a newly released open-source tool that turns public olfaction
data into two interactive maps of chemical space — one organized by molecular **structure**, the
other by **odor similarity** — and automatically flags the molecules where those two views
disagree. It is, to the author's knowledge, the first freely available tool to place
structure, vibrational-spectra-derived clustering, odor perception, and chemical identity into a
single explorable object with a built-in structure-versus-smell comparison.

The tool ships with no proprietary data. It processes datasets the user supplies from their
original sources, and builds everything locally.

---

## What it actually does

- **Two-lens mapping.** The same molecules are laid out twice: once by structural fingerprint
  similarity, once by odor-descriptor similarity (rarity-weighted). Comparing the two views
  makes the relationship between chemistry and perception visible.
- **Activity-cliff detection.** The tool automatically identifies molecules that are nearly
  structurally identical to a neighbour yet share almost no odor in common — the long-standing
  "structure-odor discontinuity" that has made smell so hard to predict. In a representative
  build, hundreds of such cliffs surface at a glance.
- **Vibrational-cluster context.** Where vibrational-spectra data is supplied, molecules carry
  their cluster membership, letting users explore how spectrally grouped ("oscillating")
  molecules relate to odor families.
- **Interactive, self-contained viewers.** Pan, zoom, search by name or odor, filter by family,
  and inspect any molecule's identity, formula, weight, functional groups, and smell.

*What it does not do: it does not predict a molecule's smell from first principles, and it does
not establish that smell is determined by molecular frequency. It is an exploration and
cross-referencing instrument, not a predictive or explanatory model.*

---

## Why it matters

Predicting odor from molecular structure is a 70-year-old open problem. A major reason is that
structure and smell don't map cleanly onto each other — small structural changes can abolish or
transform a scent, while large ones sometimes leave it untouched. Most tools show one view of
chemical space at a time. By showing structure and perception side by side and surfacing the
points where they diverge, this tool makes the *disagreement itself* the object of study — which
is exactly where the interesting science in olfaction lives.

---

## Forward-looking: open questions this tool is built to help investigate

*The following are research directions and hypotheses — not results, and not claims of a proven
mechanism. They describe what a tool like this could help explore.*

- **Vibration as an organizing axis.** One long-debated hypothesis (the vibrational theory of
  olfaction) proposes that molecular vibrational frequencies contribute to how a molecule smells.
  This remains contested and is not established science. Because this tool can cluster molecules
  by vibrational-spectra-derived features and lay them beside odor structure, it offers a way to
  *visually interrogate* how well spectral grouping tracks perceived odor — a question that
  benefits from an interactive, side-by-side view rather than a single summary statistic.
- **Mappable spectral clusters.** If subsets of "oscillating" (spectrally similar) molecules do
  correspond to coherent odor regions, the perceptual map should reveal them as clusters. Where
  they don't correspond, the activity-cliff view should expose the mismatch. Either outcome is
  informative.
- **A shared coordinate frame.** Bringing structure, spectra, identity, and percept into one
  navigable space is a prerequisite for asking sharper questions about which molecular properties
  actually carry odor information.

These are invitations to investigate, offered to the olfaction and cheminformatics communities —
not conclusions.

---

## Availability

Open-source under the MIT License (software only). The tool contains and redistributes no
third-party data; users supply datasets under those datasets' own terms. Method, code, and
interactive viewers are archived with a citable DOI.

**Cite as:** Rick Scianablo Jr (2026). *Olfactory Constellation: a tool for cross-referencing
molecular structure, vibrational data, and odor* (Version 1.0) [Software]. Zenodo.
DOI: 10.5281/zenodo.21184930

*Foundational data sources — including Ameta et al. (2024, Scientific Reports) for vibrational
and odor data — should be cited by users according to those sources' terms. The structure-odor
discontinuity ("activity cliff") framing follows Sanchez-Lengeling et al. (2019).*

---

## A note on claims

This release is presented as a **tool and method**, not as a scientific breakthrough or a proof
of any mechanism of smell. Its contribution is making existing data explorable in a new,
cross-linked way and surfacing structure-odor mismatches automatically. Any stronger claim about
how smell works would require experimental validation beyond the scope of this software.
