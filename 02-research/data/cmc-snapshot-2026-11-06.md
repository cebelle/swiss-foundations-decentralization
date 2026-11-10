# CoinMarketCap snapshot, 2026-11-06

**Label:** PUBLIC · **Captured:** 2026-11-10 · **Rule:** `02-research/sampling-rule.md`

## Source

- **Snapshot page:** https://coinmarketcap.com/historical/20261106/ ("Historical Snapshot - 06 November 2026")
- **Internet Archive copy:** https://web.archive.org/web/20261110052813/https://coinmarketcap.com/historical/20261106/ (saved by the author 2026-11-10 05:28:13 UTC; the Archive marked it "First Archive")
- **Snapshot time of day:** the page does not state one. [VERIFY with CMC methodology.]

## How it was retrieved

1. **Source of record: the author's PDF.** The author printed the page from Chrome on 2026-11-10 at 05:35 UTC (9:35 PM Pacific, 2026-11-09), after scrolling so all 200 rows loaded. It is 12 pages, image-only. It is kept **PRIVATE** and not committed, following the copyrighted-PDF rule in `AI_USE.md`.
2. **First extraction pass.** Claude (Opus 5.5) rendered the PDF at 300 dpi and ran OCR (tesseract) over each full page.
3. **Visual check.** Claude read every page image against the OCR output. Seven OCR errors were corrected from the image:
   - ranks 84, 111, 112 and 171 were misread or dropped;
   - the market caps for ranks 49 and 62 had punctuation errors;
   - the price for rank 138 was misread.
4. **Independent second pass.** Claude rendered the PDF again at 450 dpi and ran OCR on the rank, market-cap and price columns only, restricted to digits. All 200 rows matched the corrected first pass exactly.
5. **Validation.** Every market cap is well-formed, and market cap strictly decreases with rank. Ranks 1–200 are each present exactly once.
6. **Superseded first capture.** An earlier PDF (05:22 UTC) and a web fetch had figures for rows 1–20 only. Those 20 rows match this capture exactly. That capture was committed in `48db766` and is replaced by this file.

## Columns

| Column | Meaning |
| --- | --- |
| `rank` | As printed on the page. |
| `name` | As printed. Where the page truncates a name with "…", the full name is taken from the 2026-11-10 web fetch of the same page. The fetch returned "GoМining" (rank 145) with a Cyrillic М; it is recorded here in Latin characters. |
| `symbol` | Given for ranks 1–20 only. |
| `market_cap_usd`, `price_usd` | As printed, with `$` and commas removed. Nothing is rounded or estimated. |

## Unreadable values

- **Symbols for ranks 21–200 are blank.** The PDF clips the left edge of the symbol column (for example, "ISDT" for USDT), so the symbol cannot be read in full. Symbols for ranks 1–20 come from the web fetch.
- No market cap or price value is blank.

## Not done here

The exclusions and the Tier 1 and Tier 2 lists are not applied in this capture. That happens in a working session with the author.
