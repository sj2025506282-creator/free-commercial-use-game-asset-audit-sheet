# SOP Quality Audit

Date: 2026-07-13

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
| Safety / moderation risk control | 9.8 | Public submissions are prohibited; comments require all strict publish gates; banned communities are do-not-touch; moderator warnings stop the path. |
| Unattended automation suitability | 9.8 | Daily patrol now has an explicit no-quota posture: default no-link, publish at most the strongest candidate, and use Skip/Draft only for marginal cases. |
| Answer-first usefulness | 9.7 | Recent real wins continue to come from answer-only technical help; the SOP now makes no-link replies the default safe outcome. |
| Resource-link discipline | 9.8 | One free GitHub link maximum; link only after the new escalation gate passes; no paid/Gumroad/coupon language in public replies. |
| Operational clarity | 9.8 | Tiers, logs, templates, allowed/not-allowed actions, weekly-maintenance override, candidate scoring, output contracts, and daily comment caps are explicit. |
| Measurement / learning loop | 9.8 | Primary KPI is now correct skips, zero-risk published replies, and reusable owned-surface material rather than comment count or link placement. |
| Maintainability | 9.8 | Current free resources are indexed, the root README now exposes the lighter flat-tracker path, and the owned-surface docs better match the actual safe operating path. |
| Owned-surface improvement path | 9.6 | Unsafe public reply becomes FAQ/README/resource improvement instead of account action. |
| External draft review | 9.6 | DeepSeek strict review checks usefulness first, then promotion/moderation risk before notification. |

Overall: **9.79 / 10**

## Key Findings

1. The system is now safe for unattended operation only because public comments
   require strict publish gates and DeepSeek review before posting, and the
   weekly maintenance automation now has a stricter no-public-action override.
2. The biggest remaining risk is future drift if an automation or human
   reintroduces public posting, Gumroad links, or `r/gamedev` interaction
   without explicit review.
3. Recent log analysis shows the safest successful public replies are no-link
   technical answers. Resource links should be treated as an escalation path, not
   a default.
4. The system should not optimize for comment count, link placement, or revenue
   signals in Reddit participation. Correct skips and owned-surface learning are
   primary operating metrics.
5. The current free-resource entrance is clearer after adding the CC0 starter
   and exposing the flat-tracker path at the repo root, which reduces pressure
   to force mismatched links.
6. The skill wrapper reduces drift by making the same rules available outside
   this repository context.

## 2026-06-29 Weekly Recheck

- 2026-06-23 through 2026-06-29 `ANSWER_LOG.md` entries stayed no-link by default: 32 candidates, 6 answer-only posts, 0 answer-plus-link posts, 17 skips, and 9 draft-only records.
- The two high-risk license/IP boundary questions were skipped, preserving the no-legal-conclusion rule.
- Free landing pages and current free package README files did not contain paid/Gumroad/coupon/discount/upgrade leakage.
- `FREE_RESOURCE_INDEX.md` still covers the current free resources; the paid `starter-audit-template-pack-v0.2` remains outside free-resource routing.
- Current score remains **9.79 / 10** with no dimension below 9.5.

## 2026-07-13 Weekly Recheck

- 2026-07-07 through 2026-07-13 `ANSWER_LOG.md` entries stayed no-link by default: 50 candidates, 7 answer-only posts, 0 answer-plus-link posts, 21 skips, and 22 draft-only records.
- Risk mix was 47 low, 3 medium, and 0 high; medium-risk items stayed draft-only because they depended on current tooling, product cost, plugin compatibility, or third-party routing.
- Free landing pages and current free package README files did not contain paid/Gumroad/coupon/discount/upgrade leakage.
- `FREE_RESOURCE_INDEX.md` still covers the current free resources; the paid `starter-audit-template-pack-v0.2` remains outside free-resource routing.
- Added a no-link `REPLY_DRAFTS.md` pattern for Godot transparent shader self-overlap because shader/visual troubleshooting repeated across the week.
- The July 13 Unity material/export answer is covered by the existing no-link
  `Unity Mod Export Materials Missing In Game` pattern, so no new FAQ or resource
  index entry is justified.
- Current score remains **9.79 / 10** with no dimension below 9.5.

## Required Gates Before Any Public Reply

All must pass:

- Community is not banned or moderator-sensitive.
- Current community rules allow helpful replies and relevant free resources.
- Reply answers the question without needing a link.
- At most one free GitHub link is included, and only after the link escalation
  gate in `AUTO_HELP_POLICY.md` passes.
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
- During weekly maintenance, synthesize repeated no-link answers into
  `REPLY_DRAFTS.md` or README FAQ before seeking more public reply volume.
- Re-check public metrics with authenticated GitHub/Gumroad paths only if
  unattended reporting needs stronger secondary numerics.
