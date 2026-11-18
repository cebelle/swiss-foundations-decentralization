"""Tier 2 random check (codebook section 6.4, as applied by the author on 2026-11-17).

Every record carried at least one flag after the first pass, so the pool of
"records with no flags" was empty. The author ruled (logged in DEVIATIONS.md,
2026-11-17) to draw 20% of all ten records, rounded up (2), and to review every
unflagged value in the records drawn. Seed and sort order are as the codebook sets.
"""
import csv, math, random, sys

path = sys.argv[1] if len(sys.argv) > 1 else "02-research/data/tier2-coding.csv"
rows = list(csv.DictReader(open(path, newline="", encoding="utf-8")))
records = sorted({(int(r["snapshot_rank"]), r["foundation"]) for r in rows})
k = math.ceil(0.2 * len(records))
random.seed(20261106)
drawn = random.sample(records, k)
print(f"records: {len(records)}; drawn: {k}")
for rank, name in drawn:
    unflagged = [r for r in rows if r["foundation"] == name and not r["flag"]]
    print(f"- rank {rank}: {name} ({len(unflagged)} unflagged values)")
