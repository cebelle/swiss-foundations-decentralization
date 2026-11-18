# Tier 2 coding: author's rulings

**Label:** PUBLIC · **Codebook:** `02-research/codebook.md`, v1 (section 6) · **Date opened:** 2026-11-16

These rulings apply the pre-registered codebook to cases it does not settle. They do not change a field, a value or a flag rule. The author decided each one on the date shown. Claude (Fable 5.2, high effort) proposed the values and set out the options.

Deeds are cited by article number and short legal terms only. The deed files are public register documents but are not reproduced here: several contain personal data.

## Rulings of 2026-11-16

1. **T2-1. Solana, F2a, F2b and F2d.** The deed lets the council elect only candidates put forward by an "Independent Committee" of members who are neither owners nor employees of Solana Labs, Inc. (Art. 6), and remove members on that committee's recommendation (Art. 7). The deed does not say what the committee is, and it is not among the bodies the deed lists (Art. 4).
   - Ruling: read the committee, for now, as made up of council members. Code F2a `CO-OPTATION`, F2b `COUNCIL`, F2d `YES`. Keep the flag open until evidence shows what the committee is. The regulations would show it and are not public.
   - The other reading (a body outside the council) would give F2a `OUTSIDE_BODY` and F2d `NO`.
2. **T2-2. Nomination rights, F2a, all records.** Where no one else can nominate, or it is very hard for anyone else to nominate, a right to nominate is in effect a power to appoint.
   - On the law layer this is applied by the deed's wording. The deeds of the DFINITY Stiftung and the Web 3.0 Technologies Stiftung give the founder a right to propose (*Vorschlagsrecht*, Art. 6 in both). Nothing in either text makes it exclusive.
   - The author also wants the practice recorded for every foundation under F2a (practice): how nominations are made, and whether the process is public or closed. Until that is known, the law-layer values stand as proposed and unruled: DFINITY `CO-OPTATION` with the proposal right noted; Web 3.0 Technologies `MIXED`, because its deed also gives the founder a seat through a representative (Art. 5).
3. **T2-3. The Open Network Stiftung, F3.** Code `BOTH`. The deed reserves a change of purpose with a reference to Art. 86a ZGB (Art. 2) and a change of organisation without one (Art. 4). The commercial register records the purpose reservation only. The flag stays: the validity of the organisation reservation is open, because the deed predates 1 January 2024 and does not cite the revised article.
4. **T2-4. DFINITY Stiftung and Tezos Stiftung, F3.** Code the reservation as present (`PURPOSE`) and the founder as `NOT_FOUND` until the original deeds are obtained. The current restated deeds do not name the founders. The right under Art. 86a is personal, and several founders can use it only together, so the founders' identities decide whether it can still be used.
5. **T2-5. Stiftung Ethereum.** The file available from the Zug register's portal is an excerpt of the current deed (Arts. 1, 5 and 14). F2 to F5 (law layer) are not coded until the full deed is obtained. The author asked the register for it on 2026-11-16.

## Rulings on publication (2026-11-16)

6. **What is published from the deeds.** Coded values, article numbers and short legal terms are public. Deed files, long quotations and all personal data stay private.
7. **Personal data.** No personally identifiable information goes into any public file. This includes, and is not limited to, passport numbers, home addresses and dates of birth.

## Rulings of 2026-11-17

The codebook (section 6) sends a flagged value to a Fable recode before the author rules. Fable access ended on 2026-11-17, so the author ruled on these five without the recode. Claude (Opus 5.5, medium effort) proposed the values and set out the options. The departure is logged in `DEVIATIONS.md` (2026-11-17).

8. **T2-6. Web 3.0 Technologies Stiftung, F2a.** Code `MIXED`. The council elects itself, the founder may propose members and the president (*Vorschlagsrecht*), and the founder is represented on the council by at least one member (Arts. 5(1), 6, 7(2)). The guaranteed seat gives the founder a hand in appointments. Flag closed.
   - The other reading (`CO-OPTATION`, applying T2-2 strictly because the proposal right is not exclusive) was considered and not taken.
9. **T2-7. Web 3.0 Technologies Stiftung, F2d.** Keep `NO`, as the codebook's derivation rule gives once F2a is `MIXED`, with a note: the council and the founder control appointments between them, and participants have no say. The rule is not changed. Flag closed.
10. **T2-8. Web 3.0 Technologies Stiftung, F3.** Code `PURPOSE`. The deed reserves a change of purpose with a general reference to Art. 86a ZGB (Art. 2) and predates 1 January 2024. Earliest use about June 2027. Treated like T2-4, except that here the founder is named in the deed. Flag closed. Whether the ten years run from the register entry or the SHAB publication date is a legal question still marked [VERIFY]; it can move the date but not the value.
11. **T2-9. SingularityNET Foundation, F5.** Code the deed as written: dissolution is a council decision (Arts. 8(3)(g), 20(3)). Note that under Art. 88 ZGB the supervisory authority decides on dissolution. This follows the approach of T2-3: code the deed's words and record the statute beside them. Flag closed.
12. **T2-10. The Open Network Stiftung, F1 (practice).** Code `2`, the number of council members in the commercial register, and note that it is below the deed's minimum of three (Art. 5(1)). Flag closed. Whether this is a case for the authority under Art. 83d ZGB is left to the TON legal note.

