# CoinMarketCap snapshot, 2026-11-06

**Label:** PUBLIC · **Captured:** 2026-11-10 · **Rule:** `02-research/sampling-rule.md`

## Source

- **Snapshot page:** https://coinmarketcap.com/historical/20261106/ ("Historical Snapshot - 06 November 2026")
- **Internet Archive copy:** https://web.archive.org/web/20261110052813/https://coinmarketcap.com/historical/20261106/ (saved by the author 2026-11-10 05:28:13 UTC; the Archive marked it "First Archive")
- **Snapshot time of day:** the page does not state one. [VERIFY with CMC methodology.]

## How it was retrieved

1. **Author's PDF.** The author printed the page to PDF in Chrome on 2026-11-10 05:22 UTC (9:22 PM Pacific, 2026-11-09). It is 13 pages, image-only, with no text layer. It is kept **PRIVATE** and not committed, following the copyrighted-PDF rule in `AI_USE.md`. Claude read it page by page.
2. **Direct fetch.** On 2026-11-10, Claude (Opus 5.5) fetched the live snapshot URL with its web-fetch tool. The tool returns the page through a summarizing model, not raw HTML.
3. **Failed attempts.** A scheduled run on 2026-11-07 could not reach the page (unapproved fetch, no search hit). A fetch of the Archive copy on 2026-11-10 was blocked by the tool.

## What the page provides

- The page loads 200 rows, followed by a "Load More" button.
- **Rows 1–20** show the printed rank, symbol, market cap and price. Every value in these rows matches between the PDF and the fetch.
- **Rows 21–200** show the name only. No rank, symbol, market cap or price is rendered for them, in either the PDF or the fetch. The page appears to load these figures lazily as the user scrolls.

## Columns

| Column | Meaning |
| --- | --- |
| `list_position` | Row order on the page (1–200). The page is ordered by market cap, but ranks are printed only for rows 1–20. |
| `rank_printed` | The rank as printed on the page. Blank where none is shown. |
| `market_cap_usd`, `price_usd` | Copied as printed, with `$` and commas removed. Nothing is rounded or estimated. |
| `source_check` | `pdf+fetch`: the row appears in both the author's PDF and the fetch. `fetch_only`: the row was hidden in the PDF behind the sticky header or cookie banner at a page break, so only the fetch supports it. |

## Unreadable or unverified rows

- **Blank data:** symbol, market cap and price are blank for list positions 21–200. The page does not render them.
- **Fetch-only rows (55 in total):** list positions 25–30, 45–50, 65–70, 84–90, 104–109, 124–129, 144–149, 163–168 and 183–188. These names rest on a single source, which passed through a summarizing model. [VERIFY these against a PDF printed with the cookie banner dismissed.]
- **Position 145:** the fetch returned "GoМining" with a Cyrillic М. It is recorded here as `GoMining` in Latin characters.

## Not done here

The exclusions and the Tier 1 and Tier 2 lists are not applied in this capture. That happens in a working session with the author.
