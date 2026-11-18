# Tier 2 coding: first pass and comparison with the Fable calls

**Label:** PUBLIC · **Date:** 2026-11-17 · **By:** Claude (Opus 5.5, medium effort, per the `AI_USE.md` row for Tier 2 coding), a disclosed AI tool · **Data:** `02-research/data/tier2-coding.csv` · **Codebook:** v1

Published under the author's rule of 2026-11-16 (`tier2-rulings.md`, ruling 6): coded values, article numbers and short legal terms only. No deed text beyond short terms, and no personal data.

## What was coded

- **Law layer, all ten records:** F1-F6, F7 (law), F8 (law), F9, from the deeds (OCR text of the ten files held privately) and the cantonal register extracts (read 2026-11-17).
  - **Ethereum** is coded from an excerpt only, so F2-F5 are `NOT_FOUND` until the full deed arrives (ruling T2-5).
- **Practice layer:** F1 and F2c come from the register extracts, F7 from public reports.
  - **Not coded yet (`PENDING`):** F2a and F2b practice (including how nominations are made, ruling T2-2), F4 practice, and F8 practice. These need a separate search pass.
- **Rows:** 210 in total, of which 170 are coded, 40 are `PENDING`, and 21 are flagged.
- **Order:** the first pass was coded before the Fable note (`claude/tier2-legal-calls.md`, private) was opened, and compared with it afterwards. The order of the passes is logged in `DEVIATIONS.md` (2026-11-16).

## Comparison with the Fable calls (law layer, F1-F6)

**Agreement.** The two passes give the same value for F1, F2a, F2b, F2c, F2d, F4 and F6 in every codeable record, once the author's rulings T2-1 to T2-5 are applied. F3 values also agree for all ten.

**Differences for the author:**

1. **F5, TON and ASI.** The Fable note describes one pattern across the nine deeds: remaining assets go to tax-exempt organisations with a similar purpose. Two deeds do not follow it.
   - TON lets the council decide how any surplus is used, with no purpose, tax-exemption or Swiss requirement (Art. 13). It bars any return to the founder, council members or affiliates.
   - ASI lets the council name a beneficiary with the same or a similar purpose, with no tax-exemption or Swiss requirement (Art. 20).
   - The first pass codes both deeds as written.
2. **F5, ASI, who dissolves.** The ASI deed lists dissolution among the council's own resolutions (Art. 8(3)(g)), with no reference to the authority. Under Art. 88 ZGB the authority decides. Flagged in the first pass, not in the Fable note.
3. **F5, ICP, the German and English texts differ.** The English text sends remaining assets to bodies "based in Switzerland". The German text, which controls, does not say this. Noted in the first pass, not in the Fable note.
4. **F3, the date the ten years run from.** The Fable note counts from the first SHAB publication. The first pass counts from the register entry date shown on the cantonal extract, which is a few days earlier:
   - ICP: 09.11.2016, against 14.11.2016
   - Tezos: 26.04.2017, against 01.05.2017
   - Polkadot (Web 3.0 Technologies): 20.06.2017, against 23.06.2017
   - TON: 03.05.2023, against 08.05.2023

   Which date the period runs from is a legal point. [VERIFY]
5. **F3, Cardano's history.** The Fable note records that a purpose reservation was registered in 2016 and struck in 2020. The first pass coded only the current text (`NONE`) and did not check the register history. The two do not conflict. The history belongs in the source note.
6. **Regulations, ICP.** The Fable note codes regulations as `NOT_PUBLIC` for all ten. The ICP deed requires its regulations to be approved by the supervisor and filed with the commercial register (Art. 8). If they were filed, they may be obtainable from the Zürich register. [VERIFY]

## New register facts from the first pass (practice layer, read 2026-11-17)

- **Council size today:**

  | Foundation | Members |
  | --- | --- |
  | Ethereum | 4 |
  | Solana | 5 |
  | Cardano | 4 |
  | NEAR | 4 |
  | TON | 2 |
  | Web 3.0 Technologies | 3 |
  | DFINITY | 1 |
  | Interchain | 4 |
  | SingularityNET | 3 |
  | Tezos | 6 |

- **TON** is below its deed minimum of three.
- **DFINITY's** single council member has individual signing authority. Its deed allows a council of one.
- All ten list the federal supervisor (Eidg. Departement des Innern, Bern).
- **SingularityNET's** auditor (blueAUDIT GmbH) appears on the cantonal extract but not in the Zefix API record.
- **Treasury disclosure (F7 practice):**

  | Value | Foundations |
  | --- | --- |
  | `AUDITED_PUBLISHED` | Cardano (2025 statements attested by its auditor) |
  | `PERIODIC_REPORTS` | Ethereum, NEAR, Interchain, Tezos |
  | `NOT_FOUND` | Solana, TON, Web 3.0 Technologies, DFINITY, SingularityNET |

## Flags awaiting a Fable recode or an author ruling

The codebook routes flagged values to a Fable recode, then the author. Fable access under the current plan ended on 2026-11-17. Of the 21 flags:

- **16 already have rulings.**
  - Solana F2a, F2b, F2d (T2-1)
  - ICP F2a (T2-2)
  - TON F3 (T2-3)
  - ICP and Tezos F3 (T2-4)
  - Ethereum's nine law-layer gaps (T2-5): ruled, but waiting on the full deed
- **5 are open:**
  - Polkadot F2a `MIXED` and its knock-on F2d `NO`
  - Polkadot F3 (a pre-2024 reservation that refers to Art. 86a in general terms)
  - ASI F5 (who dissolves)
  - TON F1 practice (council below the deed minimum)

## Not yet done

- The practice-layer search pass (F2a/F2b nomination and removal practice, F4, F8).
- Source notes per foundation (`02-research/source-notes/`).
- The random 20% check. The codebook draws it after the first pass is complete, so it waits for the practice pass.
