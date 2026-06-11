# SOP Quality Audit

Date: 2026-06-09

Scope:

- `REDDIT_DISTRIBUTION_SOP.md`
- `AUTO_HELP_POLICY.md`
- `FREE_RESOURCE_INDEX.md`
- `REPLY_DRAFTS.md`
- `ANSWER_LOG.md`
- `DEEPSEEK_REPLY_REVIEW.md`
- `README.md`
- `reddit-answer-first-operator` skill

## Scorecard

| Dimension | Score | Notes |
| --- | ---: | --- |
| Safety / moderation risk control | 9.8 | Public auto-posting is prohibited; banned communities are do-not-touch; moderator warnings stop the path. |
| Unattended automation suitability | 9.6 | Automation can draft, log, and improve owned surfaces without public account actions. |
| Answer-first usefulness | 9.5 | Replies must stand without links; draft patterns cover the main recurring problem classes. |
| Resource-link discipline | 9.7 | One free GitHub link maximum; link only on direct match; no paid/Gumroad/coupon language in public replies. |
| Operational clarity | 9.6 | Tiers, logs, templates, allowed/not-allowed actions, candidate scoring, and output contracts are explicit. |
| Measurement / learning loop | 9.6 | `ANSWER_LOG.md` includes candidate fields, examples, weekly review questions, and a weekly summary template. |
| Maintainability | 9.5 | Old sales strategy is archived; current files are named and linked; skill captures the operating mode. |
| Owned-surface improvement path | 9.6 | Unsafe public reply becomes FAQ/README/resource improvement instead of account action. |
| External draft review | 9.6 | DeepSeek strict review checks usefulness first, then promotion/moderation risk before notification. |

Overall: **9.61 / 10**

## Key Findings

1. The system is now safe for unattended operation only because public account
   actions are disabled.
2. The biggest remaining risk is not policy text; it is future drift if an
   automation or human reintroduces public posting, Gumroad links, or `r/gamedev`
   interaction without explicit review.
3. The system should not optimize for revenue signals in Reddit participation.
   Downloads and follow-up questions are acceptable secondary signals.
4. The skill wrapper reduces drift by making the same rules available outside
   this repository context.

## Required Gates Before Any Public Reply

All must pass:

- Community is not banned or moderator-sensitive.
- Current community rules allow helpful replies and relevant free resources.
- Reply answers the question without needing a link.
- At most one free GitHub link is included.
- No paid/Gumroad/coupon/upgrade language appears.
- Risk is Low.
- DeepSeek strict review passes when available.
- User explicitly approves posting, unless a future policy changes this rule.

## Required Gates Before Any New Resource Post

All must pass:

- User explicitly approves the post.
- Target community rules are freshly reviewed.
- Direct landing page is free-only.
- No paid/Gumroad/coupon/upgrade language appears on the landing page.
- Resource has a clear quality/audit status.
- Post is benchmarked against recent successful posts in that community.

## Unattended Mode Rule

If the user cannot manually review, the system must not publish public replies.

Allowed unattended work:

- candidate discovery
- risk scoring
- reply drafting
- `ANSWER_LOG.md` updates
- README/FAQ/resource improvements
- free-only scans
- low-risk documentation commits
- DeepSeek strict draft review when `DEEPSEEK_API_KEY` is available

## Next Improvements

- Add real entries to `ANSWER_LOG.md` for 7-14 days.
- Add FAQ sections to resources when repeated questions appear.
- Re-score this audit after the first week of logged candidates.
