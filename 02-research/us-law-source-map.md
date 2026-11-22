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
- Cayman foundation companies with token-holder powers (ENS, Fluid): noted in the 2026-11-16 screen work. Statute and the Lido entities now mapped in § 8.4; ENS and Fluid still [V].

## 8. Phase 4 research block (2026-11-21)

Added by Claude (Opus 5.5, High), per `AI_USE.md` ("US-law source map"). The pending list was carried into Phase 4 on 2026-11-18. Neutral, as above: what the sources say, no argument. Status codes as at the top.

### 8.1 State attorneys general and DUNAs

- **NAAG, *State Attorneys General: Powers and Responsibilities* ch. 12 (4th ed.).** The attorney general's regulatory responsibility extends to all charitable assets, including those held by unincorporated associations. **S** (NAAG courtesy chapter PDF; edition date [VERIFY]). <https://www.naag.org/wp-content/uploads/2021/02/Powers-and-Duties-4th-Edition-Chapter-12.0-Prot-and-Regs-of-Nonprofits-and-Charitable-Assets-Courtesy-Chapter.pdf>
- **Wyo. Stat. Ann. § 17-32-101 et seq. (DUNA Act, 2024), merger provision.** Property held for a charitable purpose before a merger may not be diverted from the objects for which it was given. **P** (legislature page for SF0050). <https://www.wyoleg.gov/Legislation/2024/SF0050>
- **2026 Wyo. Sess. Laws ch. 25 (SF0022).** On winding up, assets are distributed as federal law requires (see L08). **P**.
- **Reading of the record:** no source found that subjects a DUNA as such to attorney-general supervision. Whether the attorney general's charitable-assets jurisdiction reaches a particular DUNA turns on whether it holds assets for a charitable purpose. No court or attorney-general action on a DUNA found (searched 2026-11-21). [V: Alabama and West Virginia acts; any state AG guidance]

### 8.2 Member liability across state lines

- **LLC forms (Wyoming DAO LLC, Tennessee DO).** Foreign-LLC statutes based on the uniform acts provide that the law of the state of formation governs a member's liability as a member for the company's debts. Examples seen: Iowa Code § 489.901(1)(b); Ohio Rev. Code § 1706.51(A)(2); Minn. Stat. § 322C.0801; Ariz. Rev. Stat. § 29-3901 (internal affairs; subsection D limits rights in-state). **P** (official state code pages). Not yet checked: California, New York, Delaware, Texas [V].
- **UNA forms (DUNA).** The Revised Uniform Unincorporated Nonprofit Association Act has a governing-law section: unless the governing principles specify another jurisdiction, the law of the jurisdiction where the association has its main place of activities governs [V: full text and scope; Iowa Code § 501B.4 seen in part]. The uniform acts provide that a member is not liable for the association's obligations solely because of membership (e.g., Ark. Code Ann. § 4-28-608). **P** in part. No case found applying another state's DUNA law to member liability [V].
- **Utah LLD:** not yet checked [V].

### 8.3 Federal charters

- ***McCulloch v. Maryland*, 17 U.S. (4 Wheat.) 316 (1819).** Federal power to charter a corporation (the Second Bank). **S** (via CRS); pinpoint [V].
- **CRS, *Congressional or Federal Charters: Overview and Enduring Issues*, RS22230 (Apr. 19, 2013).** Congress has chartered banks, government-sponsored enterprises, commercial corporations and others; charters set governance, powers and federal oversight. **S/P** (CRS text seen in part).
- **CRS, *Congressionally Chartered Nonprofit Organizations ("Title 36 Corporations")*, RL30340 (versions 2004–2011).** Title 36 corporations generally operate under both federal and state charters, most having been chartered under state law first; they are not agencies of the United States; the chartering process is described as honorific, which may mislead the public into assuming a direct federal relationship. **P** in part (CRS text via EveryCRSReport and ALA DttP summary). Later report: R47236 (*Title 36 Charters: The History and Evolution of Congressional Practices*) [V].
- **12 U.S.C. § 1818(e).** Federal banking agencies may remove or prohibit institution-affiliated parties (directors, officers, controlling shareholders, 12 U.S.C. § 1813(u)) from participating in a bank's affairs. **P** (eCFR, 12 C.F.R. pt. 19; OCC enforcement pages).

