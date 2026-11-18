# US-law source map

PUBLIC. Built 2026-11-18 by Claude (Opus 5.5, High), per `AI_USE.md` ("US-law source map"). Research only: what the law says and what has happened, with no argument. Every entry still has to be read in the original before it is cited in the paper (`PROCESS.md`, Phase 3).

**Status codes.**
- **P**: the primary text was seen (statute, bill, court docket or official page), at least in part.
- **S**: known from secondary sources only.
- **V**: a gap or conflict to check before citing; also marked [VERIFY] in the text.

It maps sources to the claims in `01-problem/problem-statement.md`.

## 1. "A few states have enacted statutes for decentralized entities ... most states have none" [VERIFY count]

| Statute | Citation | Date | What it does | Status |
| --- | --- | --- | --- | --- |
| Vermont blockchain-based LLC (BBLLC) | 11 V.S.A. § 4171 et seq. | 2018 | Lets an LLC use blockchain for governance. Not DAO-specific. | S; V (section range) |
| Wyoming DAO Supplement (DAO LLC) | Wyo. Stat. §§ 17-31-101 to -116 (SF0038, 2021; amended SF0068, 2022; SF0075, 2023) | eff. 1.7.2021 | DAO as an LLC, member- or algorithmically managed; dissolves if it takes no action for a year. | S (Proskauer, Stinson); V (read the text) |
| Tennessee decentralized organization (DO LLC) | Tenn. Code Ann. §§ 48-250-101 to -115 (HB2645/SB2854) | 2022 | DAO as an LLC, closely modelled on Wyoming. | S; V |
| Utah DAO Act (LLD) | Utah Code Title 48, ch. 5 (HB 357, 2023) | in force 2024 [VERIFY] | DAO as a limited liability decentralized organization; no imputed fiduciary duties; a legal representative is required. | S; V (section range, effective date) |
| Wyoming DUNA Act | Wyo. Stat. §§ 17-32-101 to -129 (SF0050, signed 7.3.2024) | eff. 1.7.2024 | Decentralized unincorporated nonprofit association with at least 100 members; governance may run through smart contracts. | P (enrolled bill, wyoleg.gov) |
| Wyoming DUNA amendments | SF0022, Enrolled Act 21, 2026 Wyo. Sess. Laws ch. 25 | eff. 1.7.2026 | Aligns the DUNA Act with the UNA Act; automatic conversion to a UNA in specified cases; assets distributed as federal law requires on winding up. | P (bill summary and digest, wyoleg.gov) |
| Alabama DUNA Act | SB 277 (2026) | signed 1.4.2026 | Adopts the DUNA model. | S; V (act number, text) |
| West Virginia DUNA Act | HB 5060 (2026) | signed 2.4.2026 | Adopts the DUNA model. | S; V (text) |

- **Count on current sources:** five states have DAO-specific entity statutes: Wyoming (two forms), Tennessee, Utah, Alabama and West Virginia. Vermont's BBLLC makes six if counted. Reports say New Hampshire and Tennessee are considering DUNA bills (S). The forms differ: three LLC variants (WY, TN, UT) and a nonprofit association model (WY, AL, WV).
- **Supports:** "a few states ... the statutes differ". With 5 or 6 of 50 states, "most states have none" holds.

## 2. "Courts ... do not consistently honor the forms that exist"

What we found:

| Case | Citation | Holding (stage) | Status |
| --- | --- | --- | --- |
| *Sarcuni v. bZx DAO* | 664 F. Supp. 3d 1100 (S.D. Cal. 2023) | Complaint plausibly alleged that the DAO was a general partnership of token holders (motion to dismiss). | S; V (pinpoint) |
| *CFTC v. Ooki DAO* | No. 3:22-cv-05416-WHO (N.D. Cal.), default judgment 8.6.2023 | The DAO is an unincorporated association, so a "person" that can be sued under the CEA. Default; the members of the association were not identified. | S; V (docket) |
| *Samuels v. Lido DAO* | 757 F. Supp. 3d 951 (N.D. Cal. 2024) (Chhabria, J.), No. 23-cv-06492-VC | Complaint plausibly alleged a general partnership; three of four investor defendants plausibly partners; Robot Ventures dismissed (motion to dismiss, 18.11.2024). | S; V (reporter cite) |
| *Samuels*, appeal | 9th Cir. No. 25-5701, filed 9.9.2025 | Pending; appellee moved for summary disposition 24.2.2026. The issue on appeal is not yet confirmed. | P (docket listing); V (issue, outcome, district-court status) |
| *Houghton v. Leshner* (Compound DAO) | N.D. Cal. (Orrick, J.); 9th Cir. No. 24-7243, opinion 21.10.2025 | The DAO-partnership theory survived dismissal (2023). The 9th Cir. held the defendants had waited too long to compel arbitration (reported). Summary judgment set for argument in Feb. 2026 (reported). | S; V |

- **What the cases show so far:** every case above concerns a DAO with no legal wrapper, and the courts fell back on default law (general partnership or unincorporated association). No case was found in which a DAO LLC, LLD or DUNA was contested, whether recognized or not (searched 2026-11-18).
- **Next search (author, 2026-11-18):** cases in which a wrapped DAO's form was contested and a court ruled on it. Recognition would show a pathway; refusal would show a limit. Either result is useful.

