---
name: reddit-answer-first-operator
description: Use when operating, auditing, or improving the user's Reddit/forum answer-first help system for game-dev asset licensing resources. Applies to finding real questions, drafting safe replies, updating ANSWER_LOG.md, improving free GitHub resources, enforcing no-auto-public-posting, and avoiding paid/Gumroad/self-promotion risks.
metadata:
  short-description: Safe answer-first Reddit/forum help system
---

# Reddit Answer-First Operator

Use this skill for the user's game-dev asset-license community-help workflow.

## Project Root

Default repo:

`/Users/sunji/Documents/work/Project/reddit/asset-audit-sheet-v0.1`

Primary files:

- `REDDIT_DISTRIBUTION_SOP.md`
- `AUTO_HELP_POLICY.md`
- `FREE_RESOURCE_INDEX.md`
- `REPLY_DRAFTS.md`
- `ANSWER_LOG.md`
- `SOP_QUALITY_AUDIT.md`

## Non-Negotiables

- Do not post Reddit comments or submissions automatically.
- Do not DM, vote, appeal moderation, or use another account.
- Keep `r/gamedev` do-not-touch unless the user explicitly asks for a fresh rule review.
- Do not mention paid products, Gumroad, coupons, discounts, Pro, or upgrades in public replies.
- Link at most one free GitHub resource, only when it directly matches the question.
- If no human can review, draft/log/update owned surfaces only.

## Daily Workflow

1. Read `REDDIT_DISTRIBUTION_SOP.md`, `AUTO_HELP_POLICY.md`, `FREE_RESOURCE_INDEX.md`, and `REPLY_DRAFTS.md`.
2. Find candidate questions only in allowed/safe communities.
3. Reject candidates that are banned-community, moderator-sensitive, legal-conclusion requests, argument threads, or poor resource matches.
4. For good candidates, draft an answer that works without any link.
5. Add one free GitHub link only if it is a direct match.
6. Append to `ANSWER_LOG.md` with `Reply Posted` set to `No`.
7. Notify only when at least one candidate is Low risk and high match.

## Weekly Workflow

1. Review `ANSWER_LOG.md` for repeated questions and risks.
2. Improve owned surfaces: README, FAQ, release notes, resource docs, `FREE_RESOURCE_INDEX.md`, or `REPLY_DRAFTS.md`.
3. Run free-only scans on public landing pages.
4. Do not publish releases, paid products, Reddit posts, or Reddit comments.
5. Commit and push low-risk documentation changes when they pass `git diff --check`.

## Candidate Scoring

Score every candidate from 0-2 on each axis:

- Relevance: direct match to asset licensing/font provenance/jam shipping/UI SFX.
- Helpfulness: useful answer can stand without a link.
- Risk: no banned community, no legal conclusion, no argument thread.
- Link fit: at most one free GitHub resource is genuinely useful.
- Originality: reply is adapted, not copied.

Notify only when total score is 8+ and Risk is 2.

## Output Contract

For each candidate:

```text
Community:
Thread:
URL:
Decision: Answer only | Answer + free link | Skip | Draft only
Score: Relevance / Helpfulness / Risk / Link fit / Originality / Total
Risk: Low | Medium | High
Resource:
Reason:
Draft:
```

When modifying docs, include:

- files changed
- validation run
- commit hash if committed

For weekly summaries include: candidates logged, decision counts, risk counts,
most common topics, resources naturally matched, owned-surface improvements,
moderation issues, and next week focus.

## Quality Target

Target score: 9.5/10.

Minimum acceptable state:

- no automatic public account actions
- no paid/public CTA leakage
- deterministic logs
- clear resource matching
- owned-surface improvement path when public reply is unsafe