### 8.4 Cayman foundation companies

- **Foundation Companies Act (2025 Revision) (Cayman Is.)** (originally Law 29 of 2017, in force Oct. 2017). **P** (CIMA consolidated text; sections not yet read).
- **Practitioner guides (Ogier, Conyers, Mourant, Appleby, Carey Olsen).** A foundation company may have no members; if it has none it must appoint a supervisor, a private role with no ownership or economic entitlement that, at minimum, may attend and vote at general meetings; constitutional documents may give a founder or others power to appoint or remove directors; the members' liability shield is described as untested in Cayman courts. **S**.
- **Lido DAO entities.** Lido Alliance BORG Foundation (Snapshot vote opened Aug. 29, 2024): a memberless, beneficiary-less Cayman foundation company whose bylaws let Lido DAO remove directors and co-approve new ones. Lido Labs BORG Foundation (on-chain vote 190 enacted July 28, 2025; "yes" votes about 5.09% of LDO supply as posted) and Lido Ecosystem BORG Foundation (2025): same form. **P** (Lido governance forum and Snapshot pages). Timing against *Samuels*: complaint filed Dec. 2023; motion-to-dismiss order Nov. 18, 2024; Alliance BORG vote opened in between; Labs and Ecosystem BORGs followed in 2025.

### 8.5 Concentration of token voting power

- **Robin Fritsch, Marino Müller & Roger Wattenhofer, *Analyzing Voting Power in Decentralized Governance: Who Controls DAOs?*, 5 Blockchain: Rsch. & Applications 100208 (2024)** (Compound, Uniswap, ENS). Finds most voting power concentrated in a small number of addresses, which rarely vote against the community outcome. **P** (abstract; full text to read).
- **Rainer Feichtinger, Robin Fritsch, Yann Vonlanthen & Roger Wattenhofer, *The Hidden Shortcomings of (D)AOs: An Empirical Study of On-Chain Governance*, arXiv:2302.12125 (2023)** (21 DAOs). Reports high concentration of voting rights; in most DAOs fewer than ten participants control a majority of voting power [V: exact statement and pinpoint]. **P** (abstract and excerpt).
- **Brett Falk et al., *Blockchain Governance: An Empirical Analysis of User Engagement on DAOs*, arXiv:2407.10945 (2024)** (Uniswap, Compound, Aave, Lido). Finds voting power highly concentrated in all four. **P** (abstract).
- ***Samuels* complaint, as reported:** about 64% of LDO held by founders and early investors [S; read the complaint].

### 8.6 Status updates for §§ 2 and 5

- ***Samuels v. Lido DAO*.** Ninth Circuit No. 25-5701 (*Samuels v. AH Capital Management, LLC*), filed Sept. 9, 2025; docket active as of Mar. 2026 [V: subject (reported as arbitration) and current status]. **P** (docket listing).
- **CLARITY Act (H.R. 3633).** Passed the House July 17, 2025 (294–134); reported by Senate Banking June 1, 2026; cloture on the motion to proceed failed 49–50 on Sept. 15, 2026. Passage this Congress is widely viewed as unlikely. **S** (Orrick, Oct. 2, 2026; CRS IF13313, Sept. 15, 2026) [V: congress.gov].

### 8.7 Swiss items (for `legal-sources-verified.md` and the bibliography)

- **ZGB Arts. 64–65, 75 (Verein).** The members' meeting is the supreme body (Art. 64(1)); one fifth of members can require a meeting (Art. 64(3)); the meeting admits and expels members, elects the board and decides all matters not given to another body (Art. 65(1)); a member may challenge an unlawful resolution in court (Art. 75). **S** (statutory text quoted in university and cantonal materials); Fedlex check pending [V]. No supervisory authority appears in Arts. 60–79 [V].
- **Tezos Foundation, 2017–18 (press).** The Swiss foundation supervisory authority set the foundation a deadline to restore its three-member council after one member left (swissinfo.ch). **S**. Press is not a codebook practice source (T2-22); usable in the article as reported fact.

