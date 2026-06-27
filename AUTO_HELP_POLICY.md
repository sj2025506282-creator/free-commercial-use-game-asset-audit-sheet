# Auto Help Policy

This project can run without daily human review only under the strict publish
gates below.

## Allowed Without Human Review

- Find candidate questions.
- Classify risk: Low, Medium, High.
- Draft answer-first replies.
- Append records to `ANSWER_LOG.md`.
- Improve owned resources such as README, FAQ, release notes, templates, and
  checklists.
- Update `FREE_RESOURCE_INDEX.md` and `REPLY_DRAFTS.md`.
- Commit and push low-risk documentation updates.
- Post a Reddit comment only when all strict publish gates pass.

## Default Daily Posture

Daily patrol has no posting quota. The default safe outcome is a no-link answer,
`Skip`, `Draft only`, or owned-surface improvement.

- Publish at most one strongest public comment per daily run unless the user
  explicitly asks to continue.
- Prefer no-link answers when the reply is already useful.
- Do not publish when the answer would be generic, the thread is already solved,
  the community rules are unclear, or the only reason to reply is placing a
  resource.
- Treat skipped high-signal questions as learning material for
  `REPLY_DRAFTS.md`, README FAQ, or `FREE_RESOURCE_INDEX.md`.

## Weekly Maintenance Override

For the recurring weekly resource-maintenance automation, do not publish any
Reddit comment or submission even if the strict publish gates would otherwise
pass.

In that mode, unattended work is limited to:

- reading and summarizing logs
- owned-surface documentation fixes
- free-only landing-page scans
- read-only GitHub / Gumroad / Reddit status checks
- weekly notes / metrics updates
- low-risk commits and pushes

## Not Allowed Without Human Review

- Posting Reddit submissions.
- Sending direct messages.
- Voting.
- Appealing moderation.
- Using any alternate account.
- Publishing paid CTAs in public communities.
- Linking Gumroad in subreddit replies.
- Posting Reddit comments that did not pass all strict publish gates.

## Strict Publish Gates

Publish a Reddit comment automatically only when all are true:

- Community is not banned, moderator-sensitive, or unclear.
- Current subreddit rules allow ordinary helpful replies.
- Candidate total score is 8+ and Risk score is 2.
- Draft is answer-first and useful without any link.
- The run has not already published a stronger candidate today, unless the user
  explicitly asked to continue.
- DeepSeek strict review passes after any needed revisions.
- Final usefulness score >= 8.
- Final subreddit tone score >= 7.
- Final promotion risk score <= 3.
- Final link dependency is `None` or `Minor`.
- No paid, Gumroad, coupon, discount, Pro, upgrade, or sales language.
- At most one free GitHub link is included, and only if the link escalation gate
  below passes and DeepSeek says keep.
- If DeepSeek says remove the link, publish the no-link version.

If any gate fails, do not publish. Revise and re-review, or mark the candidate
`Skip` / `Draft only`.

## Notification Threshold

Notify only when at least one candidate is:

- Low risk.
- A direct match for an existing free resource or answer template.
- Useful even without a link.
- Outside banned or moderator-sensitive communities.
- Passed by DeepSeek strict ordinary-user review, when DeepSeek is available.
- Published automatically under the strict publish gates, or needs a human
  decision because it is valuable but did not pass automatic publish gates.

Otherwise, append to `ANSWER_LOG.md` and stay quiet.

## Candidate Scoring

Score each candidate from 0-2:

- Relevance: matches asset licensing, font provenance, jam shipping, UI SFX, or related tooling.
- Helpfulness: the answer is useful without a link.
- Risk: outside banned/moderator-sensitive communities and not a legal conclusion request.
- Link fit: one free GitHub resource is genuinely useful, or no link is needed.
- Originality: the draft is adapted to the actual question.

Notify only when total score is 8+ and Risk is 2. Otherwise log quietly or
improve owned surfaces.

## Link Escalation Gate

Add a free GitHub link only when all are true:

- The original question directly asks about asset licensing, font provenance,
  jam shipping, UI/audio sourcing, or another workflow covered in
  `FREE_RESOURCE_INDEX.md`.
- The specific resource solves that workflow better than a plain-text answer
  alone.
- The answer remains useful if the link is removed.
- DeepSeek's final `link_decision` is `keep`.

If any condition fails, remove the link and use the no-link version.

## DeepSeek Strict Review Gate

Before notifying with a reply draft, run `scripts/deepseek_reply_review.py` when
`DEEPSEEK_API_KEY` is available.

DeepSeek reviews as a strict, nitpicky ordinary Reddit user with a
moderator-adjacent view.

Pass gates:

- usefulness score >= 8
- subreddit tone score >= 7
- promotion risk score <= 3
- link dependency is `None` or `Minor`
- recommendation is `Yes` or a clearly fixable `Revise`
- if `link_decision` is `remove`, remove the link before presenting the draft

If a draft does not pass, revise it and run DeepSeek review again. Use the
reviewer's concrete criticism as the edit brief:

- make the answer more specific to the original post
- remove or soften self-references
- remove the resource link when it is not essential
- add concrete steps, examples, or decision criteria
- keep banned paid/Gumroad/coupon/upgrade language out

Continue revising until the draft passes. If it passes all strict publish gates,
publish it and log the final posted version. If a useful, low-risk draft cannot
be made without becoming generic, promotional, legally conclusive, or off-topic,
mark the candidate `Skip` or `Draft only` and do not publish.

If DeepSeek is unavailable, apply the same rubric manually and mention that the
external review was not run.

## Output Contract

Every candidate record or notification should include:

- Community
- Thread/question
- URL
- Decision: `Answer only`, `Answer + free link`, `Skip`, or `Draft only`
- Score: Relevance / Helpfulness / Risk / Link fit / Originality / Total
- Risk: `Low`, `Medium`, or `High`
- Resource linked, or `None`
- Reason
- Draft, when useful
- DeepSeek review result, when run
- Reply Posted: `Yes` only after the public comment is actually posted

## Owned-Surface Help

If a repeated question is found but no safe public reply should be posted, help by
updating owned surfaces:

- Add a README FAQ.
- Improve a release note.
- Add a row or checklist item.
- Improve `FREE_RESOURCE_INDEX.md`.
- Add or refine a pattern in `REPLY_DRAFTS.md`.

This is the default solution when the user cannot manually review public replies.

## Weekly Learning Loop

Once per week, review `ANSWER_LOG.md` for repeated high-score skips, draft-only
records, and answer-only wins. Convert repeated patterns into owned-surface
improvements before looking for more public comments.

Primary KPI:

- correct skips
- zero-risk published replies
- reusable owned-surface material

Secondary KPI:

- comment replies or follow-up questions
- GitHub release downloads after a directly relevant answer
- number of templates or FAQ entries improved
