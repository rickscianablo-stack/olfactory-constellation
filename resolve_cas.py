#!/usr/bin/env python3
"""
Olfactory Constellation — part of the toolset.
Author & copyright holder: Rick Scianablo Jr (2026). MIT License.
This software grants no rights to any third-party data it processes.
"""
"""
resolve_cas.py  —  Add PubChem CID + CAS numbers to master_odor_map.csv

WHY THIS IS A SEPARATE SCRIPT:
CAS numbers live on PubChem, which the build environment couldn't reach.
Your machine can. Run this once locally and it fills in CID + CAS by structure.

USAGE:
    pip install requests pandas
    python resolve_cas.py master_odor_map.csv

It writes master_odor_map_with_cas.csv and checkpoints as it goes, so you can
stop and re-run — it skips rows already resolved.

Notes:
- Matching is by SMILES -> PubChem CID -> CAS (from PubChem's synonym list,
  first token matching the CAS pattern).
- PubChem asks for <=5 requests/sec; this script stays well under that.
- Expect a fraction of obscure structures to have no CID or no listed CAS.
"""
import sys, time, re, csv, os
import pandas as pd
import requests

CAS_RE = re.compile(r"^\d{2,7}-\d{2}-\d$")
BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "odor-map-cas-resolver/1.0"})


def cid_from_smiles(smiles):
    try:
        r = SESSION.get(f"{BASE}/compound/smiles/{requests.utils.quote(smiles)}/cids/JSON", timeout=20)
        if r.ok:
            return r.json().get("IdentifierList", {}).get("CID", [None])[0]
    except Exception:
        pass
    return None


def cas_from_cid(cid):
    try:
        r = SESSION.get(f"{BASE}/compound/cid/{cid}/synonyms/JSON", timeout=20)
        if r.ok:
            syns = r.json()["InformationList"]["Information"][0].get("Synonym", [])
            for s in syns:
                if CAS_RE.match(s.strip()):
                    return s.strip()
    except Exception:
        pass
    return None


def main(path):
    df = pd.read_csv(path)
    out_path = path.replace(".csv", "_with_cas.csv")
    if os.path.exists(out_path):                       # resume
        done = pd.read_csv(out_path)
        df = df.merge(done[["smiles", "pubchem_cid", "cas"]], on="smiles", how="left")
    else:
        df["pubchem_cid"] = None
        df["cas"] = None

    todo = df[df["cas"].isna()]
    print(f"{len(df)} rows | {len(todo)} still need resolving")

    for count, (i, row) in enumerate(todo.iterrows(), 1):
        cid = cid_from_smiles(row["smiles"])
        time.sleep(0.25)
        cas = cas_from_cid(cid) if cid else None
        df.at[i, "pubchem_cid"] = cid
        df.at[i, "cas"] = cas
        time.sleep(0.25)
        if count % 25 == 0:
            df.to_csv(out_path, index=False)           # checkpoint
            got = df["cas"].notna().sum()
            print(f"  {count}/{len(todo)} processed | {got} CAS found so far")

    df.to_csv(out_path, index=False)
    got = df["cas"].notna().sum()
    print(f"Done. {got}/{len(df)} rows have a CAS. Written: {out_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python resolve_cas.py master_odor_map.csv")
        sys.exit(1)
    main(sys.argv[1])
