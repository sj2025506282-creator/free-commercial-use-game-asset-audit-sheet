# SOP Quality Audit

Date: 2026-08-02

Scope:

- `REDDIT_DISTRIBUTION_SOP.md`
- `AUTO_HELP_POLICY.md`
- `FREE_RESOURCE_INDEX.md`
- `REPLY_DRAFTS.md`
- `ANSWER_LOG.md`
- `DEEPSEEK_REPLY_REVIEW.md`
- `README.md`
- `reddit-answer-first-operator` skill
- `reddit-answer-first-reviewer` skill

## Scorecard

| Dimension | Score | Notes |
| --- | ---: | --- |
| Safety / moderation risk control | 9.8 | Public submissions are prohibited; comments require all strict publish gates; banned communities are do-not-touch; moderator warnings stop the path. |
| Unattended automation suitability | 9.8 | Daily patrol now has an explicit no-quota posture: default no-link, publish at most the strongest candidate, and use Skip/Draft only for marginal cases. |
| Answer-first usefulness | 9.7 | Recent real wins continue to come from answer-only technical help; the SOP now makes no-link replies the default safe outcome. |
| Resource-link discipline | 9.8 | One free GitHub link maximum; link only after the new escalation gate passes; no paid/Gumroad/coupon language in public replies. |
| Operational clarity | 9.8 | Tiers, logs, templates, allowed/not-allowed actions, weekly-maintenance override, candidate scoring, output contracts, and daily comment caps are explicit. |
| Measurement / learning loop | 9.9 | Process and outcome evidence are now separated; posted comments get a 48-72 hour readback and unavailable metrics are recorded as unknown. |
| Maintainability | 9.9 | Daily execution and periodic SOP review now have separate skills, while the safety-critical discover-to-publish transaction remains atomic. |
| Owned-surface improvement path | 9.6 | Unsafe public reply becomes FAQ/README/resource improvement instead of account action. |
| External draft review | 9.6 | DeepSeek strict review checks usefulness first, then promotion/moderation risk before notification. |

Overall: **9.77 / 10**

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
7. The daily operator should not also own policy redesign. A separate read-only
   reviewer can improve logs, templates, and compatible tooling without
   carrying public-action permission.
8. Historical `Relevance` scoring was too narrow for the actual adjacent
   technical-help lane. The prospective `Thread fit` rubric preserves strategic
   priority while distinguishing concrete adjacent questions from weak-context
   or off-scope threads.

## 2026-07-25 Architecture Recheck

- Kept discovery, drafting, external review, publishing, permalink recovery,
  and logging inside one daily operator skill because these stages share
  safety-critical state.
- Added `reddit-answer-first-reviewer` as a public-read-only weekly and
  on-demand retrospective skill.
- Added 48-72 hour comment outcome readback so a successful API submission and
  a DeepSeek pass are not mistaken for demonstrated usefulness.
- Added SOP change classes: low-risk clarification and owned-surface changes may
  be applied automatically; publish thresholds, community bans, link limits,
  banned language, and daily volume require explicit user approval to relax.
- Replaced prospective `Relevance` scoring with a defined `Thread fit` rubric;
  historical rows remain unchanged.
- Corrected `DEEPSEEK_REPLY_REVIEW.md` to match the current unattended strict
  auto-publish policy.
- Current score is **9.77 / 10** with no dimension below 9.5. This corrects
  the previously rounded total without changing any dimension score.

## 2026-07-31 Outcome And Drift Recheck

- Read back the five mature published comments from 2026-07-24 through
  2026-07-28. All five remained present with no comment removal or lock signal;
  each had visible score 1 and no direct reply. The Mixamo parent post was
  deleted, but the comment itself remained available.
- This is positive moderation-safety evidence but weak user-adoption evidence.
  A score of 1 or no reply is not treated as proof of failure; the repeated
  pattern is enough to test answer compression and overlap control.
- Added an authority ladder so automations schedule work, skills orchestrate it,
  and `AUTO_HELP_POLICY.md` remains the unattended threshold source of truth.
- Added strict checks for a concrete gap beyond existing replies, an immediate
  direct answer and first action, DeepSeek brevity >= 7, and redundancy risk
  <= 3.
- Extended DeepSeek input with an `existing_replies` summary so high standalone
  usefulness scores cannot hide duplication with the live thread.
- Added deterministic DeepSeek output validation and normalization for required
  scores and enum values before an automated gate can consume the result.
- Added a deterministic prepublish gate for daily cap, candidate scores,
  community stops, banned language, link restrictions, DeepSeek thresholds,
  and exact reviewed-draft SHA-256. Five focused regression tests cover the
  passing path and major block paths.
- Kept the two-skill architecture. More execution skills would fragment the
  safety-critical daily transaction; deterministic checks and evidence review
  are the appropriate next layer.
- Current score remains **9.77 / 10** with no dimension below 9.5. The new gates
  are stricter and do not expand public permissions.

## 2026-08-02 Seven-Patrol Evidence Review

- Reviewed the seven most recent completed patrol days: 2026-07-26 through
  2026-07-30, plus 2026-08-01 and 2026-08-02. No patrol record exists for
  2026-07-31 because that run was used for SOP review and hardening.
- Logged 46 candidates: 7 `Answer only`, 24 `Skip`, 15 `Draft only`, and zero
  linked replies. Risk mix was 38 Low, 8 Medium, and 0 High; every Medium item
  remained `Draft only`.
