"""Build bibliography.md and one source note per legal/policy source (L-notes).

Entries are only sources checked against the original (status P in the source map).
Edit ENTRIES and re-run. Foundation sources are built separately by build_source_notes.py.
"""
import pathlib, re
OUT = pathlib.Path("02-research")
OFF = "official text"
UNOFF = "unofficial compilation of the statute; re-check on the official site before citing [VERIFY]"
ENTRIES = [
 # (section, short id, citation, url, pinpoints, claim, where used, checked against, date)
 ("Swiss law","zgb","Schweizerisches Zivilgesetzbuch [ZGB] [Civil Code] Dec. 10, 1907, SR 210 (Switz.), as in force July 1, 2026","https://www.fedlex.admin.ch/eli/cc/24/233_245_233/de",
  "Arts. 57 para. 1–3; 83b para. 1–4; 83d para. 1–2; 84 para. 1–3; 86a para. 1–5; 88 para. 1–2","Foundation law anchors: dissolution and assets, audit, defective organisation, supervision and complaints, founder's reservation, dissolution by the authority.","codebook F3, F5–F7; legal-sources-verified.md; us-law-source-map.md § 6",f"{OFF} (Fedlex, German; DE/FR/IT binding)","2026-11-18"),
 ("Swiss law","as-2022-452","Bundesgesetz vom 17. Dezember 2021 (Stärkung des Stiftungsstandorts Schweiz), AS 2022 452 (Switz.)","https://www.fedlex.admin.ch/eli/cc/24/233_245_233/de",
  "amending Arts. 84 para. 3 and 86a paras. 1, 3, 4 ZGB; in force Jan. 1, 2024","The current founder's-reservation and complaint rules date from 1.1.2024.","codebook F3; legal-sources-verified.md",f"{OFF} (Fedlex amendment note to SR 210)","2026-11-18"),
 ("US state entity statutes","vt-bbllc","Vt. Stat. Ann. tit. 11, §§ 4171–4176 (2017, No. 205 (Adj. Sess.), § 7)","https://legislature.vermont.gov/statutes/section/11/025/04172",
  "§ 4172 (election); § 4176 (LLC Act governs except where inconsistent)","An LLC using blockchain for a material part of its business may elect BBLLC status.","us-law-source-map.md § 1","Vermont Statutes Online (state legislature)","2026-11-18"),
 ("US state entity statutes","wy-dao","Wyo. Stat. Ann. §§ 17-31-101 to -116 (2021 Wyo. Sess. Laws (SF0038), amended 2022 (SF0068))","https://www.wyoleg.gov/2021/Enroll/SF0038.pdf",
  "§ 17-31-103 (LLC Act applies where not inconsistent); § 17-31-104 (DAO is an LLC); effective July 1, 2021","First DAO LLC statute.","us-law-source-map.md § 1",f"{OFF} (enrolled act); Secretary of State statute list","2026-11-18"),
 ("US state entity statutes","tn-do","Tenn. Code Ann. §§ 48-250-101 to -115 (2022 Tenn. Pub. Acts ch. 852)","https://legiscan.com/TN/text/HB2645/id/2573944/Tennessee-2021-HB2645-Chaptered.pdf",
  "§ 48-250-102 (LLC Act applies where not inconsistent); § 48-250-103 (status); effective Apr. 20, 2022","An LLC may elect decentralized-organization status.","us-law-source-map.md § 1","chaptered act (LegiScan copy of the official text)","2026-11-18"),
 ("US state entity statutes","ut-dao","Utah Code Ann. §§ 48-5-101 to -406 (H.B. 357, 2023 Gen. Sess., ch. 85; amended H.B. 318, 2024); Utah Admin. Code R154-3","https://le.utah.gov/xcode/Title48/Chapter5/C48-5_2023050320240101.pdf",
  "§ 48-5-104; § 48-5-406; effective Jan. 1, 2024","Legal personality for qualifying DAOs (LLDs).","us-law-source-map.md § 1",f"{OFF} (le.utah.gov)","2026-11-18"),
 ("US state entity statutes","wy-duna","Wyo. Stat. Ann. §§ 17-32-101 to -129 (2024 Wyo. Sess. Laws (SF0050))","https://www.wyoleg.gov",
  "effective July 1, 2024","Decentralized unincorporated nonprofit association (at least 100 members).","us-law-source-map.md § 1",f"{OFF} (enrolled act; exact URL to add [VERIFY URL])","2026-11-18"),
 ("US state entity statutes","wy-sf0022","2026 Wyo. Sess. Laws ch. 25 (Enrolled Act 21, SF0022)","https://www.wyoleg.gov/Legislation/2026/SF0022",
  "effective July 1, 2026","Aligns the DUNA Act with the UNA Act; winding-up distributions follow federal law.","us-law-source-map.md § 1","bill page and digest (wyoleg.gov)","2026-11-18"),
 ("US state entity statutes","al-duna","S.B. 277, 2026 Reg. Sess. (Ala. 2026) (enrolled)","https://alison.legislature.state.al.us/files/pdf/SearchableInstruments/2026RS/SB277-enr.pdf",
  "enrolled Mar. 16, 2026; enacted Apr. 2, 2026; effective date reported as Oct. 1, 2026 [VERIFY in enrolled text]","Alabama adopts the DUNA model.","us-law-source-map.md § 1",f"{OFF} (enrolled bill)","2026-11-18"),
 ("US state entity statutes","wv-duna","W. Va. Code §§ 36-13-1 to -31 (H.B. 5060, 2026)","https://code.wvlegislature.gov/36-13-31/",
  "§ 36-13-7 (separate legal entity); § 36-13-31 (effective July 1, 2026)","West Virginia adopts the DUNA model.","us-law-source-map.md § 1",f"{OFF} (code.wvlegislature.gov)","2026-11-18"),
 ("US federal","treas-reg-7701","Treas. Reg. § 301.7701-3 (as amended); T.D. 8697, 61 Fed. Reg. 66,584 (Dec. 18, 1996)","https://www.ecfr.gov/current/title-26/chapter-I/subchapter-F/part-301/subpart-ECFR5ffaf3310af6b61/section-301.7701-3",
  "§ 301.7701-3(a), (b)(1), (c)(1)(i)","Default partnership classification for a domestic eligible entity with two or more members; Form 8832 election.","us-law-source-map.md § 3","eCFR (current to 8/17/2026) and govinfo","2026-11-18"),
 ("US federal","sec-33-11412","Application of the Federal Securities Laws to Certain Types of Crypto Assets and Certain Transactions Involving Crypto Assets, Securities Act Release No. 33-11412, Exchange Act Release No. 34-105020, 91 Fed. Reg. 13,714 (Mar. 23, 2026) (CFTC joining)","https://www.federalregister.gov/documents/2026/03/23/2026-05635/application-of-the-federal-securities-laws-to-certain-types-of-crypto-assets-and-certain",
  "91 Fed. Reg. at 13,718 & nn.49, 50, 54","Definitions of \"functional\", \"decentralized\" and \"central party\", each for the release's purposes only.","us-law-source-map.md § 5A",f"{OFF} (Federal Register HTML)","2026-11-18"),
 ("US federal","sec-faq","SEC Div. of Corp. Fin., Frequently Asked Questions on the Application of the Federal Securities Laws to Certain Types of Crypto Assets and Certain Transactions Involving Crypto Assets, Questions 1.4–1.6 (added Nov. 2, 2026)","https://www.sec.gov/about/divisions-offices/division-corporation-finance/faqs-crypto-assets",
  "Q. 1.4 & nn.2–4; Q. 1.5; Q. 1.6","Staff views: broad-based governance, foundations as central parties, overseeing participation, degree of decentralization. Not a Commission statement.","us-law-source-map.md § 5A","sec.gov live page (last updated Nov. 2, 2026); a cached Sept. 25 copy lacks these questions","2026-11-18"),
 ("US federal","cryptofed","In re Registration Statement of American CryptoFED DAO LLC, Admin. Proc. File No. 3-21243, Initial Decision Release No. 1415 (ALJ May 17, 2023)","https://www.sec.gov/files/alj/aljdec/id1415.pdf",
  "initial decision (stop order); later dismissal date [VERIFY]","The SEC treated a Wyoming DAO LLC as the registrant; the stop order turned on missing audited financials.","us-law-source-map.md § 2","sec.gov","2026-11-18"),
 ("US nonprofit oversight","ny-npcl","N.Y. Not-for-Profit Corp. Law §§ 112(a)(4)–(5), 706(d), 1101, 1102(b)","https://www.nysenate.gov/legislation/laws/NPC/112",
  "§ 112(a)(4)–(5); § 706(d); § 1102(b)","AG actions to remove directors for cause and to dissolve; AG a necessary party to judicial dissolution.","us-law-source-map.md § 6","nysenate.gov (§§ 112, 706, 1102); Justia (§ 706(d)) "+"[VERIFY § 706(d) on nysenate.gov]","2026-11-18"),
 ("US nonprofit oversight","ca-corp","Cal. Corp. Code §§ 5142(a), 5250","https://california.public.law/codes/corporations_code_section_5142",
  "§ 5142(a)(5); § 5250","Standing to remedy breach of charitable trust; AG examination of public benefit corporations.","us-law-source-map.md § 6",UNOFF,"2026-11-18"),
 ("US nonprofit oversight","ca-gov","Cal. Gov't Code § 12598(a)","https://law.justia.com/codes/california/code-gov/title-2/division-3/part-2/chapter-6/article-7/section-12598",
  "§ 12598(a)","Primary responsibility for supervising charitable trusts resides in the AG.","us-law-source-map.md § 6",UNOFF,"2026-11-18"),
 ("US nonprofit oversight","naag","Nat'l Ass'n of Att'ys Gen., State Attorneys General: Powers and Responsibilities ch. 12 (4th ed.)","https://www.naag.org",
  "ch. 12","State AGs as primary regulators of charitable nonprofits.","us-law-source-map.md § 6","NAAG courtesy chapter (full page URL to add) [VERIFY URL]","2026-11-18"),
 ("Private ordering","duni","Decentralized Unincorporated Nonprofit Association of Uniswap (DUNI), Association Agreement (Wyo. DUNA, 2025)","https://uniswapfoundation.org/duni/DUNI-Association-Agreement.pdf",
  "ss. VIII.05, XI.02","Exclusive forum in the Wyoming Chancery Court.","us-law-source-map.md § 2","agreement PDF (uniswapfoundation.org)","2026-11-18"),
 ("International and comparator","uncitral","UNCITRAL Secretariat, Exploratory Work on Decentralized Autonomous Organizations, U.N. Doc. A/CN.9/1267 (May 13, 2026)","https://uncitral.un.org",
  "whole document; outcome of the 59th session [VERIFY]","Review of national DAO laws and an initial draft model law.","us-law-source-map.md § 5","uncitral.un.org (document URL to add) [VERIFY URL]","2026-11-18"),
 ("International and comparator","adgm-dlt","Distributed Ledger Technology Foundations Regulations 2023 (ADGM)","https://www.adgm.com",
  "ss. 14(12)(j), 49(1), 51(1)–(2), 52(3), 52(6)–(7)","Accounts must be published on the website and filed with the Registrar.","ton-case-study.md Q6","regulations PDF (document URL to add) [VERIFY URL]","2026-11-18"),
 ("International and comparator","adgm-ton","ADGM Registration Authority, Public Register entry: TON DLT Foundation, Registration No. 19992 (registered Dec. 5, 2024)","https://newreg.adgm.com",
  "register entry","TON's ADGM DLT foundation, its registration and licence status.","ton-case-study.md","ADGM public register (search page)","2026-11-18"),
 ("TON case study: primary","tonx-10q","TON Strategy Co., Quarterly Reports (Form 10-Q) for Q1 (filed May 12, 2026, Accession No. 0001493152-26-022422), Q2 (filed Aug. 11, 2026, 0001493152-26-037002) and Q3 2026 (filed Nov. 13, 2026, 0001493152-26-051556)","https://www.sec.gov/edgar/search/",
  "business and subsequent-events sections","The Foundation \"supports, but does not control or govern\" TON; silence on Telegram's 4 May role; rename dated June 8.","ton-case-study.md Q7","SEC EDGAR filings","2026-11-18"),
 ("TON case study: primary","ton-vote","TON Vote, proposal page for the Gram rename (poll closed June 8, 2026)","https://ton.vote",
  "result panel; proposal text","For 81.22% of the voted balance; proposal describes a \"change in stewardship\".","ton-case-study.md Q5","ton.vote proposal page (exact URL in ton-case-study.md)","2026-11-18"),
]
PENDING = [
 "Brunson, Standing on the Shoulders of LLCs, 57 Ga. L. Rev. 603 (2023): article and pinpoints to read",
 "Sarcuni v. bZx DAO, 664 F. Supp. 3d 1100 (S.D. Cal. 2023): pinpoint",
 "CFTC v. Ooki DAO, No. 3:22-cv-05416-WHO (N.D. Cal. June 8, 2023): docket",
 "Samuels v. Lido DAO, 757 F. Supp. 3d 951 (N.D. Cal. 2024), and 9th Cir. No. 25-5701: reporter cite, appeal status",
 "Houghton v. Leshner, 9th Cir. No. 24-7243 (Oct. 21, 2025): opinion and district-court status",
 "CLARITY Act, H.R. 3633, 119th Cong.: current status on congress.gov",
 "Zurich Foundation Law Day materials (Univ. of Zurich, 2023): debate on pre-2024 deeds",
 "Telegram, TON/Gram notice (2020) and ton.foundation self-description (accessed 2026-11-15): page text to archive",
 "Cayman foundation companies (ENS, Fluid): not yet sourced",
 "ZGB Arts. 52, 85, 86, 86b, 87: cited in research files, pinpoints not yet checked on Fedlex",
]
def slug(s): return re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-")
bib=["# Bibliography","","PUBLIC. Running source list (PROCESS.md, Phase 3). An entry is listed here only after its citation and the provision or passage relied on were checked against the source (status P in the source maps). A [VERIFY] mark means the claim was checked but one item is outstanding (an official-site check, a URL or a date); the source note says which. Each entry has a source note in `source-notes/` (L-numbered). Foundation-specific sources (deeds, register entries, foundation pages) are listed in the per-foundation source notes (numbered by snapshot rank), not repeated here.","","Citation form follows Bluebook style for US sources and Swiss conventions for Swiss sources; final Bluebook check happens at drafting.",""]
sec=None
for n,(section,sid,cit,url,pin,claim,used,chk,date) in enumerate(ENTRIES,1):
    if section!=sec:
        bib+=["",f"## {section}",""]; sec=section
    fn=f"L{n:02d}-{sid}.md"
    flag=" [VERIFY]" if "VERIFY" in (pin+chk) else ""
    bib.append(f"- {cit}. <{url}>. Source note: [`{fn}`](source-notes/{fn}).{flag}")
    note=[f"# Source note L{n:02d}: {sid}","",f"- **Source:** {cit}. <{url}>",f"- **Pinpoint cite:** {pin}",f"- **Claim it supports:** {claim}",f"- **Used in:** {used}","- **Summarized by:** AI (Claude Opus 5.5); entry built at Medium effort, research at High effort",f"- **Verified against original:** Y, {chk}, {date}" if "VERIFY" not in chk else f"- **Verified against original:** Partial, {chk}, {date}",""]
    (OUT/"source-notes"/fn).write_text("\n".join(note),encoding="utf-8")
bib+=["","## Pending (not yet entered)","","These were seen only second-hand or need a pinpoint. They enter after checking.",""]+[f"- {p}" for p in PENDING]+[""]
(OUT/"bibliography.md").write_text("\n".join(bib),encoding="utf-8")
print(len(ENTRIES),"entries")
