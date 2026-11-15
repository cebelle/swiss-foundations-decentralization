# Tier 2 codebook (pre-registered)

**Label:** PUBLIC · **Status:** v1, pre-registered (approved by the author 2026-11-14) · **Date:** 2026-11-14 · **Rule:** `02-research/sampling-rule.md` · **Pool:** `02-research/tier1-list.md`

The author decided the fields, the two-layer design, the split of the appointment field, and the review standard on 2026-11-14. Claude (Opus 5.5, high effort), a disclosed AI tool, drafted the definitions and the protocol. This codebook is committed before any Tier 2 foundation is coded. Any change after that commit is logged in `DEVIATIONS.md`.

## 1. What is coded

- **Unit:** one record per Swiss foundation that is the primary steward of a network in the Tier 2 pool. "Swiss foundation" and "primary steward" are defined in `sampling-rule.md`.
- **Other entities:** recorded under field 8. They are not coded as records of their own.
- **What this codebook does not do:** it does not score decentralization. It records structure. The anti-entrenchment analysis is argument, and belongs to Phase 4.

## 2. Two layers

Some fields are coded twice.

- **Law:** what the deed (*Stiftungsurkunde*) and the regulations (*Reglement*) provide.
- **Practice:** what the foundation publicly says it does: governance pages, annual reports, forum posts by the foundation, and blog posts by the foundation.

A gap between the layers is a finding, not an error. Each field below says which layers apply.

## 3. Sources

**Order of authority, within a layer:**

1. Zefix register extract
2. Deed
3. Regulations
4. Annual reports
5. Foundation governance pages
6. The project's own documents

Practice draws on sources 4 to 6. When two sources in the same layer conflict, the higher one controls and the record is flagged (section 6).

**Every value records:** source URL or document name, pinpoint (article, section or page), and access date. For deeds and regulations in German, French or Italian, also record the original term that decides the value (for example, *Kooptation*).

## 4. Codes for missing values

| Code | Meaning |
| --- | --- |
| `NOT_PUBLIC` | The document exists, or must exist under Swiss law, but is not publicly available. This is a finding. |
| `NOT_FOUND` | No source was found after the search steps in `sampling-rule.md`. |
| `NONE` | A source says there is none. |
| `N/A` | The field does not apply to this record. |

`NOT_PUBLIC` is never used to mean `NONE`. A foundation that publishes nothing about token holders is `NOT_FOUND` in practice, not `NONE`.

## 5. Fields

### Identifiers (no layers)

Network; snapshot rank; foundation name as registered; UID (CHE-xxx.xxx.xxx); seat; registration date; link to the register extract.

### F1. Council size

- **Layers:** law and practice.
- **Law:** the minimum and maximum number of council members the deed or regulations set, or `NONE` if no number is set.
- **Practice:** the number of members on the access date, from the register extract. If the foundation's own pages give a different number, record both and flag.

### F2. Council control

Field 2 has four parts. Together they measure whether the council can perpetuate itself.

**F2a. Appointment**

- **Layers:** law and practice.
- **Values:**
  - `FOUNDER`: the founder appoints.
  - `CO-OPTATION`: the council appoints its own members.
  - `OUTSIDE_BODY`: a named entity other than the founder appoints (record which one).
  - `TOKEN_HOLDERS`: token holders elect.
  - `MIXED`: more than one of the above (record the split).
- If the founder appoints only the first council and the council fills seats after that, code `CO-OPTATION` and note the founder's initial role.

**F2b. Removal**

- **Layers:** law and practice.
- **Values:** `FOUNDER`, `COUNCIL`, `OUTSIDE_BODY`, `TOKEN_HOLDERS`, `MIXED`, `SUPERVISOR_ONLY`.
- `SUPERVISOR_ONLY` means the documents give no one a power to remove members, so removal is left to the supervisory authority.

**F2c. Term limits**

- **Layers:** law and practice.
- **Law values:** term length in years, whether re-election is allowed, and any cap on terms. Use `NONE` if the documents set no term.
- **Practice:** the longest tenure among current members, from register entry dates.

**F2d. Self-perpetuating council (flag)**

- **Layer:** law.
- **Values:** `YES` / `NO`.
- `YES` when F2a (law) is `CO-OPTATION` and F2b (law) is `COUNCIL` or `SUPERVISOR_ONLY`. This is derived from F2a and F2b, not coded on its own judgment.

### F3. Founder's reservation (Art. 86a ZGB)

- **Layer:** law.
- **Legal anchor:** Art. 86a ZGB, as amended by the Federal Act of 17 December 2021 (in force 1 January 2024).
  - The competent federal or cantonal authority makes the change at the founder's request. The founder does not make it.
  - The deed must reserve the right. Ten years must have passed since the foundation was established or since the founder's last change. The two periods run separately.
  - If the founder is a legal entity, the right ends no later than 20 years after the foundation was established.
- **Values:**
  - `NONE`
  - `PURPOSE`
  - `ORGANISATION`
  - `BOTH`
  - `NOT_PUBLIC`
- **Also record:**
  - Founder type: natural person or legal entity. Name it if it is an entity.
  - Earliest date the reservation can be used.
  - Latest date, for a legal-entity founder.
- **Open legal point:** Art. 86a has no transitional provision. Commentators disagree on how a reservation in a pre-2024 deed reads for changes to the organization. Code the words of the deed. Flag every pre-2024 deed whose reservation refers to Art. 86a in general terms.

