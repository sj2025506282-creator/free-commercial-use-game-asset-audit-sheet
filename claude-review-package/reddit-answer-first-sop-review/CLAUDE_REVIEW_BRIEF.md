# Claude Review Brief: Answer-First Reddit/Forum Help SOP

## Context

This project started as a Reddit/GitHub/Gumroad distribution experiment for free game-asset license workflow resources.

The strategy changed after a moderation issue on `r/gamedev`. The current goal is no longer to drive a Reddit sales funnel. The current goal is:

1. Help real developers with concrete answers.
2. Keep public community behavior low-risk and non-promotional.
3. Use free GitHub resources only when directly relevant.
4. In unattended mode, never publish public comments or posts automatically.
5. Improve owned resources such as README, FAQ, templates, and resource indexes based on repeated questions.

## Current Operating Model

### Public Interaction Rule

No automatic public interaction.

The system may:

- find candidate questions
- score risk and relevance
- draft answer-first replies
- append records to `ANSWER_LOG.md`
- improve owned surfaces such as README, FAQ, resource docs, `FREE_RESOURCE_INDEX.md`, and `REPLY_DRAFTS.md`
- commit low-risk documentation changes

The system may not:

- post Reddit comments
- post Reddit submissions
- send direct messages
- vote
- appeal moderation
- use alternate accounts
- post paid CTAs
- link Gumroad in subreddit replies

### Reply Pattern

Replies must:

1. Answer the question directly.
2. Give concrete steps that work without downloading anything.
3. Include at most one free GitHub link only if directly relevant.
4. Avoid paid products, Gumroad, coupons, discounts, Pro/upgrade language, and repeated copy-paste wording.

### Candidate Scoring

Each candidate is scored 0-2 on:

- Relevance
- Helpfulness
- Risk
- Link fit
- Originality

Notify only when total score is 8+ and Risk is 2.

Otherwise, log quietly or improve owned resources.

## Current Files

- `REDDIT_DISTRIBUTION_SOP.md`: main operating SOP.
- `AUTO_HELP_POLICY.md`: unattended automation rules.
- `FREE_RESOURCE_INDEX.md`: maps question types to safe free GitHub resources.
- `REPLY_DRAFTS.md`: reusable answer patterns.
- `ANSWER_LOG.md`: candidate/reply tracking template.
- `SOP_QUALITY_AUDIT.md`: internal scorecard and gates.
- `reddit-answer-first-operator-SKILL.md`: Codex skill wrapper for repeatable execution.
- `README.md`: public repo entry point and free-resource selector.

## Quality Audit Result

Current internal score: `9.61 / 10`.

Dimensions:

- Safety / moderation risk control: 9.8
- Unattended automation suitability: 9.6
- Answer-first usefulness: 9.5
- Resource-link discipline: 9.7
- Operational clarity: 9.6
- Measurement / learning loop: 9.6
- Maintainability: 9.5
- Owned-surface improvement path: 9.6

## Key Design Decision

Because the user cannot manually review daily replies, the system must not auto-post public replies. The safe substitute is:

- draft replies
- log candidates
- improve owned resources
- notify only when high-quality, low-risk opportunities exist

## Questions For Claude

Please review the package and answer:

1. Are there any remaining moderation, spam, or self-promotion risks?
2. Is the unattended-mode boundary strict enough?
3. Are the scoring and notification thresholds appropriate?
4. Are there any loopholes where automation might still create public-account risk?
5. Is the reply template too promotional, or does it read like genuine help?
6. Should any additional categories be added to `FREE_RESOURCE_INDEX.md` or `REPLY_DRAFTS.md`?
7. Are any files redundant or confusing?
8. What would you change to make this system safer and more useful?

## Desired Review Style

Please be strict. Prioritize:

- account safety
- moderation compliance
- usefulness to real developers
- avoiding promotional behavior
- clarity for unattended automation

If you think any score is too high, explain which dimension should be reduced and why.
