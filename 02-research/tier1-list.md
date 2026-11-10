# Tier 1 list and Tier 2 pool

**Label:** PUBLIC · **Date:** 2026-11-10 · **Rule:** `02-research/sampling-rule.md` · **Snapshot:** `data/cmc-snapshot-2026-11-06.csv`

The exclusions are applied to all 200 rows in `data/universe-2026-11-06.csv`. That file lists every excluded asset by name, with its category and reason, as the sampling rule requires.

## Result

- **Networks.** After exclusions, 147 of the 200 snapshot rows are networks.
- **Tier 1 (prevalence).** The first 25 networks, running from snapshot rank 1 to rank 40.
- **Tier 2 pool.** The first 100 networks, running from snapshot rank 1 to rank 135. Tier 2 will take the networks in this pool whose primary steward is a Swiss foundation. Those are not yet identified.

## Tier 1

| # | Network | Snapshot rank |
| --- | --- | --- |
| 1 | Bitcoin | 1 |
| 2 | Ethereum | 2 |
| 3 | XRP | 5 |
| 4 | Solana | 7 |
| 5 | TRON | 8 |
| 6 | Zcash | 9 |
| 7 | Hyperliquid | 10 |
| 8 | Monero | 11 |
| 9 | Dogecoin | 12 |
| 10 | Chainlink | 14 |
| 11 | Cardano | 15 |
| 12 | Stellar | 16 |
| 13 | Bitcoin Cash | 17 |
| 14 | NEAR Protocol | 19 |
| 15 | Uniswap | 21 |
| 16 | Litecoin | 22 |
| 17 | Canton | 23 |
| 18 | Avalanche | 24 |
| 19 | Sui | 25 |
| 20 | Gram (prev. Toncoin) | 27 |
| 21 | Hedera | 29 |
| 22 | Bittensor | 34 |
| 23 | Quant | 36 |
| 24 | Ethena | 37 |
| 25 | Aave | 40 |

## Exclusions in the Tier 2 range (ranks 1–135)

| Category | Excluded |
| --- | --- |
| Stablecoins | Tether USDt, USDC, Ethena USDe, Dai, World Liberty Financial USD, PayPal USD, Global Dollar, Ripple USD, United Stables, USDD, TrueUSD, EURC, First Digital USD, Tether Gold, PAX Gold |
| Exchange and centralized-platform tokens | BNB, UNUS SED LEO, Cronos, OKB, Pump.fun, Bitget Token, Venice Token, GateToken, KuCoin Token, Nexo, AINFT, JasmyCoin |
| No associated protocol | Shiba Inu, Pepe, 币安人生, Pudgy Penguins, OFFICIAL TRUMP, SPX6900, Bonk, FLOKI |
| Wrapped, bridged and liquid-staking derivatives | None in the snapshot |

The exclusions for ranks 136–200 are listed in the CSV.

## Author's rulings on the definitions

These rulings apply the pre-registered definitions to cases the rule does not name. They do not change the rule. The author decided each one on 2026-11-10. Claude proposed them.

1. **Commodity-backed tokens are treated as stablecoins and excluded.** Affected: Tether Gold, PAX Gold.
2. **Exchange tokens are excluded even when the exchange also runs a chain that uses the token.** This follows the rule's text. Affected: BNB, Cronos, OKB, Bitget Token, GateToken, KuCoin Token.
   - Including them would have been an interpretation of the rule.
   - Had they been included, BNB and Cronos would have entered Tier 1, and Ethena and Aave would have dropped out.
3. **Shiba Inu is excluded as a memecoin.** Its L2, Shibarium, uses a different gas token. [VERIFY]
4. **Game tokens.**
   - Company-run games are excluded: Axie Infinity, The Sandbox, SuperVerse.
   - Game tokens with their own chain or DAO are included: Decentraland, ApeCoin, Gala.
   - All six are outside the Tier 2 range.
5. **Company-led projects are included when the token runs a protocol.** Included: Quant, World Liberty Financial, Pieverse, Basic Attention Token, Telcoin, Tagger. JasmyCoin is excluded as a token of a company product.
6. **"Network" covers application protocols as well as chains.** This reads "a protocol with its own native token" in the rule. So Uniswap, Ethena and Aave are networks.

## Sources

- **Well-known assets.** Claude classified these, and the author reviewed the classifications.
- **Thirty newer or less familiar assets.** These were identified from web pages a research agent opened on 2026-11-10: CoinMarketCap coin pages, Blockworks token-transparency filings, and other pages. Each row's URL is in the `source_url` column of the CSV.
- **Weaker sources.** For Lighter and Pons, the only source is CoinMarketCap's AI-generated "what is" page. [VERIFY before citing in the paper.]
