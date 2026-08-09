# SOP Experiments

Use this file to improve the answer-first SOP from evidence without reacting to
single comments or weakening safety gates.

## Experiment Rules

- Safety and transaction-integrity defects may be fixed immediately.
- Content-quality hypotheses require at least five mature published comments.
- Candidate-selection or scoring hypotheses require at least 20 candidates or
  two completed review windows, whichever is larger.
- Change one content variable at a time. Record other changes as confounders.
- Treat outcomes under 48 hours or unavailable data as `Unknown`, not zero.
- Outcome priority is moderation safety, OP reply/follow-up, useful adoption
  evidence, direct replies, then visible score. Revenue and link placement are
  not Reddit-help outcomes.
- Never lower thresholds, increase public volume, reopen a stopped community,
  or expand public actions from an experiment without explicit user approval.

Statuses: `Queued`, `Active`, `Collecting`, `Decided`, `Rejected`.

## EXP-2026-08-01: Shorter Answer-First Replies

- Status: Collecting
- Hypothesis: A direct opening plus only the necessary diagnostic steps will
  improve OP replies or follow-up without reducing technical usefulness.
- Baseline: five mature comments from 2026-07-24 through 2026-07-28 averaged
  237.4 words; all had visible score 1 and no direct reply.
- Intervention: keep the direct answer and first action in the opening; target
  roughly 90-160 words when the problem permits; keep DeepSeek usefulness >= 8,
  brevity >= 7, and redundancy risk <= 3.
- Current sample: 5 of 5 comments, averaging 129.4 words. The 2026-08-01,
  2026-08-02, 2026-08-03, and 2026-08-06 comments are mature; all four remain
  present with visible score 1 and no direct reply. The 2026-08-09 outcome is
  `Unknown` until its 48-72 hour readback.
- Primary measure: OP reply, OP follow-up question, or evidence of adoption.
- Guardrails: no moderation event, no loss of concrete correctness, no increase
  in links or daily volume.
- Decision rule: decide only after five mature intervention comments. Compare
  adoption signals and visible-score distribution with the five-comment
  baseline; preserve `Unknown` values.
- Next decision point: read back the 2026-08-09 comment after 48-72 hours. Do
  not decide the experiment from the four mature samples or the submission
  event alone.
- Confounders: topic, subreddit, posting time, and whether another complete
  answer was already present.

## EXP-2026-08-02: Direct-Fit Discovery Mix

- Status: Decided
- Hypothesis: Explicit searches in asset provenance, font provenance, jam
  shipping, UI SFX, and open-source tooling will increase direct-fit candidates
  without forcing links or unsafe replies.
- Baseline: 5 of 46 candidates in the latest seven-patrol window had
  `Thread fit = 2`; none justified publication after duplication and risk
  checks. All seven published replies had `Thread fit = 1`.
- Intervention: include direct-fit searches in each patrol while retaining the
  same candidate, risk, duplication, DeepSeek, and publish gates.
- Primary measure: direct-fit candidate count and quality.
- Guardrails: no posting quota, no forced link, no reduction in correct skips.
- Decision rule: review after two completed weekly windows and at least 20 new
  candidates.
- Decision: On 2026-08-09, the user broadened the account goal from narrow
  resource-fit discovery to ordinary-user usefulness. Keep these lanes as a
  subset, but do not optimize `Thread fit` around them alone. This is a strategy
  change, not evidence that the original hypothesis failed.

## EXP-2026-08-09: Ordinary-User Utility

- Status: Active
- Hypothesis: Prioritizing common beginner and solo-developer jobs, then giving
  one executable first action plus a success check, will create more visible
  adoption than technically correct niche answers alone.
- Baseline: The 2026-08-03 through 2026-08-09 window had 35 candidates, 3
  published answers, only 2 direct-fit candidates, and no visible direct reply
  on the mature published comments.
- Intervention: Include searches for importing/using assets, UI/input basics,
  save/export problems, performance triage, jam shipping, and source selection.
  Prefer questions that can be advanced in two to five plain-language steps.
  Draft with a direct answer, a first action, and a success check or next piece
  of evidence to collect.
- Primary measure: OP reply, follow-up question, or explicit evidence that the
  suggested step changed the result.
- Secondary measure: visible score distribution after 48-72 hours.
- Guardrails: preserve all current risk, duplication, DeepSeek, link, community,
  exact-body, and one-comment gates. Do not simplify away technical accuracy.
- Decision rule: review after at least 20 candidates and five mature published
  comments. Do not infer ordinary-user value from readability scores alone.
- Confounders: subreddit, posting time, question age, existing reply quality,
  topic complexity, and whether the OP returns to the thread.

## Maintenance Backlog

- Add reuse count and last-used date for reply patterns before adding more.
- Consolidate or archive patterns unused across four completed review windows.
- Keep raw historical log rows; make prospective changes only.
