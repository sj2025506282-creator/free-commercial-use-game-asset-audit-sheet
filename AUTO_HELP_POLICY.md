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
- Compare the draft with the existing replies. Publish only when it fills a
  specific gap that a shorter existing answer has not already solved.
- Put the direct answer and first action in the opening paragraph. Default to a
  compact diagnosis plus two to five steps; add a longer tutorial only when the
  thread's actual complexity requires it.
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
- Draft adds a concrete point not already covered by existing replies.
- Direct answer and first action are visible immediately; no unnecessary
  tutorial remains.
- The run has not already published a stronger candidate today, unless the user
  explicitly asked to continue.
- DeepSeek strict review passes after any needed revisions.
- Final usefulness score >= 8.
- Final subreddit tone score >= 7.
- Final promotion risk score <= 3.
- Final brevity score >= 7.
- Final redundancy risk score <= 3.
- Final link dependency is `None` or `Minor`.
- No paid, Gumroad, coupon, discount, Pro, upgrade, or sales language.
- At most one free GitHub link is included, and only if the link escalation gate
  below passes and DeepSeek says keep.
- If DeepSeek says remove the link, publish the no-link version.
- `scripts/reddit_prepublish_gate.py` returns `passed: true` for the exact final
  draft after the last live thread/rules re-read.
- The final draft SHA-256 matches the hash added locally by
  `scripts/deepseek_reply_review.py`; any edit requires a new DeepSeek review.

If any gate fails, do not publish. Revise and re-review, or mark the candidate
`Skip` / `Draft only`.

The deterministic prepublish gate checks machine-verifiable conditions such as
candidate scores, daily public-comment count, stopped communities, banned
language, link count/domain, DeepSeek thresholds, and final-draft identity.
Semantic claims such as standalone usefulness and the concrete missing gap must
still be verified from the live thread and included truthfully in its input.

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

- Thread fit: the question is inside the approved help scope and enough concrete
  context exists to answer it precisely. Score 2 for a direct strategic match
  such as asset licensing, font provenance, jam shipping, UI SFX, or
  open-source tooling; score 1 for a concrete adjacent game-development
  question; score 0 for an off-scope, context-empty, showcase, commercial, or
  legal-conclusion thread.
- Helpfulness: score 2 when a standalone answer gives concrete steps or a
  diagnostic path; 1 when it can only give partial direction or needs missing
  project details; 0 when it would be generic, speculative, or link-dependent.
- Risk: score 2 when community status/rules are clear and the thread is an
  ordinary help request; 1 when rules, version/plugin facts, commercial context,
  or legal adjacency remain uncertain; 0 for a stopped/banned community,
  legal-conclusion request, dispute, argument, or moderator-sensitive surface.
- Link fit: score 2 when no link is needed or one indexed free GitHub resource
  is a direct match; 1 when a resource is merely adjacent and should normally be
  omitted; 0 when the reply's value depends on a link or links are unwelcome.
- Originality: score 2 when the answer uses the thread's actual constraints,
  examples, or code path; 1 when it is adapted but still broadly reusable; 0
  when it is copied, templated, or not grounded in the post.

Historical logs and automation prompts may label Thread fit as `Relevance`.
Interpret that legacy label using the rubric above; do not rewrite old rows.

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

Include a compact summary of the current thread's existing replies in the
`existing_replies` input. For unattended publishing, do not omit this field.

DeepSeek reviews as a strict, nitpicky ordinary Reddit user with a
moderator-adjacent view.

Pass gates:

- usefulness score >= 8
- subreddit tone score >= 7
- promotion risk score <= 3
- brevity score >= 7
- redundancy risk score <= 3
- link dependency is `None` or `Minor`
- recommendation is `Yes` or a clearly fixable `Revise`
- if `link_decision` is `remove`, remove the link before presenting the draft

If a draft does not pass, revise it and run DeepSeek review again. Use the
reviewer's concrete criticism as the edit brief:

- make the answer more specific to the original post
- remove points already covered by current replies
- move the direct answer and first action into the opening paragraph
- shorten tutorial detail that the OP did not ask for
- remove or soften self-references
- remove the resource link when it is not essential
- add concrete steps, examples, or decision criteria
- keep banned paid/Gumroad/coupon/upgrade language out

Continue revising until the draft passes. If it passes all strict publish gates,
publish it and log the final posted version. If a useful, low-risk draft cannot
be made without becoming generic, promotional, legally conclusive, or off-topic,
mark the candidate `Skip` or `Draft only` and do not publish.

If DeepSeek is unavailable, apply the same rubric manually for drafting and
logging, mention that the external review was not run, and do not auto-publish.

## Output Contract

Every candidate record or notification should include:

- Community
- Thread/question
- URL
- Decision: `Answer only`, `Answer + free link`, `Skip`, or `Draft only`
- Score: Thread fit / Helpfulness / Risk / Link fit / Originality / Total
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

Use the `reddit-answer-first-reviewer` skill for this work. Weekly review is
read-only on public communities even when a daily candidate would otherwise
pass.

For every posted comment, attempt one outcome readback after 48-72 hours. Record
visible score, direct replies, OP reply or follow-up, and moderation state in the
existing Result / Follow-Up cell. Treat unavailable data as `Unknown`; do not
invent zeros.

Primary KPI:

- correct skips
- zero-risk published replies
- reusable owned-surface material

Secondary KPI:

- comment replies or follow-up questions
- OP reply or evidence that the answer was adopted
- moderation survival after 48-72 hours
- GitHub release downloads after a directly relevant answer
- number of templates or FAQ entries improved

## SOP Change Control

The weekly reviewer may automatically clarify contradictions, update compatible
tool/model names, improve logs and templates, and consolidate repeated
owned-surface patterns.

Explicit user approval is required before lowering publish thresholds,
increasing public volume, reopening a stopped community, weakening banned-word
rules, or expanding public links/actions. When rules conflict, preserve the more
conservative behavior.