## Rulings of 2026-11-17 (evening)

Made without a Fable recode, under the 2026-11-17 deviation. Claude (Opus 5.5, medium effort) proposed the values and set out the options.

**On the differences between the first pass and the Fable calls (`tier2-first-pass.md`)**

13. **T2-11. The Open Network Stiftung and SingularityNET Foundation, F5.** Code both deeds as written. Note that they depart from the common pattern, in which remaining assets go to tax-exempt bodies with a similar purpose. TON lets the council decide how any surplus is used (Art. 13). SingularityNET lets the council name a beneficiary with the same or a similar purpose, with no tax-exemption or Swiss requirement (Art. 20).
14. **T2-12. SingularityNET Foundation, F5, who dissolves.** Closed by T2-9.
15. **T2-13. DFINITY Stiftung, F5.** Code from the German text, which controls. Note that the English version adds that recipients must be "based in Switzerland". The divergence between the two language versions is recorded as a finding: readers of the English text could be misled about where the assets go.
16. **T2-14. CARDANO Stiftung, F3.** Code `NONE`, from the current deed. Note the history: the register recorded an Art. 86a purpose reservation in 2016 and struck it in 2020, after the deed amendment of 25.03.2020.

**On the practice-layer flags**

17. **T2-15. F4 (practice): protocol voting that does not reach the foundation.** Code `NOT_FOUND`, with a note on the protocol voting. This applies to Solana, NEAR, TON, Web 3.0 Technologies, Interchain and Tezos. The codebook uses `NONE` only where a source says there is no role, and these sources say nothing about the foundation.
18. **T2-16. CARDANO Stiftung, F2a (practice).** Code `CO-OPTATION`, with a note. The board made the formal appointments in 2021; the selection process was run by a law firm the supervisor had engaged.
19. **T2-17. CARDANO Stiftung, F2b (practice).** Code `MIXED`, with a note that records the supervisor's part: its 2021 intervention led to the replacement of the whole board. The supervisor has stepped in before.
20. **T2-18. CARDANO Stiftung, F4 (practice).** Code `NONE`, with a note on the Foundation's 2025 statement that it intends to involve the community in electing future board members. No mechanism exists yet.
21. **T2-19. DFINITY Stiftung, F4 (practice).** Code `NONE`. The Foundation states that governance of the network is not governance of the Foundation. Who wrote the forum post is still to be confirmed [VERIFY].
22. **T2-20. SingularityNET Foundation, F4 (practice).** Code `SELF_COMMITMENT`, with a note that the elected Supervisory Council is advisory.
23. **T2-21. NEAR Stiftung, F1 (practice).** Recording both counts is enough: four in the register on 17.11.2026, and five in the Foundation's announcement of 15.10.2026.
24. **T2-22. Stiftung Ethereum, F8 (practice).** Code `NOT_FOUND`. The 2026 spin-out of a for-profit entity is recorded in a note; it is reported only in the press, which is not a codebook practice source.

**On the random check (codebook section 6.4)**

25. **Random check.** Every record carried at least one flag, so the pool of "records with no flags" was empty. Draw 20% of all ten records, rounded up (two), with the codebook's seed and sort order, and review every unflagged value in the records drawn. Logged in `DEVIATIONS.md` (2026-11-17). The draw (`02-research/scripts/tier2_random_check.py`; output in `02-research/data/tier2-random-check-output.txt`) gave Stiftung Ethereum and Solana Stiftung.

## Random check result (2026-11-17)

26. **Review of the two records drawn.** The author reviewed all 28 unflagged values (Stiftung Ethereum 11, Solana Stiftung 17). All were confirmed except one:
    - **Solana Stiftung, F7 (practice)** changed from `NOT_FOUND` to `HOLDINGS_ONLY`. The first pass rested on one search. A fuller search found the Foundation's delegation-program dashboard, which publishes stake accounts and the total delegated, and monthly token reports for June to August 2020, with none found since. There are no full treasury figures or financial statements. Reason for the change: the first-pass search was too thin.
    - One of the two sampled records was changed, which is not more than one in five, so the review does not widen to all records (codebook section 6.4).

27. **T2-23. DFINITY Stiftung, F8 (practice).** Code the Internet Computer Association as `OTHER` (an ecosystem association), with no shared personnel on the access date. The Geneva register shows the Association was dissolved on 12.02.2025 and has been in liquidation since SHAB 19.05.2025; the DFINITY founder left its committee in that entry. Author decision 2026-11-17.
28. **Names in citation links (2026-11-17).** Source links that contain the names of public officeholders, such as press articles on leadership changes, may stay in public files. Such names are already in the public domain, and the citations must remain checkable. Ruling 7 continues to bar passport numbers, birth dates, home addresses and other private personal data.
