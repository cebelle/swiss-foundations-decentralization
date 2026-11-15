# Multi-entity networks: notes for the Tier 2 screen

**Label:** PUBLIC (approved by the author 2026-11-15) · **Date:** 2026-11-15 · **Ruling:** author, 2026-11-15 · **Screen:** `tier2-screen.md`

**Ruling.** In Cardano, TON and the ASI Alliance more than one entity could be the primary steward. The author ruled that the Swiss Stiftung is coded as the primary steward in each case. The other entities are recorded here and under codebook field F8 (related entities).

**Test applied (author's call, 2026-11-15).** Each ruling is checked against the rule's test: the entity that holds the treasury, the IP or the trademarks, or that funds core development, as the project's own documents state. Where the Swiss Stiftung fails the test, the ruling stands but goes in `DEVIATIONS.md`.

| Network | Result | Basis |
| --- | --- | --- |
| Cardano | **Pass** | The Cardano Foundation's own trademark policy names Cardano™ as its trademark and gives UID CHE-184.477.354. Per USPTO records, CARDANO (reg. 6549522) and ADA (reg. 6375037) are owned by the Cardano Foundation. |
| TON | **Fails since May 2026; kept by author ruling (deviation logged 2026-11-15)** | ADGM's announcement says the TON DLT Foundation *complements* the Swiss foundation (Swiss: Europe and the West; ADGM: MENA and APAC). In 2023 the Swiss foundation said it would oversee ecosystem development and publish reports on token distribution. Who holds the treasury today is not stated. [VERIFY] |
| ASI Alliance | **Fail → deviation** | The Alliance's own entity is Superintelligence Alliance Ltd (Singapore). The member foundations stay separate, and FET (Fetch.ai), not AGIX, became the ASI token. No source shows the SingularityNET Foundation holding the ASI treasury, IP or marks. |

**Splits (author decision, 2026-11-15).** The fact that a network is split across several entities is relevant and will be discussed in the paper: noted at minimum, possibly more. The rule already requires every entity to be recorded ("all of them are coded and the primary one is identified"), so recording splits needs no codebook change. Analysing them is Phase 4 work.

**Why it matters.** In each case the Swiss foundation was not the only legal home the project chose. Other entities were set up alongside it or after it, in other jurisdictions and for other jobs. That pattern may be a finding in its own right: a Swiss Stiftung's purpose is fixed and a supervisor sits over it, so projects build around it. [Author to decide whether this goes into the argument.]

Founding years come from secondary sources unless a register is cited. Every year is [VERIFY] until it is checked against a register or the entity's own documents.

## Cardano

| Entity | Role | Seat | Founded | Source |
| --- | --- | --- | --- | --- |
| Input Output (IOHK, now IOG) | Core research and engineering | Hong Kong at founding; now IOG | 2015 | cardanocube.com; ardana.substack.com |
| CARDANO Stiftung (Cardano Foundation) | Adoption and standards; **primary steward by ruling** | Zug | Deed 06.09.2016; SHAB 16.09.2016 | Zefix, CHE-184.477.354 |
| EMURGO | Commercial and venture arm | Tokyo | Registered June 2017 | ardana.substack.com |
| Intersect | Member-based governance body | [VERIFY] | June 2023 | forum.cardano.org |

- **Date conflict resolved:** Zefix shows a deed dated 06.09.2016, so the foundation dates from 2016, not 2017.
- **Sequence:** an engineering company came first (2015). The Swiss foundation followed within about a year. A commercial arm came next (2017), and a governance body arrived six years later (2023).

## TON (Gram, prev. Toncoin)

| Entity | Role | Seat | Founded | Source |
| --- | --- | --- | --- | --- |
| TON Foundation (before incorporation) | Described by a spokesperson as a community-led initiative | none | [VERIFY] | decrypt.co, 2023 |
| The Open Network Stiftung | **Primary steward by ruling** | Zug | Deed 11.04.2023; SHAB 08.05.2023; public launch 6 Sept 2023 | Zefix, CHE-418.000.792; eqs-news.com |
| TON DLT Foundation | ADGM DLT Foundation; says it advances core development and adoption | Abu Dhabi (ADGM) | Announced Dec 2024 | adgm.com; beincrypto.com |

- **Sequence:** an informal initiative, then the Swiss Stiftung (2023), then an ADGM foundation about fifteen months later (2024).
- **Open point:** ADGM's announcement says the TON DLT Foundation advances "core development." If the treasury or IP moved to Abu Dhabi, the rule's test would point there. Check before coding.
- **2026-11-15 residue pass: a third entity.** On 4 May 2026 Telegram replaced the TON Foundation as the network's driving force and largest validator (about 2.2M staked). That's step 3 of Durov's "Make TON Great Again" (MTONGA) roadmap. CoinShares names the operating entity as Telegram FZ-LLC (Dubai). ton.org no longer mentions the Foundation; its only governance link is "MTONGA," pointing to Durov's channel. The Foundation's own site (ton.foundation, accessed 2026-11-15) says it "empowers TON projects without controlling TON technology" and lists a two-person council (Steve Yun, Barbara Schüpbach), which matches the register. Zefix: CEO and council member Maximilian Crown left (SHAB 20.05.2026), and council president Manuel Stotz left earlier (SHAB 16.09.2025). The Foundation holds the TON logo mark: US application 79435217 (Madrid IR 1882072, IR date 22.05.2025) is in its name and pending, with no assignment of record (TSDR, checked 2026-11-15). The treasury holder is still undisclosed [VERIFY].
- **Effect on the test:** since May 2026, Telegram funds core development. On the rule's terms Telegram is now the stronger candidate, and the snapshot (2026-11-06) postdates the change. **Author ruling (2026-11-15):** keep TON in the coded Tier 2 sample and log a deviation (as with ASI). Code it as of the snapshot date, with Telegram and the ADGM TON DLT Foundation under F8. The 2026 shift of control is written up separately in `ton-case-study.md`.
- **Sequence (updated):** informal initiative → Swiss Stiftung (2023) → ADGM DLT Foundation (2024) → Telegram takes over operations (2026).

## ASI Alliance (FET)

| Entity | Role | Seat | Founded | Source |
| --- | --- | --- | --- | --- |
| Fetch.ai | Originator of FET; the token renamed ASI was FET | Cambridge (UK) for the company | [VERIFY] | businesswire.com; fetch.ai blog |
| Ocean Protocol Foundation | Alliance member | [VERIFY] | [VERIFY] | businesswire.com |
| SingularityNET Foundation | Alliance member; **primary steward by ruling** | Zug | Deed 11.07.2023; SHAB 25.07.2023 | Zefix, CHE-358.649.107 |
| Alliance foundation | The Alliance's own entity | Singapore | 2024 | mayerbrown.com |
| CUDOS | Joined as a member | [VERIFY] | Joined Sept 2024 | news.hodlfm.io |

- **Sequence:** separate projects for years. SingularityNET re-registered in Zug in 2023. The Alliance was announced 27 Mar 2024 and the merger completed 13 June 2024, with its own Singapore foundation. The member foundations remain separate legal entities.
- **The split has become a fracture.** On 9 Oct 2025, Ocean Protocol Foundation Ltd gave notice that it was resigning as a member of Superintelligence Alliance Ltd (statement on docs.superintelligence.io). Reports say the dispute concerns about 286M FET. [VERIFY]
- **Weakest of the three rulings.** The Alliance has its own Singapore foundation, and FET, not AGIX, became the ASI token. Under the rule's test (treasury, IP, trademarks, core funding), the Singapore foundation or Fetch.ai may have the stronger claim. See the note to the author in the session reply.