- All seven published comments were no-link. The five mature comments from
  2026-07-26 through 2026-07-30 remain present, unlocked, and unremoved, with
  visible score 1 and no direct reply. The 2026-08-01 and 2026-08-02 comments
  are under 48 hours old, so outcome evidence remains `Unknown`.
- Process safety is strong: no submissions, DMs, votes, paid language, Gumroad
  links, `r/gamedev` interaction, moderation warnings, or removals occurred.
- Skip quality is strong. Most skips had a complete existing answer; most
  draft-only records lacked code, version details, reproducible setup, or
  trustworthy current platform definitions.
- DeepSeek scores remain weak outcome predictors: mature comments scored highly
  in review but received no visible adoption signal. Do not lower thresholds or
  increase volume; finish the five-comment brevity/overlap experiment first.
- Candidate mix drifted toward adjacent engine support. All seven published
  comments had `Thread fit = 1`; only five candidates in the window had direct
  strategic fit, and none justified a public reply after duplication/risk
  checks. Discovery should deliberately search direct-fit lanes, without making
  them a posting quota.
- The 2026-08-01 MarginContainer candidate exposed a real review-to-publish
  race: a new answer appeared after DeepSeek review. Human re-read prevented a
  duplicate, but the deterministic gate could still pass a stale semantic
  assertion. DeepSeek now binds `existing_reply_ids`, and the prepublish gate
  requires exact equality with final `live_reply_ids`.
- `REPLY_DRAFTS.md` now contains 43 patterns and 2,036 lines. Do not add another
  pattern until repeated use is evidenced; the next reviewer should add reuse
  and last-used tracking before further template growth.
- Current score remains **9.77 / 10** with no dimension below 9.5. The live
  reply-ID binding strengthens unattended safety without expanding permissions.

## 2026-06-29 Weekly Recheck

- 2026-06-23 through 2026-06-29 `ANSWER_LOG.md` entries stayed no-link by default: 32 candidates, 6 answer-only posts, 0 answer-plus-link posts, 17 skips, and 9 draft-only records.
- The two high-risk license/IP boundary questions were skipped, preserving the no-legal-conclusion rule.
- Free landing pages and current free package README files did not contain paid/Gumroad/coupon/discount/upgrade leakage.
- `FREE_RESOURCE_INDEX.md` still covers the current free resources; the paid `starter-audit-template-pack-v0.2` remains outside free-resource routing.
- Current score remains **9.77 / 10** with no dimension below 9.5.

## 2026-07-13 Weekly Recheck

- 2026-07-07 through 2026-07-13 `ANSWER_LOG.md` entries stayed no-link by default: 50 candidates, 7 answer-only posts, 0 answer-plus-link posts, 21 skips, and 22 draft-only records.
- Risk mix was 47 low, 3 medium, and 0 high; medium-risk items stayed draft-only because they depended on current tooling, product cost, plugin compatibility, or third-party routing.
- Free landing pages and current free package README files did not contain paid/Gumroad/coupon/discount/upgrade leakage.
- `FREE_RESOURCE_INDEX.md` still covers the current free resources; the paid `starter-audit-template-pack-v0.2` remains outside free-resource routing.
- Added a no-link `REPLY_DRAFTS.md` pattern for Godot transparent shader self-overlap because shader/visual troubleshooting repeated across the week.
- The July 13 Unity material/export answer is covered by the existing no-link
  `Unity Mod Export Materials Missing In Game` pattern, so no new FAQ or resource
  index entry is justified.
- Current score remains **9.77 / 10** with no dimension below 9.5.

## 2026-07-20 Weekly Recheck

- Late 2026-07-20 and 2026-07-21 `ANSWER_LOG.md` entries were folded into the weekly review on 2026-07-21: 14 candidates, 2 answer-only posts, 0 answer-plus-link posts, 7 skips, and 5 draft-only records.
- Risk mix was 14 low, 0 medium, and 0 high; both posted replies were no-link ordinary technical-help answers.
- Free landing pages and current free package README files remain clear of paid/Gumroad/coupon/discount/upgrade leakage.
- `FREE_RESOURCE_INDEX.md` still covers all seven current free resource paths; the paid `starter-audit-template-pack-v0.2` remains outside free-resource routing.
- Read-only GitHub metrics were stable except for one additional UI SFX ZIP download; authenticated read-only Gumroad CLI still showed 0 sales and 0 `REDDIT40` uses; unauthenticated Reddit JSON checks remained limited by HTTP 403.
- The latest Unity additive-scene streaming answer was captured in `REPLY_DRAFTS.md` as a no-link reusable pattern, so no free-resource index expansion is justified.
- Current score remains **9.77 / 10** with no dimension below 9.5.

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

- Run the reviewer against the next completed seven-day window and update the
  48-72 hour outcomes for posted comments.
- Compare the next five mature comments against the 2026-07-24 through
  2026-07-28 baseline for opening clarity, answer length, direct replies, and
  overlap with existing answers.
- Require exact reviewed-versus-live reply-ID equality and re-review whenever
  the visible thread changes.
- Track template reuse and last-used date before adding more reply patterns;
  archive or consolidate patterns that remain unused across four review windows.
- Include direct-fit asset provenance, font, jam shipping, UI SFX, and
  open-source-tooling searches in discovery, but never treat them as a posting
  quota.
- Add package-level FAQ only when a repeated question maps cleanly to one owned resource.
- During weekly maintenance, synthesize repeated no-link answers into
  `REPLY_DRAFTS.md` or README FAQ before seeking more public reply volume.
- Reassess the scoring rubric after at least 20 new candidates; do not tune it
  from one patrol.
