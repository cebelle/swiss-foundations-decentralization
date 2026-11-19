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
| Vermont blockchain-based LLC (BBLLC) | 11 V.S.A. §§ 4171–4176 (2017, No. 205 (Adj. Sess.), § 7) | 2018 | An LLC that uses blockchain for a material part of its business may elect BBLLC status. Not DAO-specific. | P (legislature.vermont.gov) |
| Wyoming DAO Supplement (DAO LLC) | Wyo. Stat. §§ 17-31-101 to -116 (SF0038, 2021; amended SF0068, 2022; SF0075, 2023) | eff. 1.7.2021 | A DAO is an LLC under this chapter; the LLC Act applies where not inconsistent (§ 17-31-103). | P (enrolled SF0038; Secretary of State statute list) |
| Tennessee decentralized organization | Tenn. Code Ann. §§ 48-250-101 to -115 (2022 Tenn. Pub. Acts ch. 852) | eff. 20.4.2022 | An LLC may elect decentralized-organization status; the LLC Act applies where not inconsistent (§ 48-250-102). | P (chaptered HB2645) |
| Utah DAO Act (LLD) | Utah Code §§ 48-5-101 to -406 (H.B. 357, 2023 Gen. Sess., ch. 85; amended H.B. 318, 2024) | eff. 1.1.2024 | Legal personality for a DAO that meets the Act (§ 48-5-104); registrations accepted from 3.1.2024; implementing rule Utah Admin. Code R154-3. | P (le.utah.gov; Utah Department of Commerce) |
| Wyoming DUNA Act | Wyo. Stat. §§ 17-32-101 to -129 (SF0050, signed 7.3.2024) | eff. 1.7.2024 | Decentralized unincorporated nonprofit association with at least 100 members; governance may run through smart contracts. | P (enrolled bill, wyoleg.gov) |
| Wyoming DUNA amendments | SF0022, Enrolled Act 21, 2026 Wyo. Sess. Laws ch. 25 | eff. 1.7.2026 | Aligns the DUNA Act with the UNA Act; automatic conversion to a UNA in specified cases; assets distributed as federal law requires on winding up. | P (bill summary and digest, wyoleg.gov) |
| Alabama DUNA Act | SB 277 (2026 Reg. Sess.), enrolled 16.3.2026 | enacted 2.4.2026; eff. 1.10.2026 (reported) | Adopts the DUNA model (at least 100 members, common nonprofit purpose). | P (enrolled bill, alison.legislature.state.al.us); S (effective date) |
| West Virginia DUNA Act | W. Va. Code §§ 36-13-1 to -31 (HB 5060, 2026) | eff. 1.7.2026 (§ 36-13-31) | Adopts the DUNA model; a DUNA is a legal entity separate from its members (§ 36-13-7). | P (code.wvlegislature.gov) |

- **Count on current sources:** five states have DAO-specific entity statutes: Wyoming (two forms), Tennessee, Utah, Alabama and West Virginia. Vermont's BBLLC makes six if counted. DUNA bills were also filed in 2026 in Arkansas (HB1533), Texas (HB4518) and New Mexico (HB363); their status is unchecked (S). The forms differ: three LLC variants (WY, TN, UT) and a nonprofit association model (WY, AL, WV).
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
| *In re Registration Statement of American CryptoFED DAO LLC* | SEC Admin. Proc. File No. 3-21243; ALJ initial decision 17.5.2023 (stop order) | The SEC proceeded against a Wyoming DAO LLC as the registrant; the stop order rested on missing audited financial statements, not on the entity form. The SEC later dismissed the proceedings [VERIFY date]. | P (sec.gov) |