### 8.8 Documents uploaded by the author (2026-11-21)

- ***Samuels* complaint**, Case No. 3:23-cv-06492, ECF No. 1 (N.D. Cal. filed Dec. 17, 2023), with civil cover sheet (ECF No. 1-1). ¶ 30: of one billion LDO, 64% went to founders and initial investors, and the remaining 36% went to the treasury, "to be distributed as the holders of the other 64% see fit." ¶ 81: because 64% is dedicated to founders and early investors, ordinary investors cannot exert meaningful influence on governance. These are allegations, not findings. **P**. Replaces the secondary report in § 8.5.
- **CRS, *Title 36 Charters: The History and Evolution of Congressional Practices*, R47236 (Sept. 8, 2022).** **P** (full text uploaded); pinpoints to take at drafting.
- **Ala. S.B. 277, 2026 Reg. Sess. (introduced text).** § 10A-17-2.03: Alabama law governs a DUNA formed in Alabama, and its governing principles must name the jurisdiction of formation. Members are not liable merely because they are members. On winding up, remaining property goes to an entity with similar nonprofit purposes only if other law requires it; otherwise it is distributed under the governing principles or, failing those, to members in proportion to their interests. No attorney-general provision found by text search. **P** for the introduced text; compare with the enrolled text (L09) [V]. West Virginia text: pending upload.

- ***Samuels* order re motions to dismiss**, No. 23-cv-06492-VC, ECF No. 115 (N.D. Cal. Nov. 18, 2024): the complaint plausibly alleges that Lido DAO is a general partnership under California law, and that members of that partnership can be held liable. **P**; pinpoints to take at drafting.
- ***Samuels* district docket** (CourtListener export, 2026-11-21, 339 entries): ECF No. 201 (Oct. 21, 2025) stays the case pending appeal, with joint status reports every 120 days; latest is ECF No. 204 (Oct. 16, 2026). The appeal (ECF No. 193, filed Sept. 5, 2025, by the investor defendants) is from the Order Denying Motion to Compel Arbitration (ECF No. 192, Sept. 3, 2025), under 9 U.S.C. § 16(a)(1)(B). The Nov. 18, 2024 order is not on appeal. **P**.
- **Ala. S.B. 277 (enrolled)**: same governing-law section (§ 10A-17-2.03); effective Oct. 1, 2026. No attorney-general provision found. **P**. Supersedes the introduced-text note above.
- **Feichtinger et al. (2023)**, full text: in 17 of 21 governance systems a majority of voting power, enough to decide any vote, is controlled by fewer than 10 participants. **P** (abstract/introduction, arXiv v2).
- **Fritsch, Müller & Wattenhofer**, arXiv:2204.01176v1 full text: voting rights concentrated among a small number of addresses. **P** (preprint; journal version 2024 to match).
- **Wyo. SF0050 (2024), bill text** (24LSO-0104; this copy is the bill, not the enrolled act): property held for a charitable purpose may not be diverted in a merger unless the organization obtains an order of the attorney general, or of a district court in a proceeding of which the attorney general has notice. This is the only attorney-general role found in the DUNA Act; it applies to charitable property only. **P** [V: confirm against the enrolled act].
- **Wyo. SF0022, Enrolled Act No. 21 (2026), full enrolled text**: on winding up, assets go first to another entity with similar nonprofit purposes where state law other than the DUNA chapter, or federal law, requires it; otherwise under the governing principles; failing those, to current members. So the federal-law clause applies only when other law (e.g., tax-exemption rules) requires it. No attorney-general provision added. **P**; confirms L08.
- West Virginia DUNA text: final text not retrievable from the legislature's site (2026-11-21); L10 code pages remain the source [V].

## Next steps for this map

1. Read the remaining V items in the original: the CryptoFED dismissal date; *Samuels* and *Houghton* current status; the Sarcuni and Samuels pinpoints; Brunson pinpoints; DUNA tax design; the comparison table's [VERIFY] cells.
2. Add the confirmed entries to `bibliography.md` with source notes.
