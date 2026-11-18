"""Build one source note per Tier 2 foundation from tier2-coding.csv (codebook section 8).

Each note lists every source cited in the CSV for that foundation, the fields it
supports, and how it was checked. Re-run after any change to the CSV.
"""
import csv, collections, re, sys, pathlib

csv_path = sys.argv[1] if len(sys.argv) > 1 else "02-research/data/tier2-coding.csv"
out_dir = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "02-research/source-notes")
rows = list(csv.DictReader(open(csv_path, newline="", encoding="utf-8")))

PRIMARY = re.compile(r"(deed|Stiftungsurkunde|register|zefix|chregister|SHAB|Art\.)", re.I)
SECONDARY = re.compile(r"(theblock|cointelegraph|beincrypto|bitcoinist|finews|forklog|livebitcoinnews|dock\.io)", re.I)

def kind(src):
    if not src or src.startswith("02-research/"):
        return "internal research file"
    if SECONDARY.search(src):
        return "secondary (press)"
    if PRIMARY.search(src) or not src.startswith("http"):
        return "primary (deed or register)"
    return "foundation source (codebook sources 4-6)"

def checked(k):
    if k == "primary (deed or register)":
        return "Y (deed OCR or register read)"
    if k == "internal research file":
        return "see the cited file"
    return "N (search excerpt or page text read; not archived)"

by_f = collections.defaultdict(list)
for r in rows:
    by_f[(int(r["snapshot_rank"]), r["foundation"], r["uid"])].append(r)

for (rank, name, uid), rs in sorted(by_f.items()):
    srcs = collections.OrderedDict()
    for r in rs:
        if r["layer"] == "none":
            continue
        key = r["source"] or "(no source recorded)"
        srcs.setdefault(key, []).append(r)
    lines = [f"# Source note: {name}", "",
             f"- **UID:** {uid}  ",
             f"- **Snapshot rank:** {rank}  ",
             "- **Generated from:** `02-research/data/tier2-coding.csv` by `02-research/scripts/build_source_notes.py`  ",
             "- **Deed files are private** (tier2-rulings.md, rulings 6 and 7); deed sources are cited by article only.", ""]
    for i, (src, items) in enumerate(srcs.items(), 1):
        k = kind(src)
        dates = sorted({x["access_date"] for x in items if x["access_date"]})
        claims = "; ".join(f'{x["field"]} ({x["layer"]}): {x["value"][:120]}' for x in items)
        pins = "; ".join(sorted({x["pinpoint"][:160] for x in items if x["pinpoint"]}))
        lines += [f"## {i}. {src}", "",
                  f"- **Source:** {src} ({k})",
                  f"- **Pinpoint cite:** {pins or 'n/a'}",
                  f"- **Claim it supports:** {claims}",
                  "- **Summarized by:** AI (Claude Opus 5.5); values reviewed by the author where `author_reviewed` = yes or a ruling applies",
                  f"- **Verified against original:** {checked(k)}, {', '.join(dates) or 'date not recorded'}", ""]
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    (out_dir / f"{rank:03d}-{slug}.md").write_text("\n".join(lines), encoding="utf-8")
    print(out_dir / f"{rank:03d}-{slug}.md", len(srcs), "sources")