- **Recognition outside the courts:** Uniswap governance adopted a Wyoming DUNA ("DUNI") in 2025. Its association agreement sends disputes exclusively to the Wyoming Chancery Court (Association Agreement, ss. VIII.05, XI.02; uniswapfoundation.org). P
- **What the cases show so far:** every court case above concerns a DAO with no legal wrapper, and the courts fell back on default law (general partnership or unincorporated association). No court case was found in which a DAO LLC, LLD or DUNA was contested, whether recognized or not (searched again 2026-11-18, including Marshall Islands DAO LLCs). The SEC's CryptoFED proceeding treated a Wyoming DAO LLC as the registrant without questioning the form.
- **Search done (author's request, 2026-11-18):** for cases in which a wrapped DAO's form was contested and a court ruled on it. None found to date. The pathway so far is statutory and administrative (CryptoFED; Uniswap's DUNI), not yet judicial. Recheck before drafting.

## 3. "... the IRS ... do[es] not consistently honor the forms"

| Source | Citation | Point | Status |
| --- | --- | --- | --- |
| Entity classification ("check-the-box") | Treas. Reg. § 301.7701-3(a), (b)(1), (c)(1)(i) (T.D. 8697, 61 Fed. Reg. 66,584 (Dec. 18, 1996)) | A domestic eligible entity is a partnership by default if it has two or more members, and may elect otherwise on Form 8832. | P (eCFR, govinfo) |
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

## 5. Federal legislation and agency action touching decentralized governance

| Bill or action | Status (as of 2026-11-18) | Relevance | Status code |
| --- | --- | --- | --- |
| Digital Asset Market Clarity Act (CLARITY), H.R. 3633, 119th Cong. | Passed House 17.7.2025 (294–134). Senate Banking reported 14.5.2026 (15–9). Cloture on the motion to proceed failed 15.9.2026 (49–50). A motion to reconsider was entered, and a lame-duck session is the reported window. | The Senate text reportedly treats decentralized governance systems as distinct from coordinated entities, and says participation in decentralized governance alone does not imply control. | S (multiple outlets agree on dates and votes); V (Senate text and current status on congress.gov) |
| Promoting Innovation in Blockchain Development Act | Introduced 26.2.2026 (reported) | Developer liability; context only. | S; V |
| SEC interpretive release, joined by the CFTC: *Application of the Federal Securities Laws to Certain Types of Crypto Assets and Certain Transactions Involving Crypto Assets* | Release Nos. 33-11412, 34-105020; File No. S7-2026-09; issued 17.3.2026; 91 Fed. Reg. 13,714 (Mar. 23, 2026) | Defines "functional", "decentralized" and "central party" in footnotes 49, 50 and 54, for the release's purposes only. See section 5A. | P (Federal Register; sec.gov) |
| SEC Division of Corporation Finance, crypto-asset FAQs 1.4–1.6 | Added 2.11.2026 (page last updated 2.11.2026) | Staff views on broad-based governance, foundations and "overseeing participation"; functional is distinct from decentralized. Not a Commission rule. See section 5A. | P (sec.gov) |
| UNCITRAL, *Exploratory work on decentralized autonomous organizations: review and possible model text*, A/CN.9/1267 | 13.5.2026, for the 59th session (29.6–10.7.2026) | A review of national DAO laws and an initial draft model law on DAOs. | P (uncitral.un.org); V (session outcome) |

- No federal entity-recognition statute for DAOs was found. That is the gap the paper's remedy addresses.

## 5A. The SEC's decentralization vocabulary

Read in the primary text on 2026-11-18.

**What the Commission's release says** (91 Fed. Reg. 13,714; all three definitions are footnotes to Section III.A, *Digital Commodities*, at 13,718):
- **"Functional" (n.49):** a crypto system is functional "if the system's native crypto asset can be used on the system in accordance with the programmatic utility of the system."
- **"Decentralized" (n.50):** a crypto system is decentralized "if the crypto system functions and operates autonomously with no person, entity, or group of persons or entities having operational, economic, or voting control of the crypto system."
- **"Central party" (n.54):** "a person, entity, or group of persons or entities having operational, economic, or voting control of a crypto system."
- **Main text:** a functional crypto system "does not have a central party that oversees participation or distributes rewards to users" (at 13,718).
- **Status:** each definition is expressly "[f]or purposes of this release". The release is an interpretation of the Howey test, not an entity-law or governance standard.

**What the SEC staff add** (FAQs 1.4–1.6, 2.11.2026; staff views, "not a rule, regulation or statement of the Securities and Exchange Commission"):
- **Broad-based governance (n.2).** A governance system qualifies if it is:
  - transparent: proposals, votes, outcomes and implementation are publicly documented in good time;
  - rules-based: pre-set procedures that no single stakeholder or coordinated group can change unilaterally;
  - wide and diverse: authority is not concentrated, directly or through delegation.
- **FAQ 1.4.** Participants in broad-based governance generally are not a "group" if they are not affiliated and have no agreement to act in concert, including through delegation. The answer is the same where the governance system sits inside an organization, association or foundation and participation rests on holding the native token. Even a group must have actual control to be a central party.
- **FAQ 1.4, n.4.** The foundation itself can be a central party "where it has operational, economic, or voting control over another crypto system", for example by setting operating parameters for applications.
- **FAQ 1.4, n.3.** The view applies only to Section III of the release, not to "group" definitions under the Securities Act or Exchange Act.
- **FAQ 1.5.** A central party "oversees participation" when it has unilateral authority to:
  - grant or limit access;
  - set or change voting processes for upgrades, protocol changes or token distributions;
  - control who validates;
  - modify the code, reverse transactions or revoke access.

  It does not oversee participation where operation is fully automatic under rules-based code, or where all discretion runs solely through broad-based governance.
- **FAQ 1.6.** "Functional" and "decentralized" are distinct concepts. A functional system with a digital commodity "has characteristics of decentralization, although the degree of decentralization can vary depending on the facts and circumstances."

**Research notes (not the author's argument):**
- **Binary or spectrum.** The release's definition is binary: no one with control. The spectrum language comes only from staff (FAQ 1.6). Any account of decentralization as a spectrum finds its hook in the staff FAQ, not in the Commission's text.
- **Foundation governance vs. protocol governance.** The SEC test looks at control of the *crypto system*. A foundation is a central party only if it controls the system (n.4), which lines up with the distinction between governance over the foundation and governance over the protocol. A Stiftung council's powers over the foundation are not, by themselves, control of the protocol; FAQ 1.5's list gives the test for when they become it.
- **Codebook fit.** FAQ 1.5's four "unilateral authority" items line up with the council-power and protocol-control variables. Whether to map them formally is a Phase 4 decision for the author; codebook v1 stays locked.
- **Limits a skeptic will raise:**
  - the definitions serve securities classification;
  - staff views are not binding and can change with the Commission;
  - n.3 expressly confines the "group" reading.

## 6. The remedy's model: state formation plus federal recognition (the nonprofit pattern)

| Source | Point | Status |
| --- | --- | --- |
| IRC § 501(c)(3) and the IRS determination process (Form 1023) | Federal tax recognition of an entity formed under state law. | V (cite the statute and Treas. Reg. § 1.501(c)(3)-1) |
| NAAG, *State Attorneys General Powers and Responsibilities* (4th ed.), ch. 12 | State AGs are the primary regulators of charitable nonprofits: they ensure assets are used for charitable purposes and enforce directors' fiduciary duties. In most states only the AG has standing to act. | P (courtesy chapter, naag.org) |
| NAAG, "Charities Regulation 101" | Most AGs can pursue relief against directors who breach fiduciary duties and can dissolve the organization. | P |
| N.Y. Not-for-Profit Corp. Law § 112 | The AG may sue to remove a director for cause (§ 706) and to dissolve a corporation (art. 11), among other actions. | P (nysenate.gov) |

- **Fact to carry forward:** in the nonprofit pattern, federal recognition (IRS) does not govern the entity, but state attorneys general supervise charitable nonprofits. They can seek to remove directors and to dissolve.
- **Comparison (author, 2026-11-18):** the paper compares the US nonprofit approach with the Swiss foundation approach, where they are the same and where they differ. Functionally, the state attorney general and the Swiss supervisory authority play the same role. The table sets out the law on each side (sourced 2026-11-18). It records what the statutes provide, not how often they are used.

| Question | US: state attorney general (charitable nonprofits) | Switzerland: federal or cantonal supervisory authority (Stiftung) | Same or different |
| --- | --- | --- | --- |
| Basis | Common law of charitable trusts and state statute. In California, primary responsibility for supervising charitable trusts and protecting assets of public benefit corporations "resides in the Attorney General" (Cal. Gov. Code § 12598(a)). | Federal statute: foundations are supervised by the public body they belong to (Art. 84 para. 1 ZGB). | Same function |
| Which entities | Charitable trusts and charitable or public-benefit nonprofits. Not every nonprofit form (e.g., mutual-benefit corporations, possibly UNAs and DUNAs) [VERIFY by state]. | Every Stiftung except family and church foundations (Art. 87 ZGB [VERIFY pinpoint]). | Narrower in the US |
| Inspection | A California public benefit corporation "is subject at all times to examination by the Attorney General" (Cal. Corp. Code § 5250). | The authority ensures assets are used for their purposes (Art. 84 para. 2 ZGB); it receives annual reports and accounts [VERIFY pinpoint]. | Same function |
| Removing directors | The AG (or 10% of members) may sue to remove a director for cause; the court decides and may bar re-election (N.Y. N-PCL §§ 706(d), 112(a)(4)). | The authority takes the necessary measures when an organ is unlawfully composed, including appointing the missing organ or an administrator (Art. 83d para. 1 ZGB). Removal powers can also come from the deed (e.g., TON deed Art. 7(e)). | Same goal; different procedure (court action vs. administrative order, appealable) |
| Changing purpose or constitution | Through the court (cy pres or deviation), with the AG as a party [VERIFY state statute]. | The authority itself amends purpose or organisation (Arts. 85, 86, 86a, 86b ZGB). | Different: in the US a court changes it; in Switzerland the administrative authority does |
| Dissolution | The AG may bring an action for judicial dissolution (N.Y. N-PCL §§ 112(a)(5), 1101). In any judicial dissolution the AG is a necessary party (§ 1102(b)). | The authority dissolves the foundation on application or of its own motion (Art. 88 para. 1 ZGB). | Same outcome; different decider |
| Others with standing | Members, directors, officers and certain others may also sue; the AG must be notified and may intervene (Cal. Corp. Code § 5142(a)). | Beneficiaries, creditors, the founder, co-founders, and former and current council members may complain to the authority (Art. 84 para. 3 ZGB). There are no members. | Different: a US nonprofit can have members with standing; a Stiftung cannot |

**Open questions for the comparison:**
- whether a DUNA or a non-charitable UNA falls under AG supervision in Wyoming, Alabama and West Virginia [VERIFY];
- the cy pres statute in one model state.

## 7. Comparators already in the record (not US law)

- ADGM DLT Foundations Regulations 2023: token-holder rights (s. 40, reported); accounts published and publicly filed (ss. 49, 51; see `ton-case-study.md`, Q6). P (regulations PDF).
- Cayman foundation companies with token-holder powers (ENS, Fluid): noted in the 2026-11-16 screen work; not yet sourced here [V].

## Next steps for this map

1. Read the remaining V items in the original: the CryptoFED dismissal date; *Samuels* and *Houghton* current status; the Sarcuni and Samuels pinpoints; Brunson pinpoints; DUNA tax design; the comparison table's [VERIFY] cells.
2. Add the confirmed entries to `bibliography.md` with source notes.