### F4. Token-holder role

- **Layers:** law and practice.
- **Values:**
  - `NONE`
  - `ADVISORY`: votes are collected but bind no one.
  - `BINDING_DEED`: the deed requires the council to follow a token-holder vote.
  - `BINDING_REGULATIONS`: the regulations require it.
  - `SELF_COMMITMENT`: the foundation says it will follow votes, but no deed or regulation requires it.
- `SELF_COMMITMENT` is a practice value only.
- Whether Swiss law allows a deed to bind the council to token-holder votes is an open question for Phase 3 Swiss-law research. This codebook records what the documents say. It does not decide whether that is valid.

### F5. Dissolution

- **Layer:** law.
- **Record:**
  - Triggers for dissolution named in the deed, or `NONE` if the deed names none and relies on the statute.
  - Who may start dissolution.
  - Where remaining assets go: a named entity, a purpose, the public authority, or `NONE`.
- **Legal anchor:** dissolution by the authority, Art. 88 ZGB; destination of assets, Art. 57 ZGB. [VERIFY pinpoints before citing.]

### F6. Supervisory authority

- **Layer:** law. Source: the register extract or the authority's published list.
- **Values:** `FEDERAL` (Eidgenössische Stiftungsaufsicht) / `CANTONAL` (record the canton and the authority's name) / `NOT_FOUND`.
- **Legal anchor:** Art. 84 ZGB. [VERIFY pinpoint before citing.]

### F7. Treasury disclosure

- **Layers:** law and practice.
- **Law:** any duty to publish set out in the deed or regulations, or `NONE`. Also record the auditor named in the register extract (Art. 83b ZGB), or the exemption if one is recorded.
- **Practice values:**
  - `NONE`
  - `HOLDINGS_ONLY`: wallet addresses or holdings figures.
  - `PERIODIC_REPORTS`: unaudited reports.
  - `AUDITED_PUBLISHED`: audited financial statements are public.
- Record the most recent period covered.

### F8. Related entities

- **Layers:** law and practice.
- **For each entity:**
  - Name.
  - Legal form.
  - Jurisdiction.
  - Relationship type: `IP_HOLDER`, `IP_LICENSEE`, `SERVICE_PROVIDER`, `FUNDED_BY_FOUNDATION`, `FUNDS_FOUNDATION`, `TOKEN_ISSUER`, `SHARED_PERSONNEL`, `FOUNDER`, or `OTHER` (described).
  - Source.
- Shared personnel means a person who sits on the council and is also an officer or director of the related entity, on the access date.

### F9. Registered purpose

- **Layer:** law.
- **Record:** the purpose text from the register extract, in the original language, plus a working English translation marked as Claude's.

## 6. Coding protocol

1. **First pass.** Claude codes every record (Opus 5.5, medium effort, per `AI_USE.md`).
2. **Flags.** Claude flags a value when any of these apply:
   - two sources in the same layer conflict;
   - the value turns on how a German, French or Italian legal term is read;
   - the wording of an Art. 86a reservation is unclear, or the deed is pre-2024 and refers to the organization (F3);
   - the supervisory authority cannot be determined from the register extract;
   - more than one entity could be the primary steward;
   - the value requires a legal judgment beyond the text.
3. **Flagged calls.** Flagged calls are recoded by Fable 5.2 at high effort, per `AI_USE.md`. The author then rules on each one. Each ruling is numbered and logged in `02-research/tier2-rulings.md`, in the same form as the rulings in `tier1-list.md`.
4. **Random check.** The author also reviews a random 20% of the records with no flags, rounded up.
   - The draw is made after the first pass is complete, with Python's `random.sample` and the seed `20261106`, over the record list sorted by snapshot rank.
   - The script and its output are committed.
   - If the author changes a value in the sample, the change and its reason are logged. If the author changes values in more than one in five sampled records, every record gets author review, and that is logged as a deviation.

## 7. Output

- **Data:** `02-research/data/tier2-coding.csv`, in long format, with one row per record, field and layer. Columns:

  `network, snapshot_rank, foundation, uid, field, layer, value, source, pinpoint, access_date, original_term, flag, flag_reason, ruling_ref, author_reviewed`

- **Source notes:** one file per foundation in `02-research/source-notes/`, using `_TEMPLATE.md`.
- **Documents:** register extracts and deeds that are public records are linked, not committed. Any document obtained by ordering it from a register is kept private until the author decides on publication.

## 8. Changes

This codebook locks when it is committed. After that, any change to a field, value, flag rule or the sampling of the review is logged in `DEVIATIONS.md`, in the format: date · what changed · why · checkpoint affected.

## Legal sources used in this codebook

- Art. 86a ZGB, text as amended by the Federal Act of 17 December 2021 (Strengthening Switzerland as a Foundation Location), AS 2022 452, in force 1 January 2024. Checked on 2026-11-14 against an unofficial English translation at lawbrary.ch. [VERIFY against the official Fedlex text before citing in the paper.]
- Absence of a transitional provision for Art. 86a, and the debate on pre-2024 deeds: Zurich Foundation Law Day materials (University of Zurich, 2023), accessed 2026-11-14. [VERIFY; add to the bibliography with a source note.]
- Art. 83b, 84, 88 and 57 ZGB: named as anchors only. [VERIFY pinpoints.]
