# Sampling rule (pre-registered)

**Label:** PUBLIC · **Status:** v1, committed before the snapshot date · **Date:** 2026-10-30

Decided by the author on 2026-10-30. Definitions and method were drafted by Claude (disclosed AI tool); the author is to confirm them before the snapshot date. Any change after 2026-11-06 is logged in `DEVIATIONS.md`.

## Snapshot

- **Source:** CoinMarketCap historical snapshot for **2026-11-06**, at `https://coinmarketcap.com/historical/20261106/`. CoinMarketCap publishes dated snapshots at this URL pattern. [VERIFY the time of day the snapshot is taken.]
- **Preservation:** on or after 2026-11-06, save a copy of the snapshot (PDF or CSV export) to `02-research/data/` and submit the URL to the Internet Archive. Record the access date.

## Universe

**Network:** a protocol with its own native token. The following are excluded:

- stablecoins
- wrapped, bridged, and liquid-staking derivatives
- exchange and centralized-platform tokens
- tokens with no associated protocol

Every excluded asset is listed by name, with the reason for its exclusion.

## Tier 1: prevalence (top 25)

**Sample:** the first 25 networks in the snapshot, counted after exclusions.

**Coded for each network:**

1. Primary steward entity or entities, or "none"
2. Legal form
3. Jurisdiction
4. Source and access date

**Purpose:** to measure how often major networks use offshore stewards, and which structures they use. Non-Swiss stewards serve as comparators, for example US nonprofits and Cayman foundation companies.

## Tier 2: Swiss foundations (top 100)

**Sample:** every network ranked 1–100 in the snapshot, counted after exclusions, whose primary steward is a Swiss foundation.

**Swiss foundation:** a Stiftung under Art. 80 ff. ZGB, confirmed in the Swiss commercial register (Zefix). Associations (*Verein*) and companies (AG/GmbH) are recorded but not included in Tier 2.

**Method:**

1. **Identify the steward.** Use the project's own documents: the website's legal or imprint page, terms of use, the foundation website, and token documentation. Record each URL and its access date.
2. **Confirm in Zefix** (zefix.ch). Record the legal form, UID, seat, registration date, the registered purpose, and a link to the register extract.
3. **Identify the supervisory authority.** Determine whether it is federal (Eidgenössische Stiftungsaufsicht) or cantonal, and which canton. Use the register extract or the authority's own published information. [VERIFY that these sources are available.]
4. **Collect the governing documents:**
   - the deed (*Stiftungsurkunde*)
   - the regulations (*Reglement*)
   - annual reports
   - governance pages

   Deeds may have to be ordered from the cantonal commercial register. [VERIFY the procedure and fee.] When a document is not public, record that as a finding.
5. **Code each foundation** against a codebook, which will be pre-registered before coding begins.

## Primary steward

**Definition:** the entity that holds the treasury, the IP, or the trademarks, or that funds core development, as stated in the project's own documents. When a project has more than one entity, all of them are coded and the primary one is identified.

## Known limits

- Market capitalization measures size, not decentralization, and it changes daily. The fixed snapshot date controls for timing but not for volatility.
- Project documents may be out of date or may omit entities.
- Swiss governing documents may not be publicly available.
