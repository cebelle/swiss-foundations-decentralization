# Tier 2 screen — pass 1

**Label:** PUBLIC (pass 1 approved by the author 2026-11-15; residue update pending approval) · **Date:** 2026-11-15 · **Rule:** `sampling-rule.md` (Tier 2 and "Primary steward") · **Pool:** the 100 networks in `tier1-list.md` · **Data:** `data/tier2-screen.csv`

Claude (Opus 5.5, high effort), a disclosed AI tool, ran this pass. The author approved it for commit on 2026-11-15. All Swiss hits are confirmed in Zefix, and the author has ruled on the flagged rows.

## Status

**The inclusion question is answered for all 100 networks.** Ten have a Swiss Stiftung as primary steward. No other network turned up a Swiss Stiftung, either in project or secondary sources or in a Zefix name search of every network name (2026-11-15).

| Screen status | Count |
| --- | --- |
| Swiss Stiftung, primary steward (Tier 2) | 10 |
| Swiss entity of another form (recorded, not Tier 2) | 4 |
| Non-Swiss steward identified | 72 |
| No steward entity | 7 |
| Steward not named in any source found | 7 |

**Residue pass (2026-11-15).** The 27 rows that were "not Swiss by register check; steward still to name" now each have a named steward (or "none" / "not found") and a source. One of them, LayerZero, turned out to have a Swiss Verein (see below), so the Swiss-other-form count rises to 4. Tier 2 is unchanged at 10. TON is kept by author ruling, with a deviation logged.

## Swiss Stiftung candidates

All ten are confirmed in Zefix (2026-11-15). Candidates were first found in register mirrors (moneyhouse.ch, fundraiso.com, onlineinfo.ch) or GLEIF. *(Corrected 2026-11-15 residue pass: the earlier text said none was confirmed yet, which pass 1 had already overtaken.)*

| Network | Foundation as registered | Seat | UID | Flag |
| --- | --- | --- | --- | --- |
| Ethereum | Stiftung Ethereum | Zug | CHE-292.124.800 | |
| Solana | Solana Stiftung | Zug | CHE-436.843.713 | |
| Cardano | CARDANO Stiftung | Zug | CHE-184.477.354 | Primary steward |
| NEAR Protocol | NEAR Stiftung | Zug | CHE-312.859.108 | |
| Gram (prev. Toncoin) | The Open Network Stiftung | Zug | CHE-418.000.792 | Primary steward |
| Polkadot | Web 3.0 Technologies Stiftung | Zug | CHE-322.596.347 | |
| Internet Computer | DFINITY Stiftung | Zürich | CHE-189.770.146 | |
| Cosmos | Interchain Stiftung | Zug | CHE-199.569.367 | |
| Artificial Superintelligence Alliance | SingularityNET Foundation | Zug | CHE-358.649.107 | Primary steward |
| Tezos | Tezos Stiftung | Zug | CHE-290.597.458 | |

## Swiss entities of another form

The rule records these but keeps them out of Tier 2.

- **Pyth Network:** Pyth Data Verein (Pyth Data Association), a Verein in Baar (CHE-325.103.020).
- **Bitcoin SV:** BSV Association, a Verein in Zug (CHE-427.008.338).
- **Curve:** Swiss Stake AG in Zug (CHE-482.934.709). It owns and controls all Curve IP, and Curve has no foundation, so it is the steward. It is a company, so it is not in Tier 2.
- **LayerZero:** ZRO Verein (ZRO Association, dba "ZRO Foundation", publicly the LayerZero Foundation), a Verein in Baar (CHE-212.005.749; articles 28.04.2022; entered SHAB 29.12.2022). Its registered purpose names the LayerZero network, and it holds the Foundation's 383M ZRO allocation. Found 2026-11-15 in the residue pass. The network-name search missed it because "ZRO" shares no word with "LayerZero".

## Author's rulings (2026-11-15)

1. **Cardano, TON, ASI Alliance:** the Swiss Stiftung is coded as the primary steward. The other entities and their founding years are in `multi-entity-notes.md` and go under codebook field F8. Checked against the rule's test: Cardano passes, TON passes provisionally, and ASI fails, so the ASI ruling is logged as a deviation (draft row in `DEVIATIONS.md`).
2. **Splits:** a network split across several entities is a finding to discuss in the paper. The screen records every entity, as the rule requires.

## Method

- **Steward.** Taken from the project's own documents (terms, imprint, legal notice, foundation site) where found. Where only a secondary source was found (Blockworks Token Transparency filings, DeFiLlama, register mirrors), the CSV says so in `source_kind`.
- **Swiss check.** Every Swiss hit was searched in register mirrors by name. Then all 100 network names (plus key entity names such as DFINITY, Interchain, SingularityNET and Hashgraph) were searched in Zefix itself, keeping active Stiftungen and Vereine whose names contain the term. The only relevant hits were the 13 entities listed here, plus The Hashgraph Association (a Verein in Freienbach related to Hedera, not its steward). Limit: a foundation whose registered name shares no word with its network would not appear. **Residue pass (2026-11-15):** every steward entity named in the residue (and the named entities of the earlier non-Swiss rows) was also searched in Zefix by entity name. That found ZRO Verein (LayerZero). The only other hits were companies that are not stewards (Chainlink Labs Swiss GmbH, Luzern; VeChain Switzerland SA, Lugano) and an unrelated Verein (Shielded Labs, Zug, which belongs to Zcash, not Midnight).
- **Zefix.** Mirrors were used to find candidates. Confirmation was done in Zefix itself (built-in browser, 2026-11-15). No deviation.

## TON: author ruling (2026-11-15)

On 4 May 2026, six months before the snapshot, Telegram replaced the TON Foundation as the network's driving force and largest validator. Since then ton.org has stopped naming the Foundation. The Foundation's own site says it does not control TON technology, and its council is down to two. Its CEO left the register on 20.05.2026. The Foundation may still hold the TON mark (a US application in its name is pending [VERIFY]). The treasury holder is undisclosed [VERIFY]. On the rule's test, Telegram (which funds core development) now looks like the stronger candidate. **Ruling:** TON stays in the coded Tier 2 sample, logged as a deviation as with ASI, and gets a case-study write-up (`ton-case-study.md`). The network held itself out as decentralized throughout, which makes the shift of control evidence for the research question. The sample stays at 10.

## Still to do

- Resolve the [VERIFY] rows in the CSV (40 rows carry at least one). Most are seats of non-Swiss foundations. None of them can add a Tier 2 Stiftung: every steward name was run through Zefix.
- The name-search limit noted under Method has now bitten once (LayerZero). The 2026-11-15 sweep also searched each named steward entity, not just network names. A steward whose name is still unknown (Mantle, SUN, MemeCore and the other NOT_FOUND rows) could still be Swiss under an unrelated name.

## Observations from the register (for the author)

- **Federal supervision.** All 10 are under EDI (federal), not cantonal supervision. That matters for the thesis's "Swiss government supervisor" claim: the supervisor is the federal one.
- **Template purposes.** Ethereum, Cardano, DFINITY, NEAR, Interchain and Tezos all open their registered purpose with nearly the same words (*"Förderung von neuen Technologieentwicklungen und Applikationen, insbesondere … neuen offenen dezentralisierten Softwarearchitekturen"*). Several were first registered c/o the same Zug service provider. These look like a common drafting template. [Author to decide whether this matters.]
- **Seat moves.** Solana started in Geneva and DFINITY in Zug. Both later moved.
