# Auto Help Policy

This project can run without daily human review, but only if public account
actions are disabled.

## Allowed Without Human Review

- Find candidate questions.
- Classify risk: Low, Medium, High.
- Draft answer-first replies.
- Append records to `ANSWER_LOG.md`.
- Improve owned resources such as README, FAQ, release notes, templates, and
  checklists.
- Update `FREE_RESOURCE_INDEX.md` and `REPLY_DRAFTS.md`.
- Commit and push low-risk documentation updates.

## Not Allowed Without Human Review

- Posting Reddit comments.
- Posting Reddit submissions.
- Sending direct messages.
- Voting.
- Appealing moderation.
- Using any alternate account.
- Publishing paid CTAs in public communities.
- Linking Gumroad in subreddit replies.

## Notification Threshold

Notify only when at least one candidate is:

- Low risk.
- A direct match for an existing free resource or answer template.
- Useful even without a link.
- Outside banned or moderator-sensitive communities.

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

## Owned-Surface Help

If a repeated question is found but no safe public reply should be posted, help by
updating owned surfaces:

- Add a README FAQ.
- Improve a release note.
- Add a row or checklist item.
- Improve `FREE_RESOURCE_INDEX.md`.
- Add or refine a pattern in `REPLY_DRAFTS.md`.

This is the default solution when the user cannot manually review public replies.
