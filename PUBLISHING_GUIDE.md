# Publishing Guide — Olfactory Constellation
**Author: Rick Scianablo Jr · 2026**

This is your step-by-step to publishing the tool and getting a permanent, citable DOI in your
name. Do the steps in order. You need a computer for Steps 3–6 (GitHub + Zenodo web uploads).

---

## The deliverables — what each file is and where it goes

| File | What it is | Where it goes |
|---|---|---|
| `README.md` | Front page of your project; explains the tool, method, licensing | **Repo root** (GitHub shows it automatically) |
| `LICENSE` | MIT license, you as copyright holder | **Repo root** |
| `CITATION.cff` | Machine-readable author metadata (drives "Cite this repo" + Zenodo author) | **Repo root** |
| `ANNOUNCEMENT.md` | Full release announcement | **Repo root**, or a `/docs` folder |
| `BLURB.md` | Short social/repo-header text (3 lengths) | Use for the GitHub repo *description* + posts; keep the file in **repo root** |
| `PUBLISHING_GUIDE.md` | This file | **Repo root** (or keep locally — your call) |
| `resolve_cas.py` | Local script: pulls names/CAS from PubChem by structure | **Repo root** or a `/scripts` folder |
| `olfactory_constellation.html` | Interactive structural map (self-contained) | **Repo root** or `/viewers` |
| `perceptual_constellation.html` | Interactive perceptual map (self-contained) | **Repo root** or `/viewers` |
| `master_odor_map.csv` | Example build output (data table) | **`/examples`** — see the licensing note in Step 0 |
| `master_odor_map.xlsx` | Same, spreadsheet form | **`/examples`** — see Step 0 |

Simplest layout that works: put everything in the repo root. The folders above are optional tidiness.

---

## STEP 0 — Before you publish (the one thing to decide)

The two `master_odor_map` files were built using name data routed through GoodScents/Leffingwell,
which does **not** carry a redistribution license. **Two safe options:**

- **Option A (cleanest):** Do **not** upload the `master_odor_map` files. Publish the tool +
  viewers only. Users generate their own table by running the tool. Zero data-license risk.
- **Option B:** Regenerate the table with names sourced from **PubChem** (run `resolve_cas.py`
  first, drop the GoodScents-derived name column), then upload that clean version.

If unsure, choose **Option A**. The tool is the contribution; the table is just a demo output.

---

## STEP 1 — Get an ORCID (5 minutes, free, do this first)

1. Go to **orcid.org** → Register.
2. Copy your new ORCID iD (looks like `0000-0002-1825-0097`).
3. Open `README.md` — paste it into the author line where it says *[register free at orcid.org…]*.
4. Open `CITATION.cff` — find the line `# orcid: "https://orcid.org/0000-0000-0000-0000"`,
   remove the `#`, and put your real iD in.

This permanently ties the work to **you** as a person, not just a name.

---

## STEP 2 — Fill remaining blanks

- `LICENSE` — already says "© 2026 Rick Scianablo Jr". Update the year if publishing later.
- `README.md` / `ANNOUNCEMENT.md` — the DOI placeholder fills itself in after Step 5.

---

## STEP 3 — Create the GitHub repository

1. Go to **github.com**, sign in (or create a free account).
2. Click **New repository**.
3. Name it: `olfactory-constellation`.
4. Description (paste the one-liner from `BLURB.md`):
   *"An open tool that maps molecules by structure and by smell — and flags where the two disagree."*
5. Set to **Public**. Do **not** add a license from GitHub's menu (you already have `LICENSE`).
6. Click **Create repository**.

---

## STEP 4 — Upload your files to GitHub

Easiest (no command line):
1. On the new empty repo page, click **"uploading an existing file"**.
2. Drag in every deliverable you're publishing (see Step 0 about the master_odor_map files).
3. Scroll down, click **Commit changes**.

GitHub will automatically render `README.md` as your project's front page and, because
`CITATION.cff` is present, add a **"Cite this repository"** button.

---

## STEP 5 — Connect Zenodo to mint your DOI

1. Go to **zenodo.org** → **Log in with GitHub** (authorizes the connection).
2. Go to **zenodo.org/account/settings/github/**.
3. Find `olfactory-constellation` in the list and flip its switch **ON**.
   (This tells Zenodo to archive the repo whenever you publish a release.)

---

## STEP 6 — Publish a release (this is what creates the DOI)

1. Back on your GitHub repo, click **Releases** (right side) → **Create a new release**.
2. Tag version: `v1.0`. Release title: `Olfactory Constellation v1.0`.
3. Description: paste the summary paragraph from `ANNOUNCEMENT.md`.
4. Click **Publish release**.
5. Within a minute, Zenodo archives it and issues a **DOI**. Find it at
   **zenodo.org** under your uploads (it shows a DOI badge).

---

## STEP 7 — Close the loop

1. Copy your new DOI.
2. Paste it into `README.md`, `ANNOUNCEMENT.md`, and `CITATION.cff` (replace the placeholders).
3. Commit those edits. (Optional: cut a `v1.0.1` release so the DOI-in-README is archived too.)
4. Add the DOI badge to your README top — Zenodo gives you the markdown for it.

**Done.** Your tool is public, permanently archived, and citable as:
> Rick Scianablo Jr (2026). *Olfactory Constellation* (v1.0) [Software]. Zenodo. https://doi.org/…

---

## Optional next steps

- Share the `BLURB.md` tweet-length text with a link to the repo.
- Add ORCID's "add works" so this shows on your ORCID profile automatically.
- If you later run a validation experiment, cut a new release — each gets its own versioned DOI,
  and all versions share one "concept DOI" that always points to the latest.
