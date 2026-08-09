# DeepSeek Reply Review

Use this as the final review gate for answer-first reply drafts.

Roles:

Run two separate passes:

1. Strict, nitpicky ordinary Reddit user.
2. Moderator-adjacent rules and self-promotion risk reviewer.

Primary standard:

The reply must be genuinely useful before it is safe. A safe but generic reply
does not pass.

## Review Criteria

DeepSeek should check:

1. Does the reply directly answer the original question?
2. Does it give an ordinary user a concrete first action they can use
   immediately, without hidden prerequisites?
3. Is it adapted to the thread, not a reusable template pasted in?
4. Does it add a specific useful point not already covered by existing replies?
5. Is the direct answer and first action visible immediately, without an
   unnecessarily long tutorial?
6. If the link is removed, does the reply still have clear standalone value?
7. When applicable, does it say what success looks like or what evidence to
   collect next, and explain unfamiliar jargon briefly?
8. Is the link a minor supplement rather than the core of the reply?
9. Does the tone fit the subreddit: human, concise, non-corporate, and not like
   support-script text?
10. Does it contain or imply promotion, funneling, self-serving language,
   AI-template tone, paid/Gumroad/coupon/discount/Pro/upgrade/sales language, or
   likely self-promotion risk?

## Pass Gates

All must pass before a draft can be recommended:

- usefulness score >= 8
- subreddit tone score >= 7
- promotion risk score <= 3
- brevity score >= 7
- redundancy risk score <= 3
- link dependency is `None` or `Minor`
- link decision is `keep`, `remove`, or `no_link_present`
- if DeepSeek says `remove`, remove the link before presenting the draft
- no banned words or paid CTA language
- no public posting unless the user explicitly approves it or every strict
  automatic publish gate in `AUTO_HELP_POLICY.md` passes

If a draft fails, revise and review again. The default fix order is:

1. Improve concrete usefulness.
2. Adapt more tightly to the original question.
3. Remove points already covered by existing replies.
4. Put the direct answer and first action in the opening paragraph.
5. Remove self-reference and optional links.
6. Re-run the strict review.

Keep iterating until the draft passes. If the only passing version would be too
generic or not useful, do not recommend a reply.

The review script adds `draft_sha256` locally after the model response. The
model does not generate this value. Any draft edit invalidates the hash and
requires another review before `scripts/reddit_prepublish_gate.py` can pass.
It also binds normalized `existing_reply_ids` as `reviewed_reply_ids`. The
prepublish gate blocks when the final live comment IDs differ.

## Prompt

```text
You review Reddit replies in two separate passes.

First pass: strict, nitpicky ordinary Reddit user.
Second pass: moderator-adjacent rules and self-promotion risk reviewer.

Your most important question:
Is this reply genuinely useful to the original poster?

If the link is removed, the reply must still solve part of the problem.

Review the Reddit reply draft below.

Review in two passes.

Pass 1, ordinary Reddit user:
1. Does it directly answer the original question?
2. Does it give an ordinary user a concrete first action without hidden
   prerequisites?
3. Is it adapted to this exact thread instead of sounding like a generic template?
4. Does it add a specific useful point that the existing replies have not already covered?
5. Is the direct answer and first action visible immediately, without an unnecessarily long tutorial?
6. When applicable, does it state what success looks like or what evidence to collect next, and explain unfamiliar jargon briefly?
7. Does the tone fit the subreddit: human, concise, non-corporate, and not like support-script text?

Pass 2, moderator-adjacent risk:
8. Does the reply remain useful if every link is removed?
9. Are any links minor supplements rather than the core value?
10. Does it contain or imply promotion, funneling, self-serving language, AI-template tone, paid/Gumroad/coupon/discount/Pro/upgrade/sales language, or likely self-promotion risk?

Return strict JSON only:
{
  "usefulness_score": 0-10,
  "subreddit_tone_score": 0-10,
  "promotion_risk_score": 0-10,
  "brevity_score": 0-10,
  "redundancy_risk_score": 0-10,
  "recommendation": "Yes" | "No" | "Revise",
  "link_dependency": "None" | "Minor" | "High",
  "largest_usefulness_problem": "...",
  "largest_tone_problem": "...",
  "largest_promotion_or_rules_risk": "...",
  "sentence_to_delete_first": "...",
  "link_decision": "keep" | "remove" | "no_link_present",
  "revision_brief": "..."
}

Original thread:
[thread summary]

Existing replies:
[summary of existing replies, or None]

Existing reply IDs:
[visible Reddit comment IDs, or an empty list]

Draft reply:
[draft]
```
