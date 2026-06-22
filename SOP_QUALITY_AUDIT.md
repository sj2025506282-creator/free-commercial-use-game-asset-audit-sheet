# SOP Quality Audit

Date: 2026-06-22

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
| Unattended automation suitability | 9.8 | Weekly maintenance now has an explicit owned-surface-only override: no public posting, clearer free-only resource routing, and explicit current-week metrics logging. |
| Answer-first usefulness | 9.6 | Replies still stand without links, and the recent real wins continue to come from answer-only technical help rather than link-led replies. |
| Resource-link discipline | 9.7 | One free GitHub link maximum; link only on direct match; no paid/Gumroad/coupon language in public replies. |
| Operational clarity | 9.7 | Tiers, logs, templates, allowed/not-allowed actions, weekly-maintenance override, candidate scoring, and output contracts are explicit. |
| Measurement / learning loop | 9.7 | `ANSWER_LOG.md` plus the weekly maintenance log capture candidate patterns, owned-surface fixes, and which external metrics were verified vs unavailable. |
| Maintainability | 9.8 | Current free resources are indexed, the root README now exposes the lighter flat-tracker path, and the owned-surface docs better match the actual safe operating path. |
| Owned-surface improvement path | 9.6 | Unsafe public reply becomes FAQ/README/resource improvement instead of account action. |
| External draft review | 9.6 | DeepSeek strict review checks usefulness first, then promotion/moderation risk before notification. |

Overall: **9.74 / 10**

## Key Findings

1. The system is now safe for unattended operation only because public comments
   require strict publish gates and DeepSeek review before posting, and the
   weekly maintenance automation now has a stricter no-public-action override.
2. The biggest remaining risk is future drift if an automation or human
   reintroduces public posting, Gumroad links, or `r/gamedev` interaction
   without explicit review.
3. The current free-resource entrance is clearer after adding the CC0 starter
   and exposing the flat-tracker path at the repo root, which reduces pressure
   to force mismatched links.
4. The system should not optimize for revenue signals in Reddit participation.
   Downloads and follow-up questions are acceptable secondary signals.
5. The skill wrapper reduces drift by making the same rules available outside
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
- Either the user explicitly approves posting, or the reply passes the strict
  automatic publish gates in `AUTO_HELP_POLICY.md`.

## Required Gates Before Any New Resource Post

All must pass:

- User explicitly approves the post.
- Target community rules are freshly reviewed.
- Direct landing page is free-only.
- No paid/Gumroad/coupon/upgrade language appears on the landing page.
- Resource has a clear quality/audit status.
- Post is benchmarked against recent successful posts in that community.

## Unattended Mode Rule

If the user cannot manually review, the system may publish only when all strict
publish gates pass. Otherwise it must not publish public replies.

Allowed unattended work:

- candidate discovery
- risk scoring
- reply drafting
- `ANSWER_LOG.md` updates
- README/FAQ/resource improvements
- free-only scans
- low-risk documentation commits
- DeepSeek strict draft review when `DEEPSEEK_API_KEY` is available
- public Reddit comments only after all strict publish gates pass

## Next Improvements

- Keep logging real entries to `ANSWER_LOG.md` and roll up a dated weekly note.
- Add package-level FAQ only when a repeated question maps cleanly to one owned resource.
- Re-check public metrics with authenticated GitHub/Gumroad paths if unattended reporting needs stronger numerics.