## 3. "... the IRS ... do[es] not consistently honor the forms"

| Source | Citation | Point | Status |
| --- | --- | --- | --- |
| Entity classification ("check-the-box") | Treas. Reg. §§ 301.7701-2, -3 | A business entity that is not a corporation is a partnership by default if it has two or more members, and may elect otherwise on Form 8832. | S; V (read the regulation) |
| Brunson | Samuel D. Brunson, *Standing on the Shoulders of LLCs: Tax Entity Status and Decentralized Autonomous Organizations*, 57 Ga. L. Rev. 603 (2023) | DAOs default to partnership under check-the-box; argues entity status is settled while other tax obstacles remain. | P (catalogue entry); V (pinpoints) |
| DUNA tax design | Wyo. Stat. § 17-32-101 et seq.; practitioner commentary | DUNAs are designed to be taxed as corporations. | S; V |
| IRS guidance specific to DAOs | none found (searched 2026-11-18) | Practitioners report no DAO-specific IRS guidance as of 2026. | S |

- **What the sources show:** a partnership default and no DAO-specific guidance or case law. A state-law LLC or DUNA is classified under the general rules. The tax pathway exists but is uncertain.

## 4. "... and insurers" (the problem statement says: source or cut)

| Source | Point | Status |
| --- | --- | --- |
| Reuters via Insurance Journal (19.12.2022) | Insurers were reluctant to write D&O cover for crypto companies and added FTX exclusions. | S |
| Canadian Underwriter (undated) | Limited underwriting appetite for D&O cover where clients use blockchain or digital assets. | S; V (date) |
| Aon, "Decentralized Autonomous Organizations: New Technology Meets Traditional Risk Management" | D&O cover is a significant risk tool for DAOs (an availability claim is not made). | S |

- **What the sources show:** D&O cover for crypto- and DAO-related risk is hard to obtain. Nothing was found on insurers declining a *state DAO form* as such.
- **Author's handling (2026-11-18):** insurers are raised as a potential issue the paper is aware of. They are not regulators, but they have great practical power over whether people will serve on a council or board.

## 5. Federal legislation touching decentralized governance

| Bill | Status (as of 2026-11-18) | Relevance | Status code |
| --- | --- | --- | --- |
| Digital Asset Market Clarity Act (CLARITY), H.R. 3633, 119th Cong. | Passed House 17.7.2025 (294–134). Senate Banking reported 14.5.2026 (15–9). Cloture on the motion to proceed failed 15.9.2026 (49–50). A motion to reconsider was entered, and a lame-duck session is the reported window. | The Senate text reportedly treats decentralized governance systems as distinct from coordinated entities, and says participation in decentralized governance alone does not imply control. | S (multiple outlets agree on dates and votes); V (Senate text and current status on congress.gov) |
| Promoting Innovation in Blockchain Development Act | Introduced 26.2.2026 (reported) | Developer liability; context only. | S; V |

- No federal entity-recognition statute for DAOs was found. That is the gap the paper's remedy addresses.

## 6. The remedy's model: state formation plus federal recognition (the nonprofit pattern)

| Source | Point | Status |
| --- | --- | --- |
| IRC § 501(c)(3) and the IRS determination process (Form 1023) | Federal tax recognition of an entity formed under state law. | V (cite the statute and Treas. Reg. § 1.501(c)(3)-1) |
| NAAG, *State Attorneys General Powers and Responsibilities* (4th ed.), ch. 12 | State AGs are the primary regulators of charitable nonprofits: they ensure assets are used for charitable purposes and enforce directors' fiduciary duties. In most states only the AG has standing to act. | P (courtesy chapter, naag.org) |
| NAAG, "Charities Regulation 101" | Most AGs can pursue relief against directors who breach fiduciary duties and can dissolve the organization. | P |
| N.Y. Not-for-Profit Corp. Law § 112 | The AG may sue to remove a director for cause (§ 706) and to dissolve a corporation (art. 11), among other actions. | P (nysenate.gov) |

- **Fact to carry forward:** in the nonprofit pattern, federal recognition (IRS) does not govern the entity, but state attorneys general supervise charitable nonprofits. They can seek to remove directors and to dissolve.
- **Comparison (author, 2026-11-18):** the paper compares the US nonprofit approach with the Swiss foundation approach, where they are the same and where they differ. Functionally, the state attorney general and the Swiss supervisory authority play the same role. Points to source for the comparison: who may act, on what grounds, by what procedure (the AG goes to court; the Swiss authority decides itself, subject to appeal), and over which entities.

## 7. Comparators already in the record (not US law)

- ADGM DLT Foundations Regulations 2023: token-holder rights (s. 40, reported); accounts published and publicly filed (ss. 49, 51; see `ton-case-study.md`, Q6). P (regulations PDF).
- Cayman foundation companies with token-holder powers (ENS, Fluid): noted in the 2026-11-16 screen work; not yet sourced here [V].

## Next steps for this map

1. Read each V item in the original and update the status codes.
2. Add the confirmed entries to `bibliography.md` with source notes.
3. Search for cases contesting a wrapped DAO's form (section 2).
4. Source the AG and supervisor comparison (section 6).
