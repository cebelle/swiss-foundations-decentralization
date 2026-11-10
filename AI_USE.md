## Transparency and disclosure

There's no gold standard for open-process *doctrinal or policy* legal writing yet, which is part of what makes this project interesting. You can borrow from two adjacent places.

**Open science (pre-registration, shared materials).** A study of 300 empirical articles in top law journals found only 3% stated a pre-registration and 6% shared analytic scripts ([Schiavone et al., F1000Research 2024](https://f1000research.com/articles/12-144/v2)). Pre-registering a policy paper's plan is close to unprecedented in law, so doing it well is a contribution in itself. Borrow the mechanics: a time-stamped plan, versioned materials, a deviation log.

**Law review AI-disclosure policies.** These tell you what reviewers will expect at submission:

- [Stanford Law Review (Vol. 79)](https://www.stanfordlawreview.org/wp-content/uploads/sites/3/2026/01/Vol.-79-SLR-AI-Policy.pdf) requires disclosure of AI use that significantly affected substance, originality, or reliability, and an author footnote at publication; hallucinated sources can be grounds for rescission.
- [NYU Law Review](https://nyulawreview.org/wp-content/uploads/2026/08/NYULR-AI-Author-Policy.pdf) uses a presumption of disclosure and a [template form](https://docs.google.com/document/d/16OqyxASeCCV35dBi_OGNGjeSKmLUkslo/export?format=pdf) asking separately about writing, research, and data analysis.
- [Gutowski (Jacksonville U. L. Rev.)](https://taxprofblog.aals.org/2025/07/25/trends-policies-and-considerations-of-artificial-intelligence-use-in-law-review-authorship/) argues for normalizing disclosed AI use rather than stigmatizing it, which is the stance your repo models.

Use NYU's three categories (writing, research, analysis) as the structure of your AI-use log. Your disclosure footnote then writes itself.



| Public repo                                 | Private (separate private repo or folder)                    |
| ------------------------------------------- | ------------------------------------------------------------ |
| Research plan, AI-use policy, deviation log | Raw Claude chat exports                                      |
| Problem statement, audience memo            | Candid notes on specific people, foundations, or council members |
| Bibliography and source notes               | Copyrighted PDFs (link instead)                              |
| Session logs (cleaned)                      | Drafts shared with reviewers before release                  |
| Checkpoint snapshots of outline and drafts  | Anything under NDA or from a confidential conversation       |
| AI-use log and final disclosure             | Venue submission correspondence                              |
## Model and effort policy

Adopted 2026-11-09 (see `DEVIATIONS.md`). Two Anthropic models are used: **Claude Opus 5.5** and **Claude Fable 5.2**. Effort labels below map to the nearest setting the app offers.

**Rule:** move up a model or an effort level when the output will be **locked** (pre-registered or tagged), **carries a legal claim**, or **becomes argument**. Mechanical, checkable work stays on Opus.

| Phase | Task | Model | Effort |
| --- | --- | --- | --- |
| 3 Research | Tier 2 codebook (pre-registered; locks coding) | Opus | High |
| | Tier 1 list (apply exclusions to the snapshot) | Opus | Medium |
| | Coding each Tier 2 foundation | Opus | Medium |
| | Ambiguous coding calls (e.g., Art. 86a ZGB reservations, unclear supervisor) | Fable | High |
| | US-law source map | Opus | High |
| | Swiss-law open questions (token-holder binding role, supervisor's final word) | Fable | High |
| 4 Argument | Thesis, outline, counterarguments, recommendations | Fable | Max |
| 5 Drafting | All section drafts (one model throughout, for a consistent voice) | Fable | High |
| | Line edits, cite-checks, Bluebook | Opus | Medium |
| 6 Review | Independent review, run in a fresh chat with only this repo | Fable | Max |
| Any | Session logs, deviation entries, commits | Opus | Low |

## AI-use log format

The AI-use log lives in each session log under `sessions/`. From 2026-11-09, every entry records the model and effort used:

`date · category (writing / research / analysis) · model, effort · task · output file · author review`

Example:

`2026-11-10 · research · Opus 5.5, high · drafted Tier 2 codebook · 02-research/codebook.md · author revised field definitions`

Each session log also opens with a line listing the models used. Entries in `sessions/2026-10-29.md` and `sessions/2026-10-30.md` predate this policy. The author confirmed on 2026-11-09 that both sessions used Opus 5.5, high (recorded in `sessions/2026-11-09.md`). The final disclosure footnote names every model used.
